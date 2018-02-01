---
ecli: "ECLI:DE:BPatG:2018:010218U2Ni6.16EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 6/16"
decided: "2018-02-01"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2018&Sort=1&Seite=4&nr=37232&anz=825&pos=69&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_LE_2018-02-01_2_Ni_6_16_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0101.md", "germany/bund/acts/zpo/0323.md", "germany/bund/acts/zpo/0325.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 6/16 vom 2018-02-01

## Leitsatz

LE

## Entscheidung

BUNDESPATENTGERICHT

Leitsatz


Aktenzeichen:                       2 Ni 6/16 (EP) verb. m. 2 Ni 48/16 (EP)

Entscheidungsdatum:                 01.02.2018

Rechtsbeschwerde zugelassen:        nein

Normen:                             § 99 Abs. 1 PatG i. V. m. §§ 323, 325 ZPO



„Rechtskraft von Entscheidungen im Patentnichtigkeitsverfahren – res judicata“


Weder die Eigenschaft der Nichtigkeitsklage als Gestaltungsklage noch das Interesse der
Allgemeinheit an Rechtssicherheit betreffend den Bestand von Schutzrechten gebieten für das
Patentnichtigkeitsverfahren eine Abweichung von den allgemeinen Grundsätzen der
materiellen und subjektiven Rechtskraft (§ 99 Abs. 1 PatG i. V. m. §§ 323, 325 ZPO). Die
Rechtskraft einer die Nichtigkeitsklage abweisenden Entscheidung steht daher einer erneuten
auf dieselben Klagegründe gestützten Klage, die von am Vorverfahren nicht Beteiligten
erhoben wird, nicht entgegen.

                                                      Abschrift



                  BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES
2 Ni 6/16 (EP)
verbunden mit                  URTEIL                 Verkündet am
                                                      1. Februar 2018
2 Ni 48/16 (EP)                                            …

(Aktenzeichen)




                     In der Patentnichtigkeitssache

 …




 ECLI:DE:BPatG:2018:010218U2Ni6.16EP.0

                                           -2-



…




                   betreffend das europäische Patent 0 745 307
                                   (DE 695 14 212)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 1. Februar 2018 unter Mitwirkung des Vorsitzenden
Richters Guth sowie der Richterin Dr. Thum-Rung und der Richter Baumgardt,
Heimen und Dr. Forkel


für Recht erkannt:


        I.   Das     europäische        Patent   0   745    307   wird     unter
             Klageabweisung        im     Übrigen    mit   Wirkung   für    das
             Hoheitsgebiet der Bundesrepublik Deutschland dadurch
             teilweise für nichtig erklärt, dass seine Ansprüche folgende
             Fassung erhalten:


             1. A method of transmitting a multiplexed stream comprising
             active video data and encoded data defining a graphic image
             in the form of a rectangular region for display within an area
             of an active video signal, the pixels forming said region being
             individually defined by the encoded data, characterized in
             that the encoded data for each graphic image includes the
             size and position of said region and a time stamp
             representing the time at which said region is to be displayed.

                           -3-



2. A method as claimed in claim 1, wherein subsequent
encoded data for a given region includes a visibility code to
disable the display of said region.


3. A method as claimed in claim 1, wherein a region
comprises a plurality of subregions including an identifier
code to allow a graphic image defined by said subregion to
be referred to by a further region.


4. A method as claimed in claim 1, wherein the pixels for a
region are encoded as entries of a colour-look-up-table, the
encoded data including a compatibility code indicating a
required minimum number of entries of said colour-look-uptable.


5. A method as claimed in claim 4, wherein the pixels are
defined by n-bit pixel data, the encoded data further including
a map table for mapping said n-bit pixel data to a colour-lookup-table having more than 2n entries.


6. A method as claimed in any of the preceding claims,
wherein the encoded data is accommodated in a private
transport stream according to the MPEG2 standard or
extension thereof.


7. A method of receiving a multiplexed stream comprising
active video data and encoded data defining a graphic image
in the form of a rectangular region for display within an area
of an active video signal, comprising the steps of decoding
said encoded data into individual pixels constituting said
region, storing said pixels, and generating display signals
representing said pixels, characterized by the steps of
decoding from said encoded data for each graphic image the

                            -4-



size and position of said region and a time stamp, and
displaying the region with said size and position from a time
represented by said time stamp.


8. A method as claimed in claim 7, further comprising the
steps of decoding a visibility code included in subsequent
encoded data for a given region, and disabling the
generation of said display signals for said region in response
to said visibility code.


9. A method as claimed in claim 7, wherein a region
comprises a plurality of subregions including an identifier
code, comprising the step of including said subregion in a
further region referring to said subregion.


10. A method as claimed in claim 7, wherein the pixels for a
region are encoded as entries of a colour-look-up-table and
the encoded data includes a compatibility code indicating a
required minimum number of entries of said colour-look-uptable, comprising the step of disabling the generation of
display signals if the required number of entries is less than
available.


11. A method as claimed in claim 10, further comprising the
steps of receiving map table data, and storing said map table
data in a map table for mapping n-bit pixel data to a colorlook-up-table having more than 2n entries.


12. A method as claimed in any of claims 7-11, wherein the
video signal is encoded according to an MPEG2 standard or
extension thereof, and wherein the encoded data defining the
graphic image is accommodated in packets of an MPEG2
private transport stream.

                           -5-




13. A transmitter for transmitting a multiplexed stream
comprising active video data and encoded data defining a
graphic image in the form of a rectangular region within an
area of an active video signal, comprising means for
encoding    the   individual   pixels   forming   said   region,
characterized by further comprising means for including in
the encoded data for each graphic image the size and
position of said region and a time stamp representing the
time at which said region is to be displayed.


14. A receiver coupled to a display screen for receiving a
multiplexed stream comprising active video data and
encoded data defining a graphic image in the form of a
rectangular region within an area of an active video signal,
comprising means for decoding said encoded data into
individual pixels constituting said region, means for storing
said pixels, and means for generating display signals
representing said pixels, characterized by further comprising
means for decoding from said encoded data for each graphic
image the size and position of said region and a time stamp,
and means for displaying the region with said size and
position from a time represented by said time stamp.


15. An image signal comprising a multiplexed stream
comprising an active video signal and encoded data defining
a graphic image in the form of a rectangular region within an
area of an active video signal, the pixels forming said region
being individually defined by the encoded data, characterized
in that the encoded data for each graphic image includes the
size and position of said region and a time stamp
representing the time at which said region is to be displayed.

                                       -6-



    II.   Die Kosten des Rechtsstreits tragen die Klägerinnen zu 80% und die
          Beklagte zu 20%.


   III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120% des jeweils
          zu vollstreckenden Betrages vorläufig vollstreckbar.




                                Tatbestand




Die Beklagte war Inhaberin des am 12. Dezember 1995 angemeldeten und am
29. Dezember 1999 veröffentlichten europäischen Patents 0 745 307 B3 mit der
Bezeichnung    „SUBTITLING      TRANSMISSION         SYSTEM“     (im   Folgenden:
Streitpatent), das auf die internationale Anmeldung PCT/IB95/01118 zurückging
und für das die Priorität der Patentanmeldung EP 94203642 vom 14. Dezember
1994 in Anspruch genommen wurde. Das in der Verfahrenssprache Englisch
abgefasste Streitpatent wird vom Deutschen Patent- und Markenamt unter der
Nummer DE 695 14 212 C5 geführt.


Das Schutzrecht ist am 12. Dezember 2015 durch Zeitablauf erloschen.


Die Klägerin zu 1 wird von der Beklagten wegen Patentverletzung gerichtlich in
Anspruch genommen.


Der Klägerin zu 2 wurde vom Konzern der Beklagten mit Schreiben vom 17. Juni
2014 mitgeteilt, dass u.a. das Streitpatent von der Klägerin zu 2 ohne Lizenz
genutzt werde. Wegen des genauen Wortlauts wird auf die von der Klägerin zu 2
eingereichte Anlage NK 1 Bezug genommen.

                                       -7-



Mit Schriftsatz vom 7. März 2017 erklärte die T… GmbH,
S… Straße in D…, ihren Beitritt als Nebenintervenientin auf Seiten der
Klägerin zu 1, den sie mit Schriftsatz vom 6. September 2017 zurücknahm.


Gegen den deutschen Teil des Streitpatents wurden vor dem Bundespatentgericht
bereits mehrere Patentnichtigkeitsverfahren durchgeführt, u. a. unter dem
Aktenzeichen 4 Ni 38/03 (EU). In dem darauffolgenden Berufungsverfahren vor
dem Bundesgerichtshof (Az. Xa ZR 128/05) erging ein Urteil (vgl. die von der
Klägerin zu 2 eingereichte Anlage NK11), mit dem das Streitpatent entgegen der
ursprünglichen Entscheidung des Bundespatentgerichts nur teilweise für nichtig
erklärt wurde. Die Patentinhaberin (hiesige Beklagte) beantragte in der Folge vor
dem europäischen Patentamt eine Beschränkung des europäischen Patents
gemäß Art. 105a EPÜ mit entsprechend dem Urteil des Bundesgerichtshofs
beschränkten Ansprüchen und geänderter Beschreibung.


Mit ihrer Klage begehren die Klägerinnen die weitergehende (Teil-)Nichtigerklärung des deutschen Teils des europäischen Patents für die Vergangenheit.


In englischer Sprache lauten die geltenden, mit einer möglichen Gliederung
versehenen unabhängigen Ansprüche 1, 7, 13, 14 und 15 (Hauptantrag) wie folgt:


Anspruch 1


       a) A method
       b) of transmitting encoded data defining a graphic image in the form of a
       rectangular region for display within an area of an active video signal,
       c) the pixels forming said region being individually defined by the encoded
       data,
       characterized in that
       f) the encoded data for each graphic image includes the size and position
       of said region and a time stamp
       g) [the time stamp] representing the time at which said region is to be
       displayed.

                                       -8-




Anspruch 7:


       a1) A method
       b1) of receiving encoded data defining a graphic image in the form of a
       rectangular region for display within an area of an active video signal,
       comprising the steps of
       c1) decoding said encoded data into individual pixels constituting said
       region,
       d1) storing said pixels, and
       e1) generating display signals representing said pixels,
       characterized by the steps of
       f1) decoding from said encoded data for each graphic image the size and
       position of said region and a time stamp, and
       g1) displaying the region with said size and position from a time
       represented by said time stamp.


Anspruch 13:


       a2) A transmitter
       b2) for transmitting encoded data defining a graphic image in the form of a
       rectangular region within an area of an active video signal,
       comprising
       c2) means for encoding the individual pixels forming said region,
       characterized by further comprising
       f2) means for including in the encoded data for each graphic image the
       size and position of said region and a time stamp
       g2) [the time stamp] representing the time at which said region is to be
       displayed.


Anspruch 14:


       a3) A receiver coupled to a display screen

                                         -9-



         b3) for receiving encoded data defining a graphic image in the form of a
               rectangular region within an area of an active video signal,
               comprising
         c3) means for decoding said encoded data into individual pixels
         constituting said region,
         d3) means for storing said pixels, and
         e3) means for generating display signals representing said pixels,
         characterized by further comprising
         f3) means for decoding from said encoded data for each graphic image
         the size and position of said region and a time stamp, and
         g3) means for displaying the region with said size and position from a time
         represented by said time stamp.


