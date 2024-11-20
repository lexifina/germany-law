---
ecli: "ECLI:DE:BPatG:2024:201124U5Ni47.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "5"
aktenzeichen: "5 Ni 47/21"
decided: "2024-11-20"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=23&nr=44427&anz=391&pos=345&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-11-20_5_Ni_47_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 5 Ni 47/21 vom 2024-11-20

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
5 Ni 47/21 (EP)
(Aktenzeichen)




                      In der Patentnichtigkeitssache


…




ECLI:DE:BPatG:2024:201124U5Ni47.21EP.0

                                       -2-



               betreffend das europäische Patent EP 3 474 498
                              (DE 60 2007 060 445)


hat der 5. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 20. November 2024 durch den Richter Heimen als
Vorsitzenden sowie die Richter Dipl.-Phys. Univ. Bieringer, Schödel, Dr.-Ing. Ball
und Dipl.-Ing. Jürgensen


für Recht erkannt:


      I.     Das europäische Patent EP 3 474 498 wird mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


      II.    Die Beklagte trägt die Kosten des Rechtsstreits.


      III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des
             jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.




                                Tatbestand


Die Beklagte ist Inhaberin des europäischen Patents 3 474 498 (Streitpatent – SP).
Es beruht auf einer Teilung der europäischen Anmeldung EP 17185828.5, welche
eine Teilung der europäischen Stammanmeldung EP 07827358.8 ist, die international als israelische PCT-Anmeldung PCT/IL2007/001385 am 12. November
2007 angemeldet und als WO 2008/059484 A2 am 22. Mai 2008 veröffentlicht
wurde. Es nimmt die Prioritäten der Anmeldungen US 11/559,037 vom 13.
November 2006 und US 11/778,286 vom 16. Juli 2007 in Anspruch. Die Erteilung
des Streitpatents ist am 8. Juli 2020 veröffentlicht worden. Das in englischer
Sprache gefasste Streitpatent trägt die Bezeichnung “HASH-BASED MULTI-HOMING“, ins Deutsche übersetzt “HASH-BASIERTES MULTIHOMING”. Es ist in

                                                  -3-



Kraft und umfasst in der geltenden Fassung insgesamt 19 Patentansprüche mit dem
Vorrichtungsanspruch 1 und den auf diesen unmittelbar oder mittelbar zurückbezogenen Unteransprüchen 2 bis 19.
Mit ihrer Klage begehrt die Klägerin die vollständige Nichtigerklärung des Streitpatents.


Der Patentanspruch 1 der geltenden Fassung lässt sich gemäß Streitpatentschrift
wie folgt gliedern:


 Merkmal   Patentanspruch 1 lt. Streitpatent in           Dt. Übers. lt. Streitpatent
           englischer Sprache

 M1        A system for providing alternative             System zum Bereitstellen alternativer
           communication paths between nodes, the         Kommunikationspfade zwischen
           system comprising:                             Knoten, wobei das System umfasst:
 M1.1      first (24) and second (28) Ethernet            ersten (24) und zweiten (28) Ethernetswitches;                                      Schalter;
 M1.2      a third Ethernet switch (36A) connected        einen dritten Ethernet-Schalter (36A), der
           between the first and second Ethernet          zwischen dem ersten und zweiten Ethernetswitches as part of a Layernetwork; and     Schalter angeschlossen ist als Teil eines
                                                          Layer-2 Netzwerks; und
 M1.3      a fourth Ethernet switch (36B) connected       ein vierter Ethernet-Schalter (388), der
           between the first and second Ethernet          zwischen dem ersten und zweiten Ethernetswitches as part of the Layernetwork        Schalter als Teil des Layer-2 Netzwerks
                                                          angeschlossen ist,
           characterized in that                          gekennzeichnet dadurch, dass
 M1.4      the alternative communication paths are        die alternativen Kommunikationspfade
           Layercommunication paths and the first      Layer-2 Kommunikationspfade sind, und der
           Ethernet switch (24) is operative for          erste Ethernet-Schalter (24) betriebsbereit ist
           transmitting Ethernet frames having a          zum Übertragen von Ethernet-Rahmen mit
           destination address of the second Ethernet     einer Zieladresse des zweiten Ethernetswitch,                                        Schalters;
 M1.4.1    wherein a first group of the Ethernet frames   wobei eine erste Gruppe der Ethernetare carried only over a first communication    Rahmen nur über einen ersten
           path from the first Ethernet switch to the     Kommunikationspfad von dem ersten
           second Ethernet via the third Ethernet         Ethernet-Schalter zu dem zweiten Ethernet
           switch, and                                    über den dritten Ethernet-Schalter getragen
                                                          wird, und

                                             -4-



M1.4.2    wherein a second group of the frames that      wobei eine zweite Gruppe der Rahmen, die
          is non-overlapping with the first group are    sich nicht mit der ersten Gruppe
          carried only over a second communication       überschneidet, nur über einen zweiten
          path that is different from the first          Kommunikationspfad übertragen wird, der
          communication path from the first Ethernet     unterschiedlich ist von dem ersten
          switch to the second Ethernet switch via the   Kommunikationspfad des ersten Ethernetfourth Ethernet switch, and                    Schalters zu dem zweiten Ethernet-Schalter
                                                         über den vierten Ethernet-Schalter, und
M1.4.3    wherein the Ethernet frames are assigned to    wobei die Ethernet-Rahmen zugeteilt sind,
          be carried over the first and second           um über den ersten und zweiten
          communication paths based on the               Kommunikationspfad getragen zu werden,
          respective results of a hashing function       basierend auf den jeweiligen Ergebnissen
          applied to their respective header values in   einer Hash-Funktion, die auf ihre jeweiligen
          an header field.                               Header-Werte in einem Header-Feld
                                                         angewendet wird.



Wegen des Wortlauts der abhängigen Unteransprüche 2 bis 19 wird auf das
Streitpatent verwiesen.


Die Klägerin macht die Nichtigkeitsgründe der unzulässigen Erweiterung (Art. II § 6
Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 Buchst. c) i. V. m. Art. 123 EPÜ) sowie der
mangelnden Neuheit und der mangelnden erfinderischen Tätigkeit (Art. II § 6 Abs.
1 Nr. 1 IntPatÜG, Art. 138 Abs. 1 Buchst. a) i. V. m. Art. 54, 56 EPÜ) geltend. Sie
ist ferner der Ansicht, dass das Streitpatent die beiden Prioritäten nicht wirksam in
Anspruch nehme.


Die Klägerin stützt ihren Vortrag u. a. auf folgende Unterlagen:


     D1                      US 2003/0223424 A1;
     D2                      extreme networks, ExtremeWare User Guide,
                             Software Version 7.5, Oktober 2005;
     D3                      US 2002/0156918 A1;
     D4                      US 2007/0248092 A1;
     D5                      Tanenbaum, A. S., Computernetzwerk, 3.
                             revidierte Auflage, 2000;

                                         -5-



     D6                    WO 2005/099183 A1;
     NK2a                  US 11/559,037 (Prioritätsdokument 1);
     NK2b                  US 11/778,286 (Prioritätsdokument 2);
     NK3a                  Streitpatent (SP) - EP 3474498 B1;
     NK6                   Offenlegungsschrift WO 2008/059484 A2
                           (Stammanmeldung);
     NK10                  Archivdaten der „Wayback Machine“ zum
                           ExtremeWare User Guide;
     NK11                  USPTO Auszug zu den Assignment-Daten der
                           11/559,037;
     NK12                  Tanenbaum, Feamster, Wetherall, Computer
                           Networks, 6th Edition, 2020;
     NK13                  USPTO, MANUAL OF PATENT EXAMINING
                           PROCEDURE (MPEP), Chapter 300 Ownership
                           and Assignment, Rev. 10.2019, June 2020;
     NK14                  Wikipedia-Artikel "Fibre Channel".


Die Beklagte hat mit Schriftsatz vom 13. September 2024 zur hilfsweisen
Verteidigung des Streitpatents neun und in der mündlichen Verhandlung weitere
zwei Hilfsanträge (1 bis 9 bzw. 4a und 4b) eingereicht.


Der Patentanspruch 1 gemäß Hilfsantrag 1 unterscheidet sich vom Patentanspruch 1 gemäß Hauptantrag dadurch, dass im Merkmal M1.4.2 am Schluss die
Konjunktion „and“ gestrichen sowie nach dem Merkmal M1.4.3 folgendes neues
Merkmal M1.4.4_Hi1 hinzugefügt wird:


      M1.4.4_Hi1: and wherein the header field comprises a Media Access
                    Control, MAC, address.


Der Patentanspruch 1 gemäß Hilfsantrag 2 ist gegenüber dem erteilten Patentanspruch 1 durch die Hinzufügung der Worte „load balancing and/or failure

                                         -6-



protection by“ modifiziert. Das geänderte Merkmal M1_Hi2 lautet (die Abweichung
zum Hauptantrag ist hervorgehoben):


      M1_Hi2:       A system for load balancing and/or failure protection by
                    providing alternative communication paths between nodes, the
                    system comprising:


