---
ecli: "ECLI:DE:BPatG:2021:061221U4Ni9.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "4"
aktenzeichen: "4 Ni 9/21"
decided: "2021-12-06"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=37&nr=42398&anz=599&pos=559&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2021-12-06_4_Ni_9_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 4 Ni 9/21 vom 2021-12-06

## Entscheidung

BUNDESPATENTGERICHT

                           IM NAMEN DES VOLKES

                                      URTEIL


                                                             Verkündet am
                                                          6. Dezember 2021
        4 Ni 9/21 (EP)
       (Aktenzeichen)                                            …




                         In der Patentnichtigkeitssache


…




ECLI:DE:BPatG:2021:061221U4Ni9.21EP.0

                                        -2-




              betreffend das europäische Patent EP 1 509 903
                                (DE 603 50 108)


hat der 4. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 6. Dezember 2021 durch die Vorsitzende
Richterin Grote-Bittner sowie die Richter Dipl.-Phys. Univ. Dipl.-Wirt.-Phys.
Arnoldi, Dipl.-Ing. Matter, Dr. Söchtig und Dipl.-Phys. Univ. Dr. Haupt


für Recht erkannt:


       I.     Die Klage wird abgewiesen.


       II.    Die Klägerin hat die Kosten des Rechtsstreits zu tragen.


       III.   Das Urteil ist im Kostenpunkt gegen Sicherheitsleistung in
              Höhe von 120 % des jeweils zu vollstreckenden Betrages vorläufig
              vollstreckbar.




                                  Tatbestand


Die Beklagte ist eingetragene Inhaberin des u. a. für die Bundesrepublik Deutschland
erteilten europäischen Patents 1 509 903 (im Folgenden: Streitpatent), das aus der
PCT-Anmeldung PCT/CA2003/000830 (offengelegt als WO 03/102921 A1) hervorgegangen ist, am 30. Mai 2003 unter Inanspruchnahme der Priorität der kanadischen Patentanmeldung 2388439 vom 31. Mai 2002 angemeldet und dessen Erteilung am
12. April 2017 veröffentlicht worden ist. Im Patentregister des Deutschen Patent- und

                                          -3-


Markenamts wird das Streitpatent mit der Bezeichnung „Verfahren und Vorrichtung zur
wirksamen Verschleierung von Rahmenfehlern in linear prädiktiven Sprachkodierern“
unter dem Aktenzeichen 603 50 108 geführt.


Das Streitpatent umfasst in seiner erteilten Fassung 91 Ansprüche mit dem unabhängigen Anspruch 1 (Verfahrensanspruch) und weiteren nebengeordneten Ansprüchen 39,
54, 75, 90 und 91 sowie den abhängigen Ansprüchen 1 bis 38, 40 bis 53, 55 bis 74
sowie 76 bis 89.


Der erteilte Anspruch 1 lautet in der englischen Verfahrenssprache und seiner deutschen Übersetzung unter Hinzufügung einer Merkmalsgliederung des Senats wie folgt:


      1    A method of concealing frame erasure caused by frames of an encoded
           sound signal erased during transmission from an encoder to a decoder, and
           for accelerating recovery of the decoder after non erased frames of the encoded sound signal have been received, comprising:
                   Verfahren zum Verschleiern einer Rahmenlöschung, die durch Rahmen eines codierten Tonsignals verursacht wird, die während einer
                   Sendung von einem Codierer zu einem Decodierer gelöscht werden,
                   und zum Beschleunigen einer Wiederherstellung des Decodierers,
                   nachdem nicht gelöschte Rahmen des codierten Tonsignals empfangen wurden, aufweisend:
      3.1 determining, in the encoder, concealment/recovery parameters comprising
           at least two parameters selected from the group consisting of a signal classification parameter, an energy information parameter, a voicing information parameter and a phase information parameter;
                   Ermitteln, im Codierer, von Verschleierungs-/Wiederherstellungsparametern, die zumindest zwei Parameter aufweisen, ausgewählt aus der
                   Gruppe bestehend aus einem Signalklassifizierungsparameter, einem
                   Energieinformationsparameter, einem Stimmhaftigkeitsinformationsparameter und einem Phaseninformationsparameter;
      4    quantizing the concealment/recovery parameters; and
                   Quantisieren der Verschleierungs-/Wiederherstellungsparameter; und

                                     -4-


5      transmitting to the decoder the quantized concealment/recovery parameters determined in the encoder;
             Senden der im Codierer ermittelten quantisierten Verschleierungs-
             /Wiederherstellungsparameter an den Decodierer;
wherein:
    wobei:
6      the concealment/recovery parameters are usable to improve frame erasure
       concealment and recovery of the decoder after frame erasure;
             die Verschleierungs-/Wiederherstellungsparameter zur Verbesserung
             eines Verschleierns einer Rahmenlöschung und Wiederherstellens
             des Decodierers nach einer Rahmenlöschung verwendbar sind;
2      the sound signal is a speech signal;
             das Tonsignal ein Sprachsignal ist;
characterized in that:
    dadurch gekennzeichnet, dass:
3.2 determining, in the encoder, the concealment/recovery parameters comprises classifying successive frames of the encoded sound signal as unvoiced, unvoiced transition, voiced transition, voiced, or onset; and
             das Ermitteln, im Codierer, der Verschleierungs-/Wiederherstellungsparameter ein Klassifizieren aufeinanderfolgender Rahmen des codierten Tonsignals als stimmlos, stimmloser Übergang, stimmhafter
             Übergang, stimmhaft oder Einsetzen aufweist; und
3.3 determining the concealment/recovery parameters comprises calculating
       the energy information parameter in relation to a maximum of a signal energy for frames classified as voiced or onset, and calculating the energy
       information parameter in relation to an average energy per sample for other
       frames.
             das Ermitteln der Verschleierungs-/Wiederherstellungsparameter ein
             Berechnen des Energieinformationsparameters in Relation zu einem
             Maximum einer Signalenergie für Rahmen, die als stimmhaft oder Einsetzen klassifiziert sind, und ein Berechnen des Energieinformationsparameters in Relation zu einer Durchschnittsenergie pro Abtastung
             für andere Rahmen aufweist.

                                          -5-




