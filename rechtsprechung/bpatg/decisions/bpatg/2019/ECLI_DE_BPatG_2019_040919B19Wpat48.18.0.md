---
ecli: "ECLI:DE:BPatG:2019:040919B19Wpat48.18.0"
court: "Bundespatentgericht"
spruchkoerper: "19"
aktenzeichen: "19 W (pat) 48/18"
decided: "2019-09-04"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=37&nr=36677&anz=817&pos=567&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2019-09-04_19_W-pat_48_18_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0073.md", "germany/bund/acts/patg/0079.md", "germany/bund/acts/patg/0100.md", "germany/bund/acts/patg/0101.md", "germany/bund/acts/patg/0102.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/patkostg/0006.md"]
---

# Bundespatentgericht, 19 W (pat) 48/18 vom 2019-09-04

## Entscheidung

BUNDESPATENTGERICHT


 19 W (pat) 48/18                                                       Verkündet am
_______________                                                      4. September 2019
    (Aktenzeichen)                                                           …




                              BESCHLUSS

                            In der Beschwerdesache


                 betreffend die Patentanmeldung 100 38 570.2


…




hat der 19. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 4. September 2019 unter Mitwirkung des
Vorsitzenden Richters Dipl.-Ing. Kleinschmidt, des Richters Dipl.-Ing. J. Müller, der
Richterin Werner sowie des Richters Dipl.-Phys. Dr. Haupt




ECLI:DE:BPatG:2019:040919B19Wpat48.18.0

                                     -2-



beschlossen:


        Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse H 02 P des Deutschen Patent- und Markenamts vom 11. September 2018 aufgehoben und die Sache an das
        Deutsche Patent- und Markenamt zurückverwiesen.




                                   Gründe


                                      I.


Die Patentanmeldung 100 38 570.2 mit der Bezeichnung „Stromregelung im Stator
einer elektrischen Maschine“ ist am 3. August 2000 beim Deutschen Patent- und
Markenamt unter Inanspruchnahme der Priorität der früheren deutschen Anmeldung 100 26 775.0 vom 31. Mai 2000 eingereicht worden.


Das Deutsche Patent- und Markenamt – Prüfungsstelle für Klasse H 02 P – hat
die Anmeldung mit Beschluss vom 11. September 2018 zurückgewiesen, mit der
Begründung, der Gegenstand des Patentanspruchs 1 beruhe nicht auf einer erfinderischen Tätigkeit.


Gegen diesen Beschluss richtet sich die Beschwerde der Anmelderin vom
11. Oktober 2018. Sie beantragt,


        den Beschluss der Prüfungsstelle für Klasse H 02 P des Deutschen Patent- und Markenamts vom 11. September 2018 aufzuheben und das nachgesuchte Patent aufgrund folgender Unterlagen zu erteilen:

                                        -3-



          Patentanspruch 1, überreicht in der mündlichen Verhandlung
          am 4. September 2019,
          Patentansprüche 2 bis 10, eingereicht mit Schriftsatz vom
          17. Juni 2014,
          noch anzupassende Beschreibung und Zeichnungen.