Der Patentanspruch 1 gemäß Hilfsantrag 3 enthält das modifizierte Merkmal
M1_Hi2 gemäß Hilfsantrag 2 und streicht die Konjunktion „and“ im Merkmal M1.4.2
entsprechend Hilfsantrag 1. Er unterscheidet sich von dem erteilten Patentanspruch
1 ferner dadurch, dass nach dem Merkmal M1.4.3 folgendes Merkmal M1.4.4_Hi3
hinzugefügt wird:


      M1.4.4_Hi3: and wherein the first and second communication paths between
                    the first and second switches are used for protection against
                    failures or for providing traffic load balancing.


Der Patentanspruch 1 gemäß Hilfsantrag 4 unterscheidet sich von Patentanspruch 1 gemäß Hilfsantrag 3 dadurch, dass nach dem Merkmal M1.4.3 anstelle
des Merkmals M1.4.4_Hi3 das Merkmal M1.4.4_Hi4 hinzugefügt wird. Dieses lautet:


      M1.4.4_Hi4: and wherein the third and fourth Ethernet switches are
                    configured for Layerswitching of Ethernet frames using
                    respective Media Access Control, MAC, tables.


Der Patentanspruch 1 nach Hilfsantrag 4a enthält gegenüber dem Patentanspruch 1 gemäß Hauptantrag das geänderte Merkmal M1.4.2_Hi1 mit dem
editoriellen Streichen der Konjunktion „and“ sowie das neu hinzugekommene
Merkmal M1.4.4_Hi4a (Änderung gegenüber Hilfsantrag 4 hervorgehoben):

                                         -7-



     M1.4.4_Hi4a: and wherein the third and fourth Ethernet switches are
     configured for Layerswitching of said Ethernet frames using
     respective Media Access Control, MAC, tables.


Der Patentanspruch 1 nach Hilfsantrag 4b enthält gegenüber dem Patentanspruch 1 gemäß Hauptantrag das geänderte Merkmal M1.4_Hi4b, das geänderte
Merkmal M1.4.2_Hi1 mit dem editoriellen Streichen der Konjunktion „and“, das aus
Hilfsantrag 4a bereits bekannte Merkmal M1.4.4_Hi4a sowie das geänderte
Merkmal M1.4_Hi4b (Änderungen hervorgehoben):


     M1.4_Hi4b:    the     alternative   communication   paths   are   Layercommunication paths and the first Ethernet switch (24) is operative for
     receiving and transmitting Ethernet frames having a destination address
     of the second Ethernet switch,


Der Patentanspruch 1 gemäß Hilfsantrag 5 wird gegenüber dem erteilten Patentanspruch 1 dahingehend geändert, dass die Änderungen nach den Hilfsanträgen 3
und 4 kombiniert werden.


Der Patentanspruch 1 gemäß Hilfsantrag 6 wird gegenüber dem erteilten Patentanspruch 1 dahingehend geändert, dass die Änderungen nach den Hilfsanträgen 1
und 2 kombiniert werden.


Der Patentanspruch 1 gemäß Hilfsantrag 7 wird gegenüber dem erteilten Patentanspruch 1 dahingehend geändert, dass die Änderungen nach den Hilfsanträgen 1
und 3 kombiniert werden.


Der Patentanspruch 1 gemäß Hilfsantrag 8 wird gegenüber dem erteilten Patentanspruch 1 dahingehend geändert, dass die Änderungen nach den Hilfsanträgen 1
und 4 kombiniert werden.

                                         -8-



Der Patentanspruch 1 gemäß Hilfsantrag 9 wird gegenüber dem erteilten Patentanspruch 1 dahingehend geändert, dass die Änderungen nach den Hilfsanträgen 1,
3 und 4 kombiniert werden.


Wegen des Wortlauts der unmittelbar und mittelbar rückbezogenen Unteransprüche
der Hilfsanträge wird auf die Akte verwiesen.


Der Senat hat den Parteien am 29. Juli 2024 einen qualifizierten Hinweis erteilt. In
der mündlichen Verhandlung am 20. November 2024 hat der Senat einen weiteren
Hinweis erteilt.




Die Klägerin beantragt,



       das europäische Patent EP 3 474 498 mit Wirkung für das Hoheitsgebiet
       der Bundesrepublik Deutschland in vollem Umfang für nichtig zu erklären.




Die Beklagte beantragt,



       die Klage abzuweisen,

       hilfsweise die Klage mit der Maßgabe abzuweisen, dass das Streitpatent
       die Fassung eines der Hilfsanträge 1 bis 9, eingereicht mit Schriftsatz vom
       13. September 2024, bzw. der Hilfsanträge 4a und 4b, eingereicht in der
       mündlichen Verhandlung, erhält.


Die Beklagte verteidigt das Streitpatent in der erteilten Fassung und tritt der Klage
in allen Punkten entgegen. Insbesondere ist sie der Auffassung, dass das
Streitpatent die Prioritäten wirksam in Anspruch nehme. Sie bestreitet zudem mit

                                        -9-



Nichtwissen, dass die Druckschrift D2 vor dem Prioritätsdatum der Öffentlichkeit
tatsächlich zugänglich war.


Die Beklagte gibt an, dass die Ansprüche gemäß Hauptantrag einzeln bzw. isoliert
verteidigt werden, dass die Anspruchssätze nach den Hilfsanträgen als in sich
geschlossen gestellt sind und dass die Hilfsanträge in alphanumerischer Reihenfolge geprüft werden sollen.


Die Klägerin rügt die in der mündlichen Verhandlung gestellten Hilfsanträge 4a und
4b als verspätet.


Wegen der weiteren Einzelheiten des Vorbringens der Parteien wird auf die
zwischen den Parteien gewechselten Schriftsätze nebst Anlagen und den weiteren
Inhalt der Akte Bezug genommen.




                               Entscheidungsgründe


                                         A.


Die Klage ist zulässig und hat in der Sache Erfolg. Das Streitpatent erweist sich
sowohl nach dem Hauptantrag als auch nach allen Hilfsanträgen als nicht
rechtsbeständig und ist daher in vollem Umfang für nichtig zu erklären.
Der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag sowie den Hilfsanträgen 1 bis 9 geht jeweils über den Inhalt der Anmeldung in der ursprünglich
eingereichten Fassung gemäß Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs.
1 Buchst. c), Art. 123 EPÜ hinaus. Darüber hinaus gilt für den Hauptantrag sowie
für die Hilfsanträge 1 bis 4 und 5 bis 9 ebenfalls der geltend gemachte Nichtigkeitsgrund der mangelnden Patentfähigkeit des Gegenstandes des Patentanspruches 1

                                       - 10 -



gemäß Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52,
54, 56 EPÜ.



                     I.     Zum Gegenstand des Streitpatents


1.    Das Streitpatent EP 3 474 498 B1 (SP) mit dem Titel „HASH-BASIERTES
MULTIHOMING“ betrifft Kommunikationsnetzwerke und im Speziellen das
Kommunizieren über alternative Kommunikationspfade in Layer-2-Netzwerken (SP,
Titel und Abs. [0001]).


Das Aufsetzen und Verwenden von alternativen Kommunikationspfaden zwischen
Endpunkten in Layer-2-Netzwerken, um einen Fehlerschutz sowie ein Ausbalancieren der Verkehrslast („load balancing“) bereitzustellen, seien bereits aus
verschiedenen Netzwerkstandards von Standardisierungsorganisationen – wie
bspw. von IEEE oder auch ITU – bekannt, wozu bspw. die Link-Aggregation (LAG,
„link aggregation group“), Spannbaum-Protokolle (RSTP: „rapid spanning tree
protocol“; MSTP: „multiple spanning tree protocol“) und Ring-Netzwerke (RPR:
„Resilient Packet Ring“) zählten (SP, Abs. [0002] – [0006]).


Darüber hinaus sei ein Umschalten („switch-over“) zwischen alternativen Kommunikationspfaden bereits in verschiedenen Produkten auf dem Markt kommerziell
erhältlich, u.a. das „Ethernet Automatic Protection Switching“ (EAPS), das „Metro
Ring Protocol“ (MRP) sowie die „Fast Ring Solution“ (T-FRS) (SP, Abs. [0007]).


Schließlich zeige die US 2003/0223424 eine Mehrwegeverarbeitungsarchitektur
(„multipath processing architecture“), welche in einer Paketklassifikationsvorrichtung eines Netzwerkknotens implementiert sei (SP, Abs. [0008]).


Das Streitpatent stelle sich in diesem technischen Kontext die Aufgabe, die
Kommunikation zwischen zwei Endpunkten über ein Layer-2-Netzwerk mittels

                                        - 11 -



alternativer Kommunikationspfade zu verbessern, um eine schnelle, hinsichtlich der
Last ausbalancierte und geschützte bzw. sichere Kommunikation bereitzustellen
(SP, Abs. [0008]).


2.      Der Gegenstand des Streitpatents richtet sich an einen Ingenieur der Informatik bzw. Elektrotechnik/Informationstechnik mit abgeschlossenem Hochschulstudium und mit mehrjähriger Berufserfahrung in der Entwicklung von Netzwerkgeräten, wie bspw. Routern und Switches, wobei der Fachmann einschlägige
Kenntnisse     hinsichtlich   der   Netzwerkarchitektur   von    Lokalnetzen    bzw.
Weitverkehrsnetzen (LANs, WANs) sowie der zugrundeliegenden Netzwerkstandards, bspw. Ethernet (IEEE 802.3), aufweist.


