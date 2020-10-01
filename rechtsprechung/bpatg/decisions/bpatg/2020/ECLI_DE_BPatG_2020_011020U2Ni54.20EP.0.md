---
ecli: "ECLI:DE:BPatG:2020:011020U2Ni54.20EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 54/20"
decided: "2020-10-01"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=34&nr=40705&anz=666&pos=510&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2020-10-01_2_Ni_54_20_EP_0.txt"
cites_law: ["germany/bund/acts/grundgesetz/artikel/103.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0006.md", "germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0062.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0227.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 54/20 vom 2020-10-01

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES
                                                       Verkündet am
2 Ni 54/20 (EP)                  URTEIL               1. Oktober 2020
                                                             …
verbunden mit
2 Ni 55/20 (EP)
(Aktenzeichen)




                     In der Patentnichtigkeitssache




ECLI:DE:BPatG:2020:011020U2Ni54.20EP.0

                                       -2-




                  betreffend das europäische Patent 2 228 933
                              (DE 60 2008 017 210)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 1. Oktober 2020 unter Mitwirkung der Richterin
Hartlieb als Vorsitzende sowie der Richter Dipl.-Phys. Dr. rer. nat. Friedrich,
Dipl.-Phys. Dr. rer. nat. Zebisch, Dr. Himmelmann und Dr.-Ing. Kapels für Recht
erkannt:


I.   Das europäische Patent 2 228 933 wird mit Wirkung für das Hoheitsgebiet der
     Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt, dass seine
     Ansprüche folgende Fassung erhalten:


     1. A radio transmission apparatus comprising:

                                    -3-


   a coding unit (108, 110) configured to code control data using a MCS for a
   data channel and a MCS indicator for a data channel, which is a CQI, and
   by multiplying the CQI by a decimal scaling factor, and to switch
   associations between the MCS indicator for the data channel and
   modulation and coding schemes for the control data according to the kind
   of control data to determine the modulation and coding scheme of the
   control data based on the association after the switching; and
   a transmitting unit (114) configured to transmit data in the data channel and
   the control data as multiplexed transmission data,
   characterized in that
   the scaling factor is set for each kind of the control data, the modulation and
   coding scheme of the control data is determined based on a new CQI found
   by multiplying by the scaling factor the MCS indicator for the data channel,
   and the control data is coded with a coding rate depending on the kind of
   the control data.


2. A radio transmission method comprising:
   coding (108, 110) control data using a MCS for a data channel and a MCS
   indicator for a data channel, which is a CQI, and by multiplying the CQI by
   a decimal scaling factor;
   switching associations between the MCS indicator for the data channel and
   modulation and coding schemes for the control data according to the kind
   of control data to determine the modulation and coding scheme of the
   control data based on the association after the switching, and
   transmitting (114) data in the data channel and the control data as
   multiplexed transmission data,
   characterized in that
   the scaling factor is set for each kind of the control data, the modulation and
   coding scheme of the control data is determined based on a new CQI found
   by multiplying by the scaling factor the MCS indicator for the data channel,
   and the control data is coded with a coding rate depending on the kind of
   the control data.

                                         -4-


II. Im Übrigen wird die Klage abgewiesen.


III. Die Kosten des Rechtsstreits tragen die Klägerin zu 1) und die Klägerin zu 2)
     jeweils zu 1/20, die Beklagte zu 9/10.


IV. Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu
     vollstreckenden Betrages vorläufig vollstreckbar.




                                   Tatbestand




Die Beklagte ist Inhaberin des am 26. Dezember 2008 in der Verfahrenssprache
Englisch angemeldeten, die Priorität JP 2008000199 vom 4. Januar 2008
beanspruchenden und am 11. Juli 2012 unter dem Titel „RADIO TRANSMITTING
DEVICE     AND     RADIO    TRANSMITTING       METHOD“    mit   der   Patentschrift
EP 2 228 933 B1 veröffentlichten europäischen Patents 2 228 933 (Streitpatent).
Das Streitpatent wird vom Deutschen Patent- und Markenamt unter der Nummer
60 2008 017 210.4 geführt und umfasst 10 Ansprüche, von denen die Ansprüche
2 bis 9 direkt oder indirekt auf den Vorrichtungsanspruch rückbezogen sind.
Anspruch 10 beinhaltet einen (unabhängigen) Verfahrensanspruch.


Die Klägerinnen begehren die Nichtigerklärung des deutschen Teils des
Streitpatents in vollem Umfang. Die Beklagte verteidigt das Streitpatent in vollem
Umfang und hilfsweise beschränkt mit den Hilfsanträgen 1 bis 10 sowie den in der
mündlichen Verhandlung am 1. Oktober 2020 eingereichten weiteren Hilfsanträgen
11, 11a, 12 und 12a.


Der erteilte Patentanspruch 1 lautet in der englischen Fassung gemäß
EP 2 228 933 B1 (mit eingefügter Merkmalsgliederung):


1.    A radio transmission apparatus comprising:

                                        -5-


     1.1 a coding unit (108, 110) configured to code control data using a MCS
          for a data channel and a scaling factor; and
     1.2 a transmitting unit (114) configured to transmit data in the data channel
          and the control data
          characterized in that
          1.1.1   the scaling factor is set for each form of the control data, and
          1.1.2   the control data is coded with a coding rate depending on the
                  form of the control data.


Der erteilte Patentanspruch 1 lautet in der deutschen Fassung gemäß
EP 2 228 933 B1 (mit eingefügter Merkmalsgliederung):


1.   Funk-Sendevorrichtung, die umfasst:
     1.1 eine Codiereinheit (108, 110), die so konfiguriert ist, dass sie
          Steuerdaten unter Verwendung eines MCS für einen Datenkanal und
          eines Skalierfaktors codiert; und
     1.2 eine Sendeeinheit (114), die so konfiguriert ist, dass sie Daten in dem
          Datenkanal und die Steuerdaten sendet,
          dadurch gekennzeichnet, dass
          1.1.1   der Skalierfaktor für jede Form der Steuerdaten festgelegt wird
                  und
          1.1.2   die Steuerdaten mit einer Codierrate codiert werden, die von
                  der Form der Steuerdaten abhängt.


Der erteilte Patentanspruch 10 lautet in der englischen Fassung gemäß
EP 2 228 933 B1 (mit eingefügter Merkmalsgliederung):


10. A radio transmission method comprising:
     10.1 coding (108, 110) control data using a MCS for a data channel and a
          scaling factor; and
     10.2 transmitting (114) data in the data channel and the control data,
          characterized in that
          10.1.1 the scaling factor is set for each form of the control data, and

                                         -6-


           10.1.2 the control data is coded with a coding rate depending on the
                   form of the control data.


Der erteilte Patentanspruch 10 lautet in der deutschen Fassung gemäß
EP 2 228 933 B1 (mit eingefügter Merkmalsgliederung):


10. Funk-Sendeverfahren, das umfasst:
     10.1 Codieren (108, 110) von Steuerdaten unter Verwendung eines MCS für
           einen Datenkanal und eines Skalierfaktors; und
     10.2 Senden (114) von Daten in dem Datenkanal und der Steuerdaten,
           dadurch gekennzeichnet, dass
           10.1.1 der Skalierfaktor für jede Form der Steuerdaten festgelegt wird,
                   und
           10.1.2 die Steuerdaten mit einer Codierrate codiert werden, die von
                   der Form der Steuerdaten abhängt.


Wegen      des   Wortlauts   der   auf   den   Patentanspruch   1   rückbezogenen
Unteransprüche 2 bis 9 wird auf die Patentschrift EP 2 228 933 B1 verwiesen.


Die Klägerinnen stützen ihre Klage auf den Nichtigkeitsgrund der unzulässigen
Erweiterung, den Nichtigkeitsgrund der mangelnden Patentfähigkeit wegen
fehlender Neuheit und auf den Nichtigkeitsgrund der mangelnden Patentfähigkeit
wegen fehlender erfinderischer Tätigkeit.


Zur Stützung ihres Vorbringens hat die Klägerin zu 1) die folgenden Dokumente
genannt:


      GDM-1        EP 2 228 933 B1
      GDM-2        Registerauszug DPMA zum Streitpatent EP 2 228 933
      GDM-3        WO 2009/087743 A1
      GDM-3a       Übersetzung der WO 2009/087743 A1
      GDM-3b       Übersetzungsbestätigung zu GDM-3a
      GDM-4        Merkmalsanalyse Anspruch 1 des Streitpatents

                                       -7-


      GDM-5       3GPP TS 36.212 V8.0.0 (2007-09), Technical Specification, 3rd
                  Generation Partnership Project; Technical Specification Group
                  Radio Access Network; Evolved Universal Terrestrial Radio
                  Access (E-UTRA); Multiplexing and channel coding (Release 8)
      GDM-6       EP 1 953 943 A2
      GDM-7       US 2007/0076677 A1
      GDM-8       Klageerweiterung LG Mannheim Az.: 2 O 98/16.


Zur Stützung ihres Vorbringens hat die Klägerin zu 2) u.a. die folgenden Dokumente
genannt:


      K2          EP 2 228 933 A1 (Veröffentlichung der englischen Übersetzung
                  der internationalen Anmeldung PCT/JP2008004009)
      K6          WO 2006/134946 A1
      K6a         EP 1 892 987 A1
      K7          WO 2007/037412 A1
      K7a         EP 1 914 948 A1
      K8          R1-073842, TSG-RAN WG1 #50, „Notes from uplink control
                  signaling discussions“, Athens, Greece, August 20 – 24, 2007
      K8a         Teilnehmerliste des Treffens 3GPP TSG-RAN WG1#50
      K9          R1-073388, 3GPP TSG-RAN1#50, „UL L1/L2 Control Signals
                  with Data: Multiplexing Detail“, Athens, Greece, August 20 – 24,
                  2007
      K10         Ansprüche 1-13, vorgelegt beim Europäischen Patentamt zur
                  Anmeldung Nr. 08 870 441.6 am 21. September 2010
      K11         Prüfungsbescheid     des    Europäischen     Patentamts    vom
                  14. April 2011 zur Anmeldung Nr. 08870441.6
      K12         Eingabe der Patentinhaberin beim Europäischen Patentamt zur
                  Anmeldung Nr. 08 870 441.6 vom 16. September 2011
      K13         R1-070777, 3GPP TSG RAN1 #48, “Multiplexing of Uplink
                  Control Signaling with Data”, St. Louis, USA, February 12-16,
                  2007

                                         -8-


      K18          3GPP TS 36.212 V8.5.0 (2008-12), Technical Specification, 3rd
                   Generation Partnership Project; Technical Specification Group
                   Radio Access Network; Evolved Universal Terrestrial Radio
                   Access (E-UTRA); Multiplexing and channel coding (Release 8)
      K18a         Veröffentlichungsnachweis von K18
      K19          3GPP TS 36.213 V8.5.0 (2008-12) Technical Specification, 3rd
                   Generation Partnership Project; Technical Specification Group
                   Radio Access Network; Evolved Universal Terrestrial Radio
                   Access (E-UTRA); Physical layer procedures (Release 8)
      K19a         Veröffentlichungsnachweis von K19
      K20          R1-073334, 3GPP TSG-RAN WG1 Meeting #50, “Update to
                   64QAM CQI tables”, Athens, Greece, August 20th – 24th 2007


Die Klägerinnen machen geltend, die Ansprüche der Hilfsanträge könnten die
unzulässigen Erweiterungen in den erteilten Ansprüchen nicht beheben. Darüber
hinaus seien die Hilfsanträge 3, 4, 5, 8, 9 und 10 zurückzuweisen, weil der
Schutzbereich der unabhängigen Ansprüche gegenüber der erteilten Fassung
erweitert sei. Die Gegenstände der Ansprüche der Hilfsanträge seien nicht
patentfähig, da nicht neu, jedenfalls beruhten sie nicht auf erfinderischer Tätigkeit.


Im Hinblick auf die Erweiterung des Schutzbereichs meint die Klägerin zu 1), dass
die unabhängigen Ansprüche jetzt angäben, dass die Steuerdaten unter
Verwendung eines MCS-Zeigers („MCS indicator“) codiert würden, wobei die
Angabe, dass die Steuerdaten unter Verwendung eines Modulations- und
Codierschemas für einen Datenkanal codiert werden, entfallen sei.


Die Klägerinnen beantragen, die Hilfsanträge 11, 11a, 12 und 12a als verspätet
zurückzuweisen


Die Klägerinnen zu 1) und 2) stellen jeweils den Antrag,


      das europäische Patent 2 228 933 mit Wirkung für das Hoheitsgebiet der
      Bundesrepublik Deutschland für nichtig zu erklären.

                                        -9-


