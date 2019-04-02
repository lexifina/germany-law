---
ecli: "ECLI:DE:BPatG:2019:020419B17Wpat53.16.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 53/16"
decided: "2019-04-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=15&nr=34969&anz=817&pos=228&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-04-02_17_W-pat_53_16_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 53/16 vom 2019-04-02

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 53/16                                                   Verkündet am
 _______________                                                    2. April 2019
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


            betreffend die Patentanmeldung 10 2008 040 009.2 - 53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 2. April 2019 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der    Richterin   Eder,   des   Richters
Dipl.-Ing. Baumgardt und des Richters Dipl.-Phys. Dr. Forkel


beschlossen:


                      Die Beschwerde wird zurückgewiesen.




ECLI:DE:BPatG:2019:020419B17Wpat53.16.0

                                       -2-



                                    Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 27. August 2008 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung


              „Lastverteiltes Zuweisen von medizinischen Taskflows
                          auf Server einer Serverfarm“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 F des
Deutschen Patent- und Markenamts in der Anhörung vom 17. August 2016 mit der
Begründung zurückgewiesen, dass der Gegenstand des Patentanspruchs 1 weder
in der Fassung des Hauptantrags noch in der Fassung der (damals geltenden)
Hilfsanträge 1 bis 3 patentfähig sei; denn er beruhe gegenüber der Druckschrift D1
(s. u.) nicht auf einer erfinderischen Tätigkeit, wobei ggf. einzelne Merkmale, die
zur Lösung eines technischen Problems nicht beitragen, außer Acht zu lassen
seien.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie trägt
vor, der beanspruchte Gegenstand unterscheide sich von der Druckschrift D1
nicht nur durch die von der Prüfungsstelle genannten drei, sondern durch insgesamt sieben (einzeln erörterte) Merkmale bzw. Merkmalselemente. Des Weiteren
seien grundsätzlich alle Anspruchsmerkmale zu berücksichtigen, denn die Erfindung sei in ihrer Gesamtheit zu werten, sie dürfe gedanklich nicht in ihre Bestandteile zerlegt werden (unter Verweis auf Schulte, PatG, 8. Auflage, § 4
Rdnr. 9). Die Druckschrift D2 zeige ebenfalls eine andere Architektur. Auch die
neu eingeführten Druckschriften D3 und D4 (s. u.) gingen von anderen Systemstrukturen aus. Insbesondere seien die nunmehr geltenden unabhängigen Ansprüche 1 und 15 neu und erfinderisch gegenüber dem Stand der Technik.

                                         -3-



Die Anmelderin stellt den Antrag,


          den angegriffenen Beschluss aufzuheben und das nachgesuchte
          Patent mit folgenden Unterlagen zu erteilen:


          Patentansprüche 1 bis 15,
          überreicht in der mündlichen Verhandlung,
          Beschreibung Seiten 1 bis 22 und
          2 Blatt Zeichnungen mit Figuren 1 und 2, jeweils vom Anmeldetag.


Der geltende Patentanspruch 1, hier mit einer möglichen Gliederung versehen,
lautet:


          (a)   Verfahren zum lastverteilten Zuweisen von computer-gestützten medizinischen Taskflows auf zumindest einen Anwendungsserver (100) einer Serverfarm (10), mit folgenden
                Verfahrensschritten:


          (b)   – Erfassen eines medizinischen Taskflows mit konfigurierbaren Anforderungsbedingungen,


          (c)   wobei der medizinische Taskflow aus einer Abfolge von mehreren zeitlich versetzt ablaufenden und/oder ineinander verschachtelten Tasks besteht und


          (d)   sich die Anforderungsbedingungen auf den medizinischen
                Taskflow beziehen;


          (e)   – Konfigurieren der Anforderungsbedingungen im Hinblick
                auf eine medizinische Fragestellung

                                        -4-



       (f)   – Seitens einer Programmerweiterung (101), die auf einem
             Anwendungsserver (100) installiert ist: – Konfigurieren von
             Lastinformation von verfügbaren Anwendungsservern (100)
             der Serverfarm (10), so dass es konfigurierbar ist, welche
             Lastinformationen erfasst werden sollen;


       (g)   – Seitens eines Lastberechnungsagenten (102), der auf
             dem Anwendungsserver (100) installiert ist: Erfassen von
             Lastinformationen    von     verfügbaren    Anwendungsservern (100) der Serverfarm (10),


       (h)   – Seitens   eines   Lastverteilungsdienstes (104),   der   auf
             einem Anwendungsserver (100) der Serverfarm (10) installiert ist: Ermitteln zumindest eines Ziel-Anwendungsservers,
             wobei zumindest ein solcher Anwendungsserver (100) aus
             der Serverfarm (10) als Ziel-Anwendungsserver als Ergebnis
             bestimmt wird, der gemäß den erfassten Lastinformationen
             die erfassten Anforderungsbedingungen erfüllt,


       (j)   wobei auf dem Lastverteilungsdienst (104) eine Benutzerschnittstelle zur Anzeige eines Ergebnisses und/oder Lastergebnisses ausgebildet ist und


       (k)   wobei der Lastverteilungsdienst (104) auf vorkonfigurierbare
             Regeln zugreift, die es ihm ermöglichen, die jeweiligen Lastberechnungsagenten (102) spezifisch anzusprechen.



