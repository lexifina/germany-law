---
ecli: "ECLI:DE:BPatG:2011:100311B17Wpat77.07.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 77/07"
decided: "2011-03-10"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=17&nr=19038&anz=1310&pos=259&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-03-10_17_W-pat_77_07_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 77/07 vom 2011-03-10

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 77/07                                                  Verkündet am
_______________                                                    10. März 2011
    (Aktenzeichen)                                                      …




                               BESCHLUSS

                             In der Beschwerdesache


             betreffend die Patentanmeldung 10 2006 032 832.9-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 10. März 2011 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Fritsch,   der   Richterin   Eder,   des   Richters
Dipl.-Ing. Baumgardt und der Richterin Dipl.-Ing. Wickborn




BPatG 154
08.05

                                         -2-



beschlossen:


                        Die Beschwerde wird zurückgewiesen.




                                     Gründe:


                                          I.


Die vorliegende Patentanmeldung DE 10 2006 032 832.9-53 mit der Bezeichnung:


          „Netzwerksystem und Verfahren zur Steuerung verteilter Speicher“


ist am 14. Juli 2006 beim Deutschen Patent- und Markenamt eingereicht worden.
Sie wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen
Patent- und Markenamts mit der Begründung zurückgewiesen, der Patentanspruch 1 in der Fassung des damals geltenden Hauptantrags sowie in der Fassung der damals geltenden Hilfsanträge 1 bis 3 sei jeweils nicht gewährbar, da
sein Gegenstand gegenüber Druckschrift D1 nicht auf erfinderischer Tätigkeit
beruhe.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie stellt
den Antrag,


          den angefochtenen Beschluss aufzuheben und das nachgesuchte Patent
          mit folgenden Unterlagen zu erteilen:


          gemäß Hauptantrag mit
          Patentansprüchen 1 - 17, überreicht in der mündlichen Verhandlung,
          noch anzupassender Beschreibung S. 1 - 17 und
          3 Blatt Zeichnungen mit 3 Figuren, jeweils vom Anmeldetag,

                                       -3-



       gemäß Hilfsantrag mit
       Patentansprüchen 1 - 15, überreicht in der mündlichen Verhandlung, im
       Übrigen wie Hauptantrag.


Die Patentansprüche 1 und 11 in der geltenden Fassung des Hauptantrags mit
einer denkbaren Gliederung versehen lauten:


       „1. Netzwerksystem (1) mit einer Vielzahl über Netzwerkverbindungen (3)
       verbundener Netzelemente (2),


       a) wobei jedes der Netzelemente (2) mindestens einen Speicher (5)
           sowie   eine    Direktspeicherzugriff (DMA)      -fähige   Netzwerkschnittstelle (8) aufweist,


       b) wobei auf jedem Netzelement (2) eine Instanz (VM-Instanz, 12) einer
           virtuellen Maschine (VM, 11) läuft,


       c) die zumindest einen Teil des Speichers (5) in dem Netzelement (2) als
           globalen VM-Speicherbereich (10) bestimmt, wobei jede der VM-Instanzen (12) Zugriffsrechte hierauf besitzt,


       d) wobei jeder Speicherstelle im VM-Speicherbereich (10) eine für alle
           VM-Instanzen (12) der virtuellen Maschine (11) einheitliche globale
           Adresse zugeordnet ist,


       e) welche sich zusammensetzt aus einer Adresse des Netzelementes (2)‚
           in dem der VM-Speicherbereich (10) angeordnet ist, und einer lokalen
           realen Adresse auf diesem Netzelement (2),


       c´) wobei nach der Installation der VM-Instanzen (12) auf den einzelnen
           Netzelementen (2) jede der VM-Instanzen (12) einen VM-Speicherbe-

                                  -4-



     reich (10) in dem Speicher (5) des zugehörigen Netzelementes (2)
     bestimmt und


f)   sämtliche VM-Instanzen (12) die globalen Adressen ihrer jeweiligen
     alloziierten VM-Speicherbereiche untereinander austauschen oder die
     Adressbereiche der globalen Adressen ihrer VM-Speicherbereiche (10) untereinander austauschen, und


g) wobei mittels der lokal laufenden VM-Instanz (12a) mindestens eines
     der Netzelemente (2a) beim Zugriff auf die globale Adresse einer sich
     auf einem weiteren, entfernten Netzelement (2b) befindenden physikalischen Speicherstelle die zugehörige lokale reale Adresse auf dem
     entfernten Netzelement (2b) berechenbar und ein DMA-Aufruf mit
     Quell- und Zieladresse initiierbar ist sowie auf den globalen VM-Speicherbereich des entfernten Netzelements (2b) zugreifbar ist.“