3.    Der Senat legt dem Patentanspruch 1 und seinen Merkmalen folgendes
Verständnis zugrunde:


Mit dem Merkmal M1 ist ein System zur Bereitstellung alternativer Kommunikationspfade zwischen (Netzwerk-)Knoten beansprucht.


Das beanspruchte System weist folgende räumlich-körperliche Vorrichtungen auf:
-    einen ersten sowie einen zweiten Ethernet-Switch (Merkmal M1.1),
-    einen dritten sowie einen vierten Ethernet-Switch, die jeweils zwischen dem o.g.
     ersten und zweiten Ethernet-Switch angeordnet bzw. mit diesen verbunden sind
     und die jeweils Teil eines Layer-2-Netzwerks sind (Merkmale M1.2 und M1.3).


Unter einem Ethernet-Switch versteht der Fachmann im gegebenen technischen
Kontext ein Kopplungselement in einem Kommunikationsnetz, das verschiedene
Netzwerksegmente des gleichen Netzwerks miteinander verbindet und dafür sorgt,
dass die Datenrahmen, sogenannte „Frames“, anhand von Informationen aus dem
„Data Link Layer“ (Sicherungsschicht, Layer-2) des OSI-Modells an ihr Ziel
weitergeleitet werden. Ein Layer-2-Switch besitzt lediglich die Möglichkeit, Frames
von einem Port zum anderen zu schalten, wobei im Layerein Routing als typische

                                       - 12 -



Layer-3-Funktionalität nicht möglich ist und daher die verbundenen Geräte nur
innerhalb des gleichen Netzwerks interagieren können.


Gemäß Streitpatent, Figur 1 i.V.m. Absatz [0036], bilden die zwischengeschalteten
dritten und vierten Switches eine sogenannte „Multi-Homing-Group“ (MHG).


Das Streitpatent nennt als Netzwerk-Beispiel u.a. ein „virtual local area network“
(VLAN) bzw. Netzwerke, welche „Virtual Private LAN Services“ (VPLS)
unterstützen, (SP, Abs. [0012], [0041] – [0042]).


Gemäß Merkmal M1.4 werden Ethernet-Frames vom ersten zum zweiten Ethernet-Switch unter Verwendung der alternativen Kommunikationspfade übertragen, wobei
die im Header des Ethernet-Frames angegebene Zieladresse diejenige des zweiten
Ethernet-Switches sein soll. Der Fachmann erwartet aufgrund des verwendeten
Plurals beim Wortlaut „alternative Kommunikationspfade“ also zumindest zwei
unterschiedliche Pfade, wobei gemäß Merkmal M1.4.1 ein erster Pfad über den
dritten Ethernet-Switch und gemäß Merkmal M1.4.2 ein zweiter Pfad über den
vierten Ethernet-Switch verläuft. Eine erste Gruppe von Ethernet-Frames soll dabei
den ersten Pfad und eine disjunkte zweite Gruppe von Ethernet-Frames soll den
zweiten Pfad verwenden, so dass somit kein Ethernet-Frame über beide Pfade
zwischen den beiden „Endpunkten“ (jeweils von der Quelle bis zum Ziel) übertragen
wird.


Insoweit die Beklagte der Auffassung ist, dass der erste Knoten bzw. der erste
Ethernet-Switch kein „Endpunkt“ der Kommunikation darstelle und auch die
Beschreibung den ersten Knoten überhaupt nicht als Quelle benenne, überzeugt
das den Senat nicht. Denn das Streitpatent betrifft explizit lediglich die Layer-2
Kommunikation zwischen dem ersten und dem zweiten Knoten als sogenannte
„Endpunkte“ („endpoint“) der Kommunikation, wobei der erste Knoten mehrfach
auch als Quelle („source“) bezeichnet wird (vgl. SP, Abs. [0025], [0026], [0063],
[0065], [0070], [0072]). Im Übrigen verhält sich das Streitpatent zu einer

                                        - 13 -



anderweitigen Kommunikation bspw. betreffend einen dem ersten Knoten
vorgeschalteten Host als möglichen Ursprungsort der übermittelten Daten nicht.


Die der MHG zugehörigen Knoten 3 und 4, also der dritte und der vierte Ethernet-Switch, befinden sich stets auf den alternativen Kommunikationspfaden zwischen
den beiden „Endpunkten“ (vgl. SP, Abs. [0019], [0022], [0035], [0044] - [0045],
[0055], Unteranspruch 6). Gemäß Streitpatent, Absatz [0023], verlaufen die
alternativen Kommunikationspfade zwischen den „Endpunkten“ vollständig getrennt
voneinander und haben keinen Port, Link oder Knoten gemeinsam („Since the
member ports are distributed among different network nodes, the resulting set of
alternative communication paths has no single point of failure, i.e., no single port,
link or node that is common to all paths.“). Die Merkmale M1.4.1 und M1.4.2 fordern
dabei lediglich, dass kein Ethernet-Frame über beide Pfade am Ziel, d.h. dem
Knoten 2 bzw. dem zweiten Ethernet-Switch, ankommt. Dadurch wird jedoch nicht
ausgeschlossen, dass ein Ethernet-Frame vom Knoten 1 bzw. dem ersten Switch
sowohl zum dritten als auch zum vierten Switch gesendet wird. Der erste Knoten
versendet zumindest zu Beginn eines MAC-Lernprozesses Kopien bzw. Repliken
an beide zwischengeschalteten Switche, d.h. sowohl an den dritten als auch an den
vierten Switch, wobei aber nur ein einziger Switch der MHG das Paket zum Ziel
durchlässt und alle anderen Switche das Paket verwerfen („lnitially, the source node
broadcasts a frame addressed to the desired MAC address via all ports, in a process
commonly referred to as flooding. Replicas of the frame are received by all MHG
nodes, but only one of the MHG nodes forwards the frame via one of the MHG
member ports. The other MHG nodes discard the frame, in accordance with the
result of the hashing function.“, „Replicas of the flooded frame are received by all
MHG nodes, but only one of the MHG nodes forwards the frame via one of the MHG
member ports. The other MHG nodes discard the frame, in accordance with the
result of the hashing function.“, SP, Abs. [0025], [0064]).


Nach Abschluss des MAC-Lernprozesses und Empfangen eines entsprechenden
Feedback-Frames vom zweiten Switch versendet der erste Switch bzw. die Quelle

                                         - 14 -



weitere Frames jeweils nur noch über einen der beiden zwischengeschalteten
Switche in Abhängigkeit des jeweils pro Frame ausgewählten Übertragungswegs
(„From this stage, subsequent frames addressed to the same destination MAC
address are transmitted to only one of the MHG nodes - the one comprising the
selected MHG port.“, SP, Abs. [0026]).


Gemäß Merkmal M1.4.3 soll die Zuweisung eines Ethernet-Frames zu einem der
beiden alternativen Pfade unter Verwendung einer Hashing-Funktion erfolgen,
welche auf mindestens ein Header-Feld des Ethernet-Frames angewendet wird. Die
Hashing-Funktion wird basierend auf einem oder mehreren Header-Felder des
Frames berechnet („applying a hashing function to one or more of the header fields
at each of the two or more network nodes“, „applies a hashing function to certain
header fields of each frame it receives,“ SP, Abs. [0019], [0024]). Als Beispiele für
solche Header-Felder werden im Streitpatent u.a. ein „virtual circuit label“ (VC label),
eine VLAN-ID (VID), eine Service-ID (I-SID), eine VPLS-Kennung, eine MAC-Adresse oder eine IP-Adresse genannt (SP, Abs. [0041] – [0043] und Ansprüche 13
– 15). Merkmal M1.4.3 lässt dabei aber offen, in welchem Netzwerkknoten die
Hashing-Funktion ausgeführt wird.


Zwischen den Parteien ist strittig, ob das Hashing ebenfalls im ersten Knoten
durchgeführt werden kann. Der Wortlaut des Patentanspruchs 1 nennt nicht explizit,
an welcher Stelle die Hashing-Funktion ausgeführt wird, in seiner Breite lässt er
auch ein Hashing im ersten Knoten zu, so dass der Schutzbereich des Streitpatents
definitiv ein Hashing im ersten Knoten bzw. im ersten Ethernet-Switch umfasst.


Die Klägerin weist zutreffend darauf hin, dass dieses von der Beklagten geteilte
Verständnis des Anspruchswortlauts in der Beschreibung und den Zeichnungen
keinen Niederschlag gefunden hat. Vielmehr zeigen die Beschreibung und die
Zeichnungen sowie sämtliche Ausführungsbeispiele, ohne in Widerspruch zum
Wortlaut des Anspruchs zu stehen, dass sowohl der erste Ethernet-Switch bzw.
erste Source-Knoten als auch der zweite Ethernet-Switch bzw. zweite Destinations-

                                        - 15 -



Knoten jeweils als „Endpunkte“ der Kommunikation dienen, zwischen denen jeweils
die weiteren Knoten der MHG angeordnet sind (SP, Abs. [0017], [0019], [0022],
[0034]).


