---
ecli: "ECLI:DE:BPatG:2011:040811B17Wpat75.07.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 75/07"
decided: "2011-08-04"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=53&nr=23088&anz=1310&pos=809&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-08-04_17_W-pat_75_07_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 75/07 vom 2011-08-04

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 75/07                                                  Verkündet am
_______________                                                    4. August 2011
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2004 059 813.4-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 4. August 2011 unter Mitwirkung des Richters
Dipl.-Ing. Prasch als Vorsitzender, der Richterin Dr. Mittenberger-Huber, des
Richters Dipl.-Ing. Baumgardt und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
05.11

                                       -2-



beschlossen:


                     Die Beschwerde wird zurückgewiesen.




                                   Gründe


                                        I.


Die vorliegende Patentanmeldung, die eine Priorität vom 11. Dezember 2003 aus
Korea in Anspruch nimmt, wurde am 7. Dezember 2004 beim Deutschen Patentund Markenamt eingereicht. Sie trägt die Bezeichnung:


           „Betriebsverfahren für ein elektronisches Host-Karte-System
                              und Speichersystem“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts mit der Begründung zurückgewiesen, dass
der geltende Hauptanspruch mangels erfinderischer Tätigkeit für seinen Gegenstand nicht gewährbar sei, da dieser Gegenstand für den Fachmann aus der
Druckschrift 3 (US 5 581 708 A) nahegelegt sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Auf einen
mit der Ladung übersandten Hinweis des Senates hin, mit dem weitere im
Wesentlichen aus einem parallelen US-Prüfungsverfahren stammende Druckschriften ins Verfahren eingeführt wurden, reicht sie eingeschränkte und teilweise
klargestellte Patentansprüche nach Haupt- und nach Hilfsantrag ein. Sie macht
geltend, dass das nunmehr beanspruchte Verfahren und Speichersystem auch
durch den ergänzten Stand der Technik nicht nahegelegt sei. Insbesondere gebe
es – im Sinne des „could-would-approach“ – keinerlei Veranlassung für den

                                      -3-



Fachmann, die beanspruchten Verfahrensschritte in genau dieser Weise vorzusehen.


Die Anmelderin stellt den Antrag,


        den Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 26. Juni 2007 aufzuheben
        und das Patent auf der Grundlage folgender Unterlagen zu erteilen:


        Bezeichnung:
        Betriebsverfahren für ein elektronisches Host-Karte-System und
        Speichersystem


        Patentansprüche:


        Hauptantrag
        Patentansprüche 1 bis 11, übergeben in der mündlichen Verhandlung vom 4. August 2011 um 11:15 h


        Hilfsantrag
        Patentansprüche 1 bis 11, übergeben in der mündlichen Verhandlung vom 4. August 2011 um 11:50 h


        Beschreibung:
        Beschreibung Seiten 1 und 4 bis 11 vom Anmeldetag (7. Dezember 2004)
        Seite 2, übergeben mit Schriftsatz vom 27. Oktober 2006
        Seite 3, übergeben mit Schriftsatz vom 15. Juni 2007
        Seiten 3a, 3b und 3c, übergeben im Termin

                                      -4-



       Zeichnungen:
       6 Seiten Zeichnungen mit Figuren 1A bis 6 vom Anmeldetag.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


      „1.    Verfahren zum Betrieb eines Systems mit einer Host-Rechnereinheit (210) und einer mit dieser koppelbaren elektronischen Schaltkreiskarte (220),


             wobei die Host-Rechnereinheit zwei vorgegebene unterschiedliche Übertragungsgeschwindigkeiten unterstützt und
             die elektronische Schaltkreiskarte eine dieser Übertragungsgeschwindigkeiten unterstützt,


       mit folgenden Schritten:


       (a)   Übertragen einer Übertragungsgeschwindigkeitsinformation
             (SPEED_I), die eine der zwei Übertragungsgeschwindigkeiten spezifiziert, von der Host-Rechnereinheit zur elektronischen Schaltkreiskarte, wenn die elektronische Schaltkreiskarte an die Host-Rechnereinheit angekoppelt wird,


       (b)   Übertragen eines Antwortsignals (S_ACK) von der elektronischen Schaltkreiskarte zur Host-Rechnereinheit, wenn die
             von der elektronischen Schaltkreiskarte unterstützte Übertragungsgeschwindigkeit gleich der Übertragungsgeschwindigkeit ist, die durch die von der Host-Rechnereinheit übertragene Übertragungsgeschwindigkeitsinformation spezifiziert
             wird,

                                       -5-



       (c)   Übertragen einer Datenbitbreiteninformation (DATA_W) von
             der Host-Rechnereinheit zur elektronischen Schaltkreiskarte,
             wenn das Antwortsignal von der Host-Rechnereinheit empfangen wird, und


       (d)   Übertragen eines Befehlssignals (CMD0) von der Host-Rechnereinheit zur elektronischen Schaltkreiskarte zum Initialisieren der elektronischen Schaltkreiskarte, wenn das Antwortsignal empfangen und die Datenbitbreiteninformation übertragen wurde oder wenn auf die Übertragung der die eine der
             zwei Übertragungsgeschwindigkeiten spezifizierenden Übertragungsgeschwindigkeitsinformation      kein    Antwortsignal
             empfangen wurde,


       (e)   wonach entsprechend Daten zwischen der Host-Rechnereinheit und der elektronischen Schaltkreiskarte mit der zum
             Antwortsignal gehörigen Übertragungsgeschwindigkeit oder
             mit der anderen der zwei Übertragungsgeschwindigkeiten
             übertragbar sind.“


