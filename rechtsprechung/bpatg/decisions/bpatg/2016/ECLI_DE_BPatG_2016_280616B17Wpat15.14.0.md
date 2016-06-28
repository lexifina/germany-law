---
ecli: "ECLI:DE:BPatG:2016:280616B17Wpat15.14.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 15/14"
decided: "2016-06-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2016&Sort=1&Seite=29&nr=28357&anz=906&pos=442&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2016-06-28_17_W-pat_15_14_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0080.md"]
---

# Bundespatentgericht, 17 W (pat) 15/14 vom 2016-06-28

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 15/14                                                     Verkündet am
_______________                                                       28. Juni 2016
    (Aktenzeichen)                                                          …




                              BESCHLUSS

                            In der Beschwerdesache


             betreffend die Patentanmeldung 10 2009 054 567.0-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Juni 2016 unter Mitwirkung des Richters
Baumgardt     als    Vorsitzendem,   der   Richterin   Eder   sowie   der   Richter
Dipl.-Phys. Dr. Forkel und Dipl.-Ing. Hoffmann




BPatG 154
05.11

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 11. Dezember 2009 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


    „Verfahren und Vorrichtung zum Entwurf einer SEE-toleranten Schaltung“.


Die Anmeldung wurde von der Prüfungsstelle für Klasse G06F des Deutschen
Patent- und Markenamtes mit Beschluss vom 20. Februar 2014 aus Gründen des
Bescheids vom 12. November 2013 zurückgewiesen. Im genannten Bescheid
führt die Prüfungsstelle aus, dass der geltende Patentanspruch 1 mangels Neuheit
seiner Lehre (§ 3 PatG) nicht gewährbar sei.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Die Anmelderin stellt den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:


        gemäß Hauptantrag mit
        Patentansprüchen 1-10,
        Beschreibung Seiten 1-23 und
        4 Blatt Zeichnungen mit Figuren 1-4, jeweils vom Anmeldetag;

                                        -3-



        gemäß Hilfsantrag 1 mit
        Patentansprüchen 1-10, überreicht in der mündlichen Verhandlung,
        Beschreibung und Zeichnungen wie Hauptantrag;


        gemäß Hilfsantrag 2 mit
        Patentansprüchen 1-10, überreicht in der mündlichen Verhandlung,
        im Übrigen wie Hilfsantrag 1.


Die Anmelderin beantragt die Rückzahlung der Beschwerdegebühr.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt sind die Druckschriften


D1: DE 10 2007 024 983 A1


und


D2: DE 10 2006 055 867 A1


genannt worden.


Vom Senat wurden zusätzlich die Druckschriften


D3: SCHOOF, G.; METHFESSEL, M.; KRAEMER, R.: Fault-tolerant ASIC
Design for High System Dependability. In: Advanced Microsystems for Automotive Applications 2009, Part of the series VDI-Buch, pp 369-382, April 15,
2009,

                                         -4-



D4: LEHKY, M.; BILIK, S.: Reducing FPGA Design Modification Time. In:
VHDL International Users´ Forum, 1997, Proceedings


und


D5: SAMUDRALA, P.; RAMOS, J.; KATKOORI, S.: Selective Triple Modular
Redundancy (STMR) Based Single-Event Upset (SEU) Tolerant Synthesis for
FPGAs, IEEE Transactions on Nuclear Science, Vol. 51, No. 5, October 2004


eingeführt.


Der geltende Patentanspruch 1 gemäß Hauptantrag, hier mit einer möglichen
Gliederung versehen, lautet:


(a)   Verfahren (400) zum Entwurf einer Single-Event-Effekt-(SEE-)toleranten
      Schaltung, umfassend die Schritte:


(b)   Bereitstellen (410) einer ersten Gatternetzliste, die ein Verhalten der zu entwerfenden SEE-toleranten Schaltung durch Spezifizierung einer Vielzahl
      Logikschaltungsmodelle und/oder Speicherschaltungsmodelle sowie deren
      Verschaltung untereinander abbildet;


(c)   Bereitstellen (420) einer Zellenbibliothek, die ein fehlertolerantes Logikschaltungsmodell umfasst, das eine selbe logische Funktion wie eines aus der Vielzahl Logikschaltungsmodelle der ersten Gatternetzliste erfüllt und diesem
      zugeordnet ist, und/oder ein fehlertolerantes Speicherschaltungsmodell, das
      eine selbe Speicherfunktion wie eines aus der Vielzahl Speicherschaltungsmodelle der ersten Gatternetzliste erfüllt und diesem zugeordnet ist;


(d)   Modifizieren (430) der ersten Gatternetzliste derart, dass mindestens ein
      Logikschaltungsmodell der ersten Gatternetzliste durch das zugeordnete feh-

                                         -5-



      lertolerante Logikschaltungsmodell und/oder mindestens ein Speicherschaltungsmodell durch das zugeordnete fehlertolerante Speicherschaltungsmodell
      aus der Zellenbibliothek ersetzt wird;


