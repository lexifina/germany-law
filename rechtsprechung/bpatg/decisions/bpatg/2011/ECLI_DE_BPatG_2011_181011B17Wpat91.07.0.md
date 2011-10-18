---
ecli: "ECLI:DE:BPatG:2011:181011B17Wpat91.07.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 91/07"
decided: "2011-10-18"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2011&Sort=1&Seite=68&nr=22789&anz=1310&pos=1031&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2011-10-18_17_W-pat_91_07_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 91/07 vom 2011-10-18

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 91/07                                                   Verkündet am
_______________                                                    18. Oktober 2011
    (Aktenzeichen)                                                        …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2006 028 646.4-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 18. Oktober 2011 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch, der Richterin Eder, des Richters
Dipl.-Ing. Baumgardt und der Richterin Dipl.-Phys. Dr. Thum-Rung




BPatG 154
05.11

                                      -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe:


                                       I.


Die vorliegende Patentanmeldung ist am 22. Juni 2006 unter der Bezeichnung


     „Auswertungsverfahren für Bilddatensätze mit selbsttätiger Bestimmung
                          von Auswertungsbereichen“


eingereicht worden.


Die Prüfungsstelle für Klasse G06T hat durch Beschluss vom 24. Mai 2007 die
Anmeldung zurückgewiesen, da die mit dem Anspruch 1 beanspruchte Lehre
gemäß § 1 Abs. 3 und 4 PatG vom Patentschutz ausgeschlossen sei.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin.


Die Beschwerdeführerin beantragt,


       den angegriffenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 bis 21 und Beschreibung Seiten 1 bis 4, 4a,
       4b, 7, 8, 10, 12, 21 bis 23, jeweils vom 27. September 2011, eingegangen am 27. September 2011,

                                         -3-



          Beschreibung Seiten 5, 6, 9, 11, 13 bis 20 und 8 Blatt Zeichnungen mit 22 Figuren, jeweils vom Anmeldetag,


          wobei in Beschreibung Seite 6 Zeile 1 „ihren“ ersetzt werden soll.


Im Prüfungsverfahren vor dem Deutschen Patent- und Markenamt ist die Druckschrift


          D1: DE 100 26 700 A1


genannt worden.


Vom Senat wurden zusätzlich die Druckschriften


          D2: JP 09-285465 A (mit Abstract und Computerübersetzung)
          D3: DE 10 2004 060 396 A1


eingeführt.


Zu den Einzelheiten wird auf die Akte verwiesen.




                                          II.


Die Beschwerde ist frist- und formgerecht eingereicht und auch sonst zulässig. Sie
konnte jedoch keinen Erfolg haben, da die Gegenstände des Patentanspruchs 1
und der nebengeordneten Patentansprüche 20 und 21 nicht auf erfinderischer
Tätigkeit beruhen (§ 1 Abs. 1 in Verbindung mit § 4 Satz 1 PatG).

                                       -4-



1.   Die Patentanmeldung betrifft ein Auswertungsverfahren für Bilddatensätze
eines Untersuchungsobjekts, die einander örtlich entsprechen; außerdem einen
Datenträger, auf dem ein entsprechendes Computerprogramm gespeichert ist,
sowie einen Rechner mit einem derartigen Computerprogramm.


Gemäß der Beschreibung fallen bekanntermaßen Auswertungsverfahren für Bilddatensätze eines Untersuchungsobjekts - oftmals eines Menschen - bei vielen
Anwendungen an, unter anderem bei der Auswertung medizinischer Bilder. Ein
typisches Beispiel seien Bilddatensätze, die Blutgefäße und von den Blutgefäßen
mit Blut versorgtes Gewebe zeigten, wobei in das Blut ein Kontrastmittel injiziert
sei. Solche Bilddatensätze fielen beispielsweise bei angiographischen Untersuchungen des menschlichen Gehirns oder des menschlichen Herzens an.


