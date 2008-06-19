---
ecli: "ECLI:DE:BPatG:2008:190608B21Wpat32.05.0"
court: "Bundespatentgericht"
spruchkoerper: "21"
aktenzeichen: "21 W (pat) 32/05"
decided: "2008-06-19"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2008&Sort=1&Seite=50&nr=8586&anz=1485&pos=755&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2008-06-19_21_W-pat_32_05_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0073.md", "germany/bund/acts/patg/0080.md", "germany/bund/acts/patkostg/0003.md", "germany/bund/acts/patkostg/0006.md"]
---

# Bundespatentgericht, 21 W (pat) 32/05 vom 2008-06-19

## Entscheidung

BUNDESPATENTGERICHT


 21 W (pat) 32/05                                                Verkündet am
 _______________                                                 19. Juni 2008
    (Aktenzeichen)                                                     …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 102 34 032.3-34


…




hat der 21. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts aufgrund der mündlichen Verhandlung vom 19. Juni 2008 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Winterfeldt sowie der Richter Baumgärtner,
Dipl.-Phys. Dr. Morawek und Dipl.-Ing. Bernhart




BPatG 154
08.05

                                      -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                   Gründe


                                        I.


Die Patentanmeldung wurde am 26. Juli 2002 mit der Bezeichnung „Energiespeicher und Verfahren zur Ermittlung des Verschleißes eines elektrochemischen
Energiespeichers“ beim Deutschen Patent- und Markenamt angemeldet. Die
Offenlegung erfolgte am 5. Februar 2004.


Die Prüfungsstelle für Klasse G 01 R hat die Anmeldung mit Beschluss vom
15. März 2005 zurückgewiesen, da die im Bescheid vom 24. Februar 2003
gerügte Unklarheit im ursprünglichen Anspruch 10 auch in dem neu eingereichten,
gleichlautenden Anspruch 4 nicht beseitigt worden sei.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin.


Die Anmelderin verfolgt ihr Patentbegehren mit dem im Beschwerdeschriftsatz
vom 19. April 2005 eingereichten Patentanspruch 4 und ansonsten unveränderten
Patentansprüchen 1 bis 3 und 5 bis 11 der Eingabe vom 7. März 2005 weiter und
beantragt die Patenterteilung.

                                         -3-



Der geltende Patentanspruch 1 lautet mit einer Merkmalsgliederung versehen:


       M1      Verfahren zur Ermittlung des Verschleißes eines elektrochemischen Energiespeichers durch


       M2      - Bestimmen der Batterietemperatur (T) und


       M3      - Bestimmen einer Verschleißgröße (Qv) als Summe
                  über die Zeit (t) von temperaturabhängigen Verschleißbeiträgen (qv)


               gekennzeichnet durch


       M4a     Berechnen der Verschleißbeiträge (qv) für Batterietemperaturen (T) oberhalb einer Grenztemperatur (To)


       M4b     in Zeitintervallen (dt) nach der Formel


       M4c     qv = K0 * A * (1 + a * T + b * T2) dt,


               wobei K0 ein Proportionalitätsfaktor, A ein Zeitparameter,
               a ein erster Temperaturkoeffizient und b ein zweiter Temperaturkoeffizient ist.


Zu den Unteransprüchen 2 bis 11 wird auf die Akte verwiesen.


Des Weiteren bittet die Anmelderin um Rückzahlung der Beschwerdegebühr, da
sie zu dem von der Prüfungsstelle im Beschluss erstmals genannten Zurückweisungsgrund nicht gehört worden sei, wonach eine mathematische Methode als
solche im Patentanspruch 1 beansprucht werde.

                                      -4-



Die Anmelderin ist, wie am 18. Juni 2008 bereits telefonisch angekündigt, zur
mündlichen Verhandlung nicht erschienen.


In der mündlichen Verhandlung hat der Senat die Entgegenhaltung


        E1 JP 0 929 35 39 A - (mit Abstract und englischer Computerübersetzung)


in das Verfahren eingeführt.


Wegen weiterer Einzelheiten wird auf den Inhalt der Akten Bezug genommen.




                                       II.