„11. Verfahren zur Steuerung verteilter Speicher (5) in einem Netzwerksystem (1) mit einer Vielzahl über Netzwerkverbindungen (3) verbundener
Netzelemente (2),


a) wobei jedes der Netzelemente (2) mindestens einen Speicher (5)
     sowie eine Direktspeicherzugriff- (DMA) -fähige Netzwerkschnittstelle (8) aufweist,


b) wobei auf jedem Netzelement (2) eine Instanz (VM-Instanz, 12) einer
     virtuellen Maschine (VM, 11) installiert wird,


c) die zumindest einen Teil des Speichers (5) in dem jeweiligen Netzelement (2) als VM-Speicherbereich (10) bestimmt, auf den jede der VM-Instanzen (12) der virtuellen Maschine (11) zugreifen kann,

                                       -5-



       d) wobei jeder Speicherstelle im VM-Speicherbereich (10) eine für alle
            VM-Instanzen (12) einheitliche globale Adresse zugeordnet wird,


       e) welche sich zusammensetzt aus einer Adresse des Netzelementes (2), in dem der VM-Speicherbereich (10) angeordnet ist, und einer
            lokalen realen Adresse auf diesem Netzelement (2),


       c´) wobei nach der Installation der VM-Instanzen (12) auf den einzelnen
            Netzelementen (2) jede der VM-Instanzen (12) einen VM-Speicherbereich (10) in dem Speicher (5) des zugehörigen Netzelementes (2)
            bestimmt und


       f)   wobei sämtliche VM-Instanzen (12) die globalen Adressen ihrer jeweiligen alloziierten VM-Speicherbereiche untereinander austauschen
            oder die Adressbereiche der globalen Adressen ihrer VM-Speicherbereiche (10) untereinander austauschen, und


       g) wobei mittels der lokal laufenden VM-Instanz (12a) mindestens eines
            der Netzelemente (2a) beim Zugriff auf die globale Adresse einer sich
            auf einem weiteren, entfernten Netzelement (2b) befindenden physikalischen Speicherstelle die zugehörige lokale reale Adresse auf dem
            entfernten Netzelement (2b) berechnet und ein DMA-Aufruf mit Quellund Zieladresse initiiert wird sowie auf den globalen VM-Speicherbereich des entfernten Netzelements (2b) zugegriffen wird.“


Hinsichtlich der Unteransprüche 2 bis 10 und 12 bis 17 wird auf die Akte verwiesen.


Die Patentansprüche 1 und 10 in der Fassung des nunmehr einzigen Hilfsantrags
mit einer an die Fassung des Hauptantrags angepassten Gliederung und gegenüber der Fassung des Hauptantrags unterstrichenen Änderungen lauten:

                                 -6-



„1. Netzwerksystem (1) mit einer Vielzahl über Netzwerkverbindungen (3)
verbundener Netzelemente (2),


a) wobei jedes der Netzelemente (2) mindestens einen Speicher (5)
     sowie   eine    Direktspeicherzugriff (DMA)      -fähige   Netzwerkschnittstelle (8) aufweist,


b) wobei auf jedem Netzelement (2) eine Instanz (VM-Instanz, 12) einer
     virtuellen Maschine (VM, 11) läuft,


c) die zumindest einen Teil des Speichers (5) in dem Netzelement (2) als
     globalen VM-Speicherbereich (10) bestimmt, wobei jede der VM-Instanzen (12) Zugriffsrechte hierauf besitzt,


d) wobei jeder Speicherstelle im VM-Speicherbereich (10) eine für alle
     VM-Instanzen (12) der virtuellen Maschine (11) einheitliche globale
     Adresse zugeordnet ist,


e) welche sich zusammensetzt aus einer Adresse des Netzelementes (2), in dem der VM-Speicherbereich (10) angeordnet ist, und einer
     lokalen realen Adresse auf diesem Netzelement (2),


c´) wobei nach der Installation der VM-Instanzen (12) auf den einzelnen
     Netzelementen (2) jede der VM-Instanzen (12) einen VM-Speicherbereich (10) in dem Speicher (5) des zugehörigen Netzelementes (2)
     bestimmt und


f)   sämtliche VM-Instanzen (12) die globalen Adressen ihrer jeweiligen
     alloziierten VM-Speicherbereiche untereinander austauschen oder die
     Adressbereiche der globalen Adressen ihrer VM-Speicherbereiche (10) untereinander austauschen, und

                                  -7-



