---
ecli: "ECLI:DE:BPatG:2004:251004B20Wpat4.03.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 4/03"
decided: "2004-10-25"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2004&Sort=1&Seite=109&nr=19589&anz=2061&pos=1647&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2004-10-25_20_W-pat_4_03_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0034.md"]
---

# Bundespatentgericht, 20 W (pat) 4/03 vom 2004-10-25

## Entscheidung

BUNDESPATENTGERICHT


  20 W (pat) 4/03                                                  Verkündet am
 _______________                                                  25. Oktober 2004
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 101 12 816.9-31


…




hat der 20. Senat des Bundespatentgerichts auf die mündliche Verhandlung vom
25. Oktober 2004 durch den Vorsitzenden Richter Dipl.-Phys. Dr. Anders sowie
die Richter Hövelmann, Dipl.-Ing. Obermayer und Dipl.-Phys. Dr. Hartung


beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluß der Prüfungsstelle für Klasse H 04 L des Deutschen Patent- und Markenamts vom 22. August 2002 aufgehoben und das Patent erteilt.




BPatG 154
6.70

                                         -2-




      Bezeichnung:        Verfahren zum schnellen passiven Einmessen
                          von Transceivern auf ihr Übertragungsmedium


      Anmeldetag:         16. März 2001


      Der Erteilung liegen folgende Unterlagen zugrunde:


      Patentansprüche 1 bis 12,
      Beschreibung Spalten 1 bis 5 mit Einschub Blatt 1a,
      1 Blatt Zeichnungen Figuren 1 und 2,
      sämtlich   überreicht   in   der    mündlichen   Verhandlung   am
      25. Oktober 2004.


                                   Gründe


                                          I


Die Anmeldung wurde von der Prüfungsstelle zurückgewiesen, weil der Gegenstand des Anspruchs 1 gegenüber dem durch die Druckschrift


          (1)      US 5 673 290


belegten Stand der Technik nicht neu sei.


Folgende Entgegenhaltungen sind außerdem genannt:


          (2)      WO 99/18701 A1 und
          (3)      WO 00/67385 A1.


Die Anmelderin beantragt wie entschieden.

                                      -3-




Der Patentanspruch 1 lautet:


        "1. Verfahren zum Übertragen von Signalen mittels Transceivern
        auf einem Kanal, wie etwa auf Kupferkabeln, insbesondere auf
        Grundlage der xDSL-Übertragungstechnik, bei dem der Kanal vor
        der Nutzsignalübertragung eingemessen wird und aus dem Einmessungsergebnis Adaptionsparameter für die Nutzsignalübertragung gewonnen werden, dadurch gekennzeichnet, dass die
        Einmessung eine Störsignal-Messung im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen vorsieht, und dass die Adaptionsparameter aus den gemessenen Störsignalen auf Grundlage
        von A-Priori-Wissen über den Kanal und eines die Adaptionsparameter beschreibenden Adaptionsalgorithmus oder einer Abschätzung über Adaptionsparameter-Grenzwerte (Bounds) gewonnen werden."


Zum Wortlaut der sich dem Patentanspruch 1 anschließenden Ansprüche 2 bis 12
wird auf die in der mündlichen Verhandlung überreichten Unterlagen verwiesen.


Zur Begründung ihres Antrags führt die Anmelderin im wesentlichen aus, daß das
beanspruchte Verfahren des Anspruchs 1 gegenüber diesem Stand der Technik
neu und auch nicht nahegelegt sei. Insbesondere werde ein Übertragungs-Kanal
vor einer Nutzsignalübertragung eingemessen, indem die Einmessung eine Störsignal-Messung im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen vorsehe.

                                      -4-



                                       II


1. Die Ansprüche 1 bis 12 sind zulässig. Sie entsprechen den ursprünglich eingereichten Ansprüchen, ihre Merkmale sind in den ursprünglichen Unterlagen als zur
Erfindung gehörend offenbart.


2. Stand der Technik


