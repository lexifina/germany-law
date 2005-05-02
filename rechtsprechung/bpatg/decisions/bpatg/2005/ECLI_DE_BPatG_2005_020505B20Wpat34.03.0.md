---
ecli: "ECLI:DE:BPatG:2005:020505B20Wpat34.03.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 34/03"
decided: "2005-05-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2005&Sort=1&Seite=44&nr=18578&anz=1972&pos=666&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2005-05-02_20_W-pat_34_03_NA_0.txt"
---

# Bundespatentgericht, 20 W (pat) 34/03 vom 2005-05-02

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 34/03                                                   Verkündet am
 _______________                                                     2. Mai 2005
    (Aktenzeichen)                                                       …




                              BESCHLUSS

                            In der Beschwerdesache


               betreffend die Patentanmeldung 199 43 724.6-42


…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die    mündliche     Verhandlung   vom   2.   Mai   2005   durch    den   Richter
Dipl.-Phys. Dr. Hartung als Vorsitzenden sowie die Richterin Martens, den Richter
Dipl.-Phys. Dr. Zehendner und den Richter Dipl.-Phys. Dr. Häußler




BPatG 154
6.70

                                       -2-



beschlossen:


         Die Beschwerde wird zurückgewiesen.


                                   Gründe


                                        I


Die Patentanmeldung wurde vom Patentamt mit der Begründung zurückgewiesen,
der Gegenstand des damals geltenden einzigen Patentanspruchs beruhe nicht auf
einer erfinderischen Tätigkeit.


Die Anmelderin beantragt,


        den angefochtenen Beschluss aufzuheben und das Patent mit
        dem Patentanspruch, eingegangen am 7. April 2005, zu erteilen.


Der Patentanspruch lautet:


        "Anordnung zum Erzeugen von synchronisierten Taktimpulsen
        in mehreren an einen Feldbus (1) angeschlossenen und mit jeweils einem Taktgeber (12) versehenen Slave-Einrichtungen (3
        bis 7), die über den Feldbus (1) mit einer Master-Anordnung (2)
        verbunden sind, mittels über den Feldbus (1) an die Slave-Einrichtungen (3 bis 7) übermittelten Synchronisationstelegrammen,
        dadurch gekennzeichnet, dass
        jeder Slave-Einrichtung (3 bis 7) eine Phase-Lock-Loop-Schaltungsanordnung (10) zugeordnet ist, die einerseits die Synchronisationstelegramme empfängt und andererseits mit den Aus-

                                        -3-



        gangsimpulsen des Taktgebers (12) der jeweiligen Slave-Einrichtung (3 bis 7) beaufschlagt ist und an ihrem Ausgang (13)
        die synchronisierten Taktimpulse (T) abgibt."


Es werden ua folgende Druckschriften erörtert:


      (1)    Patent Abstracts of Japan zu JP 07-281 785 A,
      (1a)   englischsprachige Übersetzung der unter (1) genannten Druckschrift JP 07-281 785 A,
      D4     CiA CANopen, CAL-based Communication Profile for Industrial
             Systems, CiA Draft Standard 301, Version 3.0, October 1996,
             Seiten 6-1 bis 6-2.


Die Anmelderin führt im wesentlichen aus, die vorliegende Erfindung gehe von einem Stand der Technik aus, wie ihn der Standard gemäß D4 beschreibe. Der
Fachmann habe keine Veranlassung, die durch diese Norm vorgegebene Anordnung zu verändern, vor allem hinsichtlich der in D4 beschriebenen Vorgaben zum
Synchronisieren der Daten auf einem Feldbus, zB mittels eines Zeitstempels.
Auch der weiters durch Druckschriften belegte Stand der Technik gebe keinen
Hinweis darauf, Slave-Einrichtungen mit einem Taktgeber zu versehen und mit
dessen Ausgangsimpulsen eine jeder Slave-Einrichtung zugeordnete Phase-Lock-Loop-Schaltungsanordnung zu beaufschlagen. Bei dem aus der Druckschrift (1),
resp (1a), als bekannt entnehmbaren Bussystem handle es sich nicht um einen
Feldbus iSd der vorliegenden Erfindung, auch sei keine Übermittlung von Synchronisationstelegrammen beschrieben, sondern eine Übertragung von Synchronisationssignalen über eine eigens dafür vorgesehene Leitung des Bussystems.


                                         II