g) wobei mittels der lokal laufenden VM-Instanz (12a) mindestens eines
     der Netzelemente (2a) beim Zugriff auf die globale Adresse einer sich
     auf einem weiteren, entfernten Netzelement (2b) befindenden physikalischen Speicherstelle die zugehörige lokale reale Adresse auf dem
     entfernten Netzelement (2b) berechenbar und ein DMA-Aufruf mit
     Quell- und Zieladresse initiierbar ist sowie auf den globalen VM-Speicherbereich des entfernten Netzelements (2b) zugreifbar ist, und


h) wobei mehrere VM-Instanzen (12) verschiedener Netzelemente (2)
     jeweils einen Cache-Speicherbereich (6a, 6b) in dem Speicher (5a,
     5b) ihres Netzelementes vorsehen zum Zwischenspeichern von aus
     dem VM-Speicherbereich (10) angeforderten oder anzufordernden Daten und


i)   wobei die mehreren Cache-Speicherbereiche (6a, 6b) zusammen
     einen globalen, über lokale Speicherbereiche verteilten VM-Cache-Speicherbereich (6) ausbilden, welcher von der virtuellen Maschine
     verwaltbar und kontrollierbar ist.“


„10. Verfahren zur Steuerung verteilter Speicher (5) in einem Netzwerksystem (1) mit einer Vielzahl über Netzwerkverbindungen (3) verbundener
Netzelemente (2)‚


a) wobei jedes der Netzelemente (2) mindestens einen Speicher (5)
     sowie eine Direktspeicherzugriff- (DMA) -fähige Netzwerkschnittstelle (8) aufweist,


b) wobei auf jedem Netzelement (2) eine Instanz (VM-Instanz, 12) einer
     virtuellen Maschine (VM, 11) installiert wird,

                                -8-



c) die zumindest einen Teil des Speichers (5) in dem jeweiligen Netzelement (2) als VM-Speicherbereich (10) bestimmt, auf den jede der VM-Instanzen (12) der virtuellen Maschine (11) zugreifen kann,


d) wobei jeder Speicherstelle im VM-Speicherbereich (10) eine für alle
     VM-Instanzen (12) einheitliche globale Adresse zugeordnet wird,


e) welche sich zusammensetzt aus einer Adresse des Netzelementes (2)‚
     in dem der VM-Speicherbereich (10) angeordnet ist, und einer lokalen
     realen Adresse auf diesem Netzelement (2),


c´) wobei nach der Installation der VM-Instanzen (12) auf den einzelnen
     Netzelementen (2) jede der VM-Instanzen (12) einen VM-Speicherbereich (10) in dem Speicher (5) des zugehörigen Netzelementes (2)
     bestimmt und


f)   wobei sämtliche VM-Instanzen (12) die globalen Adressen ihrer jeweiligen alloziierten VM-Speicherbereiche untereinander austauschen
     oder die Adressbereiche der globalen Adressen ihrer VM-Speicherbereiche (10) untereinander austauschen, und


g) wobei mittels der lokal laufenden VM-Instanz (12a) mindestens eines
     der Netzelemente (2a) beim Zugriff auf die globale Adresse einer sich
     auf einem weiteren, entfernten Netzelement (2b) befindenden physikalischen Speicherstelle die zugehörige lokale reale Adresse auf dem
     entfernten Netzelement (2b) berechnet und ein DMA-Aufruf mit Quellund Zieladresse initiiert wird sowie auf den globalen VM-Speicherbereich des entfernten Netzelements (2b) zugegriffen wird, und


h) wobei mehrere VM-Instanzen (12) verschiedener Netzelemente (2)
     jeweils einen Cache-Speicherbereich (6a, 6b) in dem Speicher (5a,

                                          -9-



             5b) ihres Netzelementes vorsehen zum Zwischenspeichern von aus
             dem VM-Speicherbereich (10) angeforderten oder anzufordernden Daten und


        i)   wobei die mehreren Cache-Speicherbereiche (6a, 6b) zusammen
             einen globalen, über lokale Speicherbereiche verteilten VM-Cache-Speicherbereich (6) ausbilden, welcher von der virtuellen Maschine
             verwaltet und kontrolliert wird.“


Hinsichtlich der Unteransprüche 2 bis 9 und 11 bis 15 wird auf die Akte verwiesen.


Der Anmeldung soll die Aufgabe zugrunde liegen, ein Netzwerksystem und ein
Verfahren zur Verfügung zu stellen, mit dem effizient und konsistent auf verteilte
Speicher zugegriffen werden kann, um beispielsweise eine parallele Anwendung
auf verteilten Netzwerkeinheiten durchzuführen (S. 5 Abs. 2 der Anmeldeunterlagen).