(e)   Erzeugen (440) einer redundanten zweiten Gatternetzliste aus der ersten Gatternetzliste, wobei die zweite Gatternetzliste mit der ersten Gatternetzliste
      identisch ist; und


(f)   Verknüpfen (450) der ersten und der zweiten Gatternetzliste zu einer dritten
      Gatternetzliste, anhand der die SEE-tolerante Schaltung hergestellt werden
      kann, wobei für ein jeweiliges Logikschaltungsmodell und/oder ein jeweiliges
      Speicherschaltungsmodell der ersten Gatternetzliste eine erste Verbindungsleitung zu einem ersten Versorgungsspannungsanschluss eines für die zu
      entwerfende Schaltung designierten Trägerelements sowie für ein jeweiliges
      Logikschaltungsmodell und/oder ein jeweiliges Speicherschaltungsmodell der
      zweiten Gatternetzliste eine zweite Verbindungsleitung zu einem zweiten Versorgungsspannungsanschluss des Trägerelementes vorgesehen werden und


(g)   eine dritte Verbindungsleitung zwischen einem Ausgang eines jeweiligen fehlertoleranten Logikschaltungsmodells der ersten Gatternetzliste und einem
      Eingang eines zu dem jeweiligen fehlertoleranten Logikschaltungsmodell
      redundanten fehlertoleranten Logikschaltungsmodells der zweiten Gatternetzliste sowie eine vierte Verbindungsleitung zwischen einem Ausgang des
      redundanten fehlertoleranten Logikschaltungsmodells der zweiten Gatternetzliste und einem Eingang des jeweiligen fehlertoleranten Logikschaltungsmodells der ersten Gatternetzliste vorgesehen werden und/oder


(h)   zwischen einem jeweiligen fehlertoleranten Speicherschaltungsmodell der
      ersten Gatternetzliste und einem zu diesem redundanten fehlertoleranten
      Speicherschaltungsmodell der zweiten Gatternetzliste eine Synchronisationsleitung vorgesehen wird.

                                       -6-



Zu den nebengeordneten Patentansprüchen 7 bis 10 sowie zu den abhängigen
Patentansprüchen 2 bis 6 gemäß Hauptantrag wird auf die Akte verwiesen.


Der Patentanspruch 1 gemäß Hilfsantrag 1 unterscheidet sich vom Patentanspruch 1 gemäß Hauptantrag durch das Merkmal (e1), welches sich an das Merkmal (e) anschließen soll:


(e1) „wobei die Logik- und Speicherschaltungsmodelle der ersten und zweiten
     Gatternetzliste eindeutig referenzierbar benannt werden; und“


Bezüglich der Patentansprüche 2 bis 10 wird auf den Akteninhalt hingewiesen.


Der Patentanspruch 1 gemäß Hilfsantrag 2 unterscheidet sich vom Patentanspruch 1 gemäß Hauptantrag lediglich durch das Merkmal (a´), welches an die
Stelle von Merkmal (a) treten soll:


(a´) „Betriebsverfahren für eine Datenverarbeitungsvorrichtung zum Entwurf einer
     Single-Event-Effekt-(SEE-)toleranten Schaltung, umfassend die Schritte:“


In Hinblick auf die Patentansprüche 2 bis 10 wird wieder auf die Akte verwiesen.


Die Anmelderin trägt vor, dass der Vorteil des Gegenstandes der Anmeldung in
der einfachen Automatisierbarkeit eines Entwurfs eines Layouts für eine fehlertolerante Schaltung liege. Ein ursprüngliches Schaltungslayout in Form einer Gatternetzliste für eine nicht-fehlertolerante Schaltung könne durch das beanspruchte
Verfahren automatisiert in ein Schaltungslayout für eine fehlertolerante Schaltung
in Form einer weiteren Netzliste überführt werden, wobei dieselbe grundlegende
technische Funktion der Schaltung erhalten bleibe.

                                       -7-



Die jeweiligen Gegenstände nach Patentanspruch 1 gemäß Hauptantrag sowie
den Hilfsanträgen 1 und 2 seien dem Patentschutz grundsätzlich zugänglich. Sie
seien außerdem neu und beruhten auch auf erfinderischer Tätigkeit.




                                        II.


Die Beschwerde wurde rechtzeitig eingelegt und ist auch sonst zulässig. Sie hat
jedoch keinen Erfolg, da die jeweiligen Verfahren des Patentanspruchs 1 nach
Hauptantrag sowie nach den Hilfsanträgen 1 und 2 nicht auf erfinderischer Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).


1.    Die vorliegende Patentanmeldung bezieht sich auf ein Verfahren und eine
Vorrichtung zum Entwurf einer Single-Event-Effekt-(SEE-)toleranten Schaltung,
insbesondere einer Schaltung in Doppelmodular-Redundanzstruktur (Offenlegungsschrift, [0001]).


