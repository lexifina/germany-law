---
ecli: "ECLI:DE:BPatG:2023:170523U5Ni48.20EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 48/20"
decided: "2023-05-17"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=14&nr=43723&anz=529&pos=210&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-05-17_5_Ni_48_20_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 48/20 vom 2023-05-17

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      Verkündet am
                                                       17. Mai 2023
5 Ni 48/20 (EP)                                             …

(Aktenzeichen)



                     In der Patentnichtigkeitssache
…




ECLI:DE:BPatG:2023:170523U5Ni48.20EP.0

                                       -2-




                 betreffend das europäische Patent 2 944 065
                             (DE 60 2013 051 102)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 17. Mai 2023 durch den Richter Heimen als
Vorsitzenden sowie die Richter Schödel, Dr.-Ing. Ball, Dipl.-Phys. Univ. Bieringer
und Dipl.-Phys. Christoph


für Recht erkannt:


      I.     Die Klage wird abgewiesen.


      II.    Die Klägerin trägt die Kosten des Verfahrens.


      III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des zu
             vollstreckenden Betrages vorläufig vollstreckbar.




                                Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 2 944 065 (Streitpatent), das
unter Inanspruchnahme der Priorität der US 2013 13739178 vom 11. Januar 2013
am 2. Dezember 2013 angemeldet worden ist. Die Erteilung des europäischen
Patents ist am 20. Februar 2019 veröffentlicht worden. Das in englischer Sprache
gefasste Streitpatent trägt die Bezeichnung “RULE SWAPPING IN A PACKET
NETWORK“, ins Deutsche übersetzt “AUSTAUSCH VON REGELN IN EINEM
PAKETNETZ”. Es ist in Kraft und umfasst in der geltenden Fassung insgesamt 15
Patentansprüche mit dem Verfahrensanspruch 1 und auf diesen unmittelbar

                                           -3-



zurückbezogenen Unteransprüchen 2 bis 13, dem nebengeordneten Vorrichtungsanspruch 14 und dem nebengeordneten Anspruch 15 auf ein computerlesbares
(Speicher-)Medium. Mit ihrer Klage begehrt die Klägerin die vollständige
Nichtigerklärung des Streitpatents.


Die geltenden Patentansprüche 1, 14 und 15 haben mit der Gliederung des Senats
folgenden Wortlaut:


 Merkmal                Streitpatent in                 Übersetzung laut Streitpatent
                      Verfahrenssprache
M1           A method comprising: at a              Verfahren, aufweisend: an einer
             network protection device (100):       Netzwerkschutzvorrichtung
                                                    (100):
M 1.1        receiving a first rule set;            ein Empfangen einer ersten
                                                    Regelgruppe;
M 1.2        receiving a second rule set;           ein Empfangen einer zweiten
                                                    Regelgruppe;
M 1.3        preprocessing the first rule set       ein Vorverarbeiten der ersten
             and the second rule set;               Regelgruppe und der zweiten
                                                    Regelgruppe;
M 1.4        configuring a plurality of             ein Konfigurieren einer Mehrzahl von
             processors (300, 302, 304) of          Prozessoren (300, 302, 304) der
             the network protection device to       Netzwerkschutzvorrichtung zum
             process packets in accordance          Verarbeiten von Paketen gemäß der
             with the first rule set;               ersten Regelgruppe;
M 1.5        receiving packets;                     ein Empfangen von Paketen;

M 1.6        processing, by at least two of         ein Verarbeiten eines ersten Teils der
             the plurality of processors, a first   Pakete gemäß der ersten
             portion of the packets in              Regelgruppe durch mindestens zwei
             accordance with the first rule         aus der Mehrzahl von Prozessoren;
             set;
M 1.7        signaling each of the at least         ein Signalisieren an jeden der
             two of the plurality of processors     mindestens zwei aus der Mehrzahl
             to process packets in                  von Prozessoren, Pakete gemäß der
                                                    zweiten Regelgruppe zu verarbeiten;

                                      -4-



          accordance with the second rule
          set;

M 1.8     responsive to the signaling to        in Reaktion auf die Signalisierung,
          process packets in accordance         Pakete gemäß der zweiten
          with the second rule set:             Regelgruppe zu verarbeiten:
M 1.8.1   ceasing, by each of the at least      ein Beenden des Verarbeitens der
          two of the plurality of               Pakete durch jeden der mindestens
          processors, processing of the         zwei aus der Mehrzahl von
          packets;                              Prozessoren;
M 1.8.2   caching, by each of the at least      ein Zwischenspeichern von
          two of the plurality of               unverarbeiteten Paketen durch jeden
          processors, unprocessed               der mindestens zwei aus der Mehrzahl
          packets;                              von Prozessoren;
M 1.8.3   reconfiguring each of the at          ein Neukonfigurieren von jedem der
          least two of the plurality of         mindestens zwei aus der Mehrzahl
          processors to process packets         von Prozessoren, Pakete gemäß der
          in accordance with the second         zweiten Regelgruppe zu verarbeiten;
          rule set; and                         und
M 1.8.4   signaling, by each of the at least    ein Signalisieren des Abschlusses der
          two of the plurality of               Neukonfiguration zum Verarbeiten von
          processors, completion of             Paketen gemäß der zweiten
          reconfiguration to process            Regelgruppe durch jeden der
          packets in accordance with the        mindestens zwei aus der Mehrzahl
          second rule set; and                  von Prozessoren; und
M 1.9     responsive to receiving signaling     in Reaktion auf ein Empfangen der
          that each of the at least two of      Signalisierung, das jeder der
          the plurality of processors has       mindestens zwei aus der Mehrzahl
          completed reconfiguration to          von Prozessoren die Neukonfiguration
          process packets in accordance         zum Verarbeiten von Paketen gemäß
          with the second rule set,             der zweiten Regelgruppe
          processing, by the at least two       abgeschlossen hat, ein Verarbeiten
          of the plurality of processors, the   der zwischengespeicherten
          cached unprocessed packets.           unverarbeiteten Pakete durch die
                                                mindestens zwei aus der Mehrzahl
                                                von Prozessoren.


M 14.1    A network protection device           Netzwerkschutzvorrichtung
          apparatus (100), comprising:          (100), aufweisend:

                                        -5-



 M 14.1.1    a plurality of processors (300,     eine Mehrzahl von Prozessoren
             302, 304); and                      (300, 302, 304); und
 M 14.1.2    a memory storing instructions       einen Arbeitsspeicher, der
             that when executed by at least      Anweisungen speichert, die, wenn sie
             one processor of the plurality of   von mindestens einem Prozessor aus
             processors cause the apparatus      der Mehrzahl von Prozessoren
             to perform the method of any of     ausgeführt werden, die Vorrichtung
             claims 1-13.                        veranlassen, das Verfahren nach
                                                 einem der Ansprüche 1 bis 13
                                                 auszuführen.


 M 15.1       One or more non-transitory         Eine oder mehrere nicht flüchtige, von
              computer-readable media having     einem Computer lesbare Medien mit
              instructions stored thereon,       darauf gespeicherten Anweisungen,

 M 15.2       that when executed by one or       die, wenn sie von einem oder
              more computers,                    mehreren Computern ausgeführt
                                                 werden,
 M 15.3       cause the one or more           den einen oder die mehreren
              computers to perform the method Computer veranlassen, das Verfahren
              of any of claims 1-13.          nach einem der Ansprüche 1 bis 13
                                              auszuführen.



(Das offensichtlich fehlerhafte Bezugszeichen 392 in Merkmal M14.1.1 wurde
korrigiert zu 302.)


Wegen des Wortlauts der abhängigen Unteransprüche 2 bis 13 wird auf das
Streitpatent verwiesen.


Die Klägerin macht die Nichtigkeitsgründe der unzulässigen Erweiterung bezüglich
des Anspruchs 1 (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 c) EPÜ) sowie
der mangelnden Neuheit und der mangelnden erfinderischen Tätigkeit (Art. II § 6
Abs. 1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 a) i. V. m. Art. 54, 56 EPÜ) hinsichtlich der
unabhängigen Ansprüche 1, 14 und 15 geltend.

                                       -6-