Die Anmelderin vertritt die Auffassung, die Lehre der Patentansprüche 1 und 11 in
der Fassung des Hauptantrags sowie die Lehre der Patentansprüche 1 und 10 in
der Fassung des Hilfsantrags beruhten auf erfinderischer Tätigkeit gegenüber dem
genannten Stand der Technik.
Aus keiner der im Verfahren befindlichen Druckschriften sei das Ansprechen des
globalen Speicherbereichs ausschließlich über eine aus der physikalischen
Adresse des Netzelementes (z. B. MAC-Adresse) und der realen Speicheradresse
bestehende zweiteilige Adresse zu entnehmen, wodurch der globale Speicher
nichtlinear partitioniert werde. Auch der Austausch der Adressen der jeweils alloziierten Speicherbereiche untereinander sei nicht entnehmbar. In der Anmeldung
erfolge der Speicherzugriff auf Hardwareebene ohne Zwischenschaltung der virtuellen Ebene.
Der globale virtuelle Speicher in Druckschrift D1 (WO 2005/106659 A1) sei im
Unterschied zum beanspruchten Gegenstand vollständig linear adressiert und es

                                       - 10 -



erfolge eine mehrfache Virtualisierung. Die Speicherverwaltung der einzelnen globalen Speicherbereiche erfolge ausschließlich auf der virtuellen Ebene über einen
zentralen Verwalter. Die Adressen der jeweils alloziierten Speicherbereiche würden nicht ausgetauscht, die Microkernel verfügten nicht über physikalische Adressen zum Austausch. Beim Speicherzugriff sei der Distributed Virtual Machine
Monitor DVMM immer zwischengeschaltet.            Entfernter Direktspeicherzugriff
(RDMA) sei zwar möglich, aber nie als unmittelbarer Zugriff ohne Zwischenschaltung des Distributed Virtual Machine Monitor DVMM.
Auch in Druckschrift D2 (US 2004/37319 A1) sei die virtuelle Ebene immer zwischengeschaltet (Fig. 7).




                                         II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie ist jedoch nicht begründet, denn die Gegenstände der Patentansprüche 1
und 11 in der Fassung des Hauptantrags und die Gegenstände der Patentansprüche 1 und 10 in der Fassung des Hilfsantrags beruhen nicht auf einer erfinderischen Tätigkeit (§ 4 PatG).


1.   Die Anmeldung betrifft ein Netzwerksystem und ein Verfahren zur Steuerung
verteilter Speicher.
In der Beschreibungseinleitung wird aufgeführt, die vorliegende Anmeldung betreffe die Zugriffsteuerung im Rahmen entfernter Direktspeicherzugriffe (RDMA:
remote direct memory access) auf in einem Netzwerksystem in Netzelementen
verteilt angeordnete, virtuelle Speicher bei parallelem, verteiltem Computing sowie
die Speicherorganisation, bei der die verteilten Speicher vereinigt würden. Die virtuellen Speicher würden unter einer logischen Adresse angesprochen, über die in
Verbindung mit der Länge ein Speicherbereich adressiert werden könne.
Unter einer Maschine werde in der Anmeldung alternativ ein Programm oder Hardware verstanden, welche wie eine technische Maschine agiere und eine bestimm-

                                       - 11 -



te Aufgabe löse. Eine Instanz einer derartigen Maschine sei ein Programmbestandteil zur Lösung einer bestimmten Aufgabe.
Der Zugriff auf einzelne lokale Speicherstellen innerhalb eines Netzwerkelements
erfolge auf der Basis lokaler reeller Adressen.
Es sei bekannt, beispielsweise über „Infiniband“ entfernte über Netzwerkverbindungen verbundene Speicherbereiche mit hohen Bandbreiten anzusprechen.
„Infiniband“ nutze PC-Erweiterungskarten, die über eine Direktspeicherzugriff-Hardware lokale Speicherbereiche über das Netzwerk lesen und schreiben können. Dadurch sei möglich, einzelne Recheneinheiten, z. B. mit mehreren Multicore-Prozessoren, statt über herkömmliche Busverbindungen über Netzwerkverbindungen miteinander zu verknüpfen und dadurch eine schwach gekoppelte, verteilte Speicher-Topologie (distributed memory system) zu schaffen. In einem solchen Falle sei eine Adressumrechnung der lokalen virtuellen Adressen in nutzbare
physikalische Adressen erforderlich, die üblicherweise durch das Betriebssystem
erfolge, da nach dem Stand der Technik hierzu die gesamte Hardware einer
Recheneinheit durch das Betriebssystem virtualisiert und dem Anwender über
eine Software-Schnittstelle zur Verfügung gestellt werde. Der Zugriff einer Anwendung auf einen entfernten Speicherbereich erfolge mit Hilfe von Kommunikationsbibliotheken, d. h. spezieller Kommunikationsspeicher.
Bei Infiniband könne ein derartiger Speicherzugriff lediglich zwischen einzelnen
Kommunikationspaaren von jeweils zwei Recheneinheiten durchgeführt werden,
erfordere eine Vielzahl von Kommunikationsverbindungen und Abstimmungen zwischen den beteiligten Recheneinheiten sowie Kommunikationsspeichern und die
Rechenwerke der Recheneinheiten seien selbst in den Datenaustausch involviert.
Nachteilig sei weiterhin, dass bei diesem Vorgehen eine kollektive Operation einer
Vielzahl von Recheneinheiten zu aufwändig in der Organisation und eine globale
Speicherkonsistenz nicht gewährleistet seien (S. 1 Abs. 1 bis S. 5 Abs. 1 der
Anmeldeunterlagen).