Wegen der Unteransprüche 2 und 3 sowie des nebengeordneten, auf ein demgemäß betriebenes Speichersystem gerichteten Anspruchs 4 mit seinen Unteransprüchen 5 bis 11 wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 gemäß Hilfsantrag unterscheidet sich vom Anspruch 1 des Hauptantrags durch folgendes zusätzliches, zwischen den Merkmalen (a) und (b) eingefügtes Merkmal:


      „(ax) über einen zum Übertragen von Daten zwischen der Host-Rechnereinheit und der elektronischen Schaltkreiskarte genutzten Kontakt (7) der Karte,“

                                        -6-



Wegen seiner Unteransprüche 2 und 3 sowie des nebengeordneten Anspruchs 4
mit dessen Unteransprüchen 5 bis 11 wird ebenfalls auf die Akte verwiesen.


Als der Anmeldung zugrundeliegendes technisches Problem (Aufgabe) ist genannt: die Bereitstellung eines Speichersystems der eingangs genannten Art und
eines Betriebsverfahrens hierfür mit gegenüber dem oben erwähnten Stand der
Technik weiterentwickelter Übertragungsgeschwindigkeitscharakteristik (siehe geltende Beschreibung Seite 3b vom 4. August 2011, Absatz 2).




                                         II.


Die Beschwerde ist rechtzeitig eingelegt und auch sonst zulässig. Sie bleibt jedoch
ohne Erfolg, weil der Gegenstand des Patentanspruchs 1 nach Hauptantrag wie
auch nach Hilfsantrag nicht auf einer erfinderischen Tätigkeit beruht (§ 4 PatG).


1.    Die vorliegende Patentanmeldung betrifft die Ankoppelung einer elektronischen Schaltkreiskarte an eine Host-Rechnereinheit, und hier besonders die zu
Beginn erfolgende Initialisierung, um die dv-technische „Verständigung“ zwischen
Karte und Host sicherzustellen; dabei ist unter der „elektronischen Schaltkreiskarte“ beschreibungsgemäß vor allem eine Speicherkarte nach MMC-Standard oder
ähnlichem (z. B. SD) zu verstehen, siehe Offenlegungsschrift Absatz [0016] u. a..


Die in der Anmeldung in Bezug genommene Spezifikation für Multimediakarten
(MMC) nach Version 3.3 vom März 2003 (siehe Absatz [0003]; vgl. unten: D6) beschreibt Speicherkarten mit 7 Anschlusskontakten, von denen einer für die serielle
Datenübertragung, einer als Takt- und einer als Befehlsleitung verwendet wird, die
übrigen für die Betriebsspannung und Masseanschluss. Die Übertragungsrate beträgt bei einer Taktfrequenz von 20 MHz bis zu 2 MB/s (Mega-Byte pro Sekunde).

                                           -7-