Sie stützt ihre Klage u. a. auf folgende Dokumente:


     NK6                  EP 1 313 290 A1
     NK7                  WO 2005/046145 A1
     NK8                  US 2011/0055916 A1
     NK9                  US 2006/0248580 A1
     NK10                 US 2006/0195896 A1
     NK12                 Written Opinion ISA zur PCT/US2013/072566
     NK13                 Katamaya, M. et al.; A 10 Gb/s Firewall System for
                          Network Security in Photonic Era. INVITED
                          PAPER Joint Special Section on Recent Progress
                          in Optoelectronics and Communications. In: IEICE
                          TRANS. COMMUN., VOL. E88–B, NO.5, PP. 1914
                          – 1920, MAY 2005.
     NK14                 US 2006/0048142 A1
     NK15                 Golnabi, K. et al.; Analysis of Firewall Policy Rules
                          Using Data Mining Techniques. In: 10th IEEE
                          Network Operations and Systems Management
                          (NOMS 2006), PP. 305 – 315, April 2006.
     NK16                 US 2002/0174255A1
     NK17                 US 2004/0015905 A1
     NK18                 Bhave, M.P.; Computer Programming – I, Dorling
                          Kindersley (India) Pvt. Ltd., S.112, 2010
     NK19                 Datenblatt: DAPDNA-2 Dynamically Reconfigurable
                          Processor, FUJITSU MICROELECTRONICS LIMITED,
                          June 2005


Die Klägerin ist insbesondere der Auffassung, dass die Gegenstände der
angefochtenen Ansprüche vor allem bei Berücksichtigung der Druckschrift NK13
jeweils mangels Neuheit nicht patentfähig seien und auch gegenüber der NK14
jeweils kombiniert mit dem Fachwissen des Durchschnittsfachmanns, der NK8, der

                                        -7-



NK9, der NK10, der NK15, der NK16 bzw. der NK17 nicht auf einer erfinderischen
Tätigkeit beruhten.




Die Klägerin beantragt,


      das europäische Patent EP 2 944 065 mit Wirkung für das Hoheitsgebiet der
      Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,


      die Klage abzuweisen.




Die Beklagte verteidigt das Streitpatent in der erteilten Fassung und tritt der Klage
in allen Punkten entgegen. Die Druckschrift NK13 stehe der Neuheit des erteilten
Patents nicht entgegen. Sie ist der Auffassung, dass auch die Druckschrift NK14
kombiniert mit dem Fachwissen des Durchschnittsfachmanns nicht gegen die
erfinderische Tätigkeit des Streitpatents spreche.


Wegen der weiteren Einzelheiten des Vorbringens der Parteien wird auf die
zwischen den Parteien gewechselten Schriftsätze nebst Anlagen und den weiteren
Inhalt der Akte Bezug genommen.

                                         -8-




                               Entscheidungsgründe


                                          A.


Die zulässige Klage ist nicht begründet. Der Gegenstand des Patentanspruchs 1
geht nicht über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung
gemäß Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ
hinaus und auch der geltend gemachte Nichtigkeitsgrund der mangelnden
Patentfähigkeit der Patentansprüche 1 bis 15 gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG
i. V. m. Art. 138 Abs. 1 Buchst. a), 52, 54, 56 EPÜ liegt nicht vor.



                      I.     Zum Gegenstand des Streitpatents


1.     Das Streitpatent betrifft Netzwerkschutzvorrichtungen wie beispielsweise
Firewalls, Gateways, Router und Switche, die Regeln zur Überwachung bzw.
Kontrolle des an den Netzwerkgrenzen von paketvermittelnden Netzwerken einund ausgehenden Paketdatenverkehrs umfassten, wobei die Netzwerkschutzvorrichtung beim Detektieren von Übereinstimmungen zwischen Paketdatenverkehr
und Regeln entsprechende Aktionen durchführe und u. a. den Zugang zu dem zu
schützenden Netzwerk zulasse oder verwehre (Streitpatent, Absatz [0001]). Die
Regeln seien dabei in Regelgruppen („grouped into rule sets“) organisiert, welche
entsprechende     Netzwerkrichtlinien   bzw.    Netzwerkpolitik   („network   policy“)
verkörperten (Streitpatent, ebd.).


Mit stetig ansteigender Netzwerkkomplexität und mit dem Wunsch der
Administratoren nach einer immer feingranulareren Netzwerkverwaltung wachse
auch die Anzahl der Regeln in den Regelgruppen, so dass eine Netzwerkschutzvorrichtung zum Umschalten zwischen Regelgruppen eine gewisse Zeit
benötige, was zu Hindernissen bei einer effizienten Implementierung führe

                                           -9-



(Streitpatent, Absätze [0001] - [0002]). Netzwerkschutzvorrichtungen könnten
beispielsweise während eines Umschaltens zwischen zwei Regelgruppen keinen
Netzwerkverkehr bearbeiten, da ihre begrenzten Ressourcen überwiegend für den
Umschaltvorgang gebraucht würden, oder sie müssten aus dem gleichen Grund
den eingehenden Netzwerkverkehr noch anhand der alten Regelgruppe beurteilen,
was gerade bei Netzwerkangriffen nachteilig wäre (Streitpatent, Absatz [0002]).


In diesem technischen Kontext der Netzwerksicherheit bestehe daher ein Bedarf
bzw. stelle sich das Streitpatent implizit die Aufgabe, den Umschaltvorgang
zwischen     Regelgruppen     in   Netzwerkschutzvorrichtungen           zu    verbessern
(Streitpatent, Absätze [0005] - [0008]).


Als Lösung nennt das Streitpatent zum einen das „fast rule swapping“ umfassend
eine Vorverarbeitung von Regelgruppen vor ihrer Implementierung in die
Netzwerkschutzvorrichtung, um bedingt durch deren Vorverarbeitung das schnelle
Umschalten auf eine neue Regelgruppe ohne Zeitverlust zu ermöglichen
(Streitpatent, Absätze [0022] - [0023]). Zum anderen wird eine Netzwerkschutzvorrichtung mit mehreren parallel arbeitenden Prozessoren umfassend einen
synchronisierten Regelgruppenwechsel vorgeschlagen, um die Verarbeitungskapazität    der   Netzwerkschutzvorrichtung        zu    erhöhen      und    dabei    eine
Gleichbehandlung der Pakete unabhängig vom verarbeitenden Prozessor zu
gewährleisten (Streitpatent, Absätze [0025] - [0026], [0033]).


2.     Als zuständigen Fachmann sieht der Senat einen Ingenieur der Elektrotechnik
bzw.        Nachrichtentechnik/Informationstechnik          mit        abgeschlossenem
Universitätsstudium und mit mehrjähriger Berufserfahrung in der Entwicklung
vernetzter, paketvermittelnder Datenübertragungs- und Kommunikationssysteme,
wobei    dieser    insbesondere    über    detaillierte   Kenntnisse    hinsichtlich   der
einschlägigen Netzwerkgeräte, Netzwerkprotokolle sowie Netzwerk-Sicherheit,
z. B. Firewalls, verfügt.

                                          - 10 -



3.   Dieser Fachmann versteht die Lehre des Streitpatents und einige der in den
angegriffenen Ansprüchen verwendeten Begriffe vor dessen technischem
Hintergrund wie folgt:


3.1 Zum Patentanspruch 1

Der Patentanspruch 1 beansprucht ein Verfahren, welches als räumlich-körperliche
Komponente eine Netzwerkschutzvorrichtung („network protection device 100“)
aufweist (Merkmal M1), wobei die Netzwerkschutzvorrichtung wiederum gemäß den
Merkmalen M1.4, M1.6, M1.7, M1.8.1, M1.8.2, M1.8.3, M1.8.4 und M1.9 eine
Vielzahl, d. h. mindestens zwei, Prozessoren („processors 300, 302, and 304“)
umfasst, wobei gemäß Merkmalen M1.8.2 und M1.9 zumindest noch ein Speicher
(„cache“) zum Zwischenspeichern von Datenpaketen durch die Prozessoren
vorgesehen sein muss. Der Wortlaut des Patentanspruchs 1 lässt hierbei offen, ob
die multiplen Prozessoren parallel oder seriell (also in einer Reihenschaltung)
angeordnet sind und ob die Prozessoren jeweils einen eigenen Cache oder einen
gemeinsamen Cache besitzen. Das Streitpatent zeigt in dem Ausführungsbeispiel
der Figuren 3a bis 3f i. V. m. Absätzen [0026] ff. mehrere parallel angeordnete
Prozessoren 300, 302, 304 mit jeweils einem eigenem Cache 306, 308, 310.


Gemäß Streitpatent kann es sich bei der Netzwerkschutzvorrichtung um eine
Firewall, ein Gateway, einen Router oder einen Switch (Streitpatent, Absätze [0001],
[0017]) oder auch ganz allgemein um einen Computer bzw. einen Server handeln
(Streitpatent, Absätze [0035], [0037]).


Die beanspruchten Verfahrensmerkmale bzw. Verfahrensschritte M1.1 bis M1.9
können laut Ausführungsbeispiel (Streitpatent, Absätze [0035] - [0037]) in einem
einzigen Gerät („located in a single computing device“) oder verteilt über mehrere
separate Geräte durchgeführt werden, wobei jedoch jedes einzelne Gerät die
anspruchsgemäßen mindestens zwei Prozessoren aufweist.

                                       - 11 -



