---
ecli: "ECLI:DE:BPatG:2003:260503B19Wpat68.01.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 68/01"
decided: "2003-05-26"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2003&Sort=1&Seite=57&nr=21778&anz=2047&pos=858&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2003-05-26_19_W-pat_68_01_NA_0.txt"
---

# Bundespatentgericht, 19 W (pat) 68/01 vom 2003-05-26

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 68/01                             Verkündet am
 _______________                              26. Mai 2003
    (Aktenzeichen)                                 …




                      BESCHLUSS

                     In der Beschwerdesache


…




BPatG 154
6.70

                                        -2-



                        betreffend das Patent 196 20 706


hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 26. Mai 2003 unter Mitwirkung des Vorsitzenden
Richters Dipl.-Phys. Dr. Kellerer und der Richter Schmöger, Dipl.-Phys. Dr. Mayer
und Dipl.-Ing. Groß


beschlossen:


         Die Beschwerde der Einsprechenden wird zurückgewiesen.


                                    Gründe


                                         I


Das Deutsche Patent-und Markenamt - Patentabteilung 33 - hat das auf die am
23. Mai 1996 eingegangene Anmeldung erteilte Patent 196 20 706 mit der Bezeichnung "Numerisches Verfahren zur Regelung für lineare Regelvorgänge, insbesondere geeignet zur schnellen und exakten Lage- und Drehzahlregelung von
Elektromotoren" im Einspruchverfahren durch Beschluss vom 2. August 2001 in
vollem Umfang aufrechterhalten mit der Begründung, der vorgetragene Einwand,
der Patentanspruch 1 betreffe ein mathematisches Verfahren, das als solches
nicht patentierbar sei, greife nicht durch und das Verfahren des beantragten Patentanspruchs 1 sei patentfähig.


Gegen diesen Beschluss richtet sich die Beschwerde der Einsprechenden.


Der erteilte, sich vom gedruckten Patentanspruch 1 durch die nur einmalige Angabe der Formel "aLast(t) = k1 + k2×t   mit 0 ≤ t ≤ ta" unterscheidende Patentanspruch 1 lautet:

                                   -3-



"Numerisches Regelverfahren zur Regelung der Lage S und
der Geschwindigkeit V einer von einem Motor bewegten Last
sowie für andere lineare Regelvorgänge,
wobei ein Ist-Wert Sist und dessen erste zeitliche Ableitung Vist
als die zum Zeitpunkt t = 0 festgestellten Regelgrößen sowie
die beiden zugehörigen, von einem Leitsystem vorgegebenen
Soll-Werte Ssoll und Vsoll als die dem Regelziel zum Zeitpunkt
t = ta entsprechenden Führungsgrößen zu einer Stellgröße verarbeitet werden, dadurch gekennzeichnet,
dass die Stellgröße aLast auf der Grundlage der Beziehung


aLast(t) = k1 + k2×t     mit 0 ≤ t ≤ ta und


         Ssoll – Sist     Vsoll + 2 × Vist
k1 = 6 ×  − 2 × 
               ta2               ta


          Sist – Ssoll       Vsoll + Vist
k2 = 12 ×  + 6 × 
               ta3               ta2


eingestellt wird,
wobei auch Varianten der Funktion aLast(t) benutzt werden können, wenn diese gleichfalls von der Ausregelzeit ta abhängen
und die Bewegungsgleichungen

                                                -4-



                 ta

        Vist +   ∫ a (t)dt = V
                      Last              soll


                 0


                 ta          t

        Sist +   ∫ (V + ∫a (t)dt) dt = S
                       ist       Last          soll


                 0           0


        zumindest näherungsweise erfüllen".


Damit soll die Aufgabe gelöst werden, ein Regelungsverfahren zu entwickeln, das
die Nachteile des Standes der Technik, wie Überschwingen, lange Ausregelzeiten,
verzögerte Ankunft und hoher Energieverlust des Motors vermeidet und das als
genau, schnell, stabil, überschwingungsfrei, robust, energiesparend und einfach
charakterisiert werden kann (S 1 Z 27 bis 29 iVm Z 18 bis 26 der PS).