Anspruch 15:


         a4) An image signal comprising
         b4) encoded data defining a graphic image in the form of a rectangular
         region within an area of an active video signal,
         c4) the pixels forming said region being individually defined by the
         encoded data,
         characterized in that
         f4) the encoded data for each graphic image includes the size and position
         of said region and a time stamp
         g4) [the time stamp] representing the time at which said region is to be
         displayed.


In der Übersetzung des Senats lauten diese Ansprüche in deutscher Sprache wie
folgt:


Anspruch 1:


         a) Verfahren

                                      - 10 -



       b) zum Übertragen codierter Daten, welche ein graphisches Bild in Form
       eines rechteckigen Bereichs zur Wiedergabe innerhalb eines Gebietes
       eines aktiven Videosignals definieren,
       c) wobei die Pixel, die den genannten Bereich bilden, durch die codierten
       Daten einzeln definiert werden,
       dadurch gekennzeichnet, dass
       f) die codierten Daten für jedes graphische Bild die Größe und die Lage
       des genannten Bereichs und einen Zeitstempel enthalten,
       g) welcher [Zeitstempel] die Zeit darstellt, zu der der genannte Bereich
       wiedergegeben werden soll.


Anspruch 7:


       a1) Verfahren
       b1) zum Empfangen codierter Daten, welche ein graphisches Bild in Form
       eines rechteckigen Bereichs zur Wiedergabe innerhalb eines Gebietes
       eines aktiven Videosignals definieren,
       wobei das Verfahren die Verfahrensschritte umfasst:
       c1) Decodieren der genannten codierten Daten in einzelne Pixel, die den
       genannten Bereich bilden,
       d1) Speichern der genannten Pixel und
       e1) Erzeugen von Wiedergabesignalen, welche die genannten Pixel
       darstellen,
       gekennzeichnet durch die Schritte:
       f1) Decodieren aus den genannten codierten Daten für jedes graphische
       Bild der Größe und der Lage des genannten Bereichs und eines
       Zeitstempels, und
       g1) Wiedergeben des Bereichs mit der genannten Größe und Position von
       einem Zeitpunkt an, der durch den genannten Zeitstempel dargestellt ist.


Anspruch 13:


       a2) Sender

                                      - 11 -



       b2) zum Übertragen codierter Daten, welche ein graphisches Bild in Form
       eines rechteckigen Bereichs innerhalb eines Gebietes eines aktiven
       Videosignals definieren,
       umfassend:
       c2) Mittel zum Codieren der einzelnen Pixel, die den genannten Bereich
       bilden,
       dadurch gekennzeichnet, dass er ferner aufweist:
       f2) Mittel, um in die codierten Daten für jedes graphische Bild die Größe
       und die Lage des genannten Bereichs und einen Zeitstempel
       aufzunehmen,
       g2) welcher [Zeitstempel] die Zeit darstellt, zu der der genannte Bereich
       wiedergegeben werden soll.


Anspruch 14:


       a3) Empfänger, gekoppelt mit einem Wiedergabeschirm
       b3) zum Empfangen codierter Daten, die ein graphisches Bild in Form
       eines rechteckigen Bereichs innerhalb eines Gebietes eines aktiven
       Videosignals definieren,
       umfassend:
       c3) Mittel zum Decodieren der codierten Daten in einzelne Pixel, die den
       genannten Bereich bilden,
       d3) Mittel zum Speichern der genannten Pixel, und
       e3) Mittel zum Erzeugen von Wiedergabesignalen, welche die genannten
       Pixel darstellen,
       dadurch gekennzeichnet, dass er weiterhin aufweist
       f3) Mittel zum Decodieren aus den codierten Daten für jedes graphische
       Bild der Größe und der Lage des Bereichs und eines Zeitstempels, und
       g3) Mittel zur Wiedergabe des Bereichs mit der genannten Größe und
       Lage von einem Zeitpunkt an, der durch den Zeitstempel dargestellt ist.

                                       - 12 -



Anspruch 15:


        a4) Bildsignal, umfassend:
        b4) codierte Daten, welche ein graphisches Bild in Form eines
        rechteckigen Bereichs innerhalb eines Gebietes eines aktiven
        Videosignals definieren,
        c4) wobei die den genannten Bereich bildenden Pixel durch die codierten
        Daten einzeln definiert werden,
        dadurch gekennzeichnet, dass
        f4) die codierten Daten für jedes graphische Bild die Größe und die Lage
        des genannten Bereichs und einen Zeitstempel enthalten,
        g) welcher [Zeitstempel] die Zeit darstellt, zu der der genannte Bereich
        wiedergegeben werden soll.


Von     der    ursprünglich     vor    dem      genannten      Nichtigkeits-   bzw.
Beschränkungsverfahren erteilten Fassung unterscheiden sich diese Ansprüche
jeweils durch die Einfügung „for each graphic image“ bzw. „für jedes graphische
Bild“ in dem jeweiligen Merkmal f), f1), f2), f3) bzw. f4), das in der ursprünglich
erteilten Fassung nicht vorhanden war.


Hinsichtlich der auf den Patentanspruch 1 rückbezogenen Unteransprüche 2 bis 6
und der auf den Patentanspruch 7 unmittelbar oder mittelbar rückbezogen
Patentansprüche 8 bis 12 wird auf die geänderte Patentschrift (EP 0 745 307 B3)
verwiesen.


Die Beklagte verteidigt das Streitpatent gemäß Hauptantrag in vollem Umfang und
hilfsweise beschränkt gemäß den mit Schriftsatz vom 9. Januar 2018
eingereichten Hilfsanträgen I, II und III in der in der mündlichen Verhandlung
eingereichten Fassung, mit welcher offensichtliche Fehler korrigiert wurden.

                                          - 13 -



Im Hilfsantrag I ist im Patentanspruch 1 das Merkmal b) ersetzt durch:


        b’) of transmitting a multiplexed stream comprising active video data and
        encoded data defining a graphic image in the form of a rectangular region
        for display within an area of an active video signal,


Auch in den Merkmalen b1), b2) und b3) der nebengeordneten Ansprüche 7, 13
und 14 des Hilfsantrags I wurde jeweils vor „encoded data“ der Ausdruck “a
multiplexed stream comprising active video data and“ eingefügt.


Im nebengeordneten Anspruch 15 des Hilfsantrags I wurde das Merkmal b4)
ersetzt durch:


        b4’) a multiplexed stream comprising an active video signal and encoded
        data defining a graphic image in the form of a rectangular region within an
        area of an active video signal,


Zu den Hilfsanträgen II und III wird auf die Akte verwiesen.


Die Klägerinnen machen die Nichtigkeitsgründe der unzulässigen Erweiterung und
der fehlenden Patentfähigkeit geltend.


Sie sind der Ansicht, das bei der Beschränkung im genannten Berufungsverfahren
hinzugekommene Merkmal in den nebengeordneten Patentansprüchen 1, 7, 13,
14 und 15, welches besage, dass die codierten Daten aller grafischen Bilder eines
Bilddatenstroms die Größe und die Lage der rechteckigen Bereichs sowie eine
Zeitmarke, welche die Zeit darstellt, in der der Bereich wiedergegeben werden
soll, beinhalten, sei nicht ursprünglich offenbart.


Das Streitpatent sei zudem nicht patentfähig. Die Ansprüche 7 und 14 des
Streitpatents könnten die Priorität vom 14. Dezember 1994 nicht beanspruchen,
denn die Prioritätsunterlagen (bezeichnet als NI7) enthielten keine unmittelbare

                                      - 14 -



und eindeutige Offenbarung für ein „Speichern der Pixel“ bzw. für „Mittel zum
Speichern der Pixel“.
Zur Begründung der mangelnden Patentfähigkeit beziehen sich die Klägerinnen
insbesondere auf folgende Unterlagen:


      D1: US 5089899 A
      D2: EP 488676 A2
      D3: JP 06-292080 A
      D3a: Übersetzung von D3
      D4: Fachbuchauszug zur Erläuterung von D3
      D5: ISO/IEC 13818-1 vom 13. 11. 1994
      D6: EP 331417 A2
      D7: US 4675737 A
      D8: G. Möll: „Neue Leistungsmerkmale für einen künftigen Videotextstandard“, Rundfunktech. Mitteilungen 27 (1983) H.3, S. 116 - 134
      D9: WO 92/00647 A1
      D10: WO 82/04154 A1
      D11: EP 0 677 954 A2


ferner (ursprünglich von der Nebenintervenientin eingeführt)


      NI2: ISO-IEC 13818-2 vom 25. 3. 1994 (ergänzt D5)
      NI7: Prioritätsunterlagen Patentanmeldung 94203642.7
      NI8: DVB Subtitling System; mit Zeitangabe 31. Okt. 1995
      NI9: Konvolut zum Veröffentlichungsdatum von NI8.


Dazu tragen sie vor, das Streitpatent werde insbesondere von der D11
neuheitsschädlich getroffen.
Die zusätzlichen Merkmale der Hilfsanträge I bis III seien aus NI8 bekannt oder
entsprächen dem Fachwissen.
Die Klägerin zu 2 trägt des Weiteren vor, dass ihr für die Vergangenheit eine
Inanspruchnahme aus dem Streitpatent drohe.

                                           - 15 -



Die Klägerin zu 1 stellt den Antrag,


      das europäische Patent 0 745 307 im Umfang des Anspruchs 14 mit
      Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig
      zu erklären.


Die Klägerin zu 2 stellt den Antrag,


      das europäische Patent 0 745 307 in vollem Umfang mit Wirkung für das
      Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte stellt den Antrag,


      die Klagen abzuweisen,


      hilfsweise unter Klageabweisung im Übrigen das europäische Patent
      0 745 307      dadurch   teilweise     für    nichtig   zu   erklären,   dass   seine
      Patentansprüche       die Fassung eines der Hilfsanträge I bis III vom
      9. Januar 2018 in der in der mündlichen Verhandlung eingereichten
      korrigierten Fassung, in dieser Reihenfolge, erhalten.


Die Beklagte erklärt, sie verstehe die Ansprüche nach Haupt- und Hilfsantrag
jeweils als geschlossene Anspruchssätze, die jeweils in ihrer Gesamtheit
beansprucht werden.


Die Beklagte ist der Auffassung, dass der Klägerin zu 2 nach Erlöschen des
Patents das Rechtsschutzbedürfnis fehle.


Sie ist ferner der Auffassung, den Klagen stehe die Rechtskraft der genannten
Entscheidung des Bundesgerichtshofes insoweit entgegen, als erneut ein
Sachverhalt geltend gemacht werde, über den bereits rechtskräftig entschieden
worden sei. Zwar beschränke § 325 Abs. 1 ZPO die materielle Rechtskraft des
rechtskräftigen Urteils auf die Parteien des Rechtsstreits.

                                        - 16 -



Diese   Beschränkung      der   Rechtskraft      sei   mit   den   Besonderheiten   des
Nichtigkeitsverfahrens jedoch insoweit unvereinbar, als dass Nichtigkeitsurteile als
Gestaltungsurteile nicht (nur) die Rechtsverhältnisse zwischen den Parteien,
sondern den Fortbestand oder die Vernichtung des Patents beträfen.
Die Beklagte tritt i. Ü. den Ausführungen der Klägerinnen in allen Punkten
entgegen. So seien sämtliche Merkmale des geltenden Streitpatents sowie der
Hilfsanträge ursprungsoffenbart, und das Streitpatent nehme die Priorität zu Recht
in Anspruch. Sie ist weiter der Ansicht, die Entgegenhaltungen offenbarten
wesentliche Merkmale der erfindungsgemäßen Lehre nicht, und es sei auch keine
Veranlassung für den Fachmann ersichtlich, ausgehend vom genannten Stand der
Technik zur Lehre des Streitpatents zu gelangen.
Insbesondere weise die D11 keinen Zeitstempel wie das Streitpatent auf, sondern
zeige lediglich einen andersartigen Rahmenzähler.