Der erteilte Anspruch 39 lautet in der englischen Verfahrenssprache und seiner deutschen Übersetzung durch den Senat unter Fortsetzung der Merkmalsgliederung wie
folgt (wesentliche Unterschiede zum Anspruch 1 sind durch Unterstreichungen gekennzeichnet):


      1a     A method for the concealment of frame erasure caused by frames erased
             during transmission of a sound signal encoded under the form of signal encoding parameters from an encoder to a decoder, and for accelerating recovery of the decoder after non erased frames of the encoded sound signal
             have been received, comprising:
                  Verfahren für die Verschleierung einer Rahmenlöschung, die durch
                  Rahmen verursacht wird, die während einer Sendung eines Tonsignals, das unter der Form von Signalcodierungsparametern codiert ist,
                  von einem Codierer zu einem Decodierer gelöscht werden, und zum
                  Beschleunigen einer Wiederherstellung des Decodierers, nachdem
                  nicht gelöschte Rahmen des codierten Tonsignals empfangen wurden, aufweisend:
      3.1a determining, in the decoder, concealment/recovery parameters from the
             signal-encoding parameters, the concealment/recovery parameters comprising at least two parameters selected from the group consisting of a signal classification parameter, an energy information parameter, a voicing information parameter and a phase information parameter; and
                  Ermitteln, im Decodierer, von Verschleierungs-/Wiederherstellungsparametern aus den Signalcodierungsparametern, wobei die Verschleierungs-/Wiederherstellungsparameter zumindest zwei Parameter aufweisen, ausgewählt aus der Gruppe bestehend aus einem Signalklassifizierungsparameter, einem Energieinformationsparameter,
                  einem Stimmhaftigkeitsinformationsparameter und einem Phaseninformationsparameter; und
      6a     in the decoder, conducting erased frame concealment and decoder recovery in response to the concealment/recovery parameters determined in the
             decoder;

                                           -6-


                   im Decodierer, Durchführen einer Verschleierung gelöschter Rahmen
                   und Wiederherstellung des Decodierers als Antwort auf die im Decodierer ermittelten Verschleierungs-/Wiederherstellungsparameter;
      wherein:
          wobei:
      2      the sound signal is a speech signal;
                   das Tonsignal ein Sprachsignal ist;
      characterized in that:
          dadurch gekennzeichnet, dass:
      3.2a determining, in the decoder, the concealment/recovery parameters comprises classifying successive frames of the encoded sound signal as unvoiced, unvoiced transition, voiced transition, voiced, or onset; and
                   das Ermitteln, im Decodierer, von Verschleierungs-/Wiederherstellungsparametern ein Klassifizieren aufeinanderfolgender Rahmen
                   des codierten Tonsignals als stimmlos, stimmloser Übergang, stimmhafter Übergang, stimmhaft oder Einsetzen aufweist: und
      3.3 determining the concealment/recovery parameters comprises calculating
             the energy information parameter in relation to a maximum of a signal energy for frames classified as voiced or onset, and calculating the energy
             information parameter in relation to an average energy per sample for other
             frames.
                   das Ermitteln der Verschleierungs-/Wiederherstellungsparameter ein
                   Berechnen des Energieinformationsparameters in Relation zu einem
                   Maximum einer Signalenergie für Rahmen, die als stimmhaft oder Einsetzen klassifiziert sind, und ein Berechnen des Energieinformationsparameters in Relation zu einer Durchschnittsenergie pro Abtastung
                   für andere Rahmen aufweist.


Die erteilten nebengeordneten Ansprüche 54 und 75 betreffen Vorrichtungen mit Mitteln zur Durchführung von Verfahren, die denen gemäß Anspruch 1 bzw. 39 entsprechen. Die erteilten nebengeordneten Ansprüche 90 und 91 betreffen einen Decodierer
bzw. einen Codierer mit einer Vorrichtung nach dem Anspruch 75 bzw. 54 und umfassen darüber hinaus zusätzliche Merkmale. Wegen des Wortlauts der angegriffenen und

                                           -7-


erteilten nebengeordneten Ansprüche 54, 75, 90 und 91 sowie der erteilten Unteransprüche wird auf die Streitpatentschrift verwiesen.


Die Klägerin greift das Streitpatent im Umfang seiner Ansprüche 1, 10, 29 bis 33, 39,
48 bis 52, 54, 63, 75, 80, 83 bis 88, 90 und 91 – und folgend alle von der Beklagten
eingereichten Fassungen angegriffener Ansprüche nach ihren Hilfsanträgen – an und
macht die Nichtigkeitsgründe der mangelnden ausführbaren Offenbarung und der fehlenden Patentfähigkeit geltend. Die Beklagte verteidigt das Streitpatent in der erteilten
Fassung sowie mit zwei Hilfsanträgen. Wegen des Wortlauts der Hilfsanträge wird auf
den Schriftsatz der Beklagten vom 6. Dezember 2021 und die Anlage NB10, eingereicht
mit Schriftsatz vom 31. Mai 2021, verwiesen.


Die Klägerin vertritt die Auffassung, dass das Streitpatent dem Fachmann keine
Lehre an die Hand gebe, wie sich die nach Merkmal 4 erforderte Quantisierung jedenfalls auch für die Signalklassiﬁzierungsparameter durchführen und damit Anspruch 1
über die gesamte Breite des Anspruchs ausführen ließe, ohne in Konflikt mit der übrigen
Lehre des Streitpatents zu geraten. Darüber hinaus sei der Gegenstand des erteilten
Anspruchs 1 ausgehend von der Schrift


Svedberg/K3         WO 01/86637 A1


auch nicht patentfähig, insbesondere nicht erfinderisch. Als weiteren Stand der Technik
nennt die Klägerin die Schriften:


Kondoz/K4           Kondoz, A. M.: Digital Speech. Copyright © John Wiley & Sons Ltd,
                    Baffins Lane, Chichester, West Sussex PO19 1UD, England, 1994,
                    Reprinted June, November 1995, July 1996, March 1998, April
                    1999.    Titelseite,   Impressum,   Seiten    vii-xi,   34-37.   ISBN
                    0 471 623717.
Vary/MN1            Vary, P.; Martin, R.: Digital Speech Transmission: Enhancement, Coding and Error Concealment. Copyright © 2006 John
                    Wiley & Sons Ltd, The Atrium, Southern Gate, Chichester, West

                                         -8-


                    Sussex PO19 8SQ, England. Titelseite, Impressum, Seiten vxiii, 4-25, 228-315. ISBN 0-471-56018-9


Die Schrift Svedberg/K3 zeige fast alle Merkmale des Anspruchs 1 des Streitpatents
und die Merkmale 3.2 und 3.3 seien für den Fachmann ausgehend von der Lehre von
Svedberg/K3 naheliegend. Die dem Anspruchsgegenstand nach Merkmal 3.3 zugrundeliegende technische Lehre sei auf eine Unterscheidung zwischen stimmhaften und
nicht stimmhaften Rahmen beschränkt und entspreche der Vorgehensweise, wie in
Svedberg/K3 beschrieben. Wenn demnach der Fachmann ohnehin bereits eine Klassifizierung der Rahmen in stimmhafte und nicht-stimmhafte Rahmen vorgenommen habe,
habe es für ihn auf der Hand gelegen, nicht nur diese Klassifizierung zu übertragen,
sondern auch die Energie, einmal bezogen auf die maximale Signalenergie und einmal
bezogen auf die mittlere Energie des Rahmens, zu codieren und einen dementsprechenden Parameter in Relation zu eben dieser maximalen bzw. mittleren Energie zu
berechnen. Da die nebengeordneten Ansprüche der Lehre des Anspruchs 1 entsprächen, seien diese wie auch die jeweiligen abhängigen Ansprüche nicht patentfähig.




Der Senat hat den Parteien einen qualifizierten Hinweis vom 17. Februar 2021 und am
3. Dezember 2021 einen weiteren rechtlichen Hinweis erteilt.


Die Klägerin beantragt,
         das europäische Patent 1 509 903 im Umfang seiner Ansprüche 1, 10, 29
         bis 33, 39, 48 bis 52, 54, 63, 75, 80, 83 bis 88, 90 und 91 mit Wirkung für
         das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,
         die Klage abzuweisen,
         hilfsweise die Klage abzuweisen, soweit das Streitpatent gemäß den
         Hilfsanträgen 1 und 2, eingereicht mit dem Schriftsatz vom
         6. Dezember 2021, verteidigt wird.

                                          -9-