Die Einsprechende führt aus, bei dem Verfahren des Patentanspruchs 1 handele
es sich um kein Regelungsverfahren im klassischen Sinne, sondern um ein Steuerungsverfahren, denn es würden die Istgrößen zum Zeitpunkt t=0 aufgenommen,
dann werde anhand der dem Zeitpunkt t = ta entsprechenden Führungsgrößen die
Bahnkurve aLast(t) abgefahren, ohne die Istgrößen weiter zu erfassen.
Sie ist der Auffassung, aus dem Buch von Sciavicco, L. und Siciliano, B.: "Modeling and control of robot manipulators", 1996, McGrawHill, 1. Aufl., S. 170 bis 175
gehe für den Fachmann das im Patentanspruch 1 beschriebene Verfahren hervor,
denn dort seien Bahnkurven für die Strecke, die Geschwindigkeit und die Beschleunigung in Form eines kubischen Polynoms für die Strecke, einer Parabel für
die Geschwindigkeit und insbesondere einer Geraden für die Beschleunigung angegeben (S 172 Gl 5.1); auch müsse nach diesem Verfahren eine entsprechende

                                        -5-



Zeit tf, die der Ausregelzeit ta nach Patentanspruch 1 entspreche, für das Abfahren
der Bahnkurve vorgegeben werden (S 172 13. Z v unten: tf = 1).
Weiterhin meint die Einsprechende, aus dem Lexikon "Meß- und Automatisierungstechnik" von Schrüfer, E., VDI-Verlag 1992, S 499 bis 501 und 285, 286 erhalte der Fachmann wegen des Hinweises auf eine Beschleunigungssteuerung für
einen Industrieroboter (S 286 li Sp Abs 4) - neben der Position q und der Geschwindigkeit q als Stellgrößen (S 499 li Sp Abs 4 und S 500 le Abs bis S 501
Abb) - zusätzlich die Anregung, auch die Beschleunigung q als Stellgröße vorzusehen.


Die Einsprechende stellte den Antrag,


         den angefochtenen Beschluss aufzuheben und das Patent zu
         widerrufen.


Der Patentinhaber stellte den Antrag,


         die Beschwerde zurückzuweisen.


Der Patentinhaber ist der Auffassung, es handele sich bei dem Verfahren des
Patentanspruchs 1 - auch wenn in einem gewissen Zeitabschnitt gesteuert und
nicht mehr geregelt werde - um ein Regelungsverfahren, da Soll- und Ist-Werte
verarbeitet würden; er sieht auch in der Zusammenschau der beiden Entgegenhaltungen keinen Weg, um zur Erfindung zu gelangen.


Wegen weiterer Einzelheiten wird auf den Akteninhalt verwiesen.

                                       -6-



                                        II


Die zulässige Beschwerde konnte keinen Erfolg haben, weil der Patentanspruch 1
kein mathematisches Verfahren als solches beschreibt und weil das Verfahren des
Patentanspruchs 1 neu ist und auf einer erfinderischen Tätigkeit beruht.


1. Mathematisches Verfahren als solches


Der Senat hält das Verfahren des Patentanspruchs 1 für kein mathematisches
Verfahren als solches, wie sich aus der zutreffenden Begründung der Patentabteilung 33 im Beschluss vom 2. August 2001 im Einzelnen nachvollziehbar ergibt, auf
den hier verwiesen wird (vgl BGH, GRUR 1993, 896 f "Leistungshalbleiter").


2. Stand der Technik