Die Beschreibung und die Zeichnungen sind zwar nach Art. 69 I 2 EPÜ zur Auslegung der Patentansprüche heranzuziehen, da diese der Erläuterung der Patentansprüche dienen. Ihre Heranziehung darf aber regelmäßig weder zu einer
inhaltlichen Erweiterung noch zu einer sachlichen Einengung des durch den Wortsinn des Patentanspruchs festgelegten Gegenstands führen (st. Rspr.: BGHZ 189,
330 – Okklusionsvorrichtung m.w.N.). Es gilt also der Grundsatz des Vorrangs des
Patentanspruchs gegenüber Beschreibung und Zeichnungen (BGH aaO.).


Die Hashing-Funktion wird gemäß Beschreibung, insbesondere den Ausführungsbeispielen, ausschließlich in den der MHG-Gruppe 44 zugehörigen Switches 36a –
36c, d.h. in den anspruchsgemäßen dritten und vierten Switches bzw. ggf. noch in
einem mit dem Knoten 36c assoziierten Host 48 ausgeführt, wobei jeder einzelne
der Switches entscheidet, das Paket weiterzuleiten oder zu verwerfen (SP, Fig. 1
und Abs. [0024], „Each MHG node (i.e., a node comprising an MHG member port)
applies a hashing function to certain header fields of each frame it receives, in order
to determine whether to forward or discard the frame. The hashing function is
defined so that each frame is forwarded via exactly one MHG member port and its
respective multi-homing path. All the other member ports discard the frame. All MHG
nodes use the same hashing function and apply the function to both incoming and
outgoing frames.“ sowie Abs. [0025], [0034] und [0046]). Lediglich ein einziger
Switch bzw. Knoten der MHG-Gruppe leitet ein Paket nach dem Anwenden der
Hashing-Funktion weiter, alle anderen verwerfen dieses („complementary hashing“,
SP, Abs. [0047]).


Im Übrigen würde gemäß SP, Absatz [0065], der erste Ethernet-Switch bzw. erste
Source-Knoten auch nach Abschluss des MAC-Lernprozesses noch kein Hashing

                                        - 16 -



durchführen, sondern die Auswahl eines der alternativen Pfade lediglich anhand
seiner dann gelernten MAC-Tabelle treffen.


Letztlich bleibt im Patentanspruch 1 unspezifiziert, wofür die alternativen Pfade gebraucht bzw. verwendet werden. Das Streitpatent lehrt bspw. ein Load-Balancing
und ein Failover, d.h. ein Umschalten zwischen den alternativen Übertragungswegen im Fehlerfall (SP, Abs. [0002], [0008], [0030] – [0031], [0053], [0080] sowie
Unteranspruch 10).




                 II.    Zu den vorgebrachten Nichtigkeitsgründen


Der Patentanspruch 1 ist sowohl gegenüber den Ursprungsunterlagen unzulässig
erweitert (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ)
als auch mangels Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V.
m. Art. 138 Abs. 1 Buchst. a), Art. 54 EPÜ).




1.   Zum Nichtigkeitsgrund der unzulässigen Erweiterung
Der Patentanspruch 1 gemäß Hauptantrag ist unzulässig erweitert (Art. 123 EPÜ),
da der Fachmann den Gegenstand des Patentanspruchs 1 den ursprünglichen Anmeldeunterlagen gemäß der Offenlegungsschrift der Stammanmeldung WO 2008/
059484 A2 (NK6) nicht unmittelbar und eindeutig entnimmt.


1.1 Der erteilte Patentanspruch 1 wird von der Klägerin wegen unzulässiger
Erweiterung gegenüber den ursprünglich eingereichten Anmeldeunterlagen mit
dem Argument angegriffen, dass Patentanspruch 1 im Vergleich zu den ursprünglich mit der Stammanmeldung eingereichten Ansprüchen nahezu vollständig neu
formuliert wurde, so dass der nunmehr beanspruchte Gegenstand keinerlei Stütze
in der Beschreibung der Stammanmeldung (NK6) mehr hätte. Darüber hinaus seien
im Patentanspruch 1 Merkmale weggelassen worden.

                                       - 17 -




Ein europäisches Patent mit Wirkung für das Hoheitsgebiet der Bundesrepublik
Deutschland ist für nichtig zu erklären, wenn sein Gegenstand über den Inhalt der
Anmeldung in der ursprünglich eingereichten Fassung hinausgeht. Der maßgebliche Inhalt ist anhand der Gesamtheit der ursprünglich eingereichten Unterlagen zu ermitteln. Er ist nicht auf den Gegenstand der in der Anmeldung
formulierten Patentansprüche beschränkt. Entscheidend ist vielmehr, was der
Gesamtheit der ursprünglichen Unterlagen als zur angemeldeten Erfindung
gehörend zu entnehmen ist (st. Rspr.: BGH, GRUR 2010, 513 Tz. 29 - Hubgliedertor
II). Innerhalb dieses Rahmens können die Patentansprüche bis zur Erteilung weiter
gefasst werden als in der Anmeldung. Die Änderung darf aber nicht dazu führen,
dass der Gegenstand des Patents über den Inhalt der ursprünglich eingereichten
Unterlagen hinaus verallgemeinert oder zu einem Aliud abgewandelt wird.


1.2 Entgegen der Auffassung der Klägerin, die Stammanmeldung offenbare zwar
Switches, aber im Speziellen keine Ethernet-Switches, wird zur Überzeugung des
Senats ein Ethernet-Switch in einem Ethernet-Switching-Netzwerk jedoch ursprünglich offenbart („Two network nodes 24 and 28, referred to as endpoints,
communicate with one another“, „Nodes 24 and 28 may comprise switches …
Ethernet switching network“, NK6, Fig. 1 i. V. m. S. 7, Z. 2 - 9; „Ethernet Frames“,
NK6, S. 8, Z. 19 – 31; Unterstreichung hinzugefügt).


1.3 Eine unzulässige Erweiterung liegt ebenfalls nicht durch die Beanspruchung
der Zieladresse des zweiten Ethernet-Schalters sowie ggf. deren Verwendung beim
Hashing vor. Denn zum einen lehrt die Offenlegungsschrift ein Verwenden beliebiger multipler Header-Felder beim Hashing („certain header fields“, NK6, S. 5, Z.
13 - 15), zum anderen offenbart sie ein zusätzliches Verwenden von VLAN-IDs aus
dem Frame-Header („identified by a unique VLAN identifier (VID) in the frame
header.“, NK6, S. 8, Z. 19 - 28). Dem Fachmann ist auch bekannt, dass eine
alleinige Verwendung der Zieladresse mittels der Hash-Funktion stets zur Auswahl

                                        - 18 -



des identischen Pfades und nicht zu einem Load-Balancing durch die Verwendung
alternativer Pfade führen würde.


1.4 Hingegen ist die Argumentation der Klägerin, dass lediglich die Durchführung
der Hash-Funktion durch den dritten und vierten Ethernet-Switch ursprungsoffenbart sei, wohingegen ein Hashing im ersten Knoten vom erteilten Patentanspruch 1 umfasst wird, zutreffend und begründet eine unzulässige Erweiterung
(siehe ebenso die Auslegung in Ziff. I. 3.).


Denn hinsichtlich der Durchführung der Hash-Funktion offenbart die Stammanmeldung NK6 in der Beschreibung sowie den Ausführungsbeispielen ausschließlich, dass diese in jedem einzelnen Switch der zwischen dem ersten und
zweiten Knoten zwischengeschalteten MHG, also in den Netzwerkknoten zwischen
den Endpunkten der Kommunikation („communicating between two endpoints“,
NK6, S. 5, Z. 1 - 3), durchgeführt wird, wobei ein einziger Switch der MHG den
Frame bzw. das Paket anhand des Hashing-Ergebnisses durchlässt und somit
einen Kommunikationspfad unter den mehreren alternativen Kommunikationspfaden auswählt und die übrigen Switches nach Berechnung des Hashing-Ergebnisses den Frame verwerfen („complementary hashing“, NK6, S. 9, Z. 16 - 20).
Hierzu versendet der erste Knoten als sogenannte „Quelle/Source“ zunächst in
einem Initialisierungsprozess basierend auf MAC-Learning den Frame bzw.
entsprechende Repliken jeweils an sämtliche Switches der MHG (vgl. NK6, Fig. 1
BZ 36A/B/C und Fig. 2 BZ 52,54 i. V. m. S. 2, Z. 14 - 24, S. 5, Z. 13 - 18, S. 9, Z. 12
- 20).


Die ursprünglichen Ansprüche waren – auch wenn sie nur vorläufigen Charakter
hatten – ebenfalls auf einen solchen Gegenstand gerichtet (NK6, Ansprüche 1, 15),
wobei die Merkmale betreffend das Hashing im dritten/ vierten Knoten im Rahmen
des Erteilungsverfahrens weggelassen wurden. Der erteilte Patentanspruch 1
beansprucht daher in seiner Breite jedoch im Gegensatz zur Stammanmeldung

                                       - 19 -