Der geltende Patentanspruch 1 lautet:


       Stromregelkreis der Statorwicklung einer elektrischen Maschine,
       mit einem mit Stromsoll- und Stromistwerten (isq_ref, isq) gespeisten Soll-/Istwert-Vergleichsglied (5) und einem diesem nachgeschalteten PI-Regler (6), wobei der Stromregelkreis auf der Basis eines Abtastglieds (4) für den Stator-Istwert (isq) zeitdiskret arbeitet, und ferner mit einer Einrichtung (23) zur Stromprädiktion
       mit wenigstens Reglerausgangswerten (usq_ref) und Stromistwerten (isq,isd) als Eingangsgrößen und einer Stromistwertänderung (∆pred_isq) als resultierende Ausgangsgröße, wobei die Prädiktionseinrichtung (23) intern ein oder mehrere Rechenglieder (26, 27) aufweist, die Prädiktionseinrichtung (23) ein eingangseitiges Summierglied (24) aufweist, dem am ersten Eingang der
       Reglerausgangswert (usq_ref) zugeführt wird, und am zweiten
       Eingang ein Vorsteuer-Ausgangswert (USQ_EMK) zur Verfügung
       gestellt wird, wobei dem eingangsseitigen Summierglied (24) der
       Stromprädiktionseinrichtung (23) ein Totzeitglied (25) unmittelbar
       nachgeschaltet ist, dessen Zeitkonstante mit dem Abtastzeitintervall (Tab) des Abtastglieds (4) übereinstimmt, wobei das Ergebnis
       einer im Summierglied stattfindenden Subtraktion des Vorsteuer-Ausgangswerts (USQ_EMK) vom Regler-Ausgangswert (usq_ref)
       um ein Abtastzeitintervall (Tab) verzögert einem weiteren, unmittelbar am Ausgang des Totzeitglieds (25) mit seinem ersten Eingang anliegenden Summierglied (26) zugeführt und am zweiten

                                                             -4-



       Eingang des weiteren Summierglieds (26) das Ergebnis mathematischer Beziehung über Ständer-Parameter und -Ströme gemäß den Gleichungen
                                     𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑
       𝑢𝑢𝑢𝑢𝑢𝑢 = 𝑟𝑟𝑠𝑠 𝑖𝑖𝑖𝑖𝑖𝑖 + 𝑙𝑙𝑠𝑠            + 𝑢𝑢𝑢𝑢𝑢𝑢_𝑒𝑒𝑒𝑒𝑒𝑒 − 𝑙𝑙𝑠𝑠 𝜔𝜔𝜔𝜔𝜔𝜔𝜔𝜔
                                       𝑑𝑑𝑑𝑑
       und
       𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝_𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1)
                              = {𝑢𝑢𝑢𝑢𝑢𝑢_𝑟𝑟𝑟𝑟𝑟𝑟(𝑘𝑘)
                              − [𝑟𝑟𝑠𝑠 𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1) + 𝑢𝑢𝑢𝑢𝑢𝑢_𝑒𝑒𝑒𝑒𝑒𝑒(𝑘𝑘 + 1)
                                                             𝑇𝑇𝑎𝑎𝑎𝑎
                              − 𝑙𝑙𝑠𝑠 𝜔𝜔𝜔𝜔𝜔𝜔𝜔𝜔(𝑘𝑘 + 1)]}             + 𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1)
                                                              𝑙𝑙𝑠𝑠
       zugeleitet wird, wobei der Ausgang des weiteren Summierglieds (26) einem Proportionalglied (27) zugeführt wird, welches
       eine Verknüpfung mit dem Abtastintervall (Tab) und einer Statorinduktivität bewirkt, wobei dann am Ausgang der Stromprädiktionseinrichtung (23)                       die        prädiktive          Stromistwertänderung
       (∆pred_isq) als Ausgangsgröße resultiert, wobei die resultierende
       Ausgangsgröße über ein am Ausgang der Prädiktionseinrichtung (23) liegendes Summierglied (28) mit dem Stromistwert (isq)
       summiert dem Vergleichsglied (5) als prädiktiver Stromistwert
       (pred_isq) zugeführt ist.


Zum Wortlaut der auf den Patentanspruch 1 rückbezogenen Patentansprüche sowie zu weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                                                               II.


1.    Die Beschwerde der Anmelderin ist statthaft und auch im Übrigen zulässig
(§ 73 Abs. 1 und Abs. 2 Satz 1 PatG, § 6 Abs. 1 Satz 1 PatKostG). Sie hat insoweit Erfolg, als sie zur Aufhebung des angefochtenen Beschlusses und zur

                                         -5-



Zurückverweisung zur weiteren Behandlung – auf der Grundlage des in der mündlichen Verhandlung am 4. September 2019 überreichten Patentanspruchs 1 – an
das Deutsche Patent- und Markenamt gemäß § 79 Abs. 3 Satz 1 Nummer 1 und 2
PatG führt.


2.       Die Anmeldung betrifft die Regelung des Statorstromes einer elektrischen
Maschine. Da bei diesen Maschinen das Drehmoment unmittelbar von den jeweiligen Statorströmen abhängt, zielt die Anmeldung letztlich auf die Regelung des
Drehmoments und damit indirekt auch auf die Regelung der Drehzahl.


Für viele Anwendungen ist von wesentlicher Bedeutung, dass ein vorgebbares
Drehmoment und/oder die Drehzahl zum einen innerhalb möglichst kurzer Zeit
erreicht wird und zum anderen dann möglichst stabil bleibt.