Ausweislich der Anmeldung können beim Betrieb einer Schaltung in einem Anwendungsfeld, das einer erhöhten elektromagnetischen Strahlung oder einer Teilchenstrahlung (wie etwa Alpha-, Neutronen- und/oder Protonenstrahlung oder
kosmische Strahlung) ausgesetzt ist, sogenannte Single-Event-Effekte zu einem
fehlerhaften Verhalten der Schaltung führen. Derartige Umgebungsbedingungen
finden sich z. B. im Weltraum, in der Nähe von Kernreaktoren oder Teilchenbeschleunigern. Single-Event-Effekte treten bezogen auf die Taktfrequenz der Schaltung selten auf, so dass sie zeitlich als einzelne und nicht etwa als gleichzeitig
mehrfach auftretende Ereignisse betrachtet werden können (Offenlegungsschrift,
[0004]). Zu den Single-Event-Effekten zählt insbesondere der sogenannte Single-Event-Upset (SEU), aufgrund dessen sich der Zustand mindestens einer Einbitspeicherzelle ändert. Zwar bewirkt der Single-Event-Upset keinen dauerhaften
Schaden in der Schaltung, jedoch kann er zu einem fehlerhaften Verhalten der
Schaltung führen (Offenlegungsschrift, [0005]). Der demgegenüber seltener auf-

                                        -8-



tretende Single-Event-Latchup (SEL) kann hingegen eine irreversible thermische
Zerstörung der Schaltung herbeiführen, indem beispielsweise ein parasitäres
Halbleiterbauelement der Schaltung, wie etwa eine parasitäre Transistorschaltung,
in einen niederohmigen Zustand übergeht und so zu einem elektrischen Kurzschluss zwischen Betriebsspannung und Masse führt. Eine Möglichkeit, eine dauerhafte Zerstörung zu verhindern, besteht darin, den durch den niederohmigen
Zustand erhöhten Stromfluss zu unterbrechen (Offenlegungsschrift, [0006]). Um
Single-Event-Latchups zu vermeiden, werden bekanntlich strukturelle Gegenmaßnahmen getroffen, z. B. eine Vergrößerung der Abstände der Source-Drain-Gebiete zu den Wannenrändern. Eine andere Strategie zielt nicht auf die Vermeidung von Single-Event-Latchups, sondern auf deren Handhabung, beispielsweise
durch schaltungstechnische Gegenmaßnahmen, wie die Integration einer Schaltung zur Strombegrenzung der Energieversorgung der Schaltung. Zur Handhabung von Single-Event-Upsets werden im Wesentlichen beim Entwurf der Schaltung redundante Strukturen angestrebt, wie beispielsweise eine Triple-Modular-Redundancy (TMR)-Struktur. In einer solchen Struktur wird die Schaltung dreifach
ausgeführt (Offenlegungsschrift, [0007]).


Obwohl Schaltungskonzepte zur Vermeidung oder Handhabung von Single-Event-Effekten aus dem Stand der Technik bekannt sind, mangelt es an automatisierbaren Verfahren zum Entwurf solcher SEE-toleranten Schaltungen, insbesondere an
Verfahren, die mit Entwurfsprozessen für herkömmliche und nicht SEE-tolerante
Schaltungen kompatibel sind (Offenlegungsschrift, [0010]).


Als Aufgabe wird in der Anmeldung genannt, ein Verfahren oder eine Vorrichtung
bereitzustellen, das einen weitestgehend automatisierbaren Entwurf einer SEE-
toleranten Schaltung erlaubt (Offenlegungsschrift, [0012]).


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zum Entwurf einer
SEE-toleranten Schaltung zu verbessern, ist ein Informatiker mit Hochschul- oder
Fachhochschulabschluss anzusehen, der über eine mehrjährige Berufserfahrung

                                        -9-



auf dem Gebiet des computergestützten Schaltungsentwurfs und der Schaltungssimulation verfügt und der einen Ingenieur der Fachrichtung Elektrotechnik mit
fundierten Kenntnissen in der Mikroelektronik wegen des Designs integrierter
Schaltungen hinzuziehen wird.


2.    Der Hauptantrag ist nicht gewährbar, weil es dem Verfahren seines Patentanspruchs 1 an der für die Patentfähigkeit erforderlichen erfinderischen Tätigkeit
mangelt.


2.1   Zur Lehre des Patentanspruchs 1 gemäß Hauptantrag


Zur Lösung der oben genannten Aufgabe schlägt der Patentanspruch 1 ein Verfahren zum Entwurf einer Single-Event-Effekt-(SEE-)toleranten Schaltung vor
(Merkmal (a)).


Das beanspruchte Verfahren beginnt mit der Bereitstellung einer Gatternetzliste.
Die Gatternetzliste bildet ein Verhalten der zu entwerfenden SEE-toleranten
Schaltung ab. Hierzu spezifiziert sie eine Vielzahl von Logikschaltungsmodellen
und/oder Speicherschaltungsmodellen sowie deren Verschaltung untereinander, je
nach Funktion der zu entwerfenden SEE-toleranten Schaltung (Merkmal (b)).