Gerade bei Speicherkarten besteht immer der Wunsch, die Datenübertragungsgeschwindigkeit zu erhöhen. So sieht beispielsweise der später (nach dem Prioritätstag) veröffentlichte MMC-Plus-Standard eine Vier- oder Acht-Bit-Parallelübertragung, mit entsprechend mehr Anschlusskontakten, und außerdem eine höhere
Taktrate von bis zu 52 MHz vor; damit wird eine Datenübertragungsrate von bis zu
52 MB/s möglich (vgl. auch Anmeldung Absatz [0005]).


Als Konsequenz daraus, dass nun Speicherkarten mit unterschiedlicher Übertragungsrate verfügbar sind, muss bei der Ankoppelung einer Speicherkarte an eine
Host-Rechnereinheit zunächst festgestellt werden, für welche Übertragungsrate
die jeweilige Karte ausgelegt ist, d. h. ob die Datenübertragung nach dem neuen,
schnelleren Standard durchgeführt werden kann oder nicht. Hierfür schlägt die
Anmeldung ein geeignetes Verfahren in Form bestimmter Initialisierungsschritte,
sowie ein danach arbeitendes Speichersystem vor.


Die Lehre des Patentanspruchs 1 bezieht sich auf eine Host-Rechnereinheit,
welche zwei unterschiedliche Übertragungsgeschwindigkeiten unterstützt, sowie
auf eine elektronische Schaltkreiskarte, welche eine dieser beiden Übertragungsgeschwindigkeiten unterstützt; implizit wird noch davon ausgegangen, dass bei
der einen der zwei Geschwindigkeiten eine besondere „Datenbitbreite“ (im Sinne
einer Parallelübertragung mehrerer Bits, statt ein-bit-serieller Übertragung) einstellbar ist. Zur Erkennung und Festlegung der richtigen Übertragungsparameter
wird gemäß Hauptantrag das folgende in den Figuren 4A und 4B skizzierte und
insbesondere in den Absätzen [0021] bis [0027] beschriebene Verfahren beansprucht:


       –     Wenn die Karte an den Host angekoppelt wird, überträgt der
             Host zunächst eine Information SPEED_I, welche eine der
             zwei möglichen Übertragungsgeschwindigkeiten beschreibt,
             an die Karte (Schritt (a));

                                        -8-



         –   falls die Karte diese Geschwindigkeit unterstützt, sendet sie
             ein Antwortsignal S_ACK zurück (Schritt (b)); der Host
             überträgt dann eine „Datenbitbreiteninformation“ DATA_W
             (Schritt (c)) und sendet danach ein Befehlssignal CMD0 zur
             Initialisierung der Karte (teilweise Schritt (d)), so dass anschließend Daten mit dieser Geschwindigkeit übertragen
             werden können (teilweise Schritt (e));


         –   falls die Karte diese Geschwindigkeit nicht unterstützt, sendet sie kein Antwortsignal; das erkennt der Host und sendet
             ein Befehlssignal CMD0 zur Initialisierung der Karte (zweiter
             Teil von Schritt (d)), so dass anschließend Daten mit der
             anderen der beiden Geschwindigkeiten übertragen werden
             können (zweiter Teil von Schritt (e)).


Im Patentanspruch 1 gemäß Hilfsantrag ist noch zusätzlich spezifiziert, dass die
Übertragung der Geschwindigkeitsinformation SPEED_I in Schritt (a) über einen
Datenkontakt (7) der Schaltkreiskarte erfolgen soll (Merkmal (ax)).


Als Fachmann, der mit der Aufgabe betraut wird, die Übertragungsgeschwindigkeit zwischen Host und Speicherkarte zu erhöhen, und dabei aus Kompatibilitätsgründen ein Betriebsverfahren für Speicherkarten unterschiedlicher Übertragungsgeschwindigkeiten zu entwickeln, ist ein Diplom-Ingenieur der Elektrotechnik mit
Hochschul- oder Fachhochschul-Ausbildung und mehrjähriger Berufserfahrung im
Bereich der Datenübertragung zwischen Rechner und Speicher anzusehen.


