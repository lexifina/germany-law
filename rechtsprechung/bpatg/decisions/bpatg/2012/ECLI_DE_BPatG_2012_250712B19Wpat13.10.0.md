---
ecli: "ECLI:DE:BPatG:2012:250712B19Wpat13.10.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 13/10"
decided: "2012-07-25"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2012&Sort=1&Seite=58&nr=23902&anz=1451&pos=883&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2012-07-25_19_W-pat_13_10_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0045.md", "germany/bund/acts/patg/0048.md"]
---

# Bundespatentgericht, 19 W (pat) 13/10 vom 2012-07-25

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 13/10                                                      Verkündet am
_______________                                                         25. Juli 2012
    (Aktenzeichen)                                                           …




                              BESCHLUSS

                            In der Beschwerdesache


             betreffend die Patentanmeldung 10 2007 036 356.9-32


…




hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 25. Juli 2012 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Ing. Bertl, der Richterin Kirschneck sowie der Richter Dr.-Ing. Scholz
und Dipl.-Ing. Müller

beschlossen:


                     Die Beschwerde wird zurückgewiesen.


                                   Gründe


                                       I


Das Deutsche Patent- und Markenamt - Prüfungsstelle für Klasse G05B - hat die
am 31. Juli 2007 von der K… Infotects GmbH eingereichte Patentanmeldung
mit Beschluss vom 23. Juli 2009 zurückgewiesen mit der Begründung, der Patentanspruch 1 sei mangels Technizität nicht gewährbar.


Gegen diesen Beschluss richtet sich die eingegangene Beschwerde der Anmelderin.


Sie beantragt,


       den Beschluss der Prüfungsstelle für Klasse G05B des Deutschen
       Patent- und Markenamts vom 23. Juli 2009 aufzuheben und das
       nachgesuchte Patent mit folgenden Unterlagen zu erteilen,


       Patentansprüche 1 bis 8 vom 24. Juli 2012,
       Beschreibung, Seiten 2, 3, 3a, vom 24. Juli 2012,
       übrige Beschreibung vom Anmeldetag 31. Juli 2007,
       3 Blatt Zeichnungen, Figuren 1 bis 4, vom 14. November 2007,


       hilfsweise,
       Patentanspruch 1 gemäß 1. Hilfsantrag, überreicht in der mündlichen Verhandlung,
       übrige Unterlagen wie Hauptantrag.

Der geltende Patentanspruch 1 vom 24. Juli 2012 gemäß Hauptantrag lautet unter
Einfügung einer Gliederung:


       "Verfahren zur automatischen Bewertung von Fehlerursachen eines Betriebsgerätes, welches folgende Schritte umfasst:


       a - Anordnen von Sensoren oder Analysegeräten an jeweiligen zu
           überwachenden Funktionseinheiten,


       b - Initialisieren von Fehlerursachen n,


       gekennzeichnet durch:


       c - Erfassen von Signalen der jeweiligen Funktionseinheit I zur
           Ermittlung eines Ausfallsrisikos während dem Betrieb des Betriebsgerätes mittels der daran angeordneten Sensoren und
           Analysegeräten,


       d1 - Auswerten der erfassten Signale jeder Funktionseinheit I des
           Betriebsgerätes durch


       d2 - Ermittlung einer Kennzahl für die Auftrittswahrscheinlichkeit einer Fehlerursache n des Fehlers m in der Funktionseinheit I in
           Abhängigkeit der Zeitdauer der Belastung einer Funktionseinheit I innerhalb verschiedener Belastungsklassen i der Fehlerursache n des Fehlers m,


       d3 - Ermittlung einer Kennzahl für die Wahrscheinlichkeit des Entdeckens der Fehlerursache n des Fehlers m in der Funktionseinheit I,

       d4 - Ermittlung einer Kennzahl für die Bedeutung der Fehlerursache n des zum Ausfall führenden Fehlers m der Funktionseinheit I, und


       e - Ausgeben einer Risikoprioritätszahl für ein Ausfallrisiko des
           Betriebsgerätes durch eine Anzeigevorrichtung, welche durch
           Multiplikation der Kennzahlen ermittelt wird."