Die Beschwerde ist zulässig. Sie ist jedoch nicht begründet, denn der Gegenstand
des Patentanspruchs 1 ist nicht patentfähig, da er gegenüber dem Stand der
Technik gemäß der E1 nicht auf einer erfinderischen Tätigkeit beruht. Es kann
daher dahinstehen, ob der Patentanspruch 1 durch die ursprüngliche Offenbarung
gedeckt ist.


1. Die Patentanmeldung betrifft ein Verfahren zur Ermittlung des Verschleißes
eines elektrochemischen Energiespeichers.


Aus den Ausführungen in der Beschreibungseinleitung (vgl. S. 2, Abs. 3) geht hervor, dass bei der Bestimmung des Verschleißes von Energiespeichern aufgrund
des Verlustes an Speicherkapazität die Komplexität der Vorgänge im Energiespeicher ein Problem darstellt, das mit naturwissenschaftlichen Methoden nur schwer
beschreibbar ist. Auch kann erhöhte Temperatur den Verschleiß während der
Perioden ohne elektrische Beaufschlagung verstärken (S. 2, Abs. 2).

                                        -5-



Die Differenzierung des Betriebszustandes in Bezug auf den temperaturabhängigen Verschleiß erfordert jedoch einen relativ komplexen Rechenalgorithmus, der
in der Regel sehr speicheraufwändig ist und eine Implementierung auf einem
Mikrokontroller erschwert (S. 3, Abs. 1).


Daran orientiert sich die der Patentanmeldung zugrundeliegende Aufgabe, ein verbessertes Verfahren zur Ermittlung des Verschleißes eines elektrochemischen
Energiespeichers zu schaffen, mit dem eine Verschleißgröße in Abhängigkeit von
der Batterietemperatur relativ einfach bestimmt werden kann (S. 3, Abs. 2).


2. Das in Patentanspruch 1 beanspruchte Verfahren ist nicht nach § 1 Abs. 3
Nr. 1 PatG von der Patentierung ausgeschlossen, da sich sein Gegenstand nicht
auf eine mathematische Methode „als solche“ bezieht (§ 1 Abs. 4 PatG).


Aus § 1 Abs. 3 Nr. 1, Abs. 4 PatG geht hervor, dass der Gesetzgeber Lehren zum
technischen Handeln nicht deswegen vom Patentschutz ausschließen wollte, weil
innerhalb einer Erfindung mathematische Methoden zum Einsatz kommen. Vielmehr hat er durch die genannten Vorschriften nur zum Ausdruck gebracht, dass
ein Patentschutz erst in Betracht kommt, wenn der Gegenstand, für den Patentschutz begehrt wird, über eine mathematische Methode „als solche“ hinausgeht
(vgl. BGH GRUR 2004, 667 - elektronischer Zahlungsverkehr, insbesondere
S. 669, Nr. 3. (2), letzter Absatz).
Wann dies der Fall ist, ist ausgehend vom Wortlaut sachbezogen nach Sinn und
Zweck der gesetzlichen Regelung zu ermitteln. Sowohl die in Nr. 1 genannten wissenschaftlichen Theorien und mathematischen Methoden als auch die in Nr. 3
genannten Pläne, Regeln und Verfahren für gedankliche Tätigkeiten sind nur insoweit vom Patentschutz ausgeschlossen, als sie losgelöst von einer konkreten
Umsetzung beansprucht werden. Soweit sie hingegen zur Lösung eines konkreten
technischen Problems Verwendung finden, sind sie - in diesem Kontext - grundsätzlich patentfähig (BGH GRUR 2002, 143 ff. - Suche fehlerhafter Zeichenketten,
insbesondere S. 145, Nr. 1.a) cc)). Die prägenden Anweisungen der beanspruch-

                                       -6-



ten Lehre müssen der Lösung eines konkreten technischen Problems dienen. Dies
ist vorliegend der Fall. Das in der Anmeldung genannte Problem, mithilfe des
beanspruchten Verfahrens auf relativ einfache Weise den Verschleißzustand
eines elektrochemischen Energiespeichers zu ermitteln, liegt unzweifelhaft auf
technischem Gebiet. Die zur Lösung dieses Problems in Anspruch 1 genannten
Mittel sind ebenfalls technischer Natur (vgl. BGH GRUR 2005, 141 - Anbieten
interaktiver Hilfe, insbesondere S. 142, Nr. 4.a), letzter Absatz). Entgegen der im
angefochtenen Beschluss - allerdings nur als obiter dictum - auf Seite 4 geäußerten Auffassung kommt es für die Frage des Patentierungssausschlusses nach § 1
Abs. 3 Nr. 1 PatG nicht darauf an, ob sich das in Patentanspruch 1 definierte Verfahren lediglich durch eine Berechnungsformel vom bekannten Stand der Technik
unterscheidet. Der Vergleich mit dem Stand der Technik ist erst bei der Prüfung
der beanspruchten Lehre auf Neuheit und erfinderische Tätigkeit geboten.