Nach dem Entwurf der ersten Gatternetzliste mit Hilfe einer Standardbibliothek
wird eine Zellenbibliothek bereitgestellt, die wenigstens ein fehlertolerantes Logikschaltungsmodell und/oder wenigstens ein fehlertolerantes Speicherschaltungsmodell umfasst. Sowohl das Logik- als auch das Speicherschaltungsmodell der
bereitgestellten Zellenbibliothek sind zum einen fehlertolerant in Hinblick auf SEE
und haben zum anderen dieselbe Funktion wie ein entsprechendes Logikschaltungsmodell bzw. Speicherschaltungsmodell der in Merkmal (b) bereitgestellten
ersten Gatternetzliste. Weiterhin liegt eine Zuordnung zwischen den Standard-Schaltungsmodellen, wie sie in der ersten Gatternetzliste Verwendung finden, und

                                          - 10 -



den fehlertoleranten Schaltungsmodellen, die in der Zellenbibliothek enthalten
sind, vor (Merkmal (c)).


Gemäß Merkmal (d) wird die bereitgestellte erste Gatternetzliste modifiziert. Die
Veränderung soll derart erfolgen, dass mindestens ein Logikschaltungsmodell der
ersten Gatternetzliste durch das zugeordnete, fehlertolerante Logikschaltungsmodell und/oder mindestens ein Speicherschaltungsmodell durch das zugeordnete
fehlertolerante Speicherschaltungsmodell aus der gemäß Merkmal (c) bereitgestellten Zellenbibliothek ersetzt wird.


Anschließend wird eine zur ersten Gatternetzliste redundante und identische
zweite Gatternetzliste erzeugt (Merkmal (e)). Erste und zweite Gatternetzliste werden laut Merkmal (f) zu einer dritten Gatternetzliste verknüpft, anhand der die
SEE-tolerante Schaltung hergestellt werden kann. Merkmal (f) sieht außerdem
vor, dass für ein jeweiliges Logikschaltungsmodell und/oder ein jeweiliges Speicherschaltungsmodell aus der ersten Gatternetzliste in der dritten Gatternetzliste
eine erste Verbindungsleitung zu einem ersten Versorgungsspannungsanschluss
eines Trägerelements hergestellt wird, welches für die zu entwerfende Schaltung
vorgesehen ist. Darüber hinaus besagt Merkmal (f), dass ein jeweiliges Logikschaltungsmodell und/oder ein jeweiliges Speicherschaltungsmodell aus der zweiten Gatternetzliste über eine zweite Verbindungsleitung an einen zweiten Versorgungsspannungsanschluss des Trägerelementes angebunden wird.


Merkmal (g) sieht zum einen vor, dass zwischen einem Ausgang eines jeweiligen
fehlertoleranten Logikschaltungsmodells der ersten Gatternetzliste und einem Eingang eines zu einem jeweiligen fehlertoleranten Logikschaltungsmodell redundanten fehlertoleranten Logikschaltungsmodell der zweiten Gatternetzliste eine
dritte Verbindungsleitung hergestellt wird. Zum anderen ist laut Merkmal (g) eine
vierte Verbindungsleitung vorgesehen, und zwar zwischen einem Ausgang des
redundanten fehlertoleranten Logikschaltungsmodells der zweiten Gatternetzliste

                                       - 11 -



und einem Eingang des jeweiligen fehlertoleranten Logikschaltungsmodells der
ersten Gatternetzliste.


Merkmal (h) besagt noch, dass zwischen einem jeweiligen fehlertoleranten Speicherschaltungsmodell der ersten Gatternetzliste und einem zu diesem redundanten fehlertoleranten Speicherschaltungsmodell der zweiten Gatternetzliste eine
Synchronisationsleitung vorgesehen ist.


2.2   Zur Beurteilung der beanspruchten Lehre ist die Druckschrift D3 von besonderer Bedeutung.


Bei der Druckschrift D3 handelt es sich um einen Fachartikel über ein fehlertolerantes Design einer anwendungsspezifischen integrierten Schaltung für hohe
Zuverlässigkeit. Der Artikel beschreibt neue Verfahren und Designkonzepte, um in
der Fahrzeugelektronik durch Single-Event-Effekte an ASICS hervorgerufene
Schädigungen abzuschwächen. Die vorgestellten Konzepte basieren auf dem Entwurf fehlertoleranter Schaltungen, die die Zuverlässigkeit der elektronischen Komponenten erhöhen, aber zugleich das Echtzeitverhalten des gesamten Systems
nicht beeinträchtigen (Abstract).