Die Beklagte hat unter anderem folgende Unterlage eingereicht:


        NB2: Video CD Specification 2.0, Juli 1994, mit Vermerk “Confidential”


Wegen der weiteren Einzelheiten des Vorbringens der Beteiligten wird auf den
Akteninhalt verwiesen.




                         Entscheidungsgründe


                                          I.


1. Die Klagen, mit der die Nichtigkeitsgründe der fehlenden Patentfähigkeit nach
Artikel II § 6 Absatz 1 Nr. 1 IntPatÜG, Artikel 138 Abs. 1 lit. a) EPÜ i. V. m. Artikel
52, 54 Absatz 1, 2, 3 und Artikel 56 EPÜ sowie der unzulässigen Erweiterung
(Artikel II § 6 Absatz 1 Nr. 3 IntPatÜG i. V. m. Artikel 138 Absatz 1 lit. c) EPÜ)
geltend gemacht werden, sind zulässig.

                                          - 17 -




1.1.    Den Klagen steht nicht die Rechtskraft der genannten Entscheidung des
Bundesgerichtshofes (Az. Xa ZR 128/05) entgegen. Die Grenzen der materiellen
und subjektiven Rechtskraft ergeben sich aus § 99 Abs. 1 PatG i.V.m. §§ 323, 325
ZPO. Der Senat vermag nicht zu erkennen, dass aus Rücksicht auf die
Besonderheiten des Verfahrens vor dem Patentgericht (§ 99 Abs. 1, 2. Hs PatG)
die    allgemeinen    zivilprozessualen    Bestimmungen     insbesondere    über   die
subjektive Rechtskraft ausgeschlossen werden und somit eine Ausdehnung der
Rechtskraft auf nicht am Vorprozess beteiligte Personen aus Gründen des
Patentrechts geboten sein könnte. Zwar hat die unmittelbare Gestaltung eines
Rechtsverhältnisses oder einer Rechtsposition durch das Nichtigkeitsurteil
mittelbare Auswirkungen auf Dritte. Hierbei handelt es sich jedoch nur um einen
Reflex, nicht um eine Ausdehnung der Rechtskraft, so dass erst recht nicht im
Falle der Klageabweisung, die in das Streitpatent überhaupt nicht gestaltend
eingreift, eine Rechtskraftwirkung gegenüber Dritten eintreten kann.


Es     widerspräche    vielmehr   der     Wertung   des     Gesetzgebers,    der   die
Nichtigkeitsklage     als   Popularklage     ausgestaltet   hat,   wenn     bestimmte
Rechtsfragen, vornehmlich Nichtigkeitsgründe, durch einzelne Kläger „verbraucht“
werden könnten und mit den gleichen Gründen vorher unbeteiligte Dritte in
späteren Verfahren wegen entgegenstehender Rechtskraft nicht mehr gehört
werden dürften. Diese Auffassung könnte den Anspruch auf rechtliches Gehör
ohne Rechtfertigung beeinträchtigen. Der Gewinn an Rechtssicherheit für den
Patentinhaber wäre demgegenüber vernachlässigbar, da eine identische Wiederholung des Vortrags aus dem Vorprozess nur selten erfolgt und bereits geringe
Änderungen, wie hier, den Rechtskrafteinwand gegenstandslos werden lassen
würde. Soweit die Beklagte einwendet, sie sehe sich erneut Angriffen auf das
Patent ausgesetzt, die mit weitgehend identischen Gründen bereits in einem
vorangegangenen Verfahren behandelt worden seien, so hat sie dies hinzunehmen. Zwar muss die Beklagte befürchten, dass das im früheren Verfahren
erfolglose Nichtigkeitsbegehren, von einem anderen Kläger vorgetragen, nunmehr
Erfolg hat, dies ist jedoch lediglich die Folge der Ausgestaltung der Nichtigkeitsklage als Popularklage, denn das vom Gesetzgeber mit der Ausgestaltung der

                                         - 18 -



Nichtigkeitsklage als vorrangig anerkannte Allgemeininteresse an der Vernichtung
zu Unrecht eingetragener Schutzrechte kann nicht deshalb hinsichtlich einzelner
Nichtigkeitsgründe rechtskräftig verneint werden, weil ein einzelner Kläger es
erfolglos geltend gemacht hat.


Der    Senat   sieht    sich   in   diesem   Ergebnis   auch   bestätigt   durch   die
höchstrichterliche Rechtsprechung, die eine Rechtskraftwirkung der Abweisung
einer Nichtigkeitsklage gegenüber Dritten grundsätzlich verneint hat und auch
keinerlei Anhaltspunkte für die von der Beklagten postulierte Ausnahme erkennen
lässt (so auch BGH, Urteil vom 13. Juli 2013 – X ZR 36/11 Rn. 3, 7, 8 –
Tintenpatrone, juris; BGH GRUR-RR 2010, 136-138 Rn. 17; Keukenschrijver,
Patentnichtigkeitsverfahren, 9. Aufl.; ähnlich auch Schulte, § 81 Rn 45), sowie die
Rechtsprechung zur Unzulässigkeit der Klage durch einen Strohmann, die die
erneute Klage gegen dasselbe Streitpatent durch einen Dritten als Regelfall einer
grundsätzlich zulässigen Nichtigkeitsklage nennt (vgl. etwa BGH GRUR-RR 2010,
136-138 Rn. 17; BGH, Urteil vom 29. November 2011 – X ZR 23/11 –, BPatGE 52,
303, Rn 10 ff.; BGH, Urteil vom 13. Januar 1998 – X ZR 82/94 –, BPatGE 40, 279
Rn. 12; BPatG München, Urteil vom 19. Januar 2011 – 5 Ni 103/09 (EU) –,
BPatGE 52, 245-256; BGH GRUR 1998, 904-907 - Bürstenstromabnehmer).


1.2.   Das Rechtsschutzbedürfnis der Klägerin zu 2 kann nicht verneint werden.
Nach höchstrichterlicher Rechtsprechung bedarf es zu dem auf die Feststellung
der Unwirksamkeit des durch Verzicht oder Zeitablauf erloschenen Schutzrechtes
gerichteten Begehrens eines besonderen in der Person des Klägers liegenden,
aus seiner Beziehung zu dem angegriffenen Schutzrecht abzuleitenden
Interesses, wobei von einer großzügigen Gewährung von Rechtsschutz
auszugehen ist. Die Beklagte hat mit dem Schreiben vom 17. Juni 2014 (Anl. NK
1) der Klägerin zu 2 die Verletzung u.a. des Streitpatents („…formal notiﬁcation
that Vestal infringes the patents…“) vorgeworfen und sich, neben einem
Gesprächsangebot über eine Lizensierung, die Rechte aus einer unauthorisierten
Benutzung vorbehalten. Diese Verwarnung gibt der Klägerin zu 2 ausreichenden
Anlass, eine Inanspruchnahme zu befürchten (vgl. dazu Schulte, PatG, 10. Aufl.,
§81 Rn. 40f. m.w.N.).

                                      - 19 -



Einen zwischenzeitlichen Verzicht auf diese Rechte hat auch die Beklagte nicht
behauptet. Die Beklagte kann sich auch nicht mit Erfolg darauf berufen, dass der
Klägerin zu 2 die Einrede der Verjährung zustehen könnte, da diese das Bestehen
etwaiger Rechte nicht berührt, sondern lediglich ein Leistungsverweigerungsrecht
begründet. Auf die zwischen den Parteien streitige Frage, ob die Verjährung
bereits eingetreten oder gehemmt worden sein könnte, kommt es mithin nicht an.


1.3.   Es bestand kein Anlass, entsprechend dem Antrag der Klägerin zu 2) die
mündliche Verhandlung zu vertagen oder eine zusätzliche Schriftsatzfrist
einzuräumen.
Dies war weder erforderlich wegen der Einreichung der Hilfsanträge am 9. Januar
2018 noch wegen der Korrektur dieser Hilfsanträge, da die Korrektur nur ohne
weiteres ersichtliche Fehler betraf und die Klägerin ausreichend Zeit und
Gelegenheit hatte, zu allen wesentlichen Gesichtspunkten Stellung zu nehmen,
was sie auch getan hat. Dies gilt auch in Bezug auf die geänderte vorläufige
Meinung des Senats, die bereits schriftsätzlich und in der mündlichen
Verhandlung ausführlich diskutierte Problemstellungen betraf.




2. Die Klagen sind indes nur teilweise begründet.


Das Streitpatent hat in der erteilten Fassung keinen Bestand, da den
Gegenständen des Patents in der erteilten Fassung der Nichtigkeitsgrund der
fehlenden Patentfähigkeit entgegensteht. In der Fassung des Hilfsantrags I ist das
Streitpatent jedoch bestandsfähig.




                                        II.


1. Das Streitpatent betrifft ein Verfahren zum Übertragen codierter Daten, die ein
graphisches Bild in Form eines rechteckigen Bereichs (Untertitel) innerhalb eines
aktiven Videogebiets definieren, sowie ein Verfahren zum Empfangen der genann-

                                          - 20 -



ten graphischen Bilder und einen Sender und einen Empfänger zum Durchführen
der genannten Verfahren (Abs. [0001]).


Gemäß Abs. [0002] bis [0005] der Streitpatentschrift ist ein Verfahren zum
Übertragen graphischer Bilder unter der Bezeichnung "Teletext" bekannt; es
werde      insbesondere    angewandt      zur      Übertragung    von    Untertiteln   bei
Fernsehprogrammen. Das bekannte Teletextsystem sei sehr beschränkt in
Qualität und Leistung. Es sei ein zeichenbasiertes Übertragungssystem, wobei
codierte Daten übertragen würden, welche die darzustellenden Zeichen
definierten. Das Aussehen der Untertitel (Schriftart, Abstände, graphische
Fähigkeiten, Farben) sei durch Hardware festgelegt. Dieses System sei nur mit
Hilfe   sehr   teurer   und   aufwändiger       Zeichengeneratoren      fähig,   komplexe
Zeichensätze zu unterstützen, wie sie in China und Japan benutzt würden.


Inzwischen solle zum Übertragen digitaler Fernsehprogramme zum Nutzer über
verschiedene Übertragungswege oder Medien die digitale Fernsehnorm MPEG2
(ISO/IEC 13818) weltweit angewandt werden. Die MPEG2-Kompressions- und
Multiplexing-Technologie      würde dem Endnutzer eine große Auswahl an
Programmen       bieten,   wofür   eine     benutzerfreundliche     "Mensch-Maschine-Schnittstelle" erforderlich sei. Bei Satellitenübertragung mit dem hierfür typischen
großen Umfang des Empfangsgebietes, das meistens viele Sprachbereiche
einschließe, seien mehrsprachige Untertitelfähigkeiten notwendig.


Zum Stand der Technik sind verschiedene Schriften abgehandelt (Abs. [0006],
[0007]).