Zu den nebengeordneten, auf ein „Computerprogrammprodukt“ und ein „System
zum lastverteilten Zuweisen von computer-gestützten medizinischen Taskflows“
gerichteten unabhängigen Ansprüchen 13 und 15 sowie zu den Unteransprüchen 2 bis 12 und 14 wird auf die Akte verwiesen.

                                       -5-



Der Anmeldung soll nach den Angaben in der Anmeldung (siehe Offenlegungsschrift Absatz [0008]) die Aufgabe zugrunde liegen, einen Weg aufzuzeigen, mit
dem ein komplexer medizinischer Taskflow auf mehrere Server einer Serverfarm
verbessert aufgeteilt werden kann; darüber hinaus solle es möglich sein, unterschiedlichen Versionen von Applikationen unter Berücksichtigung von serverspezifischen Merkmalen und taskflow-spezifischen Anforderungen auf dem Gebiet der
Medizintechnik in die Lastverteilung einzubinden.


Folgende Druckschriften wurden zum Stand der Technik benannt:


        D1   US 6 963 917 B1
        D2   US 6 327 622 B1
        D3   DE 10 2006 004 618 A1
        D4   WO 2001 / 13 228 A2.



                                         II.


Die Beschwerde ist rechtzeitig eingegangen und auch sonst zulässig. Sie hat
jedoch keinen Erfolg, weil der Gegenstand des geltenden Patentanspruchs 1 nicht
auf einer erfinderischen Tätigkeit beruht (§§ 1 und 4 PatG).


1.    Die vorliegende Anmeldung betrifft eine Lastverteilung für komplexe medizinische Taskflows auf Anwendungsserver einer Serverfarm.


1.1   In der Beschreibungseinleitung werden medizinische Datenverarbeitungs-Systeme beschrieben, die typischerweise auf einer Gruppe von Servern basieren,
auf welche eine Gruppe von Client-Rechnern zugreift. Ein solches Client-Server-System diene zur Verarbeitung von komplexen medizinischen Taskflows, bei
denen es sich z. B. um modular aufgebaute und/oder verschachtelte Arbeitsabläufe handele, die beispielsweise eine Kernspinuntersuchung, eine Laboruntersuchung und ein anschließendes Post-Processing der Daten umfassten. Eine ein-

                                      -6-



zelne Untersuchung, etwa auf einem Magnetresonanzscanner, könne selbst verschiedene Sub-Tasks umfassen (z. B. das Erzeugen einer geeigneten Messsequenz für die auszuführende Untersuchung und das Anpassen der jeweiligen
Messsequenz auf das Untersuchungsgerät). Um den klinischen Betrieb möglichst
effizient ausführen zu können, sei es wichtig, den auszuführenden Tasks die
jeweils dafür geeigneten Server zuzuweisen; vor allem müssten die Server über
die geeigneten technischen Voraussetzungen verfügen, um den Task überhaupt
ausführen zu können (siehe Offenlegungsschrift Abs. [0002]).