Die Beklagte beantragt sinngemäß,


      die Klage abzuweisen,
      hilfsweise das europäische Patent 2 228 933 dadurch teilweise für nichtig zu
      erklären, dass seine Patentansprüche die Fassung eines der Hilfsanträge 1
      bis 10 vom 10. Januar 2020 und der Hilfsanträge 11, 11a, 12, 12a, jeweils
      überreicht in der mündlichen Verhandlung am 1. Oktober 2020, in dieser
      Reihenfolge erhalten.


Die Beklagte erklärt, dass sie die Patentansprüche gemäß Hauptantrag und
Hilfsanträgen als jeweils geschlossene Anspruchssätze ansehe, die jeweils
insgesamt beansprucht werden.


Sie tritt der Argumentation der Klägerinnen in allen wesentlichen Punkten entgegen
und vertritt die Auffassung, dass Gegenstand und Verfahren der erteilten Ansprüche
1 bis 10 hinsichtlich der vorgelegten Druckschriften neu seien und auf einer
erfinderischen Tätigkeit beruhten. Das Streitpatent sei jedenfalls in der Fassung
eines der Hilfsanträge 1 bis 12a patentfähig.


Patentanspruch 1 des Hilfsantrags 1 hat folgenden Wortlaut:

                                     - 10 -


Patentanspruch 1 des Hilfsantrags 2 hat folgenden Wortlaut:




Patentanspruch 1 des Hilfsantrags 3 hat folgenden Wortlaut:




Patentanspruch 1 des Hilfsantrags 4 hat folgenden Wortlaut:

                                     - 11 -




Patentanspruch 1 des Hilfsantrags 5 hat folgenden Wortlaut:




Patentanspruch 1 des Hilfsantrags 6 hat folgenden Wortlaut:

                                     - 12 -




Patentanspruch 1 des Hilfsantrags 7 hat folgenden Wortlaut:




Patentanspruch 1 des Hilfsantrags 8 hat folgenden Wortlaut:

                                     - 13 -




Patentanspruch 1 des Hilfsantrags 9 hat folgenden Wortlaut:

                                       - 14 -




Patentanspruch 1 des Hilfsantrags 10 hat folgenden Wortlaut:




Patentanspruch 1 des Hilfsantrags 11 hat folgenden Wortlaut:


                                  Hilfsantrag 11


1.   A radio transmission apparatus comprising:


     a coding unit (108, 110) configured to code control data using a MCS
     indicator for a data channel, which is a CQI, and by multiplying the CQI by a
     decimal scaling factor, and to switch associations between the MCS indicator
     for the data channel and modulation and coding schemes for the control data
     according to the kind of control data to determine the modulation and coding
     scheme of the control data based on the association after the switching; and
     a transmitting unit (114) configured to transmit data in the data channel and
     the control data as multiplexed transmission data,
     characterized in that

                                          - 15 -


     the scaling factor is set for each kind of the control data, the modulation and
     coding scheme of the control data is determined based on a new CQI found
     by multiplying by the scaling factor the MCS indicator for the data channel,
     and the control data is coded with a coding rate depending on the kind of the
     control data.




Wegen des Wortlauts der Unteransprüche der o.g. Hilfsanträge wird auf die Anlage
zum Schriftsatz der Beklagten vom 10. Januar 2020 sowie hinsichtlich der
Hilfsanträge 11, 12 und 12a auf die Anlage zum Protokoll der mündlichen
Verhandlung vom 1. Oktober 2020 verwiesen. Der in der mündlichen Verhandlung
am 1. Oktober 2020 überreichte Hilfsantrag 11a hat den im Tenor genannten
Wortlaut.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                            Entscheidungsgründe




Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach Artikel II
§ 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG, Artikel 138 Abs. 1 lit. a) EPÜ i. V. m. Artikel 54
und 56 EPÜ, sowie der Nichtigkeitsgrund der unzulässigen Erweiterung nach
Artikel II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜG i. V. m. Artikel 138 Abs. 1 lit. c) EPÜ geltend
gemacht werden, ist zulässig.


Die Klage ist indes nur teilweise begründet. Das Streitpatent ist in der erteilten
Fassung nicht rechtsbeständig, da den Gegenständen des Patents in der erteilten
Fassung der Nichtigkeitsgrund der unzulässigen Erweiterung und der fehlenden
Patentfähigkeit entgegensteht. In der Fassung des Hilfsantrags 11a ist das
Streitpatent jedoch patentfähig.

                                       - 16 -




                                         I.


Die in der mündlichen Verhandlung am 1. Oktober 2020 eingereichten Hilfsanträge
11, 11a, 12 und 12a sind nach § 83 Abs. 4 Satz 1 PatG nicht als verspätet
zurückzuweisen.


Damit ist über die Verteidigung des Streitpatents nach den Hilfsanträgen 11, 11a, 12
und 12a in der Sache zu entscheiden.


Gemäß § 83 Abs. 4 Satz 1 PatG kann das Patentgericht eine Verteidigung des
Beklagten mit einer geänderten Fassung des Patents zurückweisen und bei seiner
Entscheidung unberücksichtigt lassen, wenn dieses Vorbringen nach Ablauf der
hierfür nach § 83 Abs. 2 PatG gesetzten Frist erfolgt ist und die weiteren
Voraussetzungen des § 83 Abs. 4 Satz 1 Nrn. 1 bis 3 PatG erfüllt sind.




1. Mit qualifiziertem Hinweis vom 25. November 2019, der der Beklagten am
28. November 2019 zugestellt worden ist, wurde eine Frist zur beiderseitigen
Äußerung und abschließenden Stellungnahme bis zum 11. Februar 2020 gesetzt.


Die Verteidigung des Streitpatents nach den Hilfsanträgen 11, 11a, 12 und 12a ist
erst in der mündlichen Verhandlung vom 1. Oktober 2020 erfolgt und damit erst nach
der nach § 83 Abs. 2 PatG gesetzten Frist.




2. Eine Berücksichtigung der Hilfsanträge 11, 11a, 12 und 12a hat aber keine
Vertagung der bereits begonnenen mündlichen Verhandlung erforderlich gemacht
(§ 83 Abs. 4 Satz 1 Nr. 1 PatG).


Nach § 99 Abs. 1 PatG i. V. m. § 227 Abs. 1 Satz 1 ZPO kann eine Verhandlung aus
erheblichen Gründen vertagt werden.

                                          - 17 -


Ein erheblicher Grund i. S. d. § 227 Abs. 1 Satz 1 ZPO besteht im Blick auf die
Hilfsanträge 11, 11a, 12 und 12a vorliegend nicht, weil die Klägerin zu 1) bereits in
ihrem Schriftsatz vom 10. Februar 2020 auf die Unzulässigkeit aller bis zu diesem
Zeitpunkt vorgelegten Hilfsanträge 1 bis 10 hingewiesen hat, da in keinem der
Hilfsanträge definiert sei, dass der Skaliervorgang sich auf den CQI-Wert beziehe.
Auch die Klägerin zu 2) hat in ihrem Schriftsatz vom 11. Februar 2020 darauf
hingewiesen, dass alle Hilfsanträge das Fehlen einer am CQI ansetzenden
Skalierung nicht beseitigten. Insoweit sind die Klägerinnen durch die Verteidigung
der Beklagten mit einem geänderten Hilfsantrag 11a bereits nicht überrascht worden,
sondern eine derartige Verteidigung war zu erwarten. Insoweit lag keine
„Unvorhersehbarkeit“ der erfolgten Beschränkung vor und es bestand daher Anlass
für eine vorsorgliche Beschäftigung und Recherche durch die Klägerinnen im
Rahmen der ihr obliegenden Prozessförderungspflicht. Denn die Klägerinnen
mussten damit rechnen, dass die Beklagte auf den Vorhalt der unzulässigen
Verallgemeinerung durch eine entsprechende Beschränkung reagiert.


Erhebliche Gründe im Sinne von § 99 Abs. 1 PatG i. V. m. § 227 Abs. 1 ZPO, die
eine Vertagung der mündlichen Verhandlung rechtfertigen, sind regelmäßig solche,
die den Anspruch auf rechtliches Gehör nach Art. 103 Abs. 1 GG einer oder mehrerer
Parteien berühren und die gerade auch zur Gewährleistung des rechtlichen Gehörs
eine Zurückstellung des Beschleunigungs- und Konzentrationsgebots erfordern. So
lag es hier aus den geschilderten Gründen aber nicht. Zur Gewährung des
rechtlichen Gehörs und eines insoweit prozessordnungsgemäßen Verfahrens
musste die mündliche Verhandlung nicht vertagt werden (Bundesgerichtshof, Urteil
vom 13. Januar 2004, X ZR 212/02, Crimpwerkzeug I, juris, Rn. 27 m. w. N.).




                                              II.


1.    Das    Streitpatent   betrifft   eine     Funkübertragungsvorrichtung   und   ein
Funkübertragungsverfahren, die in Kommunikationssystemen verwendet werden,
welche eine adaptive Modulation verwenden.

                                      - 18 -




Nach der Beschreibung des Streitpatents gewinnt im LTE-System die Übertragung
von Signalen auf einem einzelnen Träger im Uplink, also der Übertragung von z.B.
Nutz- und Steuerungsdaten auf nur einem statt mehreren Trägern vom Endgerät
zur Basisstation, zunehmend an Bedeutung. Zusätzlich werden Studien zur
Durchführung einer adaptiven Modulation (AMC: Adaptive Modulation and Coding)
unternommen, um einen hohen Durchsatz zu erreichen. Bei der adaptiven
Modulation kann in Abhängigkeit von einem Kanalqualitätsindikator (CQI: Channel
Quality Indicator) ein benutzerspezifisches Modulations- und Codierschema (MCS:
Modulation and Coding Scheme) gewählt werden (vgl. Absatz [0002]).


Die Figur 1 des Streitpatents zeigt ein Beispiel einer MCS- bzw. CQI-Tabelle, die
ein Endgerät zur adaptiven Modulation eines Datenkanals verwendet (siehe z.B.
Dokument K20). Basierend auf einem CQI-Wert, das heißt basierend auf
Kanalqualitätsinformationen   einschließlich   eines   Signal-Rausch-Verhältnisses
(SNR), werden verschiedene Modulationsschemata und Codierungsraten aus der
Tabelle gelesen, um ein MCS für einen Datenkanal zu bestimmen (vgl. Absatz
[0004]).

                                     - 19 -




                           Figur 1 des Streitpatents


Darüber hinaus werden Studien durchgeführt, um einen Uplink-Datenkanal und
einen Uplink-Steuerkanal in demselben Rahmen zu übertragen und unter
Verwendung eines CQI, mit dem der MCS des Datenkanals bestimmt wird,
gleichzeitig auch einen MCS des Steuerkanals zu bestimmen (siehe z.B. Dokument
GDM-5). Die internationale Patentanmeldung WO 2007/037412 A1 (K7) offenbart
die Bestimmung eines Modulations- und Codierungsschemas für den Steuerkanal
aus einem CQI und einem CQI-Offset (vgl. Absatz [0005]).


Dementsprechend werden ähnlich wie beim MCS für einen Steuerkanal
verschiedene   Modulationsschemata     und    Codierungsraten   (im   Folgenden
„Spektrale Effizienz“ (SE), wobei SE als die Anzahl von Bits pro Symbol mal
Codierungsrate definiert ist) gemäß den CQIs bestimmt. Die Figur 2 des
Streitpatents zeigt ein Beispiel einer CQI-Tabelle, in der Zuordnungen zwischen

                                        - 20 -


Datenkanal SE und Steuerkanal SE gezeigt sind. In diesem Beispiel ist die
Spektrale Effizienz des Steuerkanals in Bezug auf CQIs robust eingerichtet, d.h.,
die Spektrale Effizienz (SE) ist so niedrig eingestellt, dass die Steuerdaten auch in
einer schlechten Empfangsumgebung mit ausreichender Qualität übertragen
werden (vgl. Absatz [0006]).




                               Figur 2 des Streitpatents


Gemäß Figur 3 des Streitpatents ist, wenn ein Daten- und ein Steuerkanal
gemultiplext und in demselben Rahmen übertragen werden, die Menge der für jeden
Kanal nutzbaren Ressourcen bestimmt. Sind die Übertragungsbedingungen gut, die

                                       - 21 -


Spektraleffizienz jedoch derartig robust eingestellt, dass die erforderliche Qualität
des Steuerkanals mehr als erfüllt ist, werden Funkressourcen für den Steuerkanal
bereitgestellt, die jedoch nicht benötigt werden. Da diese „verschwendeten“
Ressourcen jedoch nicht als Datenkanalressourcen verwendet werden können,
verringert sich der Datenkanaldurchsatz (vgl. Absätze [0007] und [0008] der
Streitpatentschrift).




                             Figur 3 des Streitpatents


