---
ecli: "ECLI:DE:BPatG:2001:180701U4Ni39.00.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 39/00"
decided: "2001-07-18"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2001&Sort=1&Seite=72&nr=16376&anz=1792&pos=1093&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2001-07-18_4_Ni_39_00_NA_0.txt"
cites_law: ["germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 39/00 vom 2001-07-18

## Entscheidung

-1-




             BUNDESPATENTGERICHT

                   IM NAMEN DES VOLKES



                          URTEIL
4 Ni 39/00                                        Verkündet am
(Aktenzeichen)                                    18. Juli 2001




                 In der Patentnichtigkeitssache
…

                                       -2-




                     betreffend das deutsche Patent 31 25 529


hat der 4.Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 18. Juli 2001 unter Mitwirkung des Vorsitzenden
Richters Dr. Schwendy, der Richter Dipl.-Ing. Obermayer und Dipl.-Phys. Kalkoff,
der Richterin Schuster und des Richters Dipl.-Phys. Dr. Hartung




für Recht erkannt:


   1.     Die Klage wird abgewiesen.
   2.     Die Klägerin trägt die Kosten des Rechtsstreits.
   3.     Das Urteil ist gegen Sicherheitsleistung in Höhe von
          DM 18.000.- vorläufig vollstreckbar.




                                   Tatbestand




Die Beklagte ist eingetragene Inhaberin des am 29. Juni 1981 angemeldeten
deutschen Patents (Streitpatent), das ein „Verfahren zum Umkodieren einer Folge
von Datenbits in eine Folge von Kanalbits, Anordnung zum Dekodieren der nach
diesem Verfahren kodierten Kanalbits und Aufzeichnungsträger mit einer gemäß
diesem Verfahren erzeugten Informationsstruktur“ betrifft und 15 Patentansprüche
umfasst. In Patentanspruch 1 und in den auf ihn rückbezogenen Ansprüchen 2 bis

                                        -3-



8 ist das oben genannte Verfahren zum Umkodieren beschrieben. Patentanspruch
1 lautet wie folgt


   „1. Verfahren zum Umkodieren einer Folge Datenbits in eine Folge Kanalbits,
   wobei die Folge Datenbits in unmittelbar aufeinanderfolgende Blöcke von je m
   Datenbits aufgeteilt wird und diese Blöcke in aufeinanderfolgende Blöcke von
   (n1 + n2) Kanalbits (n1 + n2 > m) umkodiert werden und wobei die Blöcke Kanalbits je einen Block von n1 Informationsbits und einen Block von n2 Trennbits enthalten derart, daß aufeinanderfolgende Blöcke von Informationsbits
   durch jeweils nur einen Block Trennbits getrennt werden und daß eine (d, k)-
   Bedingung erfüllt ist, d.h. daß zwei aufeinanderfolgende Kanalbits von einem
   ersten Typ, des Typs „1“, durch mindestens d dann höchstens k unmittelbar
   aufeinanderfolgende Bits eines zweiten Typs, des Typs „0“, getrennt werden,
   gekennzeichnet durch die nachfolgenden Schritte:


   1.      das Umwandeln der Blöcke von m Bits enthaltender Datenbits in n1 Bits
           enthaltende Blöcke Informationsbits derart, daß die (d, k)-Bedingung erfüllt ist;
   2.      das Erzeugen mehrerer möglicher Blöcke von (n1 + n2) Kanalbits durch
           Ergänzen je eines Blocks von n1 Informationsbits durch jeweils einen
           Block aus der Menge aller möglichen Blöcke von n2 Trennbits;
   3.      das Bestimmen derjenigen Blöcke von Kanalbits aus den möglichen
           Blöcken von Kanalbits, die in bezug auf den jeweils vorhergehenden
           und nachfolgenden Block von Kanalbits die (d, k)-Bedingung erfüllen;
   4.      das Ermitteln des Gleichstromanteils jedes der so bestimmten Blöcke
           von Kanalbits, die in dem vorhergehenden Schritt ermittelt wurden;
   5.      das Auswählen des Blocks von Kanalbits mit minimalem Gleichstromanteil aus den in Schritt 4 bestimmten Blöcken.


Die Ansprüche 9 und 10 betreffen den Demodulator. Anspruch 9 lautet:

                                       -4-



9. Demodulator zum Dekodieren der entsprechend dem Verfahren nach einem der
Ansprüche 2 bis 8 umkodierten Kanalbits, gekennzeichnet durch


   -      Mittel zum Detektieren des Synchronisationsmusters;
   -      Mittel zum Aufteilen der Folge von Kanalbits in Blöcke von je (n1 + n2)
          Kanalbits;
   -      Mittel zum Trennen der Blöcke von n1 Informationsbits von den Blöcken
          von n2 Trennbits;
   -      Mittel zum Umwandeln eines Blocks von n1 Informationsbits in einen
          Block von m Datenbits.


Die Ansprüche 11 und 12 betreffen den Aufzeichnungsträger. Anspruch 11 lautet:


       „11. Aufzeichnungsträger mit einer gemäß dem Verfahren nach einem
       der Ansprüche 1 bis 8 erzeugten Informationsstruktur mit Folgen von
       Kanalbitzellen, die je ein Bit enthalten, dessen Wert durch einen Pegelübergang oder einen fehlenden Pegelübergang am Anfang der Bitzelle
       dargestellt wird, dadurch gekennzeichnet, daß der Abstand zwischen
       zwei aufeinanderfolgenden Pegelübergängen maximal gleich (k + 1)
       Bitzellen und minimal gleich (d + 1) Bitzellen ist und daß höchstens
       zwei aufeinanderfolgende maximale Abstände von (k + 1) Bitzellen der
       Pegelübergänge auftreten, die Teil einer Synchronisationsinformation
       bilden.“


Wegen des Inhalts der weiteren Ansprüche wird auf die Streitpatentschrift verwiesen.


Die Klägerin hat zunächst nur die Sachansprüche 11 und 12 angegriffen und hat
behauptet, es handle sich "nicht um Ansprüche im Sinne des Patentgesetzes". Sie
könnten weder als Unter- noch als Nebenansprüche, sondern nur als "anspruchsähnliche Beschreibung" interpretiert werden. Sie beträfen zudem lediglich die

                                         -5-



Wiedergabe von Informationen, was sie vom Patentschutz ausschließe. Die Patentinhaberin habe im übrigen im Streitpatent verschiedene Anspruchskategorien
in unzulässiger Weise miteinander kombiniert und dadurch zugleich gegen das Erfordernis der Einheitlichkeit verstoßen. Die Lehre der angegriffenen Ansprüche 11
und 12 des Streitpatents sei auch nicht neu; das Streitpatent sei deshalb insoweit
für nichtig zu erklären. Zur Begründung hat sich die Klägerin auf folgende, auf die
Beklagte zurückgehende Druckschriften berufen:


1. DE 29 10 390 C2 (N2)
2. DE 29 12 216 C2 (N3)
3. DE 29 35 789 C2 (N4)


Später hat die Klägerin die Klage auf die übrigen Ansprüche erstreckt und greift
nun das Streitpatent in vollem Umfang an. Sie führt dazu aus, Patentanspruch 1
sei unzulässig erweitert und für den Fachmann nicht ausführbar. Auch Anspruch
11 sei gegenüber den ursprünglichen Anmeldungsunterlagen unzulässig geändert
und seine Lehre nicht ausführbar. Im übrigen komme den Ansprüchen 11 und 12
die beanspruchte Priorität nicht zu; die Merkmale dieser Ansprüche seien durch
den Stand der Technik neuheitsschädlich vorweggenommen. Die Klägerin beruft
sich in diesem Zusammenhang auf den Vortrag von L.B. Vries et. al., “The Compact Disc Digital Audio System : Modulation and Error-Correction”, anläßlich der
AES-Tagung in New York vom 31. Oktober bis 3. November 1980.


Die Klägerin beantragt,


     das Streitpatent für nichtig zu erklären.




Die Beklagte beantragt,


      die Klage abzuweisen.

                                      -6-




Sie tritt dem Vorbringen der Klägerin entgegen und hält das Streitpatent für bestandsfähig. Nach ihrer Auffassung betrifft Anspruch 11 einen technischen Gegenstand. Soweit die erteilte Fassung des Anspruches 11 von der ursprünglichen
Anspruchsfassung abweiche, handele es sich lediglich um eine anhand der übrigen Anmeldungsunterlagen vorgenommene sprachliche Glättung.




                            Entscheidungsgründe


Die zulässige Klage, mit der die in § 22 Abs 1 iVm § 21 Abs 1 Nr 1, 2 und 4 PatG
vorgesehene Nichtigkeitsgründe der mangelnden Patentfähigkeit, der mangelnden
Ausführbarkeit und der unzulässigen Änderung geltend gemacht werden, ist unbegründet.


Das Streitpatent betrifft ein Verfahren zum Umkodieren einer Folge Datenbits in
eine Folge Kanalbits sowie einen Demodulator zum Dekodieren der entsprechend
dem Verfahren kodierten Datenbits und einen Aufzeichnungsträger mit einer mittels dieses Verfahrens erzeugten Informationsstruktur mit Folgen von Kanalbitzellen.


Nach der Patentbeschreibung wird dabei die Folge Datenbits in unmittelbar aufeinanderfolgende Blöcke von je m Datenbits aufgeteilt und diese Blöcke in aufeinanderfolgende Blöcke von (n1 + n2) Kanalbits (n1 + n2 > m) umkodiert. Die Blöcke
Kanalbits enthalten je einen Block von n1 Informationsbits und einen Block von n2
Trennbits derart, dass aufeinanderfolgende Blöcke Informationsbits durch jeweils
nur einen Block Trennbits getrennt werden, zwei aufeinanderfolgende Kanalbits
eines ersten Typs, des Typs „1“, durch mindestens d unmittelbar aufeinanderfolgende Bits eines zweiten Typs, des Typs „0“, getrennt werden und die Anzahl unmittelbar aufeinanderfolgender Kanalbits vom zweiten Typ höchstens k ist.

                                      -7-




Bei der digitalen Übertragung oder in magnetischen und optischen Aufnahmebzw. Wiedergabesystemen liege die zu übertragende bzw. aufzunehmende Information meistens in einer Folge von Zeichen vor, die zusammen das (oft binäre)
Alphabet bildeten. Das binäre Alphabet werde durch die Zeichen „1“ und „0“ dargestellt. Das eine Zeichen, bspw. die „1“, könne auf der Magnetplatte, dem Magnetband oder auf der optischen Platte als Übergang zwischen zwei Zuständen von
Magnetisierung oder zwei Orten eines optisch aktiven Bereichs festgelegt werden.
Das andere Zeichen, die „0“, werde durch das Fehlen eines derartigen Überganges festgelegt.


Infolge bestimmter Systemanforderungen bestünden in der Praxis für die Folgen
von Zeichen, die auftreten dürften, Beschränkungen. So werde in manchen Systemen die Anforderung gestellt, dass die Folge von Zeichen selbsttaktend sei.
Dies bedeute, dass die Folge zu übertragender bzw. aufzunehmender Zeichen
genügend Übergänge aufweisen müsse, um ein Taktimpulssignal, das zu Detektion und Synchronisation notwendig sei, aus der Zeichenfolge zu erzeugen. Eine
andere Anforderung könne sein, dass bestimmte Zeichenfolgen in dem Informationssignal vermieden werden sollen, weil diese Folgen bestimmten Zwecken,
bspw. Synchronisationsfolgen, vorbehalten würden. Eine Nachahmung der Synchronisierungsfolge durch das Informationssignal beeinträchtige die Eindeutigkeit
des Synchronisationssignals und damit die Eignung zu diesem Zweck. Eine weitere Anforderung könne sein, die Übergänge einander nicht zu schnell folgen zu lassen, um die Intersymbolinterferenz zu beschränken.
Im Falle magnetischer oder optischer Aufzeichnung könne diese Anforderung
auch mit der Informationsdichte auf dem Aufzeichnungsträger in Zusammenhang
gebracht werden. Wenn bei einem bestimmten Mindestabstand zwischen zwei
aufeinanderfolgenden Übergängen auf dem Aufzeichnungsträger das entsprechende minimale Zeitintervall des aufzuzeichnenden Signals vergrößert werden
könne, werde die Informationsdichte in demselben Ausmaß vergrößert. Auch die

                                       -8-



erforderliche minimale Bandbreite hänge mit dem minimalen Abstand zwischen
den Übergängen zusammen.


Wenn Informationskanäle benutzt würden, die keinen Gleichstrom übertragen, führe dies zu der Anforderung, dass die Zeichenfolgen in dem Informationskanal einen möglichst geringen (oder überhaupt keinen) Gleichstromanteil aufwiesen.


Ein Verfahren der beschriebenen Art sei nach dem Stand der Technik bekannt
(vgl. Tang, D.T., Bahl, L.R., "Block codes for a class of constrained noiseless
channels“, Information and Control, Vol. 17, Nr. 5, Dez. 1970, Seiten 436-461). Ein
Nachteil der Kodierungsart nach diesem Verfahren sei, dass der Anteil der niedrigen Frequenzen (einschließlich Gleichstrom) an dem Frequenzspektrum des
Stromes von Kanalbits ziemlich hoch ist. Ein weiterer Nachteil sei, dass die Kodierwandler (Modulator, Demodulator) und insbesondere der Demodulator verwickelt sind.


Vor diesem Hintergrund formuliert die Streitpatentschrift die Aufgabe, ein Verfahren der eingangs erwähnten Art zum Kodieren einer Folge Datenbits in eine Folge
Kanalbits zu schaffen, das die Niederfrequenzspektrumeigenschaften des aus den
Kanalbits abzuleitenden Signals verbessert und einen einfachen Demodulator ermöglicht.


Patentanspruch 1 beschreibt demgemäß


   ein Verfahren zum Umkodieren einer Folge Datenbits in eine Folge Kanalbits,
   wobei die Folge Datenbits in unmittelbar aufeinanderfolgende Blöcke von je m
   Datenbits aufgeteilt wird und diese Blöcke in aufeinanderfolgende Blöcke von
   (n1 + n2) Kanalbits (n1 + n2 > m) umkodiert werden und wobei die Blöcke Kanalbits je einen Block von n1 Informationsbits und einen Block von n2 Trennbits enthalten derart, dass aufeinanderfolgende Blöcke von Informationsbits
   durch jeweils nur einen Block Trennbits getrennt werden und dass eine (d, k)-

                                            -9-



   Bedingung erfüllt ist, d.h. dass zwei aufeinanderfolgende Kanalbits von einem
   ersten Typ, des Typs „1“, durch mindestens d dann höchstens k unmittelbar
   aufeinanderfolgende Bits eines zweiten Typs, des Typs „0“ getrennt werden,
   gekennzeichnet durch die nachfolgenden Schritte:
   1. das Umwandeln der Blöcke von m Bits enthaltender Datenbits in n1 Bits
        enthaltende Blöcke Informationsbits derart, dass die (d, k)-Bedingung erfüllt
        ist;
   2. das Erzeugen mehrerer möglicher Blöcke von (n1 + n2) Kanalbits durch Ergänzen je eines Blocks von n1 Informationsbits durch jeweils einen Block
        aus der Menge aller möglichen Blöcke von n2 Trennbits;
   3. das Bestimmen derjenigen Blöcke von Kanalbits aus den möglichen Blöcken von Kanalbits, die in Bezug auf den jeweils vorhergehenden und
        nachfolgenden Block von Kanalbits die (d, k)-Bedingung erfüllen;
   4. das Ermitteln des Gleichstromanteils jedes der so bestimmten Blöcke von
        Kanalbits, die in dem vorhergehenden Schritt ermittelt wurden;
   5. das Auswählen des Blocks von Kanalbits mit minimalem Gleichstromanteil
        aus den in Schritt 4 bestimmten Blöcken.




Sachanspruch 11 der auf Anspruch 1 und die Unteransprüche 2 bis 8 zurückbezogen sind, betrifft


„11. Aufzeichnungsträger
   a)          mit einer gemäß dem Verfahren nach einem der Ansprüche 1 bis 8
               erzeugten Informationsstruktur
   b)          mit Folgen von Kanalbitzellen, die je ein Bit enthalten, dessen Wert
               durch einen Pegelübergang oder einen fehlenden Pegelübergang
               am Anfang der Bitzelle dargestellt wird,
   dadurch gekennzeichnet, dass

                                         - 10 -



   c)        der Abstand zwischen zwei aufeinanderfolgenden Pegelübergängen
             maximal gleich (k + 1) Bitzellen und minimal gleich (d + 1) Bitzellen
             ist und dass
   d)        höchstens zwei aufeinanderfolgende maximale Abstände von (k + 1)
             Bitzellen der Pegelübergänge auftreten, die Teil einer Synchronisationsinformation bilden.“