Die Verfahrensschritte M1.1 und M1.2 betreffen das Empfangen einer ersten und
einer zweiten Regelgruppe. Gemäß Streitpatent, Absatz [0026] kann eine
Regelgruppe („rule set“) aus einer Vielzahl – insbesondere aus Hunderttausenden
oder Millionen (Streitpatent, Absatz [0025], „large number of rules“; Absatz [0026],
„rule sets may include hundreds of thousands or millions of individual rules“) – von
individuellen Regeln bestehen. In den Ausführungsbeispielen (Streitpatent, Absätze
[0010], [0011], [0019] und [0027]) werden die Regelgruppen dahingehend
konkretisiert, dass Regelgruppen eine mit Paketkriterien verbundene Aktion sowie
ggf. weitere Funktionen umfassen, wobei die Regelgruppen beispielsweise eine
Menge an Netzwerkadressen spezifizieren, für welche die entsprechenden Pakete
akzeptiert oder abgelehnt („accept or deny“), gelöscht („drop the packets“),
protokolliert („log the packets“) oder weitergeleitet („forward the packets“) werden
sollen.


Der Anspruchswortlaut lässt offen, von wem die Netzwerkschutzvorrichtung die
Regelgruppen empfängt. Das Streitpatent offenbart in den Absätzen [0017], [0018]
und [0022] i. V. m. Figur 1, Bezugszeichen 112 beispielsweise lediglich ein
Management-Interface (MI). Der Wortlaut des Patentanspruchs 1 schließt insofern
nicht aus, dass die Regelgruppen von einer anderen Netzwerkschutzvorrichtung
empfangen werden können.


Merkmal M1.3 beansprucht das Vorverarbeiten („preprocessing“) der ersten und der
zweiten Regelgruppe, ohne jedoch auf Details hinsichtlich der Vorverarbeitung
näher einzugehen, so dass lediglich eine ganz allgemeine Vorverarbeitung
beansprucht wird. Das Streitpatent nennt als Ausgestaltungen explizit in Absatz
[0007] eine Optimierung der Regelgruppe und in den Absätzen [0020] bis [0021] ein
Zusammenfassen, Trennen und Umsortieren der Regeln („merging“, „separating“,
„reordering“,   vgl.   auch   Unteransprüche      10     bis   12),   was   ein   sehr
ressourcenintensiver    und   die   Performance    der     Netzwerkschutzvorrichtung
degradierender Prozess sei. Der Fachmann versteht jedoch – in der Breite des
Anspruchs – unter einer Vorverarbeitung ebenso bereits ein Entpacken, ein

                                       - 12 -



Dekomprimieren und/oder ein Entschlüsseln einer empfangenen Regelgruppe bzw.
ein Kompilieren und/oder Adaptieren der Regelgruppe auf einen von den
Prozessoren benötigtes (z. B. ausführbares) Format. Aus fachmännischer Sicht soll
durch das Vorverarbeiten erreicht werden, dass der Prozessor die Regeln möglichst
direkt anwenden kann.


Merkmal M1.4 betrifft ein Konfigurieren einer Vielzahl von, d. h. mindestens zwei,
Prozessoren in der Netzwerkschutzvorrichtung, um Pakete gemäß der ersten
Regelgruppe zu verarbeiten. Wie oben bereits zum Merkmal M1 ausgeführt, muss
die verwendete Netzwerkschutzvorrichtung dazu gegenständlich mindestens diese
zwei Prozessoren aufweisen.


Die Merkmale M1.5 und M1.6 betreffen ein Empfangen und Verarbeiten von
Paketen unter Verwendung der ersten Regelgruppe, wobei die Regeln der ersten
Regelgruppe auf einen ersten Anteil des empfangenen Datenverkehrs angewendet
werden.


Merkmal M1.7 beansprucht ein Signalisieren an jeden der o. g. Prozessoren in der
Netzwerkschutzvorrichtung, dass ein Regelgruppenwechsel erfolgen soll, d. h.,
zukünftig die zweite Regelgruppe zu verwenden ist. Der Auslöser bzw. der Ursprung
der Signalisierung, d. h., ob eine interne oder externe Signalisierung vorliegt, bzw.
deren Art, Typ, oder Format werden im Anspruchswortlaut nicht spezifiziert. Gemäß
Streitpatent, Absätze [0033] und [0034] („For example, network protection device
100 may receive a message invoking policy 132’s rule set or one or more network
conditions indicating a network attack may be detected.“), kann der Auslöser eine
detektierte Netzwerkattacke sein, wobei die Netzwerkschutzvorrichtung eine
(externe) Nachricht zum Regelgruppenwechsel empfängt.


Darüber hinaus zeigt das Streitpatent in den Figuren 3a bis 3f i. V. m. Absatz [0030]
beispielsweise nach einem bestimmten Regelgruppenwechsel eine (interne)
Signalisierung   an   die   Prozessoren     ausgehend     von   einem    (zentralen)

                                       - 13 -



Verwaltungsrechner („administrative processor 312“) mittels Steuerpaket („control
packet“) auf dem Datenbus 120. Gemäß Streitpatent, Absatz [0008] („Synchronizing
the processors may include signaling the processors […]“), ist diese Signalisierung
der erste Teil einer (im Streitpatent als solche bezeichneten) „Synchronisierung“ der
multiplen Prozessoren. Das Streitpatent beschreibt diesen Regelgruppenwechsel
bzw. Synchronisierungsablauf gemäß Merkmalsgruppe M1.8 detailliert in den
Figuren 3a bis 3f i. V. m. den Absätzen [0026] bis [0033]. Insbesondere soll gemäß
Absatz [0033] durch diese Synchronisierung ein einheitliches Verarbeiten der
Pakete über die Vielzahl an Prozessoren hinweg gewährleistet werden („…packets
processed by network protection device 100 at any given time may receive uniform
treatment irrespective of the particular processor which handles them.“). Die
Synchronisierung gemäß der Merkmalsgruppe M1.8 umfasst die folgenden
weiteren Schritte, welche in einem kausalen Zusammenhang („responsive to“ – „in
Reaktion“) nach der Signalisierung zum Regelgruppenwechsel gemäß M1.7
durchgeführt werden müssen:


   · M1.8.1: Beenden der aktuellen Paketverarbeitung durch die betroffenen
      mindestens zwei Prozessoren („ceasing“),
   · M1.8.2: Zwischenspeichern von neu ankommenden Paketen durch die
      betroffenen Prozessoren in einem Cache („caching“), wobei die gerade in der
      Verarbeitung befindlichen Pakete gemäß Absatz [0031] entweder noch
      abgefertigt werden können oder ebenfalls im Cache abzulegen sind,
   · M1.8.3: Rekonfigurieren bzw. Umschalten der Prozessoren auf die zweite
      Regelgruppe („reconfiguring“) sowie
   · M1.8.4       Signalisieren    eines        erfolgreichen   Abschließens     des
      Regelgruppenwechsels durch jeden betroffenen Prozessor („signaling …
      completion“).


Erst bei Erhalt einer Signalisierung für ein erfolgreiches Rekonfigurieren aller
betroffenen Prozessoren auf die zweite Regelgruppe sollen die Prozessoren gemäß
Merkmal M1.9 wieder (zeitgleich) die Arbeit aufnehmen und anschließend Pakete

                                        - 14 -



mittels der zweiten Regelgruppe verarbeiten, wozu zunächst auch die vorab im
Cache abgelegten Pakete während des Regelgruppenwechsels zählen sollen.


Gemäß den Merkmalen M1.8.4 und M1.9 erfolgt das Signalisieren grundsätzlich wie
das oben beschriebene Signalisieren gemäß Merkmal M1.7, indem Nachrichten
zwischen den Prozessoren und dem zentralen Verwaltungsrechner „administrative
processor 312“ mittels Datenbus 120 ausgetauscht werden. Da der Gegenstand
des Patentanspruchs 1 nicht auf das Ausführungsbeispiel beschränkt ist, kann der
Fachmann anstelle des im Streitpatent explizit beschriebenen Datenbusses auch
einen direkten Datenaustausch zwischen den Prozessoren – exemplarisch auch
entsprechende Kabel- oder Leitungsverbindungen o. ä. – vorsehen.