Vor diesem Hintergrund liegt dem Streitpatent als technisches Problem die Aufgabe
zugrunde, eine Funkübertragungsvorrichtung und ein Funkübertragungsverfahren
bereitzustellen, die den Datenkanaldurchsatz verbessern (vgl. Abs. [0009] der
Streitpatentschrift).


Diese Aufgabe wird durch die Funk-Sendevorrichtung des Anspruchs 1 und das
Funk-Sendeverfahren nach Anspruch 10 des Streitpatents gelöst.




2.     Der hier zuständige Fachmann ist als berufserfahrener Ingenieur der
Fachrichtung Elektrotechnik oder Nachrichtentechnik zu definieren, der einen
Hochschulstudienabschluss besitzt und über eine mehrjährige praktische Erfahrung
in der Entwicklung von Verfahren und Vorrichtungen zur Kodierung und Modulation
für die Signalübertragung in drahtlosen Mobilfunksystemen verfügt.

                                         - 22 -


Dieser Fachmann bringt sich insbesondere im Rahmen der Projekte der 3GPP in
Standardisierungsprozesse ein und ist über die aktuellen Entwicklungen und
Vorschläge in den entsprechenden Gremien informiert.




3.      Die Patentansprüche bedürfen im Hinblick auf einige Merkmale näherer
Erörterung.


Maßgeblich ist, was der angesprochene Fachmann – auch unter Einbeziehung
seines Vorverständnisses (BGH, Beschluss vom 08. Juli 2008, X ZB 13/06, GRUR
2008,      887   –   Momentanpol   II)   –   bei   unbefangener   Betrachtung   den
Patentansprüchen als Erfindungsgegenstand entnimmt. Insoweit kann die
Patentschrift im Hinblick auf die gebrauchten Begriffe auch ihr eigenes Lexikon
darstellen (BGH, Urteil vom 02. März 1999, X ZR 85/96, GRUR 1999, 909 –
Spannschraube; BGH, Urteil vom 13. April 1999, X ZR 23/97, Mitt. 2000, 105 –
Extrusionskopf).


Beansprucht werden eine Funk-Sendevorrichtung und ein Funk-Sendeverfahren.


Die Funk-Sendevorrichtung, bei der es sich beispielsweise um ein Endgerät
handeln kann, umfasst eine Codiereinheit, die Steuerdaten codiert. Die Codierung
erfolgt dabei unter Verwendung eines MCS für einen Datenkanal und eines
Skalierfaktors (Merkmal 1.1). Diesen Angaben entnimmt der Fachmann, dass,
obwohl es sich um Steuerdaten handelt, zumindest nicht nur ein „MCS für einen
Steuerkanal“ zur Codierung der Steuerdaten verwendet wird, sondern zumindest
ein „MCS für einen Datenkanal“. Bei einem „MCS“ handelt es sich gemäß
Streitpatent um ein Modulations- und Codierschema (vgl. Absatz [0002] der
Streitpatentschrift). Das MCS definiert dabei sowohl das Modulationsschema (z. B.
QPSK        (Vierphasen-Modulation),     16-QAM     (16-fach   Quadraturamplitudenmodulation) oder 64-QAM), zur Modulation, als auch das Codierschema (die
Codierrate) zur Codierung der Steuerdaten (vgl. Absätze [0002] bis [0004] und
Fig. 1).

                                          - 23 -


Dem Fachmann ist aus seinem Fachwissen bekannt, dass die Codierrate das
Verhältnis    von   Eingangsbits     zu     Ausgangsbits    angibt,    während     das
Modulationsschema die Anzahl an Bits pro Symbol definiert.


Der Patentanspruch gibt an, dass zumindest eines der für die Übertragung von
Kontrolldaten verwendeten Modulations- und Codierschemata eines ist, das auch
für die Übertragung von Daten im Datenkanal benutzt wird. Er gibt nicht an, unter
welchen Voraussetzungen dieses Modulations- und Codierschema verwendet wird.


Darüber hinaus werden die Steuerdaten auch unter Verwendung eines
Skalierfaktors codiert (Merkmale 1.1 und 10.1). Welcher Parameter skaliert werden
soll, ist im Anspruch jedoch nicht definiert, so dass dieser weder die Skalierung des
MCS, noch die Skalierung eines empfangenen CQI-Werts fordert. Es genügt also,
wenn bei der Codierung der Steuerdaten an einer Stelle das MCS für den
Datenkanal verwendet und in anderem Zusammenhang eine Abhängigkeit der
Codierung von einem Skalierfaktor geschaffen wird. Gemäß dem nicht
beschränkenden Ausführungsbeispiel 3 des Streitpatents kann die Verwendung
eines Skalierfaktors dadurch realisiert werden, dass ein das MCS bestimmender
CQI-Wert zunächst mittels Offset und anschließend durch einen multiplikativen
Skalierfaktor modifiziert wird (vgl. Absätze [0041] bis [0043] und Fig. 13 des
Streitpatents).


Gemäß Merkmal 1.1.1 bzw. 10.1.1 wird der Skalierfaktor für jede Form der
Steuerdaten festgelegt. Unter „Form der Steuerdaten“ ist dabei zu verstehen, dass
für   jede   Formatierung der      Steuerdaten,    also   auch   für   unterschiedliche
Formatierungen der gleichen Art von Steuerdaten ein eigener Skalierfaktor
festgelegt wird, was aber nicht ausschließt, dass für alle Formate derselben Art von
Steuerdaten ein einheitlicher Skalierfaktor festgelegt wird. Eine abweichende
Auslegung würde bedeuten, dass keine der in der Beschreibung vorgestellten
Ausführungsformen die anspruchsgemäße Lehre zeigt. Somit wird der Skalierfaktor
beispielsweise für jede Art der Steuerkanäle (z.B. CQI, ACK/NACK) festgelegt, so
dass ein CQI-Skalierfaktor und ein ACK/NACK-Skalierfaktor bei einer Codierung
der Steuerdaten verwendet werden.

                                          - 24 -


Jedoch definiert auch das Merkmal 1.1.1 bzw. 10.1.1 nicht, welcher Parameter mit
diesen Skalierfaktoren skaliert werden soll. Die Codierung der Steuerdaten erfolgt
somit auch nicht mit einer Codierrate, die von der Form der Steuerdaten abhängt,
sondern mit einer spezifischen Codierrate, die von der Art der Steuerkanäle abhängt
(Merkmal 1.1.2 bzw. 10.1.2).


Ferner   umfasst    die    Funk-Sendevorrichtung,     gemäß       Merkmal   1.2,   eine
Sendeeinheit, die die Daten des Datenkanals und die Steuerdaten sendet. Bei den
Steuerdaten handelt es sich dabei um die codierten (und modulierten) Daten des
Steuerkanals (vgl. Absatz [0022]), so dass die Sendeeinheit die Daten des
Datenkanals und die Daten des Steuerkanals sendet. Dazu werden die Daten
beispielsweise gemultiplext (vgl. Absätze [0008], [0023], [0040] des Streitpatents).


Ein Beispiel für die Verwirklichung dieser Lehre soll, gemäß Absatz [0010] der
Patentschrift, das Ausführungsbeispiel 3 zeigen. Dieses Ausführungsbeispiel
basiert auf dem Ausführungsbeispiel 2. Gemäß Ausführungsbeispiel 2 wird von
einem Endgerät ein CQI-Wert empfangen, aus dem mittels einer Datenkanal-CQI-Tabelle ein MCS 1 für einen Datenkanal bestimmt werden kann (vgl. Absätze
[0028], [0032], [0033] und Fig. 10 des Streitpatents). Zum empfangenen (bzw.
Daten-) CQI wird ein CQI-Offset hinzuaddiert, der einer betriebsbedingungsabhängigen Offset-Tabelle entnommen wird (vgl. Absatz [0033] und Figuren 10, 11).
Gemäß Ausführungsbeispiel 3 wird die Summe aus CQI und CQI-Offset schließlich
mit einem Skalierfaktor N multipliziert, um den Steuerkanal-CQI zu ermitteln. Dem
Streitpatent ist folgende Gleichung (2) zur Berechnung des Steuerkanal-CQI zu
entnehmen (vgl. Absatz [0041]):




Durch Variation des Skalierfaktors N können für unterschiedliche Arten von
Steuerkanälen (z.B. CQI, ACK/NACK) unterschiedliche Codierschemata verwendet
werden (vgl. Absatz [0042]). Aus einer verlängerten CQI-Tabelle können mit den
ermittelten CQI-Werten steuerkanalspezifische Werte der spektralen Effizienz (SE)
bestimmt    werden,       die   jeweils   einem    spezifischen    Modulations-    und

                                       - 25 -


Codierungsschema SE (SE = Modulationsschema * Codierrate) entsprechen (vgl.
Fig. 13).




                            Figur 13 des Streitpatents


Damit existiert keine unveränderbare Zuordnung des Nutzdaten-MCS zu einem
einzigen    Steuerdaten-MCS    mehr.   Vielmehr   kann   das   Modulations-    und
Codierschema (bzw. SE als deren Multiplikation) für die Steuerdaten über geeignete
Parameter bestimmt werden. Im Ausführungsbeispiel kommt, neben dem im
Patentanspruch nicht gelehrten Offset, ein im Patentanspruch angesprochener
Skalierfaktor N zum Einsatz. Die Lösung der Ausführungsform 3 hat damit auch den
Vorteil, dass sie mittels des Skalierungsfaktors (im Beispiel 0,7 oder 1,3) eine je

                                        - 26 -


nach Art des Steuerkanals differenzierende Wahl der Steuerdaten-Modulation und
-Codierrate ermöglicht. Mit der Verwendung eines steuerdatenartabhängigen
Skalierfaktors ermöglicht es der Patentanspruch, unterschiedliche Modulations- und
Codierraten für unterschiedliche Arten von Steuerdaten vorzusehen und hierdurch
eine Ressourcenverschwendung dadurch zu vermeiden, dass je nach den
steuerdatenartspezifischen Bedürfnissen die Ressourcen angemessen verteilt und
damit insgesamt effizienter genutzt werden können.




4.     Zum Hauptantrag


4.1.   In der erteilten Fassung ist das Streitpatent nach Artikel II § 6 Abs. 1 Satz 1
Nr. 3 IntPatÜG i. V. m. Artikel 138 Abs. 1c) EPÜ für nichtig zu erklären, da der
Gegenstand des Anspruchs 1 über den Inhalt der europäischen Patentanmeldung
in ihrer bei der für die Einreichung der Anmeldung zuständigen Behörde
ursprünglich eingereichten Fassung hinausgeht.


4.1.1. Nach ständiger Rechtsprechung gehört zum Offenbarungsgehalt einer
Patentanmeldung nur das, was den ursprünglich eingereichten Unterlagen in der
Gesamtheit ihrer Offenbarung unmittelbar und eindeutig als zu der zum Patent
angemeldeten Erfindung gehörend zu entnehmen ist. Danach ist es erforderlich,
aber auch ausreichend, dass der Fachmann die im Anspruch bezeichnete
technische Lehre den Ursprungsunterlagen unmittelbar und eindeutig als
Ausgestaltung der Erfindung bzw. als mögliche Ausführungsform entnehmen kann
(BGH, Urteil vom 25. November 2014, X ZR 119/09, GRUR 2015, 249 –
Schleifprodukt; BGH, Urteil vom 11. Februar 2014, X ZR 107712, BGHZ 200, 63
Rn. 19 ff. m. w. N. = GRUR 2014, 542– Kommunikationskanal).


Eine unzulässige Erweiterung liegt hingegen vor, wenn der Gegenstand des Patents
sich für den Fachmann erst aufgrund eigener, von seinem Fachwissen getragener
Überlegungen ergibt, nachdem er die ursprünglichen Unterlagen zur Kenntnis
genommen hat. Zu einer unzulässigen Erweiterung führen auch solche
Änderungen, durch die der Gegenstand der Anmeldung über den Inhalt der

                                       - 27 -


ursprünglich eingereichten Anmeldungsunterlagen hinaus zu einem Aliud
abgewandelt wird. Dies ist unter anderem dann der Fall, wenn die Hinzufügung
einen technischen Aspekt betrifft, der den ursprünglich eingereichten Unterlagen in
seiner konkreten Ausgestaltung oder wenigstens in abstrakter Form nicht als zur
Erfindung gehörend zu entnehmen ist (BGH, Urteil vom 09. April 2013, X ZR 130/11,
GRUR 2013, 809 – Verschlüsselungsverfahren).