Die Beschwerde ist zulässig. Sie führt jedoch nicht zum Erfolg.

                                      -4-



Der Gegenstand des Patentanspruchs beruht nicht auf einer erfinderischen Tätigkeit.


Als Fachmann ist ein Hochschulingenieur der Fachrichtung Nachrichtentechnik mit
vertieften Kenntnissen auf dem Gebiet der Datenübertragung in allgemeinen Bussystemen anzusehen, der insbesondere auch mit den Timing- und Synchronisationstechniken solcher Bussysteme vertraut ist.


a) Aus der Druckschrift (1a) iVm (1), vgl den Abstract und die Zeichnung, resp die
Zeichnung 1 und die Abschnitte [0015] bis [0029], ist eine Anordnung zum Erzeugen von synchronisierten Taktimpulsen in mehreren an einen Bus B angeschlossenen Slave-Einrichtungen b1 bis bn als bekannt entnehmbar, die über den Bus B
mit einer Master-Anordnung a verbunden sind (vgl insbesondere Abstract und
[0015]). Über den Bus B (Busleitung BA) werden an die Slave-Einrichtungen b1
bis bn Synchronisationssignale übermittelt (Abstract, reference signal, [0016],
[0019]). Jeder Slave-Einrichtung b1 bis bn ist eine Phase-Lock-Loop-Schaltungsanordnung 23 zugeordnet, die einerseits die Synchronisations- (Referenz-) signale
empfängt und an ihrem Ausgang (Pfeil zur CPU 22) die synchronisierten Taktimpulse abgibt (Abstract, [0019]).


Unter die in (1) resp (1a) abgehandelten allgemeinen Bussysteme subsumiert der
Fachmann auch Feldbusse. Nachdem außerdem die in (1), (1a) genannten Problemstellungen, nämlich den Betrieb der Anordnung und die Datenübertragung zwischen den Busteilnehmern zu beschleunigen und insbesondere das Zeitverhalten
und die Synchronisation zwischen den Busteilnehmern zu verbessern (vgl
Abstract und Abschnitte [0007] bis [0010]) Bussystemen allgemein - auch Feldbussen - zu eigen sind, bringt der Fachmann die aus (1) und (1a) als bekannt entnehmbare Anordnung auch bei dem erfindungsgemäßen Feldbus in Anschlag.

                                       -5-



Des weiteren erzeugt nach (1), (1a) die den Slave-Einrichtungen b1 bis bn zugeordnete Phase-Lock-Loop-Schaltungsanordnung 23 interne Taktimpulse (Abstract:
internal operation clock; [0019]: interior-action clock), die durch die Phase-Lock-Loop-Schaltungsanordnung 23 synchronisiert werden mit den über den Bus übermittelten Synchronisationssignalen und dann am Ausgang der Phase-Lock-Loop-Schaltungsanordnung 23 abgegeben werden (Abstract; [0019]). Überdies wird die
bekannte Phase-Lock-Loop-Schaltungsanordnung 23 bei einem Ausfall der durch
den Bus übermittelten Referenzsignale freilaufend betrieben, dh, sie gibt dann an
ihrem Ausgang von ihr selbst erzeugte Taktimpulse ab. Der Fachmann versteht
somit die bekannte Phase-Lock-Loop-Schaltungsanordnung 23 dergestalt, dass
diese einen (internen) Taktgeber aufweist, dessen Ausgangsimpulse bei Vorliegen
der durch den Bus übermittelten Synchronisationssignale mit diesen durch die
Phase-Lock-Loop-Schaltungsanordnung 23 synchronisiert werden, wobei letztere
dann an ihrem Ausgang die synchronisierten Taktimpulse abgibt (vgl zusätzlich zu
[0019] auch [0022] bis [0024], [0026] und [0029]). Es steht im Belieben des Fachmanns, anstelle des in der Phase-Lock-Loop-Schaltungsanordnung 23 angeordneten Taktgebers einen solchen als eine eigenständige Schaltungskomponente
vorzusehen. Eigenständige Taktgeber an sich, insbesondere auch in Slave-Einrichtungen, sind dem Fachmann ebenfalls geläufig (vgl (1), (1a), Zeichnung 1,
Taktgeber 2; Zeichnung 2, Taktgeber 201).