Sie tritt der Auffassung der Klägerin in allen Punkten entgegen und meint, dass
Anspruch 1 sowohl ausführbar offenbart als auch sein Gegenstand patentfähig sei,
wie dies auch in Bezug auf die Gegenstände der weiteren angegriffenen Ansprüche
der Fall sei. Denn der durch die Klassifizierung nach Merkmal 3.1 ermittelten
Klasse als Signalklassifizierungsparameter könne ohne Weiteres für das Senden
zum Decodierer ein binärer Wert zur Quantifizierung im Sinne des Merkmals 4 des
Anspruchs 1 zugeordnet werden und sei damit für den Fachmann deutlich und vollständig ausführbar offenbart. Zudem sei der Gegenstand nach Anspruch 1 neu und
beruhe auf erfinderischer Tätigkeit. Die Druckschrift Svedberg/K3 offenbare nämlich einen Teil der Merkmale 3.2 und 3.3 des Anspruchs 1 nicht und lege diesen
auch nicht nahe. Die angeführte Argumentation gelte gleichermaßen für die nebengeordneten Ansprüche 39, 54, 75, 90 und 91, auch die erteilten Unteransprüche
seien daher rechtsbeständig.


Wegen der weiteren Einzelheiten des Sach- und Streitstandes wird auf die
Schriftsätze der Parteien nebst Anlagen und den weiteren Inhalt der Akte Bezug
genommen.




                               Entscheidungsgründe


Die Nichtigkeitsklage, mit der die Nichtigkeitsgründe der mangelnden ausführbaren
Offenbarung und der fehlenden Patentfähigkeit geltend gemacht werden (Art II § 6
Abs. 1 S. 1 Nr. 1, 2 IntPatÜG i. V. m. Art. 138 Abs. 1 lit. a), b), Art. 54, Art 56 EPÜ),
ist zulässig.


Die Nichtigkeitsklage ist aber unbegründet, weil sich der Gegenstand des
Streitpatents in seiner erteilten Fassung im angegriffenen Umfang als ausführbar
offenbart und als neu und auf einer erfinderischen Tätigkeit beruhend, mithin als
patentfähig und damit als rechtsbeständig erweist. Auf die Hilfsanträge kommt es
daher nicht mehr an.

                                       - 10 -




                                         I.


1.    Die Erfindung betrifft das robuste Codieren und Decodieren eines Sprachsignals bei gelöschten bzw. verlorenen Daten beispielsweise aufgrund von Kanalfehlern in drahtlosen Übertragungssystemen oder verlorenen Paketen in Voice-over-Packet-Netzwerkanwendungen (Streitpatentschrift, Absätze 0001, 0005).


Nach den sinngemäßen Angaben in der Streitpatentschrift wandelt der Codierer
ein Sprachsignal in einen digitalen Bitstrom um, der über einen Kommunikationskanal übertragen oder auf einem Speichermedium gespeichert wird. Dabei werde
das Sprachsignal digitalisiert, d. h. abgetastet und mit üblicherweise 16 Bit pro Abtastung quantisiert. Der Codierer habe die Aufgabe, diese digitalen Abtastwerte mit
einer geringeren Anzahl von Bits darzustellen und dabei eine gute subjektive
Sprachqualität beizubehalten. Der Decodierer verarbeite den übertragenen bzw.
gespeicherten Bitstrom und wandele ihn in ein synthetisiertes Sprachsignal um
(Absatz 0003).


Die CELP-Codierung (Codebook-Excited Linear Prediction) sei eine der besten
verfügbaren Techniken, um einen guten Kompromiss zwischen subjektiver Sprachqualität und Bitrate zu erzielen. Diese Codierungstechnik bilde die Grundlage für
mehrere Sprachcodierungsstandards sowohl in drahtlosen als auch in drahtgebundenen Netzwerken. Bei einer CELP-Codierung werde das abgetastete Sprachsignal in aufeinanderfolgenden Abschnitten, sogenannten Rahmen (frames), von L
Abtastwerten verarbeitet, die typischerweise einer Zeitdauer von 10 bis 30 ms entsprächen. Ein lineares Vorhersagefilter (linear prediction (LP)) werde berechnet
und für jeden Rahmen übertragen. Die Berechnung des LP-Filters erfordere typischerweise eine Vorausschau auf ein 5-15 ms-Sprachsegment aus dem nachfolgenden Rahmen. Das Restsignal, das nach der linearen Vorhersage verbleibe,
werde in kleinere Abschnitte, sogenannte Unterrahmen (subframes), unterteilt, die
normalerweise einem Sprachsegment von 4-10 ms entsprächen. In jedem dieser
Unterrahmen werde ein Anregungssignal (excitation signal) üblicherweise aus zwei

                                      - 11 -


Komponenten gewonnen, dem aus einem adaptiven Codebuch gebildeten Tonhöhenbeitrag (pitch excitation) und dem aus einem festen/innovativen Codebuch gebildeten Beitrag. Die das Anregungssignal charakterisierenden Parameter würden
codiert und an den Decodierer übertragen, der das rekonstruierte Anregungssignal
als Eingangssignal eines inversen Vorhersagefilters verwende (Absatz 0004).


Das adaptive Codebuch bzw. der Tonhöhenprädiktor (pitch predictor) spiele eine
wichtige Rolle bei der Aufrechterhaltung einer hohen Sprachqualität bei niedrigen
Bitraten. Da der Inhalt des adaptiven Codebuchs jedoch auf dem Anregungssignal
vorangegangener Rahmen basiere, sei das Paar aus Codierer und Decodierer
(Codec) empfindlich gegenüber einem Rahmenverlust. Bei gelöschten oder verlorenen Rahmen unterscheide sich der Inhalt des adaptiven Codebuchs im Decodierer von dem im Codierer. Wenn auf eine Rahmenlöschung folgend wieder „gute“
Rahmen empfangen werden, unterscheide sich das anhand des adaptiven Codebuchs im Decodierer synthetisierte Sprachsignal von dem Synthesesignal, das sich
ohne Rahmenlöschung ergeben hätte, da der Beitrag des adaptiven Codebuchs
durch die Rahmenlöschung geändert worden sei. Die Auswirkung eines gelöschten
Rahmens würde von der Art des Sprachsegments abhängen, in dem die Löschung
stattgefunden habe. Wenn die Löschung in einem stationären Signalsegment auftrete, könne die Rahmenlöschung effizient verschleiert und die Auswirkung auf die
darauffolgenden guten Rahmen minimiert werden. Wenn andererseits die Löschung bei einem Einsetzen des Sprachsignals oder einem Übergang auftrete
(speech onset or a transition), könne sich der Effekt der Löschung über mehrere
Rahmen ausbreiten. Wenn beispielsweise der Anfang eines stimmhaften Segments
(voiced segment) verloren gehe, fehle die erste Tonhöhenperiode im adaptiven
Codebuch. Dies habe eine schwerwiegende Auswirkung auf den Tonhöhenprädiktor in darauffolgenden guten Rahmen, was zu einer langen Zeitdauer führe, bis das
Synthesesignal am Codierer gegen das Signal konvergiere, das sich ohne Rahmenlöschung ergeben hätte, und bis der Decodierer somit wiederhergestellt sei
(Absatz 0006).