nunmehr auch Implementierungen, bei denen das Hashing und somit die Pfadauswahl bereits oder auch ausschließlich im ersten Knoten, d.h. in der
Quelle/Source als „Endpunkt“ der Kommunikation, durchgeführt werden kann.


Nach der herrschenden Rechtsprechung ist es grundsätzlich nicht zu beanstanden,
wenn der Patentanspruch nicht auf die in der Patentschrift ausführbar offenbarten
Ausführungsformen beschränkt wird, sondern diese in gewissem Umfang verallgemeinert (vgl. z.B. BGHZ 198, 205 Rn. 15, - Dipeptidyl-Peptidase-Inhibitoren).
Die von der Klägerin in diesem Zusammenhang zitierte höchstrichterliche Rechtsprechung (BGH, Urteil vom 26.09.2023, X ZR 76/21 – Farb- und Helligkeitseinstellung) gibt jedenfalls dann Anlass für eine anderweitige Beurteilung, wenn den
ursprünglich eingereichten Unterlagen zu entnehmen ist, dass einzelne Merkmale
in untrennbarem Zusammenhang miteinander stehen, der Patentanspruch diese
Merkmale aber nicht in ihrer Gesamtheit vorsieht.
So steht der Umstand, dass alle in einer Anmeldung geschilderten Ausführungsbeispiele ein bestimmtes Merkmal aufweisen, der Beanspruchung von Schutz für
Ausführungsformen ohne dieses Merkmal entgegen, wenn dem Inhalt der
Anmeldung zu entnehmen ist, dass die im Patentanspruch vorgesehenen Mittel der
Lösung eines Problems dienen, das das Vorhandensein des betreffenden Merkmals
voraussetzt (BGH, Urteil vom 07.11.2017, X ZR 63/15 – Digitales Buch).


Die Beklagte vertritt die Auffassung, dass zum Zweck der Verallgemeinerung das
Merkmal eines Hashings im dritten bzw. vierten Knoten weggelassen werden darf.
Zum einen würde ein Hashing im dritten bzw. vierten Knoten kein erforderliches
Merkmal im Sinn der o.g. Rechtsprechung „digitales Buch“ für die streitpatentgemäße Problemlösung „Load Balancing“ und „Failure Protection“ bzw.
Ausfallsicherheit / Redundanz über alternative Pfade darstellen, da ein Hashing im
ersten Knoten zur Pfadauswahl unter den alternativen Kommunikationspfaden und
somit zur technischen Realisierung sowie zur Problemlösung gemäß Streitpatent
genauso genügen würde.

                                        - 20 -



Zum anderen würden die Ausführungsbeispiele in der NK6 (Seite 5, Zeilen 5 bis 6)
nur typische Ausgestaltungen mit MHG-Knoten zwischen den Endpunkten
beschreiben, was ein Hashing bspw. im ersten Knoten nicht ausschließe („In some
embodiments, multiple ports, which typically reside in different network nodes
located between the endpoints, are defined as members of a multi-homing group
(MHG).“, Hervorhebungen hinzugefügt). Zudem zeige die NK6 (Seite 3, Zeile 32 bis
Seite 4, Zeile 3) sogar explizit ein Ausführungsbeispiel mit einem Hashing ohne
Ortsbestimmung des Knotens, so dass auch der erste Knoten in Frage kommen
könnte.


Zur Überzeugung des Senats ist es jedoch auch schon aus technischer Sicht zur
Problemlösung zwingend erforderlich, dass das Hashing im dritten und vierten
Knoten durchgeführt wird. Gemäß der Lehre ist das Hashing nämlich untrennbar mit
den zwischen den Endpunkten positionierten MHG-Knoten verbunden, welche ein
komplementäres Hashing durchführen. Denn ein Hashing alleine im ersten Knoten
würde u.a. den Zielvorgaben widersprechen, indem durch die Konzentration des
Hashings ausschließlich im ersten Knoten, d.h. im Gegensatz zu den multiplen
MHG-Knoten in einem einzigen Knoten, ein unerwünschter „single Point of Failure“
ermöglicht wird sowie darüber hinaus auch Layer-2 Schleifen nicht mehr zuverlässig
unterbunden werden (vgl. NK6, S. 5, Z. 10 - 12, „Since the member ports are
distributed among different network nodes, the resulting set of alternative
communication paths has no single point of failure, i.e., no single port, link or node
that is common to all paths.“, S. 5, Z. 15 - 18, „The hashing function is defined so
that each frame is forwarded via exactly one MHG member port and its respective
multi-homing path. All the other member ports discard the frame. All MHG nodes
use the same hashing function and apply the function to both incoming and outgoing
frames. As a result, layerloops are prevented.“; Unterstreichungen hinzugefügt).
Auch die Auffassung der Beklagten, dass ein Hashing im dritten bzw. vierten Knoten
immer zu dem gleichen Hash Ergebnis führe, da die Header Werte, nämlich die
Quell- bzw. Zieladresse, bei jedem Frame identisch seien, überzeugt den Senat
nicht. Die Beklagte verkennt nämlich hierbei, dass die Header neben der Quell- und

                                        - 21 -



Zieladresse auch noch weitere Werte, wie z. B. einen Längenindikator, aufweisen
und somit selbst bei gleichbleibender Quell- und Zieladresse die Hash Ergebnisse
für jeden Frame anders sein können.


Darüber hinaus beschreiben die ursprünglichen Unterlagen (NK6, Figur 2 i. V. m.
Beschreibung Seite 10, Zeilen 13 bis 19) ein Hashing ausschließlich in den MHG-Knoten zwischen den Endpunkten und schließen ein Involvieren von anderen
Knoten sogar explizit aus („The same hashing type is configured in all MHG nodes.
Note that multi-homing configuration is performed only in the MHG nodes, i.e., the
nodes containing member ports, 15 and does not involve any other network nodes.“;
Unterstreichung hinzugefügt). Auch in diesem Beispiel empfangen die MHG-Knoten
Ethernet Frames, welche von den Endpunkten, d. h. erster/zweiter Knoten (dort:
„nodes 24 and 28“), ausgetauscht werden („The MHG nodes receives Ethernet
frames exchanged between nodes 24 and 28, …“), so dass der erste Knoten nicht
als Mitglied der MHG in Frage kommen kann.


Schließlich greift auch die Argumentation der Beklagten hinsichtlich des
Ausführungsbeispiels NK6, Seite 3, Zeile 32 bis Seite 4, Zeile 3 ohne
Ortsbestimmung nicht durch. Denn auch dort wird durch das Hashing ein „member
Port“ ausgewählt, was den Fachmann unmittelbar und eindeutig auf einen Knoten
der MHG-Gruppe hinweist, welcher wiederum zwischen den Endpunkten
erster/zweiter Knoten zu lokalisieren ist.


Somit geht der Gegenstand des Streitpatents über den Inhalt der Stammanmeldung
hinaus, denn der Fachmann entnimmt dieser lediglich die erfinderische Intention,
mittels einer zwischen den „Endpunkten“ der Kommunikation, d. h. erster/zweiter
Knoten bzw. Source und Destination, zwischengeschalteten MHG, die letztlich auch
für die Pfadauswahl mittels Hashing verantwortlich ist, die Kommunikation zwischen
diesen   zwei    Endpunkten      über    ein     Layer-2-Netzwerk   mit   alternativen
Kommunikationspfaden zum Zwecke einer schnellen, sicheren und ausbalancierten
Kommunikation zu verbessern.

                                       - 22 -




Dass der Fachmann unter Umständen erkannt hätte, dass einzelne Maßnahmen
wie bspw. das Definieren der Ports des ersten Knotens bzw. des Source-Knotens
als MHG-Gruppe anstelle der zwischengeschalteten Switche bzw. deren Ports
sowie das komplette Verlagern der Pfadentscheidung mittels Hashing in den ersten
Knoten als Endpunkt bzw. in die Quelle/Source bei gleichzeitiger Degradierung der
zwischengeschalteten Switche zum reinen Weiterleiten von Paketen, ebenso
geeignet sein könnten, reicht zweifelsfrei für eine Offenbarung als unmittelbar und
eindeutig zur Erfindung gehörend nicht aus.


Der Fachmann würde auch derart weitreichende Architekturänderungen weder dem
„Disclaimer“ gemäß Offenlegungsschrift NK6, Seite 8, Zeilen 1 bis 7, entnehmen,
da diese Netzwerkkonfigurationen ebenfalls lediglich weitere Ausgestaltung der
MHG-Knoten und nicht des Source-Knotens betreffen, noch findet er hierzu
irgendwelche anderweitigen Hinweise und Anregungen in den ursprünglichen
Anmeldeunterlagen.


Grundsätzlich war es der Beklagten allerdings auch nicht verwehrt, Schutz für eine
Ausgestaltung mit einem Hashing in einem MHG-Knoten, d.h. im dritten und vierten
Knoten, zu beanspruchen, die in sämtlichen Ausführungsbeispielen konkret
offenbart ist.




2.    Zum Nichtigkeitsgrund der mangelnden Patentfähigkeit
Der Gegenstand des erteilten Patentanspruchs 1 gemäß Hauptantrag erweist sich
gegenüber dem entgegengehaltenen Stand der Technik – insbesondere gegenüber
der Lehre der Druckschrift D2 - als nicht neu (Art. 54 EPÜ).