Der geltende Patentanspruch 1 vom 25. Juli 2012 gemäß 1. Hilfsantrag lautet unter Einfügung einer Gliederung:


       "Verfahren zur automatischen Bewertung von Fehlerursachen eines Betriebsgerätes, welches folgende Schritte umfasst:


       a - Anordnen von Sensoren oder Analysegeräten an jeweiligen zu
           überwachenden Funktionseinheiten,


       b - Initialisieren von Fehlerursachen n,


       gekennzeichnet durch:


       c - Erfassen von Signalen der jeweiligen Funktionseinheit I zur
           Ermittlung eines Ausfallsrisikos während dem Betrieb des Betriebsgerätes mittels der daran angeordneten Sensoren und
           Analysegeräten,


       d1 - Auswerten der erfassten Signale jeder Funktionseinheit I des
           Betriebsgerätes durch

d2' - Ermittlung einer Kennzahl für die Auftrittswahrscheinlichkeit
    gemäß der Formel



                                     im Wertebereich 1 bis 10

einer Fehlerursache n des Fehlers m in der Funktionseinheit I in
Abhängigkeit der Zeitdauer tImni der Belastung einer Funktionseinheit I innerhalb verschiedener Belastungsklassen i der Fehlerursache n des Fehlers m,


d5 - Ermittlung eines zum Ausfall führenden Fehlers m,


d6 - Auswahl der Fehlerursachen n in der Reihenfolge der höchsten Auftrittswahrscheinlichkeit PAImn des Fehlers m,


d7 - Durchführung einer automatischen Diagnose von Fehlerursachen mit einem Zustandsmodell, an dem die Zustandsgröße
    des Fehlers m einer Funktionseinheit l als Sollzustand berechnet wird, durch Subtraktion des Sollzustandes qImn mit einer
    gemessenen Ist-Zustandsgröße und die berechneten Zustandsabweichungen eines Fehlers m einer Funktionseinheit I
    in einer Bewertungs- und Korrelationsmatrix zusammengeführt
    werden,


d3' - Ermittlung einer Kennzahl für die Wahrscheinlichkeit des Entdeckens der Fehlerursache n des zum Ausfall führenden Fehlers m    der   Funktionseinheit I,   gemäß      der   Formel
                       ,

        d4’ -Ermittlung einer Kennzahl für die Bedeutung der Fehlerursache n des zum Ausfall führenden Fehlers m der Funktionseinheit I, gemäß der Formel

                                       im Wertebereich 1 bis 10



        wobei MTTRImn die mittlere Behebungszeit der Fehlerursache n
        des Fehlers m ist, welche aus der tatsächlichen Behebungszeit TTRImn und der Zeitdauer Δt im Verhältnis zur Anzahl ZImn des
        Auftretens der Fehlerursache n des Fehlers m ermittelt wird,


        e - Ausgeben einer Risikoprioritätszahl für ein Ausfallrisiko des
            Betriebsgerätes durch eine Anzeigevorrichtung, welche durch
            Multiplikation der Kennzahlen ermittelt wird."


Als Aufgabe hat die Anmelderin angegeben, es solle ein Verfahren zur automatischen Bewertung von Fehlerursachen eines Betriebsgerätes vorgeschlagen werden, welches eine vorbeugende und zustandsorientierte Instandhaltung von Betriebsgeräten ermöglicht, um eine höhere Zuverlässigkeit der Bewertung transparent und gesichert auszugeben (Seite 2, Absatz 3 der ursprünglichen Unterlagen;
gleichlautend auf Seite 3, Absatz 1 der Unterlagen vom 24. Juli 2012).


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.


                                          II.


1. Die frist- und formgerecht erhobene Beschwerde ist zulässig. Sie hat jedoch
keinen Erfolg.

2. Als Fachmann legt der Senat einen Diplom-Ingenieur der Fachrichtung Automatisierungstechnik mit Fachhochschulabschluss und mehrjähriger Berufserfahrung
zugrunde, der die Fehler-Möglichkeits- und -Einfluss-Analyse nach DIN 25 448
kennt und in seiner beruflichen Tätigkeit regelmäßig einsetzt.


3. Die Erfindung ist in der Anmeldung nicht so deutlich und vollständig offenbart,
dass der Fachmann sie ausführen kann. Die Anmeldung ist folglich im Ergebnis zu
Recht zurückgewiesen worden (§ 34 Abs. 4 in Verbindung mit §§ 48 und 45 Abs. 1
PatG).


3.1 Der Fachmann kennt zwar aus der DIN 25 448 die Durchführung einer Fehler-Möglichkeits- und -Einfluss-Analyse (FMEA), um bei der Planung einer Systems
Schwachstellen auffinden zu können und darauf aufbauend den Entwurf zu verbessern. Die DIN 25 448 enthält aber keine Aussagen über eine Fortschreibung
einer solchen Schwachstellenanalyse auf den späteren Betrieb des Systems, so
dass der Fachmann bei dem Bemühen, das Verfahren gemäß geltendem Patentanspruch 1 nach Hauptantrag nachzuarbeiten, allenfalls noch bei der Initialisierung der Fehlerursachen gemäß Merkmal b auf die Methodik gemäß DIN 25 448
zurückgreifen kann.