Es sei daher Aufgabe der Erfindung, Verfahren und Vorrichtungen zum Verschleiern einer Rahmenlöschung (concealing frame erasure) und zum Beschleunigen der

                                       - 12 -


Wiederherstellung des Decodierers (recovery of the decoder) zu schaffen (Absätze
0008-0011).


Diese Aufgabe soll durch ein Verfahren mit bestimmten Verfahrensschritten im Codierer gemäß dem erteilten Anspruch 1, ein Verfahren mit bestimmten Verfahrensschritten im Decodierer gemäß dem erteiltem Anspruch 39, den Vorrichtungen gemäß den erteilten Ansprüchen 54 und 75 sowie dem Decodierer und dem Codierer
gemäß den Ansprüchen 90 bzw. 91 gelöst werden.




2.    Der zuständige Fachmann ist Ingenieur der Elektro- oder Nachrichtentechnik
mit Universitätsabschluss (Diplom oder Master) und mehrjähriger Berufserfahrung
sowie mit einschlägigen Kenntnissen auf dem Gebiet der digitalen Signalverarbeitung, insbesondere der Codierung von Sprachsignalen.




3.    Mehrere Angaben im erteilten Anspruch 1 bedürfen der Erörterung:


a)    Die Rahmen eines codierten Tonsignals (Merkmal 1) umfassen die im Codierer für einen Rahmen des Tonsignals erzeugten Signalcodierungsparameter
(Streitpatentschrift Absatz 0004 Zeilen 27-29).


Im nicht patentbeschränkenden Ausführungsbeispiel (Absatz 0045 i. V. m. Absatz
0039 Zeile 31) sind diese Signalcodierungsparameter: die einmal pro Rahmen ermittelten quantisierten, interpolierten Koeffizienten des linearen Vorhersagefilters
(Â(z) also called short-term prediction parameters (STP)), die für jeden Unterrahmen ermittelte Tonhöhennacheilung nebst Verstärkungsfaktor und Index des Frequenzformungsfilter (long-term prediction (LTP) parameters T, b, and j) sowie der
Index des innovativen Codebuchs nebst Verstärkungsfaktor (innovation codebook
index k and gain g).

                                       - 13 -




                              SPS, Figur 5 (Ausschnitt)


b)    Beim Verschleiern einer Rahmenlöschung (Merkmal 1) muss der fehlende
Rahmen im Decodierer unter Verwendung der im vorherigen Rahmen erhaltenen
Informationen und durch Schätzen der Signalentwicklung im fehlenden Rahmen
erzeugt werden. Der Erfolg der Schätzung hängt nicht nur von der Verschleierungsstrategie ab, sondern auch von der Stelle im Sprachsignal, an der die Löschung
erfolgt (Absatz 0063 Zeilen 27-30).


Zum Beschleunigen der Wiederherstellung des Decodierers (Merkmal 1) muss ein
reibungsloser Übergang sichergestellt sein, wenn sich der normale Betrieb des Decodierers erholt, d. h., wenn der erste „gute“ Rahmen nach einem oder mehreren
gelöschten Rahmen im Decodierer eintrifft. Zu diesem Zeitpunkt ist der Decodierer
vom Codierer desynchronisiert, da während gelöschter Rahmen der Speicher des
Tonhöhenprädiktors im Decodierer (der Inhalt des adaptiven Codebuchs) nicht
mehr der gleiche ist wie der im Codierer. Die Schwierigkeit bei der Wiederherstellung des Decodierers ist von der Art des Sprachsignals abhängig, die von der Rahmenlöschung betroffen ist (Absatz 0063 Zeilen 30-37).


c)    Zum Verschleiern einer Rahmenlöschung und zum Beschleunigen einer
Wiederherstellung des Decodierers sollen im Codierer zumindest zwei Verschleierungs-/Wiederherstellungsparameter aus der Gruppe bestehend aus einem Signalklassifizierungsparameter, einem Energieinformationsparameter, einem Stimmhaftigkeitsinformationsparameter und einem Phaseninformationsparameter, ermittelt,
quantisiert und an den Codierer gesendet werden (Merkmale 3.1, 4, 5).


Das Ermitteln der zumindest zwei Verschleierungs-/Wiederherstellungsparameter

                                      - 14 -


muss bestimmte Verarbeitungsschritte aufweisen: ein Klassifizieren aufeinanderfolgender Rahmen des codierten Tonsignals als stimmlos, stimmloser Übergang,
stimmhafter Übergang, stimmhaft oder Einsetzen und ein Berechnen des Energieinformationsparameters in Abhängigkeit der Rahmenklassifizierung nach bestimmten Vorgaben (Merkmale 3.2, 3.3).


Der erteilte Anspruch 1 ist jedoch nicht darauf beschränkt, dass das Ergebnis des
Klassifizierens aufeinanderfolgender Rahmen (Merkmal 3.2) und der wie vorgegeben berechnete Energieinformationsparameter (Merkmal 3.3) zu quantisieren und
an den Decodierer zu senden sind. Denn der erteilte Unteranspruch 35 gibt explizit
vor, dass der Energieinformationsparameter nicht an den Decodierer gesendet
wird, und der im Merkmal 3.1 genannte Signalklassifizierungsparameter muss nicht
notwendigerweise das Ergebnis der Rahmenklassifizierung gemäß Merkmal 3.2
sein.


So enthält die Streitpatentschrift auch Varianten des Ausführungsbeispiels der Erfindung, bei denen die im Codierer ermittelte Rahmenklasse nicht an den Decodierer gesendet wird (Absatz 0064 Zeilen 39, 40, Absatz 0100). Die Rahmenklasse
kann im Codierer etwa auch aus der im Bitstrom implizit enthaltenen Information
zum Codierungsmodus eines quellengesteuerten Codierers mit variabler Bitrate
(Absatz 0097) oder aus der Stimmhaftigkeit des aus dem empfangenen Bitstrom
synthetisierten Tonsignals abgeleitet werden (Absatz 0101).


d)      Unter einem Signalklassifizierungsparameter (Merkmal 3.1) versteht der
Fachmann jede Kenngröße, anhand welcher der Decodierer feststellen kann, ob
ein quasistationäres Sprachsegment oder ein Sprachsegment mit sich schnell ändernden Eigenschaften von der Rahmenlöschung betroffen ist (vgl. die in Absatz
0071 Zeilen 20-22 angegebene Grundidee hinter der Verwendung einer Klassifizierung oder Absatz 0006 Zeilen 53-57 oder Absatz 0063 Zeile 36).


Der Fachmann subsummiert unter dem Begriff des Signalklassifizierungsparameters somit insbesondere die Rahmenklasse gemäß Merkmal 3.2, jeden der im erteilten Unteranspruch 10 genannten Parameter (vgl. auch Absatz 0094 Tabelle 2)

                                        - 15 -


und die gemäß Unteranspruch 11 errechnete Bewertungsfunktion (figure of merit,
vgl. auch Absatz 0095).


In einer Variante des Ausführungsbeispiels der Erfindung werden drei Verschleierungs-/Wiederherstellungsparameter an den Decodierer gesendet: die Rahmenklasse (class), der quantisierte Phaseninformationsparameter (τq) und der quantisierte Energieinformationsparameter (E q).




                             SPS, Figur 5 (Ausschnitt)