Aufgabe der vorliegenden Erfindung sei es, das bekannte Übertragungssystem
weiter zu verbessern und eine universelle Lösung für mehrsprachige Untertitelung
zu schaffen, insbesondere für eine MPEG2-Umgebung (Abs. [0008]).

                                         - 21 -



2.     Die patentgemäße Lehre besteht im Wesentlichen in Folgendem:


Nach der Patentschrift sollen Bilddaten für mehrere (aufeinander folgende)
graphische Bilder erzeugt, übertragen und empfangen werden. Die graphischen
Bilder sollen letztendlich in gegebene Videobilder (etwa in einem Videofilm)
eingeblendet werden, wobei die graphischen Bilder z.B. Untertitel darstellen, die
Übersetzungen in verschiedenen Sprachen bereitstellen. Die Patentschrift befasst
sich im Wesentlichen damit, welche Daten für die graphischen Bilder übertragen
werden müssen, um eine hohe Flexibilität der Darstellung zu ermöglichen.


Mit dem Ausdruck „graphisches Bild“ bezeichnet das Streitpatent einen rechteckigen Bereich im Gebiet eines aktiven Videosignals, etwa einen Untertitel, der
an einem dafür vorgesehenen Ort auf einem Bildschirm wiedergegeben werden
soll. Die den rechteckigen Bereich definierenden Daten (Bildsignal, Anspruch 15)
liegen in codierter Form vor und definieren die einzelnen Bildpunkte (Pixel) des
Bereichs (Merkmale a4), b4), c4)). Zusätzlich zu den Pixeldaten enthalten die
codierten Daten Angaben zur Größe und Lage des rechteckigen Bereichs auf dem
Bildschirm sowie einen Zeitstempel, welcher angibt, wann der Bereich wiedergegeben werden soll. Diese Angaben sollen in den codierten Daten für jedes
graphische Bild enthalten sein (Merkmale f4), g4)).


Beansprucht sind zudem ein Verfahren und ein Sender zum Übertragen solcher
Daten, wobei im Sender die zu übertragenden Daten codiert werden (Ansprüche 1
und 13 mit den Merkmalen a), a2), b), b2), c), c2), f), f2), g) und g2)).


Des Weiteren sind ein Verfahren und ein Empfänger zum Empfangen solcher
Daten beansprucht (Ansprüche 7 und 14; Merkmale a1), a3), b1), b3)). Hierbei
werden die empfangenen codierten Daten in einzelne Pixel decodiert, die gespeichert werden und aus denen Wiedergabesignale erzeugt werden (Merkmale c1),
c3), d1), d3), e1), e3)). Aus den empfangenen Daten werden zudem die Größe,
die Lage und der Zeitstempel extrahiert (decodiert); schließlich wird der
rechteckige Bereich mit der Größe und Lage zu der durch den Zeitstempel
gegebenen Zeit dargestellt (Merkmale f1), f3), g1), g3)).

                                         - 22 -



Gemäß den selbständigen Patentansprüchen des Hilfsantrags I umfassen die (zu
übertragenden bzw. zu empfangenden) Daten bzw. das beanspruchte Bildsignal
einen Multiplexstrom aus aktiven Videodaten und den bereits beschriebenen
codierten Daten.


2.1 Erläuterungsbedürftig ist die Interpretation der Einfügung „for each graphic
image“.


Nach Auffassung des Senats bezieht sich diese Einfügung in den unabhängigen
Patentansprüchen, ausgehend vom üblichen Sprachverständnis, auf alle drei im
Merkmal genannten Parameter (Größe, Position und Zeitstempel). Dies ergibt sich
aus der Formulierung der Ansprüche selbst in den Merkmalen f), f1), f2), f3) und
f4) „the encoded data for each graphic image includes the size and position of said
region and a time stamp …” bzw. “ “decoding from” / “including in” said encoded
data for each graphic image the size and position of said region and a time stamp
…”. Hätte für jedes Bild nur die Größe und die Lage enthalten sein sollen, so hätte
die Einfügung „for each graphic image“ an anderer Stelle angeordnet werden
müssen, etwa „the encoded data includes the size and position of said region for
each graphic image and a time stamp …”.


Die Beklagte widerspricht dieser Auslegung, insbesondere dem Bezug auf das
„übliche Sprachverständnis“ (Schriftsatz vom 27. Juli 2017, Seite 10 bis 12), und
verweist dazu auf die Entscheidung BGH GRUR 2007, 778 – Ziehmaschinenzugeinheit I. Sie vertritt die Auffassung, dass sich die Einfügung „for each graphic
image“ nur auf die zwei Parameter „Größe“ und „Lage“ des Bildes beziehe.


Gerade die zitierte BGH-Entscheidung stützt aber die Auslegung des Senats,
indem sie formuliert: „Schränken die sich mit der Teilabweisung befassenden
Entscheidungsgründe des Nichtigkeitsurteils den Sinngehalt eines die Erfindung
allgemein kennzeichnenden Patentanspruchs im Sinne einer Auslegung unter
seinen Wortlaut ein, erlaubt dies im Verletzungsprozess ebenso wenig eine
einschränkende     Auslegung    dieses     Patentanspruchs   wie   bei   sich   aus
Beschreibung oder Zeichnungen des Patents ergebenden Beschränkungen“

                                      - 23 -



(Leitsatz b)). Und weiter: „Der Wortsinn, den das Bundespatentgericht
Patentanspruch 1 beigelegt und an den sich das Berufungsgericht gebunden
gesehen hat, stellt nach allem eine Schutzbegrenzung dieses Anspruchs unter
seinen Wortlaut im Sinne einer Auslegung unter seinen Sinngehalt dar. Sie
schränkt den durch seinen Wortlaut festgelegten Gegenstand des Patentanspruchs 1 und den Schutzbereich des Patents unzulässig ein“ (III. 3.). Demnach
hält der Bundesgerichtshof hier an seiner Rechtsprechung fest, dass die
Auslegung   eines   –   auch   in   einem      Nichtigkeitsverfahren   geänderten   –
Patentanspruchs an seinen Wortlaut gebunden ist, so wie ihn der Fachmann
versteht; und der Fachmann wird sich, soweit er keine dagegensprechende
Gründe sieht, am (fach-) üblichen Sprachverständnis orientieren. Die Auslegung
hat nicht anhand der Urteilsgründe zu erfolgen, sondern anhand des
Anspruchswortlauts und dessen fachmännischem Verständnis.


Eine solche Auslegung steht nicht im Widerspruch zur Begründung des Bundesgerichtshofs für die Patentfähigkeit in der das Streitpatent betreffenden
Entscheidung Xa ZR 128/05 (NK11), da der beanspruchte Empfänger über das
Bekannte hinaus eben gerade für Bilder ausgelegt sein soll, bei denen jedes
einzelne die drei Parameter mitbringt, was nach den Ausführungen des Bundesgerichtshofs bereits für die zwei Parameter „Lage“ und „Größe“ nicht nahelag.


2.2. Zudem streiten die Parteien darüber, ob der beanspruchte Sender bzw.
Empfänger so arbeiten muss, dass er zwingend für jedes graphische Bild die
Parameter Lage, Größe und Zeitstempel codiert bzw. decodiert, insbesondere im
Lichte von Abs. [0027] iVm [0026] der Patentschrift, wonach nicht alle Parameter
zwingend vorhanden sein müssen; bereits definierte Bereiche können modifiziert
werden, indem z.B. nur die Lage eines Bereichs verändert wird.


Nachdem alle unabhängigen Ansprüche vorgeben, dass für jedes graphische Bild
die codierten Daten die drei Parameter Lage, Größe und Zeitstempel enthalten,
sieht der Senat die Angaben in Abs. [0027] lediglich als zusätzliche Möglichkeit
zur Ausgestaltung des Senders und Empfängers der Ansprüche 13 und 14 an.

                                       - 24 -



In der Realität kann es ohne Weiteres vorkommen, dass für mehrere aufeinander
folgende graphische Bilder ein oder mehrere Parameter (z.B. die Größe eines
Untertitels) gleich bleiben sollen. Um solche Fälle effizient verarbeiten zu können,
erscheint es sinnvoll, dass der Sender bzw. der Empfänger auch in der Lage ist,
für ein einzelnes graphisches Bild jeweils nur den oder die tatsächlich variierenden
Parameter zu codieren bzw. zu decodieren, während sich das Bild die gleich
bleibenden Parameter mit anderen Bildern teilt (vgl. Abs. [0027]).


Zentraler Punkt ist jedoch die Fähigkeit des Senders und Empfängers, eine eine
Vielzahl von aufeinander folgenden graphischen Bildern enthaltende Sequenz von
Bilddaten zu verarbeiten (zu codieren bzw. zu decodieren), in der jedem Einzelbild
eine speziell diesem Bild zugehörige Größe und Lage des Bereichs und ein
Zeitstempel zugeordnet sind. In dem Sender bzw. Empfänger muss somit
zwingend das Übertragungs- bzw. Empfangsverfahren des Anspruchs 1 bzw. 7
(mit Codierung bzw. Decodierung aller drei Parameter für jedes graphische Bild)
implementiert sein, so dass die Bildsignale des Anspruchs 15 codiert bzw.
decodiert werden können.


Zusätzlich können Verfahren oder Verfahrensteile implementiert sein, die eine
Codierung bzw. Decodierung von weniger Parametern pro graphischem Bild
erlauben; dies ist jedoch durch die patentierten Ansprüche nicht unter Schutz
gestellt.




3. Wie der Bundesgerichtshof bereits in seiner das Streitpatent betreffenden
Entscheidung Xa ZR 128/05 festgestellt hat, ist hier als zuständiger Fachmann ein
Hochschul- oder Fachhochschulabsolvent der Fachrichtung Mathematik, Informatik, Technische Informatik oder Elektrotechnik mit Erfahrung auf dem Gebiet der
digitalen Fernsehtechnik anzusehen, vgl. NK11 S. 11 zweiter vollständiger Satz.

                                       - 25 -



                                        III.


Der dem Streitpatent in der erteilten Fassung zu entnehmende Gegenstand des
Patentanspruchs 1 ist nicht neu (Artikel II § 6 Abs. 1 Nr. 1 IntPatÜG, Artikel 138
Abs. 1 lit. a), Artikel 54 EPÜ). Entsprechendes gilt für die erteilten,
nebengeordneten Patentansprüche 7, 13, 14 und 15.


Die Gegenstände der selbständigen Patentansprüche gemäß Hilfsantrag I sind
jedoch gegenüber dem Stand der Technik neu und beruhen auch auf
erfinderischer Tätigkeit.




1.     Die erteilten Patentansprüche 1, 7, 13, 14 und 15 sind in den
ursprünglichen Unterlagen und ebenso in der ersten Version der Streitpatentschrift
offenbart.
Entsprechendes gilt für die selbständigen Ansprüche 1, 7, 13, 14 und 15 des
Hilfsantrags I.


Der geltende Anspruch 1 sowie die nebengeordneten Ansprüche 7, 13, 14 und 15
gehen in WO 96/19077 A1 im Wesentlichen hervor aus den ursprünglichen
Ansprüchen 1, 2, 8, 9, 15, 16, 17, aus Tabelle II sowie aus Fig. 6 mit der
zugehörigen Beschreibung auf S. 13 Z. 9 bis S. 15 Z. 11, insbesondere S. 13
Z. 18, 19 und 24 bis 26 sowie S. 15 Z. 5 bis 11.
Dass einige der nunmehr in den geltenden Ansprüchen enthaltenen Merkmale aus
den Anmeldeunterlagen lediglich als fakultative Möglichkeit hervorgehen, steht
einer Offenbarung dieser Merkmale nicht entgegen.
Die geltenden Ansprüche 1, 7, 13, 14 und 15 gehen in der ersten Version der
Streitpatentschrift im Wesentlichen zurück auf die entsprechenden erteilten
Ansprüche, auf Tabelle II sowie Fig. 6 mit Beschreibung, insbesondere Abs.
[0032] und [0038].

                                        - 26 -



