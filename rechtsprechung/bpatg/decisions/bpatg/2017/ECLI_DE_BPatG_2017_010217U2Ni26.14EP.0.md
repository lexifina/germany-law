---
ecli: "ECLI:DE:BPatG:2017:010217U2Ni26.14EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 26/14"
decided: "2017-02-01"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=5&nr=28746&anz=809&pos=78&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2017-02-01_2_Ni_26_14_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0003.md", "germany/bund/acts/patg/0004.md", "germany/bund/acts/patg/0005.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0263.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 26/14 vom 2017-02-01

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      An Verkündungs Statt
                                                          zugestellt am
2 Ni 26/14 (EP)                                         1. Februar 2017
                                                               …
(Aktenzeichen)




                     In der Patentnichtigkeitssache

 …




 BPatG 253
 08.05

                                            -2-




…
                 betreffend das europäische Patent 0 673 034
                                   (DE 695 31 265)


hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen    Verhandlung      vom    13.    Oktober   2016   unter   Mitwirkung   des
Vorsitzenden Richters Guth sowie der Richterin Hartlieb und der Richter
Dipl.-Phys. Brandt, Dipl. Phys. Dr. Friedrich und Dipl. Phys. Dr. Zebisch


für Recht erkannt:


        I.   Das europäische Patent 0 673 034 wird mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt, dass seine Ansprüche 59 sowie 118
             folgende Fassung erhalten und die Ansprüche 60 bis 88 sich
             auf diese Fassung von Anspruch 59 und die Ansprüche 119
             bis 147 sich auf diese Fassung von Anspruch 118 rückbeziehen:


             „59. A method of reproducing data from an optical disk (100)
                     having
                     a diameter less than 140mm;
                     a thickness of 1,2mm;
                     a plurality of record tracks having data recorded thereon
                       as pits representing information,
                     said tracks being divided into a lead-in area, a program
                       area and a lead-out area;
                     said recorded data being recorded in a control information region and in plural data track regions with
                       said control information region being disposed in said
                       lead-in area or program area, said control information

                       -3-


  region    containing   control   information (122, 123)
  which is table of contents information and said control information region being a table of contents region;
said control information (122, 123) being recorded in a
  first plurality of sectors in said control information region and said user information (121) being recorded
  in a second plurality of sectors in said plural data
  track regions; and
each data track region having a respective start sector;
  said control information including addresses of the
  respective start sectors;
said method comprising the steps of:
rotating said disk (100) to obtain a constant linear velocity;
projecting (212) a pickup light beam through a lens for
  optically reading the rotating disk (100), said pickup
  light beam having a spatial frequency f=λ/2NA,
  where the spatial frequency f is less than the track
  pitch, λ is the wavelength of the pickup light beam
  and NA is the numerical aperture of the lens;
demodulating (215) the data read from said disk (100);
error correcting (216) the demodulated data;
separating (230) the error corrected data into the control information, application table of contents (ATOC)
  information and user information;
using (230) said control information to access and
  read (225) selected user tracks in response to access instructions from a user;
characterized in that
said control information (122, 123) and said user information (102) are recorded as modulated long dis-

                    -4-


  tance error correction encoded data (132) having at
  least eight parity symbols;
said data on the disk (100) is modulated as a run length
  limited (RLL) code and said step of demodulating (215) includes decoding said RLL data, said RLL
  code being a (2, 10) RLL code such that successive
  data transitions are separated by no less than 2 data
  bit cells and by no more than 10 data bit cells and
  said RLL code being recorded as 16-bit information
  words without margin bits provided between the 16-
  bit information words and said step of demodulating (215) converting said 16-bit information words
  into 8-bit information words, and said step of demodulating (215) further comprising storing in each of a
  plurality of tables several 8-bit information words,
  selecting a particular table as a function of a preceding 16-bit information word read from said
  disk (100), and reading out from the selected table
  an 8-bit information word which corresponds to the
  16-bit information word presently read from said
  disk (100); wherein at least one 16-bit information
  word read from the disk corresponds to two different
  8-bit information words one of which is stored in one
  table and the other of which is stored in another table, and wherein said step of selecting further comprises examining the 16-bit information word which
  next follows said presently read 16-bit information
  word to select said one or said other table as a function of said next-following 16-bit information word;
at least some of said plural data track regions contain
  user information (121) including MPEG-compressed
  video   data (102)   and      audio   data (104)   multiplexed (107) with each other;

                          -5-


    the tracks exhibit a pitch in the range between 0,7 µm
      and 0,9 µm;
    an application control information disposed in said program area is used to reproduce selected video and
      audio data from said disk (100), the application control information is application table of contents
      (ATOC) information identifying predetermined parameters of the user information in respective data
      track regions, wherein the MPEG-compressed video
      data in a respective data track region are encoded (102) in a selected one of plural video compression formats, the audio data are encoded (105)
      in a selected one of plural audio formats, and said
      application table of contents (ATOC) information includes plural format identifier data for identifying the
      video compression and audio formats used in each
      data track region.”


„118. Apparatus for reproducing data from an optical
      disk (100) having
    a diameter less than 140mm;
    a thickness of 1,2mm;
    a plurality of record tracks having data recorded thereon
      as pits representing information,
    said tracks being divided into a lead-in area, a program
      area and a lead-out area;
    said recorded data being recorded in a control information region and in plural data track regions with
      said control information region being disposed in said
      lead-in area or program area, said control information
      region containing control information (122, 123)
      which is table of contents information and said con-

                       -6-


  trol information region being a table of contents region;
said control information (122, 123) being recorded in a
  first plurality of sectors in said control information region and said user information (121) being recorded
  in a second plurality of sectors in said plural data
  track regions; and
each data track region having a respective start sector;
  said control information including addresses of the
  respective start sectors;
said apparatus comprising:
means for rotating (225) said disk (100) to obtain a constant linear velocity;
pickup means (212) for projecting a pickup light beam
  through a lens to optically read the rotating
  disk (100), said pickup light beam having a spatial
  frequency f=λ/2NA, where the spatial frequency f is
  less than the track pitch, λ is the wavelength of the
  pickup light beam and NA is the numerical aperture
  of the lens;
demodulating means (215) for demodulating the data
  read from said disk (100);
error correcting means (216) for error correcting the
  demodulated data;
means for separating the error corrected data into the
  control information, application table of contents
  (ATOC) information and user information; and
control means responsive to said control information to
  access and read selected user tracks in response to
  access instructions from a user;
characterized in that
said control information (122, 123) and said user information (102) are recorded as modulated long dis-

                    -7-


  tance error correction encoded data (132) having at
  least eight parity symbols;
said data on the disk (100) is modulated as a run length
  limited   (RLL)   code;       and   said   demodulating
  means (215) includes an RLL decoder, said RLL
  code being a (2, 10) RLL code, such that successive
  data transitions are separated by no less than 2 data
  bit cells and by no more than 10 data bit cells and
  said RLL code being recorded as 16-bit information
  words without margin bits provided between the 16-
  bit information   words       and   said   RLL decoder
  converting said 16-bit information words into 8-bit
  information words and said RLL decoder comprising
  a plurality of storage tables, each for storing several
  8-bit information words, means for selecting a
  particular table as a function of a preceding 16-bit
  information word read from said disk (100), and
  means for reading out from the selected table an 8-
  bit information word which corresponds to the 16-bit
  information word presently read from said disk (100);
  wherein at least one 16-bit information word read
  from the disk corresponds to two different 8-bit information words one of which is stored in one table and
  the other of which is stored in another table, and
  wherein said means for selecting includes means for
  examining the 16-bit information word which next
  follows said presently read 16-bit information word to
  control the selection of said one or said other table
  as a function of said next-following 16-bit information
  word;
at least some of said plural data track regions contain
  user information (121) including MPEG-compressed

                                  -8-


                video   data (102)   and      audio   data (104)   multiplexed (107) with each other;
              the tracks exhibit a pitch in the range between 0,7 µm
                and 0,9 µm;
              an application control information disposed in said program area is used by said control means to reproduce selected video and audio data from said
                disk (100), the application control information is application table of contents (ATOC) information
                identifying predetermined parameters of the user information recorded in respective data track regions,
                wherein the MPEG-compressed video data in a respective data track region are encoded (102) in a
                selected one of plural video compression formats,
                the audio data are encoded (105) in a selected one
                of plural audio formats, and said application table of
                contents (ATOC) information includes plural format
                identifier data for identifying the video compression
                and audio formats used in each data track region.”


       Im Übrigen wird die Klage abgewiesen.


II.    Die    Kosten    des   Rechtsstreits    werden    gegeneinander
       aufgehoben.


III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 120%
       des jeweils zu vollstreckenden Betrages vorläufig vollstreckbar.

                                       -9-


                                Tatbestand


Die Beklagte war eingetragene Inhaberin des am 18. März 2015 durch Zeitablauf
erloschenen, am 17. März 1995 - unter Inanspruchnahme der japanischen Priorität
JP 7 444 594 vom 19. März 1994 - unter der Nummer 95103980.9 beim Europäischen    Patentamt    angemeldeten      und    mit   der    EP 0 673 034 A2   am
20. September 1995 offengelegten sowie am 16. Juli 2003 veröffentlichten europäischen Patents EP 0 673 034 B1 (im Folgenden Streitpatent).


Gegen die Nichtigkeitsklägerin ist wegen Verletzung des Streitpatents Klage erhoben worden.


Das in der Verfahrenssprache Englisch abgefasste Patent mit der Bezeichnung
„Optical disk and method and apparatus for recording and then playing information
back from that disk“ (deutsch: Optische Platte und Methode und Gerät zur Aufzeichnung auf und danach Wiedergabe von Informationen von dieser Platte) wird
vom Deutschen Patent- und Markenamt unter der Registernummer 695 31 265.0
geführt und umfasst 5 selbständige und 142 auf diese selbständigen Ansprüche
direkt oder indirekt rückbezogene Patentansprüche.


Die Klägerin hatte ihre Nichtigkeitsklage zunächst gerichtet gegen die Ansprüche 59, 60 und 64, 65, 75, 83-85 (soweit diese auf einen der Ansprüche 59
oder 60 rückbezogen sind) sowie die Ansprüche 118, 119 und 123, 124, 134,
142-144 (soweit diese auf einen der Ansprüche 118 oder 119 rückbezogen sind).
Mit Schriftsatz vom 30. September 2016 hat sie das Streitpatent nun im Umfang
seiner Ansprüche 59 bis 88 sowie 118 bis 147 angegriffen.


Die Beklagte, die ihr Patent zunächst in der erteilten Fassung sowie gemäß
Schriftsatz vom 2. September 2016 hilfsweise gemäß den Hilfsanträgen I bis VIII
verteidigt hatte, rügt die Klageänderung als verspätet und verteidigt ihr Patent
nunmehr im beschränktem Umfang gemäß dem in der mündlichen Verhandlung
überreichten neuen Hauptantrag sowie gemäß neuen Hilfsanträgen 1, 2, 2 a, 2 b
und 3, die die Hilfsanträge I bis VIII vom 2. September 2016 ersetzen.

                                         - 10 -




Die Klägerin rügt die in der mündlichen Verhandlung überreichten neuen Hilfsanträge 2 a und 2 b als verspätet.


Zum Wortlaut der erteilten angegriffenen Ansprüche wird auf die Streitpatentschrift
EP 0 673 034 B1 Bezug genommen.


Die Ansprüche 59 und 118 des Streitpatents lauten in der beschränkt verteidigten
Fassung gemäß Hauptantrag in der Verfahrenssprache Englisch (mit bei unverändertem Wortlaut eingefügter Gliederung):


  „59. A method of reproducing data from an optical disk (100)
     59.1    having
        59.1.1    a diameter less than 140mm; a thickness of 1,2mm;
        59.1.2    a plurality of record tracks
            59.1.2.1   having data recorded thereon as pits representing information,
            59.1.2.2   said tracks being divided into a lead-in area, a program
                       area and a lead-out area;
            59.1.2.3   said recorded data being recorded in a control information
                       region and in plural data track regions
        59.1.3    with said control information region
            59.1.3.1   being disposed in said lead-in area or program area,
            59.1.3.2   said control information region containing control information (122, 123)
            59.1.3.3   which is table of contents information and
            59.1.3.4   said control information region being a table of contents region;
        59.1.4    said control information (122, 123) being recorded in a first
                  plurality of sectors in said control information region and said
                  user information (121) being recorded in a second plurality of
                  sectors in said plural data track regions; and

                                    - 11 -


     59.1.5   each data track region having a respective start sector; said control information including addresses of the respective start sectors;
  59.2   said method comprising the steps of:
     59.2.1   rotating said disk (100) to obtain a constant linear velocity;
     59.2.2   projecting (212) a pickup light beam through a lens for optically
              reading the rotating disk (100), said pickup light beam having a
              spatial frequency f=λ/2NA, where the spatial frequency f is less
              than the track pitch, λ is the wavelength of the pickup light beam
              and NA is the numerical aperture of the lens;
     59.2.3   demodulating (215) the data read from said disk (100);
     59.2.4   error correcting (216) the demodulated data;
     59.2.5   separating (230) the error corrected data into the control information, application table of contents (ATOC) information and
              user information;
     59.2.6   using (230) said control information to access and read (225) selected user tracks in response to access instructions from a user;
characterized in that
  59.3   said control information (122, 123) and said user information (102) are
         recorded as modulated long distance error correction encoded
         data (132) having at least eight parity symbols;
  59.4   at least some of said plural data track regions contain user information (121) including MPEG-compressed video data (102) and audio
         data (104) multiplexed (107) with each other;
  59.5   the tracks exhibit a pitch in the range between 0,7 µm and 0,9 µm;
     59.6.1   an application control information disposed in said program area
              is used to reproduce selected video and audio data from said
              disk (100),
     59.6.2   the application control information is application table of contents
              (ATOC) information identifying predetermined parameters of the
              user information in respective data track regions,

                                      - 12 -


     59.6.3   wherein the MPEG-compressed video data in a respective data
              track region are encoded (102) in a selected one of plural video
              compression formats, the audio data are encoded (105) in a selected one of plural audio formats,
     59.6.4   and said application table of contents (ATOC) information includes plural format identifier data for identifying the video compression and audio formats used in each data track region.”


„118. Apparatus for reproducing data from an optical disk (100)
  118.1 having
     118.1.1 a diameter less than 140mm; a thickness of 1,2mm;
     118.1.2 a plurality of record tracks
        118.1.2.1     having data recorded thereon as pits representing information,
        118.1.2.2     said tracks being divided into a lead-in area, a program
                      area and a lead-out area;
        118.1.2.3     said recorded data being recorded in a control information
                      region and in plural data track regions
     118.1.3 with said control information region
        118.1.3.1     being disposed in said lead-in area or program area,
        118.1.3.2     said control information region containing control information (122, 123)
        118.1.3.3     which is table of contents information and
        118.1.3.4     said control information region being a table of contents region;
     118.1.4 said control information (122, 123) being recorded in a first
              plurality of sectors in said control information region and said
              user information (121) being recorded in a second plurality of
              sectors in said plural data track regions; and
     118.1.5 each data track region having a respective start sector; said control information including addresses of the respective start sectors;
  118.2 said apparatus comprising:

                                   - 13 -


  118.2.1 means for rotating(225) said disk (100) to obtain a constant linear
           velocity;
  118.2.2 pickup means (212) for projecting a pickup light beam through a
           lens to optically read the rotating disk (100), said pickup light
           beam having a spatial frequency f=λ/2NA, where the spatial frequency f is less than the track pitch, λ is the wavelength of the
           pickup light beam and NA is the numerical aperture of the lens;
  118.2.3 demodulating means (215) for demodulating the data read from
           said disk (100);
  118.2.4 error correcting means (216) for error correcting the demodulated
           data;
  118.2.5 means for separating the error corrected data into the control
           information, application table of contents (ATOC) information and
           user information; and
  118.2.6 control means responsive to said control information to access
           and read selected user tracks in response to access instructions
           from a user;
  characterized in that
118.3 said control information (122, 123) and said user information (102) are
      recorded as modulated long distance error correction encoded
      data (132) having at least eight parity symbols;
118.4 at least some of said plural data track regions contain user information (121) including MPEG-compressed video data (102) and audio
      data (104) multiplexed (107) with each other;
118.5 the tracks exhibit a pitch in the range between 0,7 µm and 0,9 µm;
  118.6.1 an application control information disposed in said program area
           is used by said control means to reproduce selected video and
           audio data from said disk (100),
  118.6.2 the application control information is application table of contents
           (ATOC) information identifying predetermined parameters of the
           user information recorded in respective data track regions,
  118.6.3 wherein the MPEG-compressed video data in a respective data
           track region are encoded (102) in a selected one of plural video

                                          - 14 -


                    compression formats, the audio data are encoded (105) in a selected one of plural audio formats,
        118.6.4 and said application table of contents (ATOC) information includes plural format identifier data for identifying the video compression and audio formats used in each data track region.”


Hinsichtlich des Wortlauts der weiteren Patentansprüche wird auf die Patentschrift
EP 0 673 034 B 1 verwiesen.


Anspruch 59 nach Hilfsantrag 1 unterscheidet sich von Anspruch 1 nach Hauptantrag dadurch, dass zwischen die Merkmale 59.3 und 59.4 der Merkmalskomplex 59.7 eingefügt ist. Dieser lautet:


     „59.7 said data on the disk (100) is modulated as a run length limited (RLL)
            code and said step of demodulating (215) includes decoding said RLL
            data,
        59.7.1      said RLL code being a (2, 10) RLL code such that successive
                    data transitions are separated by no less than 2 data bit cells and
                    by no more than 10 data bit cells and
        59.7.2      said RLL code being recorded as 16-bit information words without margin bits provided between the 16-bit information words
                    and
        59.7.3      said step of demodulating (215) converting said 16-bit information words into 8-bit information words;”