A. Die Schutzdauer des Patents ist zwar am 29. Juni 2001 abgelaufen; in Anbetracht eines parallellaufenden Verletzungsstreits ist aber das Rechtsschutzbedürfnis der Klägerin im vorliegenden Verfahren unzweifelhaft und unstreitig.


B. Zum Patentanspruch 1


Der Patentanspruch 1 ist rechtsbeständig. Die von der Klägerin gegen diesen Anspruch geltend gemachten Widerrufsgründe gemäß § 21 Absatz 1 Nr 2 und 4 stehen ihm nicht entgegen. Der Anspruchsgegenstand geht nicht über den Inhalt der
Anmeldung in der ursprünglich eingereichten Fassung hinaus und ist auch im Patent so deutlich und vollständig offenbart, daß der Fachmann - hier ein Entwickler
mit nachrichtentechnischer Hoch- oder Fachhochschulausbildung und mit mehrjährigen Erfahrungen auf dem Gebiet der digitalen Signalcodierung - ihn ausführen
kann.


1. Die Gesamtheit der Merkmale des Anspruchs 1 ist für den Fachmann aus den
ursprünglichen Anmeldungsunterlagen als zur Erfindung gehörend entnehmbar
und zwar aus dem ursprünglichen Anspruch 1 iVm der ursprünglichen Beschreibung, Seite 9, Zeilen 19 bis 25, Seite 11, Zeile 6 bis Seite 12, Zeile 4 und dem auf
Seite 14, Zeile 17 bis Seite 16, Zeile 37 erläuterten Flußdiagramm von Figur 3.