Damit offenbart die Druckschrift D3 ein Verfahren zum Entwurf einer Single-Event-Effekt-(SEE-)toleranten Schaltung (Seite 377, Abschnitt 3.3 – „ASIC Design
Flow“). Bei der fehlertoleranten Schaltung handelt es sich um eine anwendungsspezifische integrierte Schaltung (ASIC), für die mit Hilfe einer Entwurfssoftware
(„newly developed tool“) ein Design mit Schutz gegen Störsignale, wie Single
Event Updates (SEUs) und Single Event Latchups (SELs) entwickelt werden soll
(Seite 377, dritter Absatz – Merkmal (a)).


Ausgangspunkt des bekannten Verfahrens zum Entwurf einer fehlertoleranten
Schaltung bildet eine erste Netzliste (Seite 377, zweiter Absatz, siehe „existing
netlist“). Dem Fachmann ist geläufig, dass eine solche Netzliste eine strukturelle

                                       - 12 -



Repräsentation darstellt, die eine funktionale Verhaltensbeschreibung bzw. ein
Verhaltensmodell einer digitalen Schaltung (z. B. in VHDL) auf die logischen
Modelle von Schaltungskomponenten, z. B. Gatter oder Register abbildet sowie
deren Verbindungen charakterisiert. Logik- und Speicherschaltungsmodelle in Gestalt von kombinatorischer Logik („combinational logic“, d. h. Logikgatter zur Realisierung Boolescher Funktionen) und Flipflops (also elementare Ein-Bit-Speicher)
sind außerdem wesentlicher Bestandteil der in der Druckschrift D3 wiedergegebenen Schaltungen (z. B. Figuren 1-5) und damit auch der zugeordneten Netzlisten, die den Ausgangspunkt für die fehlertoleranten SEE-Designvarianten bilden
(Merkmal (b)).


In der Druckschrift D3 wird mittels einer Software aus der ersten Netzliste eine
DMR-Netzliste generiert (Seite 377, zweiter Absatz), die erste Netzliste wird also
modifiziert, d. h. wenigstens eine Schaltungskomponente oder Teilschaltung der
ersten Netzliste wird durch eine fehlertolerante Ausführung ersetzt. Eine solche
DMR-Netzliste bildet Doppel-Modular-Redundanz ab und entspricht demnach fehlertoleranten Schaltungen wie sie etwa in den Figuren 3 bis 5 auf den Seiten 373
bis 375 dargestellt sind. Dabei ist für den Fachmann selbstverständlich, dass die
Struktur der DMR-Netzliste auf Komponentenmodellen beruht, die den in den
Abbildungen gezeigten Logik- und Speicherschaltungen entsprechen (teilweise
Merkmal (d)).


Der Druckschrift D3 ist aber weder die Bereitstellung einer Zellenbibliothek mit
zugeordneten fehlertoleranten Schaltungsmodellen i. S. d. Merkmals (c) noch
deren Verwendung zu entnehmen (restlicher Teil von Merkmal (d)).


Außerdem geht aus der Druckschrift D3 nicht unmittelbar hervor, aus der modifizierten Netzliste eine redundante zweite Netzliste zu erzeugen (Merkmal (e)).


Um die DMR-Netzliste bzw. das DMR-Design noch mit einem wirksamen Schutz
gegen Single-Event-Latchups (SELs) auszustatten, kommt laut Druckschrift D3

                                       - 13 -



eine weitere Anwendungssoftware zum Einsatz (Seite 380, dritter Absatz). Sämtliche Änderungen am DMR-Design laufen demnach weitgehend automatisiert ab.
Das Ergebnis eines fehlertoleranten Schaltungsentwurfs mit kombiniertem SEU-/
SEL-Schutz ist in Figur 8 (Seite 379) der Druckschrift D3 wiedergegeben. Dass
das dort vorgestellte Design mit einer eigenen, neuen Gatternetzliste korrespondiert, deren (redundante) Schaltungskomponenten sich aus der modifizierten ersten Netzliste - einer DMR-Netzliste - ergeben bzw. auf einer solchen beruhen, wird
vom Fachmann auf Seite 377 (zweiter und dritter Absatz) und Seite 380 (dritter
Absatz) im Rahmen der Ausführungen zum angewandten zweistufigen Entwurfsverfahren mitgelesen. Um den kombinierten SEU-/SEL-Schutz zu erreichen, wird
das aus der Figur 4 bekannte volle DMR-Design gemäß den Ausführungen unter
Abschnitt 4.1 in zwei DMR-Subsysteme SYSA und SYSB dupliziert und zusätzlich
mit SEL Steuerungen und Stromschaltern versehen (siehe Seite 378, zweiter
Absatz, siehe „The system necessarily must be doubled and SEL controllers and
power switches are added…“). Entsprechend Figur 8 sind beide Subsysteme
SYSA und SYSB (mit Logik CL, Speicher-Flipflops FF und Votern V) über zwei
separate Verbindungsleitungen VDDA und VDDB an die Versorgungsspannung
VDD angebunden. Als Trägerelement sowohl für die Anschlüsse der Versorgungsspannung als auch der jeweiligen Schaltungskomponenten soll laut Druckschrift D3 ein Chip, d. h. ein integrierter Schaltkreis auf Halbleitersubstrat dienen
(Seite 378, zweiter Absatz, siehe „system-on-chip“ – teilweise Merkmal (f)).