In Anspruch 118 des Hilfsantrags 1 ist ein Merkmalskomplex 118.7 mit den zum
Merkmalskomplex 59.7 entsprechenden Merkmalen zwischen die Merkmale 118.3
und 118.4 eingefügt. Dieser Merkmalskomplex lautet:


     „118.7 said data on the disk (100) is modulated as a run length limited (RLL)
            code; and said demodulating means (215) includes an RLL decoder,

                                          - 15 -


       118.7.1 said RLL code being a (2, 10) RLL code, such that successive
                 data transitions are separated by no less than 2 data bit cells and
                 by no more than 10 data bit cells and
       118.7.2 said RLL code being recorded as 16-bit information words without margin bits provided between the 16-bit information words
                 and
       118.7.3 said RLL decoder converting said 16-bit information words into 8-
                 bit information words;”


Bei den Ansprüchen 59 und 118 des Hilfsantrags 2 enthalten die Merkmalskomplexe 59.7 bzw. 118.7 noch weitere einschränkende Merkmale, die jeweils an das
Ende des jeweiligen Komplexes angefügt sind. Sie lauten:


       „59.7.4   and said step of demodulating (215) further comprising storing in
                 each of a plurality of tables several 8-bit information words,
       59.7.5    selecting a particular table as a function of a preceding 16-bit
                 information word read from said disk (100), and
       59.7.6    reading out from the selected table an 8-bit information word
                 which corresponds to the 16-bit information word presently read
                 from said disk (100);”
bzw.
       „118.7.4 and said RLL decoder comprising a plurality of storage tables,
                 each for storing several 8-bit information words,
       118.7.5 means for selecting a particular table as a function of a preceding
                 16-bit information word read from said disk (100), and
       118.7.6 means for reading out from the selected table an 8-bit information
                 word which corresponds to the 16-bit information word presently
                 read from said disk (100);”


Beim Hilfsantrag 2 a sind an die Merkmalskomplexe 59.7 und 118.7 des Hilfsantrags 2 noch jeweils weitere Merkmale angefügt. Sie lauten:

                                        - 16 -


        „59.7.7   wherein at least one 16-bit information word read from the disk
                  corresponds to two different 8-bit information words one of which
                  is stored in one table and the other of which is stored in another
                  table,
        59.7.8    and wherein said step of selecting further comprises examining
                  the 16-bit information word which next follows said presently read
                  16-bit information word to select said one or said other table as a
                  function of said next-following 16-bit information word.”
bzw.
        „118.7.7 wherein at least one 16-bit information word read from the disk
                  corresponds to two different 8-bit information words one of which
                  is stored in one table and the other of which is stored in another
                  table,
        118.7.8 and wherein said means for selecting includes means for examining the 16-bit information word which next follows said presently
                  read 16-bit information word to control the selection of said one or
                  said other table as a function of said next-following 16-bit information word.”


Zum damit sich insgesamt ergebenden Anspruchstext wird auf den Tenor verwiesen. Hinsichtlich des Wortlauts der weiteren Hilfsanträge 2 b und 3 wird auf den
Akteninhalt verwiesen.


Soweit die Klägerin das Streitpatent im Umfang seiner Ansprüche 59, 60 und 64,
65, 75, 83 bis 85 (soweit diese auf einen der Ansprüche 59 oder 60 rückbezogen
sind) sowie der Ansprüche 118, 119 und 123, 124, 134, 142 bis 144 (soweit diese
auf einen der Ansprüche 118 oder 119 rückbezogen sind) angreift, stützt sie ihre
Klage auf die Nichtigkeitsgründe der unzulässigen Erweiterung gegenüber der
ursprünglichen Offenbarung, der fehlenden Ausführbarkeit und der mangelnden
Patentfähigkeit auf Grund fehlender Neuheit sowie fehlender erfinderischer Tätigkeit.


Sie stützt ihr Vorbringen auf die nachstehend genannten Dokumente:

                                     - 17 -


NK1     EP 0 673 034 B1 (Streitpatentschrift);
NK1a    DE 695 31 265 T2 (deutsche Übersetzung der Streitpatentschrift);
NK2     ursprüngliche Anmeldeunterlagen zur EP 0 673 034;
NK3     Englischsprachige Übersetzung der japanischen Patentanmeldung JP 6-074 445 A (Prioritätsanmeldung);
NK4     DPMA-Registerauszug zum Aktenzeichen 695 31 265.0 vom
        1. Dezember 2014;
NK5     Verletzungsklageschrift der Sony Corporation gegen die Medion AG vom 20. August 2014;
NK6     EP 0 536 764 A1;
NK7     US 5 276 674 A;
NK8a    EPA-Prüfungsbescheid vom 29. Juni 2001;
NK8b    EPA-Prüfungsbescheid vom 23. Januar 2002;
NK8c    Anspruchssatz aus dem Prüfungsverfahren vor dem EPA;
NK8d    Merkmalsgegenüberstellung             zwischen   Anspruch 118   des
        Streitpatents und NK8c;
NK9     M. Matuszak: „Video von der CD”; in Funkschau 18/1993,
        S. 120 bis 125;
NK10    R.   Steinmetz:      „Multimedia-Technologie“,      Springer-Verlag
        Berlin Heidelberg, 1993, ISBN 3-540-56724-0, S. V bis VII
        und 124 bis 194;
NK11    International Standard IEC 908 „Compact disc digital audio
        system“, first edition 1987, ungerade, englischsprachige S. 1
        bis 5 und 9 bis 37, 52, 53;
NK12    K.C. Pohlmann: „The Compact Disc Handbook“, 2nd edition,
        ISBN 0-89579-300-8, A-R Editions Inc., Madison, Wisconsin,
        1992, S. 47 bis 99, 103 bis 108, 213 bis 242;
NK12a   K. Pohlmann: “Compact Disc Handbuch”,
        ISBN        3-88322-500-2,     1. Auflage,   IWT    Verlag   GmbH,
        Vaterstetten bei München, 1994, S. 5, 57 bis 113, 209 bis 237;
NK13    Wikipedia-Artikel            „Numerische         Apertur“       vom
        23. September 2014;

                                       - 18 -


NK14    K.A. Schouhamer Immink: „Runlength-Limited Sequences“; in:
        Proceedings of the IEEE, Vol. 78, No. 11, November 1990,
        S. 1745 bis 1759;
NK15    K.A. Schouhamer Immink: „Error Detecting Runlength-Limited
        Sequences”; in: IEEE Proceedings of the Eighth International
        Conference on Video, Audio and Data Recording, Birmingham
        24.-26. April 1990, S. 176 bis 182;
NK16    M. Mattavelli: „Low Frequency Suppression in RLL Codes for
        Optical Recording“; in: IEEE Proceedings of the Eighth International Conference on Video, Audio and Data Recording,
        Birmingham 24.-26. April 1990, S. 109 bis 115;
NK17    US 5 239 531 A;
NK18    N. Eguchi and Y. Akiyama: „High Density Optical Disk System
        Using Variable Five Modulation and SHG Green Laser“: in:
        IEEE Conference Digest of the Joint International Symposium
        on Optical Memory and Optical Data Storage, Maui, Hawaii,
        5.-9. Juli 1993, S. 55, 56;
NK19    Standard ECMA-119, Volume and File Structure of CDROM
        for Information Interchange, December 1986;
NK20    JP 4-358 356 A;
NK20a   Englischsprachige Maschinenübersetzung der NK20;
NK21    WO 94/07 332 A1;
NK22    EP 0 606 868 A2;
NK23    „Compact Disc Interactive – Full Functional Specification“,
        Philips Consumer Electronics B.V., May 1994, S. ii, TOC-1,
        TOC-3, I-I, I-1 bis I-3, III-I bis III-iv, III-1 bis III-8, IX-iii bis
        IX-viii, IX-1 bis IX-5, IX-7 bis IX-22, IX-53 bis IX-57, IX-61 bis
        IX-65, IX-79 bis IX-82;
NK23a   erweiterter Auszug der NK23, S. ii, TOC-1, TOC-3, I-i, I-1 bis
        I-7, II-i, II-iii, II-v, II-vii, II-1 bis II-15, II-37 bis II-39, III-i, III-iii,
        III-1 bis III-31, IV-i, IV-iii, IV-v, IV-1 bis IV-6, V-i, V-iii, V-v, V-vii,
        V-ix, V-xi, V-xiii, V-xv, V-xvii, V-1, V-18, V-94 bis V-97, IX-i,

                                   - 19 -


       IX-iii bis IX-viii, IX-1 bis IX-5, IX-7 bis IX-22, IX-53 bis IX-57,
       IX-61 bis IX-65, IX-79 bis IX-82;
NK24   Optical Storage Technology Association: “Universal Disk
       FormatTM Specification”, Revision 1.02, 30. August 1996,
       S. i bis iii, 1 bis 3, 89 bis 93;
NK25   Wikipedia-Artikel „DVD-Video“, 11. November 2014;
NK26   Merkmalsanalyse zu den Ansprüchen 118, 119, 123, 124,
       134, 142-144;
NK27   DVD Specifications for Read-Only Disc, Part 3, Video
       Specifications, Version 1.1, December 1997, S. VI-0, VI-I, VI-I
       bis VI-xiv, VI1-1 bis VI1-3, VI-2-1, VI3-1 bis VI3-4, VI4-82,
       VI4-83, VI4-98 bis VI4-103;
NK28   Replik des Verletzungsverfahrens One-Red LLC ./. Vestel
       Germany       GmbH        vor       dem   Landgericht   Mannheim,
       Az. 7 O 153/14, 20. Februar 2015;
NK29   EP 1 336 963 A2;
NK30   Stellungnahme zum Verfahren 7 O 153/14 LG Mannheim von
       Richter am BGH a. D. Alfred Keukenschrijver;
NK31   H.Nakajima und H.Ogawa: „Compact Disc Technology“,
       Ohmsha, Ltd., Tokio, 1992, ISBN 4-274-03347-3, S. vii-x,
       197-208;
NK32   J. van der Meer: „The Full Motion System for CD-I“. In: IEEE
       Transactions on Consumer Electronics, Vol 38, No. 4, 1992,
       S. 910-920;
NK33   Philips International B.V., Eindhoven, Firmenschrift: “An Introduction to Compact Disk-Interactive, Januar 1987;
NK34   Schriftsatz der Beklagten vom 13. Mai 2015 aus dem parallelen Verletzungsprozess One-Red LLC ./. Vestel Germany vor
       dem Landgericht Mannheim Az. 7 O 153/14;
NK35   Erläuterungen zum „High Sierra Group Level 2 Datei- und Verzeichnisstruktur gemäß Anlage NK19;
NK36   M.C.Gupta und J. Ballato: „The Handbook of Photonics“, CRC
       Press, Boca Raton, 2007, S. 15-33;

                                           - 20 -


     NK37     Brief von Bert Gall, Philips Consumer Electronics B.V. an CD
              licensees und CD Information Agreement Holders vom
              14. Juni 1993;
     NK38     Wikipedia-Artikel „Eight-to-Fourteen-Modulation“,
              https://de.wikipedia.org/wiki/Eight-toFourteen-Modulation, vom
              27. September 2016;
     NK39     DVD Specifications for Read-Only Disc, Part 1, Physical
              Specifications,      Version 1.01,    December 1997,     S. PH-0,
              PH-52-1 bis PH-62;
     NK40     US 5 696 505 A mit US 5 696 505 C1;
     NK41     K.A. Schouhamer Immink: „Coding techniques for Digital
              Recorders,        Prentice     Hall   International   (UK)   Ltd.,
              ISBN 0-13-140047-9, 5. Auflage 1995, S.81 bis 117.


Die Nichtigkeitsklägerin macht in ihrem Klageschriftsatz und mit ihren späteren
Schriftsätzen insbesondere geltend, dass
     der Gegenstand des Anspruchs 118 über den Inhalt der Anmeldung in der
      ursprünglich eingereichten Fassung hinausgehe, was analog auch für das
      Verfahren des Anspruchs 59 gelte;
     der Gegenstand des Anspruchs 118 des Streitpatents gegenüber der
      Zusammenschau der Lehren der Druckschriften NK9 mit NK7 auf keiner erfinderischen Tätigkeit des Fachmanns beruhe, was wiederum analog für das
      Verfahren des Anspruchs 59 gelte;
     der Gegenstand des Anspruchs 118 des Streitpatents gegenüber der
      Zusammenschau der Lehren der Druckschriften NK6, NK7, welche bereits
      im Patentprüfungsverfahren genannt worden waren, und NK9 auf keiner erfinderischen Tätigkeit des Fachmanns beruhe, was auch hier analog für das
      Verfahren des Anspruchs 59 gelte;
     der Gegenstand des Anspruchs 118 des Streitpatents sowie auch das
      Verfahren des Anspruchs 59 durch die Zusammenschau der Lehren der
      Druckschriften NK23 und NK7 nahegelegt seien;
     die abhängigen Ansprüche 119, 123, 124, 134, 142 bis 144 nicht
      rechtsbeständig seien, da ihre Merkmale bereits aus den Druckschriften

                                       - 21 -


       NK6, NK9, NK10 und NK12 bis NK19, NK22 und NK23 bekannt seien, so
       dass auch die Gegenstände dieser Ansprüche nahegelegt seien. Für die
       Verfahrensansprüche 60, 64, 65, 75 und 83 bis 85 gelte dies entsprechend;
      der Gegenstand des Anspruchs 118 über die Offenbarung der prioritätsbegründenden Anmeldung NK3 hinausgehe, so dass die Priorität zu Unrecht in
       Anspruch genommen werde. Dies gelte analog für das Verfahren des Anspruchs 59;
      der Gegenstand des Anspruchs 118 durch die Teilungsanmeldung aus der
       Anmeldung des Streitpatents NK29 neuheitsschädlich vorweggenommen
       werde („poisonous divisional“). Dies gelte auch für alle weiteren angegriffenen Ansprüche.


Hinsichtlich der Klageerweiterung, mit der zusätzlich weitere Unteransprüche angegriffen werden, macht die Klägerin lediglich geltend, dass die unabhängigen
Ansprüche 59 und 118, auf die die Unteransprüche rückbezogen sind, unzulässig
erweitert seien. Die Erweiterung der Klage auf die Unteransprüche 61-63, 66-74,
76-82, 86-88 und 120-122, 125-133, 135-141, 145-147 erfolge vor dem Hintergrund, dass sich die Beklagte als Verletzungsklägerin im Rahmen des parallel anhängigen Verletzungsverfahren gegen die Nichtigkeitsklägerin auch auf diese
Unteransprüche berufen könne.


Die Ansprüche in der Fassung gemäß neuem Hauptantrag sowie den neuen Hilfsanträgen seien ursprünglich nicht offenbart und nicht patentfähig.


Die Klägerin stellt den Antrag,


        das europäische Patent 0 673 034 im Umfang seiner Ansprüche 59 bis 88 sowie 118 bis 147 mit Wirkung für das Hoheitsgebiet
        der Bundesrepublik Deutschland für nichtig zu erklären.

                                        - 22 -


Die Beklagte stellt den Antrag,


         das europäische Patent 0 673 034 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig
         zu erklären, dass seine Ansprüche 59 und 118 die Fassung gemäß Hauptantrag, eingereicht in der mündlichen Verhandlung,
         hilfsweise die Fassung eines der Hilfsanträge 1, 2, 2 a, 2 b, 3, eingereicht in der mündlichen Verhandlung, erhalten und die angegriffenen Unteransprüche sich auf die jeweilige Fassung der übergeordneten Ansprüche 59 bzw. 118 rückbeziehen.


Die Beklagte erklärt, dass sie den Hauptantrag und die Hilfsanträge jeweils als geschlossene Anspruchssätze ansieht, die sie jeweils in ihrer Gesamtheit beansprucht.


Die Beklagte stellt weiter hilfsweise den Antrag,


         die mündliche Verhandlung zu vertagen.


Der Vertreter der Beklagten erklärt, er habe sich nach der Klageerweiterung nicht
mit seiner Mandantin über die Stellung von Hilfsanträgen verständigen können.


Die Beklagte, die die Ansprüche 118 und 59 ihres Patents nunmehr beschränkt in
der Fassung gemäß Hauptantrag und hilfsweise mit 5 Hilfsanträgen verteidigt, tritt
der Argumentation der Klägerin im Übrigen in vollem Umfang entgegen und begründet dies im Einzelnen. Sie unterstützt ihre Argumentation durch die Dokumente:


      NB1      Liste zur Anlagenkonkordanz;
      NB2      Entscheidung der Beschwerdekammer des Europäischen
               Patentamts T 1222/11 – 3.3.07 vom 4. Dezember 2012;
      NB3      Stellungnahme      der   großen      Beschwerdekammer      des
               Europäischen Patentamts vom 31. Mai 2001 G2/98;

                                           - 23 -


      NB4        R. Teschemacher: „Poisonous divisionals – ein Gespenst
                 verschwindet?“; in: Mitt. Heft 1/2014, S. 16 bis 18;
      NB5        K. Bacher, Vortrag auf der GRUR-Tagung 2014, Folie 15;
      NB6        Wikipedia-Artikel „MPEG-2“;
      NB7        Tufty the Cat G/15 Amicus Briefs vom 28. September 2016.


Sie ist im Wesentlichen der Ansicht, dass die geltend gemachten unzulässigen
Erweiterungen nicht gegeben seien und das Streitpatent jedenfalls in einer der
Fassungen der Hilfsanträge patentfähig sei. Dies werde auch nicht durch eine
vermeintliche „poisonous divisional“ in Frage gestellt. Nach der neueren Rechtsprechung der Beschwerdekammern des Europäischen Patentamtes sei diese für
die hier vorliegende Fallgruppe ausgeschlossen.


Wegen der weiteren Einzelheiten des Vorbringens der Beteiligten wird auf den
Akteninhalt verwiesen.




                          Entscheidungsgründe


                                            A


Die Klage ist im geltenden Umfang zulässig. Ferner sind die geltenden Hilfsanträge 1, 2, 2 a, 2 b und 3 trotz der gegenteiligen Darlegungen der Klägerin zu berücksichtigen.