Aus den vorgenannten Passagen der ursprünglichen Unterlagen ist Folgendes ersichtlich:

                                        - 11 -



Bei dem beschriebenen Verfahren wird sukzessive ein Block von Datenbits nach
dem anderen in einen entsprechenden Block von Kanalbits so umcodiert, daß die
Kanalbits eine (d, k)-Bedingung erfüllen (Oberbegriff des ursprünglichen Anspruchs 1).


Der jeweilige Block von Datenbits wird zunächst in einen entsprechenden Block
von n1 Informationsbits umgewandelt (Schritt 1 des ursprünglichen Anspruchs 1),
der die (d, k)-Bedingung erfüllt (S 9 Z 19 bis 25).


Durch Ergänzen dieses Blocks von n1 Informationsbits durch alle möglichen Bitkombinationen eines Blocks von n2 Trennbits werden mehrere mögliche Blöcke
von n1 + n2 Kanalbits erzeugt (Schritt 2 des ursprünglichen Anspruchs 1 iVm S 11
Z 6 bis 18).


Aus diesen möglichen Blöcken von n1 + n2 Kanalbits werden diejenigen bestimmt,
die in bezug auf den vorhergehenden Block, dh beim Anschließen an diesen, die
(d, k)-Bedingung erfüllen (Schritte 4 und 5 des ursprünglichen Anspruchs 1 iVm
S 11 Z 18 bis 25; ebenso Blöcke 9 und 10 des Flußdiagramms).