Aus der Informatik seien eine Vielzahl von Verfahren für Lastberechnung und
Lastverteilung auf Server einer Serverfarm bekannt, die entweder software-basiert
oder hardware-basiert arbeiteten. Diese seien jedoch meist für hardware-basierte
Kriterien ausgelegt und passten nicht für die spezifischen Charakteristika eines
medizintechnischen Taskflows. Gerade für die Anwendung in einem klinischen
bzw. medizintechnischen Kontext sei es wichtig, medizin-spezifische und klinische
Kriterien zu berücksichtigen, um eine optimale Lastverteilung erreichen zu können
(Abs. [0003] bis [0007]).


1.2   Die Anmeldung schlägt konkret vor, für einen gewünschten medizinischen
Taskflow konfigurierbare Anforderungsbedingungen vorzusehen, so dass solche
Anforderungsbedingungen sehr komplex und speziell für eine medizinische Fragestellung festgelegt werden können. So verlange etwa der Taskflow „Generiere MR
Gehirnscan“ andere technische Voraussetzungen als der Taskflow „Untersuchung
des Blutes auf bestimmte Laborwerte“; im ersten Fall müssten andere technische
Parameter erfüllt sein, um den Taskflow überhaupt zur Ausführung bringen zu
können (siehe Abs. [0052]). Durch die Lehre der Anmeldung werde es möglich,
die Anforderungsbedingungen nun speziell für medizintechnische Taskflows definieren und formulieren zu können.


Ferner müssten zur Vorbereitung der Lastverteilung die momentanen Lastinformationen von verfügbaren Anwendungsservern der Serverfarm erfasst werden.

                                         -7-



Auch hierfür wird vorgeschlagen, dass es konfigurierbar sein soll, welche Lastinformationen erfasst werden (Abs. [0017] / [0018]; Abs. [0067]). Jeder Server
könne mit einem Lastberechnungsagenten ausgestattet werden, welcher die momentane Last seines Servers errechnet.


Im laufenden Betrieb sollen dann die Lastberechnungsagenten die Lastinformationen von verfügbaren Anwendungsservern erfassen; ein Lastverteilungsdienst soll
die jeweiligen Lastberechnungsagenten spezifisch ansprechen (Abs. [0041]), um
einen solchen Anwendungsserver als Ziel zu bestimmen, der gemäß den aktuell
erfassten Lastinformationen die zuvor konfigurierten Anforderungsbedingungen
erfüllt.


Ferner soll auf dem Lastverteilungsdienst eine Benutzerschnittstelle ausgebildet
sein, um insbesondere das Ergebnis der Lastberechnung anzuzeigen, so dass
etwa eine Menge von ermittelten Ziel-Anwendungsservern angezeigt werden können, dahingehend quantifiziert, inwieweit sie die erfassten Anforderungsbedingungen erfüllen (Abs. [0065], [0027]).


1.3        Das Verfahren nach Anspruch 1 des Hauptantrags beruht damit einerseits
auf einem Erfassen eines komplexen medizinischen Taskflows und einem Konfigurieren der Anforderungsbedingungen dafür, wobei sehr detailliert festgelegt werden kann, welche Anforderungen ein Server erfüllen muss, um für eine spezielle
medizinische Fragestellung ausgewählt werden zu können (Merkmale (b), (c), (d)
und (e)); und andererseits auf einem Erfassen von Lastinformationen von verfügbaren Anwendungsservern, wobei vorab mittels einer installierten Programmerweiterung konfigurierbar ist, welche Lastinformationen erfasst werden sollen (Merkmale (f) und (g)). Mit Hilfe dieser Informationen ist es dann möglich, einen Ziel-Anwendungsserver aus der Serverfarm zu bestimmen, der unter Berücksichtigung
seiner erfassten Lastinformationen die Anforderungsbedingungen (am besten)
erfüllt (Merkmal (h)). Dabei soll der Lastverteilungsdienst die einzelnen Lastberechnungsagenten „spezifisch“ ansprechen, d. h. anhand vorkonfigurierter Regeln

                                       -8-



entscheiden, wie die einzelnen Agenten zu berücksichtigen sind (Abs. [0041]
– Merkmal (k)). Außerdem sollen die Ergebnisse angezeigt werden mittels einer
Benutzerschnittstelle auf dem Lastverteilungsdienst (Merkmal (j)).