1. Dies gilt insbesondere auch insoweit, als die Klägerin die Nichtigkeitsklage
über die zunächst mit der Klageschrift angegriffenen Patentansprüche 59, 60 und
64, 65, 75, 83-85 (soweit diese auf einen der Ansprüche 59 oder 60 rückbezogen
sind) sowie die Ansprüche 118, 119 und 123, 124, 134, 142-144 (soweit diese auf
einen der Ansprüche 118 oder 119 rückbezogen sind) des Streitpatents hinaus mit
Schriftsatz vom 30. September 2016 auf die Patentansprüche 59 bis 88 sowie 118
bis 147 des Streitpatents erweitert hat.

                                      - 24 -


Die Einbeziehung eines echten Unteranspruchs ist eine Änderung des Streitgegenstands und damit eine Klageänderung (BGH GRUR 2008, 90 - Verpackungsmaschine). Die vorliegende Klageänderung ist nach § 99 Abs. 1 PatG i. V. m.
§ 263 Abs. 1 ZPO zulässig, da sie nach Auffassung des Gerichts sachdienlich ist
(vgl. dazu Busse/Keukenschrijver, Patentgesetz, 8. Auflage, § 82 Rdnr. 32). Die
Sachdienlichkeit ist hier zu bejahen, da der bisherige Prozessstoff als Entscheidungsgrundlage verwertbar bleibt, und ein weiterer Rechtsstreit vermieden werden
kann (BGH GRUR 2010, 901 Tz. 8 - Polymerisierbare Zementmischung; BGH
GRUR 2008, 90, Tz. 11 - Verpackungsmaschine). Die Klageänderung betrifft weitere Unteransprüche und stützt sich auf den zuvor schon geltend gemachten
Nichtigkeitsgrund der unzulässigen Erweiterung, welche ursächlich in den selbständigen Ansprüchen bestehe, auf die sich diese Unteransprüche zurückbeziehen, so dass insoweit der bisherige Prozessstoff zugrunde gelegt werden kann.
Vor dem Hintergrund des bereits anhängigen Verletzungsverfahrens kann eine
Einbeziehung auch dieser Unteransprüche durch die Verletzungsklägerin nicht
ausgeschlossen werden.


Die Klageänderung i. S. d. § 263 ZPO unterliegt grds. der Präklusion des § 83
(BPatG GRURPrax 2013, 44 - Ofen), wonach die Möglichkeit besteht, verspätetes
Vorbringen zurückzuweisen. Hierfür ist es aber stets erforderlich, dass dieser Vortrag tatsächliche oder rechtliche Fragen aufkommen lässt, die in der mündlichen
Verhandlung nicht oder nur mit unverhältnismäßigem Aufwand zu klären sind.
Kann das an sich verspätete Vorbringen dagegen noch ohne Weiteres in die
mündliche Verhandlung einbezogen werden, ohne dass es zu einer Verfahrensverzögerung kommt, liegen die Voraussetzungen für eine Zurückweisung nach
§ 83 Abs. 4 PatG nicht vor (vgl. BPatG Urt. v. 15. 11. 2011 - 3 Ni 27/10;
Busse/Keukenschrijver PatG 8. Aufl., § 83 Rn. 21, 22).


Im vorliegenden Fall wurden keine Fragen in tatsächlicher und rechtlicher Hinsicht
aufgeworfen, welche die sachgerechte Vorbereitung des Termins erheblich erschwert haben bzw. in der Verhandlung nicht oder nur mit unverhältnismäßigem
Aufwand zu klären gewesen wären und dementsprechend eine Vertagung erforderlich gemacht hätten. Vielmehr konnte die Erörterung und Beurteilung der Pa-

                                       - 25 -


tentfähigkeit der zusätzlich angegriffenen Unteransprüche mit dem im Verfahren
befindlichen Stand der Technik ohne weiteres in die mündliche Verhandlung einbezogen werden. Für den Senat bestand daher keine Veranlassung, die Erweiterung der Klage auf die weiteren Unteransprüche nach § 83 Abs. 4 PatG als verspätet zurückzuweisen.


2.   Einer Zulässigkeit der Klage steht auch nicht das Erlöschen des Streitpatents
wegen Zeitablaufs entgegen. Das insoweit erforderliche Rechtsschutzbedürfnis
ergibt sich daraus, dass die Klägerin von der Beklagten wegen Verletzung des
Streitpatents gerichtlich in Anspruch genommen wird. Dies gilt auch in Bezug auf
die erst mit Schriftsatz vom 30. September 2016 angegriffenen Unteransprüche.
Die Klägerin hat insoweit ausreichend dargelegt, dass sie auch für die Klageänderung ein schutzwürdiges Interesse an der Durchführung des Nichtigkeitsverfahrens hat. Dieses liegt vor, wenn sie als Patentverletzer in Anspruch genommen
wird oder eine solche Inanspruchnahme befürchten muss (vgl. BGH GRUR 2010,
1084, Tz. 10 - Windenergiekonverter). Die Klägerin hat erklärt, dass sie befürchtet,
dass die Verletzungsklägerin sich auf die bislang nicht angegriffenen Unteransprüche beruft. Vor dem Hintergrund, dass jedenfalls die Fälle eines ersichtlich
fehlenden Rechtsschutzbedürfnisses für eine Klage gegen ein erloschenes Patent
- wenn der Patentinhaber auf alle Ansprüche aus dem Patent verzichtet hat oder
eine Inanspruchnahme aus dem Schutzrecht ernsthaft nicht in Betracht kommt
(vgl. BGH GRUR 1995, 342, 343 - Tafelförmige Elemente) – auszuschließen sind,
hat die Klägerin ihr Rechtsschutzbedürfnis im vorliegenden Fall nach Ansicht des
Senats im ausreichenden Umfang begründet.


3.   Die von der Beklagten in der mündlichen Verhandlung am 13. Oktober 2016
zur hilfsweisen Verteidigung des Streitpatents gestellten Hilfsanträge 2 a und 2 b
sind nicht - wie von der Klägerin gerügt - gemäß § 83 Abs. 4 PatG als verspätet
zurückzuweisen, da die erforderlichen Voraussetzungen hierfür nicht vorliegen.


Der Vortrag der Beklagten hat keine tatsächlichen oder rechtlichen Fragen aufkommen lassen, die in der Verhandlung nicht oder nur mit unverhältnismäßigem
Aufwand zu klären gewesen wären und dementsprechend eine Vertagung erfor-

                                        - 26 -


derlich gemacht hätten. Die Ansprüche gemäß den neuen Hilfsanträgen 2 a und 2
b enthalten zwar Änderungen gegenüber den bereits (schriftsätzlich) erörterten,
fristgerecht eingereichten ursprünglichen Hilfsanträgen, doch hat die Klägerin vor
der mündlichen Verhandlung im Rahmen ihrer Klageerweiterung die nunmehr in
die Ansprüche 59 und 118 als weitere Merkmale aufgenommenen Unteransprüche 86 und 87 bzw. 145 und 146 nur in Bezug auf die Unzulässigkeit der Ansprüche angegriffen. Die Patentfähigkeit wurde nicht angegriffen. Es war somit zu erwarten, dass die Beklagte die nach Ansicht der Klägerin bestehende Unzulässigkeit zu beseitigen versucht und entsprechend korrigierte Hilfsanträge formuliert,
indem Merkmale hinzugefügt werden, deren Patentfähigkeit nicht angegriffen
wurde. Die Klägerin musste somit auf ihre Klageänderung hin mit einer entsprechenden Reaktion der Beklagten und neuen Hilfsanträgen im vorgegebenen
Rahmen rechnen. Für den Senat bestand daher keine Veranlassung, die beiden
Hilfsanträge 2 a und 2 b nach § 83 Abs. 4 PatG als verspätet zurückzuweisen.




                                          B


In der Sache erweist sich die Klage, die auf die Nichtigkeitsgründe der unzulässigen Erweiterung, der mangelnden Patentfähigkeit sowie der mangelnden Ausführbarkeit des Streitpatents (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138
Abs. 1 lit c EPÜ, Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 lit a EPÜ
und Art. II § 6 Abs. 1 Nr. 2 IntPatÜG i. V. m. Art. 138 Abs. 1 lit b EPÜ) gestützt
wird, zum Teil als begründet.


Soweit die Beklagte das Streitpatent im Wege der zulässigen Selbstbeschränkung
nicht mehr verteidigt, war es mit Wirkung für die Bundesrepublik Deutschland
ohne Sachprüfung für nichtig zu erklären (zur st. Rspr. im Nichtigkeitsverfahren
vgl. z. B. BGH GRUR 2007, 404, 405 - Carvedilol II; Busse/Keukenschrijver, PatG,
8. Aufl., § 82 Rdn. 119 f. m. w. Nachw.; Schulte/Voit, PatG, 9. Aufl., § 81
Rdn. 128).

                                      - 27 -


                                        I.


1.   Das Streitpatent betrifft eine optische Platte und jeweils ein Verfahren zum
Aufzeichnen und zum Lesen von Information auf der Platte sowie jeweils ein Gerät
zum Ausführen der Verfahren.


Optische Platten wurden als Großspeicher für Computeranwendungen verwendet,
wobei diese optischen Platten als CD-ROMs bekannt sind. Platten, die als CD-ROM verwendet werden, werden nach dem Modell der Standard-Compact-Disc
(CD) hergestellt, die für Audioanwendungen entwickelt wurde. Sie sind grundsätzlich Audio-CDs mit verschiedenen Verbesserungen und Verfeinerungen, die insbesondere für Computeranwendungen angepasst wurden. Unter Verwendung einer derartigen CD als Standard hat die CD-ROM eine Datenspeicherkapazität von
ungefähr 600 Mbytes. Unter Verwendung der Audio-CD-Technologie als deren
Basis wurden die CD-ROMs und Plattenlaufwerke für sie relativ preiswert und populär.


Da jedoch herkömmliche Audio-CDs und das ihnen eigene Format und die damit
verbundene Speicherkapazität als Grundlage für die Entwicklung der CD-ROMs
dienten, wurde es daher schwierig, die Datenspeicherkapazität zu verbessern. Bei
typischen   Computeranwendungen       zeigte   sich,   dass   eine   Kapazität   von
600 Mbytes unzureichend ist.


Außerdem ist die Datenübertragungsrate, die von Audio-CDs erzielt werden kann,
kleiner als 1,4 Mbits/s. Computeranwendungen erfordern jedoch allgemein eine
Übertragungsrate von weit über 1,4 Mbits/s. Mit herkömmlichen CD-ROMs ist es
jedoch schwierig, eine schnellere Übertragungsrate zu erreichen.


Ein weiterer Nachteil der herkömmlichen CD-ROMs, der aufgrund der Tatsache
besteht, dass das CD-Audioformat für Computeranwendungen angepasst wurde,
ist die relativ lange Zugriffszeit in Verbindung mit dem Zugriff auf eine bestimmte
Stelle auf der Platte. Üblicherweise werden bei Audio-CDs relativ lange zusammenhängende Datenfolgen gelesen, während Computeranwendungen häufig das

                                      - 28 -


Zugreifen auf eine beliebige Stelle erfordern, um dort eine relativ kleine Datenmenge zu lesen. Das Zugreifen auf einen bestimmten Sektor kann beispielsweise
viel Zeit erfordern, da die CD-Steuerung den Sektor identifizieren muss, der gerade durch die optische Abtasteinrichtung gelesen wird.


Eine weitere Schwierigkeit in Verbindung mit CD-ROMs und aufgrund der Tatsache, dass diese CD-ROMs auf der CD-Audiotechnologie basieren, ist deren Fehlerkorrekturfähigkeit. Wenn Audiodaten von einer Audio-CD reproduziert werden,
können Fehler, die nicht korrigiert werden können, trotzdem unter Verwendung
von Interpolation auf der Basis der hohen Korrelation bei der Audioinformation, die
wiedergegeben wird, verborgen werden. Bei Computeranwendungen jedoch kann
die Interpolation, um Fehler zu verbergen, wegen der niedrigen Korrelation dieser
Daten nicht verwendet werden. Folglich müssen die Daten, die auf einer CD-ROM
aufgezeichnet sind, codiert und in einer Form moduliert werden, die eine hohe
Fehlerkorrekturfähigkeit zeigt. Daher wurden Daten auf einer CD-ROM in einem
herkömmlichen Kreuzverschachtelungs-Reed-Solomon-Code (CIRC) zusätzlich zu
einem sogenannten Blockbeendigungs-Fehlerkorrekturcode aufgezeichnet. Der
Blockbeendigungscode erfordert jedoch allgemein eine relativ lange Zeitdauer, um
die Daten zu decodieren, und außerdem glaubt man, dass die Fehlerkorrekturfähigkeit unzureichend ist, wenn Mehrfachfehler in einem Block vorhanden sind. Da
zwei Fehlerkorrekturcode-Verfahren (ECC) für eine CD-ROM verwendet werden,
während lediglich ein ECC-Verfahren für eine Audio-CD verwendet wird (nämlich
das CIRC-Verfahren), muss eine größere Menge an Nicht-Dateninformation auf
der CD-ROM aufgezeichnet werden, um diese Fehlerkorrektur auszuführen, wobei
diese Nicht-Dateninformation als „redundante“ Daten bezeichnet wird. Bei einem
Versuch, die Fehlerkorrekturfähigkeit einer CD-ROM zu verbessern, wird die
Menge an Redundanz, die aufgezeichnet werden muss, wesentlich erhöht.


Weiter ist es wünschenswert, eine genormte optische Platte dadurch zu verbessern, dass digitale Videoinformation in einem datenkomprimierten Format, beispielsweise MPEG-komprimierte Videodaten (oder PCM-Audiodaten), aufgezeichnet werden können, so dass sie als eine digitale Videoplatte (DVD) verwendet
werden kann. Es gab zum Prioritätszeitpunkt des Streitpatents und gibt jedoch

                                       - 29 -


zurzeit   unterschiedliche   MPEG-Kompressionsverfahren       oder   Formate,   die
verfügbar sind, und die weiter in der Zukunft entwickelt werden können. Es ist
schwierig, ein Videoprogramm von einer DVD wiederzugeben, wenn das MPEG-Format, welches bei der Aufzeichnung des Videoprogramms verwendet wurde,
nicht schnell bestimmt werden kann. Dieses Problem wird verschlimmert, wenn
auf einer DVD verschiedene Videoprogramme, die unterschiedliche MPEG-Formate aufweisen, sowie unterschiedliche Audioformate aufgezeichnet wurden (vgl.
Abs. [0001] bis [0007] der deutschen Übersetzung der Streitpatentschrift NK1a.).


2.   Vor diesem Hintergrund liegt der Erfindung als technisches Problem die Aufgabe zugrunde, eine verbesserte optische Platte bereitzustellen, die insbesondere
Verwendung als DVD oder als CD-ROM findet, bei der die oben genannten
Schwierigkeiten und Nachteile in Verbindung mit CD-ROMS, für die ähnliche Verwendungen bisher versucht wurden, überwunden werden (vgl. Abs. [0010] der
NK1a).


Dies bedeutet, dass eine optische Platte bereitgestellt werden soll, die eine höhere
Zugriffsgeschwindigkeit zeigt, um damit einen schnellen Zugriff auf beliebige Stellen zu ermöglichen, beispielsweise, um schnell auf Sektoren zuzugreifen, und es
soll ein verbessertes Aufzeichnungsformat für eine optische Platte bereitgestellt
werden, das die Fähigkeit verbessert, die auf ihr aufgezeichnete Videoinformation
zu identifizieren und auf diese zuzugreifen. Auch soll die Übertragungsrate gegenüber den bisher verwendeten CD-ROMs erhöht werden, und die Zugriffsfähigkeit
auf verschiedene Segmente von Videoinformation, beispielsweise Kapiteln, die auf
einer optischen Platte aufgezeichnet sind, soll verbessert werden. Es soll möglich
sein, die Daten mit reduzierter Redundanz zu speichern und die Aufzeichnungsdichte gegenüber einer CD zu erhöhen (vgl. Abs. [0011] bis [0017] der NK1a).


3.   Die gestellte Aufgabe wird u. a. durch das Verfahren des angegriffenen, selbständigen Anspruchs 59 und das Wiedergabegerät des ebenfalls angegriffenen,
selbständigen Anspruchs 118 des Streitpatents gelöst.

                                        - 30 -


Die eigentliche Erfindung des Streitpatents besteht in dem in Anspruch 1 des
Streitpatents beanspruchten Format einer optischen Platte. Die angegriffenen Ansprüche 118 und 59 betreffen ein Lesegerät für dieses Format und ein Verfahren
zum Lesen dieses Formats. Beides sind ausgehend von der eigentlich erfundenen
optischen Platte Notwendigkeiten, die im Streitpatent gemeinsam mit der optischen Platte geschützt sind. Auch in diesen Ansprüchen ist das Format der optischen Platte als Merkmale enthalten. So betreffen im geltenden Hauptantrag die
Merkmalskomplexe 118.1 und 118.3 bis 118.6 Merkmale dieser optischen Platte.
Lediglich der Merkmalskomplex 118.2 betrifft Merkmale des Lesegeräts.


Die optische Platte wird teilweise durch physikalische Merkmale und teilweise
durch abstrakte, den logischen Aufbau der auf ihr befindlichen Daten betreffende
Merkmale charakterisiert. Dies könnte bei einer optischen Platte allein problematisch sein, denn einem aufgezeichneten Datenmuster allein kann üblicherweise
dessen Sinn nicht entnommen werden. Bei einem Lesegerät ist diese Problematik
jedoch hinfällig, da hier das Lesegerät das aufgezeichnete, die Daten repräsentierende Muster interpretiert. Für ein Verfahren gilt dasselbe.


Wie bereits ausgeführt, weist die optische Platte eine Reihe von physikalischen
Merkmalen auf. So hat sie einen Durchmesser von weniger als 140 mm und eine
Dicke von 1,2 mm (Merkmal 118.1.1). Sie weist auch eine Mehrzahl von Aufnahmespuren auf (Merkmal 118.1.2), auf denen „Pits“, also Grübchen, welche die Information darstellen, aufgezeichnet sind (Merkmal 118.1.2.1). Dabei bedeutet die
Mehrzahl von Aufnahmespuren, dass sich neben einer Spur senkrecht zur Leserichtung eine weitere Spur befindet. Dies schließt nicht aus, dass diese nebeneinanderliegenden Spuren logisch nur eine Spur bilden, indem sie hintereinander
gelesen werden. Der Abstand der Spuren beträgt zwischen 0,7 µm und 0,9 µm
(Merkmal 118.5).


