---
ecli: "ECLI:DE:BPatG:2004:210904B17Wpat58.02.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 58/02"
decided: "2004-09-21"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=95&nr=19460&anz=2061&pos=1437&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-09-21_17_W-pat_58_02_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 58/02 vom 2004-09-21

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 58/02                                               Verkündet am
 _______________                                             21. September 2004
    (Aktenzeichen)                                                    …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 100 62 092.2-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 21. September 2004 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch sowie der Richter Dr. Schmitt,
Dipl.-Phys. Dr. Kraus und Dipl.-Ing. Prasch




BPatG 154
6.70

                                         -2-



beschlossen:


            Die Beschwerde wird zurückgewiesen.




                                      Gründe


                                          I.


Die am 13. Dezember 2000 beim Deutschen Patent- und Markenamt eingegangene Patentanmeldung mit der Bezeichnung „Elektronische Schaltung und Verfahren zum Testen einer Speicherzelle eines Speicherfeldes“ wurde von der Prüfungsstelle für die Klasse G11C durch Beschluß vom 16. Juli 2002 mit der Begründung zurückgewiesen, daß der Anmeldungsgegenstand nicht auf einer erfinderischen Tätigkeit beruhe.


Gegen diesen Beschluß richtet sich die Beschwerde der Anmelderin, die beantragt,


         den angefochtenen Beschluß aufzuheben und das nachgesuchte
         Patent mit folgenden Unterlagen zu erteilen:
         Patentansprüche 1 bis 3, überreicht in der mündlichen Verhandlung am 21. September 2004, Beschreibung und 1 Blatt mit einer
         Zeichnung, beides vom Anmeldetag (13. Dezember 2000).


Der geltende Patentanspruch 1 lautet:


         Verfahren zum Testen einer Speicherzelle eines Speicherfeldes (1) in einem Stresstest, wobei während eines Lesevorgangs
         an einer Adresse des Speicherfeldes ein Wert aus einer Speicherzelle ausgelesen wird und der Wert mit einem Sollwert verglichen

                                        -3-



      wird, mit folgenden Schritten:
      Durchführen einer Anzahl von Lesevorgängen an der Adresse, um
      eine Stressbedingung zu erzeugen, und ohne daß die Adresse in
      einem Fehleradressenspeicher (10) gespeichert wird, und
      Durchführen eines weiteren Lesevorgangs an der Adresse nach
      dem Durchführen der Anzahl der Lesevorgänge, wobei abhängig
      von einem Ergebnis des Vergleichs die Adresse in dem Fehleradressenspeicher (10) gespeichert wird.


Wegen der Unteransprüche 2 und 3 wird auf die Akte verwiesen.


Es ist folgende Druckschrift in Betracht gezogen worden:


      TANABE, Akira u.a.: A 30 ns 64-Mb DRAM with Built-in Self-Test and Self-Repair Function. In: IEEE J. Solid – State Circuits, vol. 27, no. 11,
      1992, S.1525 bis 1531.


Die Anmelderin führt im wesentlichen aus, der Druckschrift sei nicht entnehmbar,
eine Speicherzelle eines Speicherfeldes zunächst unter Streß zu testen, indem
eine Streßbedingung durch eine Anzahl von Lesevorgängen an einer Adresse erzeugt werde, ohne daß beim Auftreten eines Fehlers die Adresse in einem Fehleradressenspeicher gespeichert werde, und dann anschließend mit einem weiteren
Lesevorgang festzustellen, ob ein Fehler vorliege, sowie im Falle eines Fehlers die
Adresse im Fehleradressenspeicher zu speichern. Denn die Druckschrift beschreibe eine Schaltung, die wahlweise in einem Testmodus oder in einem Reparaturmodus zu betreiben sei, wobei nur im Reparaturmodus Fehleradressen in einem Fehleradressenspeicher gespeichert würden. Das Testverfahren gemäß Patentanspruch 1 sei daher durch diesen Stand der Technik weder neuheitsschädlich vorweggenommen noch nahegelegt.

                                         -4-



                                         II.


Die frist- und formgerecht eingelegte Beschwerde ist zulässig, jedoch nicht begründet, da der Gegenstand des Patentanspruchs 1 zwar neu ist, aber nicht auf
einer erfinderischen Tätigkeit beruht.
Die Druckschrift beschreibt eine elektronische Schaltung, mit der ein Verfahren
zum Testen von Speicherzellen eines Speicherfeldes durchgeführt wird, bei dem
während eines Lesevorgangs an einer Adresse des Speicherfeldes ein Wert aus
einer Speicherzelle ausgelesen wird und der Wert mit einem Sollwert verglichen
wird. Die Schaltung weist einen BIST (Built-in self-test) – Block auf, der im Test-Modus programmgesteuerte Speichertests ermöglicht, ohne daß die Adressen
fehlerhafter Speicherzellen in einem Fehleradressenspeicher (FAM) gespeichert
werden. Der Test-Modus wird durch ein externes Signal TE aktiviert. Zudem ist ein
BISR (Built-in self-repair) Block vorgesehen, der im Repair-Modus zusammen mit
dem BIST-Block einen Speichertest mit gleichzeitigem Abspeichern von Adressen
fehlerhafter Speicherzellen in dem Fehleradressenspeicher (FAM) durchführt. Der
Repair-Modus wird durch die externen Steuersignale TE und REPAIR aktiviert,
vgl. S. 1529, Fig. 11 mit Beschreibung sowie S. 1530, linke Spalte, 1. Abs.
Der Druckschrift ist weiterhin entnehmbar, im Test-Modus langandauernde Funktionstests der Speicherzellen während eines Burn-In-Prozesses durchzuführen,
vgl. S. 1529, linke Spalte, 2. Abs. Der Funktionstest, der üblicherweise auch eine
Anzahl von Lesevorgängen an einer Speicherzelle umfaßt, erfolgt demnach unter
einer Streßbedingung, ohne daß die Adressen von fehlerhaften Speicherzellen in
dem Fehleradressenspeicher (FAM) gespeichert werden. Da die während des
Funktionstests defekt gewordenen Speicherzellen durch redundante Speicherzellen des Speicherfeldes zu ersetzen sind, müssen anschließend im Repair–Modus
die jeweiligen Fehleradressen mit einem erneuten Lesevorgang erfaßt und in dem
Fehleradressenspeicher gespeichert werden. Für den Fachmann, einen mit dem
Testen von Speicherfeldern befaßten Elektronikingenieur (FH) mit langjähriger
Erfahrung, versteht es sich von selbst, daß zur Durchführung eines von einem
Burn-In-Prozeß unabhängigen Streßtests eigens eine Streßbedingung zu erzeu-

                                       -5-



gen ist und daß sich diese nicht nur durch externe Erwärmung des Speicherfeldes
wie beim Burn-in-Prozeß, sondern auch durch eine interne Erwärmung realisieren
läßt, die aus dem mehrfachen Auslesen einer Speicherzelle resultiert.
Der Gegenstand des Patentanspruchs 1 ergibt sich demnach in naheliegender
Weise aus dem Stand der Technik. Der Patentanspruch 1 ist somit nicht gewährbar.
Mit dem Patentanspruch 1 sind auch die Unteransprüche 2 und 3 nicht gewährbar.




Dr. Fritsch              Dr. Schmitt          Dr. Kraus                 Prasch


                                                                            Bb