2.1    Auf die Frage der wirksamen Inanspruchnahme älterer Prioritäten durch das
Streitpatent kommt es nicht an, da die maßgebliche Druckschrift D2 (hinsichtlich der
Neuheit) bereits vor der ältesten in Anspruch genommen Priorität veröffentlicht

                                       - 23 -



worden ist. Der Vollständigkeit halber weist der Senat darauf hin, dass bezüglich
einer unwirksamen Inanspruchnahme einer älteren Priorität in vollem Umfang die
Klägerin die Darlegungs- und Beweislast trägt (BGH GRUR 2024, 374 – Sorafenib-Tosylat). Da die Klägerin lediglich die Nichtveröffentlichung von Unterlagen zur
Übertragung der Prioritätsrechte in der Datenbank des US-amerikanischen
Patentamts vorgetragen hat, fehlt es bereits an einer substantiierten Darlegung vom
Umständen, die zur Unwirksamkeit der Rechteübertragung führen könnten.


Die Druckschrift D2 ist ein Benutzerhandbuch der Klägerin für ihr Produkt
ExtremeWare Software Version 7.5 und trägt auf der Titelseite den Hinweis
„Published October 2005“. Entgegen der Auffassung der Beklagten besteht nach
der Rechtsprechung eine – hier nicht widerlegte – Vermutung dafür, dass ein
Handbuch zum Zeitpunkt des auf der Titelseite angegebenen Publizierungsdatums
der Öffentlichkeit zugänglich war, und gilt somit als Stand der Technik (BGH, Urteil
vom 15.10.2013, X ZR 41/11 – Bildanzeigegerät; BGH, Urteil vom 7.11.2017, X ZR
113/15).


Auch im Übrigen kann die Frage der wirksamen Inanspruchnahme früherer
Prioritäten dahinstehen. Denn bei der Druckschrift D4, bei der die Frage allein von
Relevanz sein könnte, handelt es sich um eine US-Patentanmeldung, die kein
relevanter Stand der Technik ist (Art. 54 Abs. 3 EPÜ).


2.2   Der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag ist in
sämtlichen Merkmalen aus der Druckschrift D2 bekannt und nicht neu. Die D2
(ExtremeWare User Guide, Software Version 7.5) betrifft die ExtremeWare-Software der Klägerin, welche auf deren Switches installiert und betrieben wird.


Diese lehrt exemplarisch für den BlackDiamod-Switch im Kapitel 36 (ab S. 937 ff.)
die Konfiguration von transparenten LAN-Diensten (TLS) und virtuellen privaten
LAN-Diensten (VPLS), welche Layer-2-VPN-Dienste basierend auf Multi Protocol

                                      - 24 -



Label Switching (MPLS) ermöglichen, wobei zwei räumlich getrennte Netzwerksegmente bspw. desselben Unternehmensnetzwerks an verschiedenen Standorten
miteinander transparent über ein Provider-Netzwerk verbunden werden können.


Die D2, Figur 173 (S. 944), zeigt als Konfigurationsbeispiel ein System zur
Bereitstellung alternativer Kommunikationspfade zwischen den VPNs „unc“ und
„unc-wilmington“ mit einem TLS-Tunnel in einer MPLS-Domain (Merkmal M1).




Das System weist als Endpunkte einen ersten Switch (LSR1) als Quelle/Source,
einen zweiten Switch (LSR4) als Ziel/Destination sowie zwei zwischengeschaltete
Switches (LSR2, LSR3) als Teil eines Layer-2-Netzwerks auf. Die zwischen den
beiden VPN-Netzwerken „unc“ und „unc-wilmington“ ausgetauschten Frames
durchtunneln auf dem Layer-2, also ohne im Layergeroutet zu werden, in der
MPLS-Domäne das zwischengeschaltete Netzwerk mit den Switches LSR2, LSR3,
welche für die Frames transparent, d.h. nicht sichtbar, sind („Because TLS provides
Layertransport capabilities over MPLS“, D2, Fig. 173, S. 944; Unterstreichung
hinzugefügt; Merkmale M1.1, M1.2 und M1.3).

                                        - 25 -



Die Argumentation der Beklagten, bei den in Figur 173 gezeigten „Label Switch
Routern“ LSR1 bis LSR4 handele es sich um Router mit einem Layer-3 Routing und
demzufolge nicht um Layer-2 Switche, greift nicht durch.
Denn die D2, Kapitel 36 behandelt auf den Seiten 937 bis 954 das Konfigurieren
von MPLS Layer-2 VPNs mit BlackDiamond Switches.
Mit MPLS werden dabei verschiedene VPNs, wie die in Figur 173 gezeigten beiden
VPNs „unc“ und „unc-wilmington“, durch die BlackDiamond Switches auf dem
Layermiteinander verbunden. MPLS selbst wirkt hierbei wie ein zwischen dem
Layerund dem Layereingefügtes Konvergenzprotokoll, so dass der Fachmann
hier ggf. auch vom Layer-2.5 spricht. Im vorliegenden Ausführungsbeispiel der D2
liegt auch keine „Multi-Protocol“-Kommunikation (also kein MPLS mit einer
Mischung von PPP, ATM, Frame Relay bzw. Ethernet) sondern ein reines Ethernet-Netzwerk vor, wobei die Switches die Frames auf vordefinierten Pfaden anhand der
Labels gemäß der „shim header encapsulation“ durchleiten/durchtunneln (vgl.
ebenso D2, Fig. 168 und S. 894 - 896). Wie die Bezeichnung MPLS zutreffend
charakterisiert, handelt es sich bei diesem Verfahren um ein „Label Switching“ bzw.
um ein Weiterleiten/“Forwarding“ von Frames und definitiv nicht um ein Routing (vgl.
D2, S. 890, 2. Absatz, „Conceptually, label switching is straightforward. A label is a
relatively short, fixed-length identifier that is used to forward packets received from
a given link.“; Unterstreichung hinzugefügt).
Im Übrigen umfasst das Streitpatent ebenfalls die Verwendung von Routern als
Endpunkte der Layer-2 Kommunikation (vgl. SP, Abs. [0034] – [0035], „Nodes 24
and 28 may comprise switches, routers or any other type of network element.“;
Unterstreichung hinzugefügt).


Insoweit die Beklagte insbesondere darauf abstellt, dass das Streitpatent in einem
Layer-2 Netzwerk lediglich ein Weiterleiten der Ethernet-Frames basierend auf
MAC-Tabellen verstehen würde und definitiv kein Label-Switching gemäß D2,
übersieht sie dabei, dass das Streitpatent sehr wohl auch Ausführungsbeispiele
basierend auf üblichem VPLS beschreibt (SP, Abs. [0041], „… in some
embodiments, network 20 supports Virtual Private LAN Services (VPLS), as are

                                        - 26 -



known in the art. The frames associated with a particular virtual LAN (VLAN) are
identified by a unique virtual circuit (VC) label in the frame header“; Unterstreichung
hinzugefügt). Dem Fachmann ist zudem bekannt, dass VPLS sehr wohl auf MPLS
basieren und somit ebenfalls ein Label-Switching verwenden kann. Im Übrigen ist
der Gegenstand des Patentanspruchs 1 diesbezüglich auch offen und nicht auf eine
spezielle Switching-Methode beschränkt.


Gemäß der D2 werden Ethernet-Frames über bis zu vier alternative Kommunikationspfade („equal cost LSPs“) vom Quellknoten LSR1 an die Zieladresse des
Zielknotens LSR4 übertragen, wobei aufgrund des „Load-Balancings“ eine erste
Gruppe von Ethernet-Rahmen über den zwischengeschalteten Switch LSR3 und
eine zweite, nicht überlappende Gruppe von Ethernet-Rahmen über den
zwischengeschalteten Switch LSR4 – also über alternative Übertragungswege -
versendet werden („All tunneled frames are in tagged Ethernet format.“, „Tunnel
traffic can be load-shared across up to four equal cost LSPs.“, D2, S. 940; Merkmale
M1.4, M1.4.1, M1.4.2).


Das „Load-Balancing“ in der D2 beruht auf einem Ausführen einer Hash-Funktion,
welche den Label-Stack und MAC-Adressen verwendet („LSR traffic is load
balanced across multiple LSPs using a hash algorithm based only on the label stack
and MAC addresses of the packet. The label stack and MAC address hash algorithm
is based on a hash of the source and destination MAC addresses and the label
stack.“, D2, S. 912; Merkmal M1.4.3).


Auch die Argumentation der Beklagten, die D2, Seite 944, Figur 173 zeige Router-Schnittstellen LSR1 für das VLAN „unc“ sowie LSR2 für das VLAN „unc-wilmington“
mit entsprechend zugeordneten IP-Adressen, was wiederum auf einen „ingress IP
tunnel traffic“ mit Layer-3 Routing schließen lasse, vermag den Senat nicht zu
überzeugen. Denn die D2 beschreibt auf Seite 938, dass vor dem eigentlichen
Layer-2 Transport von 802.1Q Ethernet-Frames der TLS-Tunnel anhand der
jeweiligen IP-Adressen der Endpunkte mittels Label Distribution Protocol (LDP)

                                        - 27 -