Ein „breit“ formulierter Patentanspruch kann als unbedenklich zu erachten sein,
wenn sich ein in der ursprünglichen Anmeldung beschriebenes Ausführungsbeispiel
der Erfindung für den Fachmann als Ausgestaltung der im Patentanspruch
umschriebenen allgemeineren technischen Lehre darstellt und diese Lehre in der
beanspruchten Allgemeinheit für ihn bereits der Anmeldung – sei es in Gestalt eines
in   der   Anmeldung    formulierten   Patentanspruchs,     sei   es   nach   dem
Gesamtzusammenhang der Unterlagen – als zu der angemeldeten Erfindung
gehörend zu entnehmen ist (BGH, Urteil vom 29. April 2014, X ZR 19/11,
GRUR 2014, 970 – Stent; BGH, Urteil vom 11. Februar 2014, X ZR 107/12,
GRUR 2014, 542 – Kommunikationskanal; BGH, Urteil vom 17. Juli 2012,
X ZR 117/11, GRUR 2012, 1124 – Polymerschaum).


Unzulässig ist eine Verallgemeinerung hingegen, wenn den ursprünglich
eingereichten Unterlagen zu entnehmen ist, dass einzelne Merkmale in
untrennbarem Zusammenhang miteinander stehen, der Patentanspruch diese
Merkmale aber nicht in ihrer Gesamtheit vorsieht (BGH, Urteil vom 21. Juni 2016,
X ZR 41/14, GRUR 2016, 1038 Fahrzeugscheibe II; BGH, Beschluss vom
11. September 2001, X ZB 18/00, GRUR 2002, 49 – Drehmomentübertragungseinrichtung).


4.1.2. Die Anweisung „to code control data using a MCS for a data channel and a
scaling factor“ (Merkmal 1.1) erweitert den Gegenstand der Anmeldung, denn
sämtliche Offenbarungsstellen der ursprünglichen Patentanmeldung lehren
zwingend eine Verwendung eines CQI.

                                       - 28 -


Dem Ausführungsbeispiel 1 der ursprünglichen Anmeldung, bei dem es sich gemäß
Absatz [0010] der Streitpatentschrift um kein patentgemäßes Ausführungsbeispiel
handelt, ist zu entnehmen, dass aus dem empfangenen Signal eine CQI-Information
extrahiert wird, aus der mittels einer CQI-Tabelle ein MCS 1 für einen Datenkanal
bestimmt wird (vgl. K2, Absätze [0020] bis [0021]). Das MCS 2 für den Steuerkanal
wird aus der CQI-Information, der Bandbreite und mehreren bandbreitenabhängigen CQI-Tabellen bestimmt (vgl. K2, Absatz [0021]). In diesem Beispiel
werden die Steuerdaten somit nur unter Verwendung eines CQI codiert (vgl. K2,
Absätze [0023], [0031]).


Das Ausführungsbeispiel 2 der ursprünglichen Anmeldung, bei dem es sich
ebenfalls um kein patentgemäßes Ausführungsbeispiel handelt, beschreibt die
Berechnung eines Steuerkanal CQI auf Basis der empfangenen CQI-Information
(aus der auch mittels einer CQI-Tabelle ein MCS 1 für einen Datenkanal bestimmt
wird) und einer Offset-Tabelle, in der unterschiedliche Offset-Werte je nach
Übertragungsbedingung angegeben sind (vgl. K2, Absätze [0033] bis [0036] und
Fig. 10, 11). Aus dem berechneten Steuerkanal-CQI wird eine spektrale Effizienz
SE ermittelt, aus der das MCS 2 für den Steuerkanal bestimmt wird (vgl. K2, Absätze
[0040] bis [0041] und Fig. 12). Auch in diesem Beispiel werden die Steuerdaten
somit unter Verwendung eines CQI codiert.


Gemäß dem patentgemäßen Ausführungsbeispiel 3 wird der CQI nach Addition
eines bedingungsabhängigen Offsets (vgl. Ausführungsbeispiel 2) mit einem
steuerkanalartabhängigen Skalierungsfaktor multipliziert. Dem so ermittelten
Steuerkanal-CQI – je Steuerkanalart – kann ein bestimmter SE-Wert zugeordnet
werden, um daraus die Bestandteile des Steuerkanal-MCS, nämlich die
Modulationsordnung und die Codierrate zu bestimmen (vgl. K2, Absätze [0042] bis
[0043], Gleichung 2 und Fig. 13). Im Absatz [0044] wird zudem explizit darauf
hingewiesen, dass der Skalierfaktor mit einem CQI multipliziert wird („a scaling
factor is multiplied by a control channel CQI that is found by adding all the amounts
of offsets, to calculate the new control channel CQI and to determine the MCS for
the control channel“), so dass auch das Ausführungsbeispiel 3 nur die Verwendung
eines CQI offenbart.

                                      - 29 -




Auch die Ansprüche der ursprünglichen Anmeldung sehen vor, dass die Zuordnung
zwischen CQIs und Modulations- und Codierschemata entsprechend einem
Parameter umgeschaltet werden kann, um das MCS für den Steuerkanal zu
bestimmen, so dass auch in diesem zwingend die Verwendung eines CQI gelehrt
wird.


Die Argumentation der Beklagten, wonach, wenn es um das MCS für den
Datenkanal gehe, die Ausdrücke MCS und CQI synonym seien, da die Figur 1 im
Streitpatent sowohl als „MCS Tabelle“, als auch als „CQI Tabelle“ bezeichnet werde,
kann nicht überzeugen. Denn die ursprüngliche Anmeldung definiert „CQI“ als eine
Kanalqualitätsinformation, wie z.B. ein Signal-zu-Rausch-Verhältnis (SNR), die ein
Empfangsgerät aus einem empfangenen Signal extrahiert und die beispielsweise
Werte von 0 bis 30 annimmt (vgl. K2, Abs. [0002], [0004], [0020] und Fig. 1).
Demgegenüber definiert die ursprüngliche Anmeldung „MCS“ als ein Modulationsund Codierschema (vgl. K2, Absatz [0002]: „MCS (Modulation and Coding
Scheme)“), das sowohl das Modulationsschema als auch das Codierschema
beinhaltet (vgl. K2, Absätze [0002] bis [0005] und Fig. 1). Bereits diesen Angaben
entnimmt der Fachmann, dass „CQI“ und „MCS“ nicht synonym sind. Darüber
hinaus wird das „MCS“ aus dem „CQI“ bestimmt (vgl. K2, Abs. [0044]: „In this way,
according to Embodiment 3, a scaling factor is multiplied by a control channel CQI
that is found by adding all the amounts of offsets, to calculate the new control
channel CQI and to determine the MCS for the control channel“, sowie die Figuren
7 und 10). Somit entspricht das MCS nicht dem CQI, sondern wird aus dem CQI
bestimmt. Auch die Ansprüche der ursprünglichen Anmeldung sehen vor, dass die
Zuordnung      zwischen       CQI      und      MCS       entsprechend      einem
Funkkommunikationsendgerät-Parameter umgeschaltet werden kann, um das MCS
für den Steuerkanal zu bestimmen.


Somit kann der Fachmann der gesamten ursprünglichen Anmeldung nur
entnehmen, dass zwingend ein CQI herangezogen wird, um daraus nach Ermittlung
eines modifizierten Steuerkanal-CQI ein MCS für den Steuerkanal zu bestimmen.

                                       - 30 -


4.1.3. Auch die Verwendung eines Skalierfaktors ist ursprünglich nur dahin
offenbart, dass er bei der Berechnung des Steuerkanal-CQI aus dem (Datenkanal)
CQI verwendet wird.


Der erteilte Anspruch 1 umfasst eine nicht mehr am CQI, sondern eine an beliebiger
Stelle ansetzende Skalierung (vgl. Merkmal 1.1).


Der ursprünglichen Anmeldung ist demgegenüber jedoch nur zu entnehmen, dass,
wie bereits im Kapitel 4.1.2 dargelegt, der Skalierfaktor mit einem CQI multipliziert
wird (vgl. K2, Gleichung 2 und Absatz [0043]: „a scaling factor is multiplied by a
control channel CQI that is found by adding all the amounts of offsets, to calculate
the new control channel CQI and to determine the MCS for the control channel“).


Die Argumentation der Beklagten, wonach es sich bei der Offenbarung des
Absatzes [0043] um eine allgemeine Aussage, ohne Bezugnahme darauf, wo die
Skalierung ansetze, handele, ist nicht zuzustimmen, denn dieser Absatz [0043]
bezieht sich explizit auf den Skalierfaktor „N“ (vgl. Abs. [0043]: „by changing the
value, N,“), der im vorhergehenden Absatz [0042] in der Gleichung (2) zur
Berechnung des Steuerkanal-CQI eingeführt wurde.


Dementsprechend kann der Fachmann nur mit einem Anspruch rechnen, in dem
unter anderem angegeben ist, dass mit einem (Datenkanal-) CQI gearbeitet wird,
der skaliert wird, um einen in eine Steuerkanal-CQI-Tabelle einsetzbaren Wert zu
erhalten.


4.1.4. Darüber hinaus ist den Ursprungsunterlagen der Begriff „form of the control
data“ nicht zu entnehmen. Insbesondere ist nicht offenbart, dass der Skalierfaktor
für jede Form der Steuerdaten festgelegt wird (Merkmale 1.1.1/10.1.1, 1.1.2/10.1.2).


Der Offenlegungsschrift (K2) der ursprünglichen Anmeldung sind nur Festlegungen
für unterschiedliche Arten von Steuerkanälen (CQI-Kanal oder ACK/NACK-Kanal)
zu entnehmen (vgl. K2, Abs. [0043]: „where a coding scheme varies like between
an uplink CQI channel and ACK/NACK channels used in LTE, by changing the

                                        - 31 -


value, N, a control channel is applicable to different coding schemes.“, „… so that it
is possible to refer to MCSs of two kinds of control channels from the same CQI
table.“).


Demgegenüber versteht der Fachmann die Form der Steuerdaten sowohl als
Format der Steuerdaten, wie z.B. deren Rahmenlänge, als auch als deren Art, wie
z.B. CQI oder ACK/NACK.


Der Beklagten ist daher nicht zuzustimmen, dass im Lichte der Beschreibung
(Art. 69 EPÜ) das einzig richtige Verständnis des Ausdrucks „Form der
Steuerdaten“ in den Ansprüchen in der Bedeutung „Art von Steuerdaten“ sei. Der
Fachmann kann den Ursprungsunterlagen jedoch unmittelbar und eindeutig nur
unterschiedliche Arten von Steuerkanälen entnehmen (vgl. K2. Abs. [0043]: "two
kinds of control channels").


Daher ist eine Festlegung des Skalierfaktors für jede Form der Steuerdaten breiter
als eine Festlegung für jede Art der Steuerkanäle, so dass es sich bei „form of the
control data“ um eine unzulässige Änderung handelt.


4.1.5. Ferner ist den ursprünglichen Unterlagen eine unabhängige Übertragung der
Nutz- und der Steuerdaten nicht zu entnehmen (Merkmale 1.2/10.2).


Denn sowohl die Problembeschreibung als auch die Ausführungsbeispiele weisen
nur einen konkreten Bezug zur Ausgestaltung auf, dass die Nutz- und die
Steuerdaten in einem Zeitmultiplexverfahren zusammengefasst und im selben
Rahmen übertragen werden (vgl. K2, Absätze [0007] bis [0009], [0024] und Fig. 3).


Der Argumentation der Beklagten, dass sich dem Fachmann unmittelbar und
eindeutig Ausführungsformen der Erfindung erschließen, die nicht auf gemultiplexte
Daten- und Steuerkanäle beschränkt seien, ist nicht zuzustimmen. Denn im Lichte
der BGH-Entscheidung „Kommunikationskanal“ (BGH, Urteil vom 11. Februar 2014,
X ZR 107/12, GRUR 2014, 542, Rn. 32) weisen sowohl die Problembeschreibung,
als auch die Ausführungsbeispiele einen konkreten Bezug zur Ausgestaltung auf,

                                            - 32 -


dass   die      Nutz-   und   die    Steuerdaten        in   einem    Zeitmultiplexverfahren
zusammengefasst und im selben Rahmen übertragen werden. Nur aufgrund dieser
gemeinsamen Übertragung in einem Rahmen entsteht erst das Problem, dass
Steuerkanalressourcen bei günstigen Übertragungsbedingungen verschwendet
werden (vgl. K2, Absatz [0008] und Fig. 3). Dadurch ist aber auch ersichtlich, dass
sich dieses Problem der verschwendeten Ressourcen, die bei günstigen
Übertragungsbedingungen für die Übertragung zusätzlicher Nutzdaten genutzt
werden sollen, bei einer getrennten Übertragung der Steuer- und Nutzdatenkanäle
erst gar nicht stellt. Damit trägt auch nur die Wahl eines gemultiplexten Kanals zur
Lösung des gestellten technischen Problems bei und ist für diese Lösung auch
erforderlich.


4.2.   In der erteilten Fassung ist das Streitpatent auch deshalb für nichtig zu
erklären, weil es nach Artikel II § 6 Abs. 1 Satz 1 Nr. 1 IntPatÜG, Artikel 138
Abs. 1 lit. a) EPÜ nicht patentfähig ist.