Als objektive Aufgabenstellung wird seitens des Senats angesehen, den direkten
Speicherzugriff (RDMA) eines Netzelementes eines Netzwerksystems auf die über

                                         - 12 -



die Netzelemente verteilt angeordneten globalen Speicherbereiche einer virtuellen
Maschine effizient zu gestalten.


Als Fachmann, der mit der Lösung einer solchen Aufgabenstellung betraut wird,
wird ein Diplomingenieur (Universität) angesehen, der mehrjährige Berufserfahrung auf dem Gebiet des schnellen Speicherzugriffs bei Netzwerken mit schwach
gekoppelter Speichertopologie besitzt.


Als Lösung der Aufgabenstellung wird gemäß Hauptantrag angegeben, bei einem
Netzwerksystem mit einer Vielzahl über Netzwerkverbindungen verbundener Netzelemente auf jedem Netzelement eine Instanz (VM-Instanz) einer virtuellen Maschine (VM) zu installieren, die nach deren Installation einen Teil des in dem Netzelement angeordneten lokalen Speichers als globalen VM-Speicherbereich festlegt, auf den alle VM-Instanzen Zugriffsrechte besitzen. Jeder Speicherstelle im
VM-Speicherbereich wird eine für alle VM-Instanzen einheitliche globale Adresse
zugeordnet, die aus einer Adresse des Netzelementes‚ in dem der lokale VM-Speicherbereich angeordnet ist, und einer lokalen realen Adresse auf diesem
Netzelement besteht. Alle VM-Instanzen tauschen die globalen Adressen/Adressbereiche ihrer jeweils alloziierten VM-Speicherbereiche untereinander aus. Dadurch kann bei Fernzugriff einer lokal laufenden VM-Instanz auf die globale
Adresse einer physikalischen Speicherstelle eines entfernten Netzelementes die
zugehörige lokale reale Adresse des globalen VM-Speicherbereichs in der lokal
laufenden VM-Instanz ermittelt werden und ein unmittelbarer Aufruf mit Quell- und
Zieladresse für den RDMA ausgelöst werden.


Mit dem Hilfsantrag wird zusätzlich beansprucht, dass durch die VM-Instanzen
neben dem virtuellen Speicherbereich jeweils ein Cache-Speicherbereich in dem
lokalen Speicher festgelegt wird. Die mehreren Cache-Speicherbereiche bilden
zusammen einen globalen, über die lokalen Speicherbereiche verteilten VM-Cache-Speicherbereich, der von der virtuellen Maschine verwaltet und kontrolliert
wird.

                                        - 13 -



2.   Der Gegenstand des Patentanspruchs 1 und 11 in der Fassung des Hauptantrags sowie der Gegenstand des Patentanspruchs 1 und 10 in der Fassung des
Hilfsantrags beruhen nicht auf erfinderischer Tätigkeit.


Von Bedeutung für die Beurteilung der Patentfähigkeit der beanspruchten Gegenstände ist die im Prüfungsverfahren genannte, vorveröffentlichte Druckschrift


D1: WO 2005/106659 A1


sowie die im Beschwerdeverfahren mit Ladungszusatz eingeführte vorveröffentlichte Druckschrift


D2: US 2004/37319 A1.


2.1 Der Gegenstand des Patentanspruchs 1 in der Fassung des Hauptantrags
beruht für den Fachmann nicht auf erfinderischer Tätigkeit.