Der Gleichstromanteil jedes der so bestimmten Blöcke von Kanalbits wird ermittelt
(Schritt 3 des ursprünglichen Anspruchs 1 iVm S 11 Z 18 bis 26, wonach die Reihenfolge der (d, k)-Prüfung und der Ermittlung des Gleichstromanteils beliebig ist,
also der erstgenannte Vorgang dem Zweitgenannten vorangehen kann; Block 8
des Flußdiagramms).


Aus den so bestimmten Blöcken wird schließlich derjenige mit dem minimalen
Gleichstromanteil ausgewählt (Schritt 6 des ursprünglichen Anspruchs 1 iVm S 11
Z 28 bis 36).


Die gemäß obigem aus den ursprünglichen Unterlagen entnommenen Verfahrensschritte bilden inhaltlich die Merkmale des geltenden Anspruchs 1. Dabei kann

                                        - 12 -



Schritt 3 des geltenden Anspruchs 1 nur so verstanden werden, daß geprüft wird,
ob die (d, k)-Bedingung beim Anschließen des jeweiligen "möglichen" Blocks an
den vorhergehenden Block erfüllt ist, wie aus den oben angeführten Stellen der
ursprünglichen Unterlagen - Seite 11, Zeile 18 bis 25 sowie Blöcke 9 und 10 des
Flußdiagramms - ohne weiteres hervorgeht. Der im geltenden Anspruch 1 aufgeführte "nachfolgende" Block ist demnach der gerade zu überprüfende Block aus
den "möglichen" Blöcken.