Die übrigen die optische Platte betreffenden Merkmale beschreiben deren logischen Aufbau. So sind zunächst die Spuren in einen Einlaufbereich, einen Programmbereich und einen Auslaufbereich unterteilt (Merkmal 118.1.2.2). Aus den
Namen ist auf deren Reihenfolge zu schließen. Die Aufzeichnungsdaten, also das

                                      - 31 -


was an Information auf der optischen Platte gespeichert ist, sind in mehreren Bereichen gespeichert, nämlich in einem Steuerinformationsbereich („control information region“) und in mehreren Datenspurbereichen (Merkmal 118.1.2.3). Dies
bedeutet, dass es nur einen Steuerinformationsbereich gibt und mehrere Datenspurbereiche, was wiederum heißt, dass es einen zusammenhängenden Bereich
gibt, in dem die gesamte Steuerinformation enthalten ist. Dies schließt aber nicht
aus, dass es eine oder mehrere Kopien der Steuerinformation in weiteren Steuerinformationsbereichen gibt (siehe hierzu auch Fig. 4A, 4B und 5. Fig. 4B und 5
zeigen Kopien der Steuerinformation in weiteren Steuerinformationsbereichen,
TOC DATA. Vgl. auch Abs. [0052]: „In Fig. 43 (Anm.: muss 4B heißen) duplicate
TOC regions are disposed in the lead-in area…“ und Abs. [0054]: „… and a copy
of the TOC information is recorded in the program area.”).


Dieser Steuerinformationsbereich ist im Einlaufbereich oder Programmbereich angeordnet (Merkmal 118.1.3.1). Dies bedeutet, dass er entweder im Einlaufbereich
oder im Programmbereich angeordnet sein kann.
Eine Anordnung im Einlaufbereich schließt dabei nicht aus, dass im Programmbereich eine Kopie angeordnet ist.


Der Steuerinformationsbereich enthält Steuerinformation („control information“;
Merkmal 118.1.3.2), die mit Inhaltsangabeninformation („table of contents information“) gleichgesetzt ist. Dies bedeutet, dass sich im Steuerinformationsbereich die
Information befindet, die für eine Inhaltsangabe benötigt wird. Daraus ergibt sich
für den Steuerinformationsbereich auch die Bezeichnung Inhaltsangabenbereich
(„table of contents region“). Es ist nicht ausgeschlossen, dass sich dort noch weitere Informationen befinden.


Die Steuerinformation befindet sich in einer ersten Mehrzahl von Sektoren. Ein
Sektor ist wiederum eine weitere Unterteilung der aufgezeichneten Information,
welche nicht näher spezifiziert wird. In einer zweiten Mehrzahl von Sektoren, welche sich in den Datenspurbereichen befinden, ist die Benutzerinformation aufgezeichnet. Wo sich die Datenspurbereiche befinden, ist nicht angegeben. Das Übliche ist aber, dass sie sich im Programmbereich befinden.

                                         - 32 -


Wie bereits dargestellt, besteht ein Datenspurbereich aus mehreren Sektoren. Der
erste dieser Sektoren wird als Startsektor bezeichnet. Seine Adresse ist in der
Steuerinformation, welche sich in der ersten Mehrzahl von Sektoren im Steuerinformationsbereich, welcher sich im Einlaufbereich oder im Programmbereich befindet, verzeichnet (Merkmal 118.1.5).


Weitere Merkmale geben an, wie die Daten auf der optischen Platte gespeichert
sind. So sind die Steuerinformation und die Benutzerinformation als modulierte
Langabstand-Fehlerkorrektur-Codierdaten, die zumindest acht Paritätssymbole
haben, aufgezeichnet (Merkmal 118.3). Was dies („modulated long distance error
correction encoded data“) bedeutet, bleibt in gewissem Umfang offen, denn es
handelt sich um einen Begriff, der zum Prioritätszeitpunkt von wenigen verwendet
wurde und sowohl zum damaligen Zeitpunkt als auch heute kein eindeutiger
Fachbegriff ist.


Bei den Daten auf der optischen Platte handelt sich somit um modulierte Daten.
Dies bedeutet, dass ein Datenbyte (= 8 Bits) in ein Symbol umgesetzt wird, das
mehr als 8 Bit, üblicherweise 14 oder 16 Bit aufweist. Dies wird gemacht, um die
Daten mit weniger Fehlern lesen zu können, denn manche Folgen von Nullen und
Einsen können nur mit relativ hoher Fehlerwahrscheinlichkeit gelesen werden, so
beispielsweise viele Nullen oder Einsen hintereinander. Solche Kombinationen
werden demnach vermieden, was möglich ist, da man bei einem Symbol mit mehr
als 8 Bit zur Darstellung des Wertebereichs eines Bytes nicht alle Darstellungsmöglichkeiten der mehreren Bits nutzen muss und aus den Möglichkeiten nur die
günstigen auswählen kann. So müssen bei einer Darstellung mit 16 Bit nur 256 (=
8 Bit) der 65536 (= 16 Bit) möglichen Kombinationen genutzt werden.


Weiter wird mit diesem Ausdruck ausgedrückt, dass eine Fehlerkorrekturmöglichkeit eingeführt ist, was durch die Erzeugung von Paritätsdaten bzw. Paritätssymbolen geschieht. Die Parität stellt fest, ob die Anzahl an Einsen in einer dualen
Zahl gerade oder ungerade ist. Je nach Typ der Parität wird bei einer geraden
oder eine ungeraden Anzahl von Einsen eine Eins als Paritätsbit gesetzt. Macht
man dies nicht für einzelne Bits, sondern gleich für ganze Symbole, so erhält man

                                        - 33 -


als Ergebnis wiederum ein Symbol, da jede Stelle des Symbols ein Paritätsbit an
der entsprechenden Stelle im Paritätssymbol ergibt.


Erzeugt man nur ein Paritätssymbol, so kann ein einzelner Fehler festgestellt werden. Zwei Fehler können nicht erkannt werden. Eine Korrektur des Fehlers ist
nicht möglich. Erzeugt man mehrere Symbole nach unterschiedlichen Regeln, so
sind das Erkennen mehrerer Fehler und auch die Korrektur von Fehlern möglich.
Im Prinzip ist die Korrektur von umso mehr Fehlern möglich, je mehr Paritätssymbole gebildet werden. Die Anzahl der Paritätssymbole ist jedoch beschränkt, da
auch diese aufgezeichnet werden müssen und somit Speicherplatz benötigen. Es
wird beansprucht, dass mindestens acht Paritätssymbole erzeugt werden. Für
welche Datenmenge diese acht Paritätssymbole erzeugt werden, bleibt dabei offen.


Genauso bleibt offen, was unter „long distance“ zu verstehen ist. Dieser Begriff ist
nur im Vergleich zu einer „short distance“ verständlich. Das Streitpatent offenbart
ein Beispiel für „modulated long distance error correction encoded data“. Eine eindeutige Definition gibt es aber nicht an. Die Klägerin interpretiert diese Angabe
dahingehend, dass bei einer Kurzabstand-Codierung die einem Codier-Schritt
unterliegende Datenmenge (Datenblock) in Subblöcke unterteilt werde, und die
Paritätssymbole den einzelnen Subblöcken zugeordnet würden. Bei einer Langabstand-Codierung würde dagegen keine solche Aufteilung stattfinden. Alle Paritätssymbole stünden für den gesamten Datenblock zur Verfügung (vgl. NK26 und
Abs. [0022] der Streitpatentschrift).


Zumindest einige der mehreren Datenspurbereiche enthalten Benutzerinformationen, die MPEG-komprimierte Videodaten und Audiodaten enthalten. Diese Daten
sind gemultiplext, d. h. es sind wechselweise Video- und Audiodaten aufgezeichnet (Merkmal 118.4). Die Version der MPEG-Komprimierung ist dabei aus mehreren Möglichkeiten ausgewählt und das Format der Audiodatei ebenfalls (Merkmal 118.6.3). Letzteres ist kein weiter einschränkendes Merkmal, sondern zunächst lediglich eine Definition.

                                      - 34 -


Die optische Platte enthält zudem eine Anwendungssteuerinformation. Diese ist im
Programmbereich aufgezeichnet. Sie dient dazu, dass ausgewählte Videodaten
und Audiodaten von der Platte reproduziert werden (Merkmal 118.6.1). Sie ist mit
der Anwendungsinhaltsverzeichnisinformation (ATOC) gleichgesetzt, die vorher
festgelegte Parameter der Benutzerinformation identifiziert, die in dementsprechenden Datenspurbereichen aufgezeichnet sind (Merkmal 118.6.2).


Die Anwendungsinhaltsverzeichnisinformation enthält mehrere Formatidentifizierdaten, um das Videokompressionsformat und das Audioformat, welches in jedem
Datenspurbereich verwendet wird, zu identifizieren (Merkmal 118.6.4). Damit wird
der Definition im Merkmal 118.6.3 ein Sinn gegeben, der darin besteht, dem
Merkmal 118.6.4 einen eindeutigen Inhalt zu verleihen.


Damit sind die Merkmale der optischen Platte abgeschlossen. Es verbleiben die
im Merkmalskomplex 118.2 vereinten, für das Abspielgerät wesentlichen Merkmale.


Dieses weist Mittel zum Drehen der optischen Platte mit einer konstanten Lineargeschwindigkeit auf (Merkmal 118.2.1), Abtastmittel, welche in bestimmter Weise
charakterisiert werden, Demodulationsmittel (Merkmal 118.2.3), Fehlerkorrekturmittel (Merkmal 118.2.4), Mittel zum Trennen der fehlerkorrigierten Daten in Steuerinformation, ATOC-Information und Nutzerinformation (Merkmal 118.2.5) sowie
Steuermittel, die auf die Steuerinformation ansprechen, um auf ausgewählte Benutzerspuren als Antwort auf Zugriffsinstruktionen eines Benutzers zuzugreifen
und diese zu lesen (Merkmal 118.2.6). Diese Mittel müssen alle mit den Eigenschaften der optischen Platte konform sein. Eine weitere Eigenschaft der Steuermittel liefert Merkmal 118.6.1, nämlich dass die Steuermittel auch die Anwendungssteuerinformation verwenden.


Bei den Ansprüchen 59 und 118 der Hilfsanträge wird das Modulationsverfahren
noch genauer ausgeführt. So handelt es sich bei dem Modulationsverfahren um
einen lauflängenbegrenzten Code („RLL-Code“) (Merkmal 118.7), und zwar um
einen (2, 10) RLL-Code (Merkmal 118.7.1), bei dem Datenübergänge mindestens

                                       - 35 -


2 Datenbitzellen und höchstens 10 Datenbitzellen auseinander liegen. Da eine 1
einen Datenübergang darstellt, bedeutet dies, dass zwischen zwei Einsen mindestens zwei Nullen und höchstens zehn Nullen liegen müssen. Eine Begrenzung
der Anzahl der aufeinander folgenden Nullen ist notwendig, da das Datenmuster
selbsttaktend sein muss. Dies bedeutet, dass ein Lesegerät aus dem Datenmuster
erkennen muss, wie breit eine einzelne Datenbitzelle ist. Dazu ist eine möglichst
große Anzahl von Übergängen wünschenswert. Durch die Obergrenze wird nun
sichergestellt, dass ausreichend viele Datenübergänge erfolgen.


Die Untergrenze ist notwendig, um zwei aufeinanderfolgende Übergänge noch sicher unterscheiden zu können. Dies ermöglicht, die optische Auflösung des Auslesesystems bis an dessen Grenzen auszunutzen.


Bei dem RLL-Code handelt es sich um einen Code mit 16 Bit langen Wörtern, mit
deren Hilfe 8 Bit lange Wörter, also Bytes codiert sind. Der Code weist keine
Trennbits auf (Merkmale 118.7.2 und 118.7.3). Das Konzept der Trennbits („margin bits“) besteht darin, dass nicht alle Bits des Codeworts zum Codieren des
Worts der zu speichernden Information verwendet werden, sondern das erste oder
die ersten Bits dazu verwendet werden, die Bedingung für die Lauflänge beim Aneinanderreihen zweier Codewörter zu erfüllen. Sie enthalten demnach keine Information und können bei einer Decodierung unbesehen weggelassen werden.
Dies bedeutet, dass im Falle von 16 Bit langen Codewörtern die eigentliche Codierung mit 15, 14 oder noch weniger Bits erfolgt.


Hilfsantrag 2 führt die verwendete RLL-Codierung noch weiter aus, indem in den
beiden unabhängigen Ansprüchen weiter angegeben wird, dass die Decodierung
anhand mehrerer Tabellen erfolgt, in denen die 8-bit langen Datenwörter gespeichert sind, in die die 16-bit langen Codewörter umgesetzt werden sollen. Die Auswahl der Tabelle, mit deren Hilfe ein gerade gelesenes Codewort decodiert wird,
erfolgt dabei als Funktion des vorhergehenden 16-bit Codewortes (Merkmale 118.7.4 bis 118.7.6).

                                       - 36 -


Hilfsantrag 2 a fügt dem in den unabhängigen Ansprüchen noch hinzu, dass mindestens ein 16-bit Codewort zwei unterschiedliche 8-bit lange Datenwörter codiert.
Diese unterschiedlichen Umsetzungen befinden sich dabei in zwei unterschiedlichen Tabellen (Merkmal 118.7.7). Die Auswahl der Tabelle erfolgt als Funktion
des dem gerade gelesenen Codewort nachfolgenden Codeworts (Merkmal 118.7.8). Zusammengefasst bedeutet dies, dass die Auswahlfunktion für die
Tabelle, die zur Decodierung des gerade gelesenen 16-bit Codewortes verwendet
wird, eine Funktion von zumindest dem vorausgehenden und dem nachfolgenden
Codewort ist, also zumindest diese beiden Variablen aufweist.


4.   Der Gegenstand des Anspruchs 118 des Hauptantrags ergibt sich für den
Fachmann in naheliegender Weise aus der Zusammenschau der Druckschrift NK9
mit der Druckschrift NK7 unter Hinzuziehen des Wissens des Fachmanns, das
durch die Druckschriften NK10 und NK11 dokumentiert ist, so dass der Gegenstand des Anspruchs 118 nach dem Hauptantrag mangels erfinderischer Tätigkeit
nicht patentfähig ist (Art. 56 EPÜ).


Als Fachmann ist hier ein berufserfahrener Diplom-Physiker oder Diplom-Ingenieur der Fachrichtung Elektrotechnik mit Fachhochschul- oder Hochschulabschluss
und guten Kenntnissen auf dem Gebiet der optischen Speichermedien zu definieren, der sowohl mit dem physikalischen als auch dem logischen Aufbau dieser
Medien vertraut ist und zusammen mit einem Informatiker mit der Entwicklung und
Programmierung zugehöriger Lese- bzw. Abspielgeräte betraut ist.


Druckschrift NK9 beschreibt ein Videosystem, das mit „Full Motion Video System“
(„FMV-System“) bezeichnet ist (vgl. den Titel) und das eine Erweiterung des dem
Fachmann bekannten CD-I-Systems darstellt (vgl. S. 121, 3. Abs.: „Das FMV-System (Full Motion Video) ist eine Erweiterung der CD-I-Spezifikation ohne Änderung der bereits bestehenden Definitionen. Dadurch ist das System mit jedem der
Norm entsprechenden CD-I Player voll kompatibel.“). Viele Eigenschaften der CD-I-Spezifikation können der Druckschrift NK10 entnommen werden (vgl. Kapitel
„6.7.1 Compact Disc Interactive“). Dabei ist Druckschrift NK10 derart aufgebaut,
dass alle auf dem CD-Standard basierenden Datenträgerformate im Kapitel „Opti-

                                       - 37 -


sche Speichermedien“ ausgehend von der Audio-CD (CD-DA) erklärt werden, da
alle CD-Formate auf der „Red Book“ genannten Spezifikation basieren (vgl.
S. 152, letzter Abs.: „Erst ungefähr 10 Jahre später, Ende 1982, wurde die Compact Disc Digital Audio (CD-DA) eingeführt. Diese optische Platte ermöglicht die
digitale Speicherung von Stereo-Audioinformationen auf hohem qualitativen
Niveau. Hierfür wurde die von P… und S… Corporation erstellte Spezifikation im Red Book […] zusammengefasst. Alle weiteren CD-Formate basieren
auf dieser Beschreibung.“). Dies bedeutet, dass die für die Audio-CD offenbarten
Merkmale auch für alle anderen CD-Formate gültig sind, solange nichts Gegenteiliges oder Alternatives für einen CD-Typ erwähnt wird.


Aus der Druckschrift NK9 ist somit unter Bezug auf Druckschrift NK10 in Übereinstimmung mit dem Wortlaut des Anspruchs 118 ein


118 Gerät zum Reproduzieren von Daten von einer optischen Platte bekannt (vgl.
S. 120, Einleitung: „Das Full Motion System von Philips spielt schon heute
72 Minuten digitales Video in voller Bildschirmgröße ab.“),


118.1     welche aufweist (Die optischen Platten erfüllen, wie bereits dargestellt,
die CD-I-Spezifikation, die in Bezug auf die physikalischen Eigenschaften der optischen Platte mit der Audio-CD identisch ist):


118.1.1   einen Durchmesser von weniger als 140 mm (vgl. NK10, S. 160,
2. Abs.: „Die CD hat einen Durchmesser von 12 cm.“); eine Dicke von 1,2 mm (Die
Druckschriften NK9 und NK10 enthalten keine Angaben über die Dicke einer CD.
Diese kann aber der Spezifikation NK11 entnommen werden. Vgl. Tabelle auf
S. 11, Punkte 5.1.1 und 5.3: „Thickness of disc 1.2+0.3
                                                   −0.1 mm“);



118.1.2   mehrere Aufzeichnungsspuren (vgl. NK10, S. 166, 5. Abs.: „Der Programmbereich jeder CD-DA kann aus bis zu 99 Tracks unterschiedlicher Länge
bestehen.“)

                                        - 38 -