Weiterhin ist der Figur 8 aus Druckschrift D3 zu entnehmen, dass zwischen einem
Ausgang der fehlertoleranten Logikschaltung des Subsystems SYSA und einem
Eingang der redundanten fehlertoleranten Logikschaltung des Subsystems SYSB
eine dritte Verbindungsleitung vorgesehen ist (FFA  VB) und der Ausgang der
redundanten fehlertoleranten Logikschaltung des Subsystems SYSB über eine
vierte Verbindungsleitung mit dem Eingang der fehlertoleranten Logikschaltung
des Subsystems SYSA verbunden ist (VA  FFB) (teilweise Merkmal (g)).

                                      - 14 -



Eine Synchronisation zwischen den redundanten Subsystemen nach einem SEL
erfolgt automatisch mittels der Verbindungen zwischen den Votern bzw. Auswahlschaltungen und den Speicherflipflops (Seite 379, zweiter Absatz – teilweise Merkmal (h)).


Dass das bekannte Schaltungsdesign mit SEU- und SEL-Schutz aus der Verknüpfung zweier identischer Gatternetzlisten zu einer dritten Gatternetzliste entsteht,
geht aber aus der Druckschrift direkt nicht hervor. Dementsprechend ist aus der
Druckschrift auch nicht bekannt, dass die beiden DMR-Subsysteme mit Logik- und
Speicherschaltungen aus unterschiedlichen Netzlisten stammen (restliche Teile
der Merkmale (f), (g) und (h)).


2.3    Der Gegenstand des Patentanspruchs 1 gemäß Hauptantrag ist durch den
aus der Druckschrift D3 bekannten Stand der Technik nahegelegt.


Dem Fachmann ist geläufig, zur Struktur- und Verhaltensbeschreibung von Schaltkreisen (z. B. unter VHDL) oft gebrauchte Funktionen, Prozeduren und Komponenten in Bibliotheken vorzuhalten und zu pflegen. Dementsprechend lag es für
ihn auf der Hand, für den Entwurf SEE-toleranter Schaltungen gemäß Druckschrift D3 fehlertolerante Komponenten in Bibliotheken zur Wiederverwendung
geordnet abzulegen. Dass dem Fachmann die Verwendung solcher Bibliotheken
bereits vor dem Zeitrang der Anmeldung hinlänglich bekannt war, ergibt sich z. B.
aus der Druckschrift D5, in der bereits eingangs auf die Verwendung von Bibliotheken aus SEU toleranten Basisgattern und Speicherzellen beim Design elektronischer Bausteine hingewiesen wird (Seite 1, rechte Spalte, siehe „Design hardening is one of the techniques … adding a few additional transistors.“). Die in den
Merkmalen (c) und (d) zusätzlich beanspruchte Zuordnung fehlertoleranter Schaltungsmodelle zu den in der als Ausgangspunkt gewählten Netzliste zu ersetzenden Schaltungsmodellen stellt aus Sicht des Fachmannes ein zwingendes Erfordernis dar, um im Rahmen eines weitgehend automatisierten Entwurfsverfahrens
einerseits die Gesamtfunktionalität der durch die Netzliste vorgegebenen Schal-

                                       - 15 -



tung auch im DMR Design zu verwirklichen und andererseits die Schaltung gegenüber Strahlungsfehlern robust zu machen (Merkmal (c), restlicher Teil von Merkmal (d)).


Weiterhin erhält der Fachmann aus der Druckschrift D3 die Anregung, einen fehlertoleranten Schaltungsentwurf ausgehend von der Netzlistenebene durchzuführen, was u. a. die Wiederverwendung bereits erzeugter Netzlisten gestattet
(Seite 377, erster Absatz). Aufgrund dieses Hinweises und aufgrund der Erkenntnis, dass die Erzeugung eines fehlertoleranten Designs mit kombiniertem SEU-
und SEL-Schutz im Wesentlichen aus der Verdoppelung eines DMR-Designs
resultiert (Seite 378, Abschnitt 4.1) hatte der Fachmann Veranlassung, zum Entwurf einer SEE-toleranten Schaltung einmal erzeugte Netzlisten, wie z. B. DMR-Netzlisten mit ihren Schaltungsmodellen einfach zu duplizieren und in geeigneter
Weise miteinander zu verbinden (Merkmal (e), restliche Teile der Merkmale (f), (g)
und (h)). Dass dabei dem Fachmann die Verknüpfung separater Netzlisten mit
unterschiedlichen Schaltungskomponenten und deren Verbindungen zum Zeitpunkt der Anmeldung bereits geläufig war, zeigt u. a. die Druckschrift D4, die eine
inkrementelle Logiksynthese zur Modifizierung eines FPGA Designs offenbart
(Seite 146, rechte Spalte, zweiter bis sechster Absatz).