Aus Druckschrift (1), vgl Figur 1, Zusammenfassung und die Ansprüche 11 bis 18
(Sp 11 Z 19 bis Sp 12 Z 35), ist ein Verfahren zum Übertragen von Signalen mittels Transceivern auf einem Kanal, wie etwa auf Kupferkabeln, insbesondere auf
Grundlage der xDSL-Übertragungstechnik, als bekannt entnehmbar. Übertragungskanäle (subchannels) werden eingemessen, und aus dem Einmessungsergebnis werden Adaptionsparameter für die Nutzsignalübertragung gewonnen
(Sp 11 Z 19-44). Die Einmessung sieht zumindest eine Störsignal-Messung vor
(Sp 11 Z 27-30, Sp 2 Z 44-48), zusätzlich können zu den Störsignalen auch
weitere Parameter, wie Dämpfung und Phasenverschiebungen, auf jedem der Kanäle bestimmt (überwacht) werden (Sp 8 Z 4-12). Aus den gemessenen Störsignalen werden Adaptionsparameter gewonnen (Sp 11 Z 37-40) auf Grundlage
von A-Priori-Wissen über den Kanal oder einer Abschätzung über Adaptionsparameter-Grenzwerte (vgl insbesondere Angaben zu Bandbreiten und Übertragungskapazitäten in Abhängigkeit von Übertragungsentfernungen, Sp 12 Z 21-
35 iVm Sp 1 Z 62 bis Sp 2 Z 14, Sp 4 Z 6-67, zu Grenzwerten die Fig 2, 3, 4 und
7). Das bekannte Verfahren ist außerdem geeignet, Realzeit-Änderungen von
Übertragungsparametern zu erkennen und Adaptionsparameter dynamisch
anzupassen (Sp 11 Z 40-44, Sp 8 Z 12-24, Sp 2 Z 52-56). Der Verfahrensschritt
zur Bestimmung von mindestens einem Qualitätsparameter, der das Störsignal-Niveau anzeigt, durch Überwachung (Messung) eines aus einer Mehrzahl von
Übertragungskanälen (Sp 11 Z 27-30) erfolgt gemäß der in Anspruch 11
angegebenen Abfolge von Schritten vor allen anderen Schritten (Sp 11 Z 31 bis
Sp 12 Z 3), insbesondere vor einer Übertragung der Daten (Sp 12 Z 1-3). Eine

                                       -5-



definitive   Aussage   dazu,   daß   die   Einmessung    eines   Kanals     vor   der
Nutzsignalübertragung erfolgt, insbesondere im Offline-Betrieb bei deaktivierten
Transceiver-Sendeteilen, ist aus (1) nicht entnehmbar.


Aus Druckschrift (2) ist ein Verfahren mit den Merkmalen im Oberbegriff des Anspruchs 1 als bekannt entnehmbar, vgl die Figuren 1 und 2, die Zusammenfassung und den Wortlaut der Ansprüche. Der Kanal wird vor der Nutzsignalübertragung eingemessen mittels Modem 54 und DSP-Techniken (S 13 Z 31 bis S 14
Z 7, S 14 Z 35 bis S 15 Z 14). Insbesondere steuert Modem 54 den Neustart der
Datenübertragung nach einem Fehlerfall und gewinnt aus dem Einmessungsergebnis Adaptionsparameter für die Nutzsignalübertragung. Die Adaptionsparameter, wie zB Sendeleistung, Datenrate, werden Hard- oder Software-gesteuert
angepaßt (vgl Fig 3 und 5 und S 16 Z 26 bis S 24 Z 37, auch Ansprüche 5 bis 12,
S 27-28). Die Adaptionsparameter werden jedoch nicht aus gemessenen Störsignalen gewonnen, insbesondere sieht die Einmessung nach (2) keine Störsignal-Messung im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen vor.


Entgegenhaltung (3) geht nicht über den Inhalt der Druckschrift (2) hinaus und hat
im Beschwerdeverfahren keine Rolle gespielt. Sie bringt auch hinsichtlich der Beurteilung der erfinderischen Tätigkeit keine neuen Gesichtspunkte.


3. Neuheit


Der - zweifelsfrei gewerblich anwendbare - Gegenstand des Patentanspruchs 1 ist
neu, denn keine der Entgegenhaltungen zeigt, wie sich aus den vorstehenden
Ausführungen ergibt, alle seine Merkmale.


4. Erfinderische Tätigkeit


Es mag sein, daß der hier zuständige Fachmann, ein Physiker oder Hochschul-Ingenieur der Fachrichtung Nachrichtentechnik mit mehrjähriger Berufserfahrung in

                                       -6-



der Entwicklung von Verfahren zum Übertragen von Signalen mittels Transceivern
auf einem Kanal, wie etwa auf Kupferkabeln, insbesondere auf Grundlage der
xDSL-Übertragungstechnik, ausgehend von der ihm aus Druckschrift (2) geläufigen Einmessung von Übertragungskanälen vor einer Nutzsignalübertragung, in
Betracht zieht, das aus (2) bekannte Verfahren vor allem hinsichtlich der Einmessung des Kanals und der aus dem Einmessungsergebnis gewonnen Adaptionsparameter zu verbessern.