Insbesondere sieht der Senat die Offenbarung eines Zeitstempels für jedes
graphische Bild als gegeben an. Nach WO 96/19077 A1 S.3 le. Abs. und S. 13
Z. 18 und 19 enthält der Header eines PES-Pakets einen Zeitstempel, der die
Darstellungszeit für einen Bereich („region“) bzw. für jede bereichsbezogenen
Daten in dem PES-Paket angibt; ein Bereich enthält die Daten eines Bildes
(Tabelle II). Im Einzelnen umfasst laut Seite 10, Zeilen 19-20 das PES_data_field
() einen oder mehrere Bereiche (Tabelle 1, Fig. 1 bis 3). Somit ergibt sich
zumindest für den Fall eines einzigen im PES-Paket enthaltenen Bereichs eine
Zuordnung des PTS-Zeitstempels im PES-Header zu den Daten des Bereichs im
PES_data_field (), so dass der Bereich einen eigenen Zeitstempel erhält. Überdies
müssen sich innerhalb einer Multi-Seite (d. h. einer Seite mit mehreren Bereichen,
Fig. 1 bis 3) die Zeitstempel der einzelnen Bereiche um mehr als 40 msec
unterscheiden (S. 3 unten), d. h. auch in diesem Fall muss jedem Bereich ein
eigener Zeitstempel zugeordnet sein.


Dass im Kontext des MPEG2-Standards im Fall eines Stroms von Stillbildern (mit
jeweils einem zugehörigen Zeitstempel, D5 Kap. 2.1.53) eine Einteilung in
PES-Pakete, die jeweils nur höchstens ein Stillbild enthalten, durchaus realistisch
ist, zeigt im Übrigen NB2 unter 3.1 auf S. V-3 und 3.2 auf S. V-5.


Entsprechende Offenbarungsstellen wie die oben für WO 96/19077 A1
angegebenen finden sich auch in der ersten Version des erteilten Patents.


Im Übrigen bedarf die genannte Offenbarungsfrage keiner Entscheidung. Selbst
wenn man den Teilaspekt, dass ein Zeitstempel „für jedes graphische Bild“ (bzw.
für jeden Bereich) codiert bzw. decodiert wird, als nicht eindeutig ursprünglich
offenbart ansähe, so würde diese Angabe gegenüber dem ursprünglich
Offenbarten allenfalls eine Einschränkung darstellen, jedoch kein Aliud. Eine
derartige   Einschränkung     rechtfertigt   keine   Nichtig-Erklärung,   ein   nicht
ursprungsoffenbartes Merkmal darf lediglich nicht zur Stützung der Patentfähigkeit
herangezogen       werden      (siehe        BGH     GRUR       2015,     573      –
Wundbehandlungsvorrichtung).

                                       - 27 -



Auch die zusätzlichen, einen Multiplex-Datenstrom aus aktiven Videodaten und
codierten Daten betreffenden Merkmale der selbständigen Ansprüche des
Hilfsantrags I gehen aus den ursprünglichen Unterlagen und ebenso aus der
ersten Version der Streitpatentschrift hervor, vgl. in WO 96/19077 A1 S. 13 Z. 5
bis 12 und im Streitpatent Abs. [0031] vorle. Satz bis Abs. [0032] Satz 1.
Hierbei war es nicht notwendig, auch an diesen Stellen genannte weitere
Merkmale wie den MPEG2-Standard mit in die Patentansprüche aufzunehmen.
Dienen in der Beschreibung eines Ausführungsbeispiels genannte Merkmale, die
für sich, aber auch zusammen den durch die Erfindung erreichten Erfolg fördern,
der näheren Ausgestaltung der unter Schutz gestellten Erfindung, dann hat es der
Patentinhaber nach der Rechtsprechung des Bundesgerichtshofs in der Hand,
sein Patent durch die Aufnahme einzelner oder sämtlicher dieser Merkmale zu
beschränken; die Kombination muss lediglich in ihrer Gesamtheit eine technische
Lehre darstellen, die der Fachmann den ursprünglichen Unterlagen als mögliche
Ausgestaltung der Erfindung entnehmen kann (BGH X ZR 12/10 vom 30. 08. 2011
- “Antriebseinheit für Trommelwaschmaschine” Rn 30 (m.w.N.)).
Im vorliegenden Fall konnte der Fachmann den ursprünglichen Unterlagen und
ebenso der Patentschrift ohne weiteres eine Multiplexing betreffende allgemeine
Lehre    entnehmen,      ohne    weitere    im    Ausführungsbeispiel        genannte
Beschränkungen.




2.   Die selbständigen Patentansprüche 1, 7, 13, 14 und 15 des Hauptantrags
nehmen die im Streitpatent angegebene Priorität wirksam in Anspruch.
Entsprechendes gilt für die selbständigen Patentansprüche des Hilfsantrags I.


Hierzu wird auf die Erörterungen des Bundesgerichtshofs unter III.1. sowie IV.1.
der BGH-Entscheidung Xa ZR 128/05 (NK11) hingewiesen, denen sich der Senat
anschließt.


Insbesondere wird zur Frage der Offenbarung eines Zeitstempels für jedes
graphische Bild darauf hingewiesen, dass gemäß den Prioritätsunterlagen NI7 auf
S. 19 Abs. 6 jedes Videobild mit mehreren Bitmaps bzw. Bereichen überlagert

                                      - 28 -



werden kann, an beliebigen Positionen und zu beliebigen Zeiten („at any position
and time“). Im Header der zur Übertragung verwendeten PES-Pakete sind
Präsentationszeitstempel vorhanden, welche den Beginn der Präsentationszeit für
die bereichsbezogenen Daten im PES-Paket anzeigen; die Zeitstempel für in einer
Multi-Seite enthaltene Bereiche unterscheiden sich um mehr als 40 msec
(„Presentation_Time_Stamp“, S. 4).


Die oben unter III.1 beschriebenen Überlegungen zur Einteilung eines nur Stillbilder enthaltenden Datenstroms in jeweils nur höchstens ein Stillbild enthaltende
PES-Pakete (mit Zeitstempel im Header) im (in NI7 im Titel der „Page 2 of 4“
erwähnten) MPEG2-Standard gelten im Übrigen auch hier.


Zudem sieht der Senat auch eine Speicherung bzw. einen Speicher für die decodierten Daten beim Empfangsverfahren bzw. im Empfänger (Patentansprüche 7
und 14) als in NI7 offenbart an.
Zwar ist eine Speicherung für die decodierten Daten der NI7 nicht explizit zu
entnehmen. Jedoch soll das System bzw. Verfahren der NI7 in „Integrated
Receiver Decoders“ (IRDs) zum Einsatz kommen, wobei die existierende „On
Screen Display“ (OSD) – Funktionalität ausgenutzt wird und die Bitmap-Dekompression keine zusätzliche speziell zugeschnittene Hardware erfordert,
sondern lediglich ein Firmware-Update (NI7 „Page 2 if 4“ Abs. 1 und le. Abs.,
„Page 3 of 4“ Abs. 1). Der Fachmann las hier einen Speicher für decodierte Daten,
in welchem die decodierten Daten für die nachfolgende Darstellung zu speichern
sind, als in solchen Systemen allgemein üblich mit.


Diesem allgemeinen Verständnis, wonach in IRDs mit OSD-Funktionalität ein
Speicher für decodierte Daten mitzulesen war, stehen auch die aus dem
Prioritätsintervall stammende NI8 sowie die vorveröffentlichte D3 nicht entgegen.
NI8 zeigt als Standardfall einen dem Codierer nachgeordneten Pixelpuffer (6 in
Fig. 3.1). Bei der in Kap. 3 le. Abs. zusätzlich erwähnten Möglichkeit, einen
speziellen Echtzeit-Untertiteldecoder einzusetzen, der ohne Pixelpuffer auskommt,
handelt es sich dagegen um eine spezielle, ungewöhnliche Ausbildung, die sich

                                       - 29 -



dem Fachmann aus den Prioritätsunterlagen NI7 nicht ohne Weiteres erschlossen
hätte.
D3 weist explizit nur für decodierte Videodaten einen Speicher („frame memory 6“)
aus, nicht für decodierte Untertiteldaten; dies liefert jedoch keine Aussage
darüber, ob ein Speicher für decodierte Untertiteldaten vorhanden ist oder nicht.




3. Der Gegenstand des erteilten Patentanspruchs 1 gemäß Hauptantrag ist nicht
neu gegenüber dem aus der Druckschrift D11 (EP 0 677 954 A2) Bekannten.
Entsprechendes gilt für die nebengeordneten Patentansprüche 7, 13, 14 und 15
des Hauptantrags.


Die Druckschrift D11, deren Prioritätstag vor dem Prioritätstag des Streitpatents
liegt, ist gemäß Artikel 54 Abs. 3 EPÜ bei der Neuheitsprüfung zu berücksichtigen.


D11 beschreibt ein System zum Erzeugen von Untertiteldaten und zum
Überlagern der Untertiteldaten (etwa übersetzte Texte für Filme) mit einem
Hauptbild, z. B. einem Fernsehbild, vgl. Sp. 1 Abs. 1 und 2. Ein Untertitel-Datenpaket („sub image display packet“) besteht aus einem Header, den
Untertitel-Bilddaten sowie Steuerdaten, wobei der Header zumindest die
Anzeigelage, die Anzeigegröße und die Anzeigefarbe der anzuzeigenden
Untertiteldaten enthält (Sp. 2 Z. 19 bis 31). Bei den Untertitel-Bilddaten handelt es
sich um (codierte) Pixeldaten (Sp. 2 Z. 7 bis 39; Sp. 8 Z. 34 bis 44 mit Fig. 7),
deren Farben entsprechend den im Header enthaltenen Angaben (insbesondere
Adressen für eine Farbpalette, Sp. 8 Z. 34 bis 57, Fig. 8) eingestellt werden. Die
Untertitel-Steuerdaten geben an, wie die Anzeigelage, die Anzeigegröße und die
Farben der Pixel der Untertiteldaten über mehrere Frames hinweg geändert
werden sollen (Sp. 2 Z. 28 bis 31).


Die Untertitel werden als graphisches Bild in einem durch die Anzeigelage und die
Anzeigegröße    definierten   rechteckigen      Bereich   im   Gebiet   eines   aktiven
Videosignals wiedergegeben, vgl. die in Sp. 1 Abs. 2 angegebene Anwendung auf

                                                  - 30 -