Bei dieser Sachlage können die von der Klägerin angeführten Unterschiede des
Anspruchs 1 in der ursprünglichen bzw der erteilten Fassung dahinstehen, da es
grundsätzlich zulässig ist, den ursprünglichen Patentanspruch im Prüfungsverfahren klarzustellen, zu ergänzen oder zu modifizieren, soweit die übrigen Anmeldungsunterlagen hierfür eine Offenbarungsgrundlage bilden.


Insbesondere war es entgegen der Auffassung der Klägerin zulässig, an die Stelle
der die (d, k)-Prüfung über die Blockgrenzen hinweg betreffenden Schritte 4 und 5
des ursprünglichen Anspruchs 1, die kompliziert und schwer verständlich formuliert sind, die auf das wesentliche abzielende Formulierung gemäß Schritt 3 der
erteilten Fassung zu setzen, die der Aussage in der ursprünglichen Beschreibung,
Seite 11, Zeile 21 bis 25 entspricht.


2. Die Klägerin konnte den Senat auch nicht von der mangelnden Ausführbarkeit
des Verfahrens nach Anspruch 1 überzeugen.


Die Klägerin hat diesbezüglich argumentiert, gemäß Anspruch 1 solle in bezug auf
den vorhergehenden und nachfolgenden Block von Kanalbits die (d, k)-Bedingung
erfüllt werden, die Kanalbitstruktur des nachfolgenden Blocks sei aber noch nicht
festgelegt und der Fachmann erhalte keinen Hinweis, wie er dementsprechend
vorgehen solle.

                                      - 13 -