118.1.2.1 auf denen Daten als Pits, welche die Information zeigen, aufgezeichnet
sind (siehe NK10, S. 154, Abb. 6-1 und S.160, Abb. 6-4 i. V. m. dem letzten Abs.:
„Die Informationsspeicherung geschieht nach dem in Abbildung 6-1 auf S. 154 und
Abbildung 6-4 auf Seite 160 dargestellten Prinzip. Dabei beträgt die Länge der Pits
immer ein Vielfaches von 0,3 µm. Ein Übergang von Pit zu Land und Land zu Pit
entspricht der Kodierung einer 1 im Datenstrom. Eine 0 wird als kein Übergang
kodiert.“),


118.1.2.2 wobei die Spuren in einen Einlaufbereich, einen Programmbereich und
einen Auslaufbereich unterteilt sind (vgl. NK10, S. 166, 1. bis 4. Abs.: „Eine CD-DA besteht als Ganzes aus folgenden drei Bereichen: ● Der Lead-in-Bereich beinhaltet das Inhaltsverzeichnis der CD-DA. Hier wird jeweils der Beginn einzelner
Tracks registriert. ● Der Programmbereich enthält alle Tracks der CD-DA. Hier
werden die eigentlichen Daten gespeichert. ● Am Ende jeder CD-DA ist ein Leadout-Bereich vorhanden. Dieser Bereich dient nur als Hilfe für das Abspielgerät,
falls versehentlich über den Programm-Bereich hinaus gelesen wird.“);


118.1.2.3 wobei die Aufzeichnungsdaten in einem Steuerinformationsbereich und
in mehreren Datenspurbereichen aufgezeichnet sind (vgl. die bereits zitierte Stelle
auf S. 166. Der Steuerinformationsbereich ist mit dem Bereich, in dem das Inhaltsverzeichnis gespeichert ist, gleichzusetzen. Die Datenspurbereiche werden
durch die Tracks verkörpert.),


118.1.3       wobei der Steuerinformationsbereich


118.1.3.1 im Einlaufbereich oder im Programmbereich angeordnet ist (vgl. die bereits zitierte Stelle NK10, S. 166, 2. Abs., nach der der Steuerinformationsbereich
im Einlaufbereich angeordnet ist.),


118.1.3.2 wobei der Steuerinformationsbereich Steuerinformation enthält (vgl. die
bereits zitierte Stelle NK10, S. 166, 2. Abs.. Das Inhaltsverzeichnis stellt eine
Steuerinformation dar.);

                                       - 39 -


118.1.3.3 die Inhaltsverzeichnisinformation ist (vgl. die bereits zitierte Stelle
NK10, S. 166, 2. Abs.. Dort wird ausdrücklich angegeben, dass es sich um ein Inhaltsverzeichnis handelt.) und


118.1.3.4 und wobei der Steuerinformationsbereich ein Inhaltsverzeichnisbereich
ist (beinhaltet die Steuerinformation, welche sich im Steuerinformationsbereich
befindet, eine Inhaltsverzeichnisinformation, so ist eine Bezeichnung des Steuerinformationsbereichs als Inhaltsverzeichnisbereich gerechtfertigt.)


118.1.4   wobei die Steuerinformation in einer ersten Mehrzahl von Sektoren im
Steuerinformationsbereich aufgezeichnet ist und die Benutzerinformation in einer
zweiten Mehrzahl von Sektoren in den mehreren Datenspurbereichen aufgezeichnet ist (Bereits bei der Audio-CD gibt es als Blöcke bezeichnete Sektoren. Vgl.
NK10, S. 166, letzter Abs.: „Es wurde eine weitere Struktur zwischen den Frames
und den Tracks, die Blöcke nach Abbildung 6-6 auf Seite 166 eingeführt. Ein Block
hat für die CD-DA keine Bedeutung, er wird bei den weiteren CD-Technologien jedoch ähnlich zum Begriff des Sektors verwendet.“ Die Blöcke werden dann in ihrer
Form bei der CD-ROM in Abb. 6-8 und 6-9 gezeigt. Für die CD-I wird auf S. 180
beschrieben, dass dieser Standard auf der CD-ROM basiert. Vgl. NK10, S. 180,
2. Abs.: „CD-I beschreibt eigentlich ein gesamtes System. Es beinhaltet ein CD-ROM-basiertes (nicht CD-ROM/XA) Format mit einer Verschachtelung verschiedener Medien und einer Definition der Kompression unterschiedlicher Medien.“
Damit sind auch dort Sektoren, wie bei der CD-ROM vorhanden. Vgl. auch NK9,
S. 125, rechte Sp. oben: „Auf einer CD-I werden die Daten in sequentiellen Einheiten, den Sektoren abgelegt.“. Für die Steuerinformation gibt es keine Angaben,
wie das Inhaltsverzeichnis abgelegt ist, jedoch kann auch dort zumindest eine virtuelle, aber möglicherweise bedeutungslose Einteilung in einen oder mehrere
Sektoren erfolgen.); und


118.1.5   jeder Datenspurbereich einen entsprechenden Startsektor hat (Dies
lässt sich bei der CD-I nicht vermeiden, da eine Aufteilung der Spuren in Sektoren
erfolgt.); wobei die Steuerinformation Adressen der entsprechenden Startsektoren
aufweist (vgl. wiederum die zitierte Stelle NK10, S. 166, 2. Abs.. Wenn im Inhalts-

                                        - 40 -


verzeichnis der Beginn einzelner Tracks verzeichnet ist, so muss es sich dabei
zwangsweise um die Adresse des Startsektors der Datenspur handeln, denn dort
beginnt die Datenspur.);


118.2      wobei das Gerät aufweist (Die Merkmalsgruppe 118.2 gibt einige für
das Gerät spezifische, Merkmale an. Einige sind der Druckschrift NK10 zu entnehmen. Sie muss das Gerät aus Druckschrift NK9, auch wenn dies dort nicht näher beschrieben ist, aufweisen, da es in der Lage sein muss, eine CD zu lesen.):


118.2.1    Mittel zum Drehen der Platte, um eine konstante Lineargeschwindigkeit
zu erreichen (vgl. NK10, S. 160, 2. Abs.: „Die CD hat einen Durchmesser von
12 cm. Sie wird mit einer konstanten Bahngeschwindigkeit (Constant Linear Velocity = CLV) abgespielt. Damit ist die Anzahl der Umdrehungen pro Zeiteinheit
vom jeweiligen Radius der gerade abgetasteten Daten abhängig.“);


118.2.2    Abtastmittel, um einen Abtastlichtstrahl durch eine Linse zu projizieren,
um die drehende Platte optisch zu lesen (vgl. NK10, S. 154, 1. Abs.: „Das Prinzip
optischer Speichermedien nutzt die Intensität des reflektierten Laserlichts als Darstellung der Information beim Lesen. Ein Laserstrahl kann bei einer Wellenlänge
von ca. 780 nm auf ungefähr 1 µm fokussiert werden.“), wobei der Abtastlichtstrahl
eine Raumfrequenz f= λ/2NA hat, wobei die Raumfrequenz f kleiner ist als die
Spurteilung, λ die Wellenlänge des Abtastlichtstrahls ist und NA die numerische
Apertur der Linse ist (siehe Abb. 6-2, wo die Spurteilung 1,6 µm beträgt, was größer als die angegebenen 1,0 µm für das fokussierte Licht ist, so dass die beanspruchte Beziehung für den Fall einer CD erfüllt ist.);


118.2.3    Demodulationsmittel, um die Daten, die von der Platte gelesen werden,
zu demodulieren (vgl. NK10, Kapitel 6.4.2: „Eight to Fourteen Modulation“. Sind
die Daten moduliert, so muss zum Lesen der Daten auch eine Demodulationseinrichtung vorhanden sein.);


118.2.4    Fehlerkorrekturmittel, um die demodulierten Daten fehler-zu-korrigieren
(vgl. NK10, S. 163, Kapitel 6.4.3: „Fehlerbehandlung. Das Ziel der Fehlerbehand-

                                        - 41 -


lung auf einer CD-DA ist die Erkennung und Beseitigung von typischen Fehlermustern…“ und S. 168, 1. Abs.: „Die Verwendung einer CD-ROM mit ihren allgemeinen Rechnerdaten erfordert eine bessere Fehlerkorrektur und einen wahlfreien
Zugriff auf eine Dateneinheit mit höherer Auflösung als die Tracks.“);


118.2.5      Mittel zum Trennen der fehler-korrigierten Daten in Steuerinformation,
Anwendungssteuerinformation und Nutzerinformation (Da Bild und Ton wiedergegeben werden sollen, muss eine solche Trennung vorhanden sein; siehe auch
NK9, Bild 6, wo die Daten in „MPEG Audio“ und eine „Full Motion Video Plane“
aufgetrennt werden.); und


118.2.6      Steuermittel, die auf die Steuerinformation ansprechen, um auf ausgewählte Benutzerspuren als Antwort auf Zugriffsinstruktionen von einem Benutzer
zuzugreifen und diese zu lesen (vgl. NK9, S. 124, linke Sp., 3. Abs.: „Teil dieser
Kontrolle ist die Wahl, welcher MPEG-Videostream mit welchem MPEG-Audiostream (falls vorhanden - es stehen auch andere Audio-Möglichkeiten zur Verfügung) wiedergegeben wird.“ und NK10, S. 172, 3. Abs.: „Diese Path Table ermöglicht einen direkten Zugriff auf Dateien beliebiger Ebene.“);


wobei


118.4      zumindest einige der mehreren Datenspurbereiche Benutzerinformation
enthalten, die MPEG-komprimierte Videodaten und Audiodaten enthalten, die miteinander verschachtelt sind (vgl. NK9, S. 121, letzter Abs.. „Nach der Kompression des Audio- oder Video-Eingangssignals werden die Daten als MPEG Audiooder MPEG Video-Datenstrom (Stream) gespeichert. Auf der CD-I können nun
mehrere dieser Audio-/Video-Streams parallel aufgezeichnet werden.“ Siehe auch
Bild 4);


118.6.1      eine Anwendungssteuerinformation, die im Programmbereich eingerichtet ist, durch die Steuerung verwendet wird, um ausgewählte Videodaten und Audiodaten von der Platte zu reproduzieren (vgl. NK9, S. 124, linke Sp. 2. Abs.:
„Jede Full Motion CD-I enthält ein Applikations-Programm, das interaktiv mit dem

                                       - 42 -


Benutzer die Wiedergabe der Platte im FMV CD-I Player steuert.“ Und im Hinblick
darauf, dass die CD-I auf der CD-ROM beruht: NK10, S. 172: „Frühzeitig wurde
erkannt, dass die Spezifikation der Blöcke im Mode 1 mit Ihrer Äquivalenz zu
Sektoren für einen kompatiblen Datenträger nicht ausreicht. Hier fehlt das logische
Dateiformat mit dem Directory. […] Mit diesem Standard wird ein Directory-Baum
definiert, der die Informationen über alle Dateien enthält. Zusätzlich gibt es eine
Tabelle, in der sämtliche Directorys in dichtgepackter Form aufgelistet sind. Diese
Path Table ermöglicht einen direkten Zugriff auf Dateien beliebiger Ebene.“),


118.6.2   die Anwendungssteuerinformation Anwendungsinhaltsverzeichnisinformation (ATOC) ist, die vorher festgelegte Parameter der Benutzerinformation
identifiziert, die in den entsprechenden Datenspurbereichen aufgezeichnet ist (Die
ATOC kann mit dem Directory und der Path Table gleichgesetzt werden. Die Parameter sind dann der Ort und der Name der Benutzerinformation.),


118.6.3   wobei die MPEG-komprimierten Videodaten in einem entsprechenden
Datenspurbereich in einem ausgewählten einen von mehreren Videokompressionsformaten codiert sind (Gemäß Druckschrift NK9 wird ein MPEG-Format verwendet, wie dem Kasten „Applikation des MPEG-Standards“ auf S. 124 zu entnehmen ist. Es war aber zum Prioritätszeitpunkt bereits bekannt, dass es nicht bei
einem MPEG-Standard bleiben wird, weshalb wohl auch bereits die Bezeichnung
„MPEG 1“ in Druckschrift NK9 verwendet wird. So beschreibt Druckschrift NK10
im Kapitel „5.7.4 Von MPEG-1 zu MPEG-2“ bereits einen zweiten „MPEG 2“ genannten Standard, den es zum Veröffentlichungszeitpunkt der Druckschrift NK10
aber noch nicht gab.), die Audiodaten in einem ausgewählten einen von mehreren
Audioformaten codiert sind (vgl. NK9, S. 124, linke Sp. 3.Abs.. „Teil dieser Kontrolle ist die Wahl, welcher MPEG-Videostream mit welchem MPEG-Audiostream
(falls vorhanden – es stehen auch andere Audio-Möglichkeiten zur Verfügung)
wiedergegeben wird.“ und S. 125 rechte Sp., 4. Abs.: „Ein Videosektor kann
DYUV, CLUT oder RGB Daten, ein Audiosektor kann PCM oder ADPCM Level A,
B oder C enthalten.“).

                                      - 43 -


Zudem gibt Druckschrift NK9 an, dass es beim Full Motion Video System zwei
neue Betriebsarten gibt, nämlich MPEG Bewegtbild und MPEG Standbild (vgl.
S. 125, vorletzter Abs.: „Um FMV auf einer CD-I zu speichern, wurde das Kodierungsformat erweitert. Es gibt zwei neue Betriebsarten: MPEG Bewegtbild und
MPEG Standbild.“). Es muss somit beim Full Motion Video System zumindest aus
diesen beiden Formaten ausgewählt werden. Dabei ist entgegen der Ansicht der
Beklagten auch das MPEG Standbild ein Videoformat im Sinne des Streitpatents.
Dort wird nämlich auch das JPEG-Format, welches ebenfalls ausschließlich für
Standbilder verwendet wird, als Beispiel für ein Videoformat angegeben (vgl.
Abs. [0025] des Streitpatents: „The present invention records different types of
data on an optical disk, preferably for use as a CD-ROM but also adapted for use
as a digital video disk (DVD). Such data may be file data or application data to be
used by a computer, or it may comprise video data which sometimes is referred to
herein as motion picture data which includes image information and audio information and which preferably is compressed in accordance with various conventional video data compression standards, or formats such as those known MPEG-1, MPEG-2, or when still video pictures are recorded, JPEG.”). Das Streitpatent
unterscheidet demnach zwischen Filmdaten (“motion picture data”) und Standbilddaten („still video pictures“). Beides wird unter dem Begriff Videodaten („video
data“) zusammengefasst.


Auch der Ansicht der Beklagten, dass die Merkmale unzulässigerweise unterschiedlichen Standards von CDs entnommen worden seien, ist nicht zu folgen. So
ist in Druckschrift NK9 angegeben, dass der FMV-CD-Standard auf dem CD-I-Standard beruht. Weiter ist in Druckschrift NK10 deutlich angegeben, wie die einzelnen Standards aufeinander aufbauen. So ergibt sich eindeutig, dass der CD-I-Standard auf dem CD-ROM-Standard und dieser wiederum auf dem CD-DA-Standard aufbaut. Unabhängig davon, ob es für einzelne Details andere Möglichkeiten gäbe oder in diesen Standards in der Realität sogar andere Möglichkeiten
verwirklicht sind, wird der Fachmann jeweils annehmen, dass die für einen niedrigeren Standard in dieser Kette aus Standards verwirklichten Details auch im darüberliegenden verwirklicht sind, solange er keine gegenteiligen Angaben enthält.

                                     - 44 -


Insoweit ist ein Gerät mit den bisher genannten Merkmalen für den Fachmann
zumindest naheliegend.


Es verbleiben somit die Merkmale
118.3, dass die Steuerinformation und die Benutzerinformation als modulierte
Langabstand-Fehlerkorrektur-Codierdaten, die zumindest acht Paritätssymbole
haben, aufgezeichnet sind,
118.5, dass die Spuren eine Teilung im Bereich zwischen 0,7 µm und 0,9 µm zeigen und
118.6.4, dass die Anwendungsinhaltsverzeichnisinformation (ATOC) mehrere
Formatidentifiziererdaten aufweist, um das Videokompressionsformat und das Audioformat, welches in jedem Datenspurbereich verwendet wird, zu identifizieren,
die nicht ausdrücklich in den Druckschriften NK9, NK10 und NK11 offenbart sind.


In Druckschrift NK9 wird bereits darauf hingewiesen, dass ein dichteres Beschreiben in nächster Zeit, auf Grund der Entwicklung eines blauen Lasers möglich sein
wird (vgl. S. 121, 1. Abs.: „Die Entwicklung neuer blauer Laser wird aber auch da
in nächster Zeit ein dichteres Beschreiben der glitzernden Scheiben möglich machen.“). Wie der Fachmann weiß, bedeutet der Wechsel von einem roten zu einem
blauen Laser in etwa eine Halbierung der Wellenlänge, was auch eine Halbierung
der Größe der minimal auflösbaren Strukturen zur Folge hat. Dies bedeutet, dass
bereits durch diesen Satz eine Teilung der Spuren auf die Hälfte, also auf
1,6 µm / 2 = 0,8 µm angeregt wird (Merkmal 118.5). Zum Prioritätszeitpunkt des
Streitpatents gab es somit zwar noch keinen wirklich nutzbaren blauen Laser, jedoch bereits die Anregung, eine Verdichtung der Information durch die Verwendung einer kürzeren Laserwellenlänge zu erreichen.


Bei der CD wird eine Laserwellenlänge von etwa 780 nm verwendet (vgl. Druckschrift NK10, S. 154: „Das Prinzip optischer Speichermedien nutzt die Intensität
des reflektierten Laserlichts als Darstellung der Information beim Lesen. Ein Laserstrahl kann bei einer Wellenlänge von 780 nm auf ungefähr 1 µm fokussiert
werden.“). Da es zum Prioritätszeitpunkt bereits Laser mit geringerer Wellenlänge
bis in den grünen Bereich hinein gab, also bis zu Wellenlängen unter 550 nm, lag

                                         - 45 -


es für den Fachmann nahe, auch einen Laser geringerer Wellenlänge einzusetzen.