Weiter ist auch die Aussage in Merkmal a nacharbeitbar, wonach an den zu überwachenden Funktionseinheiten Sensoren oder Analysegeräte angeordnet werden
sollen, da es ohnehin gang und gäbe ist, komplexe System mittels geeigneter
Sensoren und Analysegeräte zu überwachen und zu schützen.

Da aber der Fachmann die von diesen Sensoren und Analysegeräte ausgegebenen Signale bislang lediglich dazu verwendet, auftretende Störungen möglichst
frühzeitig zu erkennen, um deren Behebung zu veranlassen oder eine geordnete
Abschaltung herbeizuführen, stellt ihn die Aussage, die erfassten Signale einer
Funktionseinheit sollen ausgewertet werden, um deren Ausfallrisiko während des
Betriebs zu ermitteln (Merkmal d in Verbindung mit Merkmal c), vor eine Aufgabe,
die er anhand der Ausführungen in der Anmeldung nicht bewältigen kann.


Dies scheitert schon daran, dass an keiner Stelle der ursprünglich eingereichten
Unterlagen angegeben ist, an welcher Stelle des Verfahrensablaufes die Ausgangssignale der Sensoren oder Analysegeräte, beispielsweise Messwerte, in die
Berechnung einfließen sollen. Sollten mit den Variablen yImn Messwerte gemeint
sein, wie die Anmelderin in der Verhandlung geltend gemacht hat, so ist das jedenfalls der Offenlegungsschrift, die mit den ursprünglichen Unterlagen übereinstimmt, nicht zu entnehmen, da dort nicht von Messwerten, sondern von Berechnungsvorschriften yImn die Rede ist (Absatz [0020], 3. Zeile auf Seite 4/11; Absatz [0030], 12. Zeile; Figur 2, Bezugsziffer 31) oder auch von einem Grenzwert yImn0 Absatz [0020], 5.-6. Zeile auf Seite 4/11) sowie einem oberen Grenzwert yImni Absatz [0020], 8. Zeile auf Seite 4/11.


Auch zu diesen Berechnungsvorschriften sind weder Kriterien genannt, wie diese
aufgestellt werden sollen noch sind konkrete Ausführungsbeispiele angegeben, so
dass der Fachmann folglich auch nicht weiß, wie er die in Merkmal d2 genannte
Kennzahl für die Auftrittswahrscheinlichkeit ermitteln soll. Die Anmelderin hat hierzu zwar auf die in Figur 3 unter Bezugsziffer 43 dargestellte Formel verwiesen,
aus der in Verbindung mit der Beschreibung (Absatz [0029] der Offenlegungsschrift) der Zusammenhang zwischen der Auftrittswahrscheinlichkeit einer Fehlerursache und der Zeitdauer der Belastung der Funktionseinheit I innerhalb verschiedener Belastungsklassen i hervorginge.

Aber selbst der Begriff Belastungsklasse, der Teil des Ausführungsbeispiels ist,
das dem Fachmann einen Weg zur Ausführung der Erfindung weisen soll, wird
weder im Wortlaut des Patentanspruchs 1 selbst, noch an anderer Stelle der ursprünglich eingereichten Unterlagen in nachvollziehbarer Weise erläutert. Vielmehr findet der Fachmann in diesem Zusammenhang einen zweiten unbekannten
Begriff, nämlich Abnutzungsgewicht (Absatz [0020] 7. Zeile; Seite 5, Absatz [0026]
8. Zeile), den er weder als Fachbegriff noch aus der Umgangssprache kennt.


Zu der besagten Formel (Figur 3 unter Bezugsziffer 43) ist im Übrigen auch nicht
angegeben, was mit den Variablen aImni sowie bImni gemeint ist. Die Anmelderin hat
zwar geltend gemacht, aImni' sei der Platzhalter für das Abnutzungsgewicht; die Beschreibung führt jedoch aus, dass die Berechnungsvorschrift yImn die Belastung einer Funktionseinheit I durch eine Fehlerursache n eines Fehlers m zum Ergebnis
habe (Seite 4, Absatz [0020] Zeilen 3 bis 5). Dies deutet eher darauf hin, das aImni
der Platzhalter für die anhand der Berechnungsvorschrift yImn ermittelt Belastung
sein müsste. Mangels eindeutiger Angaben ist es dem Fachmann jedenfalls nicht
möglich, der Variablen aImni ein bestimmte Bedeutung zuzumessen.