Dieser Einwand greift jedoch nicht durch. Wie nämlich oben unter Ziffer 1 bereits
dargelegt wurde, ist der hier angesprochene Verfahrensschritt 3 des Anspruchs 1
dahingehend auszulegen, daß unter dem "nachfolgenden Block" der aus der
Menge der "möglichen" Blöcke von Kanalbits stammende gerade betrachtete
Block von Kanalbits zu verstehen ist. Die hierzu oben angeführten Stellen der ursprünglichen Unterlagen finden sich auch in der Patentschrift (dort S 6 Z 65 bis
S 7 Z 3 sowie Blöcke 9 und 10 des Flußdiagramms der Fig 3).


Die von der Klägerin behauptete Schwierigkeit, einen noch gar nicht festgelegten
Block für die (d, k)-Prüfung heranziehen zu müssen, besteht demnach bei der gebotenen fachmännischen Auslegung des Anspruchs 1 nicht.


3. Der Senat hat keinen Zweifel daran, daß das Verfahren nach Anspruch 1 gegenüber dem bisher bekannt gewordenen Stand der Technik patentfähig ist. Die
Klägerin hat hierzu nichts Gegenteiliges vorgetragen.


C. Zum Patentanspruch 11


Auch der Patentanspruch 11 ist rechtsbeständig. Ihm stehen weder absolute
Gründe nach § 21 Absatz 1 Nr 2 und 4 PatG, noch der Grund mangelnder Patentfähigkeit nach § 21 Absatz 1 Nr 1 entgegen.


1. Gegenstand des Patentanspruchs 11 ist ein Aufzeichnungsträger mit einer Informationsstruktur, die in der allgemeinsten, dh, nur auf Anspruch 1 rückbezogenen Fassung des Anspruchs 11 nach Anspruch 1 erzeugt sein soll und die weiteren im Anspruch 11 aufgeführten Merkmale haben soll. Dieser Anspruchsgegenstand muß unabhängig von seinem Herstellungsweg die Voraussetzung für die Patentierbarkeit erfüllen (BGH GRUR 93, 651 - Tetraploide Kamille sowie GRUR 79,
461 - Farbbildröhre).

                                      - 14 -



Die Rückbeziehung auf den Anspruch 1 ergibt für den Aufzeichnungsträger nach
Anspruch 11 insbesondere die Merkmale, daß die die Informationsstruktur bildenden aufgezeichneten Kanalbits die (d, k)-Bedingung erfüllen und daß sie blockweise gleichstromminimiert sind.


Die im Anspruch 11 aufgeführten Merkmale besagen ua, daß die Informationsstruktur Folgen von Kanalbitzellen aufweist, die je ein Bit enthalten, dessen Wert
durch einen Pegelübergang oder einen fehlenden Pegelübergang am Anfang der
Bitzelle dargestellt wird und daß der Abstand zwischen zwei aufeinanderfolgenden
Pegelübergängen maximal gleich (k + 1) Bitzellen und minimal gleich (d + 1) Bitzellen ist. Diese Merkmale stehen entgegen der Auffassung der Klägerin mit der
(d, k)-Bedingung nicht im Widerspruch.


Während nämlich bei der Definition der (d, k)-Bedingung im Anspruch 1 davon die
Rede ist, daß "zwei aufeinanderfolgende Kanalbits von einem ersten Typ, des
Typs "1", durch mindestens d dann höchstens k unmittelbar aufeinanderfolgende
Bits eines zweiten Typs, des Typs "0" getrennt werden", nimmt der Wortlaut des
Anspruchs 11 auf den "Abstand zwischen aufeinanderfolgenden Pegelübergängen" Bezug. Dieser Abstand ist aber, in Längen von Bitzellen ausgedrückt, jeweils
um 1 größer als die Anzahl der zwischen den zugeordneten aufeinanderfolgenden
Einsen liegenden Nullen, wie man ohne weiteres aus einem Vergleich der Wellenform WF mit dem Block BCi von Kanalbits in Figur 1 der Patentschrift entnimmt.


Es kommt somit im Anspruch 11 klar zum Ausdruck, was beansprucht wird. Es
handelt sich nicht, wie die Klägerin meint, lediglich um eine anspruchsähnlich formulierte Beschreibung, sondern um eine Anspruchsart, die auch in der Entscheidung "Farbbildröhre" (BGH GRUR 79, 461) vorlag und keine unabhängige zweite
Lösung, sondern eine zweite Ausprägung eines erfinderischen Gedankens betrifft.


2. Daß es sich bei einem Aufzeichnungsträger um einen technischen Gegenstand
handelt, dem anspruchsgemäß hinzutretende Merkmale die Technizität nicht neh-

                                      - 15 -



men können, steht für den Senat außer Frage (BGH GRUR 00, 1007
- Sprachanalyseeinrichtung).