Eine Lösung, die Aufzeichnungsdichte zu erhöhen, ohne die Wellenlänge des
Abtastlasers zu verändern, wird in Druckschrift NK7 beschrieben (vgl. Sp. 1, Z. 10
bis 14: „1. Field of the Invention. The present invention relates to an optical recording medium and an optical read/write apparatus and, more particularly, to an
improvement in the recording density of the optical recording medium.“). Dabei
sind in Druckschrift NK7 ohne Änderung der Wellenlänge des Lasers Spurabstände bis herab auf 1,0 µm offenbart (vgl. Sp. 4, Z. 8 bis 10: „The optical recording medium according to the present embodiment employs a protective layer
4 with a thickness of 0.5 mm and a track pitch of 1 µm.“). Der Fachmann kann somit auch ohne Änderung der Wellenlänge, wie sie in Druckschrift NK9 vorgeschlagen wird, den Spurabstand verringern, indem er, wie dort vorgeschlagen, die Dicke der Schutzschicht von 1.2 µm auf 0,5 µm verringert (vgl. Sp. 1, Z. 29 bis 32:
„An optical disk of either type can read and write information through the transparent protective layer of 1.2 mm thickness with an objective lens in a numerical
aperture (NA) of 0.55.“ und die bereits zitierte Stelle Sp. 4, Z. 8 bis 10).


Der Fachmann wird im Bestreben, die Aufgabe des Streitpatents optimal zu lösen,
beide Maßnahmen zusammen verwirklichen und kommt damit auf einen Spurabstand bis hinab zu 1,0 µm·550 nm/780 nm = 0,71 µm, was gleich der Untergrenze
des beanspruchten Bereichs von 0,7 µm bis 0,9 µm ist (Merkmal 118.5).


In Zusammenhang mit der Verringerung des Spurabstandes geht Druckschrift
NK7 auch auf die notwendigen Fehlerkorrekturmechanismen ein. Sie gibt dabei
an, dass gemäß dem Stand der Technik auf einem optischen Aufzeichnungsmedium ein Reed-Solomon-Code verwendet wird, der zwei Formate, ein Format A
und ein Format B vorgibt. Das Format A ist dabei ein Reed-Solomon-Code mit
16 Paritätssymbolen und wird als ein Langabstand-Fehlerkorrektur-Code bezeichnet (vgl. Sp. 1, Z. 48 bis 58: „Further, the optical disk employs an error correction
code named as a reed-solomon code (RS code). Either of the A format and B format uses the RS code generated at the Galois Field-GF (28). One byte is made

                                        - 46 -


one symbol which is one unit of the RS code. The A format has 520 bytes
(520 symbols) arranged at 104 rows and 5 columns at two dimensions. The 104
symbols in a column direction are added with parities of 16 symbols and form the
RS code (120, 104). Such a long RS code is named as a Long Distance Code
(LDC).“). Dies ist der Ausgangspunkt für eine verbesserte Fehlerkorrektur, die in
Druckschrift NK7 offenbart wird und ebenfalls als Langabstand-Fehlerkorrektur-Code bezeichnet werden kann und 16 Paritätssymbole aufweist (vgl. Sp. 5, Z. 12
bis 23: „Referring to FIG. 2, an error correction code in a structure mentioned
above according to the present invention is shown. Each symbol consists of 8 bits,
and symbols are arranged in a matrix having 129 rows and 129 columns. In the
matrix, the i-th row has symbols expressed by Di,0 --Di,128 and is provided with 16
parity symbols Pi,0 ̶ Pi,15 to form a (145, 129) RS code. Similarly, the j-th column is
provided with symbols D0,j ̶ D128,j and 16 parity symbols Q0,j ̶ Q15,j to form a
(145,129) RS code.”).


Der Fachmann wird diesen Fehlerkorrekturmechanismus bei der Verringerung des
Spurabstandes mit übernehmen und so auf der CD modulierte (vgl. NK10, S. 162,
Abschnitt 6.4.2 „Eight to Fourteen Modulation“) Langabstand-Fehlerkorrektur-Codierdaten, die zumindest acht Paritätssymbole haben, aufzeichnen (Merkmal 118.3).


Das Merkmal 118.6.4 ist den Druckschriften nicht zu entnehmen, denn es ist lediglich offenbart, dass die Sektoren mit den Nutzerdaten Formatidentifizierdaten in
ihren Headern aufweisen (vgl. NK9, S. 125, rechte Sp. 2. Abs.. „Jeder CD-I Sektor
besteht aus einem Header, einem Subheader und einem Datenfeld (siehe auch
CD-ROM /XA und Green Book, FS 7/93). Header und Subheader liefern unter anderem die Information über Datenart, Form und Kodierung. Der Datentyp definiert
die Art der im Sektor abgelegten Daten: Video, Audio oder Programmdaten. Die
Form definiert den verwendeten Fehlerkorrekturcode.“). Damit befinden sich die
Formatidentifizierdaten zwar im Programmbereich, sie können jedoch nicht als
Bestandteil der Anwendungsinhaltsverzeichnisinformation (ATOC-information) angesehen werden.

                                       - 47 -


Ein Datum ist dann Bestandteil der Anwendungsinhaltsverzeichnisinformation,
wenn es Bestandteil einer Sammlung von gleichartigen Daten ist, die bestimmte
Informationen, die den Inhalt der Disk betreffen, enthält. Befindet sich ein einzelnes Datum, das Bestandteil eines Anwendungsinhaltsverzeichnisses und damit
der Anwendungsinhaltsverzeichnisinformation sein könnte, ausschließlich für sich
an einem Ort auf der Disk, so ist es nicht Bestandteil einer Sammlung solcher
gleichartiger Daten und damit nicht Bestandteil eines Anwendungsinhaltsverzeichnisses und in der Folge der Anwendungsinhaltsverzeichnisinformation. Damit sind
die Formatidentifizierdaten in den Headern keine Anwendungsinhaltsverzeichnisinformation, da sie sich nicht in einer solchen Sammlung befinden, und es auch
keine Kopien dieser Daten in einer solchen Sammlung gibt.


Jedoch liegt es nahe, diese Formatidentifizierdaten auch in der ATOC niederzulegen. So enthalten die üblichen Dateinamen eine Extension (Erweiterung), die den
Typ des abgespeicherten Files bestimmt. Diese Extension bestimmt dann meist
auch, mittels welchen Programms die Daten zunächst gelesen und interpretiert
werden sollen. Dies ist auch, wie dem Fachmann aus der Alltagserfahrung bekannt ist, bei der CD-ROM der Fall. Die Extension ist Bestandteil des Namens und
damit im Directory (siehe hierzu die Ausführungen zum Merkmal 118.6.2) enthalten. Dabei werden meist für verschiedene Datenkompressionsverfahren verschiedene Extensions verwendet (z. B. „.mpg“ für MPEG 1 Dateien, „.mpg2“ oder
„.mpgv“ für MPEG 2 Dateien oder „.mpg4“ für MPEG 4 Dateien). Es ist nun auch
bei der CD-I, sofern dies nicht ohnehin der Fall ist und lediglich in den Druckschriften nicht beschrieben ist, naheliegend, für die aufgezeichneten und im Directory aufgeführten Dateien entsprechende, übliche Extensions zu vergeben,
womit dann auch Formatidentifizierdaten in der ATOC vorhanden sind, um das Videokompressionsformat und das Audioformat, welches in jedem Datenspurbereich
verwendet wird, zu identifizieren.


Damit kommt der Fachmann ohne erfinderisch tätig zu werden zum Gegenstand
des Anspruchs 118 des Hauptantrags, so dass dieser nicht patentfähig ist.

                                          - 48 -


5.   Auch der Gegenstand des Anspruchs 118 nach Hilfsantrag 1 beruht auf keiner erfinderischen Tätigkeit des Fachmanns (Art. 56 EPÜ, § 4 PatG) und ist demnach nicht patentfähig.


So beschreibt Druckschrift NK10 für die Audio-CD, auf der auch das Full Motion
Video System beruht, dass eine Modulation von 8 Bits nach 14 Bits erfolgt (vgl.
S. 162: „6.4.2 Eight to Fourteen Modulation“). Bei dieser Umsetzung werden
8 Datenbits in 14 Datenbits derart umgesetzt, dass sich zwischen zwei Einsen, die
einen Wechsel von Land zu Pit oder umgekehrt darstellen, mindestens zwei Nullen und höchstens 10 Nullen befinden (vgl. S. 162, 1. bis 3. Abs.: „Jeder Wechsel
von Pit zu Land und Land zu Pit entspricht einer Eins als Kanalbit. Wenn kein
Wechsel stattfindet, so ist dies eine Null als Kanalbit. Pits und Lands dürfen jedoch
auf einer CD-DA nicht zu dicht hintereinander folgen. […] Deshalb hat man sich
darauf geeinigt, dass immer mindestens zwei Lands und zwei Pits in Folge auftreten. Zwischen je zwei Einsen als Kanalbits befinden sich mindestens zwei Nullen. Andererseits dürfen Pits und Lands nicht zu lang sein, […] Hier hat man die
maximale Länge der Pits und Lands beschränkt. Es dürfen somit maximal zehn 0
als Kanalbits hintereinander folgen.“).


Um diese Bedingungen auch beim Aneinanderfügen mehrerer 14-bit-Datenwörter
zu gewährleisten, wurden 3 zusätzliche Bits in die Symbole eingeführt, welche in
Abhängigkeit von den benachbarten modulierten Bits ausgewählt werden (vgl.
S. 162, 163 seitenübergreifender Abs.: „Beim direkten Hintereinanderfügen der
modulierten Bits (14-bit-Werte) könnte jedoch immer noch der minimale Abstand
von 2 bit unterschritten oder der maximale Abstand von 10 bit überschritten werden. Man fügt deshalb zwischen zwei aufeinanderfolgende modulierte Symbole je
3 zusätzliche Bits ein, so können die angestrebten Gesetzmäßigkeiten eingehalten
werden. Die Füllbits werden in Abhängigkeit der benachbarten modulierten Bits
ausgewählt.“). Damit ergibt sich eine Länge des Symbols von 14+3 = 17 Bit. Es
handelt sich demnach um einen (2, 10) lauflängenbegrenzten Code, der 8 Bit nach
17 Bit umsetzt und 3 Trennbits enthält (Merkmale 118.7 und 118.7.1). Ein solcher
RLL-Code ist demnach auch beim Full Motion Video System gegeben.

                                        - 49 -


Druckschrift NK14 gibt an, wie es zu diesem Code gekommen ist. Dabei wird auch
auf eine weitere Problematik bei der CD eingegangen, die darin besteht, dass der
Gleichstromanteil bzw. der Anteil mit niedriger Frequenz des codierten Datenstroms möglichst klein bleiben soll, um das den Laser bewegenden Servosystem
stabil auf der Spur halten zu können (vgl. S. 1755, linke Sp., 2. Abs.: „The
designers of the Compact Disc [4] system chose, after ample experimental evidence, an RLL code with minimum runlength d = 2. The code operates under a
second constraint, namely that the dc-content or low-frequency content of the
coded bit stream should be as small as possible. The reason for this is that the
servo systems used for track following and focusing [25] are controlled by the lowfrequency components of the signal read from the disc, and the signal could
therefore interfere with the servo systems.”).


Ausgegangen wurde dabei von einem (2, 10) RLL-Code, bei dem eine Umsetzung
von 8 nach 16 Bit erfolgt. Dieser ist nämlich, was den Speicherbedarf angeht, besonders günstig und bietet den zusätzlichen Vorteil, dass jeweils ein Byte in ein
Codewort umgesetzt wird, was gut zu den Vorgaben für die CD passt (vgl.
Table 6, 8. Zeile für d=2, k=10, m=8, n=16 und S. 1755, linke Sp., 2. Abs.: „The
design team opted for a fixed-length block structure. A source block length M = 8
is an adequate choice, since the entire format (16-bit audio samples, error correction, etc.) is byte oriented. Table 6 reveals that a fixed-length block code with the
parameter R = 8/16, d = 2 and k = 10 is feasible.”).


Weiter verweist die Offenbarungsstelle in Zusammenhang mit Tabelle 9 (siehe
Table 9, 2. Zeile für d = 2, k = 10, n‘ = 14, R = 8/16) darauf, dass in diesem Rahmen ein Code möglich ist, der auf der in dieser Druckschrift als „Construction 2“
bezeichneten Konstruktion beruht und 14 Informationsbits und 2 Trennbits besitzt
(vgl. S. 1755, linke Sp., 2. Abs.: „Specifically, from Table 9 we conclude that a
code based on Construction 2 with fourteen information and two two merging bits
is possible. In order to reduce the complexity of the decoder logic that transforms
the fourteen channel bits into eight data bits, the relationship between data patterns and code patterns have to be optimized.”).

                                        - 50 -


Die Konstruktion des 16-bit-Codes als 14-bit-Code mit 2 Trennbits ist dabei deshalb erfolgt, um eine eindeutige Rücktransformation zu ermöglichen, die keine
Vielzahl von Tabellen benötigt, mit deren Hilfe in Abhängigkeit von anderen
Codewörtern, so beispielsweise vorausgehenden Codewörtern, eine Codierung
und in der Folge eine Decodierung erfolgt. Dies vereinfacht die Codierung und
auch die Decodierung deutlich (vgl. S. 1752, rechte Sp. vorletzter Abs.: „The previous construction technique has the obvious drawback that we require a large
number of look-up tables for encoding. As a matter of fact, the number of look-up
tables equals, in general, the number of principal states, which, if the maximum
runlength k is large, can be quite prohibitive.”). Dies bedeutet, dass die Erzeugung
von mehreren Tabellen für die Umsetzung des Codes ohne die Verwendung von
Trennbits die übliche allgemeine Vorgehensweise ist. Mit der Erzeugung eines nur
14 Bit langen Codes plus zwei Trennbits wird nur eine oder eine geringe Anzahl
der möglichen Lösungen, welche mit Tabellen darstellbar sind, erreicht, so dass
es sich bei diesem Code um eine Teilmenge der möglichen Lösungen eines 16 Bit
langen Codes handelt.


Dies wird aus dem Abschnitt B der Druckschrift NK14 nochmals deutlich, wo die
Darstellung in Tabellen für ein einfaches Beispiel gezeigt wird (siehe S. 1752, linke
Sp., 2. Tabelle von oben.). Dabei wird, auch wenn das nicht näher ausgeführt ist,
gezeigt, dass auch eine Darstellung des 2 Bit langen Codes aus den Tabellen als
1 Bit langer Code plus ein Trennbit möglich ist (siehe S. 1752, linke Sp., 3. Tabelle
von oben).


Bei der CD ist in der Folge festgestellt worden, dass eine Darstellung mit 14 Bit
plus 2 Trennbits, also mit einem 16 Bit langen Code zwar informationstheoretisch
möglich ist, damit aber die Forderung nach einem ausreichend kleinen Gleichstromanteil nicht erfüllt werden kann. Deshalb wurde ein drittes Trennbit eingefügt,
so dass letztendlich ein 17 Bit langer Code entstanden ist, wodurch etwa 6 % der
Speicherkapazität verloren gehen (vgl. S. 1755, rechte Sp., 1. Abs.: „In itself, two
merging bits would be sufficient for continuing to satisfy the runlength conditions. A
third merging bit is necessary, however, to provide sufficient freedom for effective

                                       - 51 -


suppression of low-frequency content, even though it entails a loss of six percent
of the playing time.”).


Auch beim Full Motion Video System wird demnach auf 6 % der Speicherkapazität
verzichtet, indem die bei der CD übliche Modulation verwendet wird. Dem Fachmann ist dabei bekannt, dass er diese 6 % gewinnen kann, indem er zu der am
Anfang der Überlegungen stehenden Idee eines allgemeinen RLL-Codes mit
16 Bit langen Codewörtern, welche in mehreren Tabellen aufgeführt sind, zurückkehrt. Eine solche Rückkehr zu einer bereits früher bekannten und offenbarten
Idee, um deren bekannte Vorteile für eine damit in unmittelbarem Zusammenhang
stehende Aufgabenstellung zu nützen, kann eine erfinderische Tätigkeit jedoch
nicht begründen.


Dies bedeutet, dass die Merkmale, dass der RLL Code als 16-bit Informationswörter ohne Trennbits zwischen den 16-bit Informationswörtern aufgezeichnet ist
(Merkmal 118.7.2) und der RLL Decoder diese 16-bit Informationswörter in 8-bit
Informationswörter umsetzt (118.7.3), eine erfinderische Tätigkeit nicht begründen
können. Damit ist auch der Gegenstand des Anspruchs 118 des Hilfsantrags 1
mangels erfinderischer Tätigkeit (Art. 56 EPÜ) nicht patentfähig.


6.   Der Gegenstand des Anspruchs 118 nach Hilfsantrag 2 beruht ebenfalls auf
keiner erfinderischen Tätigkeit des Fachmanns (Art. 56 EPÜ, § 4 PatG) und ist
demnach ebenfalls nicht patentfähig.


Wie bereits zu Anspruch 118 des Hilfsantrags 1 ausgeführt, ist ein RLL-Code, der
mehrere Tabellen verwendet, durchaus üblich (Merkmal 118.7.4). Die Verwendung mehrerer Tabellen wird oft deshalb nötig, weil es keine eineindeutige Codierung gibt, mit deren Hilfe auch eine Aneinanderreihung der Codewörter unter Einhaltung der Lauflängenbedingungen möglich ist. Die Tabelle, mit deren Hilfe ein
Datenwort codiert bzw. decodiert wird, wird dann beispielsweise auf Grund des
vorausgehenden Codewortes ausgewählt (Merkmal 118.7.5) und die Umsetzung
des Codewortes aus dieser Tabelle ausgelesen (Merkmal 118.7.6) (vgl. Druckschrift NK14, S. 1750, spaltenübergreifender Abs.: „One approach that has proved

                                        - 52 -


very successful for the conversion of arbitrary source information into constrained
sequences is the one constituted by block codes. The encoder chops the source
sequence into blocks of length m, and under the code rules such blocks are
mapped onto words of n channel symbols. The obvious method for the construction of RLL codes is to employ codewords that can be freely cascaded without
violating the sequence constraints; the codewords employed have a one-to-one
correspondence with the source words. A logical step, then, is to extend this
mechanism to codes, where the translations are not one-to-one, but are, for
example, a function of the latest codeword transmitted. The source words operate
with a number of alternative translations (or modes); each of them is interpreted by
the decoder in the same way. During transmission, the choice of a specific translation is made in such a way that the specified constraints of the encoded sequence, after transmission of the new codeword, are not violated. Codes that
operate with a unique representation of the source words are called state-independent codes, and codes whose translations are not one-to-one are called statedependent codes. The restriction of state-independent encoding leads, in general,
to codes that are more complex than state dependent codes for a given bit-persymbol value.” und vgl. die bereits zitierte Stelle S. 1752, rechte Sp.).