Die Druckschrift R1-070777 (K13) ist ein Standardisierungsbeitrag und befasst sich
mit dem Multiplexen von Steuersignalen mit Aufwärtsverbindungsdaten und stellt
ein Multiplexverfahren vor, das auf der Punktierung von Daten basiert (vgl. K13,
Kapitel 1). In der Praxis ist das Multiplexen der Steuersignalisierung mit
Aufwärtsverbindungsdaten            aufgrund     der         unterschiedlichen   Leistungsanforderungen zwischen Nutzdaten und Steuerdaten eine Herausforderung
(vgl. Kap. 2). Um die Einzelträgereigenschaft der Aufwärtsstreckenübertragung zu
erhalten, muss die Steuersignalisierung vor der diskreten Fourier-Transformation
(DFT) mit Daten gemultiplext werden. Dies kann dadurch erreicht werden, dass
Aufwärtsverbindungsdaten        gleichmäßig          punktiert   werden,   um    Raum    für
Steuersignalisierung zu schaffen (vgl. Kapitel 3, 1. Absatz). Da sowohl die Steuerals auch die Nutz-Daten mit der gleichen Leistung übertragen werden müssen, kann
ein zuverlässiger Empfang der Steuerinformationen durch geeignete Auswahl der
Modulation und Codierung erreicht werden. Dazu wird eine Codewort-Zuordnung
(„codeword mapping“), eine Wiederholung (falls erforderlich) und die Modulation
entsprechend den Informationen über den Kanal durchgeführt.

                                       - 33 -


Diese Auswahl kann an das MCS des Datenblocks gebunden werden, um die
Decodierung zu unterstützen (vgl. Seite 2, vorletzter Absatz: „this selection can be
tied to the MCS of the data block“).


Die Codewort-Zuordnung („codeword mapping“) für die Steuersignale kann auf zwei
Arten erfolgen. Im ersten Fall werden alle Steuerfelder wie CQI, ACK, MIMO, wie in
der Figur 3 gezeigt, in ein einziges Codewort abgebildet, d.h., gemeinsam codiert.




                                  Figur 3 der K13


Mit diesem Ansatz kann es jedoch schwierig sein, die Leistungsanforderungen
verschiedener Steuerfelder zu erfüllen. Außerdem ist der Overhead höher (vgl.
Seite 2, letzter Absatz).


Daher wird im zweiten Fall jedes Steuerfeld (z.B. CQI, ACK) individuell einem
Codewort mit einem eigenen Wiederholungsfaktor („repetition factor“) zugeordnet,
wie in Figur 4 dargestellt. Dieses ermöglicht mithilfe unterschiedlicher Codierung
und Wiederholung eine individuelle Anpassung der Sendeenergie, sodass die
Leistung jedes Steuerfelds gesteuert werden kann (vgl. Seite 3, erster Absatz).




                                  Figur 4 der K13

                                       - 34 -


Da die Steuerdaten vor der diskreten Fourier-Transformation (DFT) mit Nutzdaten
gemultiplext werden, ist für einen zuverlässigen Empfang eine geeignete
Modulations- und Codierungsauswahl für die Steuerdaten erforderlich (vgl. S. 3, 2.
Absatz: „modulation and coding selection for control“). Infolgedessen ist die Menge
der zu punktierenden codierten Daten auf der Grundlage des für die Steuerdaten
ausgewählten MCS variabel (vgl. Seite 3, zweiter Absatz).


Damit offenbart die Druckschrift K13 mit den Worten des erteilten Anspruchs 1


1. A radio transmission apparatus (vgl. K13, Kapitel 1: “UE”) comprising:
  1.1 a coding unit configured to code (“codeword mapping, repetition”) control
        data (vgl. Fig. 4: “CQI, …, ACK”) using a MCS for a data channel (“MCS of
        the data block”) and a scaling factor (“repetition factor”) (vgl. Seite 2,
        vorletzter Absatz: “Subsequent to codeword mapping, repetition (if
        necessary) and modulation selection are performed according to
        information about the channel. Obviously, this selection can be tied to the
        MCS of the data block to aid in the decoding.” Für den Fachmann ist dabei
        selbstverständlich, dass ein UE eine entsprechende Codiereinheit
        aufweist.); and
  1.2 a transmitting unit configured to transmit data in the data channel and the
        control data (vgl. Kapitel 3, 1. Absatz: “To preserve the single-carrier
        property of uplink transmission, L1/L2 control signalling must be multiplexed
        with data prior to the DFT when both data and control are to be transmitted
        in the same TTI.” Für den Fachmann ist dabei auch selbstverständlich, dass
        ein UE eine entsprechende Sendeeinheit aufweist.)
        characterized in that
        1.1.1   the scaling factor (“repetition factor”) is set for each form of the
                control data (vgl. Fig. 4: “CQI, …, ACK”) (vgl. Seite 3, 1. Absatz:
                “each control field is individually mapped to a codeword with its own
                repetition factor as shown in Figure 4”), and
        1.1.2   the control data is coded with a coding rate (vgl. Seite 3, 1. Absatz
                und Fig. 4: „using different coding and repetition“) depending on the
                form of the control data (vgl. Fig. 4: “CQI, …, ACK”).

                                           - 35 -




Aus der Druckschrift K13 ist somit eine Funk-Sendevorrichtung mit sämtlichen
Merkmalen des erteilten Anspruchs 1 bekannt, die daher wegen fehlender Neuheit
(Artikel 54 EPÜ) nicht patentfähig ist.


Die Beklagte argumentiert, dass der „Wiederholungsfaktor“ lediglich angebe, wie oft
ein entsprechendes Codewort wiederholt werden solle und dieses nicht das
Geringste mit einer Skalierung bzw. Umskalierung mittels eines Skalierfaktors zu
tun habe, d.h. einer Multiplikation einer gegebenen Skala mit einem multiplikativen
Faktor zur einfachen Veränderung einer gegebenen Grundskala. Während nach
dem Prinzip des Streitpatents eine einzige Rechenoperation (d.h. eine
Multiplikation) genüge, um eine variable und flexible Einstellung der Steuerdaten-MCS zu vollziehen, erfordere das System der K13 eine Vielzahl von
Repetiereinheiten, in welchen jeweils dezidiert und einzeln ein Repetierfaktor
eingestellt werden müsse. Dies verlange eine entsprechende Entscheidungs- und
Einstellungslogik,    die     wesentlich     komplexer      sei   als    die   einfache
Multiplikationsoperation des Streitpatents. Zudem enthalte das spezielle Konzept
der K13 keinerlei Hinweis auf einen Mechanismus, bei dem mittels eines
steuerdatenformabhängigen        Skalierfaktors     eine   variable   Anpassung   einer
Steuerdaten-MCS an eine gegebene Nutzdatenkanal-MCS stattfinden könne.


Dieses überzeugt den Senat nicht, denn der erteilte Anspruch 1 setzt nicht voraus,
dass eine gegebene Skala, wie z.B. eine CQI-Skala oder ein Wert dieser Skala mit
einem Faktor multipliziert wird. Beansprucht wird lediglich ein Skalierfaktor, der für
jeden Steuerdatentyp festgelegt wird, so dass die Codierrate der Steuerdaten
jeweils von deren Typ abhängt. Dieses erfüllt der Wiederholungsfaktor der K13, der
für jeden Steuerdatentyp (z.B. CQI, ACK) festgelegt wird (vgl. K13, Seite 3, erster
Absatz: „In this case, each control field is individually mapped to a codeword with
its own repetition factor as shown in Figure 4“). Dieser Wiederholungsfaktor skaliert
auch die Codierrate, denn der Wiederholungsfaktor multipliziert das Codewort, so
dass dieselbe Steuerinformation mit einer entsprechend multiplizierten Anzahl an
Bits übertragen wird, also das Verhältnis von Eingangsbits zu Ausgangsbits
(Codierrate) skaliert wird.

                                         - 36 -




Darüber hinaus verlangt der erteilte Anspruch 1 auch keine variable Anpassung
eines Steuerdaten-MCS an ein gegebenes Datenkanal-MCS, sondern lediglich die
Verwendung eines Datenkanal-MCS und eines Skalierfaktors für die Codierung der
Steuerdaten. Weder ein Steuerdaten-MCS, noch eine variable Anpassung sind im
Anspruch 1 genannt.


Weiterhin ist unerheblich, ob die Lehre der K13 „komplexer“ ist, da sie alle Merkmale
des Gegenstands des Anspruchs 1 offenbart.


Der Gegenstand des Anspruchs 1 in der erteilten Fassung ist daher in der K13
neuheitsschädlich vorweggenommen.




5.     Die Verteidigung des Streitpatents in der Fassung der Hilfsanträge 1 bis 11
führt ebenfalls nicht zum Erfolg.


5.1.   Da der Anspruch 1 des Streitpatents in den Fassungen der Hilfsanträge 1
bis 10 jeweils das Merkmal CQI (vgl. Kap. 4.1.2.) und eine am CQI ansetzende
Skalierung (vgl. Kap. 4.1.3.), sowie überdies in den Fassungen nach den
Hilfsanträgen 1 und 6 einen gemultiplexten Kanal (vgl. Kap. 4.1.5.) nicht enthält,
kann die Beklagte das Streitpatent auch nicht in den Fassungen nach den
Hilfsanträgen 1 bis 10 in zulässiger Weise beschränkt verteidigen, da die damit
verteidigten Gegenstände in den ursprünglich eingereichten Unterlagen nicht
offenbart sind.


5.2.   Die Verteidigung des Streitpatents mit den Hilfsanträgen 3 bis 5 und 8
bis 11 ist ebenfalls wegen Erweiterung des Schutzbereichs unzulässig.


Der Anspruch 1 des erteilten Patents ist auf eine Codiereinheit gerichtet, die so
konfiguriert ist, dass sie Steuerdaten unter Verwendung eines MCS für einen
Datenkanal codiert (vgl. Merkmal 1.1).

                                           - 37 -


Da das Teilmerkmal „MCS for a data channel“ jeweils im Anspruch 1 der
Hilfsanträge 3 bis 5 und 8 bis 11 gestrichen ist, ist der Schutzbereich der jeweiligen
Gegenstände gegenüber der erteilten Fassung erweitert.




6.       Zum Hilfsantrag 11a


Demgegenüber kann die Beklagte das Streitpatent erfolgreich mit der Fassung nach
Hilfsantrag 11a verteidigen, weil diese Fassung zulässig ist, insbesondere keine
unzulässige Erweiterung der ursprungsoffenbarten Erfindung enthält und neu, nicht
nahegelegt und damit patentfähig ist.


6.1.     Der mit einer Gliederung versehenen Anspruch 1 gemäß Hilfsantrag 11a
unterscheidet sich von dem erteilten Anspruch 1 (Hauptantrag) durch die mittels
Unter- und Durchstreichungen gekennzeichneten Änderungen:


1. A radio transmission apparatus comprising:
       1.1’’’ a coding unit (108, 110) configured to code control data using a MCS for
             a data channel and a MCS indicator for a data channel, which is a CQI,
             and by multiplying the CQI by a decimal scaling factor,
             1.1.3    and to switch associations between the MCS indicator for the
                      data channel and modulation and coding schemes for the control
                      data according to the kind of control data to determine the
                      modulation and coding scheme of the control data based on the
                      association after the switching; and
       1.2   a transmitting unit (114) configured to transmit data in the data channel
             and the control data
             1.2.1    as multiplexed transmission data,
             characterized in that
             1.1.1’   the scaling factor is set for each formkind of the control data,
             1.1.4    the modulation and coding scheme of the control data is
                      determined based on a new CQI found by multiplying by the
                      scaling factor the MCS indicator for the data channel,

                                          - 38 -


             1.1.2’   and the control data is coded with a coding rate depending on
                      the formkind of the control data.


6.2.   Der Nichtigkeitsgrund der unzulässigen Erweiterung nach Artikel II § 6 Abs. 1
Satz 1 Nr. 3 PatG, Artikel 138 Buchst. c) liegt bei der Fassung nach Hilfsantrag 11a
nicht vor.


Die Merkmale des Gegenstands des Anspruchs 1 nach Hilfsantrag 11a gehen in
zulässiger Weise auf die ursprünglichen Anmeldeunterlagen, veröffentlicht als
EP 2 228 933 A1 (K2), zurück.


Der Anspruch 1 des Hilfsantrags 11a basiert auf der Figur 6 der K2, die eine Funk-Sendevorrichtung (vgl. Abs. [0015]: „radio communication terminal apparatus“;
Merkmal 1.) mit einer Codiereinheit (vgl. Abs. [0021]: „MCS selection section 108“
und „coding and modulation section 110“; Merkmal 1.1‘‘‘teilweise) und einer
Sendeeinheit (vgl. Abs. [0027]: „radio transmitting section 114“; Merkmal 1.2teilweise)
offenbart.