Entgegen der Auffassung der Klägerin steht dem Anspruchsgegenstand auch
nicht der Ausschließungsgrund des § 1 Absatz 2 Nr 4 PatG iVm Absatz 3 (Wiedergabe von Informationen als solchen) entgegen.


Um eine bloße Wiedergabe von Informationen handelt es sich schon deshalb
nicht, weil der beanspruchte Aufzeichnungsträger mit der auf ihm aufgezeichneten
Informationsstruktur nicht dazu bestimmt ist, dem Menschen Informationsinhalte
direkt zu vermitteln, wie es zB bei Tabellen, Formularen, Schriftanord-nungen udgl
der Fall ist, die deswegen vom Patentschutz ausgeschlossen sind (Schulte PatG
6. Aufl § 1 Rdn 119). Vielmehr dient der Aufzeichnungsträger, wie für den Fachmann ohne weiteres klar ist, dazu, mit einer Wiedergabeeinrichtung zusammenzuwirken, die zur Abtastung und Verarbeitung der aufgezeichneten Bitfolgen ausgebildet ist.


Auch wenn man die von den Parteien erörterte, zu der gleichlautenden Bestimmung von Artikel 52 (2) (d) und (3) EPÜ ergangene Entscheidung "Datenstrukturprodukt/PHILIPS" des EPA (GRUR Int 2001, 167) betrachtet, ist festzustellen, daß
auch deren Grundsätze nicht dazu führen, im Anspruchsgegenstand eine Wiedergabe von Informationen im Sinne von § 1 Absatz 2 Nr 4 PatG zu erblicken.


Der vorliegend beanspruchte Aufzeichnungsträger ist nämlich nur durch die auf
ihm aufgezeichnete funktionelle Datenstruktur gekennzeichnet, die auf das System abgestimmt ist, in der der Aufzeichnungsträger zu verwenden ist, wohingegen
ein kognitiver Gehalt der aufgezeichneten Daten keine Rolle spielt.


Wie dazu im einzelnen der Patentschrift zu entnehmen ist, hat die Erfüllung der (d,
k)-Bedingung iVm dem Merkmal, wonach der Wert eines Bits durch einen
Pegelübergang oder einen fehlenden Pegelübergang am Anfang der Bitzelle dar-

                                       - 16 -



gestellt wird, den Sinn, einerseits die Taktung einer die Aufzeichnung abtastenden
Wiedergabeeinrichtung sicherzustellen und andererseits die Übergänge nicht zu
schnell aufeinanderfolgen zu lassen, um die Mindestbandbreite und die Intersymbolinterferenz möglichst gering zu halten (Patentschrift S 3 Z 36 bis 65). Die Minimierung des Gleichstromanteils soll die Zuverlässigkeit der Detektion der aufgezeichneten Signale verbessern (Patentschrift S 6 Z 56 bis 58), während die Synchronisationsinformation es der Wiedergabeeinrichtung ermöglichen soll, zwischen den Informationsbits und den Trennbits zu unterscheiden (Patentschrift S 8
Z 66 bis S 9 Z 5).


Die die Informationsstruktur beschreibenden Anspruchsmerkmale sind daher nach
Überzeugung des Senats technischer Natur.


3. Der Anspruch 11 geht auch nicht über den Inhalt der Anmeldung in der ursprünglich eingereichten Fassung hinaus. Sein Merkmalsinhalt ist für den Fachmann dem ursprünglichen Anspruch 12 iVm Teilen der übrigen ursprünglichen
Anmeldungsunterlagen als zur Erfindung gehörend entnehmbar.


Das von der Klägerin diesbezüglich aufgeführte Merkmal des ursprünglichen Anspruchs 12
"daß höchstens Folgen des doppelten maximalen Abstandes von (k+1) Bitzellen
auftreten und daß diese Folgen einen Teil einer Synchronisationsfolge bilden"
mag zwar mißverständlich formuliert sein. Die von der Klägerin vertretene Auslegung dieses Merkmals dahingehend, daß damit Folgen mit einem Abstand zwischen zwei aufeinanderfolgenden Pegelübergängen vom Doppelten des Abstandes von k + 1 Bitzellen gemeint seien, wird bereits dadurch ausgeschlossen, daß
dies die k-Bedingung verletzen würde, die gemäß dem ersten kennzeichnenden
Merkmal des ursprünglichen Anspruchs 12 aber eingehalten wird.


Aus Seite 17, Zeile 29 bis Seite 18, Zeile 25 der ursprünglichen Beschreibung und
der Darstellung des Blocks Synchronisationsbits in Figur 4 wird dagegen für den

                                      - 17 -



Fachmann klar, was mit dem fraglichen Merkmal gemeint ist: Zwei unmittelbar
aufeinanderfolgende, je die Länge von k + 1 Bitzellen aufweisende Abstände zwischen Pegelübergängen sind Teil einer Synchronisationsinformation, wobei das
unmittelbare Aufeinanderfolgen von drei derartigen Abständen vermieden wird.