2.      Aus dem entgegengehaltenen Stand der Technik kommt folgenden Druckschriften eine besondere Bedeutung zu (Nummerierung wie im bisherigen Verfahren):

                                        -9-



        D4   US 2003 / 112 611 A1
        D5   US 5 798 507 A
        D6   MultiMediaCard System Summary Version 3.31, März 2003


D4 betrifft eine Multifunktions-Speicherkarte als Fortentwicklung der MMC- bzw.
SD-Speicherkarten, welche mit diesen kompatibel sein soll (vgl. insbesondere Absätze [0002] bis [0004], Absatz [0011]). Hier ist zusätzlich auch ein 4-Bit-paralleler
Datenübertragungsmodus vorgesehen, der z. B. durch einen Befehl beim Ankoppeln der Speicherkarte (command from the host device … at power-on, siehe Absatz [0046] letzter Satz) eingestellt werden kann. Der Fachmann entnimmt der D4
die Lehre, bei Weiterentwicklungen bekannter Speicherkarten besonders auf
Kompatibilität mit den Vor-Versionen zu achten, so dass die nach altem Standard
arbeitenden Karten weiterhin betreibbar sind; außerdem, zur Erhöhung der Übertragungsrate statt der bekannten ein-bit-seriellen Übertragung eine 4-Bit-Parallelübertragung vorzusehen und die Busbreite beim Ankoppeln einer Speicherkarte
entsprechend deren Fähigkeiten vom Host aus geeignet einzustellen (ähnlich
Merkmal (c)).


D5 beschreibt ein Kartenlese-/-schreibgerät (IC card reader / writer 1), das mit
Chipkarten nach verschiedenen Übertragungsprotokollen mit unterschiedlichen
Taktfrequenzen ("T=1": 3,5 MHz; "T=14": 4,9 MHz) zusammenarbeiten kann. In
einer Ausführungsform (Figur 5 und Beschreibung Spalte 5 Zeile 58 ff.) sendet das
Lese-/Schreibgerät nach dem Einstecken einer Chipkarte und deren dadurch
ausgelöstem Reset eine Taktfrequenz von 3,5 MHz und erwartet eine Antwort der
Karte; wenn die Karte nach dem T=1-Protokoll arbeiten kann, sendet sie ein
Antwortsignal zurück, und die Kommunikation kann auf dieser Basis stattfinden
(Spalte 6 Zeile 2 – 5, Zeile 26 ff.) – insoweit entspricht die Lehre der D5 den beanspruchten Merkmalen (a), (b) und teilweise (e). Wenn die Karte hingegen nach
dem T=14-Protokoll arbeitet, antwortet sie auf die Anfrage nicht (teilweise Merkmal (d)); das Lese-/Schreibgerät erkennt dies und ändert die gesendete Taktfrequenz auf 4,9 MHz, um so anzufragen, ob die Karte das T=14-Protokoll verwendet

                                       - 10 -



(siehe Spalte 6 Zeile 9 – 25, insbesondere „if no response is supplied from the IC
card when a preset time has elapsed“). Dem Flussdiagramm in Figur 5 ist entnehmbar, dass erneut geprüft wird, ob die Karte antwortet (Schritt S5d) – wenn
nein, wird die Karte als „abnormal card“ bestimmt und beispielsweise ausgeworfen
(vgl. Spalte 5 Zeile 13 - 17, zu einer anderen Ausführungsform).


D6 dürfte der bereits in der Anmeldung Absatz [0003] zitierten Dokumentation des
MMC-Standards entsprechen. Kapitel 3 beschreibt das gesamte Datenübertragungskonzept; Abschnitt 3.2.2 auf Seite 13 ist zu entnehmen, dass nach dem Anschaltvorgang (power-on reset) der Host Initialisierungsbefehle schicken soll (ähnlich Merkmal (d)). Gemäß Seite 21 sind für die Informationsübertragung der CMD-Anschluss und der DAT-Anschluss vorgesehen (vgl. auch Figur 7 bis 11).


3.    Zum Hauptantrag


Dem Hauptantrag konnte nicht gefolgt werden, weil das Verfahren nach Patentanspruch 1 den Durchschnittsfachmann aus dem Stand der Technik nahegelegt
war und somit nicht auf einer erfinderischen Tätigkeit beruhte.