übersetzte Texte für Filme. Die Übertragung der codierten Untertiteldaten für die
Wiedergabe liest der Fachmann mit. Damit sind die Merkmale a) und b) erfüllt.
Die Pixel des Untertitelbereichs werden durch die codierten Daten einzeln definiert
(Sp. 16 Z. 38 u. 39 „bit map data system“; Fig. 7) – Merkmal c).
Die codierten Untertitel-Daten enthalten im Header unter anderem die Größe und
Lage       des   Untertitels,   der        dem    Haupt-Videobild     überlagert   wird,   sowie
Startzeitzuordnungsdaten, die angeben, von welcher anzuzeigenden Einheit
(Frame) des Haupt-Videobildes an die Anzeige des Untertitelbildes gestartet wird
(Sp. 3 Z. 9 bis 21).
Damit ist jedem graphischen Bild (Untertitel) eine Anzeige-Framenummer und
damit eine Startzeit für die Anzeige zugeordnet, so dass Merkmal g) sowie der auf
einen Zeitstempel bezogene Teil des Merkmals f) erfüllt sind.


Allgemein kann mit dem Untertitel-Datenpaket für jede anzuzeigende Einheit (d. h.
jeden Frame) des Hauptbildes Größe, Lage und Farbe des Untertitelanteils
geändert werden (Sp. 2 Z. 35 bis 38, Sp. 16 Z. 32 bis 35), d.h. für den jeweils zum
Frame gehörigen Untertitel sind insbesondere die Größe und die Lage änderbar.
Nachdem jeder Untertitel einem (oder mehreren aufeinander folgenden) Frame(s)
des Hauptbildes zugeordnet ist, sind somit für jeden Untertitel die Parameter
Größe und Lage im Untertitel-Datenpaket enthalten.
Damit ist auch der auf die Größe und die Lage bezogene Teil des Merkmals f)
erfüllt.


Die Beklagte wendet ein, D11 beziehe sich auf ein NTSC-System, also ein
analoges Fernsehsystem, bei dem Halbbilder mit vorgegebener Frequenz
übertragen       würden     und       in    der     Abtastlücke     zusätzliche    Informationen
aufgenommen würden. Im NTSC-System der D11 gebe die Framenummer jeweils
nur die Anzahl der Frames ausgehend vom letzten I-Frame des Hauptbildes an
(D11 Sp. 10 Z. 19 bis 23 iVm Fig. 11), d.h. die Framenummer gelte jeweils nur für
einen relativ kurzen Zeitraum zwischen zwei I-Frames (30 Frames, das entspricht
bei einer Datenrate von 30 Frames pro Sekunde einem Zeitraum von einer
Sekunde).

                                      - 31 -



Beim NTSC-System würden die empfangenen Frames sofort angezeigt, der
Rahmenzähler werde einmal pro Sekunde zurückgesetzt und zähle nur von einem
I-Frame zum nächsten. Eine Systemzeit wie im Streitpatent zur Synchronisation
von Bitmapdaten mit aktiven Videodaten sei nicht vorhanden. Zudem sei mit dem
streitpatentgemäßen System eine Formatumsetzung von einem 50 Hz - auf ein
60 Hz - System problemlos möglich, da die Zeitstempel unverändert blieben. Das
System der D11 erfordere dagegen in diesem Fall eine neue Programmierung.


Dies basiert jedoch auf einem gegenüber der allgemeinen Offenbarung der
Begriffe „Zeitstempel“ im Streitpatent und „Rahmenzähler“ in D11 eingeschränkten
Verständnis. Einerseits ist der Zeitstempel im erteilten Anspruch 1 nicht auf eine
Systemzeit beschränkt, und andererseits ist D11 nicht auf eine Zählung von
wenigen Frames relativ zu jeweils einem aus einer Vielzahl von Stützframes
beschränkt, wie sich aus den folgenden Überlegungen ergibt:


Im Streitpatent enthält Abs. [0011] allgemeine Angaben zum Zeitstempel:
„Transmitting a time stamp representing the time at which said region is to be
displayed allows multilingual subtitles to be transmitted in advance and to be
displayed in exact synchronism with the video signal.” Damit muss auch beim
Streitpatent der Beginn der Anzeige eines Untertitels mit Hilfe des Zeitstempels
letztendlich einem Frame des Haupt-Videobilds zugeordnet werden („to be
displayed in exact synchronism with the video signal“). Demnach fällt auch ein
Rahmenzähler unter den Begriff „Zeitstempel“. Allerdings muss der Zeitstempel
oder Rahmenzähler es gemäß den Angaben in Abs. [0011] prinzipiell erlauben,
mehrsprachige Untertitel im voraus zu übertragen und zur angegebenen Zeit (bzw.
ab dem angegebenen Frame) darzustellen, d.h. der Zeitstempel bzw. Rahmenzähler muss über einen hierfür erforderlichen Zeitraum bzw. eine erforderliche
Rahmenanzahl zählen können.
Eine lediglich den Ausführungsbeispielen zugeordnete spezielle Form eines
Zeitstempels, z.B. als ein auf eine Systemzeit bezogener Zeitstempel (vgl.
Patentschrift Abs. [0031] Z. 23 bis 26 sowie Abs. [0038]), kann dagegen den
allgemeineren Begriff „Zeitstempel“ nicht einschränken.

                                      - 32 -



Aus der Angabe in D11 Sp. 3 Z. 9 und 19 bis 23 „The header portion includes …
sub image display start timing assigning data for assigning from what display unit
of the main image the display of the sub image is started“ (d.h. der Header enthält
Zeitpunkts-Zuordnungsdaten, um festzulegen, ab welchem Frame des Haupt-Videobilds das Untertitelbild angezeigt werden soll) ist in Bezug auf den Rahmenzähler eine allgemeine Lehre zu entnehmen, ohne Beschränkung auf ein kurzes
Zeit- bzw. Rahmenintervall. Das in D11 Fig. 11 mit Beschreibung nur beispielhaft
angegebene NTSC-Verfahren (D11 Sp. 10 Z. 19 und 20 „For example, …, in the
case of the NTSC system …“) mit der Rahmenzählung jeweils nur zwischen
benachbarten I-Frames schränkt die allgemeinere Lehre der D11 nicht ein.


Der in D11 verwendete allgemeine Rahmenzähler entspricht somit dem
Zeitstempel des Streitpatents.


Der von der Beklagten angeführte Vorteil einer einfachen Umstellung zwischen
Systemen mit unterschiedlicher Bildfrequenz ist im Streitpatent nicht erwähnt und
kann deshalb die Interpretation des Zeitstempels nicht einschränken.


Damit ist der erteilte Anspruch 1 (Hauptantrag) durch D11 neuheitsschädlich
getroffen.


Entsprechendes gilt für die nebengeordneten Ansprüche 13 und 15.


Des Weiteren sind auch die Gegenstände der nebengeordneten Ansprüche 7 und
14 nicht neu gegenüber D11.


Ein Decodierverfahren sowie einen Empfänger mit Decodierer las der Fachmann
nämlich in D11 ebenfalls mit. Auch ein Speicher für die decodierten Pixeldaten ist
als in derartigen Systemen üblich mitzulesen (ebenso wie in den Prioritätsunterlagen zum Streitpatent). Im Übrigen sieht die in D11 Sp. 10 Z. 19 und 20 in
Verbindung mit Fig. 11 beispielhaft genannte Fernsehnorm NTSC ein Zeilensprungverfahren vor, was einen Pixelspeicher voraussetzt.

                                         - 33 -



Zu den übrigen Merkmalen der Ansprüche 7 und 14 gelten die obigen
Ausführungen zum Anspruch 1 entsprechend.


Mit    den   Hauptansprüchen    fallen    auch      die   auf   diese   rückbezogenen
Unteransprüche, für die ein eigenständiger erfinderischer Gehalt weder explizit
behauptet noch für den Senat ersichtlich ist und da die Beklagte die Ansprüche
nach    Haupt-   und   Hilfsantrag   jeweils      als   geschlossene    Anspruchssätze
beansprucht.




4. Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag I ist neu gegenüber
dem Stand der Technik und beruht auch auf erfinderischer Tätigkeit.
Entsprechendes gilt für die nebengeordneten Patentansprüche 7, 13, 14 und 15
des Hilfsantrags I sowie die auf sie rückbezogenen Unteransprüche, deren
Patentfähigkeit von den übergeordneten Ansprüchen getragen wird.


4.1 Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag I wird durch die
nach dem Prioritätstag des Streitpatents veröffentlichte Druckschrift D11 nicht
neuheitsschädlich vorweggenommen.
Entsprechendes gilt für die nebengeordneten Patentansprüche 7, 13, 14 und 15
des Hilfsantrags I.


In D11 werden die aktiven Videodaten und die Untertiteldaten bei der Anzeige
gemeinsam dargestellt. D11 ist sehr wenig über die Art der Datenübertragung zu
entnehmen; Sp. 17 Z. 11 bis 13 erläutert, dass die Untertiteldisplaydaten (welche
aber keine Header- und Steuerdaten beinhalten und damit auch keine Größen-,
Lage- und Zeitsteuer-Daten, vgl. Fig. 1 und 2) von der Anzeigeeinrichtung in den
Frame-Intervallen ausgegeben werden. Ob jedoch die codierten Untertiteldaten
und die Hauptbilddaten (aktive Videodaten) überhaupt auf einem gemeinsamen
Weg übertragen werden und auf welche Weise die Datenübertragung geschieht,
ist D11 nicht zu entnehmen. Insbesondere ist in D11 kein Hinweis darauf
erkennbar, aktive Videodaten und Untertiteldaten (die Größen-, Lage- und
Zeitdaten beinhalten) im Multiplex-Verfahren zu verbinden (und gemeinsam zu

                                          - 34 -



übertragen), wie dies in allen selbständigen Patentansprüchen des Hilfsantrags I
gefordert ist.
Die von den Klägerinnen hierzu genannte Fig. 10 in D11 betrifft lediglich die
Farbzuordnung      zu    den   bereits   decodierten   Untertiteldaten   sowie     deren
Überlagerung mit dem Hauptbild zum Zweck der gemeinsamen Darstellung, kann
jedoch ein Multiplexing von codierten Untertiteldaten und aktiven Videodaten nicht
nahelegen.
Zudem zeigt die ebenfalls von den Klägerinnen genannte Fig. 1 (mit „sub image
data packet“) lediglich, dass die codierten Untertiteldaten in Form von Datenpaketen übertragen werden, sagt jedoch nichts über die Art der Übertragung der
aktiven Videodaten aus.


4.2 Auch die übrigen im Verfahren genannten, vor dem Prioritätstag des
Streitpatents veröffentlichten Druckschriften nehmen den Gegenstand des
Patentanspruchs 1 gemäß Hilfsantrag I nicht neuheitsschädlich vorweg und
konnten diesen nicht nahelegen.


Dies ergibt sich daraus, dass diese Druckschriften bereits den Gegenstand des
Patentanspruchs 1 gemäß Hauptantrag nicht neuheitsschädlich treffen und auch
nicht nahelegen konnten, wie im Folgenden gezeigt wird.
Sie können somit auch der Patentfähigkeit des Patentanspruchs 1 gemäß
Hilfsantrag I    nicht   entgegenstehen,      der   alle   Merkmale      des     erteilten
Patentanspruchs 1 enthält sowie eine zusätzliche Einschränkung („a multiplexed
stream comprising active video data and encoded data”).


Entsprechendes gilt für die nebengeordneten Ansprüche 7, 13, 14 und 15.


4.2.1 Die Druckschrift D5 konnte den jeweiligen Gegenstand des Anspruchs 1
nach Hauptantrag und nach Hilfsantrag I nicht vorwegnehmen. Ausgehend von D5
war dieser für den Fachmann auch nicht naheliegend.
Entsprechendes gilt für die nebengeordneten Patentansprüche 7, 13, 14 und 15
des Hilfsantrags I.

                                        - 35 -