In einer Vielzahl von Fällen führe ein Rechner Auswertungen der Bilddatensätze
durch. Anhand einer zeitlichen Sequenz der Bilddatensätze könne der Rechner
beispielsweise eine Perfusionsanalyse des mit Blut versorgten Gewebes vornehmen oder eine Flussgeschwindigkeit des Blutes in Gefäßen bestimmen.


Um eine rechenintensive Auswertung in den gesamten Bilddatensätzen zu vermeiden, sei es möglich, dass dem Rechner vom Bediener ein Auswertungsbereich
(oftmals als ROI = region of interest bezeichnet) vorgegeben werde und der Rechner die Auswertung auf den Auswertungsbereich beschränke. Jedoch sei die Vorgabe des Auswertungsbereichs durch einen Bediener zeitaufwändig und fehlerträchtig.


Gemäß S. 3 Abs. 2 der geltenden Beschreibung soll die Aufgabe der vorliegenden
Anmeldung darin bestehen, ein Auswertungsverfahren für eine zeitliche Folge von
Bilddatensätzen eines Untersuchungsobjekts zu schaffen, mittels dessen eine
selbsttätige Ermittlung des Auswertungsbereichs möglich ist.

                                         -5-



Der mit einer möglichen Gliederung versehene Patentanspruch 1 betrifft ein


       a)      Auswertungsverfahren für eine zeitliche Folge von Bilddatensätzen (1 bis 7) eines Untersuchungsobjekts,

       b)      wobei jeder Bilddatensatz (1 bis 7) eine Vielzahl von Bilddatenelementen (9) aufweist,

       c)      wobei jedem Bilddatenelement (9) ein Ort (x, y) in einem mehrdimensionalen Raum zugeordnet ist und jedes Bilddatenelement (9) einen Bilddatenwert aufweist,

       d)      wobei die Bilddatenwerte örtlich miteinander korrespondierender
       Bilddatenelemente (9) der Bilddatensätze (1 bis 7) durch zumindest im
       Wesentlichen örtlich gleiche Bereiche des Untersuchungsobjekts bestimmt
       sind,

       e)      wobei ein Rechner (10) für jeden Bilddatensatz (1 bis 7) selbsttätig

       e1) unter Anwendung einer auf den Bilddatenwerten der Bilddatenelemente (9) der Bilddatensätze (1 bis 7) basierenden Gesamtzuordnungsvorschrift den jeweiligen Bilddatensatz (1 bis 7) in einen Leerbereich (22) und einen Signalbereich (23) aufteilt, so dass jedes Bilddatenelement (9) des jeweiligen Bilddatensatzes (1 bis 7) entweder
               dem Leerbereich (22) oder dem Signalbereich (23) zugeordnet ist,

       e2) eine den Signalbereich (23) des jeweiligen Bilddatensatzes (1 bis 7)
               vollständig enthaltende geschlossene Hülle (24) ermittelt und

       e3) anhand der geschlossenen Hülle (24) des jeweiligen Bilddatensatzes (1 bis 7) einen Auswertungsbereich (8) ermittelt, so dass eine
               weitere Auswertung des jeweiligen Bilddatensatzes (1 bis 7) auf dessen Auswertungsbereich (8) beschränkbar ist,

                                        -6-



       f)    wobei der Rechner (10) für einen bestimmten der Bilddatensätze (1
       bis 7) dessen Auswertungsbereich (8) anhand des Signalbereichs (23) des
       bestimmten Bilddatensatzes (1 bis 7) sowie der Signalbereiche (23) der
       zeitlich vor oder nach dem bestimmten Bilddatensatz (1 bis 7) liegenden
       Bilddatensätze (1 bis 7) ermittelt.