1.4    Als Fachmann, der mit der Aufgabe betraut wird, einen Weg aufzuzeigen,
mit dem komplexe medizinische Taskflows besser als bisher auf mehrere Server
einer Serverfarm aufgeteilt werden können, sieht der Senat einen Diplom-Informatiker oder System-Programmierer mit Fachhochschul-Ausbildung und mehrjähriger
Berufserfahrung im Bereich von Client-Server-Systemen und der Arbeitslast-Verteilungen auf mehrere Server an.



2.     Dem Antrag der Anmelderin kann nicht gefolgt werden, weil der Gegenstand des geltenden Patentanspruchs 1 zumindest nicht auf einer erfinderischen
Tätigkeit beruht. Inwieweit auch andere Gründe entgegenstehen, kann offen bleiben.


2.1    Es bestehen gewisse Zweifel, ob die Merkmale des geltenden Patentanspruchs 1 so, wie sie jetzt beansprucht werden, auch ursprünglich offenbart
waren. Darauf kommt es angesichts der nachfolgenden Beurteilung (siehe Abschnitt 2.2) aber nicht mehr an.


Es kann auch dahinstehen, ob alle Merkmale des Patentanspruchs 1 zur Lösung
eines technischen Problems beitragen, und ob einzelne Merkmale ggf. nicht zu
berücksichtigen wären (vgl. BGH GRUR 2011, 125 – Wiedergabe topografischer
Informationen).


2.2    Ein Verfahren zum lastverteilten Zuweisen von computergestützten medizinischen Taskflows gemäß dem geltenden Patentanspruch 1 ergab sich für den
Fachmann in naheliegender Weise aus dem Stand der Technik.

                                        -9-



2.2.1 Als nächstliegend kann die Druckschrift D3 (DE 10 2006 004 618 A1) aus
dem Hause der Anmelderin angesehen werden.


Sie geht aus von einem medizinischen DV-System in einer verteilten Rechner-Umgebung mit mehreren Verarbeitungsknoten (Rechnern, Instanzen), die in
einem Netzwerk zusammengeschlossen und für medizinische Taskflows vorgesehen sind (Figur 1, Abs. [0044] / [0045]). Entsprechend den Erläuterungen in Abs.
[0015] der vorliegenden Anmeldung lassen sich diese unterschiedlichen Rechenknoten als Server einer Serverfarm verstehen (Teil von Merkmal (a)).


Gemäß Anspruch 1 der D3 sollen erfasste medizinische Bilddaten zur Weiterverarbeitung auf geeignete Rechen-Knoten (Server) verteilt werden (= verteiltes Zuweisen von Tasks i. S. d. Merkmals (a)). Dazu wird in einem ersten Schritt für die
aktuell zu managenden Bilddaten bestimmt, welcher datentechnische Arbeitsablauf mit welcher Folge von Arbeitsschritten erforderlich ist (siehe Abs. [0021]); der
erforderliche Arbeitsablauf stellt einen „medizinischen Taskflow“ im Sinne der vorliegenden Anmeldung dar (Merkmal (c)). In einem weiteren Schritt werden die
Bilddaten gezielt an solche Knoten gesendet, die für die gewünschte Bearbeitung
die erforderliche Funktionalität aufweisen (Abs. [0027]); der Fachmann liest hier
mit, dass bei der vorangegangenen Bestimmung der Folge von Arbeitsschritten
auch die Anforderungsbedingungen an die Rechen-Knoten mit festgelegt worden
sein müssen (vgl. Abs. [0016]: Bestimmung der „relevanten“ Knoten, also derjenigen Knoten, welche die erforderliche Funktionalität aufweisen – Teil von Merkmal (b), ferner Merkmal (d)). Dabei gibt die D3 bereits die Lehre, dass die Bestimmung des Arbeitsablaufs (u. a.) durch den Anwender über eine Benutzer-Schnittstelle möglich sein soll (siehe Abs. [0021] Mitte: „… dass ein Anwender
einen bestimmten Arbeitsablauf definiert … indem er bestimmte Arbeitsschritte
aus einer ihm über eine spezifische Benutzer-Schnittstelle angebotenen Menge
von möglichen Arbeitsschritten auswählt“ – Merkmal (e), Rest von Merkmal (b)).
Schließlich können bei der Bestimmung der „relevanten“ Knoten im Netzwerk
gemäß Abs. [0016] / [0029] noch weitere Parameter einfließen, so z. B. die Aus-

                                        - 10 -