D5    betrifft    den   MPEG2-Systemstandard          in    einem     Entwurf        vom
13. November 1994. Im früheren Nichtigkeitsverfahren Xa ZR 128/05 ist der
Bundesgerichtshof nach Befragung des gerichtlichen Sachverständigen, der selbst
an der Entwicklung dieses Standards beteiligt war, zu der Überzeugung gelangt,
dass dieser Entwurf (dortige NK6) jedenfalls am 13. November 1994 und damit vor
dem Prioritätstag des Streitpatents der Fachöffentlichkeit allgemein zugänglich
war (vgl. NK11 S. 12 Abs. 3). Hierauf kommt es hier jedoch nicht an, da D5 die
Patentfähigkeit der Anspruchsfassung gemäß Hilfsantrag I nicht in Frage stellt.


Gemäß D5 können einer oder mehrere Ströme von codierten Video- und Audiosowie anderen Daten zu einzelnen oder mehrfachen, für Speicherung oder
Übertragung      geeigneten   Strömen    kombiniert   werden,    wobei    Zeitstempel
verwendet werden, die u.a. die Decodierung und Darstellung der Daten betreffen
(S. x „Introduction“). Die zu kombinierenden Datenströme (Multiplex) sind in PES
(packetized elementary stream) - Paketen organisiert, die zu einem einzelnen
Strom, insbesondere einem Transportstrom aus Programmen mit unabhängigen
Zeitbasen kombiniert werden können Kap. ( „Introduction“ S. xi Abs. 1, 4 und 5;
Fig. 0-1). Ein PES-Paket besteht aus einem Header und einer Payload (enthaltend
z.B. Videodaten), wobei der Header u.a. einen Zeitstempel für die Darstellung
(presentation time stamp PTS) enthalten kann (vgl. die Definitionen in Kap. 2.1.20
bis 2.1.53 sowie Annex F Fig. F-2).
Eine Videosequenz kann auch aus einem einzigen codierten Bild (Stillbild)
bestehen, dem ein Zeitstempel PTS für die Präsentationszeit zugeordnet ist
(Kap. 2.1.53 “still picture”). In einem Datenstrom können mehrere Stillbilder
enthalten sein, vgl. Kap. 2.6.2 „Video stream descriptor“ mit „still picture flag“
(„…when set to „1“ indicates that the video stream contains only still pictures“).
Der „Target background descriptor“ mit dem „video window descriptor“, welche
insbesondere die Lage eines für die Bilddarstellung vorgesehenen Fensters bzw.
Bereichs enthalten, sind jedoch dem gesamten Datenstrom zugeordnet, also allen
in dem Datenstrom codierten Stillbildern gemeinsam (Kap. 2.6.12 „Target background descriptor“ mit „The video window descriptor is then used to describe, for
the associated stream, the location on the grid …“ und Kap. 2.6.14 “Video window

                                        - 36 -



descriptor”), so dass jedes Stillbild des Datenstroms nach der Decodierung im
Empfänger am selben Ort darzustellen ist.


Gemäß der zur Ergänzung von D5 genannten NI2 (weiterer Teil eines Entwurfs
eines Codierungsstandards für Video- und Audiodaten, mit Datum 25. März 1994)
enthält eine Videosequenz einen Sequenzheader (Tabelle 6.2.2 auf S. 28),
welcher nach Tabelle 6.2.2.1 auf S. 29 u.a. eine Breite und Höhe („horizontal size
value“, „vertical size value“) für die Sequenz umfasst. Eine individuelle Position für
die Sequenz ist dort jedoch nicht vorgesehen.
Selbst wenn man der früheren Nebenintervenientin darin folgen wollte, dass die
individuelle Festlegung bzw. Decodierung der Größe für jede aus einem Stillbild
bestehende Sequenz durch D5 in Kombination mit NI2 nahegelegt wäre, so geht
doch die Festlegung einer individuellen Position für jedes Stillbild (jedes
graphische Bild) bzw. deren Decodierung aus D5 und NI2 nicht hervor und wird
durch diese Druckschriften auch nicht nahegelegt.


Im System der D5 wäre es im Prinzip auch möglich, für jedes Stillbild einen
eigenen Datenstrom vorzusehen, wobei jedem Datenstrom und damit jedem
Stillbild eine eigene Lage zugeordnet werden könnte; dies würde allerdings
einigen Aufwand für die Codierung und Decodierung erfordern (einschließlich der
Synchronisation einer Vielzahl einzelner Datenströme für die einzelnen Stillbilder).
Für eine solche aufwändige Vorgehensweise hätte es eines Anlasses bedurft. Der
Senat kann jedoch ausgehend von D5 keinen Anlass für den Fachmann erkennen,
jedem Stillbild eine eigene Lage zuzuordnen.


Für die Wahl einer anderen Codierungsart für örtlich wechselnde Graphikbilder
(Untertitel), nämlich in einem privaten (freien) Datenstrom ist ebenfalls keine
Anregung erkennbar, auch wenn gemäß D5 grundsätzlich ein (beliebiger) privater
Datenstrom vorgesehen ist (Annex H.0 „Private Data“, S. 118).


Zudem mag es im System der D5 zwar theoretisch möglich sein, in programmspezifischen Informationen (PSI), die wiederholt in Multiplexdaten eingestreut
werden (Kap. C.9 „…interspersing of PSI information with fine granularity in the

                                         - 37 -



multiplexed data“) und in ihrer Mappingtabelle (PMT) Deskriptoren enthalten
können, den „video window descriptor“ kontinuierlich zu ändern, wie die Nebenintervenientin vorbringt (vgl. Eingabe vom 20. März 2017, Kap. 3.2.1). Jedoch ist
zu berücksichtigen, dass gemäß Kap. 2.6.12 die im „video window descriptor“
enthaltene Position der Videodaten jeweils für den gesamten Strom gleich ist,
worauf oben bereits hingewiesen wurde. Eine Anregung, die PSI bzw. PMT in der
zur Erzeugung wandernder Untertitel erforderlichen Geschwindigkeit zu ändern
und hierbei für jedes in einem Datenstrom enthaltene Stillbild neue Positionsdaten
zu verwenden ist D5 nicht zu entnehmen.


Nach alledem lag es für den Fachmann nicht nahe, ausgehend von D5 in den
codierten Daten für jedes graphische Bild eine Information insbesondere über die
Lage des Bereichs vorzusehen, in dem das graphische Bild dargestellt werden
soll, wie dies die Merkmale f), f1), f2), f3) und f4) verlangen.


4.2.2 Auch die Druckschrift D3 konnte den jeweiligen Gegenstand des
Anspruchs 1 nach Hauptantrag und nach Hilfsantrag I nicht vorwegnehmen oder
nahelegen.


D3 bzw. D3a zeigt in Fig. 1 mit Beschreibung die Decodierung von Videodaten,
Audiodaten und Untertiteldaten sowie insbesondere die Filterung der decodierten
Daten. Die in den Untertiteldaten enthaltenen Untertitelsystemdaten enthalten
Informationen wie Untertitelnummer, Erzeugungs- oder Decodierzeit für Untertitel-Bitmapdaten       (etwa   einen    Zeitstempel),    Anzeigeposition    für     Untertitel,
Farbinformation usw.; diese Bestandteile sind in Abs. [0026] pauschal aufgeführt.
Ob sich einzelne Bestandteile jeweils auf ein einzelnes Untertitelbild (ein
graphisches Bild im Sinne des Streitpatents) oder auf eine Untertitelsequenz
(mehrere nacheinander anzuzeigende graphische Bilder) beziehen, ist D3 nicht
eindeutig    zu   entnehmen.      Insbesondere     ist   nicht   entnehmbar,    ob    die
Anzeigeposition für jedes einzelne (graphische) Bild oder nur gemeinsam für eine
Sequenz von graphischen Bildern decodiert wird. Der in Abs. [0023] erwähnte
MPEG Video Decodierer spricht gegen die Möglichkeit „einzelnes Bild“, vgl. die
obigen Ausführungen zu D5. In Zusammenhang damit ist auch das Argument der

                                        - 38 -



Beklagten in ihrer Widerspruchsbegründung in 2 Ni 48/16 nicht von der Hand zu
weisen, dass D3, die sich im Wesentlichen mit der Filterung von decodierten
Daten befasst, die Elemente der Codierung bzw. Decodierung als bekannt
voraussetzt und nur kurz erwähnt, so dass davon auszugehen ist, dass es sich
hierbei um übliche Verfahren und Komponenten handelt.


Die Merkmale f) und f1) sind damit in D3 nicht vollständig erfüllt. Ein Naheliegen
ist angesichts des dem Fachmann damals bekannten (MPEG, MPEG2)-Standards
bzw. Standardentwurfs für Videodaten ebenfalls nicht zu erkennen. Auch in der
von der Beklagten genannten Video CD Spezifikation 2.0 (NB2) ist kein Hinweis
auf eine individuelle Anzeigeposition für Graphikbilder (Stillbilder oder Untertitelbilder) erkennbar.


4.2.3 Auch die Druckschrift D6 in Verbindung mit D7 konnte den jeweiligen
Gegenstand des Anspruchs 1 nach Hauptantrag und nach Hilfsantrag I nicht
vorwegnehmen oder nahelegen.


D6 zeigt die Wiedergabe von auf einem Speichermedium gespeicherten
Videodaten und Audiodaten, welch letztere zusätzlich graphische Codes
(entsprechend graphischen Bildern) als Subcode enthalten. Bei der Wiedergabe
werden die Subcodedaten Stillbildern überlagert, die aus den Videodaten
extrahiert und gespeichert wurden (Fig. 11 und 13 bis 15 mit Beschreibung), wobei
der zeitliche Ablauf der Wiedergabe der in die Audiodaten eingebetteten
Subcodes auf der gespeicherten Reihenfolge beruht und mit der Wiedergabe der
Audiodaten korreliert (Sp. 18 Z. 57 bis Sp. 19 Z. 15); d.h. durch die Einbettung der
Graphikbilder in die Audiodaten ist der zeitliche Ablauf des Abspielens bzw. der
Darstellung   bereits   festgelegt.   Ein   Zeitstempel   für   die   Darstellung   der
Graphikbilder in Bezug zu den Videobildern erscheint hier unnötig.


Ein solcher konnte daher auch durch D7 nicht nahegelegt werden, welche die
Lehre gibt, Videodaten einerseits und Zeichendaten für Untertitel andererseits an
getrennten Speicherorten (Speichermedien) abzulegen und sowohl für die
Videodaten als auch für die Zeichen- bzw. Untertiteldaten Framenummern oder

                                       - 39 -



Zeitstempel mitzuspeichern, um für die Darstellung eine korrekte Zuordnung der
Untertitel zu den Videoframes zu ermöglichen.


4.2.4 Auch die Druckschrift D8 konnte den jeweiligen Gegenstand des Anspruchs
1 nach Hauptantrag und nach Hilfsantrag I nicht vorwegnehmen oder nahelegen.