Auch in dem Bemühen der Variablen bImni eine Bedeutung zuzumessen, findet der
Fachmann in den Anmeldeunterlagen keine verlässliche Quelle. Selbst wenn er
bezüglich der Variablen bImni überhaupt weiterführende Literatur über die Weibull-Verteilung, die in der Beschreibung erwähnt ist (Absatz [0020], vorletzte Zeile), herangezogen hätte, aus der laut Anmelderin hervorgehe, dass b Imni ein Formfaktor
sei, wäre der Fachmann nicht in der Lage gewesen, diesen Faktor in geeigneter,
zielführender Weise festzulegen, da in der Anmeldung dazu weder Kriterien noch
Beispiele genannt sind.


Im Übrigen hat die Anmelderin trotz eines entsprechenden Hinweises des Senats
auch keine Fachliteratur vorgelegt, die ihre Darlegungen stützen könnte.

Demnach ist zu der ersten Kennzahl gemäß Merkmal d2 des Patentanspruchs 1
weder bekannt, wie die Eingangsgrößen einfließen noch was die angegebenen
Platzhalter bedeuten noch wie diese berechnet werden.


Es kann daher dahin gestellt bleiben, ob der Fachmann anhand der Angaben in
den ursprünglichen Unterlagen in der Lage wäre, die beiden weiteren Kennzahlen
gemäß den Merkmalen d3 sowie d4 zu ermitteln.


Jedenfalls ist die Erfindung schon bezüglich der ersten Kennzahl nicht so deutlich
und vollständig offenbart, dass der Fachmann sie ausführen kann (§ 34 Abs. 4
PatG).


3.2. Die obigen Ausführung zum Patentanspruch 1 gemäß Hauptantrag gelten
gleichermaßen auch für den Patentanspruch 1 gemäß 1. Hilfsantrag, da der Gegenstand für den Schutz begehrt wird, durch die Aufnahme zusätzlicher Merkmale
in den Anspruchswortlaut komplexer wird und somit auch die Anforderungen an
die Deutlichkeit und Vollständigkeit der Offenbarung der Erfindung größer werden.


Somit kann auch dahin gestellt bleiben, ob der Fachmann den ursprünglichen Unterlagen den Wortlaut oder zumindest den Wortsinn des Patentanspruchs 1 gemäß 1. Hilfsantrag als zur Erfindung gehörend entnehmen konnte.


4. Auch der Hinweis der Anmelderin auf BGH Xa ZR 126/07 - Klammernahtgerät
konnte den Senat nicht zu einer anderen Einschätzung der Sach- und Rechtslage
bewegen. Wenngleich in dem dortigen Leitsatz angegeben ist, es sei nicht erforderlich, dass mindestens eine praktisch brauchbare Ausführungsform als solche
unmittelbar und eindeutig offenbart ist, bedeutet das im Lichte der weiteren Ausführungen in diesem Urteil nicht, das generell kein Ausführungsbeispiel der Erfindung anzugeben sei oder die Forderung nach einer deutlichen und vollständigen
Offenbarung nicht mehr bestünde.

Vielmehr stellt der höchstrichterliche Senat dort fest, es reiche aus, wenn der
Fachmann ohne eigenes erfinderisches Bemühen Unvollständigkeiten ergänzen
und sich notfalls mit Hilfe orientierender Versuche Klarheit verschaffen könne.


Im gegenwärtigen Fall liegen jedoch erhebliche Lücken in wesentlichen Teilen der
erfindungsgemäßen Lehre vor, so dass der Fachmann selbst nach umfangreichen
Versuchen nicht die Gewissheit haben könnte, ob er tatsächlich das erfindungsgemäße Verfahren ausgeführt hat.


Selbst wenn er aufgrund eigenem erfinderischen Bemühens eine eigene Lösung
der von der Anmelderin genannte Aufgabe gefunden und ein Verfahren zur automatischen Bewertung von Fehlerursachen eines Betriebsgerätes entwickelt hätte,
welches eine vorbeugende und zustandsorientierte Instandhaltung von Betriebsgeräten ermöglicht, um eine höhere Zuverlässigkeit der Bewertung transparent
und gesichert auszugeben, könnte er nicht sicher sein, ob dieses zu den gleichen
Ergebnissen führt, wie das von der Anmelderin erfundene.


Somit war die Beschwerde zurückzuweisen.




Bertl                Kirschneck                 Dr. Scholz                 J. Müller




                                                                                  Pü