Soweit   zwischen     den    Parteien    das     fachmännische    Verständnis    des
Synchronisierens im Kontext der offenbarten Lehre des Streitpatents streitig ist, ist
der Senat der Ansicht, dass die „Synchronisierung“ der Prozessoren sowohl zu
Beginn als auch am Ende jeweils die entsprechende anspruchsgemäße
Signalisierung erfordert, wobei die Art und Weise der Signalisierung auch heterogen
sein oder auch auf unterschiedlichen Wegen erfolgen kann. Anspruchsgemäß muss
die Signalisierung jedoch einerseits gemäß M1.7 sowie M1.9 an alle betroffenen
Prozessoren gerichtet sein (und muss folglich auch von diesen an einem Eingang
empfangen werden) und andererseits gemäß M1.8.4 von jedem einzelnen der
betroffenen Prozessoren ausgehen (und muss folglich auch von jedem einzelnen
an einem Ausgang ausgegeben werden). Einer reinen Zeitsteuerung des
Synchronisierungsprozesses bzw. des Regelgruppenwechsels – beispielsweise
anhand eines Abzählens von Taktzyklen zum Bestimmen einer vorab festgelegten
Umschaltdauer eines Prozessors nach dem Empfangen eines Triggers zum Starten
des Regelgruppenwechsels – fehlt die beanspruchte Signalisierung bzw. das
Anzeigen des erfolgreichen Abschlusses der Rekonfiguration durch den Prozessor
und fällt nach Überzeugung des Senats nicht unter den Wortlaut des
Patentanspruchs 1. Darüber hinaus mangelt es einem Taktsignal auch bereits schon
daran, dass es von einem zentralen Taktgenerator oder Quarz bereitgestellt wird

                                         - 15 -



und nicht – wie in M1.8.4 gefordert – von jedem einzelnen der betroffenen
Prozessoren ausgeht.


Hinsichtlich der Reihenfolge der beanspruchten Verfahrensschritte gilt nach der
Überzeugung des Senats Folgendes:


Grundsätzlich gibt die semantische Reihenfolge der Verfahrensschritte im Text
eines Verfahrensanspruchs nicht zugleich auch die funktionelle Reihenfolge für die
Durchführung der einzelnen Verfahrensschritte vor (vgl. BGH, Urteil vom 9. Mai
2017, X ZR 97/15, Rd. 12 - Bremsbeläge), sofern aus dem Patentanspruch als
Ganzes sowie dem technischen Zusammenhang des Streitpatents nichts anderes
hervorgeht. Die Reihenfolge für die Verfahrensschritte der Merkmalgruppe M1.8
zusammen mit Merkmal M1.9 ist jedoch in Reaktion auf das Merkmal M1.7
festgelegt, denn die Verfahrensschritte M1.8 bis M1.9 stehen in kausalem
Zusammenhang mit der Signalisierung gemäß Merkmal M1.7 und bilden eine
logische Abfolge infolge der Signalisierung, die nicht geändert werden kann, ohne
die Lehre des Streitpatents zu verlassen.


Hinsichtlich der Merkmale M1.1 bis M1.7 entnimmt der Fachmann jedoch dem
Streitpatent, Absatz [0038] („one of ordinary skill in the art will appreciate that the
steps illustrated in the illustrative figures may be performed in other than the recited
order“), dass die Abfolge der Verfahrensschritte auch flexibel gehandhabt werden
kann. Darüber hinaus wird eine veränderte technische Situation mit einem
sequentiellen Empfangen und Vorverarbeiten von neuen Regelgruppen – während
des laufenden Betriebs – aufgrund der Verkehrsflüsse im Netzwerk beschrieben,
wobei das Empfangen und Vorverarbeiten der neuen Regelgruppe zeitlich erst so
viel später erfolgt, dass bereits Pakete anhand der vorherigen Regelgruppe
verarbeitet werden (Streitpatent, Absatz [0021], „For example, network protection
device 100 may preprocess policy 130’s rule set and then implement the
preprocessed rule set with respect to network traffic flowing between networks 104
and 106. Later, it may be desired to reconfigure network protection device 100 to

                                       - 16 -



implement policy 132’s rule set with respect to network traffic flowing between
networks 104 and 106. Accordingly, policy 132's rule set may be preprocessed and
network protection device 100 may be reconfigured to implement the preprocessed
rule set with respect to network traffic flowing between networks 104 and 106.“).


Aus diesem technischen Kontext und der Gesamtschau des Streitpatents entnimmt
der Fachmann daher, dass das Empfangen der zweiten Regelgruppe gemäß
Merkmal M1.2 sowie die Vorverarbeitung der zweiten Regelgruppe gemäß Merkmal
M1.3 (zweite Hälfte) auch erst nach dem Verarbeiten der empfangenen Pakete mit
der ersten Regelgruppe gemäß Merkmal M1.6, aber noch vor dem Signalisieren
des Regelgruppenwechsels zur zweiten Regelgruppe gemäß Merkmal M1.7
erfolgen kann.


Der Gegenstand des Patentanspruchs 1 ist somit nicht darauf beschränkt, dass
zunächst die erste und die zweite Regelgruppe empfangen sein müssen (Merkmale
M1.1 und M1.2), bevor mit der Vorverarbeitung der ersten Regelgruppe (Merkmal
M1.3) begonnen wird. Vielmehr kommt es für das „fast rule swapping“ darauf an,
dass die zweite Regelgruppe zum Zeitpunkt des Regelgruppenwechsels bereits
empfangen und vorverarbeitet sein muss, um ein effizientes, schnelles Umschalten
der Regelgruppen i. S. d. Streitpatents zu ermöglichen.




3.2 Zum nebengeordneten Patentanspruch 14
Der   nebengeordnete      Patentanspruch        14   betrifft   eine   entsprechende
Netzwerkschutzvorrichtung („network protection device apparatus“) mit multiplen
Prozessoren und einem Programmspeicher zur Durchführung des Verfahrens, u. a.
gemäß Patentanspruch 1. Der Fachmann versteht die Merkmale des nebengeordneten Patentanspruchs 14 daher wie die entsprechenden Merkmale des
Patentanspruchs 1.

                                           - 17 -



3.3 Zum nebengeordneten Patentanspruch 15
Der nebengeordnete Patentanspruch 15 betrifft ein oder mehrere nicht flüchtige,
von einem Computer lesbare Medien mit darauf gespeicherten Anweisungen („nontransitory computer-readable media having instructions stored thereon“) zur
Durchführung des Verfahrens, u. a. gemäß Patentanspruch 1, durch einen oder
mehrere Computer. Der Fachmann versteht die Merkmale des nebengeordneten
Patentanspruchs        15    daher   wie     die    entsprechenden   Merkmale      des
Patentanspruchs 1.




                 II.        Zu den vorgebrachten Nichtigkeitsgründen


Das Streitpatent ist gegenüber den Ursprungsunterlagen nicht unzulässig erweitert
(Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 c) EPÜ) und es erweist sich auch
als patentfähig (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a),
Art. 52, 54 EPÜ).




1.   Zum Nichtigkeitsgrund der unzulässigen Erweiterung:
Der Gegenstand des Patentanspruchs 1 geht nicht über den Inhalt der
Patentanmeldung in ihrer bei der für die Einreichung der Anmeldung zuständigen
Behörde ursprünglich eingereichten Fassung hinaus. Der Fachmann entnimmt den
Gegenstand des genannten Anspruchs den ursprünglichen Anmeldeunterlagen
unmittelbar und eindeutig.


Der erteilte Patentanspruch 1 setzt sich aus den ursprünglichen Ansprüchen 1 bis
3 zusammen. Die Auffassung der Klägerin, dass der beanspruchte Gegenstand des
Streitpatents aufgrund des Weglassens des Begriffs der „Synchronisierung“ gemäß
den ursprünglichen Ansprüchen 2 und 3 nicht ursprünglich offenbart sei, greift nicht
durch.

                                     - 18 -




Denn zum einen offenbaren die ursprünglichen Anmeldeunterlagen hinsichtlich der
Synchronisierung nichts anderes als die minimalen Anforderungen umfassend die
Signalisierung der Paketverarbeitung mit der zweiten Regelgruppe, das Stoppen
der Paketverarbeitung mit der ersten Regelgruppe („ceasing“), das Caching, das
Rekonfigurieren sowie die Signalisierung („completion“) gemäß den bereits in den
erteilten Anspruch aufgenommenen Merkmalen M1.8 und M1.8.1 bis M1.8.4 (vgl.
Offenlegungsschrift WO 2014/109843 A1, Fig. 3B - 3F und Fig. 4 i. V. m. Absätzen
[06], [28] - [34] und [36]). Zum anderen ist die Synchronisierung gemäß
Offenlegungsschrift, Absatz [06], optional („… may include synchronizing the
processors.“, Unterstreichung hinzugefügt) und gemäß Absatz [28] lediglich
vorteilhaft und somit fakultativ („… it may be advantageous to synchronize the
processors… “, Unterstreichung hinzugefügt).