Das aus der Druckschrift (1) als bekannt entnehmbare Verfahren zum Übertragen
von Signalen mittels Transceivern auf einem Kanal zeigt dem Fachmann auf, daß
zur Gewinnung von Adaptionsparametern gemessene Störsignale hinreichen mögen (Sp 11 Z 27-28). Zwar können gemäß (1) auch weitere, die Qualität der Datenübertragung kennzeichnende Parameter, wie Dämpfung oder Phasenverschiebung, überprüft werden (Sp 8 Z 4-10), nach (1) reicht es aber zur Gewinnung von
Adaptionsparametern aus, daß mindestens ein Parameter, der die Größe der
Störsignale kennzeichnet, überprüft - gemessen – wird, um aus den gemessenen
Störsignalen Adaptionsparameter auf Grundlage von A-Priori-Wissen über den
Kanal oder einer Abschätzung über Adaptionsparameter-Grenzwerte zu gewinnen
(Sp 11 Z 27-44). Einen die Adaptionsparameter beschreibenden Adaptionsalgorithmus setzt der Fachmann bei der Gewinnung der Adaptionsparameter auf
Grundlage von A-Priori-Wissen über den Kanal voraus, auch wenn ein solcher
nicht expressiv verbis in den den Stand der Technik belegenden Druckschriften
aufgeführt ist. Auch mag der Fachmann das in (1) beschriebene Verfahren für ein
Einmessen vor der Nutzsignalübertragung in Anschlag bringen, ein solches Einmessen des Kanals vor der Nutzsignalübertragung ist dem Fachmann aus (2) geläufig.


Keine der Druckschriften vermittelt dem Fachmann jedoch eine Anregung dahingehend, daß die Einmessung eine Störsignal-Messung im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen vorsieht. Zwar ist bei dem aus (1) als bekannt
entnehmbaren Verfahren die Störsignal-Messung dem ersten Verfahrensschritt in

                                       -7-



einer Reihe von weiteren zugeordnet (Sp 11 Z 27-30), insbesondere vor dem
letzten Schritt der eigentlichen Nutzsignalübertragung (Sp 12 Z 1-3). Jedoch erzeigt sich das in (1) geschilderte Verfahren durchgängig als geeignet für ein dynamisches Updaten der Adaptionsparameter während einer Datenübertragung,
also im Online-Betrieb bei aktivierten Transceiver-Sendeteilen (Sp 11 Z 36-44; Sp
8 Z 18-24). Folgt der Fachmann, ausgehend von einem Verfahren nach Druckschrift (2), dem in (1) beschriebenen Verfahrensablauf, dann mag er wohl ein
Einmessen des Kanals vor der Nutzsignalübertragung vorsehen, jedoch bei aktivierten Transceiver-Sendeteilen, nachdem ein dynamisches Updaten der Adaptionsparameter ohnehin während einer Datenübertragung, im Online-Betrieb bei
aktivierten Transceiver-Sendeteilen erfolgt. Eine Einmessung mittels einer Störsignal-Messung im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen zieht
der Fachmann dagegen nicht in Betracht. Dafür spricht auch, daß nach (1) durchgängig eine Störsignal-Messung iVm Messungen weiterer Parameter und ein dynamisches Updaten von Adaptionsparametern bei einer Mehrzahl von (Sub-) Kanälen erfolgt. Außerdem wird bei der Kanalüberwachung die Ermittlung des zumindest einen Adaptionsparameters, der die Störsignalpegel umfaßt, für jeden
Kanal gesondert durchgeführt (at each of a multiplicity of subchannels). Dieser
Kanal ist sendeseitig durch Modulation einer bestimmten Hilfsträgerfrequenz zugeordnet. Die empfangsseitige Demodulation verlangt demnach eine aktive Sendeeinheit (Sp 11 Z 29-30 und Z 40-44; Sp 2 Z 44-56; Sp 8 Z 7-24). Letztendlich ist
auch aus dem allgemeinen Fachwissen heraus keine Veranlassung ersichtlich, die
den Fachmann eine Einmessung eines Kanals mittels einer Störsignal-Messung
im Offline-Betrieb bei deaktivierten Transceiver-Sendeteilen nahelegen könnte.


5. Die Patentansprüche 2 bis 12 betreffen über das Selbstverständliche hinausgehende Ausgestaltungen des Gegenstandes des Patentanspruchs 1 und sind daher
ebenfalls gewährbar.

                                    -8-



6. Die Anmeldung genügt den Anforderungen des § 34 PatG.




Dr. Anders             Hövelmann          Obermayer        Dr. Hartung


                                                                   Pr