Aus dem Lexikon "Meß- und Automatisierungstechnik" von Schrüfer, E., VDI-Verlag 1992, S 499 bis 501 und 285, 286 sind numerische Regelungsverfahren zur
Regelung der Lage und der Geschwindigkeit einer von einem Motor bewegten
Last (Industrieroboter-Hand) bekannt. Dabei werden ein Ist-Wert q und dessen
erste zeitliche Ableitung q als Regelgrößen, sowie die beiden zugehörigen, vorgegebenen Soll-Werte qr und qr zu einer Stellgröße F verarbeitet (S 499, 500 Abbildungen: Regelungsverfahren 1 bis 3). Bei diesen Verfahren werden die Soll-Werte
qr, qr für die Lage und die Geschwindigkeit von Soll- bzw Referenzbahnen vorgegeben (S 499 li Sp Mitte und re Sp Mitte bzw S 500 li Sp letzter Abs bis re Sp
Abs 1). Bei den bekannten Regelungsverfahren wird die Stellgröße F daher entsprechend vorgegebener Soll- bzw Referenzkurven geregelt. In der Druckschrift
ist neben einer Positions- und einer Geschwindigkeitssteuerung auch eine Beschleunigungssteuerung für Industrieroboter erwähnt (S 286 li Sp). Im Zusammenhang mit diesen Angaben liest der Fachmann, hier ein Diplomingenieur mit
Hochschulstudium und Kenntnissen der numerischen Steuerung und Regelung

                                        -7-



mit, dass für eine Soll- bzw Referenzbahn auch die Beschleunigung vorgegeben
werden kann, entsprechend der zu regeln ist.


In dem Buch von Sciavicco, L. und Siciliano, B.: "Modeling and control of robot
manipulators", 1996, McGrawHill, 1. Aufl., S. 170 bis 175 sind Bahnkurven (Profile) für die Punkt-zu-Punkt-Bewegung eines Manipulators dargestellt (Fig 5.1 iVm
mit Gleichungen 5.1), die den Weg, die Geschwindigkeit und die Beschleunigung
als Funktion der Zeit zeigen. Nach den Gleichungen 5.1 berechnet sich der zwischen einem Initialisierungspunkt t = 0 und einem finalen Punkt t = tf = 1 gelegene
Weg entsprechend einem kubischen Polynom (Fig 5.1: pos). Die Geschwindigkeit
berechnet sich entsprechend einer Parabel (Fig 5.1: vel) und die Beschleunigung
entsprechend einer Geraden (Fig 5.1: acc).


3. Neuheit


Die aus dem Lexikon "Meß- und Automatisierungstechnik" aaO bekannten Regelungsverfahren beruhen darauf, dass einem Regler für Industrieroboter jeweils
Soll-Werte für die Lage qr und die Geschwindigkeit qr vorgegeben werden, die von
off-line berechneten, gespeicherten Soll- bzw Referenzbahnen herrühren (S 499
li Sp Abs 3 und re Sp Mitte bzw S 500 li Sp letzter Abs bis re Sp Abs 1). Entsprechend dieser Soll-Referenzbahnen wird der Industrieroboter anhand der festgestellten Ist-Werte q, q geregelt, dh die Stellgröße F gebildet (S 499 li Sp Abs 4 iVm
mit Abbildung und S 500 letzter Abs bis re Sp Abb).


Das Verfahren des Patentanspruchs 1 unterscheidet sich von den aus dem Lexikon "Meß- und Automatisierungstechnik" aaO bekannten Regelungsverfahren somit dadurch, dass jeweils nur ein Soll-Wert für die Lage und Geschwindigkeit,
nämlich Ssoll und Vsoll als die dem Regelziel zum Zeitpunkt t = ta entsprechenden
Führungsgrößen vorgegeben werden und zusammen mit nur jeweils einem Ist-Wert für die Lage Sist und die Geschwindigkeit Vist als die zum Zeitpunkt t = 0 fest-

                                         -8-



gestellten Regelgrößen zu einer Stellgröße aLast entsprechend der im Patentanspruch 1 angegebenen Gleichung berechnet werden.