lastung des Knotens (lastverteiltes Zuweisen = Rest von Merkmal (a)). D. h. insoweit ist in der Druckschrift D3 die Lehre der Merkmale (a) bis (e) vorbeschrieben.
In welcher Weise die Lastverteilung erfolgt, ist im Detail allerdings nur wenig entnehmbar, Abs. [0029] verweist hier nur auf einen „Zuordnungsmechanismus“, welcher z. B. die Auslastung der einzelnen Knoten berücksichtigt (Prinzip der Merkmale (g) und (h)).


Dem Fachmann waren aber Verfahren zur Lastverteilung in einem Server-Netzwerk geläufig. So beschreibt z. B. die Druckschrift D4 (WO 2001 / 13 228 A2, vorveröffentlichte PCT-Anmeldung zu der vom USPTO entgegengehaltenen Druckschrift „Carlson“) ein Verfahren zum Load Balancing in einem Application Server
System, wobei auf einem Application Server 230 (Figur 4) bzw. 320A … 320D
(Figur 7) ein load balancing service 222 (Figur 4) oder 330 (Figur 7) als „Lastverteilungsdienst“ im Sinne des Merkmals (h) läuft (Seite 13 Zeile 14 ff.). Der Lastverteilungsdienst verwendet Informationen von einem „Load Monitor“ (Figur 4),
welcher als „Lastberechnungsagent“ Lastinformationen des jeweiligen Anwendungsservers erfasst (Merkmal (g)). Dabei können Lastinformationen der Application Server untereinander ausgetauscht werden (Seite 13 Zeile 21 / 22), so dass
der Lastverteilungsdienst entscheiden kann, welcher Server für einen neuen
Request am besten geeignet ist (weitgehend Merkmal (h)). Die Konfiguration,
welche Last-Informationen erfasst werden sollen, erfolgt mittels einer Benutzerschnittstelle (z. B. gemäß Figur 10), mit welcher ein Administrator Kriterien für die
Bestimmung der Last (Figur 8: z. B. CPU Load, Disk I/O, Server Response
Time …) konfigurieren kann (Seite 14 Zeile 5 ff. – weitgehend Merkmal (f)). Dazu
ist ein „administrative tool“ vorgesehen, welches als die beanspruchte „Programmerweiterung“ verstanden werden kann (Rest von Merkmal (f)). Die vom Administrator wählbaren Belastungs-Kriterien („server load criteria“ Seite 13 Zeile 22 ff.)
entsprechen dabei einem „Satz von vorkonfigurierten Regeln“, die es dem Lastverteilungsdienst ermöglichen, Lastverteilungsagenten auf anderen Application Servern spezifisch anzusprechen (Seite 13 Zeile 21 – entsprechend Merkmal (k)).

                                       - 11 -



Die D4 gibt keine Lehre bezüglich spezieller Anforderungsbedingungen und solcher Anwendungsserver, welche die erfassten Anforderungsbedingungen erfüllen.
Eine Berücksichtigung auch von Anforderungsbedingungen leitet sich jedoch aus
der Lehre der Druckschrift D3 ab, welche ausdrücklich vorschlägt, nur solche Rechenknoten zu berücksichtigen, die für die gewünschte Bearbeitung die erforderliche Funktionalität aufweisen (D3 Abs. [0027] bis [0029] „relevante Knoten“ – Rest
von Merkmal (h)).