D8 behandelt mögliche Erweiterungen für einen künftigen Videotextstandard,
unter anderem ein „Alphafotografieverfahren“, das auf punktweise definierten
Bilddaten beruht, die codiert, übertragen und decodiert werden (Kap. 2.3. mit
2.3.1.), und das in künftige Standards europäischer Länder einbezogen werden
soll (Kap. 4.1., 4.2. mit 4.2.4.).
Es ist davon auszugehen, dass die in der Farbtafel 12 auf S. 131 gezeigte alphafotografische Videotextseite mit Bildeinschub des erweiterten UK-Teletextsystems
im Ganzen alphafotografisch codiert und übertragen wird, wie dies auch beim
japanischen und beim kanadischen Alphafotografieverfahren der Fall ist, vgl.
Kap. 2.3 auf S. 121 re. Sp. le. Abs. bis S. 122 li. Sp. Abs. 1 sowie S. 132 li. Sp.
Abs. 1 le. Satz. Hierbei ist es nicht nötig und erscheint auch nicht sinnvoll, in den
codierten Daten Koordinaten (Position und Größe) für den Bildeinschub
mitzucodieren.
Auch wenn aufgrund begrenzter Übertragungsleistung nur Teilbereiche einer
Videotextseite fotografisch übertragen werden (S. 123 li. Sp. Abs. 2), so ist damit
noch keine Anregung gegeben, für jeden übertragenen Bereich eine eigene
Position und Größe mitzucodieren; vielmehr sieht der Fachmann in diesem Fall
eher festgelegte Bereichsgrößen und -abmessungen vor, um möglichst wenig
zusätzliche Daten (Overhead) übertragen zu müssen.


Selbst wenn man der Klägerin zu 2 darin folgen will, dass per Videotext auch
Untertitel für Fernsehprogramme übertragen werden (siehe Klageschriftsatz S. 43
bis 45 sowie Streitpatent Abs. [0002]), so ergibt sich aus D8 keine Anregung, für
jeden Videotext-Untertitel eine speziell diesem zugehörige Position und Größe
vorzusehen, d.h. die Positionen und Größen der einzelnen Untertitel variabel zu
gestalten.

                                          - 40 -



Im Übrigen ist in D8 auch kein Zeitstempel für die Darstellung ausgewiesen.
Hierauf kommt es jedoch nicht mehr an.


4.2.5 Auch die Druckschrift D9 konnte den jeweiligen Gegenstand des Anspruchs
1 nach Hauptantrag und nach Hilfsantrag I nicht vorwegnehmen oder nahelegen.


D9 zeigt die Speicherung von zusätzlichen Untertiteldaten auf Audiodisks, welche
im Wesentlichen Audiodaten (keine Videodaten) enthalten, vgl. S. 1 Z. 4 bis 15,
S. 4 Z. 3 bis 15 sowie die auf S. 2 Z. 13 bis 14 und S. 7 Z. 24 und 25 genannten
Standards, bei denen es sich sämtlich um Audiostandards handelt. Die Untertitel-Texte werden im standardmäßig vorgesehenen Untertitelkanal der Audiodisk
gespeichert und beim Abspielen der Audiodisk auf einem Display wiedergegeben
(S. 4 Z. 19 bis S. 5 Z. 14 iVm Fig. 2).
Das Speichern der Untertitel-Textdaten erfolgt in Form von „packs“ (S. 6 Z. 26ff
i.V.m. Fig. 4 a,b,c), die jeweils einen Header mit Positions- und Größendaten
sowie einem Zeitstempel aufweisen („beginning row“, „beginning column“, „column
width“, „column height“, „start time“; S. 8 Z. 25 bis S. 9 Z. 12, S. 12 Z. 5 bis 20),
wobei für jeden Untertitel ein separater Header vorhanden ist (S. 9 Z. 17 bis 18);
danach folgen die zeichencodierten Textdaten bis zu einer Endmarkierung
(Fig. 4b,c; S. 9 Z. 22 bis S. 10 Z. 9).
Mehrere packs (z.B. je 10 packs) bilden einen Video-Frame. Den Videoframes ist
eine vorgegebene Framegeschwindigkeit zugeordnet, vgl. Appendix 1 auf S. 20
unten
    („#define FRAME_PACKS           10     /* number of packs in a video frame*/“;
        „#define SEC_FRAMES         30     /* number of frames in a second */“).


Somit beschreibt D9 das Speichern von Text-Untertiteldaten auf Audiodisks, wobei
die Untertitel beim Abspielen der Audiodisk zu Videoframes zusammengesetzt
und diese als eine Art Untertitel-Film auf einem Display dargestellt werden (dies ist
offensichtlich mit dem Ausdruck „subtitles for movies“ im Abstract gemeint).

                                          - 41 -



In D9 ist kein Hinweis darauf zu erkennen, Untertiteldaten zusammen mit
Videodaten (statt mit Audiodaten) zu speichern, die Untertiteldaten bei der
Darstellung auf einem Bildschirm in das Gebiet des aktiven Videosignals
einzublenden und die Untertiteldaten nicht als Zeichensymbole, sondern über
individuelle Pixel zu codieren.


4.2.6. Die übrigen Druckschriften D10, D1 und D2 liegen weiter ab und wurden
nur zu Unteransprüchen (D10, mit Farbnachschlagtabelle) genannt oder nicht
weiter für die Argumentation verwendet.


4.3   Auch    die    Argumentation      der    Klägerinnen   zum   Empfänger   des
nebengeordneten Patentanspruchs 14 konnte zu keiner anderen Beurteilung
führen.
Entsprechendes      gilt   für    das   Empfangsverfahren    des   nebengeordneten
Patentanspruchs 7.


Nach Ansicht der Klägerinnen war ein aus D5 bekannter Empfänger bereits in der
Lage, einen Datenstrom zu verarbeiten, der für jedes Stillbild die in Rede
stehenden Daten (Größe, Position und Zeitstempel), insbesondere eine
zugehörige Position enthielt. Wenn ein Empfänger diese Daten für mehrere Bilder
decodieren könne, so könne er dies auch für jedes einzelne Bild tun, wenn er
derartige Daten bekomme. Hierfür seien keine Modifikationen am Empfänger
notwendig.


Dieser Argumentation konnte der Senat sich nicht anschließen.


Wie oben unter 4.2.1 erläutert, ist gemäß D5 ein „Target background grid
descriptor“ mit „video window descriptor“ (Kap. 2.6.12 und Kap. 2.6.14)
vorgesehen, welche insbesondere die Position eines für die Bilddarstellung
vorgesehenen Fensters bzw. Bereichs enthalten und dem gesamten Datenstrom
zugeordnet sind, d.h. allen in dem Datenstrom codierten Stillbildern gemeinsam,
so dass jedes Stillbild des Datenstroms nach der Decodierung im Empfänger am
selben Ort darzustellen ist.

                                       - 42 -



Ein in D5 mitzulesender Empfänger bzw. ein Empfangsverfahren (vgl. etwa
Kap. 0.8.1 „De-multiplexing“) war demnach dazu ausgelegt Datenströme zu lesen
und zu verarbeiten, die pro Datenstrom maximal eine derartige Positionsangabe
enthielten. Es ist davon auszugehen, dass im Fall eines Datenstroms, der mehr
als eine solche Positionsangabe aufweist (welche weiteren Positionsangaben
dann an einer hierfür vom Standard D5 nicht vorgesehenen Stelle des
Datenstroms enthalten sein müssten), der Empfänger mit diesen weiteren
Positionsangaben schlichtweg nicht umgehen konnte, d.h. er konnte sie nicht
decodieren und auch keine entsprechenden Daten für die Darstellung einzelner
Stillbilder des Datenstroms an unterschiedlichen Positionen erstellen; bestenfalls
konnte er die weiteren Positionsangaben ignorieren. Jedenfalls ist D5 kein Hinweis
darauf zu entnehmen einen Empfänger so auszulegen, dass er mit mehr als einer
Position pro Datenstrom im streitpatentgemäßen Sinn umgehen kann.


Entsprechendes gilt für die oben unter 4.2.1 erläuterte theoretische Möglichkeit, in
programmspezifischen Informationen (PSI), die wiederholt in Multiplexdaten
eingestreut werden und in ihrer Mappingtabelle (PMT) Deskriptoren enthalten
können, jeweils unterschiedliche Deskriptoren vorzusehen. Das wiederholte
Einstreuen der PSI ist als eine Art „Einsprunghilfe“ für Empfänger gedacht, die an
beliebigen Stellen im Verlauf der Datenübertragung neu hinzukommen (D5
Kap. C.9 Abs. 1 „in applications where random access is a consideration“).
Nachdem ein in D5 mitzulesender Empfänger bzw. ein Empfangsverfahren
erwartete, dass sich die Deskriptoren in der wiederholt in Multiplexdaten
eingestreuten PSI nicht ändern, ist davon auszugehen, dass er mit dem Fall sich
ändernder Deskriptoren in der PSI nicht umgehen konnte (möglicherweise wertete
er die PSI nicht bei jedem Erscheinen aus) und die Deskriptoren in der PSI
jedenfalls nicht in der Weise berücksichtigte, dass die einzelnen Stillbilder an
jeweils zugehörigen, unterschiedlichen Positionen dargestellt werden.


Somit geht aus D5 kein Empfänger und kein Empfangsverfahren hervor, das pro
Datenstrom mehr als eine Positionsangabe decodiert und die einzelnen Stillbilder
eines Datenstroms an den jeweiligen, unterschiedlichen Positionen wiedergibt.

                                     - 43 -



Ein solcher Empfänger bzw. ein solches Empfangsverfahren war ausgehend von
D5 für den Fachmann auch nicht naheliegend.


Wie ebenfalls oben unter 4.2.1 erläutert, wäre es im System der D5 theoretisch
auch möglich, für jedes Stillbild einen eigenen Datenstrom (mit eigener Position)
vorzusehen. Dies würde allerdings einen hohen Aufwand für die Codierung und
Decodierung (einschließlich der Synchronisation einer Vielzahl einzelner Datenströme für die einzelnen Stillbilder) erfordern und wäre dem Fachmann weder
naheliegend noch überhaupt sinnvoll erschienen. Auch der Stand der Technik gibt
keinerlei Hinweise auf derartig aufgebaute kombinierte Datenströme; es handelt
sich hierbei um eine rein theoretische Möglichkeit, die in der Praxis nicht zu
erwarten ist.
Damit erübrigt es sich darauf einzugehen, ob ein in D5 mitzulesender oder durch
D5 nahegelegter Empfänger bzw. ein entsprechendes Empfangsverfahren mit
solchen rein theoretischen kombinierten Datenströmen hätte umgehen können.
Der Fachmann wird den Anspruch 14 ist nämlich so verstehen, dass der
beanspruchte Empfänger mit codierten Daten umgehen kann, welche die im
Anspruch geforderten Parameter enthalten und auch in der Realität zu erwarten
sind, nicht jedoch mit rein theoretisch konstruierten Daten ohne praktische
Relevanz.




                                       IV.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. §§ 91 Abs. 1 Satz 1,
101 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                     - 44 -



                                       V.


                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG
gegeben.


Die Berufungsfrist beträgt einen Monat. Sie beginnt mit der Zustellung des in
vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von fünf
Monaten nach Verkündung. Die Berufung ist durch einen in der Bundesrepublik
Deutschland zugelassenen Rechtsanwalt oder Patentanwalt schriftlich beim
Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


    - die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
    - die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte
Abschrift des angefochtenen Urteils vorgelegt werden.




Guth          Baumgardt       Dr.Thum-Rung           Dr. Forkel        Heimen

                                                                    RiBPatG Heimen
                                                                    ist an das BMJV
                                                                    abgeordnet und
                                                                        kann nicht
                                                                     unterschreiben

                                                                          Guth