3.1   Als Ausgangspunkt ist zunächst die bekannte MMC-Speicherkarte gemäß
D6 mit einer 1-Bit-Datenbusbreite (siehe Tabelle Seite 5 unten / Figur 14 oben)
und mit einer maximalen Taktfrequenz von 20 MHz (Tabelle Seite 5 oben) in den
Blick zu nehmen. Das Systemkonzept sah bereits vor, dass die Host-Rechnereinheit nach Ankoppelung einer solchen Speicherkarte vor Beginn einer Datenübertragung ein Befehlssignal zum Initialisieren der Karte an diese überträgt (Seite 13
oben – teilweise Merkmal (d)).


3.2   Für die Aufgabenstellung, die Übertragungsgeschwindigkeit zwischen Host
und Speicherkarte zu erhöhen, war keine besondere Anregung erforderlich – derartige Weiterbildungen und Verbesserungen sind vielmehr typisch für den Aufgabenbereich des hier zuständigen Fachmanns (s. o.).

                                     - 11 -



In dieser Richtung konnte der Fachmann beispielsweise der D4 die Lehre entnehmen, die Anzahl der Kartenkontakte zu erhöhen und statt der 1-Bit-Datenübertragung eine 4-Bit-Parallelübertragung vorzusehen; dazu erhielt er aus D4 den
deutlichen Hinweis, auf Kompatibilität mit den vorherigen Kartenversionen zu
achten, so dass die nach altem Standard arbeitenden Karten weiterhin betreibbar
sind. Daraus ergab sich zwangsläufig ein Systemkonzept der Art, dass der Host-Rechner sowohl den alten Standard wie auch das schnellere Verfahren unterstützen muss; die Speicherkarte hingegen kann entweder von alter Art oder für eine
schnellere Übertragung ausgelegt sein (entsprechend dem ersten und zweiten
Absatz des Anspruchs 1, allgemein auf das verwendete Übertragungsprotokoll
bezogen). Nach Ankoppelung der Speicherkarte an den Host muss eine Vereinbarung der zu verwendenden Datenbusbreite vorgenommen werden, zum Beispiel
durch Einstellen vom Host aus wie als Möglichkeit in D4 beschrieben (im Prinzip
entsprechend Merkmal (c)).


3.3     Dem Fachmann war auch geläufig, dass sich eine höhere Übertragungsgeschwindigkeit durch eine Erhöhung der Taktfrequenz erreichen lässt (dieser Zusammenhang ist nahezu trivial). Hier stellte sich jedoch ebenfalls das Kompatibilitätsproblem, insbesondere die Frage, wie sich erkennen lässt, mit welcher
Übertragungsgeschwindigkeit eine beliebige angekoppelte Karte betrieben werden
soll.


Hierzu konnte der Fachmann beispielsweise aus D5 das Verfahren entnehmen,
dass der Host eine Übertragungsgeschwindigkeitsinformation in Form einer der
möglichen Taktfrequenzen zur Speicherkarte überträgt; wenn die Speicherkarte
damit arbeiten kann, sendet sie ein Antwortsignal zurück, und die Kommunikation
kann auf dieser Basis stattfinden; andernfalls sendet sie kein Antwortsignal zurück, was den Host veranlasst, eine andere Taktfrequenz „auszuprobieren“. Dieses Vorgehen entspricht im Wesentlichen den Merkmalen (a), (b) und teilweise
(d), (e).

                                      - 12 -



3.4   Insoweit ergibt sich, dass alle einzelnen Aspekte der beanspruchten Lehre
dem Fachmann aus dem Stand der Technik bekannt waren. Zwar ist das Verfahren exakt in der beanspruchten Reihenfolge und mit genau den beanspruchten
Schritten nicht vorbeschrieben, so dass der Gegenstand des Patentanspruchs 1
nach Hauptantrag neu ist. Es verließ aber nicht den Rahmen üblichen fachmännischen Handelns, die einzelnen Ideen zusammenzufügen und dafür, so wie es
beansprucht ist, ein gemeinsames Initialisierungskonzept zu schaffen.