Als Aufgabe ist angegeben, vor allem im Bereich der Servoantriebe sollen
schnelle bzw. hochdynamische und gleichzeitig stabile sowie präzise arbeitende
Regelkreise geschaffen werden, bei denen der Anstieg des Statorstromes maximal sein kann. Gegebenenfalls solle auch ein Überschwingen eingedämmt oder
vermieden sein (Seite 3, Zeilen 9 bis 13 der Beschreibung zum Hauptantrag vom
4. März 2016).


Diese Aufgabe werde durch einen Stromregelkreis mit den im geltenden Patentanspruch 1 genannten Merkmalen gelöst.


3.       Der Patentanspruch 1 lautet unter Einfügung einer Gliederung:


     a      Stromregelkreis der Statorwicklung einer elektrischen Maschine, mit
     b      einem mit Stromsoll- und Stromistwerten (isq_ref, isq) gespeisten Soll-/Istwert-Vergleichsglied (5) und
     c      einem diesem nachgeschalteten PI-Regler (6),

                                      -6-



d     wobei der Stromregelkreis auf der Basis eines Abtastglieds (4)
      für den Stator-Istwert (isq) zeitdiskret arbeitet, und
e0    ferner mit einer Einrichtung (23) zur Stromprädiktion mit
e1    wenigstens Reglerausgangswerten (usq_ref) und
e2    Stromistwerten (isq,isd)
e3    als Eingangsgrößen und
e4    einer Stromistwertänderung (∆pred_isq)
      als resultierende Ausgangsgröße,
f     wobei die Prädiktionseinrichtung (23) intern ein oder mehrere
      Rechenglieder (26, 27) aufweist,
f1    die Prädiktionseinrichtung (23) ein eingangseitiges Summierglied (24) aufweist,
f11   dem am ersten Eingang der Reglerausgangswert (usq_ref)
      zugeführt wird,
f12   und     am    zweiten   Eingang       ein   Vorsteuer-Ausgangswert
      (USQ_EMK) zur Verfügung gestellt wird,
f2    wobei        dem   eingangseitigen          Summierglied (24)   der
      Stromprädiktionseinrichtung (23) ein Totzeitglied (25) unmittelbar nachgeschaltet ist,
f21   dessen Zeitkonstante mit dem Abtastzeitintervall (Tab) des Abtastglieds (4) übereinstimmt,
f3    wobei das Ergebnis einer im Summierglied stattfindenden Subtraktion des Vorsteuer-Ausgangswerts (USQ_EMK) vom Regler-Ausgangswert (usq_ref)
f31   um ein Abtastzeitintervall (Tab) verzögert
f32   einem weiteren, unmittelbar am Ausgang des Totzeitglieds (25)
      mit seinem ersten Eingang anliegenden Summierglied (26) zugeführt
f4    und am zweiten Eingang des weiteren Summierglieds (26) das
      Ergebnis mathematischer Beziehung über Ständer-Parameter
      und -Ströme zugeleitet wird, gemäß den Gleichungen

                                                          -7-



                                     𝑑𝑑𝑑𝑑𝑑𝑑𝑑𝑑
      f41   𝑢𝑢𝑢𝑢𝑢𝑢 = 𝑟𝑟𝑠𝑠 𝑖𝑖𝑖𝑖𝑖𝑖 + 𝑙𝑙𝑠𝑠 𝑑𝑑𝑑𝑑 + 𝑢𝑢𝑢𝑢𝑢𝑢_𝑒𝑒𝑒𝑒𝑒𝑒 − 𝑙𝑙𝑠𝑠 𝜔𝜔𝜔𝜔𝜔𝜔𝜔𝜔

            und
      f42   𝑝𝑝𝑝𝑝𝑝𝑝𝑝𝑝_𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1) = {𝑢𝑢𝑢𝑢𝑢𝑢_𝑟𝑟𝑟𝑟𝑟𝑟(𝑘𝑘) − [𝑟𝑟𝑠𝑠 𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1) + 𝑢𝑢𝑢𝑢𝑢𝑢_𝑒𝑒𝑒𝑒𝑒𝑒(𝑘𝑘 +
                                                𝑇𝑇
            1) − 𝑙𝑙𝑠𝑠 𝜔𝜔𝜔𝜔𝜔𝜔𝜔𝜔(𝑘𝑘 + 1)]} 𝑙𝑙𝑎𝑎𝑎𝑎 + 𝑖𝑖𝑖𝑖𝑖𝑖(𝑘𝑘 + 1)
                                                     𝑠𝑠

            zugeleitet wird,
      f5    wobei der Ausgang des weiteren Summierglieds (26) einem
            Proportionalglied (27) zugeführt wird,
      f51   welches eine Verknüpfung mit dem Abtastintervall (Tab) und einer Statorinduktivität bewirkt,
      f6    wobei dann am Ausgang der Stromprädiktionseinrichtung (23)
            die prädiktive Stromistwertänderung (∆pred_isq) als Ausgangsgröße resultiert,
      g11   wobei die resultierende Ausgangsgröße
      g2    über ein am Ausgang der Prädiktionseinrichtung (23) liegendes
            Summierglied (28) mit dem Strom-Istwert (isq) summiert
      g12   dem Vergleichsglied (5) als prädiktiver Strom-Istwert (pred_isq)
            zugeführt ist.