Damit ist auch der Gegenstand des Anspruchs 118 nach Hilfsantrag 2 dem Fachmann nahegelegt, da dieser die Verwendung mehrerer Tabellen als den allgemeinen Fall der RLL-Codierung verstehen wird, von dem bei der Entwicklung der Modulation für die CD ausgegangen wird.


Die übrigen angegriffenen Ansprüche des Hauptantrags und der Hilfsanträge 1
und 2 fallen mit dem jeweiligen selbständigen Anspruch 118, da die Anspruchssätze der einzelnen Anträge geschlossene Anspruchssätze darstellen.


Da der Hauptantrag und die Hilfsanträge 1 und 2 bereits mangels Patentfähigkeit
fallen, erübrigt sich hier ein Eingehen auf die von der Klägerin erhobenen Bedenken betreffend unzulässiger Erweiterung und mangelnder Ausführbarkeit.

                                       - 53 -


7.   Die Klage ist unbegründet soweit die Nichtigerklärung des Streitpatents in
der Fassung der Patentansprüche, die mit dem Hilfsantrag 2 a verteidigt wird,
begehrt wird. Diese Fassung der Patentansprüche ist zulässig und ihre Lehre ist
ausführbar und patentfähig.


a)   Die Patentansprüche nach Hilfsantrag 2 a sind zulässig.


aa) Die Klägerin macht geltend, dass in Zusammenhang mit den nicht in den ursprünglichen Unterlagen enthaltenen Begriffen „Steuerinformationsbereich“ („control information region“), dem damit verbundenen Begriff „Steuerinformation“
(„control information“) und „Anwendungssteuerinformation“ („application control
information“) eine unzulässige Erweiterung gegenüber der ursprünglichen Offenbarung erfolgt sei. Die Begriffe „Steuerinformationsbereich“ und „Anwendungssteuerinformation“ treten, wie von der Klägerin angegeben, in den ursprünglichen
Unterlagen nicht auf. Der Begriff „Steuerinformation“ kommt in den ursprünglichen
Unterlagen an genau einer Stelle vor (vgl. ursprüngliche Unterlagen NK2, S. 17,
Mitte bzw. S. 7, Z. 42 bis 44 der Offenlegungsschrift EP 0 673 034 A2: „Such subcode information is generated by a suitable source and, as will be described
further below in conjunction with Fig. 11, is used to provide helpful identifying and
control information related to the user data that is recorded on the disk.“), wird
aber dort lediglich zur Erläuterung des Inhalts des Sektorheaders für die Benutzerinformation verwendet, von dem ausgesagt wird, dass eine in ihm enthaltene Subcodeinformation nützliche Identifikations- und Steuerinformationen in Bezug auf
die Nutzerdaten zur Verfügung stellt. Diese Stelle hat demnach nichts mit dem im
Anspruch verwendeten Begriff „Steuerinformation“ zu tun.


In den ursprünglichen Unterlagen sind jedoch die Begriffe „TOC (Table Of Contents)-Information“ („TOC information“), „TOC-Bereich“ („TOC region“), „Anwendungsinhaltsverzeichnisinformation“ („application table of contents information“,
„ATOC information“) und „Anwendungsinhaltsverzeichnisbereich“ („application
TOC region“) enthalten. In den Ansprüchen 59 und 118 des Hilfsantrags 2 a werden die Begriffe „Steuerinformation“ („control information“), „Steuerinformationsbereich“ („control information region“) und „Anwendungssteuerinformation“ („applica-

                                       - 54 -


tion control information“) mit den offenbarten Begriffen „Inhaltsverzeichnisinformation“ („table of contents information“; Merkmal 59.1.3.3 bzw. 118.1.3.3), „Inhaltsverzeichnisbereich“ („table of contents region“; Merkmal 59.1.3.4 bzw. 118.1.3.4)
bzw. „Anwendungsinhaltsverzeichnisinformation“ („application table of contents
information“; Merkmal 59.6.2 bzw. 118.6.2) gleichgesetzt. Dies geschieht jeweils
durch das einfache Wort „ist“ („is“). Dadurch werden die breiteren, ursprünglich
nicht offenbarten Begriffe durch die engeren, ursprünglich offenbarten Begriffe
eingeschränkt. Es erfolgt somit keine Erweiterung durch einen breiteren Begriff
gegenüber der ursprünglichen Offenbarung und auf Grund der Einschränkung
werden auch die Gegenstände der Ansprüche 59 und 118 gegenüber dem erteilten Anspruch eingeschränkt.


Dem Einwand der Klägerin, dass die Verbindung der Begriffe durch „ist“ nicht ausschließen würde, dass neben den ursprünglich offenbarten Informationen noch
weitere Information enthalten sein könnten, also beispielsweise die Steuerinformation neben der Inhaltsangabeninformation noch weitere Informationen enthalten
könne, ist nicht zu folgen. Denn das Wort „ist“ drückt eine Gleichsetzung beider
Begriffe aus. Es ist nicht notwendig, dies durch Ausdrücke wie „ausschließlich“ zu
verstärken, denn dies würde am Inhalt der Gleichsetzung nichts ändern. Die
Gleichsetzung wirkt demnach so, wie wenn an Stelle des einen Begriffs jeweils der
gleichgesetzt andere stünde.


ab) Im Merkmal 59.1.3.1 bzw. 118.1.3.1 wird jeweils beansprucht, dass der Steuerinformationsbereich und damit der Inhaltsverzeichnisbereich im Einlaufbereich
oder im Programmbereich angeordnet ist. Die Klägerin macht hierzu geltend, dass
dies nicht ausschließe, dass der Steuerinformationsbereich auch übergreifend
vom Einlaufbereich in den Programmbereich angeordnet ist, was ursprünglich
nicht offenbart sei.


Ursprünglich offenbart sind die folgenden Möglichkeiten der Anordnung der TOC-Bereiche:

                                       - 55 -


   1. nur im Einlaufbereich, dort möglicherweise Kopien (siehe Fig. 4A, 4B
      i. V. m. S. 26, 27, seitenübergreifender Abs. der ursprünglichen Beschreibung NK2, insbesondere S. 27, Z. 2 und 3: „In Fig. 4B duplicate TOC regions are disposed.“)
   2. im Einlaufbereich und eine Kopie im Programmbereich (Fig. 5)
   3. nur im Programmbereich (siehe Fig. 6 und 7).


Damit ist tatsächlich eine übergreifende Anordnung im Einlauf- und Programmbereich ursprünglich nicht offenbart. Jedoch wird eine solche, anders als im erteilten
Patent, wo beansprucht wurde, dass der Steuerinformationsbereich „in zumindest
einem von dem Einlaufbereich oder dem Programmbereich angeordnet ist“, mit
der Formulierung in den Ansprüchen 59 und 118 des Hilfsantrages 2 a entgegen
der Ansicht der Klägerin auch nicht mehr beansprucht. Der Fachmann wird das
„oder“ hier als exklusives Oder verstehen, denn er würde nicht davon sprechen,
dass der Steuerinformationsbereich im Einlaufbereich angeordnet sei, wenn dort
nur ein Teil des Steuerinformationsbereichs angeordnet wäre. Für den Programmbereich gilt das Entsprechende. Das Wort „oder“ verbindet somit lediglich diese
beiden Möglichkeiten als Alternativen. Sollte das Wort „oder“ in diesem Fall nicht
als exklusives Oder verstanden werden, so müsste dies, wie dies beim Streitpatent in der erteilten Version der Fall ist, durch eine zusätzliche Angabe deutlich
gemacht werden.


Auch in diesem Punkt liegt somit keine unzulässige Erweiterung gegenüber der
ursprünglichen Offenbarung vor. Die Änderung gegenüber dem erteilten Patent ist
zudem einschränkend und damit zulässig.


ac) Die Klägerin sieht eine zusätzliche Unzulässigkeit darin, dass die Formulierung der Patentansprüche 59 und 118 nicht ausschließe, dass es sich bei dem
Steuerinformationsbereich um einen nicht zusammenhängenden mehrteiligen Bereich handle, was ursprünglich ebenfalls nicht offenbart sei. Dem ist insoweit zuzustimmen, dass tatsächlich kein mehrteiliger Steuerinformationsbereich bzw. Inhaltsangabenbereich ursprünglich offenbart ist. Jedoch wird der Fachmann unter
dem Steuerinformationsbereich auch keinen mehrteiligen, nicht zusammenhän-

                                        - 56 -


genden Bereich verstehen, denn das Wort „Bereich“ („region“) steht im Singular.
Üblicherweise würde der Fachmann, wenn es sich um mehrere nicht zusammenhängende Teilbereiche handeln würde, von „Bereichen“ („regions“) sprechen, also
den Plural setzen. Dies schließt nicht aus, dass in bestimmten Fällen ein Bereich
so betrachtet werden kann, dass er sich aus mehreren, nicht zusammenhängenden Teilbereichen zusammensetzt. Hierzu bedarf es aber einer konkreten Angabe
oder eines speziellen Grundes, dass eine solche Möglichkeit besteht. Diese gibt
es aber im Streitpatent nicht, so dass der Fachmann im Falle des Streitpatents
den Steuerinformationsbereich als einen zusammenhängenden Bereich ansehen
wird.


ad) Als weiteren Grund für eine unzulässige Erweiterung macht die Klägerin das
Merkmal 59.2.5 bzw. 118.2.5 geltend, dass ein Trennen der fehlerkorrigierten Daten erfolge, bzw. das Gerät Mittel hierzu aufweise. Dieses sei ursprünglich nur insofern offenbart, als angegeben werde, dass ein Separieren in TOC-Information,
ATOC-Information und Nutzerinformation erfolge (vgl. die ursprünglichen Ansprüche 75 und 150 die den Ansprüchen 59 und 118 zugrunde liegen.). Bei den Ansprüchen 59 und 118 des Hilfsantrags 2 a kann diese Unzulässigkeit jedoch nicht
mehr bestehen, da in den Merkmalen 59.2.5 bzw. 118.2.5 wieder die in den ursprünglichen Ansprüchen beanspruchte Trennung beansprucht wird.


ae) Die Klägerin macht keine weiteren unzulässigen Erweiterungen geltend, so
dass sich eine ausführliche Erläuterung der Zulässigkeit der übrigen Merkmale der
Ansprüche 59 und 118, die der Senat alle für zulässig erachtet, erübrigt. Die Ansprüche 59 und 118 des Hilfsantrags 2 a sind somit zulässig. Dies gilt auch für die
übrigen angegriffenen Ansprüche, die die Klägerin nur in Zusammenhang mit der
angeblichen Unzulässigkeit der selbständigen Ansprüche, auf die sich diese Ansprüche zurückbeziehen, als unzulässig erachtet.


b)      Die Lehren der Ansprüche des Hilfsantrags 2 a sind im Streitpatent so deutlich und vollständig offenbart, dass ein Fachmann sie ausführen kann (Art. 83
EPÜ, § 34 Abs. 4 PatG).

                                        - 57 -


ba) Die Klägerin zweifelt die Ausführbarkeit der Lehre der Ansprüche 59 und 118
dahingehend an, dass sie angibt, dass das Merkmal 59.5 bzw. 118.5, wonach der
Abstand der Spuren im Bereich zwischen 0,7 µm und 0,9 µm liegt, nicht ausführbar sei. Damit meint sie offensichtlich, dass die gesamte Lehre des Anspruchs bei
Erfüllung des Merkmals 59.5 bzw. 118.5 nicht ausführbar sei, denn das Merkmal
selbst ist deutlich angegeben, und zudem ist es kein Problem, eine Spur mit dem
angegebenen Abstand herzustellen, so dass das Merkmal für den Fachmann
problemlos zu realisieren ist. Sie meint damit, dass eine Angabe fehle, wie die Information auch bei einem Spurabstand im beanspruchten Bereich noch wie im
Merkmal 59.2.2 bzw. 118.2.2 beansprucht von der Platte ausgelesen werden
kann. Ihrer Ansicht nach benötigt der Fachmann eine Information, wie er die Auslesemittel zu gestalten hat, um die im beanspruchten Bereich beabstandeten Spuren noch auflösen und damit auslesen zu können.


In der Patentschrift wird hierzu angegeben, dass die Wellenlänge λ = 635 nm beträgt und die numerische Apertur einen Wert von NA = 0,52 besitzt, wodurch sich
eine räumliche Auflösung von 611 nm ergibt (vgl. Abs. [0027]: „As a result of the
linear density and track pitch of the disk, information is optically read from the disk
by a pick-up head which projects a light beam of wavelength λ; through a lens
having a numerical aperture NA such that the projected beam exhibits a spatial
frequency ℓ, where ℓ = λ/(2NA). The light source for the optical pick-up preferably is
a laser beam whose wave length is λ = 635nm, this laser beam being projected
through a lens whose numerical aperture is NA = 0.52, resulting in the spatial frequency ℓ = 611 nm.”). Das Streitpatent gibt somit an, dass mit diesen Werten für
die Wellenlänge und die numerische Apertur der Linse eine räumliche Auflösung
erreicht wird, die unter der Untergrenze des Spurabstandes liegt, was somit eine
optische Trennung der benachbarter Spuren voneinander gestattet. Die in der
Patentschrift angegebene Formel, die zur Berechnung von ℓ benutzt wird, ist zwar
eine Näherung, doch zeigt sie, dass eine optische Auflösung im Bereich des beanspruchten Spurabstandes möglich ist.


Die von der Klägerin durchgeführte Berechnung (vgl. den Schriftsatz vom
30. September 2016, Hauptantrag, Punkt 2.) geht von den Daten der CD aus und

                                       - 58 -


bestimmt die durch die Änderung der Wellenlänge und der numerischen Apertur
verursachte Änderung, womit sie auf einen Spurabstand von 1,1 µm kommt. Diese
Rechnung sagt aber nichts darüber aus, ob beim CD-Standard an die Grenze des
optischen Auflösungsvermögens gegangen wurde, so dass aus dem Vergleich der
beiden Rechnungen der Fachmann nur die Erkenntnis ziehen kann, dass bei der
CD ohne Änderung des optischen Auslesesystems noch ein geringerer Spurabstand als ihn die CD-Norm vorschreibt, möglich wäre. Insgesamt ergibt sich somit,
dass die Lehre in Bezug auf den Spurabstand so deutlich und vollständig offenbart
ist, dass ein Fachmann sie ausführen kann.


bb) Die    Klägerin   bezweifelt   zudem    die   Ausführbarkeit   der   Lehre   des
Merkmalskomplexes 59.7 bzw. 118.7 des Hilfsantrags 2 a (vgl. Schriftsatz vom
30. September 2016, Abschnitt Hilfsantrag III, Punkt 2b). Sie führt sinngemäß aus,
dass es nicht trivial sei, einen Code zu erstellen, der eine 8 nach 16 Codierung für
einen (2, 10) RLL-Code ist. Dem Fachmann werde im vorliegenden Patent kein
Beispiel gegeben, wie ein solcher Code aussehen könnte, insbesondere gäbe es
keine Tabellen, wie beispielsweise in den Dokumenten NK39 oder NK40, die eine
Lösung des Problems explizit darstellen würden.


Diesen Bedenken ist aber nicht zu folgen, denn der Fachmann weiß, wie er vorzugehen hat. Hierzu wird insbesondere auf die Druckschrift NK14 verwiesen, die
eine detaillierte Beschreibung der begrenzenden Eigenschaften von lauflängenbegrenzten Folgen und einen verständlichen Überblick der praktischen Aspekte der
Übersetzung beliebiger Daten in lauflängenbegrenzte Sequenzen gibt (vgl. die Zusammenfassung: „A detailed description is furnished of the limiting properties of
runlength-limited sequences, and a comprehensive review is given of the practical
aspects involved in the translation of arbitrary data into runlength-limited sequences.“). Druckschrift NK14 stellt somit eine Zusammenfassung des Wissens
des Fachmanns über lauflängenbegrenzte Codierung dar. In Druckschrift NK14
werden dabei auch Konstruktionsmethoden für RLL-Codes aufgezeigt. Das Streitpatent zeigt zwar keine explizite Lösung für einen zu verwendenden Code, doch
genügen dem Fachmann die in den Abs. [0123] bis [0158] gemachten Angaben,
um allein mit Hilfe seines Fachwissens selbst einen Code zu entwickeln. Dies mag

                                      - 59 -


einen großen Aufwand bedeuten und nur mit der Hilfe von Computern zu lösen
sein, doch spielt die Größe des Aufwands keine Rolle, solange der Fachmann
weiß, wie er vorzugehen hat. Da es sich um einen einmaligen Aufwand handelt, ist
dieser kein Hindernis.


Da die Klägerin keine weiteren Punkte für eine mangelnde Ausführbarkeit geltend
gemacht hat, und auch die übrigen Merkmale in ihrem Zusammenhang ausführbar
sind, sind die Lehren der Ansprüche 59 und 118 ausführbar. Auch bei den Lehren
der angegriffenen Unteransprüche besteht hinsichtlich der Ausführbarkeit kein
Zweifel.


c)   Das gewerblich anwendbare (Art. 57 EPÜ, § 5 PatG) Verfahren nach Anspruch 59 und der gewerblich anwendbare Gegenstand des Anspruchs 118 des
Hilfsantrags 2 a sind gegenüber dem Stand der Technik neu (Art. 54 EPÜ,
§ 3 PatG) und beruhen auch auf einer erfinderischen Tätigkeit des Fachmanns
(Art. 56 EPÜ, § 4 PatG). Sie sind damit patentfähig (Art. 52 Abs. 1 EPÜ, § 1 Abs. 1
PatG).