Druckschrift D1 bezieht sich auf ein Netzwerksystem mit einer Vielzahl über Netzwerkverbindungen verbundener Netzelemente, bei dem jedes der Netzelemente
mindestens einen Speicher sowie eine Netzwerkschnittstelle (I/O module) aufweist
(S. 56 le. Abs. - S. 57 Abs. 1, Fig. 9). Die Fähigkeit zum direkten Speicherzugriff
(RDMA) ergibt sich z. B. aus S. 44 Abs. 4, S. 53 Abs. 2 und der Anwendung von
Infiniband (z. B. S. 53 Abs. 3 Satz 1) (Merkmal a).
Auf jedem Netzelement läuft eine Instanz (Distributed Virtual Machine Monitor
DVMM mit den Bestandteilen Microkernel und Management Agent) einer virtuellen
Maschine (Virtual Machine Architektur VMA) (S. 13 le. Abs. - S. 14 Abs. 2, Fig. 2,
8) (Merkmal b).
Nach der Installation der VM-Instanzen auf den einzelnen Netzelementen (während der Boot-Phase: S. 24 vorletzte und letzte Zeile, oder nach dem Restart:
S. 19 Z. 11 f.) bestimmt die Instanz (Distributed Virtual Machine Monitor DVMM
mit Microkernel) zumindest einen Teil des Speichers in dem Netzelement als glo-

                                       - 14 -



balen VM-Speicherbereich 602 (Fig. 6, S. 15 Z. 8-10, S. 42 Abs. 4, S. 43 Z. 7f.),
wobei jede der VM-Instanzen Zugriffsrechte hierauf besitzt (S. 42 le. Abs.) (Merkmale c, c´). Jeder Speicherstelle im VM-Speicherbereich wird eine für alle VM-Instanzen der virtuellen Maschine einheitliche globale Adresse zugeordnet (S. 44
Abs. 2) (Merkmal d), bei der es sich um eine virtuelle Adresse handelt.
Sämtliche VM-Instanzen tauschen (mit Hilfe des Management Agents als Bestandteil des Distributed Virtual Machine Monitor DVMM) die eigenen Konfigurationsdaten untereinander aus (S. 18 Abs. 3 Satz 1, S. 22 Abs. 2, S. 25 le. Abs. -
S. 26 Abs. 2), wozu die globalen Adressbereiche ihrer jeweiligen alloziierten VM-Speicherbereiche gehören (S. 51 Abs. 4), wobei die Konfigurationsinformation
dem Microkernel des Distributed Virtual Machine Monitor DVMM zugeleitet wird
(S. 17 Z. 10-13) (Merkmal f). Im Falle der dynamischen Anpassung der Ressourcen kann ein Managementserverprogramm den Austausch der erforderlichen Konfigurationsdaten anstoßen (S. 15 Abs. 3). Das Managementserverprogramm kann
aber auch in den einzelnen Nodes verteilt angeordnet sein (S. 18 Abs. 1, S. 20
Z. 9 von unten bis Z. 5 von unten), so dass dann von jedem einzelnen Node der
Austausch der Konfigurationsdaten bewirkt wird (S. 23 Z. 9-11).
Die Speicherverwaltung erfolgt ebenfalls dezentral über das Distributed Shared
Memory DSM in Verbindung mit dem Distributed Memory Manager DMM (S. 53
Z. 4-6). Hierfür befindet sich das Distributed Shared Memory (DSM 816 in Fig. 8)
in jeder Instanz (DVMM) als Support, das bei Zugriffswunsch einer Anwendung
einen entfernten direkten Speicherzugriff ermöglicht (RDMA) (S. 44 Abs. 4, S. 53
Abs. 2), und das die für den direkten Speicherzugriff erforderliche Adressübersetzung von der virtuellen in die reale Adresse vornimmt (S. 52 letzter seitenübergreifender Satz), wozu die Zuordnung von virtuellen zu realen Adressen aller Speicherbereiche erforderlich ist und neben dem Austausch der virtuellen Adressen
auch den Austausch der realen Adressen erfordert (S. 51 Abs. 2 Satz 1 und
Abs. 4 Satz 1 und 2). Es gehört zum Grundlagenwissen des Fachmanns, dass das
direkte Ansprechen einer realen Speicherstelle über deren reale Adresse erfolgt
und sich die reale Adresse einer Speicherstelle des globalen Speicherbereichs
aus der Adresse des Netzelementes, in dem sich der anzusprechende Speicher-

                                        - 15 -