3.     Als Fachmann geht der Senat von einem Diplom-Ingenieur bzw. Master der
Fachrichtung Elektrotechnik aus, der theoretische Betrachtungen über die Regelung elektrischer Maschinen anstellt und dazu befähigt ist.


Dazu verfügt der Fachmann insbesondere über fundierte Kenntnisse sowohl über
den Aufbau elektrischer Maschinen als auch über die Theorien der Regelungstechnik, wie die Raumzeigerdarstellung sowie deren Anwendung, insbesondere
bei der zeitdiskreten Vektorregelung von Drehfeldmaschinen.


4.1    In der Regelungstechnik werden mathematische Modelle entwickelt, durch
die sich Regelungsvorgänge möglichst wirklichkeitsgetreu beschreiben lassen.
Sowohl das zu regelnde Gerät als auch die Regelvorrichtung werden dabei derart

                                       -8-



auf ihr Verhalten reduziert, dass unabhängig davon, was geregelt wird, immer dieselben mathematischen Modelle zur Anwendung kommen können.


4.2   Im streitgegenständlichen Fall einer rotierenden elektrischen Maschine wird
außerdem die Raumzeigertheorie zu Hilfe genommen, die ein mathematisches
Hilfsmittel zur Beschreibung von drei-Größen-Systemen mit sinusförmiger Periodizität mittels Transformation auf zwei voneinander unabhängige Größen darstellt
und sich daher unter bestimmen Voraussetzungen zur Modellierung und Regelung
der dynamischen Vorgänge von Drehstromantrieben eignet.


4.3   Mittels einer Einrichtung zur Stromprädiktion soll es möglich sein, die
Stromänderung im jeweils nächsten Regelungsintervall vorherzubestimmen (ursprüngliche Beschreibung, Seite 13, Zeilen 15 bis 21). Dazu weist die Prädiktionseinrichtung ein oder mehrere Rechenglieder auf. Da die Regelungstechnik ohnehin mit mathematischen Modellen arbeitet, die es ermöglichen, losgelöst von einer
bestimmten Anwendung zu rechnen, vermutet der Fachmann hinter diesen Rechengliedern Programmblöcke, mittels denen geeignete Algorithmen abgearbeitet
werden, wobei jedoch auch eine Realisierung mittels konkreter Schaltungen erfolgen kann.


5.    Die Merkmale a bis f des geltenden Patentanspruchs 1 gehen auf die ursprünglichen Patentansprüche 15 sowie 16 zurück. Die Merkmale f1 bis g12 finden
ihre Stütze in der ursprünglichen Beschreibung in der Figurenbeschreibung zur
Figur 7 auf Seite 14, Zeilen 8 bis 30 i. V. m. den Gleichungen (4) und (5) auf
Seite 13, Zeilen 17 und 25.


Somit geht der geltende Patentanspruch 1 nicht über den Inhalt der Anmeldung
hinaus, in der diese beim Deutschen Patent- und Markenamt ursprünglich eingereicht worden ist. Daher ist der Patentanspruch 1 zulässig.

                                            -9-



6.        Im bisherigen Verfahren vor dem Deutschen Patent- und Markenamt ist bislang auf folgende Druckschriften Bezug genommen worden:


      D1     BROSCH, Peter; FRIEDRICH, Hartmut; KIRSTE, Hans-H.;
             SCHRÖDER, Herbert: Strom und Spannung, wie gewünscht. In:
             elektronikpraxis, Nr. 5, Mai 1984, Seiten 150 bis155
      D2     LUTZ, Holger; WENDT, Wolfgang: Taschenbuch der Regelungstechnik, 2. Auflage Verlag Harri Deutsch, Frankfurt am Main, 1998,
             Seiten 418 bis 426
      D3     DE 41 29 261 C1
      D4     DE 43 10 778 C2