Vorliegend erschöpft sich der Gegenstand des Patentsanspruchs 1 nicht in einer
Berechnungsformel, wie dies nach § 1 Abs. 4 PatG für einen Patentierungsausschluss erforderlich wäre. Sowohl das Merkmal [M2] (Bestimmen der Batterietemperatur (T)) als auch die Berücksichtigung des Zeitverlaufs erfordern Messvorgänge. In dem Verfahren nach Patentanspruch 1 werden Anweisungen beansprucht, mit denen ein konkretes technisches Problem gelöst wird, so dass es
nicht darauf ankommt, ob der Patentanspruch auch auf die Verwendung eines
Algorithmus abstellt (BGH a. a. O. - Anbieten interaktiver Hilfe S. 142, Nr. 4.a),
Absatz 2).


3. Das in Patentanspruch 1 angegebene Verfahren ist neu, denn das Berechnen
der Verschleißbeiträge für Batterietemperaturen oberhalb einer Grenztemperatur
nach der Formel, wie im Merkmal [M4c] angegeben, ist aus dem in Betracht gezogenen Stand der Technik nicht bekannt.


Das Verfahren gemäß dem Patentanspruch 1 beruht jedoch nicht auf einer erfinderischen Tätigkeit. Vielmehr ergibt es sich für den Fachmann aufgrund seiner

                                         -7-



Kenntnisse und Fähigkeiten in naheliegender Weise aus dem Stand der Technik.
Als Fachmann ist ein mit der Entwicklung von wiederaufladbaren elektrochemischen   Speicherbatterien   befasster,   berufserfahrener     Diplom-Physiker      oder
Diplom-Ingenieur zu definieren.