Dieser aus den ursprünglichen Unterlagen entnehmbare Sachverhalt wird mit der
Formulierung des geltenden Anspruchs 11 "daß höchstens zwei aufeinanderfolgende maximale Abstände von (k + 1) Bitzellen der Pegelübergänge auftreten, die
Teil einer Synchronisationsinformation bilden" zutreffend beschrieben.


Die Klägerin sieht außerdem eine unzulässige Änderung des geltenden Anspruchs 11 darin, daß dieser im Unterschied zum ursprünglichen Anspruch 12, der
keine Rückbeziehung aufweist, auf einen der Ansprüche 1 bis 8 rückbezogen ist.
Aufgrund dieser Rückbeziehung sei eine Ausführung entstanden, die offensichtlich
fehlerhaft und durch die ursprünglichen Unterlagen nicht gedeckt sei.


Die Klägerin sieht wohl auch hier eine Diskrepanz zwischen der im Anspruch 1
aufgeführten (d, k)-Bedingung und dem oben schon erörterten Merkmal des Anspruchs 11, welches sich auf den Abstand zwischen zwei aufeinanderfolgenden
Pegelübergängen bezieht. Daß aber von einer Diskrepanz zwischen diesen
Merkmalen keine Rede sein kann, ist vorstehend unter Punkt 1 bereits dargelegt
worden.


4. Der Gegenstand des Anspruchs 11 ist in den Patentunterlagen auch so deutlich
und vollständig offenbart, daß ein Fachmann ihn ausführen kann.


Die Klägerin hat sich zu diesem Widerrufsgrund auf die von ihr gesehene Diskrepanz zwischen der im Anspruch 1 aufgeführten (d, k)-Bedingung und den im Anspruch 11 aufgeführten maximalen und minimalen Abständen zwischen
Pegelübergängen berufen. Diesbezüglich wird jedoch auf die Darlegungen unter
dem obigen Punkt 1 verwiesen.

                                        - 18 -




5. Für den Anspruch 11 ist auch die beanspruchte Priorität vom 14. Juli 1980 zugrunde zu legen.


Es kann dahinstehen, ob der von der Klägerin diesbezüglich angeführte Anspruch 2 der Voranmeldung die beanspruchte Priorität des Anspruchs 11 zu begründen vermag.


Wie unter dem vorstehenden Punkt 3 jedoch bereits dargelegt worden ist, war der
Merkmalsinhalt des Anspruchs 11 aus den ursprünglichen Anmeldungsunterlagen
für den Fachmann entnehmbar. Die dabei herangezogenen Teile der ursprünglichen Anmeldungsunterlagen sind inhaltlich gleichlautend auch in den Unterlagen
der Voranmeldung enthalten, nämlich dort auf Seite 22, Zeile 26 bis 35 und Seite 14, Zeile 37 bis Seite 15, Zeile 27 sowie Figur 4.


Der Gegenstand des Anspruchs 11 ist somit entgegen der Auffassung der Klägerin auch in den Unterlagen der Voranmeldung als zur Erfindung gehörend offenbart worden.


6. Der Senat hat keinen Zweifel daran, daß der Gegenstand des Anspruchs 11
gegenüber dem bisher bekannt gewordenen Stand der Technik patentfähig ist.


Die Klägerin hat zwar behauptet, der Gegenstand des Anspruchs 11 sei durch die
von ihr zitierte AES-Veröffentlichung neuheitsschädlich vorweggenommen. Da
diese Veröffentlichung jedoch ein Nachdruck eines für eine Tagung vom
31. Oktober bis 3. November 1980 bestimmten Manuskripts ist, bleibt sie in Anbetracht der für den Anspruch 11 geltenden Priorität vom 14. Juli 1980 für die Frage
der Patentfähigkeit außer Betracht.


D. Gegen die Patentansprüche 2 bis 10 und 12 bis 15 hat die Klägerin keine gesonderten, dh, unabhängig von den oben behandelten Angriffen auf die Ansprü-

                                    - 19 -



che 1 und 11 bestehenden Bedenken vorgetragen. Für den Senat ist nichts erkennbar, was den Rechtsbestand dieser Ansprüche in Frage stellen könnte.


E. Die Kostenentscheidung beruht auf § 84 Abs 2 PatG iVm § 91 Abs 1 Satz 1
ZPO, der Ausspruch zur vorläufigen Vollstreckbarkeit auf § 99 Abs 1 PatG iVm §
709 ZPO.




Dr. Schwendy        Obermayer          Kalkoff      Schuster      Dr. Hartung
                                                                           Wel