Der in diesen Druckschriften wiedergegebene Stand der Technik steht der Gewährbarkeit des geltenden Patentanspruchs 1 nicht entgegen:


Wie schon von der Prüfungsstelle zutreffend ausgeführt, offenbart die Druckschrift
DE 43 10 778 C2 (D4) hinsichtlich des Gegenstandes des Patentanspruchs 1 einen


      a      Stromregelkreis der Statorwicklung einer elektrischen Maschine
             (Titel, Patentanspruch 1), mit
      b      einem mit Strom-Soll- und Strom-Istwerten iw(k), 𝚤𝚤̂(k+1) gespeisten Soll-/Istwert-Vergleichsglied (Figur 1) und
      c                                              � P, K
             einem diesem nachgeschalteten PI-Regler K    � I (Seite 4,
             Zeile 54),
      d      wobei der Stromregelkreis auf der Basis eines Abtastglieds für
             den Stator-Istwert i(k) zeitdiskret arbeitet (Seite 2, Zeile 6), und
      e0     ferner mit einer Einrichtung zur Stromprädiktion (Seite 5, Zeilen 4 bis 6) mit
      e1     wenigstens Reglerausgangswerten 𝑢𝑢�(k), 𝑢𝑢�(k-1) und
      e2     Strom-Istwerten i(k)

                                          - 10 -



      e3     als Eingangsgrößen und
      e4     einer Strom-Istwertänderung 𝚤𝚤̂(k+1)
             als resultierende Ausgangsgröße,
      f      wobei die Prädiktionseinrichtung ein oder mehrere Rechenglieder aufweist (Seite 15, Zeilen 37 bis 49),


Zu Einzelheiten der Prädiktionseinrichtung wird in der Druckschrift D4 auf die
Druckschrift DE 41 29 261 C1 (D3) verwiesen (Seite 5, Zeilen 4 bis 6).


Gemäß Druckschrift D3 weist die Prädiktionseinrichtung ein Summierglied auf,
dem


      f11     ein Reglerausgangswert iN(k) sowie
      f12    ein Vorsteuerausgangswert ∆UST(k) zur Verfügung gestellt wird
             (Seite 4, Zeilen 20 bis 27 und Seite 4, Zeile 65 bis Seite 5,
             Zeile 3).


Jedoch sind weder der Druckschrift D3 noch der Druckschrift D4 weitere Einzelheiten zu entnehmen, wie die Eingangsgrößen der Prädiktionseinrichtung verarbeitet werden, so dass sich zumindest die Vorgehensweise entsprechend den
Merkmalen f2 bis f6 nicht in naheliegender Weise aus der Zusammenschau dieser
beiden Druckschriften ergibt.


Da die Möglichkeit einer Stromprädiktion in den Druckschriften D1 sowie D2 nicht
thematisiert wird, konnte der Fachmann diesen ebenfalls keine Anregung entnehmen, die zum Gegenstand des geltenden Patentanspruchs 1 geführt hätten.


7.        Das Verfahren ist jedoch noch nicht zur Entscheidung reif, die Anmeldung
wird deshalb mit dem in der mündlichen Verhandlung übergebenen Patentanspruch 1 zur weiteren Prüfung an das Patentamt zurückverwiesen. § 79 Abs. 3
Satz 1 PatG bestimmt, dass das Patentgericht die angefochtene Entscheidung

                                      - 11 -



aufheben kann, ohne in der Sache selbst abschließend zu entscheiden. Eine Zurückverweisung kommt insbesondere dann in Betracht, wenn die Gründe, die der
angefochtenen Entscheidung zugrunde liegen, nicht mehr bestehen, aber eine
neue Sachprüfung erforderlich ist, weil die Patentfähigkeit noch nicht oder nicht
ausreichend Gegenstand der Prüfung war (§ 79 Abs. 3 Satz 1 Nr. 1 und 3 PatG,
vgl. Busse PatG, 8. Aufl., § 79 Rdn. 89; Schulte PatG, 10. Auflage, § 79 Rdn. 26).