Denn die reine Auswahl aus verschiedenen dem Fachmann zur Verfügung stehenden Möglichkeiten kann nicht als erfinderisches Handeln bewertet werden,
wenn sie nicht in irgendeiner Weise besondere oder unerwartete Vorteile hat (vgl.
dazu BGH GRUR 2008, 56 – Injizierbarer Mikroschaum). In der beanspruchten
Zusammenstellung und Reihenfolge der einzelnen Maßnahmen (Übermitteln einer
Geschwindigkeitsinformation, Warten auf Antwortsignal zur Erkennung der Geschwindigkeit, Senden einer Datenbitbreiteninformation, Initialisierungsbefehl)
lässt sich aber kein synergistischer Effekt, keine besondere kombinatorische Wirkung erkennen; vielmehr handelt es sich um eine einfache Aggregation, jede Teilmaßnahme funktioniert genau so, wie der Fachmann es erwarten durfte, und zeigt
nicht mehr als den vorhersehbaren Effekt.


3.5   Die Anmelderin hat vorgetragen, dass das beanspruchte Verfahren einen
Geschwindigkeitsvorteil gegenüber dem aus D5 bekannten Verfahren zum Erkennen der Taktfrequenz biete, für den der Stand der Technik keine Veranlassung
gebe und der eine erfinderische Tätigkeit erkennen lasse. Denn für den Fall, dass
die Speicherkarte nicht mit der ersten übertragenen Geschwindigkeit arbeiten
könne, werde anspruchsgemäß unmittelbar die zweite Geschwindigkeit eingestellt;
der in D5 beschriebene zusätzliche Schritt, erneut abzuwarten, ob die Karte eine
Antwort sendet, könne entfallen.


Dieses Argument vermochte den Senat nicht zu überzeugen. Gemäß D5 ist zwar
vorgesehen, nach dem Senden der zweiten Taktfrequenz abzuwarten, ob die

                                       - 13 -



Speicherkarte eine Antwort sendet (siehe D5 Figur 5 Schritt S5d, ggf. 15b). Diese
Abfrage bietet aber den Vorteil, solche Karten erkennen und auszusondern zu
können, die weder mit der einen noch mit der anderen Taktfrequenz betreibbar
sind; dem gegenüber steht der Nachteil einer zusätzlichen Warteschleife. Auf der
anderen Seite hat das beanspruchte Verfahren den Vorteil der höheren Geschwindigkeit, gegenüber dem Nachteil, Karten nicht erkennen zu können, die für beide
Taktfrequenzen ungeeignet sind – mit dem Risiko, dass das System hängenbleibt,
weil eine ungeeignete Karte keine Daten senden oder empfangen kann. Das Abwägen bekannter Vor- und Nachteile stellt jedoch lediglich typisches fachmännischen Handeln dar, mit dem sich das Vorliegen einer erfinderischen Tätigkeit nicht
begründen lässt (vgl. BGH GRUR 1996, 857 – Rauchgasklappe).


3.6   Die Anmelderin hat ferner geltend gemacht, dass es dem Fachmann zwar
vielleicht möglich gewesen wäre, die beanspruchten Verfahrensschritte in der beanspruchten Reihenfolge vorzuschlagen; er habe aber keinerlei Veranlassung
dazu gehabt („could-would-approach“), so dass sich das behauptete Naheliegen
erst in rückschauender Betrachtungsweise erschließe.


Dem ist entgegenzuhalten, dass sämtliche beanspruchten Einzelmaßnahmen dem
Fachmann vor dem Prioritätstag geläufig waren; sonach könnte allenfalls in der
konkreten Auswahl oder in der beanspruchten Reihenfolge der Arbeitsschritte eine
Besonderheit gesehen werden. Die Anmeldung enthält aber keine Begründung,
nennt keine besonderen Vorteile für die Auswahl oder Reihenfolge. Der Senat
kann hier nicht mehr als eine letztlich nach Belieben getroffene Festlegung als
eine von wenigen offenstehenden Möglichkeiten erkennen, die grundsätzlich nicht
geeignet ist, eine erfinderische Leistung zu begründen (vgl. BGH GRUR 2004, 47
– Blasenfreie Gummibahn I, mit Kritik am "could-would-test" (IV 3. c)).