Der Fachmann entnimmt der ursprünglichen Anmeldung, dass die Codiereinheit
(108, 110) Steuerdaten codiert (vgl. Abs. [0023]: „Coding and modulation section
110 encodes and modulates control data“). Diese Codierung erfolgt unter
Verwendung eines CQI (vgl. Abs. [0021]: „CQI information outputted from decoding
section 107“ und Fig. 6, 10), der auch ein MCS für einen Datenkanal angibt (vgl. K2,
Abs. [0021], [0029]: „Based on a CQI received as input, MCS determination section
202 determines MCS 1 for the data channel“), und den der Fachmann somit als
MCS-Indikator für einen Datenkanal versteht. Darüber hinaus offenbart die
ursprüngliche Anmeldung in der Gleichung (2) auch die Multiplikation des CQI mit
einem dezimalen Skalierfaktor „N“ (vgl. K2, Abs. [0042]: “where N is a decimal”)
(Merkmal 1.1‘‘‘).


Der Skalierungsfaktor wird dabei für jede Art von Steuerdaten festgelegt (vgl. K2,
Abs. [0043]: „apply a case where a coding scheme varies like between an uplink

                                         - 39 -


CQI channel and ACK/NACK channels used in LTE, by changing the value, N“)
(Merkmal 1.1.1’).


Der Gleichung (2) der K2 ist auch zu entnehmen, dass die Codiereinheit die
Zuordnung zwischen dem MCS-Indikator für den Datenkanal (vgl. Gleichung (2)
rechts: „CQI“) und Modulations- und Codierungsschemata für die Steuerdaten (vgl.
Gleichung (2) links: „control channel CQI“) gemäß der Art der Steuerdaten wechselt
(vgl. Abs. [0043]: „apply a case where a coding scheme varies like between an
uplink CQI channel and ACK/NACK channels used in LTE, by changing the value,
N“), um das Modulations- und Codierungsschema der Steuerdaten basierend auf
der Zuordnung nach dem Umschalten zu bestimmen (vgl. Abs. [0044]: „to calculate
the new control channel CQI and to determine the MCS for the control channel“)
(Merkmal 1.1.3).


Das Modulations- und Codierungsschema der Steuerdaten wird basierend auf
einem neuen CQI bestimmt (vgl. K2, Abs. [0044]: „to calculate the new control
channel CQI and to determine the MCS for the control channel“), der durch
Multiplizieren des MCS-Indikators für den Datenkanal (vgl. Gleichung (2) rechts:
„CQI“) mit dem Skalierungsfaktor (vgl. Gleichung (2) rechts: „N“) gefunden wird
(Merkmal 1.1.4), und die Steuerdaten werden mit einer Codierungsrate in
Abhängigkeit von der Art der Steuerdaten codiert (vgl. Abs. [0043]: „where a coding
scheme varies like between an uplink CQI channel and ACK/NACK channels used
in LTE, by changing the value, N, a control channel is applicable to different coding
schemes“) (Merkmal 1.1.2‘).


Der ursprünglichen Anmeldung ist auch zu entnehmen, dass die Sendeeinheit (vgl.
Abs. [0027]: „radio transmitting section 114“; Merkmal 1.2teilweise) konfiguriert ist, um
Daten in dem Datenkanal und die Steuerdaten als gemultiplexte Übertragungsdaten
zu übertragen (vgl. K2, Abs. [0024]: „Channel multiplexing section 111 performs
time-division multiplexing of the transmission data for the data channel outputted
from coding and modulation section 109 and the transmission data for the control
channel outputted from coding and modulation section 110“, Abs. [0027]: „ Radio
transmitting section 114 frequency-converts the baseband signal outputted from CP

                                        - 40 -


addition section 113 to a radio frequency band signal, and transmits the converted
signal via antenna 101“ und Fig. 6) (Merkmale 1.2, 1.2.1).


Der Einwand der Klägerinnen, wonach im Ausführungsbeispiel 3 der ursprünglichen
Anmeldung, das auf dem Ausführungsbeispiel 2 basiere, auch ein Offset-Wert
angewendet werde, der als wesentliches Element im Anspruch 1 nicht weggelassen
werden könne, vermag nicht zu greifen. Denn der ursprünglichen Anmeldung ist
zum einen zu entnehmen, dass der Offset bei verschiedenen Bedingungen Null sein
kann (vgl. K2, Abs. [0036]: „when the data channel scheduling method is dynamic
scheduling, the offset is zero“, Abs. [0037]: „the offset is zero when the data channel
is used with frequency hopping“, sowie Abs. [0038]: „the offset is zero when a data
channel transmission is the first“), so dass in diesen Fällen nur der Skalierfaktor den
CQI beeinflusst. Zum anderen kann aber auch der Skalierfaktor auf den Wert 1
gesetzt werden (vgl. K2, Abs. [0043]: „N=1“), so dass sich nur noch eine Offset-Abhängigkeit ergibt. Somit entnimmt der Fachmann der ursprünglichen Anmeldung,
dass das Offset- und das Skalierungs-Konzept auch voneinander unabhängig
anwendbar sind.


6.3.   Der Anspruch 1 in der Fassung nach Hilfsantrag 11a schränkt den
Gegenstand des Anspruchs 1 erteilter Fassung durch die zusätzlichen
Merkmalsteile der Merkmale 1.1‘‘‘, 1.1.3, 1.1.4 und 1.2.1 in zulässiger Weise ein, so
dass der Schutzbereich gegenüber der erteilten Fassung nicht erweitert ist.


6.4.   Der Zeitrang des Patents im Umfang des Hilfsantrags 11a ist der der
Prioritätsanmeldung JP 2008-000199, also der 4. Januar 2008.


6.5.   Der Gegenstand des Anspruchs 1 des Hilfsantrags 11a wird durch den im
Verfahren    befindlichen    Stand     der       Technik   weder    neuheitsschädlich
vorweggenommen, noch dem Fachmann nahegelegt.


6.5.1. Die Druckschrift K13 offenbart zwar ein Multiplexen von Daten und
Steuerdaten (vgl. Titel: „Multiplexing of Uplink Control Signaling with Data“ und
Figur 4; Merkmal 1.2.1), sowie die Merkmale 1.1.1‘ und 1.1.2‘, jedoch sind der K13

                                      - 41 -


weder ein MCS-Indikator für einen Datenkanal, der ein CQI ist, noch eine
Multiplikation dieses CQI mit einem dezimalen Skalierungsfaktor, im Sinne des
Merkmals 1.1‘‘‘, noch die Merkmale 1.1.3 und 1.1.4 zu entnehmen.


Für den Fachmann gibt es aus der K13 insbesondere auch keine Veranlassung,
das MCS der Steuerdaten basierend auf einem neuen CQI zu bestimmen, der durch
Multiplizieren eines MCS-Indikators für den Datenkanal mit dem Skalierungsfaktor
ermittelt wird.


6.5.2. Die K6/K6a (WO 2006/134946 A1 / EP 1 892 987 A1) offenbart einen Sender
(„transmitter“) zur Übertragung von Nutzdaten eines Datenkanals („shared data
channel“) und Steuerdaten eines Steuerkanals („shared control channel“). Die Nutzund Steuerdaten der Kanäle werden mittels Zeitmultiplexverfahren („multiplexing
portion 235“) gebündelt (vgl. K6a, Abs. [0086] und Fig. 23). Bei den Steuerdaten
des Steuerkanals handelt es sich beispielsweise um ACK/NACK, CQI oder
Informationen zum Ändern des scheduling (vgl. Abs. [0102] und Fig. 25).




                          Figur 25 der Druckschrift K6a

                                        - 42 -


Die Steuerdaten jedes Steuerkanals bzw. jeder Steuerdatenart (ACK/NACK, CQI,
SCHEDULING REQUEST INFO) werden jeweils einer eigenen Modulations- und
Codiereinheit zugeführt (vgl. Abs. [0103]: „Each of the modulating and coding
portions 255, 256, 257, 258 modulates the channel input to the modulating and
coding portion by a selected modulating method and encodes the modulated
channel by a selected coding method“, sowie Fig. 25). Dabei benötigen die
ACK/NACK 1 Bit, die CQI 5 Bit und die Informationen zum Ändern des scheduling
10 Bit für die Übertragung (vgl. Abs. [0056], Sp. 13, Z. 27-30). Die MCS Nummern
für den Steuerkanal können den MCS Nummern des Datenkanals entsprechen (vgl.
Spalte 26, Zeilen 14-17: „The MCS numbers may be the same as the numbers used
for the shared data channels, or may be prepared separately from the MCS numbers
for the shared control channels“). Für einen Steuerkanal wird abhängig von der
Anzahl der Steuerbits, die abhängig von der Art der Steuerdaten ist, eine große oder
eine kleine MCS-Zahl und damit eine große oder eine kleine Codierungsrate
verwendet (vgl. Abs. [0106], Sp. 26, Z. 32-42). Somit ist das Modulations- und
Codierungsverfahren in jedem Kanal (ACK/NACK, CQI, scheduling request info)
unterschiedlich (vgl. Abs. [0103] und Fig. 25).


Daher offenbart die K6/K6a mit den Worten des Anspruchs 1 nach Hilfsantrag 11a