Zum Ermitteln der Rahmenklasse wird auf der Grundlage der in Tabelle 2 als Signalklassifizierungsparameter bezeichneten Kenngrößen: normierte Korrelation r̅x,
spektrales Neigungsmaß e̅
                        t , Signal-Rausch-Verhältnis snr, Tonhöhenstabilitäts-

zähler pc, relative Signalenergie Es am Ende des aktuellen Rahmens und Nulldurchgangszähler zc,




                       SPS, Absatz 0094, Tabelle 2 (Ausschnitt)



welche mittels einer jeweiligen linearen Funktion skaliert und jeweils auf den Wertebereich zwischen 0 und 1 begrenzt werden, eine Bewertungsfunktion f m (merit
function, Absatz 0095) gebildet:

                                      - 16 -




Das Klassifizieren aufeinanderfolgender Rahmen des codierten Tonsignals erfolgt
anhand der in Tabelle 3 angegebenen Regeln. Ein Rahmen soll beispielsweise
dann als stimmhaft klassifiziert werden, falls die Bewertungsfunktion f m den Wert
0,66 aufweist und der vorhergehende Rahmen zu einer der Klassen stimmhaft,
stimmhafter Übergang oder Einsetzen gehört:




                            SPS, Absatz 0096, Tabelle 3


e)    Die Definitionen der Rahmenklassen stimmlos, stimmloser Übergang,
stimmhafter Übergang, stimmhaft bzw. Einsetzen in den erteilten Unteransprüchen
5-9 dürfen nicht schon einschränkend im Anspruch 1 (Merkmal 3.2) mitgelesen
werden.


Damit verbleibt für das Verständnis etwa der Klasse Einsetzen (Merkmale 3.2, 3.3)
nur ein Teil der Angaben aus der Beschreibung, nämlich die zirkelhafte Angabe:
als Einsetzen klassifizierte Rahmen entsprechen Rahmen mit stimmhaftem Einsetzen, bei denen das Einsetzen bereits ausreichend gut aufgebaut ist, um die für
verlorene stimmhafte Rahmen vorgesehene Verschleierung zu verwenden (Absatz
0076 Seite 11 Zeilen 14, 15).

                                       - 17 -


f)    Die Streitpatentschrift enthält keine Definition des Begriffs Quantisieren
(Merkmal 4), verwendet diesen aber in einer breiteren Bedeutung als fachüblich.


Üblicherweise versteht der Fachmann das Quantisieren eines Parameters als Abbilden eines wertekontinuierlichen Parameters auf einen diskreten Wert einer beschränkten Menge von Werten. Hingegen wird in der Streitpatentschrift auch ein
mit einer bestimmten Präzision codierter Parameter als quantisierter Parameter
bezeichnet (Absatz 0114 Zeilen 42-45). An anderer Stelle der Streitpatentschrift
heißt es sogar explizit, dass ein stückweise linearer Quantisierer verwendet wird,
um die Stimmhaftigkeitsinformationen zu codieren (Absatz 0116 Seite 19 Zeile 4).


Der Fachmann wird daher unter dem im erteilten Anspruch 1 geforderten Quantisieren (Merkmal 4) auch ein Codieren der Verschleierungs-/Wiederherstellungsparameter verstehen, denn der sich aus der Patentschrift ergebende Inhalt der im
Anspruch verwendeten Begriffe ist auch dann maßgebend, wenn dieser von dem
allgemeinen technischen Sprachgebrauch abweicht.


g)     Unter einem Maximum einer Funktion versteht der Fachmann den Wert der
Funktion an einer Stelle des Definitionsbereichs, wenn die Funktion in einer hinreichend kleinen Umgebung (lokales Maximum) oder über den gesamten Definitionsbereich (globales Maximum) keine größeren Werte annimmt.


Das Ausführungsbeispiel des Streitpatents definiert das Maximum der Signalenergie für Rahmen, die als stimmhaft oder Einsetzen klassifiziert sind (Merkmal 3.3),
als Maximalwert E der Abtastwertquadrate s2(i) des unterabgetasteten und vorverarbeiteten Sprachsignals in einem Teilabschnitt am Ende des Rahmens, welcher
der einfachen bzw. der doppelten Tonhöhenperiode tE des vorhergehenden Unterrahmens entspricht (Absatz 0110):




                           SPS, Absatz 0110 Gleichung (16)


Die Streitpatentschrift enthält keine Stelle, die Anlass zu der Annahme gibt, dass

                                       - 18 -


unter einem Maximum einer Signalenergie für Rahmen etwas anderes als ein lokaler Maximalwert der Abtastwertquadrate in einem nicht näher bestimmten Teilabschnitt des Rahmens zu verstehen wäre (vgl. etwa auch die Berechnungsvorschrift
in Absatz 0145 Zeile 55).


Das philologische Argument der Klägerin, die Sprache im ersten Teil des Merkmals
3.3 unterscheide sich an der Stelle „a maximum of a signal energy for frames“
maßgeblich von der Sprache „average energy per sample“ im zweiten Teil des
Merkmals 3.3, beispielsweise formuliere das Merkmal gerade nicht „maximum
energy per sample“ oder ähnliches, führt zu keiner anderen Beurteilung. Denn das
Maximum einer Funktion wird nicht pro Stelle des Definitionsbereichs der Funktion,
sondern für eine Umgebung oder für den gesamten Definitionsbereich der Funktion
bestimmt. Es kann auch dahinstehen, ob das Ergebnis der Berechnungsvorschrift
(16) im Absatz 0110 die Dimension einer Leistung hat, denn – wie vorstehend ausgeführt – ist der sich aus der Patentschrift ergebende Inhalt der im Patentanspruch
verwendeten Begriffe auch dann maßgebend, wenn dieser von dem allgemeinen
technischen Sprachgebrauch abweicht.


h)      Ein Berechnen eines Energieinformationsparameters in Relation zu einem
Maximum einer Signalenergie für bestimmte Rahmenklassen (Merkmal 3.3) setzt
eine nicht näher bestimmte Berechnungsvorschrift voraus, mit welcher ein Energieinformationsparameter aus einem Maximum einer Signalenergie berechnet wird
(vgl. Absatz 0110 Gleichungen (15), (16)).




4.      In der erteilten Fassung des Patents liegt der Nichtigkeitsgrund der mangelnden Offenbarung nicht vor (Art. II § 6 Abs. 1 S. 1 Nr. 2 IntPatÜG, Art. 138
Abs. 1 lit. b) EPÜ).


Die Klägerin hat nicht in Frage gestellt und der Senat hat keine Zweifel, dass der
Fachmann die Anweisungen im Ausführungsbeispiel des Streitpatents ausführen
kann.

                                       - 19 -


Entgegen der Auffassung der Klägerin kann der Fachmann auch die Anweisung im
Merkmal 4 des erteilten Anspruchs 1, insbesondere das Quantisierens des Signalklassifizierungsparameters, ausführen. Nach den vorstehenden Überlegungen zum
Verständnis des Anspruchs 1 subsummiert der Fachmann unter dem Begriff des
Signalklassifizierungsparameters, insbesondere die Rahmenklasse gemäß Merkmal 3.2, jeden der im erteilten Unteranspruch 10 genannten Parameter (vgl. auch
Tabelle 2) und die gemäß Unteranspruch 11 errechnete Bewertungsfunktion (figure
of merit, vgl. auch Absatz 0095).