Die Anmelderin argumentiert, dass die beanspruchte Zellenbibliothek derart ausgelegt sei, dass zwischen nicht-fehlertoleranten und fehlertoleranten Schaltungsmodellen Zuordnungen bestünden. Aus der Druckschrift D5 seien aber lediglich
Zellenbibliotheken ohne Zuordnung bekannt, so dass der Fachmann passende
Schaltungsmodelle aus der Bibliothek zuerst heraussuchen müsse. Zwar ist der
Anmelderin darin zuzustimmen, dass aus der Druckschrift D5 eine Zellenbibliothek
mit einander zugeordneten nicht-fehlertoleranten und fehlertoleranten Schaltungsmodellen nicht unmittelbar entnehmbar ist. Der zuständige Fachmann entnimmt
aber der Druckschrift D3 die Implementierung eines weitgehend automatisierten
Ansatzes für den Schaltungsentwurf (Seite 377, erster Absatz; Seite 380, dritter
Absatz). Für ein solches Entwurfsverfahren stellt die Zuordnung von nicht-fehler-

                                      - 16 -



toleranten zu fehlertoleranten Schaltungsmodellen eine zwingende Notwendigkeit
dar, wenn aus einer vorgegebenen Netzliste ohne Eingriffe seitens des Benutzers
eine DMR Netzliste erzeugt werden soll.


Die Anmelderin führt weiterhin aus, dass zwar der Fachmann in der SEE-toleranten Schaltung der Figur 8 eine Netzliste mitlesen möge, er jedoch dabei nicht mitlese, mit welchen Maßnahmen und in welcher Reihenfolge dieser Maßnahmen
diese Netzliste erstellt werde. Insbesondere sei das Verknüpfen einer ersten und
zweiten Gatternetzliste zu einer dritten Netzliste aus der Druckschrift D3 weder
bekannt noch nahegelegt. Auch dieser Einwand der Anmelderin vermochte nicht
zu überzeugen. Gerade weil die Druckschrift D3 vorschlägt, fehlertolerante Schaltungen ausgehend von Netzlisten zu erzeugen, um bereits erstellte Netzlisten wiederverwenden zu können, bot es sich dem Fachmann an, einmal erzeugte DMR
Netzlisten zu kopieren und die so erzeugten Netzlisten entsprechend dem Design
der gewünschten redundant ausgelegten Schaltungsanordnung konsistent miteinander zu verknüpfen.


Es waren für den Fachmann somit lediglich fachgemäße Überlegungen erforderlich, um in Kenntnis der Druckschrift D3 zu einem Verfahren mit sämtlichen Merkmalen des Patentanspruchs 1 in der Fassung des Hauptantrags zu gelangen.


2.4    Da über einen Antrag nur einheitlich entschieden werden kann, sind auch
die Patentansprüche 2 bis 10 gemäß Hauptantrag nicht gewährbar (BGH GRUR
1997, 120 – Elektrisches Speicherheizgerät).


3.     Die Hilfsanträge 1 und 2 können nicht günstiger als der Hauptantrag beurteilt werden.


3.1    Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 1 beruht nicht
auf erfinderischer Tätigkeit, weil das zusätzliche Merkmal (e1) durch den Stand
der Technik nahegelegt ist.

                                      - 17 -



3.1.1 Der auf ein Verfahren gerichtete Patentanspruch 1 gemäß Hilfsantrag 1
umfasst sämtliche Merkmale des Patentanspruchs 1 gemäß Hauptantrag, unterscheidet sich von diesem aber durch das zusätzliche Merkmal (e1):


(e1)   „wobei die Logik- und Speicherschaltungsmodelle der ersten und zweiten
       Gatternetzliste eindeutig referenzierbar benannt werden; und“.


Laut Merkmal (e1) sollen die Schaltungsmodelle der ersten und zweiten Gatternetzliste so benannt werden, dass sie eindeutig referenziert werden können. In der
Beschreibung wird hierzu ausgeführt, dass nach dem Erzeugen der zweiten aus
der ersten Gatternetzliste alle Elemente der zweiten Gatternetzliste neu benannt
werden, so dass jedes Element der ersten und der zweiten Gatternetzliste eindeutig angesprochen werden kann (Offenlegungsschrift, [0082]).


3.1.2 Da der Fachmann nicht nur bestrebt ist, Schaltkreise zu entwerfen, sondern
diese auch zu simulieren, lag es für ihn nahe, die in den jeweiligen Netzlisten der
SEE-toleranten Schaltungen enthaltenen Schaltungsmodelle noch vor deren Verknüpfung mit eindeutigen Bezeichnungen zu versehen, so dass die jeweiligen
Modelle mit ihren Ein- und Ausgängen nicht nur konsistent und eindeutig auf Netzlistenebene miteinander verbunden werden können, sondern auch bei der Validierung des gesamten Schaltungsentwurfs mittels eines Logiksimulators eindeutig
adressiert werden können (Merkmal (e1)).