ca) Die Ansprüche 59 und 118 des Hilfsantrags 2 a enthalten gegenüber den
entsprechenden Ansprüchen nach Hilfsantrag 2 jeweils zwei weitere die Modulation betreffende Merkmale. Das erste Merkmal, dass mindestens ein 16-bit Wort
zwei verschiede 8-bit Informationswörter als Übersetzung hat, von denen eines in
einer Tabelle und das andere in einer anderen Tabelle gespeichert ist (Merkmal 59.7.7 bzw. 118.7.7), ist dabei für den Fachmann selbstverständlich, denn erst
diese Tatsache erfordert die Verwendung von Tabellen für die Decodierung, denn
anderenfalls könnten die Tabellen zu einer einzigen zusammengefasst werden.
Dass dies üblich ist, zeigt sich auch in dem einfachen Beispiel aus Druckschrift
NK14. Dort sind auf S. 1752 als Gleichungen 26 drei Tabellen gezeigt, von denen
zwei, nämlich W(σ2) und W(σ3) die gleichen Symbole enthalten. Diesen sind aber
zunächst noch keine Ausgangssymbole zugeordnet. In der Folge werden dann
dieselben Symbole denselben Ausgangssymbolen zugeordnet, nämlich jeweils
das Symbol „01“ dem Ausgangssymbol „1“ und das Symbol „10“ dem Ausgangssymbol „0“. Rein theoretisch macht es aber an dieser Stelle keinen Unterschied,

                                         - 60 -


wenn in der einen Tabelle W(σ2) diese Zuordnung auch so gemacht würde, die
Zuordnung in der Tabelle W(σ3) aber umgedreht würde, so dass dort dem Symbol
„01“ das Ausgangssymbol „0“ und dem Symbol „10“ das Ausgangssymbol „1“ zugeordnet würde. Dann erhielte man zwei Symbole, denen jeweils zwei unterschiedliche Ausgangssymbole zugeordnet wären, die sich aber in zwei unterschiedlichen Tabellen befänden. In diesem einfachen Fall ist es in der Folge ganz
einfach eine günstige Wahl zu treffen. In einem komplizierteren Fall ist diese
günstige Wahl aber meist nicht so leicht zu erkennen oder sogar unmöglich.


Auf das zweite Merkmal 59.7.8 bzw. 118.7.8, dass die Auswahl der Tabelle auch
die Untersuchung des dem aktuellen 16-Bit Wort folgenden 16-bit Wortes zusätzlich zum vorausgehenden 16-bit-Wort erfordert, gibt es lediglich in Druckschrift
NK14 einen Hinweis. Dort wird beschrieben, dass es auch Erzeugungsmethoden
für Codes gibt, bei denen die Codierung und in der Folge auch die Decodierung
von vergangenen und von zukünftigen Codewörtern abhängen kann (vgl. S. 1757,
linke Sp., 2. Abs.: „G. Look-Ahead Encoding Technique. Another class of design
techniques documented in the literature [29], [22], [30], [31], [18], [32] is called future-dependent or look-ahead (LA) coding. A block code is said to be look-ahead if
the encoding and decoding of a current block may depend on upcoming symbols.
The coding schemes may also depend on the current state of the channel and on
past as well as future symbols.”).


Zwar nimmt Druckschrift NK14 auch die CD als Einstieg für die in ihr gemachten
Ausführungen, doch fehlt ein konkreter Hinweis bzw. Anlass, eine solche Form der
lauflängenbegrenzten Codierung auch bei einer CD zu verwenden. Insbesondere
ist für den Fachmann nicht erkennbar, dass eine solche Lösung benötigt wird, um
das zusätzliche Problem des geringen Gleichstromanteils zu lösen, so dass es für
den Fachmann nicht naheliegt, diese Codierung zu verwenden.


Die Klägerin hat trotz des Hinweises des Senats in der mündlichen Verhandlung
auf Abschnitt „G Look-Ahead Encoding Technique“ der Druckschrift NK14 weder
Ausführungen gemacht, ob und insbesondere wie dieser Stand der Technik das
Merkmal 59.7.8 bzw. 118.7.8 nahelegen könnte, noch hat sie auf einen weiteren

                                      - 61 -


Stand der Technik hingewiesen, der das Merkmal, das in den von ihr ebenfalls bereits vor der mündlichen Verhandlung angegriffenen Unteransprüchen 87
bzw. 146 des Streitpatents enthalten ist, deren Patentfähigkeit nicht konkret angegriffen worden ist, nahelegen könnte. Sie hat in der Folge trotz ihres Angriffs auf
den nunmehr in Anspruch 118 des Hilfsantrags 2 a beanspruchten Gegenstand
bzw. das in Anspruch 59 des Hilfsantrags 2 a beanspruchte Verfahren auch nicht
angegeben, wie der Stand der Technik ausgehend von der Druckschrift NK9 diesen Gegenstand bzw. dieses Verfahren nahelegen könnte.


cb) Die einzige Druckschrift, die die zusätzlichen Merkmale der Ansprüche 59
und 118 des Hilfsantrags 2 a in Zusammenhang mit einer optischen Speicherplatte offenbart, ist die Druckschrift NK29, die von der Anmeldung des Streitpatents abgetrennt wurde (vgl. Ansprüche 84 und 141). Diese weist aber in Bezug
auf die nach Hilfsantrag 2 a beanspruchten Verfahren und Gegenstände keinen
älteren Zeitrang als das Streitpatent auf, so dass sie nicht patenthindernd wirken
kann.


Der Zeitrang des Verfahrens des Anspruchs 59 und der Wiedergabevorrichtung
nach Anspruch 118 sind der Anmeldetag des Patents, also der 17. März 1995,
denn die in Anspruch genommene Prioritätsanmeldung JP 7444594 vom
19. März 1994 offenbart weder das Verfahren des Anspruchs 59 noch die Wiedergabevorrichtung des Anspruchs 118 gemäß Hilfsantrag 2 a.


So offenbart die Prioritätsanmeldung in ihren selbständigen Ansprüchen bezüglich
eines lauflängenbegrenzten Codes lediglich, dass eine (2, 10) Lauflängenbegrenzung erfolgt (vgl. in der Übersetzung der Prioritätsschrift NK3 die Ansprüche 1, 5,
8 und 11, z. B. in Anspruch 11 „…and undergoing modulation by using (2, 10) as
run length limited (d, k) code,…“). Weitere Angaben hierzu gibt es weder in den
selbständigen noch in den Unteransprüchen.


Die Beschreibung der Prioritätsschrift enthält zwei Beispiele. Ein erstes Beispiel
betrifft eine verbesserte 8 nach 14 Modulation, die mit zwei statt der bei der CD
üblichen drei Trennbits auskommt, so dass eine 8 nach 16 Codierung entsteht

                                           - 62 -


(vgl. die Abs. [0132] bis [0172] der Übersetzung NK3 der Prioritätsschrift). Da aber
beim Anspruch 59, wie auch beim Anspruch 118 eine Codierung mit Trennbits
ausgeschlossen ist (vgl. Merkmale 59.7.2 bzw. 118.7.2), ist dieses Ausführungsbeispiel ohne Relevanz.


Das zweite Beispiel (vgl. Abs. [0173] bis [0190]) kommt ohne Trennbits aus und
weist folgende die lauflängenbegrenzte Codierung betreffende Merkmale des Anspruchs 59 auf:


59.7 die Daten auf der Platte sind als lauflängenbegrenzter (RLL) Code moduliert und der Schritt des Demodulierens schließt die Decodierung der besagten
RLL Daten ein (vgl. Abs. [0174]: „8-16 modulation also satisfies the condition of
EFM which is a code in which zeros range from two to less than 10 between 1 and
1, i.e., run length limited (2, 10) code.”).


59.7.1 wobei besagter RLL Code ein (2,10) RLL Code ist, derart, dass
aufeinanderfolgende Datenübergänge nicht weniger als 2 Datenbitzellen und nicht
mehr als 10 Datenbitzellen auseinander sind (vgl. die zitierte Stelle aus
Abs. [0174]).


59.7.2 wobei besagter RLL Code als 16-bit Informationswörter ohne Trennbits zwischen den 16-bit Informationswörtern aufgezeichnet ist (vgl. Abs. [0174]: „On the
contrary, this system directly converts 8 bits into 16 bit code. There is no margin
bit.”),


59.7.3 wobei besagter Demodulationsschritt die besagten 16-bit Informationswörter in 8-bit Informationswörter umsetzt (vgl. Abs. [0190]: “In accordance with the
above-described method, it is possible to realize 8-16 modulation for directly converting 8 bits of input data into 16 bits by making reference to the table and demodulation of inverse conversion.”),


59.7.4 und besagter Demodulationsschritt weiter das Speichern einer Vielzahl von
8-bit Informationswörtern in jeder einer Mehrzahl von Tabellen aufweist (vgl.

                                         - 63 -


Abs. [0187]: „ In Fig. 31, tables IT1 ~ IT4 written in memories 84 ~ 87 such as
ROM, etc. serve to carry out inverse conversion with respect to conversion of the
respective fundamental tables T1 ~ T4. Here, since there is no common conversion
value with respect to respective tables Ta, Tb divided in dependency upon the
DSV and conversion value, i.e., original 8 bit value is univocally determined in inverse conversion, inverse conversion tables are combined into a single table.”),


59.7.5 Auswählen einer bestimmten Tabelle als eine Funktion eines vorhergehenden 16-bit Informationswortes, das von der Platte gelesen wurde (vgl. Abs. [0189]:
„Here, code which does not yet undergo inverse conversion is inputted to table
selector 83 to examine the end thereof to recognize the next table to switch selecting switch 83 to that table to obtain the next output.”),


59.7.7 wobei mindestens ein 16-bit Informationswort, das von der Platte gelesen
wird, zwei verschiedenen 8-bit Informationswörtern entspricht, wovon eines in einer Tabelle und das andere in einer anderen Tabelle gespeichert ist (Dies ist nicht
explizit offenbart, doch muss dem so sein, denn sonst könnten die Tabellen zu einer zusammengefasst werden. Die zitierte Stelle in Abs. [0187] zeigt, dass der
Autor sich darüber Gedanken gemacht hat, indem er angibt, dass die Ta und Tb
Versionen einer Tabelle für die Codierung immer zu einer einzigen Tabelle für die
Decodierung zusammengefasst werden können.).


Es verbleibt das Merkmal 59.7.8, dass der Auswahlschritt zusätzlich die Untersuchung des 16-bit Informationswortes, das dem gerade gelesenen als nächstes
folgt, aufweist, um die besagte eine oder die besagte andere Tabelle als Funktion
des nachfolgenden 16-bit Informationswortes auszuwählen. Diesen Schritt enthält
das Verfahren nicht. Zwar wird auch dort das nachfolgende 16-bit Informationswort zur Decodierung herangezogen, doch wird es nicht zur Auswahl der Tabelle
verwendet. Bei dem in diesem Beispiel verwendeten Code enthält eine Tabelle
mindestens ein 16-bit Informationswort, dem zwei 8-bit-Informationswörter zugeordnet sind. Diese befinden sich demnach nicht in zwei unterschiedlichen, sondern
in einer einzigen Tabelle. Es wird dann die richtige Decodierung an Hand des
nachfolgenden 16-Bit-Informationswortes ausgewählt, nicht aber die Tabelle.

                                        - 64 -


In der Prioritätsschrift ergibt sich das für den Fachmann als Ergebnis der Auflösung der darin enthaltenen widersprüchlichen Darstellungen. Zunächst sei hierzu
auf Abs. [0189] verwiesen, der die Decodierung beschreibt (vgl. Abs. [0189]:
„Moreover, in the case where the same conversion code is allocated to different 8
bit values in one table, it is necessary to recognize table to which the next code
belongs as described above. In view of this, an approach is employed to input
code inputted next of the preceding stage of register 82 to table selector 83 to read
it in advance to discriminate table of that code to switch selecting switch 88 to this
table.”). Die Bezugszeichen beziehen sich dabei auf Fig. 31. Dort wird gezeigt,
dass zwei Signale in die Auswahl eingehen, nämlich eines vor dem Register (82)
und eines nach dem Register (82). Danach wird die Tabelle ausgewählt. Was dies
genau bedeutet, ist, wenn von der Figur allein ausgegangen wird, unklar, denn
nach dem Register ist das Signal das, das dem aktuellen Wert entspricht. Auch
Abs. [0189] offenbart als Ergebnis die reine Auswahl der Tabelle („to switch selecting switch to this table.“)


Dem Fachmann wird dabei auffallen, dass er mit einer reinen Auswahl der Tabelle
keine eindeutige Decodierung vornehmen kann, denn die gleichen 16-Bit Informationswörter für zwei unterschiedliche 8-bit-Wörter befinden sich in einer Tabelle
(„in one table“), so dass dann, wenn er die Tabelle auswählt, immer noch zwei
Möglichkeiten der Decodierung bestehen. Er wird somit einen Widerspruch feststellen, den er im Folgenden auflösen muss.


Hierzu wird er auf Grund des Hinweises, dass die Decodierung schon vorher beschrieben worden sei („as described above“), den Inhalt der Abs. [0178]
und [0179], die damit gemeint sind, heranziehen. Dort ist nochmals eindeutig beschrieben, dass sich die gleichen 16-bit Informationswörter in einer Tabelle befinden und die Decodierung aus einer Tabelle mittels des nachfolgenden 16-bit Informationswortes erfolgt. Dies wird dann anhand eines Beispiels erläutert (vgl.
Abs. [0178] und [0179]: „Here, it is assumed that a conversion such that different
two input values are converted into the same code in the same fundamental table
is permitted. In this case, when there is employed an approach to change fundamental table used next into, e.g., table T2 or T3, original input value is univocally

                                         - 65 -


determined at the time of demodulation. For example, in the case where input
values are “10” and “20” in the fundamental table T2, when they are assumed to
be both converted into “0010000100100100”, an allocation is made such that
when input value is “10”, the next table is T2 and when input value is “20”, the next
table is T3. Accordingly, at the time of demodulation, in the case of carry out reverse conversion of “0010000100100100”, the next code is examined. If that code
belongs to the fundamental table T2, it is seen that the original value is “10”. If that
code belongs to the fundamental table T3, it is seen that the original value is
“20”.”). Damit wird der Fachmann den Widerspruch so auflösen, dass mit Hilfe des
nachfolgenden Wertes bei einer ausgewählten Tabelle der Wert ausgewählt wird,
in den ein 16-bit Informationswort decodiert wird.


Damit fällt das in der Prioritätsschrift offenbarte Verfahren und auch das dort offenbarte Lesegerät nicht unter den Anspruch 59 bzw. 118 des Hilfsantrags 2 a, da
das Verfahren das Merkmal 59.7.8 nicht aufweist. Insgesamt ist damit insbesondere der Anmeldetag des Streitpatents auch der Zeitrang für die Ansprüche 59
und 118 sowie alle auf diese Ansprüche rückbezogenen Unteransprüche.


Zwar ist dem Fachmann auf Grund seines Fachwissens klar, dass er die die zwei
Decodierungsmöglichkeiten enthaltende Tabelle auch in zwei dann jeweils nur
noch eine Decodierungsmöglichkeit enthaltende Tabellen aufspalten kann, um so
mittels des nachfolgenden 16-bit Informationswortes die jeweils richtige Tabelle
auswählen zu können, wie dies in den Ansprüchen 59 und 118 beansprucht wird,
jedoch wird gerade dieses im Beispiel der Prioritätsanmeldung nicht gemacht, so
dass es dort nicht offenbart ist.


Das Beispiel ist auch im Streitpatent enthalten (vgl. Abs. [0143] bis [0158]). Dort ist
der letzte Abs. [0158] insoweit allgemeiner gehalten, als dort der besagte Widerspruch nicht mehr auftritt. Er ergibt sich aber mit dem vorhergehenden Beispiel in
Abs. [0151], wo sich zeigt, dass die zwei Codierungen in dasselbe 16-bit Informationswort sich in derselben Tabelle befinden. Die Teilungsanmeldung enthält das
Beispiel in derselben Form wie das Streitpatent.

                                         - 66 -


Damit ergibt sich, dass das Beispiel aus der Teilungsanmeldung NK28 das Verfahren des Anspruchs 59 bzw. das Lesegerät des Anspruchs 118 nicht neuheitsschädlich vorwegnehmen kann. In Bezug auf die Ansprüche 84 und 141, welche
das Merkmal 59.7.8 bzw. 118.7.8 des Hilfsantrags 2 a offenbaren, weist die Teilungsanmeldung denselben Zeitrang wie die Ansprüche 59 und 118 des Hilfsantrags 2 a auf, nämlich den Anmeldetag des Streitpatents. Damit kann die Teilungsanmeldung weder das Verfahren des Anspruchs 59 noch den Gegenstand
des Anspruchs 118 neuheitsschädlich vorwegnehmen. Die von der Klägerin aufgeworfene Frage der neuheitsschädlichen Teilungsanmeldung („poisonous divisional“) stellt sich somit beim Hilfsantrag 2 a nicht.


d)      Die auf die schutzfähigen übergeordneten Ansprüche rückbezogenen
Unteransprüche stellen schutzfähige Ausprägungen der Lehre der Hauptansprüche dar.




                                           II.


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 92 Abs. 1
Satz 1 ZPO. Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 709
Satz 1 und 2 ZPO.




                                           III.


                        Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils - spätestens nach Ablauf von fünf Monaten nach Verkündung -
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder

                                        - 67 -


Patentanwalt      schriftlich   beim    Bundesgerichtshof,     Herrenstraße     45a,
76133 Karlsruhe, einzulegen.

Die Berufungsschrift muss

       - die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
       - die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,

enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils vorgelegt werden.

Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht (BGH/BPatGERVV) auf elektronischem Weg beim Bundesgerichtshof einzulegen, wird hingewiesen (www. bundesgerichtshof.de/erv.html).




Guth               Hartlieb        Brandt           Dr. Friedrich        Dr. Zebisch


                                                                                    Pr