a)    Der Fachmann kann die fünf im Merkmal 3.2 genannten Rahmenklassen,
stimmlos, stimmloser Übergang, stimmhafter Übergang, stimmhaft oder Einsetzen,
auf eine kleinere Menge von Elementen abbilden, nämlich auf die im Ausführungsbeispiel Absatz 0077 genannten 2 Bit, was nach den vorstehenden Überlegungen
als Quantisieren zu verstehen ist.


Der Einwand der Klägerin, mit einer solchen Abbildung sei nicht der bei einem
Quantisieren untrennbare Informationsverlust verbunden, denn aus den für den aktuellen Rahmen übertragenen 2 Bit und den für den Vorgängerrahmen übertragenen Klassenangaben stünden letztlich fünf Klassen für den aktuellen Rahmen zur
Verfügung, da nach Figur 7 des Streitpatents nur gewisse Abfolgen von Zustandsänderungen erlaubt seien, kann dahinstehen. Denn beim Auftreten von Rahmenlöschung stehen die Verschleierungs-/Wiederherstellungsparameter im Decodierer
gerade nicht für alle aufeinanderfolgenden Rahmen zur Verfügung.


b)    Der Fachmann kann die im erteilten Unteranspruch 10 bzw. in Tabelle 2 genannten Signalklassifizierungsparameter, normierte Korrelation r̅x, spektrales Neigungsmaß e̅t, Signal-Rausch-Verhältnis snr, Tonhöhenstabilitätszähler pc, relative
Signalenergie Es am Ende des aktuellen Rahmens und Nulldurchgangszähler zc,
quantisieren, denn diese stellen nach Skalierung mit den in Tabelle 2 angegebenen
Koeffizienten reelle Zahlen dar, die jeweils auf den Bereich zwischen 0 und 1 begrenzt sind (Absatz 0094).


Für die normierte Korrelation r̅x ist zudem mit Gleichung (20) in Absatz 0118 der

                                       - 20 -


Streitpatentschrift




explizit eine Berechnungsvorschrift für einen Quantisierungsindex i angegeben. Es
ist unerheblich, dass das Streitpatent kein Ausführungsbeispiel umfasst, in dem die
in Tabelle 2 genannten Signalklassifizierungsparameter an den Decodierer gesendet werden. Denn es gibt keinen Rechtssatz des Inhalts, dass jede mögliche Ausführungsform der beanspruchten Erfindung durch ein Ausführungsbeispiel in der
Beschreibung zu erläutern ist.


c)     Der Fachmann ist schließlich auch in der Lage, das Berechnungsergebnis
der in Absatz 0095 angegebenen Bewertungsfunktion f m zu quantisieren. Denn die
Tabelle 3 der Streitpatentschrift gibt gerade an, nach welchen Regeln der aktuelle
Rahmen abhängig u. a. vom Ergebnis der wertekontinuierlichen Bewertungsfunktion f m auf eine der sechs diskreten Klassen stimmhaft, stimmhafter Übergang,
stimmlos, Einsetzen und stimmloser Übergang abgebildet werden soll.


d)     Es mag sein, dass das Quantisieren der verschiedenen Varianten des Signalklassifizierungsparameters zu unterschiedlichen Quantisierungsfehlern und zu
einem unterschiedlichen Bandbreitenbedarf bei der Übertragung der quantisierten
Signalklassifizierungsparameter führt. Das stellt jedoch nicht die Ausführbarkeit
des Gegenstands des Anspruchs 1 oder die Verwendbarkeit der quantisierten Signalklassifizierungsparameter für die im Merkmal 6 des Anspruchs 1 angegebenen
Zwecke in Frage.


Im Übrigen setzt die Ausführbarkeit über den gesamten beanspruchten Bereich
(vgl. BGH, Urteil vom 25. Februar 2010 – Xa ZR 100/05, GRUR 2010, 414 Tz. 23
– Thermoplastische Zusammensetzung) nicht voraus, dass alle Varianten des Ausführungsbeispiels des Streitpatents miteinander beliebig kombinierbar sein müssen.

                                         - 21 -


5.    In seiner erteilten Fassung erweist sich das Streitpatent im angegriffenen
Umfang als patentfähig, nämlich als neu und auf einer erfinderischen Tätigkeit beruhend (Art. 138 Abs. 1 Buchstabe a) i. V. m. Art. 54, 56 EPÜ i. V. m. Art. II § 6
Abs. 1 S. 1 Nr. 1 IntPatÜG).




5.1   Der Gegenstand des erteilten Anspruchs 1 ist neu.


a)    Der Gegenstand des erteilten Anspruchs 1 ist gegenüber dem Stand der
Technik nach der Schrift Svedberg/K3 neu.


Svedberg/K3 betrifft eine verbesserte Vorwärtsfehlerkorrektur (FEC)-Technik beim
redundanten Codieren von Sprachdaten (Abstract). Hierbei erzeugt ein Codierer
aus einem Eingangs-Sprachsignal unter Verwendung eines Primärsynthesemodells primär codierte Daten und unter Verwendung eines redundanten Synthesemodells redundant codierte Daten. Im Ausführungsbeispiel werden primär ein algebraischer Codebuch-verstärkter linearer Vorhersagecodierer (ACELP) gemäß
dem GSM-EFR-Standard (Seite 23 Zeilen 4-8) und redundant ein linearer Vorhersagecodierer (LPC based vocoder) mit Eigenschaften eines für das U.S.-Militär
entwickelten Codierers (LPC-10) und Eigenschaften von GSM-EFR verwendet
(Seite 23 Zeilen 16-18 i. V. m Seite 9 Zeilen 1-17). Die primär und die redundant
codierten Daten werden in einem Paketierer zu einer Folge von Paketen kombiniert
und über ein paketbasiertes Netzwerk an den Decodierer übertragen (Abstract).
Die nachfolgende durch den Senat ergänzte Figur 6 von Svedberg/K3 zeigt, wie
redundante Daten (rot markierte Blöcke) an Primärdaten (weiße Blöcke) angehängt
werden. Beispielsweise enthält das erste Paket Primärdaten für den Rahmen n, an
die redundant codierte Daten für den vorhergehenden Rahmen nangehängt werden (Seite 11 Zeilen 17-21).




          Svedberg/K3, Figur 6 (Ausschnitt) mit Hervorhebungen durch den Senat

                                        - 22 -


Svedberg/K3 schlägt vor, dass wenn das Paket mit dem primärcodierten Rahmen
n verlorengeht (in vorstehender Figur das erste Paket), aber anschließend das Paket empfangen wird, das die Primärdaten für den nachfolgenden Rahmen n+1 sowie die redundant codierten Daten für den Rahmen n enthält (in vorstehender Figur
das zweite Paket), der Decodierer den Rahmen n unter Verwendung der redundanten Daten decodiert und mit diesen Daten auch das primäre Synthesemodell, etwa
das adaptive Codebuch, aktualisiert (Seite 18 Zeilen 10-18), also in der Sprache
des Streitpatents die Rahmenlöschung verschleiert und den Decodierer wiederherstellt. Zudem werden die Primärdaten des Rahmens n+1 zur Vorausschau (look
ahead)-Verarbeitung verwendet, beispielsweise um einen gleichmäßigeren Übergang zwischen Rahmen n und dem nachfolgenden Rahmen n+1 bereitzustellen
(Seite 19 Zeilen 18-23), also um die Wiederherstellung des Decodierers zu beschleunigen.