Dies ist vorliegend der Fall. Aus der Akte ist nämlich nicht ersichtlich, dass die
Prüfungsstelle des Deutschen Patent- und Markenamtes sich inhaltlich mit dem
lediglich im Ausführungsbeispiel gemäß Figur 7 gezeigten und in der zugehörigen
Beschreibung erwähnten Aufbau und der Funktionsweise der Prädiktionseinrichtung auseinandergesetzt und dazu recherchiert hätte. Daher hat der Senat von
einer abschließenden Entscheidung abgesehen, zumal nicht auszuschließen ist,
dass sich bei einer ergänzenden Recherche herausstellt, dass es sich bei den zusätzlich in den Patentanspruch 1 aus der Beschreibung aufgenommenen Merkmalen um eine Vorgehensweise handelt, die dem Fachmann an sich vertraut ist.


Der Senat hat außerdem davon Abstand genommen, auf eine Überarbeitung und
Vorlage der Beschreibung und der Zeichnungen hinzuwirken, da noch nicht abschließend über die Gewährbarkeit der Patentansprüche entschieden werden
konnte. Es obliegt vielmehr der Prüfungsstelle, im Rahmen der weiteren Prüfung
darauf zu achten, dass die Unterlagen im Falle der Patenterteilung alle Erfordernisse des Patentgesetzes und der Patentverordnung erfüllen; insoweit wird die
Prüfungsstelle dann auf eine Überarbeitung der Beschreibung sowie der Zeichnungen hinzuwirken haben, falls sie eine Patenterteilung in Aussicht stellen kann.
Dabei kann dann auch die Klarstellung bezüglich der mit der Figur 10 identischen
Figur 11, deren Inhalt offensichtlich nicht mit der Beschreibung übereinstimmt, erfolgen.

                                          - 12 -



                                 Rechtsmittelbelehrung


Gegen diesen Beschluss steht den an dem Beschwerdeverfahren Beteiligten das
Rechtsmittel der Rechtsbeschwerde zu (§ 99 Abs. 2, § 100 Abs. 1, § 101 Abs. 1 PatG).


Nachdem der Beschwerdesenat in dem Beschluss die Einlegung der Rechtsbeschwerde
nicht zugelassen hat, ist die Rechtsbeschwerde nur statthaft, wenn einer der
nachfolgenden Verfahrensmängel durch substanziierten Vortrag gerügt wird (§ 100 Abs. 3
PatG):


     1.    Das beschließende Gericht war nicht vorschriftsmäßig besetzt.
     2.    Bei dem Beschluss hat ein Richter mitgewirkt, der von der Ausübung
           des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis
           der Befangenheit mit Erfolg abgelehnt war.
     3.    Einem Beteiligten war das rechtliche Gehör versagt.
     4.    Ein Beteiligter war im Verfahren nicht nach Vorschrift des Gesetzes
           vertreten, sofern er nicht der Führung des Verfahrens ausdrücklich oder
           stillschweigend zugestimmt hat.
     5.    Der Beschluss ist aufgrund einer mündlichen Verhandlung ergangen, bei
           der die Vorschriften über die Öffentlichkeit des Verfahrens verletzt
           worden sind.
     6.    Der Beschluss ist nicht mit Gründen versehen.


Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe, schriftlich einzulegen (§ 102
Abs. 1 PatG).


Die Rechtsbeschwerde kann auch als elektronisches Dokument, das mit einer
qualifizierten oder fortgeschrittenen elektronischen Signatur zu versehen ist, durch
Übertragung in die elektronische Poststelle des Bundesgerichtshofes eingelegt werden
(§ 125a Abs. 3 Nr. 1 PatG i. V. m. § 1, § 2 Abs. 1 Satz 1, Abs. 2, Abs. 2a, Anlage (zu § 1)
Nr. 6 der Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof
und Bundespatentgericht (BGH/BPatGERVV)). Die elektronische Poststelle ist über die
auf der Internetseite des Bundesgerichtshofes www.bundesgerichtshof.de/erv.html

                                      - 13 -



bezeichneten    Kommunikationswege    erreichbar   (§ 2   Abs. 1   Satz 2   Nr. 1
BGH/BPatGERVV). Dort sind auch die Einzelheiten zu den Betriebsvoraussetzungen
bekanntgegeben (§ 3 BGH/BPatGERVV).


Die Rechtsbeschwerde muss durch einen beim Bundesgerichtshof zugelassenen
Rechtsanwalt als Bevollmächtigten des Rechtsbeschwerdeführers eingelegt werden
(§ 102 Abs. 5 Satz 1 PatG).




Kleinschmidt              J. Müller            Werner                 Dr. Haupt


                                                                              Pr