Im Buch von Sciavicco, L. und Siciliano, B.: "Modeling and control of robot manipulators" aaO ist in Übereinstimmung mit der im Patentanspruch 1 enthaltenen
Gleichung „aLast(t) = k1 + k2 × t“ zwar angegeben, dass eine Last (Manipulator) bei
einer Punkt-zu-Punkt-Bewegung linear beschleunigt werden soll (S 172 Gl 5.1:
q = 6a3t + 2a2). Ein numerisches Regelverfahren ist in Zusammenhang mit dieser
Gleichung in dem Buch aber nicht angesprochen.


Das Verfahren des Patentanspruchs 1 unterscheidet sich schon deshalb von dem
daraus Bekannten.


Die übrigen noch im Verfahren befindlichen Entgegenhaltungen, die in der mündlichen Verhandlung weder vom Senat noch von den Beteiligten aufgegriffen wurden, gehen über den vorstehend abgehandelten Stand der Technik nicht hinaus
und bringen auch keine neuen Gesichtspunkte, so dass auf sie nicht eingegangen
zu werden braucht.


4. Erfinderische Tätigkeit


Das im Patentanspruch 1 beschriebene Verfahren weist im Gegensatz zur Auffassung der Einsprechenden alle charakteristischen Eigenschaften eines Regelungsverfahrens auf. Denn bei ihm wird jeweils ein Soll-Wert Ssoll, Vsoll vorgegeben, der
mit jeweils einem festgestellten Ist-Wert Sist, Vist zu einer Stellgröße aLast(t) verarbeitet wird. Damit beruht das Verfahren - im Gegensatz zu einer Steuerung - auf
einem geschlossenen Regelkreis.


Als nächstkommenden Stand der Technik sieht der Senat daher das Regelungsverfahren beschreibende "Lexikon Meß- und Automatisierungstechnik" aaO an.

                                        -9-



Ausgehend von dem dort beschriebenen Verfahren mag der Fachmann in Kenntnis des Buches von Sciavicco, L. und Siciliano, B.: "Modeling and control of robot
manipulators" aaO zwar darauf kommen, die dort angegebenen Gleichungen als
Soll- bzw Referenzbahnen vorzusehen. Auch wird er, wenn er die Beschleunigung
als Stellgröße benötigt, als Soll- bzw Referenzbahn gemäß den dortigen Vorgaben
eine Geradengleichung verwenden (Gl 5.1: q = 6a3t + 2a2). Damit ist er jedoch
nicht beim Gegenstand des Patentanspruchs 1; er hat lediglich das aus dem Lexikon "Meß- und Automatisierungstechnik" bekannte Verfahren so ausgestaltet,
dass die Beschleunigung entsprechend einer eine Gerade darstellenden Soll- bzw
Referenzbahn geregelt wird.


Dagegen hat der Anmelder ein Verfahren gefunden, das darauf beruht, auf eine
off-line-berechnete, gespeicherte, und die Soll-Werte enthaltende Soll- bzw Referenzbahn zu verzichten und stattdessen den darin enthaltenen Kurvenverlauf im
Regler nach der im Patentanspruch 1 angegebenen Formel zu ermitteln, zu deren
Berechnung jeweils ein Soll-Wert Ssoll, Vsoll, jeweils ein Ist-Wert Sist, Vist und die
Ausregelzeit ta bekannt sein müssen.


Der Fachmann musste demnach erfinderisch tätig werden, um ein numerisches
Regelungsverfahren mit den Merkmalen des Patentanspruchs 1 anzugeben. Zu
einer anderen Sichtweise könnte der Fachmann nur mit einer in Kenntnis der Erfindung vorgenommenen rückschauenden und deshalb unzulässigen Betrachtung
kommen.


Mit dem dem Erteilungsantrag zugrundeliegenden Patentanspruch 1 haben auch
die auf diesen direkt oder indirekt rückbezogenen Patentansprüche 2 bis 10 Bestand.


Dr. Kellerer             Schmöger                     Dr. Mayer                 Groß


                                                                                   Be