2.   Zum Nichtigkeitsgrund der mangelnden Patentfähigkeit:
Dem Gegenstand von Patentanspruch 1 des Streitpatents in der erteilten Fassung
steht der Nichtigkeitsgrund der fehlenden Patentfähigkeit nicht entgegen, da das
unter Schutz gestellte Verfahren gegenüber dem im Nichtigkeitsverfahren
entgegengehaltenen Stand      der Technik      –   insbesondere hinsichtlich   der
Druckschriften NK13/NK19 sowie NK14 – neu ist und auf einer erfinderischen
Tätigkeit beruht.




2.1 Zur Neuheit
Der Gegenstand gemäß erteiltem Patentanspruch 1 erweist sich gegenüber dem
von der Klägerin im Verfahren genannten Stand der Technik als neu im Sinne des
Art. 54 EPÜ.


2.1.1 Das Verfahren des erteilten Patentanspruchs 1 ist neu gegenüber der
Druckschrift NK13/NK19 („Katayama“ bzw. Datenblatt „DAPDNA-2“), insbesondere

                                          - 19 -



fehlen die Merkmale M1.8.2 und M1.9 nach Streitpatent jeweils teilweise. Darüber
hinaus geht das Merkmal M1.8.4 aus der NK13/NK19 nicht unmittelbar und
eindeutig hervor.


Die NK13 betrifft ein verteiltes Firewall-System und ein entsprechendes Verfahren
für die Netzwerksicherheit umfassend vernetzte Firewalls in den Border-Routern an
der Netzwerkgrenze als Netzwerkschutzvorrichtungen (NK13, Titel und Fig. 1,
S. 1914, rechte Spalte, erster Absatz und S. 1915, rechte Spalte, erster Absatz;
Merkmal M1). Die vorgeschlagene Firewall gemäß NK13 basiert auf acht in einer
Pipelinestruktur seriell verschalteten, rekonfigurierbaren DAPDNA-2-Prozessoren
des Unternehmens IP-Flex/Fujitsu, welche als Dual-Core-Prozessoren mit dem
RISC-Core-DAP       („Digital   Application    Processor“)   und     einer    parallelen
Datenverarbeitung mittels 376 konfigurierbaren “Processing Elements (PEs)” im
DNA    („Distributed   Network     Architecture“)   ausgeführt     sind,     was   einen
Datendurchsatz von bis zu 10 Gb/s erlaubt (NK13, Fig. 7 und 8 i. V. m. Zusammenfassung, “We have developed a prototype system of a network ﬁrewall using
reconﬁgurable processors.”, S. 1918, linke Spalte, erster Absatz, “It is tandem
implemented on eight DAPDNA-2 chips with 10 Gb/s data and 5 Gb/s control data.”;
Datenblatt NK19, Fig. 1).


Ein Empfangen einer initialen ersten Regelgruppe (in der Vergangenheit
beispielsweise bei der ursprünglichen Erstinstallation bzw. Inbetriebnahme des
verteilten Firewall-Systems), deren Vorverarbeitung, das Konfigurieren der
Prozessoren und das Verarbeiten empfangener Pakete gemäß den Merkmalen
M1.1, M1.3 (teilweise/erste Hälfte), M1.4, M1.5 und M1.6 liest der Fachmann in der
Druckschrift NK13 unmittelbar mit (NK13, S. 1918, linke Spalte, zweiter Absatz, „The
ﬁrewall system located on the gateway can be realized on the prototype system
installing the ﬁrewall conﬁguration.“).


Die NK13 lehrt ein Empfangen einer zweiten Regelgruppe an einem Border-Router
im Fall einer Detektion eines Angriffs durch einen der anderen Border-Router, wobei

                                        - 20 -



die Border-Router – entgegen der Auffassung der Beklagten – nicht nur eine einzige
Regel, sondern vielmehr eine Regelgruppe umfassend eine Vielzahl an Regeln
untereinander austauschen (NK13, S. 1915, linke Spalte, letzter Absatz, „The other
is that the border router advertises the attack information and its ﬁltering rules when
the router detects the attacks.“; S. 1919, rechte Spalte, erster Absatz, “Therefore,
our system does not depend on the packet size or the number of ﬁrewall rules.”,
Unterstreichungen hinzugefügt; Merkmal M1.2).