Der nebengeordnete Patentanspruch 20 betrifft einen


       Datenträger, auf dem ein Computerprogramm (20) gespeichert ist, wobei
       das Computerprogramm (20) bewirkt, dass ein Rechner (10) ein Auswertungsverfahren nach einem der obigen Ansprüche ausführt, wenn das
       Computerprogramm (20) in den Rechner (10) geladen ist und vom Rechner (10) ausgeführt wird.


Der nebengeordnete Patentanspruch 21 betrifft einen


       Rechner, der einen Massenspeicher (13) aufweist, in dem ein Computerprogramm (20) gespeichert ist, wobei der Rechner nach Aufruf des Computerprogramms (20) ein Auswertungsverfahren nach einem der Ansprüche 1 bis 19 ausführt.


Gemäß den Merkmalen a) bis d) sollen mehrere Bilddatensätze eines Untersuchungsobjekts ausgewertet werden, die jeweils in etwa denselben Objektbereich
darstellen. Es kann sich um zu unterschiedlichen Zeitpunkten aufgenommene
Bilddaten handeln, die beispielsweise die Ausbreitung eines Kontrastmittels in
Blutgefäßen zeigen. Jeder Bilddatensatz wird gemäß Merkmal e1) in einen Leerbereich und in einen Signalbereich unterteilt; im einfachsten Fall kann dies über
eine auf die einzelnen Bilddatenelemente wirkende Schwellwertoperation erfolgen,
vgl. Fig. 10. Anhand dieser Unterteilung wird eine den Signalbereich umschließende Hülle ermittelt, etwa ein den Signalbereich umschließendes Rechteck, vgl.
in Fig. 2 bis 7 die mit 8a bis 8f bezeichneten Bereiche (Merkmal e2)). Anhand die-

                                         -7-



ser Hülle wird ein Auswertebereich bestimmt, der beispielsweise etwas größer
sein kann als die Hülle (vgl. den die Hülle 24 im Abstand a umgebenden Auswertebereich in Fig. 3), der aber auch die Hülle selbst sein kann; die weitere Auswertung ist auf diesen Bereich beschränkbar (Merkmal e3)).


Hierbei ermittelt der Rechner für einen bestimmten der Bilddatensätze dessen
Auswertungsbereich anhand des Signalbereichs des bestimmten Bilddatensatzes
sowie der Signalbereiche der zeitlich vor oder nach dem bestimmten Bilddatensatz
liegenden Bilddatensätze (Merkmal f)).


Der Auswertebereich kann für jeden Bilddatensatz individuell bestimmt werden,
vgl. die ursprünglichen Ansprüche 1 und 20; er kann aber auch für alle Bilddatensätze einheitlich bestimmt sein, vgl. die ursprünglichen Ansprüche 1 und 21.


Als Fachmann sieht der Senat hier einen in der medizinischen Bilddatenverarbeitung erfahrenen Fachhochschul- oder Hochschul-Ingenieur der Fachrichtung Informationstechnik an.


2.   Die Gegenstände des geltenden Anspruchs 1 und der nebengeordneten
Ansprüche 20 und 21 beruhen nicht auf erfinderischer Tätigkeit.


Die Druckschrift D2 zeigt ein Auswerteverfahren von zeitlich aufeinander folgenden Ultraschallbilddatensätzen eines schlagenden Herzens, vgl. Abstract sowie
Abs. [0012] Satz 4 der Computerübersetzung („... in each frame for example, in 1
heartbeat.“) - Merkmal a). Jeder Bilddatensatz weist wie üblich eine Vielzahl von
Bilddatenelementen mit zugehörigen Bilddatenwerten auf, wobei die zeitlich aufeinander folgenden Bilddatensätze jeweils im Wesentlichen denselben Bereich
des zu untersuchenden Objekts (Schnitt durch Patientenherz) darstellen, somit
jedem Bilddatenelement ein Ort in einem mehrdimensionalen Raum (vom Ultraschallfächer erfasster Herzbereich) zugeordnet ist und die Bilddatenwerte korrespondierender Bilddatenelemente der Bilddatensätze durch im Wesentlichen örtlich

                                       -8-