konfiguriert wird, während des Betriebs hingegen wird ein Layer-2 Transport
verwendet. Darüber hinaus weisen gemäß D2, Figur 173 die beiden Switches LSR1
und LSR2 für „unc“ bzw. „unc-wilmington“ die gleiche IP Adresse „9.9.9.0/24“ auf,
d.h. beide VLANs gehören zum selben IP-Subnetz, was gemäß D2, Seite 592, Figur
110 ein Switching basierend auf Ethernet MAC-Adressen und kein Routing
basierend auf IP-Adressen impliziert.




3.   Zu den Unteransprüchen
3.1 Die Klägerin ist der Auffassung, sämtliche Unteransprüche seien gegenüber
dem vorgetragenen Stand der Technik nicht neu bzw. beruhten nicht auf erfinderischer Tätigkeit. Die Beklagte hat hierzu zu den Unteransprüchen 3 bis 8 im
Detail und zu den Unteransprüchen 2 und 9 bis 15 lediglich pauschal Stellung
genommen. Die Beklagte verteidigt den Hauptantrag nicht als geschlossenen
Anspruchssatz, sondern die Ansprüche werden einzeln bzw. isoliert verteidigt.


Die auf den Patentanspruch 1 mittelbar oder unmittelbar rückbezogenen Unteransprüche 2 bis 19 erweisen sich aber ebenfalls als nicht rechtsbeständig, da sie
aus demselben Grund wie Patentanspruch 1 unzulässig sind. Denn die erteilten
Unteransprüche 2 bis 19 heilen jeweils den Mangel der unzulässigen Erweiterung
hinsichtlich der potentiellen Verortung des Hashings außerhalb der MHG-Knoten,
bspw. im ersten Knoten, nicht.


Zwar betreffen die rückbezogenen Unteransprüche 2 bis 4 die Thematik des
Hashings, eine Beschränkung des Hashings auf die Netzwerkknoten der MHG, d.h.
bspw. den dritten oder vierten Knoten, ist diesen jedoch nicht zu entnehmen.
Die Unteransprüche 5 und 6 ordnen den dritten und den vierten Knoten zumindest
einer MHG zu, allerdings umfassen sie ebenfalls keine Einschränkung hinsichtlich
einer Verortung des Hashings in diesen Netzwerkknoten.
Auch den übrigen Unteransprüchen 7 bis 19 ist nichts zu entnehmen, was den o.g.
Mangel der unzulässigen Erweiterung heilen könnte.

                                        - 28 -




3.2 Aufgrund        des   durchgreifenden   Nichtigkeitsgrundes   der   unzulässigen
Erweiterung kann die Patentfähigkeit der Unteransprüche 2 bis 19 dahingestellt
bleiben.


Allerdings teilen die Unteransprüche 2 bis 19 auf der Grundlage des beiderseitigen
Parteivortrages das Schicksal des unabhängigen Anspruchs, weil sie nicht mehr als
handwerkliche, aus dem genannten Stand der Technik D1 bis D3 und D5 bis D6
bekannte Lehren zum technischen Handeln darstellen und damit nichts
eigenständig Patentfähiges enthalten.




                              III.   Zu den Hilfsanträgen


Die Hilfsanträge 1 bis 9 sind nicht zulässig. Es kann daher dahingestellt bleiben, ob
die erst in der mündlichen Verhandlung überreichten Hilfsanträge 4a und 4b als
verspätet gelten.
Darüber hinaus sind die Hilfsanträge 1 bis 4 und 5 bis 9 ebenfalls nicht patentfähig.


1.    Zum Hilfsantrag 1
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 1 ist nicht zulässig (Art. II
§ 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ). Zudem
ist sein Gegenstand mangels Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a), Art. 54 EPÜ).


1.1   Der Vorrichtungsanspruch 1 nach Hilfsantrag 1 enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1.4.2_Hi1 mit dem
editoriellen Streichen der Konjunktion „and“ sowie dem neu hinzugekommenen
Merkmal M1.4.4_Hi1 (Änderungen zum erteilten Anspruch hervorgehoben):

                                        - 29 -



      M1.4.4_Hi1: „ , and wherein the header field comprises a Media
                   Access Control, MAC, address.“


Das Merkmal M1.4.4_Hi1 gemäß Hilfsantrag 1 bildet die mit Patentanspruch 1
beanspruchte Vorrichtung dahingehend weiter aus, dass nunmehr das für das
Hashing im Merkmal M1.4.2 verwendete Header-Feld im Speziellen eine MAC-Adresse umfassen soll.


1.2    Der Patentanspruch 1 gemäß Hilfsantrag 1 ist unzulässig.


Der Patentanspruch 1 gemäß Hilfsantrag 1 geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei jedoch die damit verbundenen Änderungen den Mangel
der unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, nicht heilen.


1.3    Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 1 ist ebenfalls
nicht patentfähig, da auch das hinzugekommene Merkmal M1.4.4_Hi1 durch die
Lehre der Druckschrift D2 neuheitsschädlich vorweggenommen wird.


Denn die D2 beschreibt ein Load Balancing der Frames über die multiplen LSPs
basierend auf einem Hashing der MAC-Adressen (vgl. D2, S. 912, „LSR traffic is
load balanced across multiple LSPs using a hash algorithm based only on the label
stack and MAC addresses of the packet. The label stack and MAC address hash
algorithm is based on a hash of the source and destination MAC addresses and the
label stack.“ und „Non-IP ingress tunnel traffic is distributed across TLS tunnel LSPs
based on the MAC addresses of the packet.“; Unterstreichung hinzugefügt).


Hinsichtlich der unveränderten Merkmale des Patentanspruchs 1 wird auf die
entsprechenden Ausführungen zum Hauptantrag verwiesen.

                                        - 30 -



1.4    Da der Hilfsantrag 1 als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.


2.     Zum Hilfsantrag 2
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 2 ist nicht zulässig (Art. II
§ 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ). Zudem
ist sein Gegenstand mangels Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a), Art. 54 EPÜ).


2.1    Der Vorrichtungsanspruch 1 nach Hilfsantrag 2 enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1_Hi2 (Änderungen
hervorgehoben):


      M1_Hi2:      „A system for load balancing and/or failure protection
                   by providing alternative communication paths between
                   nodes, the system comprising:“


Das Merkmal M1_Hi2 gemäß Hilfsantrag 2 spezifiziert für die mit Patentanspruch 1
beanspruchte Vorrichtung ein Zweckmerkmal für Lastausgleich („load balancing“)
und/oder Fehlerschutz („failure protection“).


2.2    Der Patentanspruch 1 gemäß Hilfsantrag 2 ist unzulässig.


Der Patentanspruch 1 gemäß Hilfsantrag 2 geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei die damit verbundenen Änderungen den Mangel der
unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, jedoch nicht heilen.


2.3    Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2 ist ebenfalls
nicht patentfähig, da er durch die Lehre der Druckschrift D2 neuheitsschädlich
vorweggenommen wird.

                                       - 31 -




Denn die D2 zeigt auf den Seiten 912 und 940 gleichfalls jeweils einen
Lastausgleich (dort: „LSR traffic is load balanced across multiple LSPs using a hash
algorithm based only on the label stack and MAC addresses of the packet.“ und
„Tunnel traffic can be load-shared across up to four equal cost LSPs.“).
Darüber hinaus offenbart die D2 einen entsprechenden Fehlerschutz auf den Seiten
924 und 933/934 (dort: „Redundant LSPs“ und „A secondary path is also created
which, in the event of failure of a link or node on the primary path, activates the
secondary path for the LSP.“). Somit sind beide Alternativen des Merkmals M1_Hi2
vorbekannt.


Hinsichtlich der unveränderten Merkmale des Patentanspruchs 1 wird auf die
entsprechenden Ausführungen zum Hauptantrag verwiesen.


2.4   Da der Hilfsantrag 2 als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.




3.    Zum Hilfsantrag 3
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 3 ist nicht zulässig (Art. II
§ 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ). Zudem
ist sein Gegenstand mangels Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a), Art. 54 EPÜ).


3.1   Der Vorrichtungsanspruch 1 nach Hilfsantrag 3 enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1_Hi2 umfassend das
Zweckmerkmal für Lastausgleich und/oder Fehlerschutz, das geänderte Merkmal
M1.4.2_Hi1 mit dem editoriellen Streichen der Konjunktion „and“ sowie das neu
hinzugekommene Merkmal M1.4.4_Hi3 (Änderungen hervorgehoben):

                                        - 32 -



      M1.4.4_Hi3: „ , and wherein the first and second communication
                   paths between the first and second switches are used
                   for protection against failures or for providing traffic
                   load balancing.“


Das Merkmal M1.4.4_Hi3 gemäß Hilfsantrag 3 spezifiziert für die mit
Patentanspruch 1 beanspruchte Vorrichtung zusätzlich zum Zweckmerkmal
M1_Hi2 nunmehr auch eine Verwendung („are used for“) für Fehlerschutz
(„protection against failures“) und/oder Lastausgleich („load balancing“).