b)    Svedberg/K3 offenbart dem Fachmann in Worten des erteilten Anspruchs 1:
ein


      1    Verfahren zum Verschleiern einer Rahmenlöschung, die durch Rahmen
           eines codierten Tonsignals verursacht wird, die während einer Sendung
           von einem Codierer zu einem Decodierer gelöscht werden,
               (Seite 12 Zeilen 15-19: … when the packet containing primary data
               is "lost." In such a case, the control logic 518 simply serves to fill in
               gaps in the received stream of primary-encoded frames with redundant-encoded frames;
               Seite 16 Zeile 27: … the use of an error concealment algorithm)
           und zum Beschleunigen einer Wiederherstellung des Decodierers,
           nachdem nicht gelöschte Rahmen des codierten Tonsignals empfangen
           wurden, aufweisend:
               (Seite 18 Zeilen 10-16: Consider, for instance, the state in which
               the decoder module 704 has not received the current frame's primary data (i.e., the primary data is lost) … The decoded values are
               then used to update the primary synthesis model. A CELP-based
               model, for instance, may require updates to its adaptive codebook;

                                - 23 -


        Seite 19 Zeilen 13-21: … the decoder module 704 fails to receive
        the packet containing primary-encoded frame n, but subsequently
        receives the packet containing the primary-encoded data for frame
        n+1 … the decoder module 704 can use the primary data for frame
        n+1 (yet to be decoded) for look-ahead processing. For instance,
        the primary data for frame n+1 can be used to improve interpolation
        of energy levels to provide a smoother transition between frame n
        and frame n+1.)
3.1 Ermitteln, im Codierer, von Verschleierungs-/Wiederherstellungsparametern, die aufweisen,
    einen Energieinformationsparameter,
        (Seite 23 Zeile 30 und Seite 24 Zeile 2: In operation, the GSM-VOC
        encoder … The root mean square (RMS) energy value of the
        speech is then calculated.)
    einen Stimmhaftigkeitsinformationsparameter
        (Seite 24 Zeile 21: The encoder calculates the voicing;
        Seite 25 Zeilen 3, 13-18: To determine if the speech is voiced or
        not, the encoder compares … The information sent to the decoder
        includes the above-computed voicing for both half-frames)
    und einen Phaseninformationsparameter;
        (Seite 21 Zeilen 6-8: the encoder module 702 determines and transmits information pertaining to the pitch phase of the original speech
        signal (such as pitch pulse position and pitch pulse sign) in the redundant coding.)
4   Quantisieren der Verschleierungs-/Wiederherstellungsparameter; und
        (Seite 22, Zeilen 24-27: These parameters can be converted to a
        different format for representing the parameters with reduced bandwidth (e.g., by quantizing the parameters using a method which requires fewer bits than the primary synthesis model used by the primary encoder 802));
        Seiten 25, 26 übergreifender Satz: Further, the encoder converts
        the RMS value into dB and then linear quantizes it using seven bits,
        although fewer bits can be used (e.g., five or six bits).;

                               - 24 -


       Seite 26 Zeile 2: The voicing state uses two bits to represent the
       voicing in each half-frame.;
       Da für die vorstehend genannten drei Verschleierungs-/Wiederherstellungsparameter die in Tabelle 1 Zeilen 4-7 angegebene Anzahl
       von Bits zur Verfügung steht, wird der Fachmann auch den Phaseninformationsparameter ohne weiteres quantisieren.)




                           Svedberg/K3, Seite 26, Tabelle 1


5   Senden der im Codierer ermittelten quantisierten Verschleierungs-
    /Wiederherstellungsparameter an den Decodierer; wobei:
       (vgl. die vorstehend genannten Fundstellen)
6   die Verschleierungs-/Wiederherstellungsparameter zur Verbesserung
    eines Verschleierns einer Rahmenlöschung und Wiederherstellens des
    Decodierers nach einer Rahmenlöschung verwendbar sind;
       (Seite 29 Zeilen 8, 23-28: State: Red Single Error …
       The coding technique extracts the … RMS value, pitch pulse position, and pitch pulse sign, and decodes the extracted values into
       decoded parametric values. The technique also extracts voicing decisions from the frame … The voicing state controls the actions taken in constructing the excitation.;
       Seite 30 Zeilen 26, 27: The decoder module then adjusts the excitation vector's amplitude with an RMS value for each subframe.;
       Seite 31 Zeilen 1, 2: the decoder module can instead perform adjustment on a pitch pulse-basis.)
2   das Tonsignal ein Sprachsignal ist;

                                      - 25 -


               (Bezeichnung: … speech coding)
      wobei:
      3.2Teil das Ermitteln, im Codierer, der Verschleierungs-/Wiederherstellungsparameter ein Klassifizieren aufeinanderfolgender Rahmen des codierten Tonsignals als stimmlos (voiced or not), stimmloser Übergang (the
           transition from voiced to unvoiced speech), stimmhafter Übergang (the
           start of a voiced segment) oder stimmhaft (voiced or not) aufweist; und
               (Seite 25 Zeilen 3-18: To determine if the speech is voiced or not,
               the encoder compares … The encoder uses … to quickly react to
               the start of a voiced segment … to detect voicing during a voiced
               segment … the encoder determines if the previous half-frame was
               voiced … the encoder will mark the half-frame where the transition
               from voiced to unvoiced speech occurs as voiced)
      3.3Teil das Ermitteln der Verschleierungs-/Wiederherstellungsparameter ein
           Berechnen des Energieinformationsparameters in Relation zu einer
           Durchschnittsenergie pro Abtastung aufweist.
               (Seite 23 Zeile 30 und Seite 24 Zeile 2: In operation, the GSM-VOC
               encoder … The root mean square (RMS) energy value of the
               speech is then calculated.;
               Seite 36 Zeilen 8-17: the RMS measure in the last subframe could
               be changed to measure the last complete pitch epoch so that only
               one pitch pulse is measured.;
               Das Berechnen des RMS-Wertes der Signalenergie über einen Unterrahmen steht in einer mathematischen Relation zu einer Durchschnittsenergie pro Abtastung, weil ein Unterrahmen eine vorbestimmte feste Anzahl von Abtastwerten umfasst.)


Der Stand der Technik nach Svedberg/K3 offenbart weder unmittelbar und eindeutig eine Klasse Einsetzen (Restmerkmal 3.2) noch ein Berechnen des Energieinformationsparameters in Relation zu einem Maximum einer Signalenergie für
stimmhafte oder als Einsetzen klassifizierte Rahmen (Restmerkmal 3.3).


Denn nach Svedberg/K3 wird im Codierer unabhängig von der Klassifizierung des

                                      - 26 -