bereich befindet, sowie der lokalen realen Adresse der Speicherstelle im jeweiligen Speicherbereich zusammensetzt (S. 51 Abs. 4 Satz 1 f.) (teilweise Merkmal e), und damit das unmittelbare Ansprechen eines globalen Speicherbereichs
im Rahmen eines direkten Speicherzugriffs (RDMA) über eine derart zweiteilige
Adresse erfolgt. Der Fachmann entnimmt Druckschrift D1, dass mittels der lokal
laufenden VM-Instanz mindestens eines der Netzelemente beim direkten Zugriff
auf die globale Adresse einer sich auf einem weiteren, entfernten Netzelement
befindenden physikalischen Speicherstelle die zugehörige lokale reale Adresse
auf dem entfernten Netzelement berechnet und ein RDMA-Aufruf mit Quell- und
Zieladresse initiiert wird sowie auf den globalen VM-Speicherbereich des entfernten Netzelements zugegriffen wird (S. 44 Abs. 4, S. 52 letzter seitenübergreifender
Satz, S. 53 Abs. 2) (Merkmal g).
Im Unterschied zu Druckschrift D1 werden gemäß Merkmal e die globalen VM-Speicherbereiche nicht mit einer linearen virtuellen Adresse versehen, sondern die
realen Adressen genutzt, die sich bekannterweise aus der Adresse des Netzelementes sowie der lokalen realen Adresse der Speicherstelle des jeweiligen Speicherbereichs zusammensetzen.
Es liegt jedoch im Bereich des Wissens des Fachmanns, dass Speicherbereiche
(alternativ zu Druckschrift D1) auch real adressiert werden können. Denn es
gehört zum Grundwissen des Fachmanns, dass bei der Adressierung eines verteilt
angeordneten Speichers Alternativen zur Verfügung stehen, die jeweils bekannte
Vor- und Nachteile aufweisen. Der Fachmann kann den Speicher zum einen (wie
in Druckschrift D1) virtuell adressieren, um einen linearen Adressraum zu schaffen, dann ist jedoch eine Übersetzung der virtuellen in reale Adressen erforderlich.
Zum anderen kann der Speicher real adressiert werden, hierfür ist keine Adressübersetzung erforderlich, jedoch existiert dann kein linearer Adressraum.
Für die Auswahl einer der beiden ihm bekannten Möglichkeiten unter Abwägen
der jeweiligen Vor- und Nachteile und unter Inkaufnahme der entsprechenden
Nachteile ist kein erfinderisches Zutun erforderlich.

                                        - 16 -



Die von der Anmelderin geltend gemachten Unterschiede der beanspruchten
Lehre zu der aus Druckschrift D1 entnehmbaren resultieren durch die in Druckschrift D1 verwendete virtuelle Adressierung der globalen Speicherbereiche. Bei
alternativer Verwendung der realen Adressierung ergibt sich das unmittelbare
Ansprechen der globalen Speicherbereiche über eine aus der physikalischen
Adresse des Netzelementes und der realen Speicheradresse bestehende zweiteilige Adresse und der erforderliche Austausch nur der realen Adressen der jeweils
alloziierten Speicherbereiche unmittelbar.
Auch die Argumentation der Anmelderin, der Speicherzugriff erfolge ohne Zwischenschaltung der virtuellen Ebene ausschließlich auf Hardwareebene, greift
nicht. Denn in der Anmeldung wird davon ausgegangen, dass mittels der lokal laufenden VM-Instanz mindestens eines der Netzelemente beim Zugriff auf die globale Adresse einer sich auf einem weiteren, entfernten Netzelement befindenden
physikalischen Speicherstelle die zugehörige lokale reale Adresse des entfernten
Netzelementes berechnet wird (Merkmal g des Anspruchs 1, S. 6 Z. 10-15, S. 7
Abs. 3, S. 12 le. Abs., S. 16 Z. 1-6 der Anmeldeunterlagen). Damit ist beim Speicherzugriff die VM-Instanz sowohl bei der beanspruchten Lehre als auch in Druckschrift D1 (Distributed Virtual Machine Monitor DVMM als VM-Instanz) immer
beteiligt. Es wird weder beansprucht noch in der Anmeldung wegen des hohen
Abstraktionsniveaus offenbart, wie der hierbei stattfindende Ablauf innerhalb der
VM-Instanz erfolgt.


Es bedurfte für den Fachmann somit lediglich fachgemäßen Zutuns, in Kenntnis
der Druckschrift D1 zu einem Netzwerksystem mit sämtlichen Merkmalen des
Anspruchs 1 in der Fassung des Hauptantrags zu gelangen.