3.2    Der Patentanspruch 1 gemäß Hilfsantrag 3 ist unzulässig.


Der Patentanspruch 1 gemäß Hilfsantrag 3 geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei die damit verbundenen Änderungen den Mangel der
unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, jedoch nicht heilen.


3.3    Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 3 ist ebenfalls
nicht patentfähig, da er durch die Lehre der Druckschrift D2 neuheitsschädlich
vorweggenommen wird.


Wie bereits unter Ziff. III. 2.3 ausgeführt, zeigt die D2 auf den Seiten 912 und 940
jeweils einen Lastausgleich (dort: „LSR traffic is load balanced across multiple LSPs
using a hash algorithm based only on the label stack and MAC addresses of the
packet.“ und „Tunnel traffic can be load-shared across up to four equal cost LSPs.“).
Darüber hinaus offenbart die D2 einen entsprechenden Fehlerschutz auf den Seiten
924 und 933/934 (dort: „Redundant LSPs“ und „A secondary path is also created
which, in the event of failure of a link or node on the primary path, activates the
secondary path for the LSP.“)

                                       - 33 -



Hinsichtlich der übrigen Merkmale des Anspruchs 1 gemäß Hauptantrag sowie der
vorangegangenen Hilfsanträge wird auf die entsprechenden Ausführungen
verwiesen.


3.4    Da der Hilfsantrag 3 als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.




4.     Zum Hilfsantrag 4
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 4 ist nicht zulässig (Art. II
§ 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ). Zudem
ist sein Gegenstand mangels Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1
IntPatÜG i.V.m. Art. 138 Abs. 1 Buchst. a), Art. 54 EPÜ).


4.1    Der Vorrichtungsanspruch 1 nach Hilfsantrag 4 enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1_Hi2 umfassend das
Zweckmerkmal für Lastausgleich und/oder Fehlerschutz, das geänderte Merkmal
M1.4.2_Hi1 mit dem editoriellen Streichen der Konjunktion „and“ sowie das neu
hinzugekommene Merkmal M1.4.4_Hi4 (Änderungen hervorgehoben):


      M1.4.4_Hi4: „ , and wherein the third and fourth Ethernet switches
                   are configured for Layerswitching of Ethernet frames
                   using respective Media Access Control, MAC, tables.“


Das Merkmal M1.4.4_Hi4 gemäß Hilfsantrag 4 spezifiziert für die mit
Patentanspruch 1 beanspruchte Vorrichtung eine Konfiguration („are configured
for“) mit MAC-Tabellen zum Layer-2 Schalten von Ethernet-Frames.


4.2    Der Patentanspruch 1 gemäß Hilfsantrag 4 ist unzulässig.

                                        - 34 -



Der Patentanspruch 1 gemäß Hilfsantrag 4 geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei die damit verbundenen Änderungen den Mangel der
unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, jedoch nicht heilen.


4.3     Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 4 ist ebenfalls
nicht patentfähig, da er durch die Lehre der Druckschrift D2 neuheitsschädlich
vorweggenommen wird.


Mit dem Merkmal M1.4.4_Hi4 wird lediglich beansprucht, dass sowohl der dritte als
auch der vierte Knoten jeweils ein Switch ist, welcher ganz allgemein mit einer MAC-Tabelle konfiguriert ist und ausgestaltet ist, damit Ethernet-Frames weiterzuleiten.
Die D2, Kapitel 6 (S. 139 ff.) beschreibt die FDB („Forwarding Database“) der
ExtremeWare Switche, welche die gelernten MAC-Adressen zum Weiterleiten der
Ethernet-Frames beinhaltet (dort: „The switch maintains a database of all media
access control (MAC) addresses received on all of its ports. It uses the information
in this database to decide whether a frame should be forwarded or filtered.“;
Unterstreichung hinzugefügt). Das Merkmal M1.4.4_Hi4 ist dadurch verwirklicht.


Hinsichtlich der übrigen Merkmale des Patentanspruchs 1 gemäß Hauptantrag
sowie    der   vorangegangenen     Hilfsanträge   wird   auf   die   entsprechenden
Ausführungen verwiesen.


4.4     Da der Hilfsantrag 4 als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.




5.      Zum Hilfsantrag 4a
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 4a ist nicht zulässig (Art.
II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ).

                                        - 35 -



5.1    Der Vorrichtungsanspruch 1 nach Hilfsantrag 4a enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1.4.2_Hi1 mit dem
editoriellen Streichen der Konjunktion „and“ sowie das neu hinzugekommene
Merkmal M1.4.4_Hi4a (Änderungen hervorgehoben):


      M1.4.4_Hi4a: „ , and wherein the third and fourth Ethernet switches
      are configured for Layerswitching of said Ethernet frames using
      respective Media Access Control, MAC, tables.“


Das Merkmal M1.4.4_Hi4a gemäß Hilfsantrag 4a spezifiziert für die mit
Patentanspruch 1 beanspruchte Vorrichtung eine Konfiguration („are configured
for“) mit MAC-Tabellen zum Layer-2 Schalten der im Anspruch vorab genannten
(„said“)   Ethernet-Frames     durch    die      Switches   auf   den    alternativen
Kommunikationspfaden (dritter und vierter Switch), also eine Abgrenzung zum
Label-Switching gemäß D2.


5.2    Der Patentanspruch 1 gemäß Hilfsantrag 4a ist unzulässig.


Der Patentanspruch 1 gemäß Hilfsantrag 4a geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei die damit verbundenen Änderungen den Mangel der
unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, jedoch nicht heilen.


5.3    Da der Hilfsantrag 4a als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.




6.     Zum Hilfsantrag 4b
Der Patentanspruch 1 in der Fassung gemäß Hilfsantrag 4b ist nicht zulässig (Art.
II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ).

                                        - 36 -



6.1    Der Vorrichtungsanspruch 1 nach Hilfsantrag 4b enthält gegenüber der
Fassung gemäß Hauptantrag das geänderte Merkmal M1.4.2_Hi1 mit dem
editoriellen Streichen der Konjunktion „and“, das aus Hilfsantrag 4a bereits
bekannte Merkmal M1.4.4_Hi4a sowie das geänderte Merkmal M1.4_Hi4b,
(Änderungen hervorgehoben):


      M1.4_Hi4b:    „the alternative communication paths are Layercommunication paths and the first Ethernet switch (24) is operative for
      receiving and transmitting Ethernet frames having a destination address
      of the second Ethernet switch,“


Das Merkmal M1.4_Hi4b gemäß Hilfsantrag 4b beansprucht nunmehr einen ersten
Knoten („first Ethernet switch“), welcher Ethernet-Frames mit einer Zieladresse des
zweiten Knotens empfängt, um diese an den zweiten Knoten zu senden. Merkmal
M1.4_Hi4b lässt dabei offen, woher der empfangene Ethernet-Frame stammt.


6.2    Der Patentanspruch 1 gemäß Hilfsantrag 4b ist unzulässig.


Der Patentanspruch 1 gemäß Hilfsantrag 4b geht aus dem Anspruch 1 gemäß
Hauptantrag hervor, wobei die damit verbundenen Änderungen den Mangel der
unzulässigen Erweiterung hinsichtlich der potentiellen Verortung des Hashings
außerhalb der MHG-Knoten, bspw. im ersten Knoten, jedoch nicht heilen.


Darüber hinaus wird nunmehr mit dem Empfangen von Ethernet-Frames im ersten
Knoten mit einer Zieladresse des zweiten Knotens beansprucht, dass der erste
Knoten weder Endpunkt noch Quelle/Source der Kommunikation ist. Eine solche
Konfiguration bzw. eine solche Kommunikation wird in der NK6 jedoch überhaupt
nicht adressiert, da die NK6 ausschließlich eine Kommunikation zwischen dem
ersten und dem zweiten Knoten als „Endpunkte“ betrifft (vgl. NK6, S. 2, Z. 11 – 13,
„… a method for communication between first and second nodes via a
communication network …“; Unterstreichung hinzugefügt).

                                         - 37 -




6.3    Da der Hilfsantrag 4b als geschlossener Anspruchssatz verteidigt wird, fallen
damit auch die abhängigen Ansprüche.




7.     Zu den Hilfsanträgen 5 bis 9
Die Hilfsanträge 5 bis 9 sind Kombinationen der Hilfsanträge 1 bis 4. Der jeweilige
Patentanspruch 1 ist daher nicht zulässig (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. c), Art. 123 EPÜ). Zudem ist sein Gegenstand mangels
Neuheit nicht patentfähig (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i.V.m. Art. 138 Abs. 1
Buchst. a), Art. 54 EPÜ), wobei auf die obigen Ausführungen zu diesen
Hilfsanträgen in den Ziff. III.1. bis 4. verwiesen wird.




                                           B.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.



                                           C.


                               Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland

                                     - 38 -



zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigen schriftlich oder
in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe,
einzulegen.




Heimen         Bieringer          Schödel         Dr. Ball        Jürgensen

                                   - 39 -



Bundespatentgericht

      5 Ni 47/21 (EP)
         (Aktenzeichen)




Verkündet am

20. November 2024

…

Justizbeschäftigte
als Urkundsbeamtin der Geschäftsstelle