Nach NK13 werden die empfangenen Regeln gemäß einer zweiten Regelgruppe
vorverarbeitet, indem die neuen Regeln (ggf. zusammen mit bereits vorhandenen
Regeln) in einen der umschaltbaren Rekonfigurationsspeicher der DAPDNA-2-
Prozessoren implementiert werden (NK13, Fig. 5 und S. 1915, rechte Spalte, letzter
Absatz, „…, a new rule is added to the ﬁltering table, …“; S. 1917, rechte Spalte,
erster Absatz, „exchange the conﬁgurations by rewriting the conﬁguration
memories.“; NK19, S. 1, rechte Spalte, „Dynamic Reconfiguration“, S. 2, rechte
Spalte, Tabelle DAPDNA-2 Specification: „Number of configurations: Four banks
(one foreground bank, three background banks. Background banks can be loaded
from external memory for unlimited number of configurations to be used.)“; Merkmal
M1.3 (teilweise/zweite Hälfte).


Der Fachmann entnimmt der NK13 ebenfalls ein Signalisieren an die acht (das
bedeutet i. S. des Streitpatents mindestens zwei) der seriell in der Pipelinestruktur
der Firewall angeordneten DAPDNA-2-Prozessoren, dass im Folgenden die zweite
Regelgruppe verwendet werden soll, wobei diese Signalisierung ein Umschalten
zwischen den Rekonfigurationsspeichern der Prozessoren bewirkt, um so mittels
der neuen Regeln die Netzwerkattacke abzuwehren (NK13, Fig. 6, Fig. 8 und S.
1915, rechte Spalte, letzter Absatz, „… the border ﬁrewall receives the attack
information … the attacks are orchestrally blocked by border ﬁrewalls.“; S. 1917,
rechte Spalte, dritter Absatz, „By dynamically exchanging the reconﬁguration
memories, we can realize new functions.“; S. 1918, linke Spalte, erster Absatz, „It is

                                       - 21 -



tandem implemented on eight DAPDNA-2 chips“, Unterstreichungen hinzugefügt;
Merkmal M1.7).


Die   NK13    offenbart   jedoch   keinerlei    Details   hinsichtlich   der   genauen
Implementierung, wie bzw. in welchem zeitlichen Ablauf das Umschalten der acht
seriell angeordneten DAPDNA-2-Prozessoren umgesetzt wird. Es bleibt also offen,
ob das Umschalten der Prozessoren synchron oder sequentiell erfolgt. Gleiches gilt
für eine hierzu ggf. verwendete Signalisierung. Darüber hinaus lehrt die NK13 nicht,
wie die zum Zeitpunkt des Regelgruppenwechsels in der Paketverarbeitung der
jeweiligen Prozessoren befindlichen Pakete zu behandeln sind.


Die NK13 führt lediglich aus, dass ein „hitless update“ der Prozessoren ohne
Unterbrechung der Dienste („without interrupting services“) durchgeführt werden
soll (NK13, S. 1917, rechte Spalte, oben), wobei das Update auf die zweite
Regelgruppe ohne Paketverlust erfolgen soll (NK13, Fig. 10 Bezugszeichen A
i. V. m. S. 1918, rechte Spalte, erster Absatz: „The line A shows that no packet is
lost when a function is updated, and it is independent to function size.”). Die NK13
offenbart zudem, dass jeder Prozessor innerhalb eines Taktes von 6 ns
umgeschaltet werden kann (NK13, S. 1917, rechte Spalte, vorletzter Absatz, „This
processor can handle more than 10 Gb/s traﬃc with 166 MHz processing. In
addition, it has four dynamic reconﬁguration memories, and exchanges within one
clock (about 6 nsec.).“, Unterstreichung hinzugefügt).


Der Regelgruppenwechsel der seriell angeordneten Prozessoren gemäß NK13
erfolgt also jeweils innerhalb eines einzigen Taktzyklus mit einem Stoppen bzw.
einem kurzen Unterbrechen der Paketverarbeitung in jedem der Prozessoren für
einen einzigen Clock-Cycle, wobei zumindest die aktuell von der Firewall
empfangenen, d. h. die neu angekommenen, Pakete in einem Eingangsspeicher
(„buffer type implementation“, „queue“) zwischengespeichert werden sollen (NK13,
S. 1917, rechte Spalte, zweitletzter Absatz, „The buﬀer-type implementation is easy,
and requires only a small buﬀer.“; S. 1918, linke Spalte, erster Absatz, “In order to

                                       - 22 -



hitless update, the buffer is implemented on the system.”; Merkmale M1.8, M1.8.1,
M1.8.2 teilweise, M1.8.3).


Daher fehlt das Merkmal M1.8.2 zumindest teilweise, da aufgrund der seriellen
Pipelinestruktur der multiplen Prozessoren in der NK13 nur der erste DAPDNA-2-
Prozessor und nicht, wie es der Anspruchswortlaut gemäß Patentanspruch 1
spezifiziert, mehrere Prozessoren jeweils im Einzelnen beim Verarbeitungsstopp
(Merkmal M1.8.1: „ceasing“) unverarbeitete Pakete in einem jeweiligen Cache
zwischenspeichern (Merkmal M1.8.2: „caching“).


Darüber hinaus fehlt in der NK13 die anspruchsgemäße Signalisierung zwischen
den Prozessoren gemäß Merkmal M1.8.4 vollständig, welche den Prozessoren
gegenseitig   den    erfolgreichen   Abschluss   der     Rekonfiguration   („signaling
completion“) kenntlich machen soll, um so ein synchrones Wiederaufnehmen der
Paketverarbeitung zu ermöglichen.


Gemäß NK13 werden zwar zunächst die zwischengespeicherten Pakete nach der
neuen Konfiguration (d. h. der zweiten Regelgruppe i. S. des Streitpatents)
verarbeitet, jedoch erfolgt dies ebenfalls ohne die bereits genannte, vorherige
streitpatentgemäße    Signalisierung   („signaling     completion“)   zwischen   den
Prozessoren, welche den erfolgreichen Abschluss der Rekonfiguration sämtlicher
Prozessoren anzeigt (vgl. NK13, S. 1918; Merkmal M1.9 teilweise).


Soweit die Klägerin hinsichtlich Merkmal M1.8.2 argumentiert, dass der „hitless
update“ ohne Paketverlust zwangsläufig ein Zwischenspeichern der sich in
Bearbeitung befindlichen Pakete sämtlicher DAPDNA-2-Prozessoren erfordere und
sich dafür der gemäß NK13 Figur 8 i. V. m. S. 1918, linke Spalte, erster Absatz
umlaufende 5 Gb/s Kontrolldaten-Bus eigne bzw. dafür sogar vorgesehen sei,
während der Rekonfiguration die aktuell bearbeiteten Pakete der jeweiligen
Prozessoren in den Eingangsspeicher zurückzuführen, überzeugt dies den Senat
nicht. Denn die NK13 zeigt sowohl in Figur 5 (b) i. V. m. S. 1917, rechte Spalte als

                                         - 23 -



auch in Figur 8 i. V. m. S. 1918, linke Spalte lediglich eine einzige Warteschlange
(„queue“, „reconfiguration queue“, „the buffer“) bzw. einen mit dem ersten Prozessor
assoziierten     Eingangsspeicher       („buffer    type     implementation“)      zum
Zwischenspeichern der während der Rekonfiguration neu empfangenen Pakete,
wobei laut NK13 die Speicherimplementierung einfach zu gestalten und der
Eingangsspeicher entsprechend klein sei (NK13, S. 1918, rechte Spalte, vorletzter
Absatz: „The buﬀer-type implementation is easy, and requires only a small buﬀer.“).
Eine Rückführung der sich aktuell in Verarbeitung befindlichen Pakete sämtlicher
Prozessoren während der Rekonfiguration in den Eingangsspeicher ist der NK13
weder unmittelbar noch eindeutig zu entnehmen.


Die Argumentation der Klägerin, dass hinsichtlich der Synchronisierung der
Prozessoren die komplette anspruchsgemäße Signalisierung entsprechend den
Merkmalen M1.8.1 bis M1.8.4 mitzulesen sei, überzeugt ebenso wenig. Denn ein
Mitlesen bedeutet, dass der Fachmann die Synchronisierung der Prozessoren in
der gleichen Weise, wie im Patentanspruch 1 beansprucht, implementieren muss.
Demgegenüber verweist die Beklagte zu Recht auf eine Vielzahl potentieller,
alternativer Implementierungsmöglichkeiten ohne eine solche anspruchsgemäße
Signalisierung, die gleichfalls ein „hitless update“ ohne Paketverlust realisieren, und
nennt   dabei    beispielhaft   das    auf    „shadow      paging“   basierte,   zweite
Ausführungsbeispiel gemäß NK17, Absatz [0054], wobei ein Regelgruppenwechsel
jeweils nur die neu empfangenen Pakete betrifft und die aktuellen Pakete in
Bearbeitung noch mittels der ursprünglichen Regelgruppe abgearbeitet werden
(dort: „Shadow paging guarantees that a packet whose processing has already
begun, will be processed to the end using those rules in effect when the processing
of the packet was started. Shadow paging also allows frequent updating, since the
principle of shadow paging allows for a plurality of generations of filter code to be in
concurrent execution. In other words, the interval between subsequent filter rule
updates can be shorter than the average processing time of a packet, whereby
many updates can occur during the average processing time of a packet.“).

                                            - 24 -



2.1.2 Das Verfahren des erteilten Patentanspruchs 1 ist auch neu gegenüber der
Druckschrift NK14 (US 2006/0048142 A1). Gegenteiliges hat die Klägerin nicht
geltend gemacht. Zur Überzeugung des Senats fehlen in der NK14 die Merkmale
M1.4, M1.6, M1.7, M1.9 jeweils teilweise und die Merkmalsgruppe M1.8, M1.8.1 bis
M1.8.4 geht aus der NK14 überhaupt nicht hervor.


Die NK14 betrifft ein „SYSTEM AND METHOD FOR RAPID RESPONSE
NETWORK POLICY IMPLEMENTATION“ (NK14, Titel). Gemäß der NK14 wird in
einer Netzwerkvorrichtung („network infrastructure device“) umfassend eine PEF
(„policy enforcement function“), welche beispielsweise ein Netzwerkzugangsgerät
(„network entry device“), eine Firewall, ein Router, ein Gateway oder ein Switch ist,
im Fall eines detektierten Angriffs („attack detection“) eine Rekonfiguration von
Regeln/Policies mittels ggf. vorab lokal gespeicherten Regelsätzen/Policies („preinstalled policy and/or PER sets“) durchgeführt, wobei der Fokus auf ein schnelles
Umschalten („rapid reaction“) gelegt wird. Hierzu wird eine Signalisierung von „rapid
response identifiers (RR)“ zwischen einem Policy Manager und der jeweiligen PEF
vorgeschlagen (NK14, Fig. 2 und 4, Absätze [0037], [0046], [0050], [0056] mit
Tabelle).


Die Argumentation der Klägerin, dass diese vom Policy Manager mittels Multicast
oder Broadcast durchgeführte Signalisierung zum Regelgruppenwechsel an ein
oder mehrere ausgewählte PEFs, die ebenfalls eine Überprüfung des Status einer
jeweils     initiierten   Implementierung     der     neuen      Regelgruppe    bzw.   eines
Regelgruppenwechsels           durch    den     Policy        Manager    umfassen,      eine
anspruchsgemäße            „Synchronisierung“        multipler    Prozessoren     in   einer
Netzwerkschutzvorrichtung darstelle (NK14, Absatz [0021], „The policy manager
function may also confirm the status of implementation of an initiated policy/rule set
change.“ und Absatz [0041], „… to implement the policy and/or PER set by signaling
the processor 253 to initiate the enforcement of the selected policy and/or PER
set(s). That signaling may be achieved as through communication using multicast
and/or broadcast communication methods …“), greift nicht durch. Denn der

                                       - 25 -



Fachmann entnimmt der NK14 bereits keine multiplen Prozessoren in einem
einzelnen Gerät („device“) einer Netzwerkschutzvorrichtung zur Paketverarbeitung
gemäß den Merkmalen M1.4, M1.6, M1.7, M1.9 (jeweils teilweise), da dort pro Gerät
der Netzwerkschutzvorrichtung nur ein einziger Prozessor gemäß Figur 2,
Bezugszeichen 253 i. V. m. Absatz [0038] vorhanden ist ( „A network infrastructure
device having forwarding functionality and with the PEF 250 includes a forwarding
engine 252, a processor 253, an ingress port interface 254, an egress port interface
255, and a communication function 258.“; Unterstreichungen hinzugefügt).


Entgegen der Auffassung der Klägerin handelt es sich bei den in der NK14, Figur 1,
Bezugszeichen 105a und 105b dargestellten beiden „Network entry devices“ nicht
um eine verteilte Netzwerkschutzvorrichtung, sondern jeweils um eigenständige
Geräte („device“) mit jeweils einer eigenen PEF 250 zur Überwachung einer
eigenen dediziert zugeordneten Schnittstelle zum Netzwerk wie beispielsweise eine
WLAN-Schnittstelle oder eine Internet/WAN-Schnittstelle. Da hier keine Arbeitsteilung von multiplen Prozessoren bei der Paketverarbeitung i. S. d. Streitpatents
vorliegt, ist ein Addieren der jeweils pro Gerät vorhandenen einzelnen Prozessoren
(NK14, Fig. 2, Bezugszeichen 253) zu multiplen Prozessoren nicht opportun.


Darüber hinaus fehlt folglich ebenso das im Anschluss an die Signalisierung zum
Regelgruppenwechsel durchzuführende „Synchronisieren“ der (in der NK14 nicht
vorhandenen) multiplen Prozessoren gemäß der Merkmalsgruppe M1.8, M1.8.1 bis
M1.8.4. Die NK14 adressiert weder explizit ein anspruchsgemäßes Stoppen
(„ceasing“) der Paketverarbeitung durch den jeweiligen Prozessor, noch ein
Zwischenspeichern der sich gerade in der Verarbeitung befindlichen Pakete bzw.
der während des Rekonfigurierens neu empfangenen Pakete in einem Cache.
Schließlich fehlt in der NK14 ebenfalls das Signalisieren einer erfolgreich
abgeschlossenen     Rekonfiguration    („signaling   …   completion“)   unter   den
Prozessoren gemäß M1.8.4, um dann anschließend gemäß Merkmal M1.9 die
Paketverarbeitung basierend auf dem neuen Regelsatz synchron weiterzuführen.

                                         - 26 -



Zwar beschreibt die NK14 die Bestätigung des Empfangs einer Nachricht zur
Rekonfiguration vom „Policy Manager“, die den „rapid response identifier (RR)“
durch jede einzelne PEF mittels einer Bestätigung („acknowledgement“) umfasst,
diese betrifft jedoch ausschließlich die Signalisierung gemäß Merkmal M1.7,
zumindest soweit diese als Broadcast-Nachricht ausgestaltet ist (NK14, Tabelle in
Absatz [0056], „RR-N … May use a single broadcast command, Follow-up for
confirmation, with individual acknowledgements“).


Hinsichtlich    der   ebenfalls   in   der   NK14   offenbarten    Überprüfung     des
Implementierungsstatus einer Regelsatzänderung in einer PEF wird hingegen
lediglich weiter dazu ausgeführt, dass „der Policy Manager“ die PEF diesbezüglich
anfragt („polling“) und von dieser eine entsprechende Bestätigung erhält (NK14,
Absatz [0048], „Further, the effect of the policy change implementation may be
verified or evaluated by, for example, polling the one or more selected PEFs 250 to
confirm receipt of the selected rapid response identifiers communicated as well as
any or all implementation activities (Step 311). Such verification may be of particular
interest in those instances when policy change implementation instructions are
communicated by multicast or broadcast messaging.“; Unterstreichungen
hinzugefügt).


2.1.3 Dass der Gegenstand des erteilten Patentanspruchs 1 aus einer der übrigen
im Verfahren befindlichen und weiter abliegenden Druckschriften neuheitsschädlich
vorweggenommen sei, hat weder die Klägerin vorgetragen, noch ist dies für den
Senat ersichtlich.




2.2 Zur erfinderischen Tätigkeit
Das Verfahren gemäß erteiltem Patentanspruch 1 beruht auch auf einer
erfinderischen Tätigkeit im Sinne des Art. 56 EPÜ, da es sich für den Fachmann
nicht in naheliegender Weise aus dem entgegengehaltenen Stand der Technik
ergibt. Insbesondere gelangt der Fachmann ausgehend vom Stand der Technik

                                      - 27 -



nach einer der Druckschriften NK13 oder NK14 nicht in naheliegender Weise zum
Verfahren des erteilten Patentanspruchs 1.


2.2.1 Erfinderische Tätigkeit ausgehend von der Druckschrift NK13
Die Argumentation der Klägerin hinsichtlich des in der NK13 fehlenden Merkmals
M1.8.2, der Fachmann sehe für das „hitless update“ ohne Paketverlust den 8 kByte
großen     „Data   Cache“   des   DAP-Cores    gemäß     NK19,    Figur   1   zum
Zwischenspeichern für die während der Rekonfiguration in Verarbeitung
befindlichen Pakete vor, überzeugt den Senat nicht. Denn gemäß dem Datenblatt
NK19 ist der DNA-Core des DAPDNA-2-Prozessors verantwortlich für das parallele
Verarbeiten der Nutzdaten, d. h. der Pakete, wobei die Nutzdaten über die DNA-
„direct I/O“-Schnittstelle unter Umgehung des internen High-Speed-Datenbusses
der PE-Matrix zu- und abgeführt werden (NK19, Fig. 1 i. V. m. S. 2, linke Spalte,
vierter Absatz, „The DNA Direct I/O can be also used to communicate directly with
external devices, bringing data in for processing on the PE Matrix, bypassing the
Bus Switch and memory interface.“). Daher ist es für den Senat weder ersichtlich,
noch lässt sich der NK13/NK19 für den Fachmann eine entsprechende Anregung
bzw. ein Hinweis entnehmen, warum der Data-Cache des DAP-Cores zum
Zwischenspeichern der sich bei der Rekonfiguration in der Verarbeitung durch den
DNA-Core befindlichen Pakete dienen soll.


Die gleiche Begründung gilt im Wesentlichen für die Argumentation der Klägerin,
dass gemäß NK13/NK19 bereits zwei Prozessoren, nämlich die beiden
Prozessorkerne des ersten DAPDNA-2-Chips – also der DAP-Core sowie der DNA-Core – in der Serienschaltung Zugriff auf den Cache hätten, wie dies Merkmal 1.8.2
fordert.


Auch die Ansicht der Klägerin, der Fachmann würde ausgehend von der NK13 die
NK8 hinzuziehen und den ersten DAPDNA-2-Prozessor, welcher in der
Serienschaltung aus acht Prozessoren die meisten Pakete zu verarbeiten habe, aus
Rechenkapazitätsgründen bzw. zur Steigerung der Leistungsfähigkeit der Firewall

                                          - 28 -



durch zwei parallel geschaltete DAPDNA-2-Prozessoren ersetzen, um in der Folge
Merkmal M1.8.2 zu verwirklichen, teilt der Senat nicht. Zwar weist der DNA-Core
gemäß NK19 sechs „direct I/O“-Kanäle zum Verbinden multipler DAPDNA-2-
Prozessoren auf, was prinzipiell eine derartige Verschaltung der acht DAPDNAs
gemäß NK13 mit zwei parallelen sowie sechs seriellen Prozessoren zuließe.
Allerdings zeigt die NK19, S. 2, linke Spalte („Multiple DAPDNA-2 processors can
be connected through the DNA Direct l/O and integrated into a single system at 16
Gbps throughput.“) jedoch auch, dass eine Serienschaltung multipler DAPDNA-2-
Prozessoren in einem System integriert mit 16 Gb/s Datendurchsatz sowieso bereits
eine 60% Marge gegenüber den in der NK13 vorgeschlagenen 10 Gb/s
Datendurchsatz des Firewalls aufweist, wodurch die technische Veranlassung für
den Fachmann zur Umsetzung einer derart modifizierten Architektur nicht ersichtlich
ist.


Zudem konnte die Klägerin nicht überzeugend darlegen, dass der Fachmann für die
Realisierung   der   „hitless     update“     Funktionalität   die     anspruchsgemäße
Signalisierung „Completion“ gemäß Merkmal M1.8.4 verwenden würde, um ein
synchrones Weiterführen der Paketverarbeitung gemäß Merkmal M1.9 durch die
multiplen Prozessoren zu triggern.


Die Klägerin trägt vor, dass gemäß NK13, Figur 8, bedingt durch die serielle
Pipelinestruktur zwischen einer Makro- und einer Mikro-Konfiguration der
Prozessoren unterschieden werden müsse, wobei die Signalisierung zum
Umschalten der DAPDNA-2-Prozessoren bzw. zur (Mikro-)Rekonfiguration gemäß
Merkmal M1.7 erst von einem zum nächsten Prozessor in einer Art Kaskade
weitergereicht werden müsse, wobei die auftretenden zeitlichen Versätze nicht zu
prädizieren wären. Um unter solchen Randbedingungen überhaupt das „hitless
update“ ohne Paketverlust zu ermöglichen, müssten somit alle acht seriellen
Prozessoren    unbedingt        rechtzeitig   rekonfiguriert   sein,    ehe   mit   der
Weiterverarbeitung der Pakete begonnen werden könne. Aus diesem Grund

                                          - 29 -



verwende      der    Fachmann       als      die   offensichtlichste   Lösung     den
Sicherheitsmechanismus der Signalisierung „Completion“ gemäß Merkmal M1.8.4.


Nach Ansicht des Senats berücksichtigt die Klägerin jedoch nicht, dass für eine
potentielle Signalisierung „Completion“ durch die o. g. Kaskade eine im
Wesentlichen ähnliche zeitliche Unsicherheit gegeben wäre wie für die o. g. (bereits
erfolgte) Signalisierung zur Rekonfiguration, wobei hier jedoch verschärfend gemäß
Merkmal M1.8.4 jeder einzelne der acht Prozessoren die entsprechende
Signalisierung zu den anderen sieben Prozessoren anstoßen müsste, welche
wiederum gemäß Merkmal M1.9 von jedem der anderen Prozessoren empfangen
werden müsste. Der Senat vermag nicht zu erkennen, wie dadurch aufgrund des
angeblich immanent vorliegenden zeitlichen Versatzes bei jeder einzelnen der
insgesamt mindestens acht (unter Annahme eines in der NK13 nicht offenbarten
Multicasts) bzw. maximal 56 (8x7=56; bei einem genauso wenig offenbarten Punktzu-Punkt Unicast) Signalisierungsnachrichten eine sichere Synchronisierung der
acht Prozessoren ohne Paketverlust erzielt werden kann, insbesondere unter der
Randbedingung einer nicht nennenswert bemerkbaren Unterbrechung des Service
(NK13, S. 1914, rechte Spalte, „a hitless ﬁrewall algorithm update function without
interrupting services.“). Hierzu trägt die Klägerin auch nichts vor.


Darüber hinaus fehlt im Vortrag der Klägerin ein Beleg für ein solches Fachwissen,
diese spezielle Form der Synchronisierung gemäß der Merkmalsgruppe M1.8 zu
verwenden, z. B. durch die Nennung von Lehrbüchern. Ebenso umfasst keine der
im Verfahren genannten Entgegenhaltungen die anspruchsgemäße Signalisierung
„Completion“ gemäß Merkmal M1.8.4.


Dagegen zeigt NK17 in Absatz [0054] zudem mit dem „Shadow Paging“ eine
gleichfalls   mögliche,   alternative     Implementierung,   welche    ohne   jegliche
Signalisierung auskommt und welche trotz häufiger Updates der Regelsätze für
hohe Datenraten geeignet erscheint, wie die Beklagte in der mündlichen

                                          - 30 -



Verhandlung vorgetragen hat (siehe auch die Ausführungen zur Neuheit gemäß Ziff.
2.1.1).


Schließlich entnimmt der Fachmann aus Sicht des Senats der NK13 auch keinerlei
Anregungen bzw. Hinweise, sowohl das anspruchsgemäße Zwischenspeichern der
Pakete durch multiple Prozessoren gemäß Merkmal M1.8.2, als auch die
anspruchsgemäße „Synchronisierung“, umfassend insbesondere die Signalisierung
„Completion“     zwischen   den       Prozessoren,   gemäß    Merkmal    M1.8.4    zu
implementieren.


2.2.2 Erfinderische Tätigkeit ausgehend von der Druckschrift NK14
Entgegen der Auffassung der Klägerin sieht der Senat in der NK14 weder einen
Hinweis noch eine Anregung, die der NK14 fehlenden Merkmale gemäß
Patentanspruch 1 hinzuzufügen, die die multiplen Prozessoren und insbesondere
die „Synchronisierung“ jener mittels der anspruchsgemäßen Signalisierung beim
Regelgruppenwechsel (Merkmale M1.4, M1.6, M1.7, M1.9 jeweils teilweise sowie
Merkmalsgruppe M1.8, M1.8.1 bis M1.8.4 komplett) umfassen.


Hinsichtlich der Kombination der Druckschrift NK14 mit dem fachmännischen
Wissen belegt durch die Druckschriften NK8, NK9, NK10, NK15, NK16 und NK17
argumentiert die Klägerin lediglich pauschal, indem sie den Gegenstand des
Patentanspruchs 1 aus der Vielzahl der genannten Druckschriften mosaikartig
zusammenzufügen versucht. Der Senat kann hierbei jedoch nicht erkennen, wo der
Fachmann       beispielsweise   die    Signalisierung   „Completion“   der   multiplen
Prozessoren beim Abschluss der Rekonfiguration gemäß Merkmal M1.8.4
entnimmt.


Zwar zeigt die NK17 in einem ersten Ausführungsbeispiel für den Regelgruppenwechsel eine Signalisierung zwischen einer Regel-Kompilierungseinheit
(„rule compiling entity“) und einem Paketfilter („rule processing entity“) umfassend
die beiden Nachrichten „PAUSING OF PROCESSING“ sowie „CONTINUING OF

                                      - 31 -



PROCESSING“, jedoch dient diese Signalisierung zum einen nur dem Umschalten
eines Prozessors und nicht der Synchronisierung multipler Prozessoren, und zum
anderen werden gemäß NK17 die vor dem Regelgruppenwechsel empfangenen
Pakete im Paketfilter stets mit der alten, ursprünglichen ersten Regelgruppe
verarbeitet (NK17, Fig. 1, Bezugszeichen 130, 150 i. V. m. Absatz [0031], Absatz
[0037], „… in which the packet processing entity is a first processor and the rule
compiling entity is a second processor, …“; Fig. 4, Bezugszeichen 430, 440 i. V. m.
Absätzen [0045] – [0046]).


Ausgehend von der NK14 führt auch die von der Klägerin vorgetragene
Zusammenschau mit der NK13 nicht zu ihrem Ziel. Abgesehen davon, dass die
NK14 mit einer zentralen Netzwerküberwachung und Regelverwaltung durch den
„Policy Manager“ und die NK13 mit dem vorgeschlagenen verteilten Firewallsystem
ohne jegliche Zentraleinheit völlig verschiedene Firewallarchitekturen betreffen,
würde ein Ersetzen der „network entry devices“ gemäß NK14 durch die DAPDNA-2-Firewall-Prototypen allenfalls die teilweise fehlenden Merkmale M1.4, M1.6, M1.7,
M1.9 hinsichtlich der multiplen Prozessoren pro Netzwerkschutzvorrichtung bzw.
pro Gerät ergänzen.


Wie oben zur Neuheit ausgeführt (siehe Ziff. 2.1.1 und 2.1.2), offenbaren weder die
NK14 noch die NK13 das Zwischenspeichern von Paketen durch die multiplen
Prozessoren in einem Cache gemäß Merkmal M1.8.2. Zudem betrifft auch die aus
der NK14 bekannte Signalisierung zwischen „Policy Manager“ und PEF/„network
entry device“ mit der Bestätigung der Rekonfigurationssignalisierung M1.7 sowie
der Überwachung des Implementierungszustands des neuen Regelsatzes in der
PEF mittels Polling nur die Makro-Konfiguration eines jeweiligen Firewall-Prototypen (bzw. „network entry device“) und nicht die Mikro-Konfiguration der dort
vorhandenen    acht   DPADNA-2-Prozessoren.        Da   allerdings   schon   diese
Signalisierung gemäß NK14 weder zu Merkmal M1.8.4 noch zu Merkmal M1.9 führt,
kann auch eine potentielle Signalisierung zwischen dem „Policy Manager“ und
jedem einzelnen DAPDNA-2-Prozessor eines jeweiligen Firewall-Prototypen (bzw.

                                        - 32 -



„network entry device“) hinsichtlich seiner Mikro-Konfiguration dahingestellt bleiben.
Der Fachmann würde eine derartige Signalisierung nach Überzeugung des Senats
aufgrund der zusätzlichen Verzögerungen auch nicht vorsehen.


2.2.3 Zu den übrigen Druckschriften NK3 bis NK10 und NK15 bis NK18 hat die
Klägerin hinsichtlich der erfinderischen Tätigkeit nicht vorgetragen. Auch der Senat
kann nicht erkennen, wie diese im Einzelnen oder in Kombination zum Gegenstand
des erteilten Patentanspruchs 1 führen können.




3.   Entsprechendes gilt für die angegriffenen, nebengeordneten Patentansprüche
14 und 15, welche bereits durch ihren Rückbezug auf den patentfähigen
Patentanspruch 1 rechtsbeständig sind. Gegenteiliges hat die Klägerin nicht geltend
gemacht.




4.   Hinsichtlich der ebenfalls angegriffenen Unteransprüche 2 bis 13, welche
vorteilhafte Ausgestaltungen des Erfindungsgegenstands betreffen, gelten auch die
vorstehenden, den Patentanspruch 1 betreffenden Ausführungen entsprechend.
Die Unteransprüche sind ebenfalls bereits durch ihren Rückbezug auf den
patentfähigen Patentanspruch 1 rechtsbeständig. Auch diesbezüglich hat die
Klägerin nichts Gegenteiliges geltend gemacht.




                                         B.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                      - 33 -




                                       C.


                            Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigen schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Heimen          Schödel            Dr. Ball         Bieringer        Christoph