Das noch übrige Merkmal (j) betrifft eine Benutzerschnittstelle auf dem Lastverteilungsdienst zur Anzeige eines „Ergebnisses und/oder Lastergebnisses“. Solche
Benutzerschnittstellen zur Anzeige, wie programmierte Verfahren ablaufen und zu
welchen Ergebnissen sie führen, waren dem Fachmann jedoch vertraut, siehe
etwa D4 Figur 20 zur Anzeige von „Server Events“ (i. V. m. Seite 41 Zeile 35 ff.
„Logging Facility“). Das Vorsehen einer derartigen Benutzerschnittstelle hat sicherlich keinen „kombinatorischen Effekt“ bezüglich der übrigen Merkmale, sondern
stellt nur eine übliche Maßnahme zur Beurteilung des Programmerfolges durch
den Administrator dar und kann das Vorliegen einer erfinderischen Tätigkeit nicht
begründen.


Damit ergab sich das Verfahren mit den Merkmalen des Patentanspruchs 1, wenn
der Fachmann die in der Druckschrift D3 nur unvollständig beschriebene Lastverteilung für medizinische Taskflows, unter Einbeziehung seines Fachwissens über
„fachübliche“ Maßnahmen, entsprechend dem Beispiel der Druckschrift D4 konkretisierte.


2.2.2 Die Anmelderin hat dagegen gerichtet vorgetragen, dass die zitierten
Druckschriften andere Systemkonzepte beträfen (etwa wenn die Druckschrift D2
lediglich ein Load-Balancing auf Basis eines DNS-Servers lehre). Hier ist aber zu
berücksichtigen, dass die Druckschrift D3 das konkrete Verfahren zur Lastverteilung dem Fachmann überlässt; dieser wird ihm geläufige Beispiele, wie etwa das
der Druckschrift D4, heranziehen und auf das Ausgangsverfahren (entsprechend

                                      - 12 -



der Druckschrift D3) anwenden, und ggf. unterschiedliche Systemkonzepte daran
anpassen.


Die Anmelderin misst noch der Formulierung in Merkmal (k) besondere Bedeutung
bei, dass der Lastverteilungsdienst (104) auf vorkonfigurierbare Regeln zugreife,
um die jeweiligen Lastberechnungsagenten (102) „spezifisch anzusprechen“.
Gemäß Absatz [0041] bedeute dies, dass die Lastberechnungsagenten unterschiedlich angesprochen werden könnten – insbesondere sollten die Lastberechnungsagenten eines bestimmten Anwendungsservers gar nicht erst angesprochen
werden, wenn dieser die angeforderte Konfiguration (z. B. bei zu wenig CPU-Ressourcen) nicht bereitstellen könne.


Es ist jedoch bereits fraglich, ob eine derart eingeschränkte Interpretation des
Anspruchswortlauts überhaupt zulässig ist (vgl. etwa BGH GRUR 2007, 309
– Schussfädentransport, Leitsatz a); BPatG GRUR 2000, 794 – Veränderbare
Daten). Selbst wenn man dies zu Gunsten der Anmelderin unterstellt, kann auch
eine solche Beschränkung (dass also nur Lastberechnungsagenten derjenigen
Anwendungsserver angesprochen werden sollen, welche die Anforderungsbedingungen erfüllen) das Vorliegen einer erfinderischen Tätigkeit nicht begründen.
Denn schon die Lehre der Druckschrift D3 unterscheidet zwischen Rechenknoten,
welche die geforderte Funktionalität nicht aufweisen, und „relevanten“ Knoten
(siehe D3 Abs. [0016]); dort ist ausdrücklich darauf abgestellt, nur solche Knoten
in Betracht zu ziehen, welche für die Durchführung der geforderten Arbeitsschritte
infrage kommen (siehe D3 Abs. [0027] bis [0029]). Auch unabhängig davon ist es
für den Fachmann, der immer um Optimierung der Abläufe bemüht ist, eine selbstverständliche Maßnahme, Baugruppen vom Ablauf auszuschließen, die für die
geforderten Arbeitsschritte nicht geeignet sind (vgl. BGH GRUR 2014, 647 – Farbversorgungssystem).


2.3   Mit dem Patentanspruch 1 fallen auch die übrigen Patentansprüche, da
über einen Antrag nur einheitlich entschieden werden kann.

                                       - 13 -



                             Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

   1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
   2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
      Erfolg abgelehnt war,
   3. einem Beteiligten das rechtliche Gehör versagt war,
   4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
      sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
      zugestimmt hat,
   5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
      Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
   6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                 Eder                Baumgardt                 Dr. Forkel




                                                                                  Fa