Rahmens bzw. Halbrahmens stets die Wurzel des quadratischen Mittelwerts (RMS)
der Energie des Sprachsignals entweder über den letzten Unterrahmen oder über
die letzte vollständige Tonhöhenepoche gemessen, so dass nur ein Tonhöhenimpuls gemessen wird (Seite 36 Zeilen 9-11). Ein Rahmen umfasst in Svedberg/K3
typischerweise 160 Abtastwerte (Seite 23 Zeilen 10), ein Unterrahmen somit 40
Abtastwerte (Seite 5 Zeile 10) und eine vollständige Tonhöhenepoche, also ein
Tonhöhenimpuls, etwa 30 bis 80 Abtastwerte, denn die Kehrwerte typischer
Sprachgrundfrequenzen liegen im Bereich von 3,8 bis 10 ms.


Die in Svedberg/K3 offenbarte Wurzel des quadratischen Mittelwerts (RMS) der
Energie steht nicht in einer Relation zu einem Maximum der Signalenergie für Rahmen, die als stimmhaft oder Einsetzen klassifiziert sind (Restmerkmal 3.3). Die
Klägerin selbst veranschaulicht und belegt das allgemeine Fachwissen des Fachmanns über Signalformen von stimmhaften und nicht-stimmhaften Rahmen anhand
von Figur 3.1 des Fachbuchs Kondoz/K4.




                           Kondoz/K4, Seite 36 Figur 3.1


Auf Grund der spikeförmigen Gestalt der Tonhöhenimpulse stimmhafter Sprachsegmente kann der Fachmann entgegen der Behauptung der Klägerin nicht davon
ausgehen, dass sich der RMS-Wert und das Maximum der Energie eines Tonhöhenimpulses für als stimmhaft oder Einsetzen klassifizierte Rahmen kaum voneinander unterscheiden würden.


Diese Behauptung der Klägerin wird weder durch die mit Schriftsatz vom 14. Juni

                                       - 27 -


2021 Seite 12 vorgelegten Varianten 1 bis 3 von Signalformen noch durch den
Verweis auf spezielle periodische Signalformen, wie Dreieck-, Rechteck-, sinusförmiges und gaußförmiges Signal, gestützt. Denn in den mit Schriftsatz vom 14. Juni
2021 Seite 12 vorgelegten Varianten 1 bis 3 haben entweder alle Abtastwerte des
Sprachsignals dieselbe Amplitude D oder ist nur ein einziger bzw. sind nur drei von
64 Abtastwerten von Null verschieden. Derartige Signalformen wird der Fachmann
nicht als stimmhaft oder Einsetzen klassifizieren. Der Fachmann geht auch nicht
davon aus, dass ein Sprachsignal, das als stimmhaft oder Einsetzen klassifiziert
ist, ausschließlich periodische Signalkomponenten, wie Dreieck-, Rechteck-, sinusförmige oder gaußförmige Signale, umfasst. Vielmehr berücksichtigt der Fachmann
bei der Codierung von Sprachsignalen mit dem Beitrag des innovativen Codebuchs
zum Anregungssignal auch die nicht-periodischen Anteile des Sprachsignals.


b)    Der Gegenstand des erteilten Anspruchs 1 ist auch gegenüber dem Stand
der Technik nach der Schrift Kondoz/K4 neu.


Die Klägerin hat Gegenteiliges nicht einmal geltend gemacht. Die Schrift Kondoz/K4 wurde von der Klägerin vielmehr zum Beleg und zur Veranschaulichung des
allgemeinen Fachwissens des Fachmanns über Signalformen von stimmhaften und
nicht-stimmhaften Rahmen eingeführt.


c)    Das Fachbuch Vary/MN1 weist eine Copyright-Angabe für das Jahr 2006
auf, ist somit nachveröffentlicht und kein Stand der Technik für das Streitpatent.




5.2   Der Gegenstand des erteilten Anspruchs 1 beruht auch auf einer erfinderischen Tätigkeit.


a)    Svedberg/K3 gibt keine Anregungen oder Hinweise, den Energieinformationsparameter in Abhängigkeit der Rahmenklasse zu bestimmen und diesen in Relation zu einem Maximum einer Signalenergie für stimmhafte oder als Einsetzen
klassifizierte Rahmen zu berechnen (Restmerkmal 3.3).

                                        - 28 -


Denn eine Tonhöhenepoche, über die nach Svedberg/K3 die Wurzel des quadratischen Mittelwerts der Energie des Sprachsignals zu berechnen ist, wird nicht nur
in stimmhaften Sprachsegmenten, sondern in allen Unterrahmen des Sprachsignals bei der Suche im adaptiven Codebuch bestimmt.


b)    Auch bei Hinzunahme des Fachbuchs Kondoz/K4 liegen die Maßnahmen im
Restmerkmal 3.3 nicht nahe.


Entgegen der Auffassung der Klägerin ist die Figur 3.1 von Kondoz/K4 kein Beleg
dafür, dass der Fachmann benachbarte Signalspitzen stimmhafter Signale möglichst aneinander angleichen würde. Denn diese Figur zeigt lediglich exemplarische
Signalformen stimmhafter und stimmloser Signale.




             Kondoz/K4, Seite 36 Figur 3.1 mit Ergänzungen durch den Senat


In der Streitpatentschrift erfährt der Fachmann vielmehr, dass bei einer Rahmenlöschung während eines stimmhaften Sprachsegments das Anregungssignal (excitation) des letzten guten Rahmens typischerweise mit einer Dämpfungsstrategie
zur Verschleierung der Rahmenlöschung verwendet wird. Wenn nach der Rahmenlöschung ein neues lineares Vorhersagefilter (LP filter) mit dem ersten guten Rahmen im Decodierer eintrifft, kann es zu einer Fehlanpassung zwischen der Energie
des Anregungssignals und der Verstärkung des neuen linearen Vorhersagefilters
kommen. Daher sei die Einstellung der Signalenergie bei Rahmenlöschung während stimmhafter Sprachsegments am wichtigsten (Streitpatentschrift, Absatz
0143). Zu derartigen Überlegungen des Streitpatents enthalten weder Svedberg/K3
noch Kondoz/K4 Anregungen oder Hinweise.

                                      - 29 -




c)    Auf Grund der vorstehenden Überlegungen zum Restmerkmal 3.3 kann es
dahinstehen, ob durch Svedberg/K3 ein Klassifizieren auch in eine Klasse „Einsetzen“ nahegelegt wird (Restmerkmal 3.2).




6.    Die Gegenstände der angegriffenen erteilten nebengeordneten Ansprüche
39, 54, 75, 90 und 91 sind ebenfalls neu und beruhen auf einer erfinderischen Tätigkeit, denn sie enthalten jeweils ein dem Merkmal 3.3 des erteilten Anspruchs 1
vergleichbares Merkmal. Zur Vermeidung von Wiederholungen wird auf die vorstehenden Ausführungen des Senats verwiesen. Auch die angegriffenen erteilen Unteransprüche erfüllen die an sie zu stellenden Anforderungen.




                                       II.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 S. 1 und S. 2 ZPO.




                            Rechtsmittelbelehrung




Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils, spätestens aber innerhalb eines Monats nach Ablauf von fünf
Monaten nach Verkündung, durch einen in der Bundesrepublik Deutschland
zugelassenen Rechtsanwalt oder Patentanwalt als Bevollmächtigten schriftlich

                                   - 30 -


oder in elektronischer Form beim Bundesgerichtshof, Herrenstr. 45 a, 76133
Karlsruhe, einzulegen.




Grote-Bittner            Arnoldi   Matter        Söchtig        Dr. Haupt