gleiche Bereiche des Untersuchungsobjekts bestimmt sind - Merkmale b), c), d).
Gemäß dem Abstract soll automatisch ein geschlossener elliptischer Bereich („region of interest“) festgelegt werden, der eine aus den Bilddaten extrahierte Kontur
einer Herzkammer umhüllt. Hierzu wird in jedem Bilddatensatz („frame“) eines
Herzschlagzyklus die Kontur einer Herzkammer automatisch ermittelt, vgl.
Abs. [0012] Satz 1 bis 4; d. h. jeder Bilddatensatz wird (über eine auf den Bilddatenwerten basierende Zuordnungsvorschrift) in einen Signalbereich (Herzkammer
mit Kontur) und einen Leerbereich eingeteilt - Merkmal e1) i. V. m. e). Gemäß
Abs. [0012] und [0017] ff. wird aus den in den einzelnen Bilddatensätzen ermittelten Konturen die Neigung und die Länge der Achsen einer gemeinsamen umhüllenden Ellipse ermittelt. Als nachfolgende Auswertung ist in Abs. [0001] die
Bestimmung der Fläche der Herzkammer angegeben, die gemäß Abs. [0003] bis
[0005] auf den geschlossenen Hüllbereich („region of interest“) beschränkt ist,
d. h. der ermittelte Hüllbereich dient als Auswertebereich für einen betrachteten
Bilddatensatz - Merkmale e2), e3). Durch diese Beschränkung ist gemäß Fig. 5
mit Beschreibung die Konturverfolgung und Flächenbestimmung weniger fehlerbehaftet als bei Auswertung im gesamten Bildbereich, da die Hülle für Bereiche mit
unvollständiger Kontur als Konturgrenze dient.


Ob der ermittelte Auswertebereich für nur einen Bilddatensatz oder für alle Bilddatensätze verwendet wird, geht aus D2 nicht eindeutig hervor; eine Auswertung in
allen Bilddatensätzen drängte sich jedoch dem Fachmann auf, um bei der nachfolgenden Auswertung den zeitlichen Verlauf eines interessierenden Parameters
(hier: Fläche der Herzkammer) zu ermitteln. Gemäß dem Ausführungsbeispiel in
D2 werden zur Ermittlung der Neigung und ebenso der Größe (Länge der Achsen)
des elliptischen Auswertebereichs alle Bilddatensätze in einem Herzschlag herangezogen; somit ist davon auszugehen, dass der ermittelte Auswertebereich
einheitlich für alle auszuwertenden Bilddatensätze herangezogen wird. Eine für
den Fachmann naheliegende Alternative besteht darin, den Auswertebereich, insbesondere die Längen der Ellipsenachsen für jeden Bilddatensatz individuell zu
bestimmen, so dass der Auswertebereich, innerhalb dessen die Kontur der Herz-

                                       -9-



kammer verfolgt wird, nicht nur an die Gesamtheit der Bilddatensätze, sondern
(noch etwas genauer) an jeden Bilddatensatz individuell angepasst werden kann
- Merkmal e) i. V. m. e2) und e3).
Bei einer solchen individuellen Festlegung schlagen, wie dem Fachmann bewusst
war, Schwankungen und sonstige Fehler im gemessenen Bilddatensatz stärker zu
Buche als bei einer Mittelung über sämtliche Bilddatensätze hinweg. Eine einfache, im Griffbereich des Fachmanns liegende Möglichkeit zur Verminderung von
Fehlereinflüssen ist das Heranziehen benachbarter Pixelbereiche, sowohl innerhalb eines Bilddatensatzes als auch über mehrere benachbarte Bilddatensätze
hinweg. Zur Verminderung von Fehlern bei der Festlegung des individuellen Auswertebereichs für einen bestimmten Bilddatensatz bot es sich daher an, nicht nur
diesen Bilddatensatz, sondern auch benachbarte Bilddatensätze heranzuziehen,
also die Signalbereiche der dem bestimmten Bilddatensatz zeitlich benachbarten
Bilddatensätze zu berücksichtigen; dies beinhaltet sowohl solche Bilddatensätze,
die zeitlich vor dem bestimmten Bilddatensatz liegen, als auch solche, die zeitlich
nach dem bestimmten Bilddatensatz liegen. Eine derartige Interpretation ist nach
Überzeugung des Senats von Merkmal f) umfasst.