b) Damit ist der Fachmann aber ohne erfinderische Überlegungen bereits zum Gegenstand des Patentanspruchs gelangt.


Zwar weist, wie die Anmelderin und Beschwerdeführerin argumentiert, die aus (1)
resp (1a) als bekannt entnehmbare Anordnung, insbesondere deren Bus B, im
Gegensatz zu dem erfindungsgemäßen Feldbus eine eigene - zusätzliche - Leitung BA zur Übermittlung der Synchronisationssignale (Referenzsignale) auf, wobei die Synchronisationssignale auch nicht als Synchronisationstelegramme, sondern in anderer Form übermittelt werden, jedoch wird eine solche eigene Leitung
zur Übermittlung von Synchronisationstelegrammen durch die vorliegende Formu-

                                        -6-



lierung des geltenden Anspruchs zumindest nicht ausgeschlossen. Auch könnte
eine der Argumentation der Anmelderin entsprechende Fassung des Patentanspruchs das Vorliegen einer erfinderischen Tätigkeit nicht begründen. Der Fachmann entnimmt bereits der Druckschrift (1), (1a), dass es auch Bussysteme ohne
eine separate Leitung BA zur Übermittlung von Referenzsignalen gibt (vgl zB
Zeichnung 2), und außerdem ist nach (1), (1a) Vorsorge getroffen für einen Ausfall
der Referenzsignale, beides ist für den Fachmann Veranlassung, auch den Verzicht auf eine gesonderte Leitung für Synchronisationssignale zumindest ins Auge
zu fassen. Selbstverständlich ist dem Fachmann dabei die Übermittlung von Synchronisationssignalen in Form von Synchronisationstelegrammen, wenn - verschiedene - Daten abwechselnd und seriell über ein und dieselbe Leitung übertragen werden. Ein solches Vorgehen entnimmt der Fachmann ebenfalls bereits der
(1), (1a), zB betreffs der Datenleitung BC, vgl Zeichnung 1.


Der weiters von der Anmelderin vorgetragenen Auffassung, dass durch den Standard D4 als dem Stand der Technik, der für die vorliegende Erfindung von grundlegender und normativer Bedeutung sei, der Fachmann auf die dort beschriebene
Problemstellung bzgl einer Synchronisation insbesondere mittels Zeitstempeln gewissermaßen festgelegt gewesen sei, kann ebenfalls nicht gefolgt werden. Vielmehr sind auch in der D4 bereits weitere Möglichkeiten zur Verbesserung der Synchronisation genannt, insbesondere auch zusätzliche Leitungen, vgl Seite 6-2, Abschnitt 6.2, letzter Satz, und Abschnitt 6.3. Der Fachmann sah sich deshalb durchaus veranlasst, Stand der Technik aus dem weiteren Umfeld allgemeiner Bussysteme, wie durch (1), (1a) druckschriftlich belegt, in seine Betrachtungen einzubeziehen.

                                         -7-



c) In Anbetracht der Sachlage kann die Frage, ob die Fassung des Patentanspruchs zulässig ist, dahingestellt bleiben.


Dr. Hartung             Martens                Dr. Zehendner   Dr. Häußler


                                                                        Be