3.1.3 Der Patentanspruch 1 gemäß Hilfsantrag 1 ist nach allem nicht gewährbar,
da auch das Merkmal (e1) eine erfinderische Tätigkeit nicht begründen kann.


3.2    Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2 ergab sich in
naheliegender Weise aus dem aufgezeigten Stand der Technik.

                                      - 18 -



3.2.1 Der Patentanspruch 1 gemäß Hilfsantrag 2 unterscheidet sich vom Patentanspruch 1 gemäß Hauptantrag lediglich in Merkmal (a´), welches an die Stelle
von Merkmal (a) treten soll:


(a´)   „Betriebsverfahren für eine Datenverarbeitungsvorrichtung zum Entwurf
       einer Single-Event-Effekt-(SEE-)toleranten Schaltung, umfassend die Schritte:“


Mit dem Merkmal (a´) wird lediglich präzisiert, dass das mit dem Patentanspruch 1
gemäß Hauptantrag beanspruchte Verfahren zum Entwurf einer SEE-toleranten
Schaltung auf einer Datenverarbeitungsvorrichtung (automatisiert) abgearbeitet
werden soll.


3.2.2 Aus der Druckschrift D3 geht aber gerade hervor, dass das dort angesprochene Entwurfsverfahren als Entwicklungswerkzeug („tool“) implementiert ist, das
den Schaltungsentwurf weitgehend automatisiert durchführen kann (Seite 377,
Abschnitt 3.3). Der Fachmann wird in dem Werkzeug eine Anwendung bzw. eine
Software erkennen, die auf einem Computersystem, also einer Datenverarbeitungsvorrichtung abläuft. Merkmal (a´) ist somit aus der Druckschrift D3 bekannt.


3.2.3 Unter Berücksichtigung der Ausführungen zum Hauptantrag ist auch der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag 2 aus der Druckschrift D3
nahegelegt.


3.3    Mit dem jeweiligen Patentanspruch 1 gemäß Hilfsantrag 1 und 2 fallen auch
die jeweils zugehörigen Patentansprüche 2 bis 10.


4.     Für die Rückzahlung der Beschwerdegebühr gemäß § 80 Abs. 3 PatG
bestand keine Veranlassung.

                                      - 19 -



Ob die Beschwerdegebühr zurückgezahlt wird, steht im pflichtgemäßen Ermessen
des Senats. Sie ist veranlasst, wenn es aufgrund besonderer Umstände unbillig
wäre, die Gebühr einzubehalten. Maßgebend sind dafür alle Umstände des Falles
(Benkard, Patentgesetz, 11. Aufl., § 80 Rdn. 22; Schulte, PatG, 9. Auflage (2014),
§ 73 Rdn. 123 ff., § 80 Rdn. 111 ff.). Die Billigkeit der Rückzahlung kann sich
danach aus einem Verfahrensverstoß durch das Deutsche Patent- und Markenamt
ergeben (Schulte, a. a. O. § 73 Rdn. 131, 145; Benkard a. a. O. § 80 Rdn. 23, 27;
BPatG BIPMZ 2006, 372, 374 – Frequenzsignal; BPatGE 47, 224, 231 – Mikroprozessor; 49, 154, 161 ff. – Tragbares Gerät; BPaG Mitt. 2010, 41, 43 – Mobilfunknetzwerk).


Eine fehlerhafte Begründung der Entscheidung oder eine sachliche Fehlbeurteilung durch die Prüfungsstelle genügen dem noch nicht. Hinzukommen müssten
noch besondere Umstände, die das Einbehalten der Gebühr als ungerecht
erscheinen ließen (vgl. Schulte a. a. O.). Davon kann im vorliegenden Fall aber
nicht die Rede sein. Ein schwerwiegender Verfahrensfehler oder eine unangemessene Sachbehandlung sind nicht ersichtlich. Ein grober Verstoß gegen die Verfahrensökonomie kann im Ablauf des Prüfungsverfahrens ebenfalls nicht erkannt werden.




                                       III.


Nachdem keiner der gestellten Anträge Erfolg hatte, war die Beschwerde der
Anmelderin gegen den Zurückweisungsbeschluss der Prüfungsstelle für Klasse G06F des Deutschen Patent- und Markenamtes zurückzuweisen.

                                            - 20 -



                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht
zugelassen hat, ist sie nur statthaft, wenn gerügt wird, dass


   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes
      kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war, sofern er
      nicht der Führung des Verfahrens ausdrücklich oder stillschweigend zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim
Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich
einzulegen.




Baumgardt                    Eder                     Dr. Forkel                  Hoffmann




                                                                                           Fa