Die Ausführungen zum Patentanspruch 1 in der Fassung des Hauptantrags gelten
sinngemäß auch für den Patentanspruch 11 in der Fassung des Hauptantrags.


2.2 Der Gegenstand des Patentanspruchs 1 in der Fassung des Hilfsantrags
beruht ebenfalls nicht auf erfinderischer Tätigkeit.

                                        - 17 -



Der Patentanspruch 1 in der Fassung des Hilfsantrags basiert auf dem Patentanspruch 1 in der Fassung des Hauptantrags. Er unterscheidet sich von diesem
durch die zusätzliche Aufnahme der Merkmale h und i, wonach mehrere VM-Instanzen verschiedener Netzelemente jeweils einen Cache-Speicherbereich in
dem Speicher ihres Netzelementes vorsehen zum Zwischenspeichern von aus
dem VM-Speicherbereich angeforderten oder anzufordernden Daten und wobei
die mehreren Cache-Speicherbereiche zusammen einen globalen, über lokale
Speicherbereiche verteilten VM-Cache-Speicherbereich ausbilden, welcher von
der virtuellen Maschine verwaltet und kontrolliert wird.


Die VM-Instanzen (Distributed Virtual Machine Monitor DVMM) der verschiedenen
Netzelemente der Druckschrift D1 sehen ebenfalls jeweils einen virtuellen Cache-Speicherbereich in dem Speicher ihres Netzelementes zum Zwischenspeichern
von aus dem globalen VM-Speicher angeforderten oder anzufordernden Daten vor
(S. 54 Abs. 3 Satz 1) (Merkmal h).
In Druckschrift D1 wird ein globaler VM-Cache-Speicherbereich nicht explizit genannt. Der Fachmann wird den Cache jedoch in analoger Weise zum verteilt
angeordneten globalen VM-Speicher (Fig. 6, S. 43 Abs. 2) organisieren, und damit
einen aus den einzelnen Cache-Speicherbereichen bestehenden globalen, über
die lokalen Speicherbereiche verteilt angeordneten VM-Cache-Speicherbereich
schaffen, der von der virtuellen Maschine verwaltet und kontrolliert wird (Merkmal i).
Eine Anregung hierzu findet der Fachmann beispielsweise in Druckschrift D2.
Denn Druckschrift D2 bezieht sich ebenfalls auf ein Netzwerksystem mit einer
Vielzahl über Netzwerkverbindungen verbundener Netzelemente, die einen Speicher sowie eine Direktspeicherzugriff (DMA) -fähige Netzwerkschnittstelle zum
RDMA aufweist und die Virtualisierung erlaubt (Abs. [0014], [0067], [0098], Fig. 7)
und mittels der lokal laufenden Instanz mindestens eines der Netzelemente beim
Zugriff auf die globale Adresse einer sich auf einem weiteren, entfernten Netzelement befindenden physikalischen Speicherstelle die zugehörige lokale reale
Adresse auf dem entfernten Netzelement berechnet und ein DMA-Aufruf mit Quell-

                                       - 18 -



und Zieladresse initiiert wird sowie auf den globalen VM-Speicherbereich des entfernten Netzelements zugegriffen wird (Abs. [0112], [0121], [0124]).
Neben einem globalen Speicher (S. 8 Sp. 1 Z. 25-30) sind lokale Cache-Speicherbereiche vorgesehen (Abs. [0111], [0128]), die einen globalen Cache-Speicherbereich bilden (S. 16 Sp. 2 Z. 9-28) (Merkmale h, i).


Damit können die im Anspruch 1 in der Fassung des Hilfsantrags zusätzlich aufgenommenen Merkmale erfinderische Tätigkeit nicht begründen.


Die Ausführungen zum Patentanspruch 1 in der Fassung des Hilfsantrags gelten
entsprechend ebenfalls zum Patentanspruch 10 in der Fassung des Hilfsantrags.


3.   Die Gegenstände der Ansprüche 1 und 11 in der Fassung des Hauptantrags
sowie der Ansprüche 1 und 10 in der Fassung des Hilfsantrags sind somit nicht
patentfähig. Mit den Ansprüchen 1 und 11 in der Fassung des Hauptantrags sowie
den Ansprüchen 1 und 10 in der Fassung des Hilfsantrags fallen notwendigerweise auch die jeweils darauf rückbezogenen Unteransprüche, zumal die Unteransprüche lediglich fachgemäße Ausgestaltungen beinhalten und dafür auch keine
erfinderische Besonderheit geltend gemacht wurde.




Dr. Fritsch                  Eder               Baumgardt              Wickborn




                                                                              Fa