Aus der E1 ist ein Diagnoseverfahren zur Ermittlung des Zustandes, somit des
Verschleißes eines elektrochemischen Energiespeichers bekannt (vgl. die
Bezeichnung („Storage Battery Deterioration Diagnostic Method …“) [M1]. Das
Verfahren beruht einzig auf der Überwachung der Temperatur der Speicherbatterie [M2], um daraus auf die Verschlechterung ihres Zustandes zu schließen (vgl.
Abs. [0008] der Übersetzung …„only by supervising the temperature“…). Im
Absatz [0021] ist dargelegt, dass bei Lagerung des Energiespeichers unterhalb
einer gewissen Grenztemperatur - bspw. 25° C - keine nennenswerte Verschlechterung auftritt (Z. 6 von unten …„in T < To …since a period until it reaches a life
does not change substantially“, … ). Oberhalb dieser Grenztemperatur werden
Verschleißbeiträge   temperaturabhängig        nach   der   Formel   K=2[(T-T0)/10] • 100
(Abs. [0057]) errechnet und in einer Tabelle (Drawing 5) abgespeichert [M4a]. Der
Verschleiß - Alterungszustand - des Energiespeichers wird ermittelt, indem aus
auf eine Stunde bezogenen K-Werten bei einer bestimmten Temperatur durch
Multiplizieren mit der Anzahl der Stunden, während der Speicher der jeweiligen
Temperatur ausgesetzt ist, ein Verschleißbeitrag in einem Zeitintervall (Anzahl der
Stunden) errechnet wird [M4b]. Ist der Energiespeicher in mehreren Zeitintervallen
(bspw. 5000, 10000, 8000 Stunden) unterschiedlichen Temperaturen ausgesetzt,
so wird die gesamte Verschleißgröße als Summe über die Zeit aus den einzelnen
temperaturabhängigen Verschleißbeiträgen ermittelt [M3] (vgl. dazu Abs. [0061]
ab Zeile 8 zu dem aufgezeigten Beispiel).


Bei dem Verfahren aus E1 basiert die Berechnung der einzelnen Verschleißbeiträge auf dem Abnahmekoeffizienten K, der sich aus einer Exponentialfunktion mit
der Basis 2 errechnet, um damit den oberhalb der Grenztemperatur nicht linear,
sondern exponentiell anwachsenden Verschleißbeiträgen gerecht zu werden.

                                       -8-



Beim Gegenstand des Anspruchs 1 gründet die Berechnung der nichtlinear
anwachsenden Verschleißbeiträge demgegenüber auf einer Taylorreihe, auf der
die im Merkmal [M4c] angegebene Formel aufbaut.


Die Berechnung einer überproportional - nicht linear - ansteigenden Größe, im vorliegenden Falle der Verschleißbeiträge oberhalb der Grenztemperatur, näherungsweise anhand einer Potenzreihe (Taylorreihe 2. Ordnung) anstatt einer Exponentialfunktion vorzunehmen, ist eine für den Fachmann naheliegende Maßnahme, da
Potenzreihen zum Grundwissen des Fachmanns gehören.


4. Für eine Rückzahlung der Beschwerdegebühr aus Billigkeitsgründen nach
§ 80 Abs. 3 PatG besteht kein Anlass. Nach § 3 PatKostG wird die Beschwerdegebühr mit Einreichung der Beschwerde fällig und ist gemäß § 6 Abs. 1 S. 1
PatKostG innerhalb der Beschwerdefrist des § 73 Abs. 2 S. 1 PatG zu zahlen.
Dies ist vorliegend geschehen, die mit Rechtsgrund bezahlte Gebühr ist damit verfallen. Eine verfallene Gebühr kann nur bei Vorliegen gravierender Umstände
zurückbezahlt werden, auf Grund derer es unbillig erschiene, den Beschwerdeführer mit der Gebühr zu belasten, beispielsweise bei erhebliche Verfahrensfehlern
im patentamtlichen Verfahren. Ein derartiger Sachverhalt liegt hier nicht vor. Zwar
macht die Beschwerdeführerin geltend, ihr sei bezüglich der auf § 1 Abs. 3 Nr. 1
PatG gestützten Zurückweisung das rechtliche Gehör versagt worden. Dabei übersieht sie aber, dass die Anmeldung im Beschluss vom 15. März 2005 nur mit der
Begründung zurückgewiesen worden ist, dass die mit Bescheid vom 24. Februar 2003 gerügte Unklarheit im ursprünglichen Anspruch 10 auch in dem neu
eingereichten, gleich lautenden Anspruch 4 nicht beseitigt worden sei und auch
die Beschreibung insoweit keine deutliche und hinreichend vollständige Offenbarung beinhalte, dass der Fachmann sie ausführen könne. Dieser wegen des in
Anspruch 4 trotz entsprechender Rüge nicht beseitigten Mangels führte dann in
Übereinstimmung mit der Rechtsprechung zur Zurückweisung der gesamten
Anmeldung (BGH GRUR 1997, 120 - elektrisches Speicherheizgerät). Insoweit
hatte die Beschwerdeführerin die Möglichkeit gehabt, sich zu äußern.

                                      -9-



Auf die im Ergebnis nicht tragfähigen Ausführungen zum Patentierungsausschluss
nach § 1 Abs. 3 Nr. 1 PatG (s. o.) hat die Prüfungsstelle die Zurückweisung
ersichtlich nicht gestützt. Daher war es entbehrlich, dass die Anmelderin hierzu
Stellung nehmen konnte. Punkt II. 2 des Beschlusses enthält nur eine Erklärung,
warum ein weitere Aufforderung an die Anmelderin zur Mängelbeseitigung unterblieben war. Die Prüfungsstelle hat den Sachverhalt insoweit nicht abschließend
beurteilt, wie sich aus der Formulierung ergibt, dass die Weiterverfolgung der
Anmeldung unter Verzicht auf den gerügten Anspruch „mit hoher Wahrscheinlichkeit“ eine Zurückweisung nach sich gezogen „hätte“.


5. Mit dem nicht gewährbaren Patentanspruch 1 fallen aufgrund der Antragsbindung auch die Unteransprüche 2 bis 11. Im Übrigen hat die Überprüfung seitens
des Senats ergeben, dass auch diese Patentansprüche keine Patent begründende
Substanz enthalten.




Dr. Winterfeldt         Baumgärtner            Dr. Morawek             Bernhart




                                                                          Pr/Fa