1. A radio transmission apparatus (vgl. Abs. [0086]: “transmitter”) comprising:
    1.1’’’teils a coding unit (vgl. Abs. [0102]: “modulating and coding portions 255,
             256, 257, 258” und Fig. 25) configured to code control data using a
             MCS for a data channel and a MCS indicator for a data channel (vgl.
             K6a, Abs. [0106], Sp. 26, Z. 13: „a Modulation and Coding Scheme
             (MCS) number“; Z. 14-16: “The MCS numbers may be the same as
             the numbers used for the shared data channels”), which is a CQI (vgl.
             Abs. [0117]: “Or, the CQI measured at the base station may be
             provided to the mobile station”), and by multiplying the CQI by a
             decimal scaling factor,
             1.1.3    and to switch associations between the MCS indicator for the
                      data channel and modulation and coding schemes for the
                      control data according to the kind of control data to determine

                                 - 43 -


               the modulation and coding scheme of the control data based
               on the association after the switching (In der K6a wird für den
               „shared control channel“ abhängig von der Anzahl der
               Steuerbits, die abhängig von der Art der Steuerdaten ist
               (ACK/NACK 1 Bit, CQI 5 Bit und Buffergröße & Leistung
               beispielsweise 10 Bit) eine große oder eine kleine MCS-Zahl
               und damit eine große oder eine kleine Codierungsrate
               verwendet (vgl. Abs. [0106], Sp. 26, Z. 32-42). Damit ist die
               Codiereinheit   der   K6a    eingerichtet,   die   Zuordnungen
               zwischen dem MCS-Indikator für den Datenkanal (vgl. Abs.
               [0110]: „… (MCS number) are provided through the downlink
               shared control channel to the mobile station“) und MCS für die
               Steuerdaten (vgl. Abs. [0106]: „MCS number to be employed
               for the shared control channel“) gemäß der Art der
               Steuerdaten (vgl. Abs. [0056]: ACK/NACK , CQI, buffer size &
               power) zu wechseln, um das MCS der Steuerdaten basierend
               auf der Zuordnung nach dem Wechsel zu bestimmen (vgl.
               Abs. [0106]: large number of bits - large MCS number, small
               number of bits - small MCS number”); and
1.2   a transmitting unit configured to transmit data in the data channel and
      the control data (vgl. Abs. [0101]: “Subsequently, the signals are
      transmitted through an element corresponding to the RF portion 14 in
      FIG. 1.” und Fig. 23)
      1.2.1    as multiplexed transmission data (vgl. Abs. [0086], [0090]:
               „The multiplexing portion 235 multiplexes one or more
               channels“ und Fig. 23),
      characterized in that
      1.1.1’   the scaling factor is set for each kind of the control data,
      1.1.4    the modulation and coding scheme of the control data is
               determined based on a new CQI found by multiplying by the
               scaling factor the MCS indicator for the data channel,
      1.1.2’   and the control data is coded with a coding rate depending on
               the kind of the control data (vgl. Sp. 13, Z. 27-30: „The control

                                       - 44 -


                     information indicates whether a packet is appropriately
                     received (ACK) or not (NACK) in downlink, and is expressed
                     by one bit in the simplest case“; Sp. 13, Z. 48-55: „The CQI
                     may be a received signal-to-interference power ratio (SIR)
                     measured by the mobile station, for example. … This control
                     information may be expressed by an information amount of 5
                     bits, for example“; Sp. 13, Z. 31-43: “The buffer size and the
                     transmission power may be expressed by an information
                     amount of 10 bits, for example”; Sp. 26, Z. 35-42: „Namely,
                     when a large number of control bits has to be transmitted, a
                     large MCS number (a large number of modulation level values
                     (modulation orders), a large channel coding rate) may be
                     employed. In addition, when only a small number of control
                     bits is required, a small MCS number (a small number of
                     modulation level values (modulation orders), a small channel
                     coding rate) may be employed”).


Der Druckschrift K6/K6a ist somit nicht zu entnehmen, dass die Steuerdaten unter
Verwendung eines dezimalen Skalierfaktors codiert werden, der mit dem CQI
multipliziert wird (Merkmal 1.1rest), dass dieser Skalierfaktor für jede Art der
Steuerdaten festgelegt wird (Merkmal 1.1.1‘) und dass das Modulations- und
Codierungsschema der Steuerdaten basierend auf einem neuen CQI bestimmt
wird, der durch Multiplizieren des MCS-Indikators für den Datenkanal mit dem
Skalierungsfaktor ermittelt wird (Merkmal 1.1.4).


Die Klägerinnen sind der Auffassung, dass durch die Auswahl einer Zeile in der
Tabelle von Fig. 27 der K6/K6a für ACK/NACK und die Auswahl einer anderen Zeile
für CQI die Steuerdaten mit unterschiedlichen Codierraten (z.B. 1/3 für MCS1 und
2/3 für MCS3) codiert würden, wobei die Codierrate für MCS3 doppelt so groß sei
wie die für MCS1. Somit seien die Codierraten für verschiedene Steuerdaten skaliert
und die Codierung von Steuerdaten erfolge unter Verwendung eines Skalierfaktors,
der die Codierrate beeinflusse und für jede Art der Steuerdaten festgelegt sei.
Entsprechend könne auch die Datenmodulation der Figur 27 dargestellt werden.

                                        - 45 -




Dem kann nicht zugestimmt werden. Denn der Druckschrift K6/K6a ist, wie auch
von den Klägerinnen dargelegt, nur zu entnehmen, dass einzelne Zeilen der
Figur 27 ausgewählt werden. Dabei mögen auch die Kanalcodierungsfaktoren
(„channel coding factor“) der ersten und der dritten Zeile der Figur 27 oder die
benötigte Anzahl an Symbolen der Datenmodulation („data modulation“) der ersten
und der vierten Zeile der Figur 27 zueinander in einem Verhältnis stehen, doch ist
der   gesamten    Druckschrift   NK27     weder    explizit   ein   Skalierfaktor   der
Kanalcodierungsfaktoren oder der Datenmodulation zu entnehmen, noch, dass
solch einer für jede Art der Steuerdaten festgelegt ist und mit dem CQI (vgl. in Figur
27 die Spalte „MCS number“) multipliziert wird.


Auch wenn die K6a dem Fachmann nahelegt, abhängig von der Art und damit der
Größe der Steuerdaten (ACK/NACK 1 Bit, CQI 5 Bit und Buffergröße & Leistung
beispielsweise 10 Bit) eine große oder eine kleine MCS-Zahl und damit eine große
oder eine kleine Codierungsrate zu verwenden, gibt es für den Fachmann aus der
K6a keine Veranlassung, das MCS der Steuerdaten basierend auf einem neuen
CQI zu bestimmen, der durch Multiplizieren des MCS-Indikators für den Datenkanal
mit einem Skalierungsfaktor ermittelt wird.


Die Klägerinnen verweisen zwar auf die in der Figur 27 der K6a offenbarten
Kanalcodierfaktoren (1/3, 1/2, 2/3, …). Der K6a ist jedoch kein Hinweis zu
entnehmen, diese Kanalcodierfaktoren mit den ebenfalls in der Figur 27 offenbarten
MCS Nummern (MCS1, MCS2, MCS3, …) zu multiplizieren.


Der Gegenstand des Anspruchs 1 des Hilfsantrags 11a ist dem Fachmann somit
auch nicht aus der Druckschrift K6/K6a nahegelegt.


6.5.3. Die Druckschrift GDM-5 (3GPP TS 36.212 V8.0.0 (2007-09)) offenbart weder
einen MCS-Indikator für einen Datenkanal der ein CQI ist, noch eine Multiplikation
dieses CQI mit einem dezimalen Skalierungsfaktor, im Sinne des Merkmals 1.1‘‘‘,
noch die Merkmale 1.1.1‘, 1.1.3 und 1.1.4.

                                        - 46 -


Die Klägerinnen verweisen auf die Seite 21 der GDM-5, die im Kapitel 5.2.2.6
offenbare, dass unterschiedliche Codierungsraten für die Steuerinformation erreicht
würden, indem eine unterschiedliche Anzahl von codierten Symbolen für ihre
Übertragung zugewiesen werde („Different coding rates for the control information
are achieved by allocating different number of coded symbols for its transmission“).
Die Anzahl codierter Symbole ließe sich durch eine natürliche Zahl ausdrücken. Es
gäbe also eine erste natürliche Zahl für die Anzahl codierter Symbole der ersten
Form von Steuerdaten sowie eine zweite natürliche Zahl für die Anzahl codierter
Symbole der zweiten Form von Steuerdaten. Zwei natürliche Zahlen stünden in
einem Verhältnis zueinander, das eindeutig definiert sei durch einen „multiplikativen
Faktor". Dieser multiplikative Faktor nehme einen Skalierfaktor vorweg.


Diese Argumentation konnte nicht überzeugen, denn der Druckschrift GDM-5 ist nur
zu entnehmen, dass eine unterschiedliche Anzahl von codierten Symbolen zu
unterschiedlichen Codierraten der Steuerinformation führt, wobei für die CQI, ACK
und CQI&ACK insgesamt drei Arten der Kanalcodierung verwendet werden (vgl.
GDM-5, Kap. 5.2.2.6, 5.2.3). Dabei wird weder ein Skalierfaktor offenbart oder
nahegelegt, noch, dass die Anzahl von codierten Symbolen in einem Verhältnis
zueinanderstehen, dass, z.B. multiplikativ, beeinflusst wird.


6.5.4. Da die Priorität des Streitpatents zu Recht in Anspruch genommen ist, ist die
Druckschrift GDM-6 (EP 1 953 943 A2), deren Prioritätsdatum vor dem Prioritätstag
des Streitpatents liegt, nur für die Neuheitsprüfung nach Art. 54 (3) EPÜ relevant.


Die Verwendung eines MCS für einen Datenkanal zur Codierung der Steuerdaten
dürfte der GDM-6 zwar zu entnehmen sein. Denn im Absatz [0022] ist offenbart,
dass die Basisstation den Übertragungsparameter sendet, der Folgendes umfasst:
Modulationsverfahren (Mod_tx) wie BPSK, QPSK, 16QAM usw., Bandbreite (N_tx),
PUSCH-Übertragungsleistungswert (P_tx) von der Mobilstation zu der drahtlosen
Basisstation und die Codierungsraten des Datensignals und des Steuersignals.
Somit wird nur ein Modulationsverfahren für das Daten- und das Steuersignal
gesendet, so dass dieser Parameter des MCS für einen Datenkanal auch zur
Codierung der Steuerdaten verwendet wird.

                                       - 47 -




Jedoch gibt es in der GDM-6 insbesondere keinen Hinweis auf einen Skalierfaktor,
der gemäß Merkmal 1.1.1‘ für jeden Typ der Steuerdaten festgelegt wird.


Die Nichtigkeitsklägerinnen verweisen diesbezüglich auf die Datensignalgröße
(DBS) vor der Codierung und dem Ratenabgleich (vgl. GDM-6, Abs. [0030]: „the
mobile station can calculate the data signal size (DBS) before coding and rate
matching“). Mit der Übertragungsdatengröße (transmission data size TxBS) kann
eine temporäre Codierungsrate (DBS/TxBS) berechnet werden (vgl. Abs. [0037]),
und aus diesem Quotienten mittels einer Tabelle eine Codierungsrate (Rctrl_m)
jedes Steuersignals m gefunden werden (vgl. Abs. [0044]: „FIG. 5 shows an
example of a table used to find the coding rate (Rctrl_m) of each control signal m
based on the temporary coding rate (DBS/TxBS) that is calculated from the data
signal size (DBS) before coding and rate matching and the transmission data size
(TxBS)”).


Bei der Datensignalgröße (DBS) handelt es sich allerdings um keinen festgelegten
Skalierfaktor, sondern nur um die Größe des Datensignals. Diese ist auch nicht als
abhängig von dem Typ der Steuerdaten beschrieben.


Dementsprechend sind der GDM-6 weder eine Multiplikation eines CQI mit einem
dezimalen Skalierfaktor im Sinne des Merkmals 1.1‘‘‘, noch die Merkmale 1.1.3 und
1.1.4 zu entnehmen.


6.5.5. Der Druckschrift GDM-7 (US 2007/0076677 A1) ist zwar zu entnehmen, dass
Steuerdaten mit einer Codierrate (Codierschemata) codiert werden, die von dem
Typ der Steuerdaten abhängt (vgl. Absatz [0021]: „During operation, base station
104 will group remote units 101-103 based on their received signal quality. Transmit
power and encoding schemes for control information are allowed to vary for each
group of remote units 101-103 and for different type of control information“)
(Merkmal 1.1.2’). Darüber hinaus kann auch eine Gruppierung anhand eines Typs
(kritisch/nicht-kritisch) der Steuernachrichten erfolgen (vgl. Absatz [0032]: „In a
similar manner, more critical messages may be in groups having lower index

                                         - 48 -


numbers than non-critical messages“). Die unterschiedlichen Gruppen werden mit
unterschiedlicher Codierrate und Wiederholungsfaktor codiert (vgl. Absatz [0034]:
„In other examples two groups may have the same modulation such as QPSK, with
reliability (if different) distinguished by code rate, power level, repetition factor, or
another transmission parameter“). Somit dürfte auch ein Skalierfaktor (repetition
factor) für jeden Typ der Steuerdaten festgelegt werden (Merkmal 1.1.1‘).


Der Druckschrift GDM-7 ist jedoch die Verwendung eines MCS für einen Datenkanal
nicht zu entnehmen. Auch im von den Klägerinnen zitierten Absatz [0019] ist nur
eine Übertragung von Steuerdaten in Abhängigkeit einer Modulation und einer
Codierrate zu entnehmen (vgl. Absatz [0019]: „In one embodiment of the present
invention, control data may also be transmitted with a link quality dependent
modulation and coding rate. Thus, data transmissions with high quality are typically
assigned higher order modulations rates and/or higher channel coding rates with
the modulation order and/or the code rate decreasing as quality decreases.“).


Darüber hinaus offenbart die GDM-7 keinen MCS-Indikator für einen Datenkanal,
der ein CQI ist, keine Multiplikation eines CQI mit dem Skalierfaktor (Teilmerkmale
1.1‘‘‘) sowie auch nicht die Merkmale 1.1.3 und 1.1.4.


6.5.6. Der im Absatz [0005] des Streitpatents genannten Druckschrift K7/K7a (WO
2007/037412 A1 / EP 1 914 948 A1) ist zu entnehmen, dass ein Modulations- und
Codierschema für einen Steuerkanal aus einem CQI und einem CQI-Offset
bestimmt werden können (vgl. K7a, Absätze [0060]-[0063]). Dieser Offset wird
jedoch für den Steuerinformationskanal als Ganzes und nicht für jeden Typ der
Steuerdaten festgelegt (vgl. K7a, Absatz [0011]: „The radio transmitting apparatus
of the present invention determines an MCS of the transmission signal based on a
CQI reported from a communicating party and adopts a configuration including: a
determining section that determines an MCS for a data channel based on the CQI
reported from the communicating party and determines an MCS for a control
channel based on the same CQI, and a transmitting section that transmits the
transmission signal including the data channel and the control channel”).

                                      - 49 -


Die Klägerinnen verweisen auf den Absatz [0030] der K7a, nach dem für einen CQI
die Werte für MCS1 (für den Datenkanal SDCH) und MCS2 (für den
Steuerinformationskanal SCCH) ausgewählt würden. Zunächst würde für jeden CQI
ein MCS-Wert für den Datenkanal SDCH bestimmt werden. Dann würden anhand
dieses MCS-Werts für den SDCH eine durchschnittliche Übertragungsrate A für den
SDCH und weitere Werte B, C, D und E bestimmt. Schließlich würde der Wert des
Ausdrucks „A x (1-C)" mit dem Wert des Ausdrucks „A x (1-D) x (E + B)/B" verglichen
und das MCS für den Steuerkanal SCCH bestimmt. Somit erfolge die Codierung der
Steuerdaten unter Verwendung des MCS-Werts MCS1 für den Datenkanal SDCH
und zwar in Form der aus MCS1 ermittelten durchschnittlichen Datenrate A. In den
Wert E gehe der Unterschied ein zwischen der Anzahl der Symbole des SCCH,
wenn MCS1 verwendet werde, und der Anzahl der Symbole des SCCH, wenn
MCS2 verwendet werde. Somit sei E abhängig von der Anzahl der Symbole, die zur
Codierung der Steuerdaten benötigt würden, also von der Art der Steuerdaten.
Weiterhin bestimme E den Skalierfaktor (E + B)/B, der bei der Auswahl von MCS2
verwendet werde. Folglich erfolge die Codierung der Steuerdaten unter
Verwendung eines Skalierfaktors, der für jede Art der Steuerdaten festgelegt sei.


Diese Argumentation kann jedoch nicht überzeugen, denn in den Absätzen [0029]
bis [0031] der K7a wird nur beschrieben, wie der MCS 1 für den Datenkanal SDCH
und der MCS 2 für den gesamten Steuerinformationskanal SCCH so eingestellt
werden, dass die PAPRs (Peak to Average Power Ratio), das Verhältnis von
Spitzenleistung zur mittleren Leistung des jeweiligen Signals, für den SCCH und
den SDCH innerhalb des Bereichs des angenommenen PAPR bleiben und eine
Übertragungsrate des SCCH und des SDCH maximal wird (vgl. K7a, Absatz [0031]:
„In other words, in CQI look-up table 122, MCS 1 and MCS 2 are set such that the
PAPRs for the SCCH and SDCH remain within the range of the assumed PAPR and
a transmission rate of the SCCH and SDCH becomes a maximum”). Die
Steuerdaten werden somit nicht, wie vom Merkmal 1.1.2‘ gefordert, mit einer
Codierrate codiert, die von der Art der Steuerdaten abhängt, sondern mit einer
Codierrate, die bei einem rechnerischen Vergleich unterschiedlicher MCS, in die
auch die jeweils resultierende Anzahl der Symbole des SCCH eingeht, zu einer
höheren Übertragungsrate führt (vgl. K7a, Abs. [0030]).

                                        - 50 -




Darüber hinaus wird auch kein Skalierfaktor für jeden Typ der Steuerdaten im Sinne
des Merkmals 1.1.1‘ festgelegt, denn die Variable „E“ in der Berechnungsvorschrift
des Absatzes [0030] der K7a beschreibt die Differenz zwischen der Anzahl von
Symbolen des SCCH (MCS 1) und der Anzahl von Symbolen des SCCH (MCS 2),
wenn zwei unterschiedliche Modulation und Codierungsschemata für den gesamten
Steuerkanal verwendet werden. Die Differenz in der Symbolzahl bezieht sich auf
den gesamten Steuerkanal und ist nicht für jeden Steuerdatentyp festgelegt.


Ferner offenbart die K7/K7a auch keine Multiplikation eines CQI mit einem
Skalierfaktor und auch nicht die Merkmale 1.1.3 und 1.1.4. Der Fachmann ist
ausgehend von der K7/K7a auch nicht veranlasst, nach einer entsprechenden
Ausgestaltung im Stand der Technik zu suchen.


6.5.8. Der Druckschrift K8 (R1-073842) ist zu entnehmen, dass für einen gleichen
Verstärkungsfaktor der Steuer- und Nutzdaten (vgl. K8, Kap. 7.2.2: „Same gain
factor for control and data“) unterschiedliche Codierungsraten der Steuerdaten
durch Verwenden einer unterschiedlichen Anzahl von Symbolen erreicht werden.
Die für die Steuersignalisierung zu verwendende Codierungsrate wird dabei vom
PUSCH MCS vorgegeben und die Beziehung in einer Tabelle ausgedrückt. In dieser
Tabelle ist jedes PUSCH-MCS mit einer bestimmten Codierrate für die
Steuersignalisierung verknüpft, d.h. der Anzahl von Symbolen, die für eine
ACK/NAK- oder eine bestimmte CQI/PMI-Größe verwendet werden sollen.
Nutzdaten und die verschiedenen Steuerdatenfelder (ACK/NAK, CQI/PMI) werden
auf separate Modulationssymbole abgebildet, d.h. ein einzelnes Symbol
(QPSK/16QAM/64QAM) kann nicht sowohl Nutzdaten als auch Steuerdaten
enthalten (vgl. K8, Kap. 7.2.2, erste Spiegelstriche).


Das Dokument K8 beschreibt somit lediglich eine Tabelle, in der jedes MCS mit
einer bestimmten Codierrate für die Steuersignalisierung verknüpft ist (vgl. K8, Kap.
7.2.2: „A table links each PUSCH MCS with a given coding rate for control
signalling“). Die Codierrate gibt die Anzahl von Symbolen vor, die für eine
ACK/NAK- oder eine bestimmte CQI/PMI-Größe verwendet werden sollen („the

                                        - 51 -


number of symbols to use for an ACK/NAK or a certain CQI/PMI size“). Somit
werden die Steuerdaten nicht mit einer Codierrate codiert, die von der Art der
Steuerdaten abhängt, sondern mit einer Codierrate, die die Anzahl von Symbolen
für die gesamten Steuerdaten, also für ACK/NACK oder CQI/PMI, vorgibt. Eine Typ-Abhängigkeit, wie von Merkmal 1.1.2‘ definiert, ist somit nicht offenbart.


Darüber hinaus sind der K8 auch kein Skalierfaktor (Merkmale 1.1‘‘‘, 1.1.1‘ und
1.1.4) und auch keine Zuordnung eines CQI zu einem MCS für Steuerdaten im
Sinne des Merkmals 1.1.3 zu entnehmen.


6.5.9. Die Druckschrift K9 (R1-073388) befasst sich mit dem Multiplexen von
Steuer- und Datensignalen. Da die Steuersignale vor der diskreten Fourier-Transformation (DFT) mit Datensignalen gemultiplext werden, ist für einen
zuverlässigen Empfang eine geeignete Modulations- und Codierungsauswahl für
die Steuersignale erforderlich (vgl. Kapitel 1). Aufgrund der unterschiedlichen
Leistungsanforderungen können Steuersignale und Datensignale unterschiedliche
Modulation und Codierung aufweisen, wobei die MCS der Steuerungsfelder vom
Daten-MCS abhängen. Zur Implementierung kann eine Mapping-Tabelle zwischen
Steuerungs- und Daten-MCS definiert werden (vgl. S. 1, letzter Absatz „Control
MCS selection is tied to data MCS“). Um die für die Steuersignale erforderliche
Menge an Uplink-Ressourcen zu minimieren und um sicherzustellen, dass die
Leistungsanforderungen erfüllt werden, sollte jedes Steuerfeld separat codiert
werden (vgl. S. 1, vorletzter Absatz „Separate coding for each control field“ und
Figur 3).


Die Druckschrift K9 offenbart somit eine Funk-Sendevorrichtung („UE“), die eine
Codiereinheit umfasst, die so konfiguriert ist, dass sie Steuerdaten („control“) unter
Verwendung eines MCS für einen Datenkanal „Control MCS selection is tied to data
MCS“ codiert (Merkmale 1 und 1.1‘‘‘teilweise). Die Steuerdaten werden auch mit einer
Codierrate codiert, die vom Typ der Steuerdaten abhängt (vgl. Abschnitt „Separate
coding for each control field“: „each ﬁeld should be separately coded as illustrated
in Figure 3“ und Abschnitt „Symbol level multiplexing“: „control and data multiplexing
is performed at the symbol level to allow different modulation and coding rate

                                        - 52 -


selections“   und    Figur   3)   (Merkmal   1.1.2’).   Der   Fachmann   liest   dabei
selbstverständlich mit, dass das UE eine Sendeeinheit aufweist, die so konfiguriert
ist, dass sie Daten in dem Datenkanal und die Steuerdaten gemultiplexed sendet
(Merkmale 1.2, 1.2.1).


Die Druckschrift K9 offenbart jedoch keinen dezimalen Skalierfaktor, der für jede Art
der Steuerdaten festgelegt und mit einem CQI multipliziert wird (Merkmale 1.1‘‘‘rest,
1.1.1‘ und 1.1.4).


Da die Druckschrift K9 dem Fachmann keine Anregung in Richtung eines
Skalierfaktors gibt, ist der Fachmann ausgehend von der K9 auch nicht veranlasst,
nach einen Skalierfaktor im Stand der Technik zu suchen.


6.5.10. Die im Absatz [0004] des Streitpatents zum Stand der Technik genannte
Druckschrift K20 (R1-073334) offenbart eine aktualisierte CQI-Tabelle, um eine
64QAM-Modulation im HSDPA zu unterstützen (vgl. K20, Kap. 1). Dieser sind CQI-Werte, eine Anzahl von HS-PDSCH Kanälen, Modulationsschemata, alte und neue
Transportblockgrößen, deren Differenz, alte und neue Codierraten und deren
Differenz zu entnehmen (vgl. K20, Kap. 2).


Die K20 offenbart insbesondere keinen Skalierfaktor im Sinne der Merkmale 1.1‘‘‘,
1.1.1‘ und 1.1.4. Darüber hinaus ist der K20 auch keine Abhängigkeit von der Art
der Steuerdaten im Sinne der Merkmale 1.1.1‘, 1.1.2‘ und 1.1.3 zu entnehmen.


6.5.11. Die Druckschriften K18 und K19 sind nicht zu berücksichtigen, da diese erst
nach dem maßgeblichen Prioritätstag der Öffentlichkeit zugänglich waren.


6.5.12. Da keine der Druckschriften des gesamten im Verfahren genannten Standes
der Technik die Merkmale aufweist oder zumindest nahelegen kann, wonach
Steuerdaten unter Verwendung eines dezimalen Skalierfaktors codiert werden, der
mit einem CQI multipliziert wird (Teilmerkmal 1.1), und, dass das Modulations- und
Codierungsschema der Steuerdaten basierend auf einem neuen CQI bestimmt
wird, der durch Multiplizieren des MCS-Indikators für den Datenkanal mit dem

                                       - 53 -


Skalierungsfaktor ermittelt wird (Merkmal 1.1.4), kann auch eine Zusammenschau
des Standes der Technik dies nicht leisten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 11a ist damit dem Fachmann
weder durch einzelne der vorgenannten Druckschriften noch durch deren
Kombination oder unter Einbeziehung seines Fachwissens nahegelegt. Der
Gegenstand des Anspruchs 1 des Hilfsantrags 11a ist somit neu und beruht auf
einer erfinderischen Tätigkeit.


6.6.   Die vorstehenden Ausführungen zu Anspruch 1 nach Hilfsantrag 11a gelten
entsprechend auch für den nebengeordneten Verfahrensanspruch 2.


6.7.   Da sich somit das Streitpatent in der von der Beklagten hilfsweise
verteidigten Fassung nach Hilfsantrag 11a als schutzfähig erweist, war die Klage
insoweit teilweise abzuweisen. Bei diesem Sachstand bedarf es daher keiner
Entscheidung mehr, ob das Streitpatent auch in den Fassungen der Hilfsanträge 12
oder 12a schutzfähig wäre.




                                        III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 92 Abs. 1 Satz 1 Alt. 2, 100 Abs. 1 ZPO.


Dabei hat der Senat berücksichtigt, dass der als schutzfähig verbleibende
Patentgegenstand gegenüber demjenigen der erteilten Fassung eingeschränkt ist.
Diese Einschränkung macht nach der Schätzung des Senats 9/10 der
wirtschaftlichen Verwertbarkeit des Streitpatents aus, da der beschränkte
Gegenstand nicht mehr standardrelevant ist, sodass der Beklagten trotz teilweisem
Fortbestand des Streitpatents in beschränkter Fassung in diesem Umfang die
Kosten des Rechtsstreits aufzuerlegen waren.

                                       - 54 -


Die Klägerinnen haften für die Kosten nach Kopfteilen (§ 84 Abs. 2 Satz 2 Halbsatz
1 PatG i. V. m. § 100 Abs. 1 ZPO). Sind mehrere Klageverfahren, die dasselbe
Patent zum Gegenstand haben, zum Zwecke der gleichzeitigen Verhandlung und
Entscheidung verbunden worden, sind die Kläger notwendige Streitgenossen
gemäß § 62 ZPO (vgl. BGH, Urteil vom 27. Oktober 2015 – X ZR 11/13 -,
Rn. 47 - 49, juris).


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.




                                         IV.


                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils - spätestens nach Ablauf von fünf Monaten nach
Verkündung - durch einen in der Bundesrepublik Deutschland zugelassenen
Rechtsanwalt oder Patentanwalt schriftlich beim Bundesgerichtshof, Herrenstraße
45a, 76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.

                                     - 55 -




Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht     (BGH/BPatGERVV)        auf     elektronischem   Weg   beim
Bundesgerichtshof     einzulegen,   wird      hingewiesen     (www.bundesgerichtshof.de/erv.html).




 Hartlieb       Dr. Friedrich   Dr. Zebisch          Dr. Himmelmann     Dr. Kapels