3.7   Der Gegenstand des Patentanspruchs 1 nach Hauptantrag beruht nach
alledem nicht auf einer erfinderischen Tätigkeit, da die beanspruchten Maßnahmen, für sich betrachtet, im Rahmen des Wissens und Könnens des Durch-

                                       - 14 -



schnittsfachmanns lagen, und die beanspruchte Zusammenstellung und Reihenfolge nichts über das hinaus leistet, was der Fachmann in diesem Zusammenhang
erwartet hätte.


Mit dem Patentanspruch 1 fallen zwangsläufig auch die übrigen Ansprüche, da
über einen Antrag nur einheitlich entschieden werden kann.


4.     Zum Hilfsantrag


Der Patentanspruch 1 nach Hilfsantrag kann nicht anders beurteilt werden als
Patentanspruch 1 nach Hauptantrag, da das zusätzliche Merkmal ebenfalls keine
erfinderische Tätigkeit erforderte.


4.1    Patentanspruch 1 des Hilfsantrags unterscheidet sich vom Anspruch 1 des
Hauptantrags durch folgendes zusätzliches, zwischen den Merkmalen (a) und (b)
eingefügtes Merkmal:


       „(ax) über einen zum Übertragen von Daten zwischen der Host-Rechnereinheit und der elektronischen Schaltkreiskarte genutzten Kontakt (7) der Karte,“


D. h. dass die Übertragung der Geschwindigkeitsinformation SPEED_I in Schritt
(a) über einen Datenkontakt (7) der Schaltkreiskarte erfolgen soll.


4.2    Hier ist zunächst festzuhalten, dass für eine digitale Informationsübertragung überhaupt nur ein Datenkontakt oder der CMD-Kontakt infrage kommen, vgl.
D6 Tabelle 1 und Figur 7 – 14. Die Auswahl einer von zwei Möglichkeiten, ohne
dass ein besonderer Vorteil angegeben wird oder erkennbar ist, kann nicht als
erfinderische Leistung bewertet werden, vgl. oben 3.6.

                                       - 15 -



Die Anmelderin sieht in der Übertragung über den Datenkontakt bereits deswegen
einen besonderen Unterschied zu D5, weil dort die Geschwindigkeitsinformation in
Form des Anlegens einer Taktfrequenz übertragen wurde, nicht als Datenwort
über eine Datenleitung. Tatsächlich liegt darin ein gewisser prinzipieller Unterschied. Aber auch hier gilt, dass die Menge der Möglichkeiten, wie die erforderliche Geschwindigkeitsinformation vom Host zur Speicherkarte übertragen werden
kann, sehr stark begrenzt ist. Dabei wird der Durchschnittsfachmann berücksichtigen, dass eine Übertragung von Informationen in Form von Datenworten, d. h.
als digitale Daten, für Speicherkarten der in Rede stehenden Art üblich ist (vgl. D6
Figuren 7 – 14); er wird ein solches Verfahren daher gegenüber dem Anlegen
unterschiedlicher Frequenzen vorziehen, zumal dafür nicht vorgesehene Karten
durch letzteres möglicherweise sogar beschädigt werden könnten. Daher kann in
dem „Rückgriff“ auf die an sich übliche Art der Übertragung von digitalen Daten
keine erfinderische Leistung gesehen werden, ebensowenig wie in der Auswahl
eines von zwei möglichen Kontakten.


Dass der Fachmann keine konkrete Anregung erhielt, den Datenkontakt (7) zu
wählen, kann – mit derselben Begründung wie beim Hauptantrag, s. o. 3.6 – zu
keiner anderen Beurteilung führen.


4.3   Der Patentanspruch 1 des Hilfsantrags beruht daher nicht auf einer erfinderischen Tätigkeit. Auf die übrigen Ansprüche braucht nicht weiter eingegangen zu
werden, da über einen Antrag nur einheitlich entschieden werden kann.

                                       - 16 -




                                        III.


Die Beschwerde der Anmelderin gegen den Zurückweisungsbeschluss der
Prüfungsstelle war sonach zurückzuweisen.




Prasch        Dr. Mittenberger-Huber            Baumgardt   Dr. Thum-Rung




                                                                        Me