Durch diese Überlegungen, die ausgehend vom aus D2 Bekannten sämtlich im
Bereich typischen fachmännischen Handelns lagen, konnte der Fachmann zum
Verfahren gemäß dem geltenden Anspruch 1 gelangen, wozu keine erfinderische
Tätigkeit erforderlich war.


Entsprechendes gilt für die Gegenstände der nebengeordneten Ansprüche 20 und
21.


Nach Ansicht der Anmelderin ist „oder“ in Merkmal f) als ausschließendes Oder zu
interpretieren, d. h. dass zusätzlich zu dem bestimmten Bilddatensatz entweder
nur die vor dem bestimmten Bilddatensatz liegenden Bilddatensätze oder nur die
nach dem bestimmten Bilddatensatz liegenden Bilddatensätze herangezogen werden. Zur Stützung dieser Interpretation verweist sie in den Anmeldeunterlagen auf

                                      - 10 -



Fig. 21 Schritt S42 „anhand … der zeitlich eher liegenden (oder der zeitlich später
liegenden) Bilddatensätze“, die zugehörige Beschreibung auf S. 23 Z. 33 bis 35
(„… Auswertungsbereiche der zeitlich eher liegenden oder zeitlich später liegenden Bilddatensätze“) sowie auf Fig. 1 bis 7. Zu diesen Figuren führt sie aus, bei
Stopp des Kontrastmitteleintrags in das Gefäßsystem sei es vorteilhaft, wenn bei
der Festlegung des Auswertebereichs nur die vorhergehenden oder nur die nachfolgenden Figuren mit berücksichtigt würden.


Dieser Argumentation konnte sich der Senat nicht anschließen.


Weder aus der Beschreibung S. 23 Z. 33 bis 35 noch aus der zugehörigen Fig. 21
geht eindeutig hervor, dass die Formulierung in Merkmal f) im Sinne eines ausschließenden Oder zu interpretieren ist. Zudem ist den Figuren 1 bis 7 und den
zugehörigen Beschreibungsteilen kein Hinweis auf die Heranziehung zeitlich vor
oder nach einem bestimmten Bilddatensatz liegender Bilddatensätze zur Festlegung eines Auswertebereichs zu entnehmen; einen sich etwa daraus ergebenden
Vorteil offenbart die Anmeldung ebenfalls nicht. Auch die übrigen Anmeldeunterlagen offenbaren hinsichtlich der fraglichen Formulierung in Merkmal f) keine Hinweise auf eine einschränkende Interpretation. In Ermangelung solcher Hinweise ist
Merkmal f) breit auszulegen und umfasst auch die Interpretation „benachbarte
Bilddatensätze, und zwar sowohl solche, die zeitlich vor dem bestimmten Bilddatensatz liegen, als auch solche, die zeitlich nach dem bestimmten Bilddatensatz
liegen“.


Der Anspruch 1 und ebenso die nebengeordneten Ansprüche 20 und 21 sind
sonach nicht gewährbar.

                                     - 11 -



3.   Da über einen Antrag nur einheitlich entschieden werden kann, sind auch die
abhängigen Patentansprüche 2 bis 19 nicht gewährbar (BGH in GRUR 1997, 120
„Elektrisches Speicherheizgerät“).




Dr. Fritsch             Eder             Baumgardt              Dr. Thum-Rung




                                                                             Fa
