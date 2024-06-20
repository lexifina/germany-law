---
ecli: "ECLI:DE:BPatG:2024:200624U2Ni7.23EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 7/23"
decided: "2024-06-20"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2024&Sort=1&Seite=12&nr=44249&anz=391&pos=185&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2024-06-20_2_Ni_7_23_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 7/23 vom 2024-06-20

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                       Verkündet am
                                                       20. Juni 2024
2 Ni 7/23 (EP)

(Aktenzeichen)


                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2024:200624U2Ni7.23EP.0

                                       -2-




              betreffend das europäische Patent EP 2 777 269
                             (DE 60 2012 010 808)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts aufgrund der
mündlichen Verhandlung vom 20. Juni 2024 durch die Vorsitzende Richterin
Hartlieb sowie die Richter Dipl.-Phys. Univ. Dr. Forkel, Dr. Himmelmann, Dipl.-Phys.
Univ. Dr. Städele und Dr.-Ing. Harth für Recht erkannt:


I.      Das europäische Patent EP 2 777 269 wird mit Wirkung für das
        Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


II.     Die Kosten des Rechtsstreits trägt die Beklagte.


III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des zu
        vollstreckenden Betrages vorläufig vollstreckbar.




                                 Tatbestand




Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in französischer Verfahrenssprache erteilten europäischen Patents EP 2 777 269
(deutsches Aktenzeichen DE 60 2012 010 808) (Streitpatent), das am 6. November
2012 angemeldet und am 16. September 2015 veröffentlicht worden ist und das die
Bezeichnung „PROCÉDÉ DE CODAGE ET DÉCODAGE D’IMAGES, DISPOSITIF

                                        -3-



DE    CODAGE       ET    DÉCODAGE        ET    PROGRAMMES          D’ORDINATEUR
CORRESPONDANTS“ („Verfahren zur Codierung und Decodierung von Bildern,
Codierungs-      und       Decodierungsvorrichtung        sowie       entsprechende
Computerprogramme“) trägt. Das Streitpatent geht zurück auf die am 6. November
2012 angemeldete internationale Patentanmeldung PCT/FR2012/052551. Die
Anmeldung wurde am 16. Mai 2013 unter der internationalen Veröffentlichungsnummer WO 2013/068683 A1 veröffentlicht. Nach Eintritt in die europäische Phase
wurde die Anmeldung unter der europäischen Anmeldenummer 12794437.9 als
europäische Anmeldung geführt. Das Streitpatent nimmt die Priorität FR 1160114
vom 7. November 2011 in Anspruch und betrifft im Allgemeinen den Bereich der
Bildverarbeitung, genauer gesagt die Codierung und Decodierung von digitalen
Bildern und digitalen Bildsequenzen (Abs. [0001] Streitpatentschrift).


Das in vollem Umfang angegriffene Streitpatent umfasst 6 Patentansprüche,
darunter den auf ein „Verfahren zum Codieren wenigstens eines in Partitionen
unterteilten Bildes“ gerichteten Patentanspruch 1 und den nebengeordneten, auf ein
„Verfahren zum Decodieren eines Datensignals“ gerichteten Patentanspruch 3. Mit
dem nebengeordneten Patentanspruch 2 wird eine „Vorrichtung zum Codieren
wenigstens eines in Partitionen unterteilten Bildes“, mit dem nebengeordneten
Patentanspruch 4 eine „Vorrichtung zum Decodieren eines Datensignals“
beansprucht.     Der     nebengeordnete       Patentanspruch      5      betrifft   ein
„Rechnerprogramm, das Befehle enthält, um das Codierungsverfahren nach
Anspruch 1 auszuführen“. Der nebengeordnete Patentanspruch 6 betrifft ein
„Rechnerprogramm, das Befehle enthält, um das Decodierungsverfahren nach
Anspruch 4 auszuführen“.


Im Einzelnen lauten die sechs Patentansprüche in der französischen Fassung sowie
der deutschen Übersetzung des Streitpatents wie folgt:

                                         -4-



Patentanspruch 1:
Anspruch 1                               Übersetzung
Procédé de codage d´au moins une Verfahren zum Codieren wenigstens eines
image découpée en partitions,            in Partitionen unterteilten Bildes,
une partition courante (Bi) à coder wobei eine zu codierende aktuelle Partition
contenant des données                    (Bi) Daten enthält,
dont au moins une donnée est wovon wenigstens ein Datenelement mit
affectée d´un signe,                     einem Vorzeichen behaftet ist,
les données étant des coefficients de wobei die Daten Koeffizienten einer direkten
transformation direct,                   Transformation sind,
ledit   procédé     de   codage     étant wobei das Codierungsverfahren dadurch
caractérisé en ce qu´il met en gekennzeichnet ist, dass es für diese
oeuvre, pour ladite partition courante, aktuelle Partition die folgenden Schritte
les étapes suivantes:                    ausführt:
- calcul (S3) de la valeur d'une - Berechnen (S3) des Wertes einer Funktion,
fonction représentative de la parité de die die Parität der Summe der Daten der
la somme des données de ladite aktuellen Partition unter Ausschluss des
partition courante à l'exclusion dudit Vorzeichens, das verdeckt ist, repräsentiert,
signe soit caché,
- comparaison (S4) de ladite valeur - Vergleichen (S4) des berechneten Wertes
calculée à la parité dudit signe,        mit der Parität des Vorzeichens,
- en fonction du résultat de ladite -       in   Abhängigkeit    vom    Ergebnis   des
comparaison, modification (S5) ou Vergleichens Modifizieren (S5) oder nicht
non d'au moins une des données de Modifizieren            wenigstens      eines    der
la partition courante,                   Datenelemente der aktuellen Partition,
- en cas de modification, codage - im Fall des Modifizierens Codieren (S20)
(S20) des données de la partition der Daten der Partition, die das wenigstens
comprenant ladite au moins une eine modifizierte Datenelement enthält,
donnée modifiée

                                          -5-



sans le signe de ladite au moins une ohne das Vorzeichen des wenigstens einen
donnée modifiée.                           modifizierten Datenelements.




Patentanspruch 2:
Anspruch 2                                  Übersetzung
Dispositif de codage (CO) d´au moins Vorrichtung (CO) zum Codieren wenigstens
une image découpée en partitions,           eines in Partitionen unterteilten Bildes,
une      partition   courante    à   coder wobei eine zu codierende aktuelle Partition
contenant des données                       Daten enthält,
dont au moins une donnée est wovon wenigstens ein Datenelement mit
affectée d´un signe,                        einem Vorzeichen behaftet ist,
les données étant des coefficients de wobei die Daten die Koeffizienten einer
transformation direct,                      direkten Transformation sind,
ledit dispositif étant caractérisé en ce wobei         die     Vorrichtung      dadurch
qu´                                         gekennzeichnet ist, dass
il comprend des moyens d´traitement sie             Verarbeitungsmittel       (MTR_CO)
(MTR_CO) qui, pour ladite partition umfasst, die für diese zu codierende
courante à coder, sont aptes à:             aktuelle Partition dafür ausgelegt sind:
- calculer la valeur d'une fonction - den Wert einer Funktion, die die Parität der
représentative de la parité de la Summe der Daten der aktuellen Partition
somme        des     données    de   ladite repräsentiert,   unter    Ausschluss        des
partition courante à l'exclusion dudit Vorzeichens zu berechnen,
signe,
- comparer ladite valeur calculée à la - den berechneten Wert mit der Parität des
parité dudit signe,                         Vorzeichens zu vergleichen,
- modifier ou non au moins une des - wenigstens eines der Datenelemente der
données de la partition courante en aktuellen Partition in Abhängigkeit vom
fonction      du     résultat   de   ladite Ergebnis des Vergleichens zu modifizieren
comparaison,                                oder nicht zu modifizieren,

                                        -6-



et en ce qu´                             und dass
il comprend des moyens (CE_CO) de sie Mittel (CE_CO) umfasst, um im Fall des
codage des données de la partition Modifizierens durch die Verarbeitungsmittel
comprenant ladite au moins une Daten der Partition, die das wenigstens eine
donnée modifiée sans le signe de modifizierte Datenelement enthält, ohne
ladite au moins une donnée modifiée, das Vorzeichen des wenigstens einen
en cas de modification par lesdits modifizierten Datenelements zu codieren.
moyens de traitement.




Patentanspruch 3:
Anspruch 3                               Übersetzung
Procédé de décodage d'un signal de Verfahren            zum      Decodieren     eines
données représentatif d'au moins une Datensignals, dass wenigstens ein in
image découpée en partitions qui a été Partitionen unterteiltes Bild repräsentiert,
précédemment codée,                      das vorher codiert worden ist,
une partition courante (Bi) à décoder wobei      eine     zu   decodierende   aktuelle
contenant des données                    Partition (Bi) Daten enthält,
dont au moins une donnée est wovon wenigstens ein Datenelement mit
affectée d´un signe,                     einem Vorzeichen behaftet ist,
les données étant les coefficients de wobei die Daten die Koeffizienten einer
transformation direct,                   direkten Transformation sind,
ledit procédé de décodage étant wobei               das        Decodierungsverfahren
caractérisé en ce qu´il comprend, dadurch gekennzeichnet ist, dass es für
pour ladite partition courante, les die aktuelle Partition die folgenden Schritte
étapes suivantes :                       umfasst:
- décodage (SD2, SD3) des données - Decodieren (SD2, SD3) von Daten der
de   ladite    partition   courante,   à aktuellen Partition unter Ausschluss des
l'exclusion dudit signe,                 Vorzeichens,

                                        -7-



- calcul (SD4) de la valeur d'une - Berechnen (SD4) des Wertes einer
fonction représentative de la parité de Funktion, die die Parität der Summe der die
la somme des données décodées de codierten Daten der aktuellen Partition
ladite partition courante,                repräsentiert,
- obtention, à partir de ladite valeur anhand des berechneten Wertes Erhalten
calculée, de la valeur dudit signe,       des Wertes des Vorzeichens,
si la parité de la somme des données wobei, falls die Parität der Summe der
a une première valeur le signe est Daten           einen    ersten    Wert      hat,    das
positif                                   Vorzeichen positiv ist
et si la parité de la somme des und, falls die Parität der Summe der Daten
données a une deuxième valeur le einen zweiten Wert hat, das Vorzeichen
signe est négatif.                        negativ ist.




Patentanspruch 4:
Anspruch 4                                Übersetzung
Dispositif (DO) de décodage d´un Vorrichtung (DO) zum Decodieren eines
signal de données représentatif d´au Datensignals,          das    wenigstens     ein    in
moins     une   image    découpée     en Partitionen unterteiltes Bild repräsentiert,
partitions qui a été précédemment das im Voraus codiert worden ist,
codée,
une partition courante à decoder wobei             eine    zu    decodierende     aktuelle
contenant des données                     Partition Daten enthält,
dont au moins une donnée est wovon wenigstens ein Datenelement mit
affectée d´un signe,                      einem Vorzeichen behaftet ist,
les données étant les coefficients de wobei die Daten die Koeffizienten einer
transformation direct,                    direkten Transformation sind,
ledit dispositif de décodage étant wobei             die        Decodierungsvorrichtung
caractérisé en ce qu´                     dadurch gekennzeichnet ist, dass

                                     -8-



il comprend, pour ladite partition sie für die aktuelle zu decodierende
courante à décoder, des moyens Partition Verarbeitungsmittel (MTR DO)
d´traitement (MTR_DO) qui sont aptes umfasst, die dafür ausgelegt sind:
à:
- décoder les données de ladite - die Daten der aktuellen Partition unter
partition courante, à l'exclusion dudit Ausschluss     des      Vorzeichens     zu
signe,                                decodieren,
- calculer la valeur d'une fonction - den Wert einer Funktion zu berechnen, die
représentative de la parité de la die Parität der Summe der decodierten
somme des données décodées de Daten der aktuellen Partition repräsentiert,
ladite partition courante,
- obtenir, à partir de ladite valeur - anhand des berechneten Wertes den Wert
calculée, la valeur dudit signe,      des Vorzeichens zu erhalten,
si la parité de la somme des données wobei, falls die Parität der Summe der
a une première valeur le signe est Daten       einen   ersten    Wert   hat,   das
positif                               Vorzeichen positiv ist
et si la parité de la somme des und, falls die Parität der Summe der Daten
données a une deuxième valeur la einen zweiten Wert hat, das Vorzeichen
signe est négatif.                    negativ ist.


Patentanspruch 5:
Anspruch 5                           Übersetzung
Programme d´ordinateur comportant Rechnerprogramm, das Befehle enthält, um
des instructions pour mettre en das Codierungsverfahren nach Anspruch 1
oeuvre le procédé de codage selon auszuführen,
la revendication 1,
lorsque ledit procédé de codage est wenn das Codierungsverfahren auf einem
exécuté sur un ordinateur.           Rechner ausgeführt wird.

                                        -9-



Patentanspruch 6:
 Anspruch 6                                Übersetzung
 Programme d´ordinateur comportant Rechnerprogramm, das Befehle enthält, um
 des instructions pour mettre en das Decodierungsverfahren nach Anspruch
 oeuvre le procédé de décodage 4 auszuführen,
 selon la revendication 4,
 lorsque ledit procédé de décodage wenn das Decodierungsverfahren auf einem
 est exécuté sur un ordinateur.            Rechner ausgeführt wird.




Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:
NK A          Verletzungsklageschrift der Beklagten gegen die die Klägerin, die T…
              SAS und die T… Ltd. (Schriftsatz der Patent-, Rechtsanwälte E…,
              H…, vom 15. November 2022 an das LG M…);
NK B          Protokoll über die öffentliche Sitzung des 2. Senats (Nichtigkeitssenat)
              des    Bundespatentgerichts      vom     16.   März     2023      in   der
              Patentnichtigkeitssache 2 Ni 39/21 (EP);
NK I          EP 2 777 269 B1 (Streitpatentschrift);
NK I-DE       EP 2 777 269, deutsche Übersetzung der Erfindungsbeschreibung;
NK II         DPMA, Registerauszug zum Aktenzeichen 60 2012 010 808.8,
              Stand am 22. März 2023;
NK III        Merkmalsgliederung     der    Verfahrensansprüche       1   und   3    des
              Streitpatents;
NK IV         WO 2013/068683 A1;
NK IV-DE      Deutsche Maschinenübersetzung der ursprünglichen Anmeldung WO
              2013/068683 A1;
NK 1          J.-M. Thiesse et al.: „Rate Distortion Data Hiding of Motion Vector
              Competition Information in Chroma and Luma Samples for Video
              Compression“, IEEE Transactions on Circuits and Systems for Video
              Technology, Vol. 21, No. 6, June 2011, S. 729-741;

                                    - 10 -



NK 2       J.-M. Thiesse et al.: „Data Hiding of Intra Prediction Information in
           Chroma Samples for Video Compression”, in: 2010 17th IEEE
           International Conference on Image Processing, 26.-29. Sept. 2010, S.
           2861-2864;
NK 3       E. Esen et al.: „Robust Video Data Hiding Using Forbidden Zone Data
           Hiding and Selective Embedding“, IEEE Transactions on Circuits and
           Systems for Video Technology, Vol. 21, No. 8, August 2011, S. 1130-
           1138;
NK 4       J. K. Paruchuri et al.: „Joint Optimization of Data Hiding and Video
           Compression“, IEEE International Symposium on Circuits and
           Systems, 2008, S. 242-245;
NK 5       F. Bossen et al.: „Video Coding Using a Simplified Block Structure and
           Advanced Coding Techniques”; in: IEEE Transactions on Circuits and
           Systems for Video Technology, Vol. 20, Nr.12, December 2010,
           S. 1667-1675;
NK 6       R. Cohen et al.: „Low Complexity Embedding of Information in
           Transform Coefficients”; Document JCTVC-E428_r2, 5. Meeting des
           Joint Collaborative Team on Video Coding (JCT-VC), Geneva, 16. -
           23. März 2011;
NK 7       D. Marpe et al.: „The H.264/MPEG4 Advanced Video Coding Standard
           and its Applications“, Standards Report, IEEE Communications
           Magazine, August 2006;
NK 8       Y. Wang et al.: „Video Processing and Communications“, Prentice
           Hall, Signal Processing Series, 2002 (in Auszügen);
NK 9       B. Bross et al.: „WD4: Working Draft 4 of High-Efficiency Video
           Coding”,   Document    JCTVC-F803_d5,       6.   Meeting   des   Joint
           Collaborative Team on Video Coding (JCT-VC), Torino, 14. - 22. Juli
           2011;
NK 9-pub   JCT-VC DOCUMENT MANAGEMENT SYSTEM, Preview document
           JCTVC-F803 for Torino meeting (MPEG number m21449), B. Bross,
           W.-J. Han, J.-R. Ohm, G. J. Sullivan, T. Wiegand (Editors);

                                      - 11 -



NK 10        I. Amonou et al.: „Description of video coding technology proposal by
             France Telecom, NTT, NTT DOCOMO, Panasonic and Technicolor“,
             Document JCTVC-A114, 1. Meeting des Joint Collaborative Team on
             Video Coding (JCT-VC), Dresden, 15. - 23. April 2010.


Die Klägerin stellt den Antrag,
             das europäische Patent EP 2 777 269 in vollem Umfang mit Wirkung
             für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig zu
             erklären.


Die Beklagte stellt den Antrag,
             die Klage abzuweisen,
             hilfsweise
             das europäische Patent EP 2 777 269 unter Klageabweisung im
             Übrigen dadurch teilweise für nichtig zu erklären, dass seine
             Patentansprüche die Fassung der Hilfsanträge I bis XII vom 18. März
             2024, in dieser Reihenfolge, erhalten.


Die Beklagte tritt der Argumentation der Klägerin in allen wesentlichen Punkten
entgegen. Sie vertritt die Auffassung, dass die beanspruchte Lehre auf einer
erfinderischen Tätigkeit des Fachmanns beruhe, ausführbar und ursprünglich
offenbart sei. Die beanspruchte Lehre sei jedenfalls in einer der Fassungen der
Hilfsanträge patentfähig.


Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:
ES1        Urteil des BPatG vom 4. August 2022 in der Patentnichtigkeitssache
           2 Ni 6/21 (EP);
ES2        Urteil des BPatG vom 16. März 2023 in der Patentnichtigkeitssache
           2 Ni 39/21 (EP);
ES3        Merkmalsgliederungen der Patentansprüche 1 bis 4;

                                      - 12 -



ES4       H.S. Malvar et al., „Low-Complexity Transform and Quantization in
          H.264/AVC“, : IEEE Transactions on Circuits and Systems for Video
          Technology, Vol. 13, No. 7, July 2003, S. 598-603;
ES5       P. Campisi et al.,”Compressive Data Hiding: An Unconventional
          Approach for Improved Color Image Coding”, in: EURASIP Journal on
          Advances in Signal Processing, February 2003, S. 152-163.


Die Beklagte hat in der mündlichen Verhandlung am 20. Juni 2024 erklärt, dass sie
die   Patentansprüche   gemäß     Hauptantrag   und   Hilfsanträgen   als   jeweils
geschlossene Anspruchssätze ansehe, die jeweils insgesamt beansprucht würden.


Hilfsantrag I vom 18. März 2024 lautet:

- 13 -

- 14 -

                                       - 15 -



Hilfsantrag II vom 18. März 2024 lautet:

- 16 -

                                       - 17 -




Hilfsantrag III vom 18. März 2024 lautet:

- 18 -

- 19 -

                                      - 20 -




Hilfsantrag IV vom 18. März 2024 lautet:

- 21 -

- 22 -

                                      - 23 -




Hilfsantrag V vom 18. März 2024 lautet:

- 24 -

- 25 -

- 26 -

                                      - 27 -



Hilfsantrag VI vom 18. März 2024 lautet:

- 28 -

- 29 -

                                      - 30 -




Hilfsantrag VII vom 18. März 2024 lautet:

                                       - 31 -




Hilfsantrag VIII vom 18. März 2024 lautet:

- 32 -

                                      - 33 -



Hilfsantrag IX vom 18. März 2024 lautet:

                                      - 34 -




Hilfsantrag X vom 18. März 2024 lautet:

- 35 -

                                      - 36 -




Hilfsantrag XI vom 18. März 2024 lautet:

- 37 -

                                      - 38 -



Hilfsantrag XII vom 18. März 2024 lautet:

                                         - 39 -




Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                              Entscheidungsgründe


Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6   Abs. 1 Satz 1    Nr.   1 IntPatÜbkG   i. V. m.   Art. 138   Abs. 1 lit. a)
EPÜ i. V. m. Art. 52 und 56 EPÜ, der Nichtigkeitsgrund der unzureichenden
Offenbarung nach Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜbkG, Art. 138 Abs. 1 lit. b)

                                           - 40 -



EPÜ i. V. m. Art. 83 EPÜ und der Nichtigkeitsgrund der unzulässigen Erweiterung
nach Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜbkG, Art. 138 Abs. 1 lit. c) EPÜ i. V. m.
Art. 100 lit. c) EPÜ geltend gemacht wird, ist zulässig.


Die Klage ist auch begründet. Das Streitpatent ist für nichtig zu erklären, weil es
weder in der erteilten Fassung nach Hauptantrag noch in der Fassung eines der
Hilfsanträge Bestand hat.




                                             I.


1.       Das Streitpatent betrifft die Codierung und Decodierung von digitalen Bildern
(vgl. Streitpatentschrift NK I, Absatz [0001]). Es geht von Videocodierern aus, wie
sie beispielsweise aus den Standards MPEG oder H.264 bekannt sind. Gemäß
diesen Standards sind die zu codierenden Videobilder in Makroblöcke unterteilt,
welche jeweils aus Blöcken bestehen, die durch Vorhersage von Intra- oder Inter-Bildern codiert werden (NK I, Absatz [0003]). Für jeden Block wird ein Restblock
codiert, der dem ursprünglichen Block abzüglich einer Vorhersage entspricht. Die
Restblöcke werden durch eine Transformation nach Art einer diskreten
Kosinustransformation („DCT“) transformiert und danach quantisiert, so dass
Koeffizienten erhalten werden, von denen einige positiv und andere negativ sind.
Diese werden im Allgemeinen in einer Zickzack-Leseanordnung durchlaufen. Am
Ende des Durchlaufs wird eine eindimensionale Liste mit Koeffizienten erhalten, die
„quantisierter Rest“ genannt wird. Die Koeffizienten dieser Liste werden
anschließend entropiecodiert (NK I, Absatz [0004]).


Daneben werden auch die folgenden Informationen entropiecodiert (NK I, Absatz
[0005]):


     •   eine Information, die die Position des letzten von null verschiedenen
         Koeffizienten der Liste angibt;

                                           - 41 -



   •   für alle Koeffizienten, die vor dem letzten von null verschiedenen
       Koeffizienten liegen, eine Information, die angibt, ob ein jeweiliger Koeffizient
       gleich null ist oder nicht;
   •   für jeden von null verschiedenen Koeffizienten eine Information, die angibt,
       ob der Koeffizient gleich eins ist oder nicht;
   •   für jeden von null und eins verschiedenen Koeffizienten, der vor dem letzten
       von null verschiedenen Koeffizienten liegt, der um zwei verminderte absolute
       Koeffizientenwert;
   •   für jeden von null verschiedenen Koeffizienten dessen Vorzeichen, wobei „0“
       einem positiven und „1“ einem negativen Vorzeichen entspricht.


Zudem werden Informationen codiert, die für den verwendeten Codierungsmodus
repräsentativ    sind,    z. B.      der   Vorhersagemodus        (Inter-,   Intra-   oder
Standardvorhersage) oder das verwendete Transformationsverfahren (wie etwa
„DCT    4x4“,   d. h.    eine     auf   einem   4x4-Pixelgitter   ausgeführte     diskrete
Kosinustransformation). Die codierten quantisierten Reste und die übrigen
codierten Informationen eines Blocks bilden ein Datensignal, das an den Decodierer
übertragen wird (NK I, Absatz [0006]).


In der Streitpatentschrift wird ferner ausgeführt, dass aus dem Stand der Technik
ein Verfahren zum „Verbergen von Daten“ („Data Hiding“) vorgeschlagen worden
sei, bei dem die Codierung eines sogenannten „Konkurrenzindex“ - beispielsweise
des Index „MVComp“, der einem im Inter-Vorhersagemodus codierten Block
zugeordnet ist und den Wert 0 oder 1 haben kann - in Form eines separaten
Bestandteils des Datensignals vermieden wird. Dazu wird der Wert des
Konkurrenzindex in der Summe der Transformationskoeffizienten des quantisierten
Rests des Blocks „verborgen“, d. h. durch die Parität dieser Summe implizit
ausgedrückt. In diesem Zusammenhang meint Parität die Eigenschaft einer ganzen
Zahl, gerade oder ungerade zu sein. Eine gerade Summe (gerade Parität) der
Koeffizienten stellt eine 0 dar, eine ungerade Summe eine 1. Die Parität der Summe
kann dem zu repräsentierenden Wert (0 oder 1) entweder entsprechen oder nicht.

                                     - 42 -



Im zweiten Fall ist es notwendig, mindestens einen Transformationskoeffizienten
durch Addition oder Subtraktion eines ungeraden Zahlenwerts (z. B. von 1, 3 oder
5) zu modifizieren, damit eine ungerade Summe der Transformationskoeffizienten
gerade wird oder umgekehrt. Der Decodierer bestimmt dann die Parität der Summe
der aus dem Datensignal rekonstruierten Transformationskoeffizienten und erhält
dadurch den „verborgenen“ Wert des Konkurrenzindex (NK I, Absätze [0010],
[0011]).




2.    Das Streitpatent kritisiert, dass bei diesem bekannten Verfahren die
modifizierten Koeffizienten nicht immer optimal ausgewählt werden, so dass die
Modifikationen in dem Datensignal, das an den Decodierer übermittelt wird,
Störungen hervorrufen und der Effizienz der Videokompression schaden. Zudem
seien die Reduktion der Signalisierungskosten und die Kompressionseffizienz nicht
optimal, weil der Konkurrenzindex MVComp die Werte 0 und 1 nicht mit gleicher
Wahrscheinlichkeit annehme. Daher sei die eingesparte Datenmenge kleiner als ein
Bit pro Index MVComp, wohingegen in der Parität des quantisierten Rests aber ein
(ganzes) Bit pro Index übertragen werden könne (NK I, Absatz [0011]).


Hiervon ausgehend macht es sich das Streitpatent zur Aufgabe, diese Nachteile
des Standes der Technik zu beheben (NK I, Absatz [0012]).




3.    Erfindungsgemäß soll diese Aufgabe gelöst werden durch ein Verfahren bzw.
eine Vorrichtung zum Codieren wenigstens eines in Partitionen unterteilten Bildes
nach Patentanspruch 1 bzw. Patentanspruch 2, ein Verfahren bzw. eine Vorrichtung
zum Decodieren eines Datensignals nach Patentanspruch 3 bzw. Patentanspruch 4, sowie durch ein „Rechnerprogramm, das Befehle enthält, um das
Codierungsverfahren nach Anspruch 1 auszuführen“ gemäß Patentanspruch 5 und
ein „Rechnerprogramm, das Befehle enthält, um das Decodierungsverfahren nach
Anspruch 4 auszuführen“ gemäß Patentanspruch 6.

                                       - 43 -



Die Merkmale der Patentansprüche 1 bis 6 können wie folgt gegliedert werden (mit
angepasster Übersetzung und nach Korrektur eines grammatikalischen Fehlers in
Patentanspruch 4):


Patentanspruch 1:


         Anspruch 1                              Übersetzung
M1.1     Procédé de codage d´au moins une Verfahren zum Codieren wenigstens
         image découpée en partitions,           eines     in    Partitionen   unterteilten
                                                 Bildes,
M1.2     une partition courante (Bi) à coder wobei eine zu codierende aktuelle
         contenant des données                   Partition (Bi) Daten enthält,
M1.2.1 dont au moins une donnée est wovon                       denen   wenigstens     ein
         affectée d´un signe,                    Datenelement mit einem Vorzeichen
                                                 behaftet ist,
M1.2.2 les données étant des coefficients de wobei die Daten Koeffizienten einer
         transformation direct,                  direkten Transformation sind,
M1.2.3 ledit    procédé     de    codage   étant wobei      das     Codierungsverfahren
         caractérisé en ce qu´il met en dadurch gekennzeichnet ist, dass
         oeuvre, pour ladite partition courante, es für diese aktuelle Partition die
         les étapes suivantes:                   folgenden Schritte ausführt umsetzt:
M1.3     calcul (S3) de la valeur d'une fonction Berechnen (S3) des Wertes einer
         représentative de la parité de la Funktion, die die Parität der Summe
         somme       des   données   de    ladite der Daten der aktuellen Partition
         partition courante                      repräsentiert,
M1.3.1 à l'exclusion dudit signe soit caché,     unter Ausschluss des Vorzeichens,
                                                 das verdeckt verborgen werden soll,
                                                 ist, repräsentiert,

                                       - 44 -



M1.4     comparaison (S4) de ladite valeur Vergleichen (S4) des berechneten
         calculée à la parité dudit signe,         Wertes     mit     der     Parität      des
                                                   Vorzeichens,
M1.5     en fonction du résultat de ladite in Abhängigkeit vom Ergebnis des
         comparaison, modification (S5) ou Vergleichens Modifizieren (S5) oder
         non d'au moins une des données de nicht Nicht-Modifizieren wenigstens
         la partition courante,                    eines    der     Datenelemente          der
                                                   aktuellen Partition,
M1.6     en cas de modification, codage (S20) im Fall des Modifizierens Codieren
         des    données      de   la    partition (S20) der Daten der Partition, die das
         comprenant ladite au moins une wenigstens                    eine         modifizierte
         donnée modifiée                           Datenelement enthält,
M1.6.1 sans le signe de ladite au moins une ohne             das       Vorzeichen          des
         donnée modifiée.                          wenigstens       einen         modifizierten
                                                   Datenelements.




Patentanspruch 2:


         Anspruch 2                                Übersetzung
M2.1     Dispositif de codage (CO) d´au Vorrichtung (CO) zum Codieren
         moins une image découpée en wenigstens                     eines    in     Partitionen
         partitions,                               unterteilten Bildes,
M2.2     une    partition   courante   à     coder wobei eine zu codierende aktuelle
         contenant des données                     Partition Daten enthält,
M2.2.1   dont au moins une donnée est wovon                  denen        wenigstens       ein
         affectée d´un signe,                      Datenelement mit einem Vorzeichen
                                                   behaftet ist,
M2.2.2   les données étant des coefficients de wobei die Daten die Koeffizienten
         transformation direct,                    einer direkten Transformation sind,

                                       - 45 -



         ledit dispositif étant caractérisé en wobei       die        Vorrichtung    dadurch
         ce qu´                                   gekennzeichnet ist, dass
M2.2.3   il comprend des moyens d´traitement sie Verarbeitungsmittel (MTR_CO)
         (MTR_CO) qui, pour ladite partition umfasst, die für diese zu codierende
         courante à coder, sont aptes à:          aktuelle Partition dafür ausgelegt
                                                  sind:,
M2.3     calculer la valeur d'une fonction den Wert einer Funktion, die die
         représentative de la parité de la Parität der Summe der Daten der
         somme      des   données     de   ladite aktuellen      Partition       repräsentiert,
         partition courante                       unter Ausschluss des Vorzeichens
                                                  zu berechnen,
M2.3.1   à l'exclusion dudit signe,               unter Ausschluss des Vorzeichens,
M2.4     comparer ladite valeur calculée à la den berechneten Wert mit der Parität
         parité dudit signe,                      des Vorzeichens zu vergleichen,
M2.5     modifier ou non au moins une des wenigstens                       eines           der
         données de la partition courante en Datenelemente                 der       aktuellen
         fonction    du   résultat    de   ladite Partition      in     Abhängigkeit       vom
         comparaison,                             Ergebnis       des      Vergleichens      zu
                                                  modifizieren          oder       nicht    zu
                                                  modifizieren,
         en ce qu´                                und dass
M2.6     il comprend des moyens (CE_CO) sie Mittel (CE_CO) umfasst, um im
         de codage des données de la Fall des Modifizierens durch die
         partition comprenant ladite au moins Verarbeitungsmittel                Daten     der
         une donnée modifiée sans le signe Partition, die das wenigstens eine
         de ladite au moins une donnée modifizierte Datenelement enthält,
         modifiée, en cas de modification par ohne            das        Vorzeichen        des
         lesdits moyens de traitement.            wenigstens           einen     modifizierten
                                                  Datenelements zu codieren.

                                        - 46 -



Patentanspruch 3:


         Anspruch 3                                Übersetzung
M3.1     Procédé de décodage d'un signal de Verfahren zum Decodieren eines
         données représentatif d'au moins une Datensignals, dass wenigstens ein in
         image découpée en partitions qui a Partitionen               unterteiltes     Bild
         été précédemment codée,                   repräsentiert, das vorher codiert
                                                   worden ist,
M3.2     une partition courante (Bi) à décoder wobei eine zu decodierende aktuelle
         contenant des données                     Partition (Bi) Daten enthält,
M3.2.1 dont au moins une donnée est wovon                     denen      wenigstens     ein
         affectée d´un signe,                      Datenelement mit einem Vorzeichen
                                                   behaftet ist,
M3.2.2 les données étant les coefficients de wobei die Daten die Koeffizienten
         transformation direct,                    einer direkten Transformation sind,
M3.2.3 ledit procédé de décodage étant wobei das Decodierungsverfahren
         caractérisé en ce qu´il comprend, dadurch gekennzeichnet ist, dass
         pour ladite partition courante, les es für die aktuelle Partition die
         étapes suivantes:                         folgenden Schritte umfasst:
M3.3     décodage (SD2, SD3) des données Decodieren (SD2, SD3) von Daten
         de   ladite   partition    courante,    à der    aktuellen      Partition    unter
         l'exclusion dudit signe,                  Ausschluss des Vorzeichens,
M3.4     calcul (SD4) de la valeur d'une Berechnen (SD4) des Wertes einer
         fonction représentative de la parité de Funktion, die die Parität der Summe
         la somme des données décodées de der die codierten Daten der aktuellen
         ladite partition courante,                Partition repräsentiert,
M3.5     obtention, à partir de ladite valeur anhand des berechneten Wertes
         calculée, de la valeur dudit signe,       Erhalten        des     Wertes      des
                                                   Vorzeichens,

                                   - 47 -



M3.5.1 si la parité de la somme des données wobei, falls die Parität der Summe
         a une première valeur le signe est der Daten einen ersten Wert hat, das
         positif                             Vorzeichen positiv ist
M3.5.2 et si la parité de la somme des und, falls die Parität der Summe der
         données a une deuxième valeur le Daten einen zweiten Wert hat, das
         signe est négatif.                  Vorzeichen negativ ist.




Patentanspruch 4:


         Anspruch 4                          Übersetzung
M4.1     Dispositif (DO) de décodage d´un Vorrichtung (DO) zum Decodieren
         signal de données représentatif d´au eines Datensignals, das wenigstens
         moins une image découpée en ein in Partitionen unterteiltes Bild
         partitions qui a été précédemment repräsentiert, das vorher im Voraus
         codée,                              codiert worden ist,
M4.2     une partition courante à decoder wobei eine zu decodierende aktuelle
         contenant des données               Partition Daten enthält,
M4.2.1   dont au moins une donnée est wovon            denen       wenigstens     ein
         affectée d´un signe,                Datenelement mit einem Vorzeichen
                                             behaftet ist,
M4.2.2   les données étant les coefficients de wobei die Daten die Koeffizienten
         transformation direct,              einer direkten Transformation sind,
         ledit dispositif de décodage étant wobei die Decodierungsvorrichtung
         caractérisé en ce qu´               dadurch gekennzeichnet ist, dass
M4.2.3   il comprend, pour ladite partition sie für die aktuelle zu decodierende
         courante à décoder, des moyens Partition              Verarbeitungsmittel
         d´traitement (MTR_DO) qui sont (MTR_DO)             umfasst,   die     dafür
         aptes à:                            ausgelegt sind:

                                       - 48 -



M4.3     décoder    les   données     de    ladite die Daten der aktuellen Partition
         partition courante, à l'exclusion dudit unter Ausschluss des Vorzeichens
         signe,                                   zu decodieren,
M4.4     calculer la valeur d'une fonction den           Wert    einer      Funktion     zu
         représentative de la parité de la berechnen,           die   die    Parität    der
         somme des données décodées de Summe der decodierten Daten der
         ladite partition courante,               aktuellen Partition repräsentiert,
M4.5     obtenir, à partir de ladite valeur anhand des berechneten Wertes
         calculée, la valeur dudit signe,         den   Wert    des   Vorzeichens        zu
                                                  erhalten,
M4.5.1   si la parité de la somme des données wobei, falls die Parität der Summe
         a une première valeur le signe est der Daten einen ersten Wert hat, das
         positif                                  Vorzeichen positiv ist
M4.5.2   et si la parité de la somme des und, falls die Parität der Summe der
         données a une deuxième valeur la le Daten einen zweiten Wert hat, das
         signe est négatif.                       Vorzeichen negativ ist.




Patentanspruch 5:


         Anspruch 5                               Übersetzung
M5.1     Programme d´ordinateur comportant Rechnerprogramm,                 das   Befehle
         des instructions pour mettre en enthält,                     um                das
         oeuvre le procédé de codage selon Codierungsverfahren                         nach
         la revendication 1,                      Anspruch 1 auszuführen,
M5.2     lorsque ledit procédé de codage est wenn das Codierungsverfahren auf
         exécuté sur un ordinateur.               einem Rechner ausgeführt wird.

                                          - 49 -



Patentanspruch 6:


           Anspruch 6                               Übersetzung
 M6.1      Programme d´ordinateur comportant Rechnerprogramm,                   das   Befehle
           des instructions pour mettre en enthält,                        um            das
           oeuvre le procédé de décodage Decodierungsverfahren                          nach
           selon la revendication 4,                Anspruch 4 auszuführen,
 M6.2      lorsque ledit procédé de décodage wenn das Decodierungsverfahren
           est exécuté sur un ordinateur.           auf einem Rechner ausgeführt wird.




4.      Als zuständiger Durchschnittsfachmann, der vorliegend mit der Aufgabe
betraut wird, die zu übertragende Datenmenge für codierte Videos zu verringern
und eine effizientere Decodierung zu ermöglichen, ohne große Störungen in den
decodierten Bilddaten hervorzurufen, ist ein Hochschulabsolvent aus dem Bereich
der   Informationstechnik,   Informatik     oder   Elektrotechnik    mit    mehrjähriger
Berufserfahrung auf dem Gebiet der Entwicklung von digitalen Videocodierund -decodierverfahren anzusehen, der mit den dabei zum Einsatz kommenden
Techniken und den wichtigen Standards vertraut ist und dem insbesondere die im
Rahmen       der     Standardisierungsprozesse        diskutierten       Beiträge      zur
Weiterentwicklung bestehender Standards bekannt sind.




5.      Zur Lehre des Streitpatents


Die eigentliche Leistung des Streitpatents liegt darin, mittels eines (an sich
bekannten)     Data-Hiding-Verfahrens        Vorzeichen   der       zu     übertragenden
Transformationskoeffizienten zu verbergen (vgl. NK I, Absatz [0012]). Diese
Vorzeichen bieten sich in besonderer Weise an, verborgen zu werden, weil bei den
Transformationskoeffizienten positive und negative Vorzeichen mit gleicher
Wahrscheinlichkeit auftreten, so dass beim Verbergen eines Vorzeichens jeweils

                                       - 50 -



ein ganzes Bit eingespart wird und daher die Signalisierungskosten erheblich
reduziert werden können (vgl. NK I, Absatz [0013]).


5.1   Zum erteilten Patentanspruch 1


5.1.1 Das Codierverfahren nach dem Patentanspruch 1 des Streitpatents betrifft
wenigstens ein „in Partitionen unterteiltes“ (digitales) Bild (Merkmal M1.1). Absatz
[0020] der Streitpatentschrift ist zu entnehmen, dass der Begriff „Partition“ eine
Codierungseinheit bezeichnet, wie sie etwa aus dem HEVC/H.265-Standard
bekannt ist, d. h. einen rechteckigen Block, der aus einzelnen Pixeln
zusammengesetzt ist.


Gemäß den Merkmalen M1.2 und M1.2.2 soll eine zu codierende aktuelle Partition
Koeffizienten einer „direkten“ Transformation enthalten. Unter einer derartigen
Transformation versteht der Fachmann eine (Vorwärts-)Transformation in einen
anderen Raum (z. B. eine herkömmliche diskrete Kosinustransformation (DCT) aus
dem Ortsraum in den Frequenzraum), die durch eine entsprechende inverse
Transformation rückgängig gemacht werden kann (vgl. NK I, Absätze [0081], [0186];
s. auch ES4, Seite 599, rechte Spalte, erster vollständiger Absatz sowie Seite 600,
linke Spalte, letzter Absatz i. V. m. Figur 1). Ein „Koeffizient einer direkten
Transformation“ ist somit ein Koeffizient, der aus einer solchen Transformation
hervorgegangen ist (wie etwa ein quantisierter DCT-Koeffizient). Merkmal M1.2.1
legt die Menge der Koeffizienten dahingehend fest, dass wenigstens einer der
Koeffizienten mit einem Vorzeichen behaftet - also von null verschieden - sein soll.
Dem Fachmann ist geläufig, dass das (positive oder negative) Vorzeichen eines
Koeffizienten üblicherweise mittels eines separaten 1-bit-wertigen Syntaxelements
codiert wird (vgl. das auf den Seiten 45 und 77 des Standardisierungsbeitrags NK 9
angegebene Syntaxelement „coeff_sign_flag[ n ]“).


Weiterhin soll das beanspruchte Codierverfahren für die aktuelle Partition mehrere
Schritte umsetzen, die in den Merkmalen M1.3 bis M1.6.1 beschrieben sind

                                        - 51 -



(Merkmal M1.2.3):


5.1.2 So soll zunächst der Wert einer Funktion berechnet werden, die die Parität
der Summe der Daten der aktuellen Partition repräsentiert (Merkmal M1.3).


Die Parität dieser Summe bezeichnet die Eigenschaft der Summe, einen geraden
oder ungeraden Zahlenwert zu haben. In diesem Sinne spricht das Streitpatent von
einer Summe quantisierter Koeffizienten, die bei einem geraden Zahlenwert mit dem
Wert „0“ des MVComp-Index und bei einem ungeraden Zahlenwert mit dem Wert
„1“ des MVComp-Index verknüpft wird (vgl. NK I, Absatz [0011], Spalte 3, Zeilen 9
bis 13).


Parität kann auch als eine Eigenschaft des das Vorzeichen codierenden Bits oder
Syntaxelements aufgefasst werden, gleich null (positives Vorzeichen) oder gleich
eins (negatives Vorzeichen) zu sein (vgl. NK I, z. B. Absatz [0037] - „Dans l´exemple
proposé, ladite convention est telle qu´un signe positif est associé à un bit de valeur
égale à zéro, tandis qu´un signe négatif est associé à un bit de valeur égale à un”).


Wie die Parität berechnet bzw. welche Funktion hierzu angewendet wird, legt
Merkmal M1.3 nicht fest. Ebenso wenig verlangt dieses Merkmal, dass durch
Auswertung der Funktion unmittelbar der Wert der Parität (also „0“ oder „1“) erhalten
wird. Vielmehr kann im Ablauf des Verfahrens auch eine andere Darstellung
verwendet werden, welche für die Parität steht bzw. diese repräsentiert.


5.1.3 Gemäß Merkmal M1.3.1 erfolgt das Berechnen des in Merkmal M1.3
genannten Funktionswertes unter der durch die Angabe „à l'exclusion dudit signe
soit    caché”   umschriebenen      Bedingung.     Laut    der    Übersetzung      des
Patentanspruchs 1 in der Streitpatentschrift soll darunter ein Berechnen zu
verstehen sein, welches unter Ausschluss des Vorzeichens erfolgt, das „verdeckt
ist“.

                                          - 52 -



a)    Es erscheint jedoch nicht sinnvoll, den Funktionswert aus Merkmal M1.3
anhand eines Vorzeichens zu berechnen, das bereits „verdeckt“ bzw. verborgen ist.


Denn der anspruchsgemäße Vorgang des Verbergens des Vorzeichens ist erst mit
Merkmal M1.5 abgeschlossen; die Berechnung des zuvor in Merkmal M1.3
genannten Funktionswerts ist gerade eine Voraussetzung hierfür. Dies ist auch
damit in Einklang, dass die Beschreibung des Streitpatents nur im Zusammenhang
mit dem Schritt der Entropiecodierung davon spricht, dass ein Vorzeichen
ausgeschlossen wird (vgl. NK I, Absätze [0038], [0039], [0047], [0048], [0061],
[0064],   [0100],     [0101],   [0111],   [0112],     [0128],   [0131]),    und   dieser
Entropiecodierungsschritt - bei ihm wird das verborgene Vorzeichen gerade nicht
codiert - erst nach den Schritten der Berechnung des Funktionswerts und der
Modifikation der Datenelemente ausgeführt wird (vgl. Figuren 1 und 3 - die Schritte
S3 und S5 bzw. C8 und C10 sind kein Bestandteil der Entropiecodierung, welche
erst in den Schritten S20 bzw. C20 erfolgt).


b)    Zwar könnte bei einem Vorzeichen, dessen Parität keine Modifikation der
Koeffizienten   zur    Folge    hat   (weil   diese   Parität   mit   der   Parität   der
Koeffizientensumme bereits übereinstimmt), davon gesprochen werden, dass das
Vorzeichen bereits bei der Berechnung des Funktionswerts „verborgen ist“ (vgl.
Merkmal M1.3). Gegen ein Verständnis von Merkmal M1.3.1, gemäß dem Merkmal
M1.3 lediglich auf den Ausschluss solcher Vorzeichen beschränkt ist, spricht
allerdings deutlich, dass die Merkmale M1.5/M1.6/M1.6.1 gerade den Fall des
Modifizierens miteinschließen.


c)    Daher ist - gerade auch im Hinblick auf den Gesamtzusammenhang der
streitpatentgemäßen Lehre - eine Interpretation des Subjonctif „soit caché“ in
Merkmal M1.3.1 sinnvoll, gemäß der der Funktionswert unter Ausschluss eines
Vorzeichens berechnet wird, das verborgen werden soll. Dieses Vorzeichen gehört
zu einem Datenelement aus der Menge vorzeichenbehafteter Datenelemente, auf

                                          - 53 -



die Merkmal M1.2.1 mit der Angabe „wenigstens ein Datenelement“ implizit Bezug
nimmt.


Ein derartiges Berechnen des Funktionswertes wird aus Sicht des Fachmanns z. B.
dann vorgenommen, wenn die Summe der Koeffizienten modulo 2 - d. h. die Parität
dieser Summe - berechnet wird und dabei nur der Betrag des verborgenen
Datenelements berücksichtigt wird, nicht aber dessen Vorzeichenbit. Dies ist
insbesondere      dann     der    Fall,   wenn      sämtliche     Vorzeichenbits      aller
vorzeichenbehafteten      Datenelemente       bei   der    Berechnung      der    Summe
weggelassen und nur die Beträge dieser Datenelemente addiert werden.


Denn dem Fachmann ist geläufig, dass die Parität einer Summe invariant
gegenüber Vorzeichenänderungen bei den einzelnen Summanden ist und daher
auch ohne die Werte eines oder mehrerer Vorzeichen der Summanden berechnet
werden kann. So ergibt sich beispielsweise für die in Absatz [0093] der
Streitpatentschrift genannte Liste SE1 = (+9, -7, 0, 0, +1, 0, -1, +2, 0, 0, +1)
unabhängig davon, ob die Datenelemente der Liste unter Ausschluss ihres
Vorzeichens aufsummiert werden oder nicht, für die Summe der Datenelemente
jeweils ein ungerader Wert (5 bei Einbeziehen des Vorzeichens, 21 bei Ausschluss
aller Vorzeichen, und beispielsweise 19 bzw. 7 bei Ausschluss des negativen
Vorzeichens des zweiten bzw. siebten Koeffizienten). Entsprechendes gilt für die
modifizierte Liste SEm1 = (+9, -6, 0, 0, +1, 0, -1, +2, 0, 0, +1), für die sich jeweils ein
gerader Summenwert ergibt.


Da nur von null verschiedene Koeffizienten ein Vorzeichen besitzen, das verborgen
werden kann, muss eine Vereinbarung zwischen Codierer und Decodierer darüber
bestehen, zu welchem (von null verschiedenen) Koeffizienten einer Partition ein zu
verbergendes Vorzeichen gehören soll.


d)     Entsprechendes gilt auch für Ausführungsformen, bei denen mindestens
zwei Vorzeichen codiert werden.

                                       - 54 -




Dabei ist festzuhalten, dass in der Parität einer Summe von Daten - also in einer
zweiwertigen Information - streng genommen nur genau ein Vorzeichen verborgen
werden kann, wenn ansonsten keine zusätzlichen Vereinbarungen getroffen
werden. Dies bedeutet somit, dass für alle Ausführungsbeispiele, die die
Übertragung mehrerer Vorzeichen betreffen (vgl. NK I, Absätze [0055] bis [0064],
[0119] bis [0131]), Anpassungen vorgenommen werden müssen. Das Streitpatent
schlägt in Hinblick auf das Verbergen mehrerer Vorzeichen die Verwendung der
Funktion „Summe der Datenelemente modulo 2N“ („la somme modulo 2N des
données“, vgl. NK I, Absätze [0061], [0128]) vor, deren Werte für N = 2 gemäß den
Absätzen [0059] und [0060] der Streitpatentschrift insgesamt vier verschiedene
Kombinationen zweier aufeinanderfolgender Vorzeichen zugeordnet sind. Weil die
möglichen Werte (0, 1, 2 und 3) dieser Funktion selbst die Eigenschaft haben, in
Übereinstimmung     mit   der   zugehörigen     Summenparität    geradzahlig    oder
ungeradzahlig zu sein, steht jeder einzelne Wert zugleich für die Parität der Summe
der Koeffizienten, so dass die Funktion die Parität repräsentiert. Insoweit ergibt es
durchaus Sinn, den mittels der Funktion „Summe der Datenelemente modulo 2N“
ermittelten Wert bzw. die sich daraus gemäß Vereinbarung ergebenden
Vorzeichenfolgen mit mehreren zu verbergenden digitalen Informationen bzw.
Vorzeichen zu vergleichen und gegebenenfalls mehrere Koeffizienten zu
modifizieren. Die Gesamtheit der Koeffizienten wird dann natürlich ohne die zu
verbergenden digitalen Informationen codiert.


5.1.4 Merkmal M1.4 verlangt, dass der in den Merkmalen M1.3/M1.3.1 berechnete
Funktionswert mit der Parität des in Merkmal M1.3.1 angesprochenen - zu
verbergenden - Vorzeichens verglichen wird. Ein solcher Vergleich wird z. B. dann
realisiert, wenn überprüft wird, ob der berechnete Funktionswert dem Vorzeichen
eines Elements einer Liste entspricht, die digitale Informationen enthält, die einer
Entropiecodierung unterzogen werden sollen (NK I, Figur 1 i. V. m. Absatz [0036] -
„… le module de traitement MTR_CO vérifie si la parité de la valeur du signe à
cacher correspond à la parité de la somme des données de la liste D1”).

                                        - 55 -



5.1.5 In Abhängigkeit vom Ergebnis dieses Vergleichs wird gemäß Merkmal M1.5
wenigstens eines der Datenelemente der aktuellen Partition modifiziert oder nicht
modifiziert.


a)     Eine Modifikation genau eines Datenelements wird in der Streitpatentschrift
in den Absätzen [0040] bis [0046] am Beispiel der Liste D1 und in den Absätzen
[0103] bis [0110] am Beispiel der Liste SE1=(+9, -7, 0, 0, +1, 0, -1, +2, 0, 0, +1)
erläutert. Die Modifikation wird dabei in Schritt S5 bzw. C10 vorgenommen.


Bei beiden Beispielen kann das modifizierte Datenelement ausgewählt werden,
indem zunächst +1 oder -1 zu jedem modifizierbaren Datenelement der Liste
hinzugefügt    und   anschließend    eine    dieser   Modifikationen   nach    einem
vorbestimmten Kriterium ausgewählt wird (NK I, Absätze [0044], [0105]). Dieses
kann ein „rate-distortion“-Kriterium sein (Absätze [0106], [0107]), welches
üblicherweise verwendet wird, um einen Ausgleich zwischen der Anzahl der pro
Zeiteinheit an den Decodierer übertragenen codierten Bits (d. h. der Bitrate) und der
aus der Modifikation resultierenden Bildverzerrung zu erzielen.


Im zweiten Beispiel soll das Vorzeichen des ersten von null verschiedenen
Elements der Liste SE1 verborgen werden, d. h. das (positive) Vorzeichen der Zahl
+9. Da die Summe der Listenelemente den Wert 5 und damit eine ungerade Parität
besitzt, das zu verbergende Vorzeichen aber positiv ist, wird das zweite von null
verschiedene Listenelement -7 durch Addition von +1 abgeändert, so dass sich der
modifizierte Wert -6 und eine modifizierte Liste SEm1=(+9, -6, 0, 0, +1, 0, -1, +2, 0,
0, +1) ergibt (vgl. NK I, Absätze [0107], [0108] - die dort angegebene Liste SEm1
enthält mit dem Wert „+6“ einen offensichtlichen Fehler). Die Summe der
Listenelemente ist jetzt gleich +6 und weist somit eine gerade Parität auf, die der
Parität des zu verbergenden positiven Vorzeichens entspricht.


Somit wird im zweiten Beispiel nicht der Koeffizient modifiziert, dessen Vorzeichen
verborgen werden soll; jedoch ergibt sich aus Absatz [0093] der Streitpatentschrift

                                         - 56 -



unmittelbar, dass jeder der aus elf Koeffizienten bestehenden Liste SE1
modifizierbar ist (siehe „la sous-liste SE1 obtenue est telle que SE1 = (9, -7, 0, 0, 1,
0, -1, 2, 0, 0, 1). En conséquence, onze coefficients modifiables sont obtenus […]“),
so dass eine „rate-distortion“-Optimierung auch zur Modifikation des ersten
Koeffizienten der Liste - und damit des ersten von null verschiedenen Koeffizienten
der zu codierenden aktuellen Partition - geführt haben könnte.


b)     Dass bei mehreren zu verbergenden Vorzeichen mehrere Koeffizienten
modifiziert werden müssen, ist für den Fachmann offensichtlich und ergibt sich auch
aus den Absätzen [0062] und [0129] der Streitpatentschrift (siehe „modification d'au
moins une donnée modifiable“, „modification d'au moins un coefficient modifiable“).


5.1.6 Im Fall des Modifizierens werden die Daten der Partition codiert, die das
wenigstens eine modifizierte Datenelement enthält (Merkmal M1.6). Bei der
Codierung handelt es sich üblicherweise um eine Entropiecodierung (vgl. NK I,
Figur 1, Schritt S20; Figur 3, Schritt C20).


5.1.7 Gemäß Merkmal M1.6.1 soll diese Codierung ohne das Vorzeichen des
wenigstens einen modifizierten Datenelements vorgenommen werden („codage […]
sans le signe de ladite au moins une donnée modifiée”). Das bedeutet, dass das
Datenelement, dessen Vorzeichen verborgen werden soll, mit dem Datenelement
zusammenfällt, welches modifiziert wird.


a)     Dieser im Streitpatent nicht ausdrücklich angesprochene Fall wird von den in
den Absätzen [0016] bis [0054] bzw. [0055] bis [0131] der NK I beschriebenen
Ausführungsformen der vorliegenden Erfindung erfasst.


So    kann     nach    Absatz     [0032]       das   Vorzeichen    eines     beliebigen
(vorzeichenbehafteten) Datenelements verborgen werden. Ferner ist es aus
fachmännischer Sicht selbstverständlich, dass die in Absatz [0044] beschriebene
Prüfung unterschiedlicher Modifikationen modifizierbarer Datenelemente für

                                       - 57 -



bestimmte Bildinhalte bzw. Partitionen ohne Weiteres ergeben kann, dass die
Modifikation desjenigen Datenelements am günstigsten ist, dessen Vorzeichen
verborgen werden soll, solange die Modifikation nicht zu Decodierungsfehlern führt.
Derartige Fehler können sich nach Absatz [0046] der Streitpatentschrift ergeben,
wenn eine Modifikation des ersten von null verschiedenen Datenelements dazu
führt, dass dieses den Wert null hat; in diesem Fall würde der Decodierer das
decodierte Vorzeichen nicht dem Datenelement zuweisen, dem es codiererseitig
zugeordnet ist.


Entsprechendes gilt auch für die in den Absätzen [0055] bis [0131] der NK I
beschriebene Ausführungsform. Zwar wird dort der zweite Koeffizient „-7“ modifiziert
und nicht der erste Koeffizient „+9“, dessen Vorzeichen verborgen werden soll (s. o.
sowie NK I, Absätze [0089], [0108], [0110]). Um das in Absatz [0106]
angesprochene „rate-distortion“-Kriterium anzuwenden und dadurch zur Auswahl
des zweiten Koeffizienten unter Berücksichtigung der mit verschiedenen
Modifikationen verbundenen Bitraten und Verzerrungen zu gelangen, müssen
Codiervorgänge durchgeführt werden, bei dem jeder modifizierbare Koeffizient
modifiziert (vgl. Absatz [0105] - „il est procédé à l'ajout de +1 ou -1 à chaque
coefficient modifiable“) und die zugehörige Partition anschließend codiert wird. Da
der erste von null verschiedene Koeffizient („+9“) nach Absatz [0093] ein
modifizierbarer Koeffizient ist, muss also auch dieser im Rahmen der „ratedistortion“-Optimierung modifiziert und die daraufhin erhaltene Partition codiert
werden.


b)    Gemäß dem vorstehend unter a) beschriebenen Vorgehen fällt der
Koeffizient, dessen Vorzeichen verborgen werden soll, nicht immer mit dem
modifizierten Koeffizienten zusammen, sondern nur für bestimmte Bildinhalte bzw.
Partitionen. Da Patentansprüche im Zweifel so auszulegen sind, dass sämtliche
Ausführungsbeispiele zu ihrer Ausfüllung herangezogen werden können (vgl. BGH,
Urteil vom 2. Juni 2015, X ZR 103/13 - Kreuzgestänge), verbleibt für die von der
Klägerin vertretene Auslegungsvariante, gemäß der Patentanspruch 1 vorgeben

                                           - 58 -



soll, dass das Datenelement, dessen Vorzeichen verborgen wird, für jede zu
codierende aktuelle Partition - also „stets“ - modifiziert werden muss, kein Raum.
Für diese Variante liefern die Beschreibung des Streitpatents wie auch die Figuren
keinerlei Anhaltspunkte.


c)      Der   Senat    interpretiert    Merkmal     M1.6.1    daher   derart,    dass    das
Datenelement, das modifiziert wird, von Fall zu Fall - also für bestimmte Partitionen
des in Merkmal M1.1 angesprochenen Bildes - mit dem vorab bestimmten
Datenelement zusammenfällt, dessen Vorzeichen verborgen werden soll, aber nicht
für jede beliebige Partition dieses Bildes mit diesem Datenelement identisch sein
muss.


Für diese Lesart spricht auch, dass der Wortlaut des erteilten Patentanspruchs 1
lediglich verlangt, dass das beanspruchte Codierverfahren zum Codieren eines in
Partitionen unterteilten Bildes geeignet sein soll (vgl. Merkmal M1.1), und dieses
Erfordernis bereits dann erfüllt ist, wenn die Verfahrensschritte der Merkmale
M1.2.3 bis M1.6.1 für eine einzige zu codierende Partition dieses Bildes mit Erfolg
ausgeführt werden können.


5.2     Zum erteilten Patentanspruch 2


Die Merkmale M2.1 bis M2.2.3 des auf eine Vorrichtung gerichteten erteilten
Patentanspruchs       2    unterscheiden     sich    im    Wesentlichen     durch       einen
Kategoriewechsel       von    den      Merkmalen    M1.1     bis   M1.2.3   des     erteilten
Patentanspruchs 1. Die weiteren Merkmale M2.3 bis M2.6 entsprechen den
Merkmalen M1.3 bis M1.6.1 (wobei in Merkmal M2.3.1 der in Merkmal M1.3.1
enthaltene    Zusatz      „soit   cache“   fehlt)   und    benennen    Mittel,    die    eine
Codiervorrichtung zur Realisierung des Codierverfahrens nach Patentanspruch 1
des Streitpatents besitzen muss.

                                       - 59 -



Die vorstehenden Ausführungen aus Abschnitt I.5.1 gelten für den Patentanspruch
2 des Streitpatents ebenfalls; insbesondere wird der Fachmann das in Merkmal
M2.3.1 angesprochene Vorzeichen als vorab bestimmtes, zu verbergendes
Vorzeichen ansehen. Denn auch die Merkmale M2.4 und M2.6 beziehen sich auf
dieses Vorzeichen und geben an, dass dieses vom Codieren ausgenommen bzw.
dessen Parität mit dem berechneten Wert verglichen werden soll.


5.3    Zu den erteilten Patentansprüchen 3 und 4


5.3.1 Der auf eine Vorrichtung zum Decodieren eines Datensignals gerichtete
erteilte Patentanspruch 4 benennt Mittel, die eine Decodiervorrichtung zur
Realisierung des Decodierverfahrens nach Patentanspruch 3 des Streitpatents
besitzen muss. Insoweit genügt es, sich mit dem Verfahrensanspruch 3
auseinanderzusetzen;     die    zugehörigen     Ausführungen     gelten    für   den
Vorrichtungsanspruch 4 entsprechend.


5.3.2 Das Verfahren zum Decodieren eines Datensignals nach Patentanspruch 3
soll laut den Merkmalen M3.1 bis M3.2.2 dadurch charakterisiert sein, dass das
Datensignal wenigstens ein in Partitionen unterteiltes Bild repräsentiert, das vorher
codiert worden ist, wobei eine zu decodierende aktuelle Partition Koeffizienten einer
direkten Transformation - also z. B. einer diskreten Kosinustransformation (s. o.,
Abschnitt I.5.1.1) - enthalten soll, von denen mindestens einer von null verschieden
ist.


Ferner soll das Decodierverfahren dadurch gekennzeichnet sein, dass es für die
aktuelle Partition die in den Merkmalen M3.3 bis M3.5.2 beschriebenen Schritte
umfasst (Merkmal M3.2.3).


Der erste dieser Schritte besteht darin, dass Daten(elemente) der aktuellen Partition
unter Ausschluss eines der in Merkmal M3.2.1 angesprochenen Vorzeichen
decodiert werden (Merkmal M3.3).

                                         - 60 -



Der Fachmann erkennt, dass dieses Vorzeichen ein verborgenes Vorzeichen sein
kann, welches nicht in Form eines Syntaxelements im Bitstrom übertragen worden
ist und daher in Schritt M3.3 nicht decodiert, sondern - wie in den Merkmalen M3.4
und M3.5 beschrieben - anhand eines Funktionswerts erhalten werden soll, der die
Parität der Summe der decodierten Daten(elemente) bzw. Koeffizienten
repräsentiert. Dabei soll das Vorzeichen positiv bzw. negativ sein, falls die Parität
der Summe der Daten(elemente) einen ersten bzw. zweiten Wert hat (Merkmale
M3.5.1, M3.5.2).


Zwar deutet die Fallunterscheidung der Merkmale M3.5.1 und M3.5.2, bei der
anhand der Summenparität der Daten(elemente) ein positives oder negatives
Vorzeichen zugewiesen wird, darauf hin, dass mit Patentanspruch 3 die
Decodierung genau eines verborgenen Vorzeichens beansprucht wird. Allerdings
hat auch dann, wenn die in Merkmal M3.4 genannte Funktion die „Summe der
Koeffizienten modulo 2N“ ist, so dass sich im Fall N = 2 die Funktionswerte 0, 1, 2
und 3 ergeben (was laut Absatz [0060] der NK I mit den Vorzeichenkombinationen
„+ +“, „+ -“, „- +“ und „- -“ korrespondiert), die Parität der Summe der Daten die Werte
0, 1, 0 und 1, welche den Funktionswerten 0, 1, 2 bzw. 3 entsprechen.
Dementsprechend ist der Wert des zweiten Vorzeichens einer solchen
Vorzeichenkombination bei Parität 0 positiv und bei Parität 1 negativ. Insofern
beschreibt Patentanspruch 3 auch einen Bestandteil eines Verfahrens zur
Rekonstruktion zumindest zweier verborgener Vorzeichen.


5.4    Zu den erteilten Patentansprüchen 5 und 6


Der erteilte Patentanspruch 5 bzw. der erteilte Patentanspruch 6 ist auf ein
Rechnerprogramm gerichtet, das Befehle enthält, um das Codierungsverfahren
nach Anspruch 1 bzw. das Decodierungsverfahren nach Anspruch 4 auszuführen.


Den Verweis auf Anspruch 4 in Patentanspruch 6 wertet der Senat als
offensichtlichen Fehler, denn nach der Logik der zu den Patentansprüchen 3, 4 und

                                      - 61 -



6 analog aufgebauten Patentansprüche 1, 2 und 5 ist hier eindeutig der Ausdruck
„nach Anspruch 3“ zu erwarten. Von diesem Verständnis des mit Patentanspruch 6
beanspruchten Gegenstands wird im Folgenden ausgegangen.




                                        II.


Das Streitpatent hat in der erteilten Fassung keinen Bestand, weil die jeweiligen
Gegenstände seiner unabhängigen Patentansprüche nicht patentfähig sind.




1.     Gemäß dem von der Klägerin genannten Stand der Technik war vor dem
Prioritätszeitpunkt des Streitpatents im Rahmen der Versuche, bekannte
Videocodierstandards wie H.264/AVC zu verbessern, bereits vorgeschlagen
worden, eine binäre Information (insbesondere ein Flag) zur Steuerung der
Codierung/Decodierung in den zu übertragenden Datenpaketen zu verbergen,
speziell als Parität einer Summe von Daten (siehe z. B. Druckschriften NK 1, NK 2).
Dazu musste ggf. ein Datenelement modifiziert werden, wobei versucht wurde, die
dabei entstehende Verzerrung zu minimieren. Keine der von der Klägerin zitierten
Druckschriften gibt jedoch explizit die Lehre, das Vorzeichen eines der zu
codierenden Transformationskoeffizienten zu verbergen und in Form einer Parität
einer Koeffizientensumme zu übertragen.


Mit Rücksicht auf den aus den angeführten Druckschriften bekannten Stand der
Technik ist der jeweilige Gegenstand der erteilten Patentansprüche 1 bis 6 sonach
neu.




2.     Ausgehend von Druckschrift NK 1, die mit Ausnahme der Merkmale M1.3.1,
und M1.6.1 sowie eines Teils von Merkmal M1.4 sämtliche Merkmale des erteilten

                                        - 62 -



Patentanspruchs 1 zeigt, beruht die Lehre des erteilten Patentanspruchs 1 jedoch
nicht auf einer erfinderischen Tätigkeit.


2.1    Die Druckschrift NK 1 geht von einem H.264/AVC-Hybrid-Videocodierer aus,
der Intra- und Inter-Prädiktion zur Codierung von Makroblöcken verwendet, um
räumliche und zeitliche Redundanzen auszunutzen. Dabei wird eine diskrete
Kosinustransformation auf Blöcke mit 4x4 oder 8x8 Pixeln angewendet, die jeweils
die Differenz zwischen einem Prädiktionsblock und einem aktuellen Makroblock
repräsentieren. Anschließend werden die aus der Differenzbildung resultierenden
Prädiktionsfehlerblöcke quantisiert und entropiecodiert. Auf diese Weise werden
Blöcke quantisierter DCT-Koeffizienten („QDCT Coefficients“) erhalten, welche
sowohl ein positives als auch ein negatives Vorzeichen besitzen können und denen
wiederum Konkurrenzindizes und Bewegungsvektoren zugeordnet sind. Alle diese
Größen werden entropiecodiert und im Bitstrom übertragen (vgl. NK 1, Figur 1
i. V. m. Seite 729, rechte Spalte, letzter Absatz bis Seite 730, linke Spalte, erster
Absatz - „The choice to encode a macroblock in Intra, Inter, or Skip, is nonnormative. […] for each Intra and Inter mode, the best predictor is selected and the
difference between the selected predictor and the current block is transformed with
a 4x4 or 8x8 discrete cosine transform (DCT), quantized and entropy coded. Luma
and chroma residuals are transmitted in this way“; Seite 730, linke Spalte, zweiter
Absatz - „A large part of this bitstream is composed of the competition indices, the
other information are the pixels and the motion vector residuals”; Seite 730, linke
Spalte, dritter Absatz - „Also context adaptive encoding is performed, so that indices
are efficiently encoded”).


Damit sind die Merkmale M1.1, M1.2, M1.2.1 und M1.2.2 in NK 1 offenbart.


NK 1 lehrt ferner, einen Bewegungsvektor-Index („MVComp index“) als 1-
bit-wertigen Parameter im Rahmen eines Data-Hiding-Verfahrens verborgen zu
übertragen (Seite 730, linke Spalte, vierter Absatz - „we propose to use data hiding
knowledge for decreasing the rate cost of these competition indices. In particular,

                                        - 63 -



we choose to deal with the motion information index generated by the MVComp tool
[4]“; Seite 732, rechte Spalte, Absatz IV.A, erster Satz).


Im Hinblick auf eine entsprechende Modifikation der quantisierten DCT-Koeffizienten wird unter den Abschnitten IV.A und IV.B auf Seite 733 beispielhaft
der k-te Block betrachtet. Dabei wird darauf hingewiesen, dass bei der Modifikation
ausschließlich die transformierten Koeffizienten des k-ten Blocks ungleich null
(an≠0) berücksichtigt werden sollen (Seite 733, linke Spalte, vorletzter Absatz - „We
consider N transform coefficients an, an≠0“). Einer dieser Koeffizienten wird dann
anhand eines „rate-distortion“-Kriteriums ausgewählt (Seite 733, rechte Spalte,
erster Absatz - „The problem is to select the modification couple (an, mj) which gives
the best RD compromise“) und entsprechend Gleichung (8) durch Addition einer
ungeraden Zahl mj modifiziert.


Um den MVComp-Index zu verbergen, berechnet der Codierer den Wert der
Funktion |Sk| mod 2 aus Gleichung (5) auf Seite 732; die Größe Sk ist laut Gleichung
(4) die Summe über sämtliche Koeffizienten an. Die Funktion |Sk| mod 2 kann die
Werte 0 und 1 annehmen und repräsentiert die Parität der Summe der
transformierten Koeffizienten der aktuellen Partition (s. auch Seite 732, rechte
Spalte, Abschnitt IV.A - „In order to meet these requirements, we propose to use the
parity of the coefficients sum to mark the MVComp index“).


Somit ist Merkmal M1.3 in Druckschrift NK 1 offenbart.


Der Codierer vergleicht anschließend den berechneten Funktionswert mit der
Parität des MVComp-Index i, der ebenfalls die Werte 0 oder 1, also „gerade Parität“
oder „ungerade Parität“ annehmen kann. In Abhängigkeit vom Ergebnis des
Vergleichs wird entschieden, ob einer der von null verschiedenen Koeffizienten
modifiziert werden muss, um die erforderliche Parität zu erhalten.


Vergleich und Modifikation gehen insbesondere aus Seite 732, rechte Spalte,

                                        - 64 -



Abschnitt IV.A, vorletzter Absatz (siehe Gleichung (5)) sowie aus Seite 733, linke
Spalte, Abschnitt IV.B (siehe Gleichungen (7) und (8)) der Druckschrift NK 1 hervor.


Mit dem Vergleich von berechnetem Funktionswert und Parität und der davon
abhängigen Entscheidung über die Modifikation ist das Merkmal M1.5 sowie ein Teil
von Merkmal M1.4 verwirklicht. Es verbleibt allerdings der Unterschied, dass in
Druckschrift NK 1 die Parität des MVComp-Index verglichen werden soll, nicht aber
die Parität des zu verbergenden Vorzeichens, wie es gemäß Merkmal M1.4 der Fall
sein soll.


Selbstverständlich werden im weiteren Verlauf des aus der Druckschrift NK 1
bekannten Codierverfahrens die transformierten Koeffizienten der Partition codiert,
und zwar zusammen mit dem modifizierten Koeffizienten (Merkmal M1.6). Dies
kommt auf Seite 730 i. V. m. Seite 735 der Druckschrift NK 1 direkt zum Ausdruck,
wonach die Entropiecodierung ohne den MVComp-Index erfolgt, der verborgen wird
und daher nicht zur Übertragung vorgesehen ist (Seite 730, linke Spalte, erster
Absatz - „[…] the difference between the selected predictor and the current block is
transformed […] quantized and entropy coded“; Seite 735, linke Spalte, Abschnitt
V.A., erster Absatz - „The 4x4 DCT transform is enabled and CABAC entropy coding
method, known to provide the best results, is selected […]“; Seite 735, rechte Spalte,
Abschnitt V.B., erster Absatz - „Fig. 4 gives the percentage of predictor index
transmitted and those which are not transmitted thanks to either the predictors
equality or the index hiding. […] we can note that the percentage of non-transmitted
index is higher than 30% and reaches 90% at high bitrate“).


Aus der NK 1 gehen allerdings der verbleibende Teil von Merkmal M1.4 sowie die
Merkmale M1.3.1 und M1.6.1 nicht unmittelbar hervor.


2.2    Mit dem verbleibenden Teil des Merkmals M1.4 - d. h. dem Umstand, dass
nicht der MVComp-Index, sondern ein Vorzeichen eines Koeffizienten verborgen
wird und dementsprechend in Merkmal M1.4 der berechnete Wert mit der Parität

                                        - 65 -



dieses Vorzeichens verglichen wird - kann ein Vorliegen erfinderischer Tätigkeit
nicht begründet werden.


So weist die Druckschrift NK 1 darauf hin, dass der Nutzen beim Verbergen der
vorgeschlagenen Information eher gering und die Auswahl des MVComp-Index
lediglich beispielhaft ist (Seite 731, linke Spalte, erster vollständiger Absatz - „The
most studied topic is to hide information in the nonzero DCT coefficients of a
compressed video stream“; Seite 731, rechte Spalte, letzter Absatz - „Hiding data in
pixels residuals …“; Seite 732, linke Spalte, Abschnitt III.B, erster Absatz - „As a
consequence, the data to be hidden can be all the competition information
generated for each macroblock …“; dritter Absatz - „According to these values, it is
already known that the overall gain of the proposed approach will remain low“).
Dementsprechend schlägt die Druckschrift NK 1 in Abschnitt VII vor, das
beschriebene Data-Hiding auch auf andere Konkurrenzindizes anzuwenden (Seite
740, rechte Spalte, siehe „The proposed method consequently appears as a nice
and efficient way to reduce the cost of other more costly competition indices while
taking care of the impact on the chroma component“). Gleichzeitig weist die
Druckschrift NK 1 an mehreren Stellen auf die Bedeutung einer verbesserten
Codierung für die transformierten Koeffizienten hin (Seite 733, linke Spalte, zweiter
Absatz - „It is important to notice that the proposed scheme has also the ability to
reduce the coding cost of the coefficients […]“; Seite 736, linke Spalte, zweiter
Absatz - „[…] it is important to notice that the proposed scheme has potentially a
double impact on the coding efficiency: first, the decrease of the coding cost due to
the index non-transmission, and second, the improvement of transform coefficients
coding   by   the   removal    of   useless      coefficients.”)   sowie   darauf,   dass
Bildinformationen in Pixelwerten verborgen werden können, die aus einer Wavelet-Transformation hervorgegangen sind (Seite 731, linke Spalte, dritter vollständiger
Absatz, siehe „The authors proposed to exploit data hiding to improve coding
efficiency by hiding the chrominance information in the wavelet domain of the
luminance component […]“).

                                        - 66 -



Damit gibt die Druckschrift NK 1 eine deutliche Anregung, das Verbergen von Daten
hinsichtlich verschiedener Aspekte weiter zu untersuchen, und zwar nicht nur für
Konkurrenzindizes, sondern gleichermaßen für die transformierten Koeffizienten.
Da der Fachmann stets bestrebt ist, die Codierkosten für die im Videodatenstrom
organisierten Informationen bei gleichbleibender Übertragungsqualität möglichst
gering zu halten, bot es sich für ihn an, insbesondere all diejenigen Informationen
auf eine Eignung für ein Data-Hiding zu überprüfen, die nicht effizient
entropiecodiert bzw. komprimiert werden können. Dass solche schlecht codierbaren
Informationen   in   Verbindung   mit   den      transformierten   Koeffizienten   zum
Prioritätszeitpunkt des Streitpatents dem Fachmann bekannt waren, wird u. a. durch
den Tagungsbeitrag NK 9 belegt.


Die dortigen Ausführungen zur arithmetischen Codierung bzw. CABAC-Systematik
geben wieder, dass auf die jeweiligen Vorzeichen der transformierten Koeffizienten
aufgrund ihrer gleichmäßigen Wahrscheinlichkeitsverteilung nur ein vereinfachtes,
unvollständiges Codierverfahren („Bypass“) angewendet werden kann (vgl. NK 9,
Seiten 195/196, siehe „NOTE“; Seite 183, Tabelle 9-46, letzte Zeile; Seiten 76/77,
Abschnitt 7.4.10, siehe „coeff_sign_flag[n]“), was mit Lehrbuchwissen aus der
Informationstheorie in Einklang steht, wonach eine willkürliche Information, deren
Auftrittswahrscheinlichkeit nahezu gleichverteilt ist, nicht effizient codiert bzw.
komprimiert werden kann (vgl. NK 8, Seite 227, erster Absatz).


Weiterhin untersucht die Druckschrift NK 1, welchen Einfluss das Verbergen eines
Konkurrenzindex auf die Bitrate hat („bitrate change“). In diesem Zusammenhang
wird auf Seite 732, Abschnitt IV.A der Druckschrift NK 1 unter Punkt 1) eine
Bedingung für die Anwendung des Data-Hiding formuliert, die die durch das Data-Hiding erzielte Änderung der Bitrate in Beziehung zu den Kosten der
Indexsignalisierung setzt, welche wiederum ein Maß für die Entropie bzw.
Gleichverteilung des betreffenden Index darstellen. Aus der Bedingung wird klar,
dass das Data-Hiding insbesondere dann problemlos angewendet werden kann,
wenn die Änderung der Bitrate gegenüber den Kosten der Indexsignalisierung klein

                                        - 67 -



bleibt, was ja bei hohen Signalisierungskosten häufig und leicht erfüllt ist. Der
Fachmann wird erkennen, dass sich infolgedessen gerade Syntaxelemente mit
hohen Codierkosten, wie z. B. Vorzeichen von Transformationskoeffizienten, dazu
eignen, in den Transformationskoeffizienten per Data-Hiding verborgen zu werden.


In Kenntnis der bekannten CABAC-Systematik lag es somit für den Fachmann auf
der Hand, mit Hilfe des in Druckschrift NK 1 beschriebenen Verfahrens anstelle
eines Konkurrenzindex die 1-bit-wertige Information betreffend das Vorzeichen
eines transformierten Koeffizienten zu verbergen, um auf diese Weise eine
unvollständige   arithmetische    Codierung      zu   umgehen   und   dadurch   die
Codiereffizienz deutlich zu steigern.


2.3   Auch Merkmal M1.3.1 kann eine erfinderische Tätigkeit nicht stützen.


2.3.1 So ist dieses Merkmal bei der Prüfung der Patentfähigkeit des Gegenstands
des erteilten Patentanspruchs 1 außer Acht zu lassen (BGH, Urteil vom 17. Februar
2015 - X ZR 161/12 – Wundbehandlungsvorrichtung, juris), da aus diesem nicht
ursprungsoffenbarten Merkmal – das zwar lediglich zu einer Beschränkung des
Schutzgegenstands und nicht zu einem Aliud führt – keine Rechte hergeleitet
werden können (vgl. BGH, Beschluss vom 5. Oktober 2000 – X ZR 184/98 -
Zeittelegramm, Rn. 48 - 52, juris; BGH, Beschluss vom 21. Oktober 2010 – Xa ZB
14/09 – Winkelmesseinrichtung, Rn. 11 – 24, juris).


a)    Das Merkmal M1.3.1 ist der ursprünglichen Offenbarung (Anlage NK IV) nicht
unmittelbar und eindeutig als zur Erfindung gehörend zu entnehmen.


So enthält diese Druckschrift in Anspruch 1 in den Zeilen 9/10 zwar das Merkmal
„calcul (S3) de la valeur d'une fonction représentative des données de ladite
partition courante à l' exclusion dudit signe“, aber das demgemäß ausgeschlossene
Datenelement ist irgendeines der in den Zeilen 5/6 dieses Anspruchs 1 genannten
Vorzeichen. Ferner ergibt sich aus den letzten beiden Spiegelstrichen des

                                         - 68 -



Anspruchs 1 nur, dass ein modifiziertes Datenelement codiert wird; dies muss nicht
das Datenelement mit dem zu verbergenden Vorzeichen sein.


Des Weiteren kommt die Formulierung „à l'exclusion du signe“ oder „à l'exception
du signe“ in der Beschreibung nur in Verbindung mit dem Codieren (oder
Decodieren) der aktuellen Partition vor (vgl. NK IV, z.B. Seite 13, Zeile 12 bis 18
sowie Seite 20, Zeile 21 bis 30). Wenn die Berechnung des Funktionswertes als Teil
einer Entropiecodierung angesehen werden könnte, hätte ein Ausschluss eines
Vorzeichens bei der Entropiecodierung zwangsläufig zur Folge, dass das
Vorzeichen nicht bei der Berechnung des Funktionswertes verwendet werden kann.
Eine derartige Interpretation steht allerdings im Widerspruch zur Beschreibung und
den Figuren (vgl. NK IV, Seite 11, Zeile 12 bis 30 und Seite 20, Zeile 7 bis Seite 22,
Zeile 17 sowie Figuren 1 und 3 - dort folgt die Entropiecodierung in Schritt S20 bzw.
C20 nach der Berechnung des Funktionswertes in Schritt S3 bzw. C8). Somit kann
Merkmal M1.3.1 nicht aus denjenigen Beschreibungsstellen abgeleitet werden, die
auf einen Ausschluss eines Vorzeichens beim Codieren bzw. Decodieren Bezug
nehmen.


Ferner geht aus dem auf Seite 21, Zeilen 11 bis 20 beschriebenen
Ausführungsbeispiel gerade hervor, dass die Vorzeichen der Elemente der Liste
SE1 in die Berechnung des Summenwerts 5 mit einbezogen werden (vgl. auch Seite
31, Zeilen 10 bis 13 für den Fall der decodiererseitigen Summenberechnung).


Auch anderweitig geht aus NK IV nicht unmittelbar und eindeutig hervor, dass das
zu   verbergende    Vorzeichen     bei   der      Berechnung   des   Funktionswertes
ausgeschlossen sein soll.


b)    Das Merkmal M1.3.1 konkretisiert die mit Merkmal M1.3 beanspruchte
Berechnung des Funktionswerts dahingehend, dass dazu das Vorzeichen des zu
verbergenden Datenelements ausgeschlossen werden soll; damit scheiden andere
Möglichkeiten aus, bei denen das Vorzeichen in die Berechnung des

                                       - 69 -



Funktionswerts mit einbezogen wird. Sonach liegt eine Einschränkung des
angemeldeten Gegenstands vor (vgl. BGH, Wundbehandlungsvorrichtung, a. a. O.,
Rn. 53), aus der keine Rechte hergeleitet werden können (vgl. BGH, Urteil vom
21. Juni 2011 – X ZR 43/09 – Integrationselement, Rn. 26 – 29, juris).


c)    Die Beklagte argumentiert sinngemäß, es sei klar, dass die Summenparität
auf der Decoderseite bestimmt wird, ohne das verborgene Vorzeichen zu
berücksichtigen; daher sei davon auszugehen, dass auch auf der Encoderseite so
vorgegangen werde. Ferner gebe Merkmal M1.3.1 nicht an, wie die Berechnung
des Funktionswerts - der ja unabhängig von dem Vorzeichen des verborgenen (oder
irgendeines anderen) Koeffizienten sei - vorzunehmen sei. In jedem Fall werde nach
Merkmal M1.3.1 und der Ursprungsanmeldung die Berechnung desselben Werts
verlangt.


Dem folgt der Senat nicht.


Denn dem Codierer liegt das verborgene Vorzeichen vor, so dass es grundsätzlich
mehrere Möglichkeiten gibt, die Summenparität zu berechnen - nämlich unter
Verwendung von keinem, einem einzigen, mehreren oder allen Vorzeichen der
vorzeichenbehafteten Koeffizienten. Bereits aus diesem Grund kann nicht
unmittelbar von der Decodiererseite auf die Codiererseite geschlossen werden.
Auch das Argument, mit Merkmal M1.3.1 und in NK IV werde derselbe Wert
berechnet, steht dem nicht entgegen. Abgesehen davon gibt das Merkmal M1.3.1
durchaus an, wie die in Merkmal M1.3 angesprochene Berechnung vorzunehmen
ist - nämlich gerade unter Ausschluss des Vorzeichens, das verborgen werden soll.


2.3.2 Selbst wenn das Merkmal M1.3.1 bei der Prüfung der erfinderischen Tätigkeit
berücksichtigt würde, könnte es eine erfinderische Tätigkeit nicht tragen.


Denn für den Fachmann ist es selbstverständlich, dass die Vorzeichenbits der
Koeffizienten an zur Bestimmung des Werts der Funktion |Sk| nicht erforderlich sind

                                            - 70 -



und deren Berücksichtigung nur zusätzlichen Rechenaufwand erfordert, ohne etwas
am Rechenergebnis - dem Betrag der Summe der Koeffizienten an - oder dessen
Parität zu ändern. Der Fachmann wird somit die Vorzeichenbits der Koeffizienten an
bei der Berechnung der Funktion |Sk| nicht verwenden, um den hierfür erforderlichen
Rechenaufwand gering zu halten.


2.4    Schließlich realisiert der Fachmann das verbleibende Merkmal M1.6.1
bereits dann, wenn er die aus der Druckschrift NK 1 bekannte Lehre - wie oben in
Abschnitt   II.2.2   ausgeführt   -   auf     das    Verbergen   der   Vorzeichen    von
Transformationskoeffizienten anwendet und dabei typische Videoinhalte codiert.
Letzteres ist eine Selbstverständlichkeit ohne erfinderischen Gehalt.


In diesem Fall muss er den Koeffizienten, dessen Vorzeichen verborgen werden
soll, für jeden Block vorab festlegen. Es ist dann selbstverständlich, dass der von
dem „rate distortion“-Optimierungsalgorithmus der NK 1 zur Modifikation
ausgewählte Koeffizient an (vgl. Abschnitt IV.B - „The problem is to select the
modification couple (an, mj) which gives the best RD compromise“) bei bestimmten
zu codierenden Blöcken - also von Fall zu Fall - mit dem vorab festgelegten
Koeffizienten zusammenfällt, dessen Vorzeichen verborgen werden soll.


Dies ist insbesondere dann gegeben, wenn ein aktuell zu codierender Block einen
DC-Koeffizienten gleich null sowie genau einen von null verschiedenen AC-Koeffizienten besitzt, der nicht zu null modifiziert wird (Modifikationen zu null sind in
diesem Fall ausgeschlossen, vgl. NK 1, Seite 733, linke Spalte, erster Absatz - „For
the blocks which only contain one non-null coefficient, this coefficient cannot be
changed to zero in order to avoid the transmission of only zeroes coefficients which
will induce decoding error […] if […] an index is hidden by the modification […] of
the unique non-null transform coefficient to zero, this block will not be considered as
a block with hidden index at the decoder because no transform coefficient will be
available“), oder auch dann, wenn ein Block genau zwei von null verschiedene
Koeffizienten umfasst, da es in diesem Fall sehr häufig vorkommt, dass der von

                                       - 71 -



dem Optimierungsalgorithmus zur Modifikation ausgewählte Koeffizient auch
derjenige ist, dessen Vorzeichen verborgen werden soll. Denn andernfalls würde
der Algorithmus immer nur den anderen Koeffizienten auswählen, dessen
Vorzeichen nicht verborgen werden soll, was für typische, zeitlich variable
Bildinhalte äußerst unwahrscheinlich ist. Entsprechendes gilt auch für aktuelle
Partitionen mit genau drei oder vier von null verschiedenen Koeffizienten.


2.5   Die Beklagte trägt vor, dass die Wahl eines Vorzeichens als zu verbergende
Information nicht naheliegend sei. Ihre Ausführungen halten jedoch einer näheren
Überprüfung nicht stand. Im Einzelnen:


2.5.1 Nach Auffassung der Beklagten weise die Druckschrift NK 1 nicht auf die
Bedeutung einer verbesserten Codierung für die Transformationskoeffizienten hin.
Eine derartige Folgerung beruhe - ähnlich wie bei dem der BGH-Entscheidung
„Energieversorgungssystem“ (Urteil       vom 4.   August 2020, X ZR 40/18)
zugrundeliegenden Fall - bestenfalls auf einer analysierenden Betrachtungsweise
von Textstellen, die in eine Abstraktion oder sogar in eine Umdeutung der dort
angesprochenen     konkreten   Sachverhalte     münde    und   funktionelle   Details
ausblende; vorliegend fehle insbesondere auch ein Anlass, auf grundlegende
Funktionsprinzipien        zurückzugreifen.        Die         Bedeutung         der
Transformationskoeffizienten ergebe sich lediglich aus der Veränderung ihres
Werts und lasse sich auch nicht durch einen allgemeinen Wunsch des Fachmanns
nach einer Erhöhung der Codiereffizienz rechtfertigen. Allenfalls würde der
Fachmann ausgehend von der Druckschrift NK 1 prüfen, ob es andere
Konkurrenzindizes gebe, die besser als der MVComp-Index zum Verbergen
geeignet seien. Auch in der vom Senat zitierten Passage auf Seite 740 gehe es nur
um Konkurrenzindizes.


Diese Einwände greifen nicht durch.

                                          - 72 -



So ist zunächst anzumerken, dass Verfahren zur Codierung von Bildinformationen,
die von den gängigen Standards ausgehen, immer eine effiziente und gleichzeitig
möglichst verlustfreie Codierung der Bildinformationen im Blick haben. Im Verfahren
der   Druckschrift   NK 1    sind   die     zu     codierenden   Bildinformationen   die
Transformationskoeffizienten; ihre Codierung steht daher naturgemäß im Fokus des
fachmännischen Interesses. Die Feststellungen, dass das von der Druckschrift
NK 1 vorgeschlagene Verfahren die zur Codierung der Koeffizienten erforderlichen
Codierkosten reduziert, indem Reihen nebeneinanderliegender Nullen erzeugt
werden (vgl. NK 1, Seite 733, linke Spalte, zweiter Absatz) und unnützen
Koeffizienten der Wert null zugewiesen wird (vgl. NK 1, Seite 736, linke Spalte,
zweiter Absatz), bringen dies klar und deutlich zum Ausdruck, indem sie auf die
Vorteile einer effizienten Codierung der Transformationskoeffizienten hinweisen
und damit dem Fachmann deren Wichtigkeit vor Augen führen.


Diese Erkenntnis schließt der Fachmann in seine Überlegungen zur Verbesserung
der Lehre der Druckschrift NK 1 mit ein. Dies gilt gleichermaßen für den - durchaus
relevanten - Hinweis „The proposed method consequently appears as a nice and
efficient way to reduce the cost of other more costly competition indices while taking
care of the impact on the chroma component“ auf Seite 740 der Druckschrift NK 1,
welcher es aufgrund der darin enthaltenen Verallgemeinerung auf das Verbergen
von aufwändiger zu codierenden Konkurrenzindizes dem Fachmann nahebringt,
andere, ebenfalls aufwändig zu codierende 1-bit-wertige Informationen für ein Data-Hiding in Betracht zu ziehen, ohne hierbei drastische Verschlechterungen der
Chroma-Komponenten in Kauf nehmen zu müssen.


Im Übrigen können die Ausführungen im zweiten und dritten Absatz der rechten
Spalte auf Seite 729 (siehe „The scheme proposed in this article is independent of
the characteristics of the competition information: we use data hiding in order to
transmit competition indices“) als (weitere) Anregung angesehen werden, mit dem
Data-Hiding-Verfahren der Druckschrift NK 1 nicht nur Konkurrenzindizes zu
verbergen. Denn mit diesen Ausführungen kommt klar zum Ausdruck, dass das

                                             - 73 -



Data-Hiding unabhängig von den Eigenschaften von Konkurrenzinformationen ist,
so dass sich der Gedanke aufdrängt, ob das von NK 1 vorgeschlagene Schema
auch „derart unabhängig“ von den Konkurrenzinformationen ist, dass es zum
Verbergen weiterer Informationen genutzt werden kann. Vor diesem Hintergrund
lässt sich der Teilsatz „we use data hiding in order to transmit competition indices“
im Sinne von „obwohl das in der vorliegenden Veröffentlichung beschriebene
Verfahren eine Codierung weiterer Informationen erlaubt, wird im vorliegenden
Artikel die Codierung von Konkurrenzindizes beschrieben“ verstehen.


2.5.2 Die        Beklagte    argumentiert,     die    Wahl     des   Vorzeichens   eines
Transformationskoeffizienten sei nicht die einzig sinnvolle Wahl im H.265-Standard.
Wenn der Fachmann vor die Aufgabe gestellt wäre, die Lehre der Druckschrift NK 1
auf den H.265/HEVC-Standard anzuwenden, würde er einen der dort vorgesehenen
Konkurrenzindizes - etwa den in NK 2 als optimale Wahl für das Data-Hiding
angesehenen - Most-Probable-Mode-Index („MPM-Index“) - innerhalb der
Transformationskoeffizienten übertragen.


Dieses Argument ändert aber nichts daran, dass der Fachmann Anlass hatte, all
diejenigen Informationen auf eine Eignung für ein Data-Hiding hin zu überprüfen,
die nicht effizient entropiecodiert bzw. komprimiert werden können. Er hätte daher
ausgehend von der Druckschrift NK 1 gerade auch das Vorzeichen eines
Koeffizienten in diesem Sinne überprüft und wäre unmittelbar zum Schluss
gekommen, dass ein solches Vorzeichen nicht effizient entropiecodiert werden
kann,     weil    positive   und   negative     quantisierte   DCT-Koeffizienten   gleich
wahrscheinlich sind. Dass der Fachmann möglicherweise auch den MPM-Index
verborgen hätte, steht dem nicht entgegen (vgl. BGH, Urteil vom 8. Juni 2021, X ZR
69/19, Rn. 35, mit Hinweis auf BGH, Urteil vom 16. Februar 2016, X ZR 5/14 -
Anrufroutingverfahren, Rn. 36 - „Kommen für den Fachmann zur Lösung eines
Problems mehrere Alternativen in Betracht, können mehrere von ihnen naheliegend
sein“).

                                               - 74 -



2.5.3 Ferner führt die Beklagte aus, Druckschrift NK 1 lege nicht nahe,
Bildinformation in Pixeldaten zu verbergen.


Dies     gelte   insbesondere         für    den   Hinweis    auf     das      Verbergen       von
Chrominanzinformationen durch die Autoren des von der Beklagten als ES5 ins
Verfahren eingeführten Referenzdokuments [16] (vgl. NK 1, Seite 731, linke Spalte,
Abschnitt II.B, Punkt 2)). Auch betone der erste Absatz in Abschnitt III.B der NK 1,
dass zwischen dem in der Druckschrift NK 1 vorgeschlagenen Verfahren und den
aus den Referenzdokumenten [16] und [17] vorbekannten Verfahren erhebliche
Unterschiede bestehen und dass es beim in dem Absatz angesprochenen
Verbergen von Chrominanzkomponenten in der Luminanzkomponente nicht darum
gehe, eine einzelne binäre Information in einem Datenblock zu verbergen, sondern
ein mehrwertiges Informationssignal.


Auch diese Argumente führen zu keiner anderen Beurteilung.


Nach Auffassung des Senats entnimmt der Fachmann dem ersten Absatz in
Abschnitt III.B der Druckschrift NK 1 i. V. m. dem allgemein Data-Hiding-Verfahren
betreffenden     Abschnitt     II.B     insbesondere,     dass      auf     dem    Gebiet      der
Videokompression grundsätzlich beliebige Daten verborgen werden können („data
hiding for video compression“), und zwar insbesondere Chrominanzkomponenten
(d. h.    Bildinformationen)     in         Luminanzkomponenten           (d. h.   in     anderen
Bildinformationen, siehe „chrominance […] components are hidden in luminance
components       before   compression“).           Da   sowohl      Chrominanz-         als   auch
Luminanzkomponenten          gemäß           den   gängigen      Videocodierstandards          als
vorzeichenbehaftete DCT-Koeffizienten codiert werden, liegt der Schluss nahe,
dass vorzeichenbehaftete DCT-Koeffizienten in anderen DCT-Koeffizienten
verborgen werden können. Die zitierten Textstellen sind somit ein weiteres Indiz
dafür, auch die Vorzeichen selbst in DCT-Koeffizienten zu verbergen. Dass sich die
aus den Dokumenten [16] und [17] bekannten Verfahren von dem aus der

                                          - 75 -



Druckschrift NK 1 bekannten Verfahren unterscheiden, steht dieser Erkenntnis nicht
entgegen.


2.5.4 Weiterhin vertritt die Beklagte die Auffassung, das Ziel des Data-Hiding liege
zudem nicht darin, ein bestimmtes Datenelement möglichst effizient zu übertragen,
sondern darin, die Gesamtdatenmenge bzw. -rate zu reduzieren. Daher wähle die
Fachperson für das Data-Hiding grundsätzlich ein Datenelement, das einen
möglichst großen Anteil am Gesamtdatenvolumen habe. Dass der gemäß
Druckschrift NK 1 verborgene MVComp-Index oftmals nur für einen Teil der
codierten Partitionen bestimmt werde, spreche im Hinblick auf die Auswahl eines
Datenelements für das Data-Hiding gerade für eine erfinderische Tätigkeit, da
grundsätzlich jede codierte Partition ein Vorzeichen enthalte, das verborgen
übertragen werden könne, dies aber gerade nicht aus dem Stand der Technik
bekannt      gewesen       sei.    Während         die   Druckschrift     NK      1    die
Transformationskoeffizienten nur als „Trägermaterial“ betrachte, nehme das
Streitpatent eine grundlegend andere Perspektive ein, indem es das Trägermaterial
zum verborgenen Gegenstand mache.


Auch diesem Vorbringen kann nicht zugestimmt werden.


So weiß der Fachmann, dass die Vorzeichen - ebenso wie der MVComp-Index -
getrennt von den Beträgen der Koeffizienten als separate zweiwertige Flags
gespeichert und verarbeitet werden (vgl. NK 9, Abschnitt 7.4.10, siehe
„coeff_sign_flag[n]“), und dass jeder Block mindestens ein Vorzeichen enthält, das
gleichverteilt auftritt (s. o., Abschnitt II.2.2). Daher ist ihm klar, dass ein Vorzeichen-Flag zum Verbergen sogar besser geeignet ist als der MVComp-Index. Dies spricht
nach Überzeugung des Senats ausgehend von Druckschrift NK 1 nicht für, sondern
vielmehr gegen eine erfinderische Tätigkeit.


2.5.5 Die Beklagte weist darauf hin, die Textstellen auf Seite 733 und 736 der
Druckschrift NK 1 (dort jeweils linke Spalte, zweiter Absatz) bezögen sich nur auf

                                           - 76 -



Vorteile,   die   sich     ergeben       würden,    weil    die     Summenparität   der
Transformationskoeffizienten - zusätzlich zu einer Dateneinsparung durch das
Verbergen des MVComp-Index - durch spezielle Modifikationen (Additionen von -5,
- 3, -1, 1, 3 oder 5) der Koeffizienten an den Wert des zu verbergenden MVComp-Index angepasst werde, so dass insbesondere Koeffizienten zu null modifiziert
würden. Eine Anregung, insoweit nach Verbesserungen bei der Übertragung der
Transformationskoeffizienten zu suchen, ergebe sich nicht. Es erscheine
unzutreffend, das Verfahren hinsichtlich der Codierung von Koeffizienten und der
Einsparung durch die Nicht-Übertragung des verdeckten Bits unter zwei
voneinander unabhängigen Aspekten zu betrachten.


Dass die Dateneinsparung durch das verdeckte Übertragen des MVComp-Index
gering sei, da dessen Anteil an der Gesamtübertragung mit 2% gering sei und dies
ganz allgemein für Konkurrenzindizes gelte, entspreche nicht der Offenbarung der
Druckschrift NK 1; diese beziehe laut Seite 740, linke Spalte den Nachteil des
geringen Anteils am gesamten Datenvolumen lediglich auf den MVComp-Index und
schlage insoweit nur vor, stattdessen andere Konkurrenzindizes verdeckt zu
übertragen, die mit höheren Codierungskosten verbunden seien.


Auch diese Argumente greifen nicht durch.


Der Fachmann ist nämlich stets bestrebt, die Codierkosten für die im
Videodatenstrom          organisierten      Informationen         bei   gleichbleibender
Übertragungsqualität möglichst gering zu halten. Vor diesem Hintergrund weisen
die von der Beklagten genannten Textstellen den Fachmann darauf hin, dass der
Verbesserung der Codierung der Transformationskoeffizienten eine besondere
Bedeutung zukommt (s. o.). Dem Fachmann ist klar, dass diese Verbesserung beim
aus der Druckschrift NK 1 bekannten Verfahren sowohl darauf zurückzuführen ist,
dass mit dem MVComp-Index eine 1-bit-wertige Information verborgen wird, als
auch darauf, dass die Werte +1/-1, +3/-3 und +5/-5 zu den Koeffizienten addiert
werden. Der letztgenannte Umstand ändert aber nichts daran, dass sich durch das

                                              - 77 -



Verbergen     von      Vorzeichen   anstelle       des    MVComp-Index       noch      größere
Einsparungen erreichen lassen.


2.5.6 Ferner führt die Beklagte aus, das in der Druckschrift NK 1 beschriebene
Verfahren führe im Hinblick auf die Codierung der Transformationskoeffizienten
bereits zu Verbesserungen, ohne dass Modifikationen des Verfahrens erforderlich
wären. Die damit verbundenen Dateneinsparungen beträfen sämtliche Bestandteile
der Transformationskoeffizienten, aufgrund der in der Druckschrift NK 1
angestrebten Modifikation von Koeffizienten zu null auch einschließlich ihrer
Vorzeichen.      Der    Umstand,    dass       sich    das   Vorzeichenbit     nicht   effizient
entropiecodieren lasse, bestätige dem Fachmann nur die in der Druckschrift NK 1
genannten Vorteile geeignet gewählter Modifikationen und bilde eine zusätzliche
Motivation, solche Modifikationen vorzunehmen.


Auch diese Ausführungen können nicht überzeugen.


Denn dass im Verfahren der Druckschrift NK 1 Koeffizienten zu null modifiziert
werden können und sich dadurch Einsparungen ergeben, ändert nichts daran, dass
der   Fachmann         ausgehend        von     Druckschrift    NK     1     nach      weiteren
Einsparmöglichkeiten Ausschau hält. Das Verbergen eines Vorzeichens eines
Koeffizienten stellt gerade eine solche weitere Möglichkeit dar.


2.5.7 Außerdem spreche es nach Ansicht der Beklagten für das Vorliegen einer
erfinderischen      Tätigkeit,   dass    für     das     Data-Hiding   eines     Vorzeichens
Schwierigkeiten zu überwinden seien, die beim Verbergen eines gesonderten
Parameters nicht aufträten. So müsse ein Transformationskoeffizient bestimmt
werden, dessen Vorzeichen verborgen werde, und es müsse verhindert werden,
dass es zu einer Desynchronisierung zwischen Codierer und Decodierer komme.


Diese Schwierigkeiten bestehen nach Überzeugung des Senats nicht.

                                        - 78 -



Selbstverständlich wird der Fachmann nur solche Datenelemente verbergen, die
sonst im Bitstrom übermittelt werden müssten. Damit bieten sich die im Bitstrom zu
übermittelnden Vorzeichen der von null verschiedenen Koeffizienten für ein Data-Hiding an, welche ja separat von den Koeffizienten im Bitstrom übermittelt werden
(vgl. das in NK 9 angesprochene „coeff_sign_flag[n]“).


Zudem war dem Fachmann eine Desynchronisation als mögliche Fehlerquelle im
Zusammenhang mit dem Verbergen eines Konkurrenzindex selbstverständlich
bekannt, genauso wie die Vermeidung bestimmter Modifikationen zu ihrer
Behebung. Denn auch die Druckschrift NK 1 lehrt Regeln, die Änderungen an den
Transformationskoeffizienten zu beschränken. So wird darauf hingewiesen, dass
ein Koeffizient nicht zu null geändert werden kann, wenn der Block nur diesen einen
von null verschiedenen Koeffizienten enthält (vgl. NK 1, Seite 733, linke Spalte,
erster Absatz - „For the blocks which only contain one non-null coefficient, this
coefficient cannot be changed to zero in order to avoid the transmission of only
zeroes coefficients which will induce decoding error: […] As a result, a wrong parsing
will be performed to read the index.”). Für den Fachmann war es selbstverständlich,
ausgehend von der Druckschrift NK 1 die dort offenbarten Regeln zur Vermeidung
von Desynchronisation auf das Verbergen eines Vorzeichens eines Koeffizienten
zu übertragen und zu gewährleisten, dass der Codierer nur solche Partitionen
ausgibt, aus denen der Decodierer ein verborgenes Vorzeichen fehlerfrei
rekonstruieren kann.


2.6   Nach allem beruht der Gegenstand des erteilten Patentanspruchs 1 nicht auf
einer erfinderischen Tätigkeit.




3.    Der erteilte Patentanspruch 2 kann nicht günstiger beurteilt werden. Er betrifft
eine Vorrichtung, die ausschließlich durch Mittel charakterisiert wird, die
zwangsläufig verwendet werden müssen, um das Codierverfahren nach dem
erteilten Patentanspruch 1 zu realisieren.

                                        - 79 -



Für den erteilten Patentanspruch 2 gilt daher die Argumentation zum erteilten
Patentanspruch 1 in gleicher Weise, so dass der Gegenstand des erteilten
Patentanspruchs 2 ebenfalls nicht auf erfinderischer Tätigkeit beruht.


Entsprechendes gilt für den Gegenstand des erteilten Patentanspruchs 5. Dieser
betrifft ein Rechnerprogramm, das Befehle enthält, um das Codierverfahren nach
dem erteilten Patentanspruch 1 bei Ausführung auf einem Rechner auszuführen.
Dass ein derartiges Rechnerprogramm erforderlich ist, um mit dem aus Druckschrift
NK 1 bekannten Verfahren Vorzeichen von Transformationskoeffizienten zu
verbergen, ist selbstverständlich und geht auch aus dieser Druckschrift hervor (vgl.
NK 1, Seite 735, linke Spalte, Abschnitt V.A., erster Satz).




4.    Auch der Gegenstand des auf ein Decodierverfahren gerichteten erteilten
Patentanspruchs 3 beruht nicht auf erfinderischer Tätigkeit.


Dieser Patentanspruch korrespondiert in seinem Oberbegriff (Merkmale M3.1 bis
M3.2.2) mit den Merkmalen M1.1 bis M1.2.2. Zur Vermeidung von Wiederholungen
sei an dieser Stelle zunächst auf die diesbezüglichen Ausführungen in Abschnitt
II.2.1 hingewiesen.


Darüber hinaus lehrt die Druckschrift NK 1, dass der Wert des MVComp-Index, d. h.
der Wert der verborgenen Information, für jede Makroblock-Partition aus der Parität
der Summe der decodierten transformierten Koeffizienten wiederhergestellt wird
(vgl. Seite 735, linke Spalte, erster vollständiger Absatz - „The decoding only needs
to compute the coefficients sum and its modulo for each macroblock partition with
non-null transform coefficients“ i. V. m. Gleichung (6) auf Seite 733). Dieser
rekonstruierte Wert kann entweder 0 oder 1 sein. Damit sind die Merkmale M3.2.3
(für sich genommen) und M3.4 aus der Druckschrift NK 1 bekannt, und zudem geht
aus ihr auch das Erhalten der beiden möglichen Werte des MVComp-Index anhand
zweier Werte der Koeffizientensumme hervor. Diese Maßnahme betrifft zwar nicht

                                       - 80 -



die Rekonstruktion der beiden möglichen Werte eines verborgenen Vorzeichens,
stimmt jedoch in ihrer algorithmischen Struktur mit den Merkmalen M3.5, M3.5.1
und M3.5.2 exakt überein.


Zudem ist es selbstverständlich, dass die Beträge der Transformationskoeffizienten
und ggf. weitere nicht verborgene Vorzeichen an den Decodierer übertragen und
dort unter Ausschluss des verborgenen Vorzeichens entropiedecodiert werden
(Merkmal M3.3).


Von der Lehre der Druckschrift NK 1 unterscheidet sich die Lehre des erteilten
Patentanspruchs 3 somit nur dadurch, dass anstelle eines Konkurrenzindex das
Vorzeichen eines transformierten Koeffizienten rekonstruiert wird (vgl. Merkmale
M3.5, M3.5.1, M3.5.2). Dass dies nahegelegen hat, ergibt sich aber aus den
Ausführungen zu Merkmal M1.4 aus Abschnitt II.2.




5.    Der erteilte Patentanspruch 4 betrifft eine Vorrichtung, die ausschließlich
durch Mittel charakterisiert wird, die zwangsläufig verwendet werden müssen, um
das Decodierverfahren nach dem erteilten Patentanspruch 3 zu realisieren.


Für den erteilten Patentanspruch 4 gilt daher die Argumentation zum erteilten
Patentanspruch 3 entsprechend, so dass der Gegenstand des erteilten
Patentanspruchs 4 ebenfalls nicht auf erfinderischer Tätigkeit beruht.




6.    Der erteilte Patentanspruch 6 kann nicht günstiger beurteilt werden.


Nach Auffassung des Senats ist dieser auf ein Rechnerprogramm gerichtet, das
Befehle enthält, um das Decodierverfahren nach dem erteilten Patentanspruch 3
bei Ausführung auf einem Rechner auszuführen (s. o., Abschnitt I.5.4).

                                         - 81 -



Es   ist   aber    selbstverständlich,    dass    der   Fachmann   ein      derartiges
Rechnerprogramm zur Decodierung einsetzt, wenn er ausgehend von dem aus der
Druckschrift NK 1 bekannten Codier- und Decodierverfahren Vorzeichen von
Transformationskoeffizienten verbirgt. Gegenüber dem erteilten Patentanspruch 3
enthält der erteilte Patentanspruchs 6 somit nichts Zusätzliches, das ein Vorliegen
von erfinderischer Tätigkeit rechtfertigen könnte.




7.     Nach allem haben sämtliche Patentansprüche 1 bis 6 des Streitpatents
keinen Bestand.




                                          III.


Auch die Hilfsanträge bleiben ohne Erfolg.


Der Nichtigkeitsgrund der mangelnden Patentfähigkeit besteht in den Fassungen
der Hilfsanträge I bis XII unverändert fort.


Angesichts dessen kann die Frage der Zulässigkeit der darin vorgenommenen
Änderungen dahinstehen. Diesbezüglich ist aber festzuhalten, dass der Umstand,
dass die Hilfsanträge I bis VI das im erteilten Patentanspruch 1 ursprünglich nicht
offenbarte Merkmal M1.3.1 erneut aufweisen, nach der Rechtsprechung des
Bundesgerichtshofs deren Zulässigkeit nicht entgegensteht           (vgl.    BGH     -
Wundbehandlungsvorrichtung, a. a. O., Rn. 55; s. auch BPatG, Urteil vom
22. August 2018, 4 Ni 10/17, Abschnitt V.1.2 der Entscheidungsgründe).




1.     Hilfsantrag I kann keinen Erfolg haben, da das neu in Patentanspruch 1
aufgenommene Merkmal eine Patentfähigkeit nicht begründen kann.

                                       - 82 -



1.1    Patentanspruch 1 nach Hilfsantrag I ergibt sich aus dem erteilten
Patentanspruch 1 durch Einfügen des Merkmals


M1.2.4Hi I   et la donnée affectée du signe étant la première donnée non nulle de
             la partition courante à coder,


bzw. auf Deutsch


M1.2.4Hi I   und es sich bei dem mit dem Vorzeichen behafteten Datenelement um
             das erste von null verschiedene Datenelement der zu codierenden
             aktuellen Partition handelt,


zwischen den Merkmalen M1.2.2 und M1.2.3.


1.1.1 Das auf Merkmal M1.2.1 rückbezogene Merkmal M1.2.4Hi I verlangt, dass es
sich bei „dem“ mit dem Vorzeichen behafteten Datenelement um das erste
Datenelement aus der in Merkmal M1.2.1 angesprochenen, aus „wenigstens einem“
- d. h. einem oder mehreren - Datenelement(en) bestehenden Menge der von null
verschiedenen Datenelemente einer zu codierenden aktuellen Partition handelt.


1.1.2 Auf den ersten Blick beschreibt Merkmal M1.2.4Hi I genau den in Absatz
[0033] der Streitpatentschrift ausdrücklich angesprochenen Fall, dass das erste von
null verschiedene Datenelement mit dem vorab bestimmten Datenelement
zusammenfallen soll, dessen Vorzeichen verborgen wird.


Dies hat jedoch in den anspruchsgemäßen Anweisungen keinen Niederschlag
gefunden. Denn falls eine zu codierende aktuelle Partition mehrere von null
verschiedene    Datenelemente     enthält,    muss   das   in   Merkmal   M1.2.4Hi I
angesprochene erste von null verschiedene Datenelement nicht unbedingt mit dem
vorab bestimmten Datenelement zusammenfallen, dessen Vorzeichen verborgen
werden soll bzw. verborgen wird. Denn Merkmal M1.3.1 verlangt in Verbindung mit

                                      - 83 -



den Merkmalen M1.4 bis M1.6.1 lediglich, dass das Vorzeichen eines beliebigen
vorab bestimmten Datenelements aus der Menge der in Merkmal M1.2.1 genannten
Datenelemente verborgen werden soll (s. o., Abschnitt I.5.1.3); dieses vorab
bestimmte Datenelement muss nicht dasjenige Datenelement sein, auf das
Merkmal M1.2.4Hi I Bezug nimmt.


1.1.3 Mithin versteht der Senat Merkmal M1.2.4Hi I derart, dass das vorab
bestimmte Datenelement, dessen Vorzeichen anspruchsgemäß verborgen wird,
von Fall zu Fall mit dem ersten von null verschiedenen Datenelement der zu
codierenden aktuellen Partition zusammenfällt, aber nicht für jede Partition mit
diesem Datenelement identisch sein muss.


1.2    Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag I beruht mit
Rücksicht auf den aus der Druckschrift NK 1 bekannten Stand der Technik nicht auf
erfinderischer Tätigkeit.


1.2.1 Dass der streitpatentgemäße Decodierer das Datenelement überhaupt
ermitteln kann, dessen Vorzeichen zu rekonstruieren ist, macht es naturgemäß
erforderlich, dass es zwischen Codierer und Decodierer eine Vereinbarung darüber
gibt, zu welchem Transformationskoeffizienten das zu verbergende Vorzeichen
gehören soll. Demnach kann die Festlegung auf ein spezielles Datenelement nicht
über die Merkmale des Hauptantrags hinaus zur erfinderischen Tätigkeit von
Hilfsantrag I beitragen.


Nichts Anderes gilt, wenn die Lehre der Druckschrift NK 1 auf das Verbergen eines
Vorzeichens übertragen wird. Es muss dann zwangsläufig derjenige Koeffizient
festgelegt werden, dessen Vorzeichen verborgen wird, damit Codierer und
Decodierer synchronisiert sind. Trivialerweise kommt dafür auch nur ein Koeffizient
ungleich null in Frage, weil Null-Koeffizienten kein Vorzeichen haben. Die
Vorzeichenbits für einen Codierblock sind dabei als Gruppe von Bits codiert (vgl.
NK 9), wobei die Festlegung auf einen ganz bestimmten Koeffizienten für das zu

                                        - 84 -



versteckende Vorzeichen, z. B. den ersten, zweiten oder dritten Koeffizienten, im
vorliegenden Fall eine Patentfähigkeit nicht begründen kann. Vielmehr ist das
Festlegen auf das Vorzeichen des ersten von null verschiedenen Datenelements
als eine letztlich „beliebige“ Maßnahme zu verstehen, die im Hinblick auf das aus
Druckschrift NK 1 bekannte Codierverfahren keine erkennbaren Vor- oder Nachteile
hat, sondern eher ohne bestimmten Grund getroffen worden ist. Dem Streitpatent
ist keine Begründung oder Erläuterung zu dieser Maßnahme (wie etwa eine Angabe
besonderer Vorteile) entnehmbar, so dass diese entsprechend der BGH-Entscheidung „Blasenfreie Gummibahn I“ (Urteil vom 24. September 2003, X ZR
7/00, GRUR 2004, 47) zu beurteilen ist: „Eine von einem bestimmten Zweck oder
Ergebnis losgelöste, letztlich nach Belieben getroffene Auswahl ist für sich
grundsätzlich nicht geeignet, eine erfinderische Tätigkeit zu begründen“ (vgl. auch
BGH, Urteil vom 22. Mai 2007, X ZR 56/03, GRUR 2008, 56 - injizierbarer
Mikroschaum).


Selbst wenn davon ausgegangen würde, dass der erste und letzte Koeffizient
ungleich null für ein Verbergen des Vorzeichens deshalb in besonderer Weise
geeignet sind, weil sie trivialerweise stets zur Verfügung stehen (zumindest gilt dies
für eine Partition mit wenigstens zwei Koeffizienten ungleich null), so würde die
Festlegung auf einen dieser beiden Koeffizienten vor dem Hintergrund der in der
Druckschrift NK 1 beschriebenen Lehre auf Zweckmäßigkeitserwägungen beruhen
und letztendlich auch ins Belieben des Fachmanns gestellt sein, was wiederum eine
erfinderische Tätigkeit nicht begründen könnte.


Darüber hinaus ist generell auch nicht erkennbar, dass die Wahl des Koeffizienten,
dessen Vorzeichen verborgen werden soll, in irgendeiner Weise auf „technische“
Überlegungen zurückgeht oder irgendeinen Beitrag zur Lösung eines technischen
Problems leistet. Außer Frage steht, dass es eine Vereinbarung zwischen Codierer
und Decodierer darüber geben muss, welches der Vorzeichen verborgen werden
soll; ob man hierfür aber aus einer Menge an sich gleichwertiger Koeffizienten den
ersten oder irgendeinen anderen Koeffizienten heranzieht, bedarf keiner

                                       - 85 -



„technischen“ Überlegungen, sondern ist im Grunde ins Belieben des Fachmanns
gestellt. Weil aufgrund der Streitpatentschrift kein technischer Bezug hergestellt
werden kann, ist dieser Aspekt des Merkmals M1.2.4Hi I bei der Prüfung auf
erfinderischer Tätigkeit nicht zu berücksichtigen (entspr. BGH, Urteil vom
26. Oktober 2010, X ZR 47/07, GRUR 2011, 125 - Wiedergabe topografischer
Informationen; BGH, Urteil vom 18. Dezember 2012, X ZR 3/12, GRUR 2013, 275
- Routenplanung).


1.2.2 Das von der Beklagten vorgebrachte Argument, Merkmal M1.2.4Hi I begründe
eine erfinderische Tätigkeit, weil es gegenüber der Festlegung, dass das
Vorzeichen eines Datenelements an einer bestimmten festen Position innerhalb der
Partition verborgen wird, sicherstelle, dass immer ein Vorzeichen verborgen werden
könne, vermag nicht zu überzeugen.


Denn der Fachmann wird zum Verbergen von Vorzeichen trivialerweise
ausschließlich Transformationskoeffizienten in Betracht ziehen, die von null
verschieden sind, da nur diese ein Vorzeichen haben, das verborgen werden kann.
Aus seiner Sicht ist es abwegig, gedanklich einen Schritt zurückzugehen und das
Vorzeichen auf Basis einer festen absoluten Position innerhalb einer Partition (z. B.
der zweiten, fünften oder elften Position der Partition) auszuwählen, weil an einer
solchen festen Position bei vielen Partitionen überhaupt kein von null verschiedener
Transformationskoeffizient vorhanden ist, dessen Vorzeichen verborgen werden
könnte.


Selbst wenn der Beklagten dahingehend gefolgt würde, dass der Fachmann in
Betracht ziehen würde, den Koeffizienten, dessen Vorzeichen verborgen werden
soll, anhand einer festen Position innerhalb einer Partition auszuwählen, würde er
damit allenfalls den Nachteil in Kauf nehmen, bei vielen Partitionen gar kein
Vorzeichen verbergen zu können, obwohl diese Partitionen vorzeichenbehaftete
Koeffizienten enthalten. Ein mit einem solchen Vorgehen verbundener Vorteil ist
aber weder in der Streitpatentschrift offenbart noch anderweitig erkennbar (vgl.

                                        - 86 -



BGH, Urteil vom 24. April 2018, X ZR 50/16 - Gurtstraffer; BGH, Urteil vom 13. Juni
2023, X ZR 51/21 - Schlossgehäuse).


1.3    Unter Berücksichtigung der Ausführungen zum Hauptantrag ist der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag I nicht patentfähig. Mit dem
Patentanspruch 1 fallen auch alle übrigen Patentansprüche des Hilfsantrags I.




2.     Hilfsantrag II kann nicht günstiger beurteilt werden.


2.1    Patentanspruch 1 nach Hilfsantrag II ergibt sich aus dem erteilten
Patentanspruch 1, indem das Merkmal M1.2.3 durch das Merkmal


M1.2.3Hi II   ledit procédé de codage étant caractérisé en ce
              un nombre des données de la partition courante à coder
              à l’exception des données nulles situés avant la première donnée non
              nulle et des données nulles situés après la dernière donnée non nulle,
              est comparé avec un seuil prédéterminé (TSIG),
              et en ce que ledit procédé´il met en oeuvre, pour ladite partition
              courante, les étapes suivantes
              si le nombre est supérieur au seuil (TSIG):


bzw. auf Deutsch


M1.2.3Hi II   wobei das Codierungsverfahren dadurch gekennzeichnet ist, dass
              eine Anzahl der Datenelemente der zu codierenden aktuellen Partition
              mit Ausnahme der Datenelemente gleich null, die vor dem ersten von
              null verschiedenen Datenelement liegen und die nach dem letzten von
              null verschiedenen Datenelement liegen,
              mit einem zuvor bestimmten Schwellenwert (TSIG) verglichen wird,

                                       - 87 -



             und es das Verfahren für diese aktuelle Partition die folgenden Schritte
             umsetzt,
             falls die Anzahl größer als der Schwellenwert (TSIG) ist:


ersetzt wird (Merkmalsbestandteile, die im Rahmen des Hilfsantrags II neu in den
Anspruch aufgenommen worden sind, sind unterstrichen wiedergegeben).


2.1.1 Das    neue   Merkmal    M1.2.3Hi II   verlangt,   dass   „eine   Anzahl“   von
Datenelementen - eine numerische Größe - der zu codierenden aktuellen Partition
mit einem zuvor bestimmten Schwellenwert verglichen wird. Diese Anzahl soll die
Datenelemente gleich null, die vor dem ersten oder nach dem letzten von null
verschiedenen Koeffizienten angeordnet sind, nicht beinhalten.


Aus fachmännischer Sicht wird der Schwellenwertvergleich durchgeführt, um zu
garantieren, dass der modifizierte Koeffizient aus einer hinreichend großen
Grundmenge modifizierbarer Koeffizienten ausgewählt wird. In diesem Fall ergibt
sich mit hoher Wahrscheinlichkeit ein akzeptabler Kompromiss zwischen der durch
die Modifikation des ausgewählten Koeffizienten verursachten Verzerrung der
codierten Bildinhalte und der zur Übermittlung dieser Bildinhalte erforderlichen
Bitrate.


2.1.2 Dem Streitpatent ist diesbezüglich zu entnehmen, dass die in dem neuen
Merkmal genannte Anzahl von Datenelementen, die mit dem Schwellenwert
verglichen wird, „die“ (Gesamt-)Anzahl modifizierbarer Koeffizienten sein kann (vgl.
NK I, Absatz [0094] i. V. m. den Absätzen [0084] und [0093]). Dass sich die
beanspruchte „eine Anzahl“ auf modifizierbare Koeffizienten beziehen und/oder die
Anzahl sämtlicher modifizierbarer Koeffizienten einer Partition sein muss, verlangt
der Anspruchswortlaut allerdings nicht.


Gemäß dem Streitpatent sind Koeffizienten dann modifizierbar, wenn deren
Modifikation keine Desynchronisation hervorruft. Aus diesem Grund sind die vor

                                        - 88 -



dem ersten von null verschiedenen Koeffizienten liegenden Koeffizienten nicht
modifizierbar. Daneben können auch die nach dem letzten von null verschiedenen
Koeffizienten angeordneten Koeffizienten aus Gründen der Berechnungskomplexität nicht modifiziert werden (NK I, Absätze [0042], [0092]); letzteres ist für
den Fachmann dadurch motiviert, dass am Ende einer Partition oftmals lange
lückenlose Reihen von Null-Koeffizienten liegen, die als Ganzes sehr effizient
entropiecodiert werden können. Koeffizienten mit Wert null, die zwischen dem
ersten und letzten von null verschiedenen Koeffizienten liegen, sind nach der
streitpatentgemäßen Lehre ebenfalls modifizierbar (vgl. das in Absatz [0093] der
NK I genannte Beispiel, bei dem die Teilliste SE1 elf modifizierbare Koeffizienten
hat, unter denen sich Nullen befinden).


2.2   Die Maßnahmen des Merkmals M1.2.3Hi II sind aus dem Stand der Technik
nahegelegt.


So beschreibt die Druckschrift NK 1 an mehreren Textstellen, dass sich die Anzahl
zur Verfügung stehender Transformationskoeffizienten auf das Data-Hiding
auswirkt und insbesondere das Verbergen in den Transformationskoeffizienten
ineffizienter wird, wenn weniger Transformationskoeffizienten zum Modifizieren zur
Verfügung stehen.


Diese Textpassagen betreffen Seite 734, rechte Spalte, Abschnitt C, erster Absatz:
„[…] a key feature of the proposed scheme is to have enough transform coefficients
to easily balance between rate and distortion modification”; Seite 736, linke Spalte,
zweiter Absatz: „Indeed, due to the decrease of the transform coefficients available
for hiding, the efficiency of the scheme decreases for lower bitrates and becomes
quasi-negligible for very low bitrates […]” sowie
Seite 736, linke Spalte, dritter Absatz: „The efficiency of the proposed scheme is
related to the number of transform coefficients available”.

                                       - 89 -



Angesichts der angeführten Textstellen wird der Fachmann durch die Druckschrift
NK 1 unmittelbar veranlasst, die aus der Druckschrift NK 1 bekannte Lehre derart
zu modifizieren, dass das Durchführen des Data-Hiding-Verfahrens von der Anzahl
der verfügbaren (d. h. modifizierbaren) Transformationskoeffizienten abhängt.
Entgegen der Auffassung der Beklagten hat in diesem Zusammenhang die
Einführung eines Schwellenwerts, mit dem die jeweilige Anzahl modifizierbarer
Koeffizienten eines Blocks verglichen wird, so dass das Data-Hiding-Verfahren nur
bei einer hinreichend hohen Anzahl modifizierbarer Koeffizienten durchgeführt wird,
für den Fachmann zumindest nahegelegen.


Gemäß Druckschrift NK 1 sind nur die von null verschiedenen Koeffizienten eines
Blocks modifizierbar (vgl. Seite 733, linke Spalte, Satz nach Gleichung (7) sowie
drittletzter Satz - „The transform coefficients equal to zero are not considered to
avoid breaking the zero series“). Da der Schwellenwertvergleich ausschließlich
modifizierbare Koeffizienten betrifft, ermittelt der Fachmann somit die Anzahl der
von null verschiedenen - modifizierbaren - Koeffizienten eines Blocks und vergleicht
diese mit dem Schwellenwert. Diese Anzahl beinhaltet diejenigen Koeffizienten
nicht, die vor dem ersten oder nach dem letzten von null verschiedenen
Koeffizienten angeordnet sind und den Wert null haben.


Auf diese Weise gelangt der Fachmann zu Merkmal M1.2.3Hi II, ohne erfinderisch
tätig zu werden.


2.3   Die Beklagte begründet ihre gegenteilige Auffassung sinngemäß wie folgt:


2.3.1 Die Druckschrift NK 1 scheine zwar grundsätzlich auf das Problem
hinzuweisen, die die zusätzlichen Merkmale der Ansprüche gemäß Hilfsantrag II
lösten, gebe jedoch keinen Hinweis auf die streitpatentgemäße Lösung. Vielmehr
schlage diese Druckschrift (statt eines Schwellenwertvergleichs) vor, Luma- und
Chromakomponenten für das Data-Hiding zusammenzufassen und den MVComp-Index in diesen zusammengefassten Blöcken zu verbergen, sowie in Fällen, in

                                         - 90 -



denen der MVComp-Index für aufeinanderfolgende Blöcke gleichbleibe, beide
Blöcke zusammenzufassen und den Index anhand der Parität der Summe aller
Transformationskoeffizienten beider Blöcke zu übertragen.


Diese Einwände überzeugen nicht.


So ändert der Umstand, dass gemäß Druckschrift NK 1 ein Verbergen des
MVComp-Index in zusammengefassten Chroma- und Luma-Blöcken durch eine zu
geringe Anzahl von Chroma-Koeffizienten motiviert ist, nichts daran, dass auch
derart zusammengefasste Blöcke in vielen Fällen eine sehr geringe Anzahl von
Nicht-Null-Koeffizienten enthalten können, deren Modifikation verhältnismäßig
große Verzerrungen verursacht. Entsprechendes gilt für den Fall der in Druckschrift
NK 1 vorgeschlagenen Zusammenfassung aufeinanderfolgender Blöcke. Dieser
Fall betrifft zudem nur spezielle Blockkombinationen, nämlich aufeinanderfolgende
Blöcke mit gleichen Prädiktoren (vgl. NK 1, Abschnitt IV.C, zweiter Absatz; zum
Begriff „Prädiktor“ vgl. NK 9, Seite 6, Definition 3.77).


Das grundsätzliche Problem, dass es Blöcke geben kann, bei denen die zur
Verfügung stehende Anzahl modifizierbarer Koeffizienten so gering ist, dass deren
Modifikation eine inakzeptable Verzerrung verursacht, wird daher durch die
zusätzliche Berücksichtigung weiterer Koeffizienten nicht abschließend gelöst. Der
Fachmann wird daher durchaus andere Ansätze in Betracht ziehen, diesem
Problem zu begegnen. Solche Ansätze basieren entweder auf einer weiteren
Erhöhung der Anzahl modifizierbarer Koeffizienten pro zu verbergendem
Vorzeichen, oder aber darauf, Blöcke oder Blockkombinationen mit zu wenigen
modifizierbaren Koeffizienten von einem Data-Hiding auszunehmen, um große
Verzerrungen zu vermeiden. Um derartige Blöcke oder Blockkombinationen zu
identifizieren, ist es platt selbstverständlich, einen Vergleich der Anzahl der
vorhandenen      modifizierbaren      Koeffizienten      mit   einem   Schwellenwert
durchzuführen,     dessen    Überschreitung       eine   hinreichend   große   Anzahl
modifizierbarer Koeffizienten anzeigt.

                                          - 91 -



2.3.2 Nach Auffassung der Beklagten seien zudem laut Druckschrift NK 1 lediglich
von null verschiedene Transformationskoeffizienten modifizierbar, wohingegen dies
gemäß den Anspruchsmerkmalen auch für Datenelemente mit Werten gleich null
gelte, die zwischen dem ersten und letzten von null verschiedenen Datenelement
angeordnet seien. Die Druckschrift NK 1 lege weder einen derartigen Satz
modifizierbarer         Datenelemente          noch        einen       entsprechenden
Schwellenwertvergleich nahe.


Auch diesem Argument kann nicht gefolgt werden.


Denn der Wortlaut des Patentanspruchs 1 nach Hilfsantrag II verlangt nicht, dass
Nullen in den Schwellenwertvergleich miteinbezogen werden, sondern nur, dass
eine bestimmte Anzahl von Datenelementen, zu denen die Null-Koeffizienten vor
dem ersten und nach dem letzten von null verschiedenen Koeffizienten nicht
gehören, mit einem Schwellenwert verglichen wird. Genau dies ist der Fall, wenn
ausgehend von dem aus Druckschrift NK 1 bekannten Data-Hiding-Verfahren die
Anzahl der modifizierbaren (d. h. der von null verschiedenen) Koeffizienten mit
einem Schwellenwert verglichen wird.


2.3.3 Ferner argumentiert die Beklagte, da laut Patentbeschreibung die
modifizierbaren Transformationskoeffizienten stets den ersten und den letzten von
null    verschiedenen     Koeffizienten    sowie      sämtliche    dazwischenliegenden
Koeffizienten umfassen würden, seien die im Rahmen des Hilfsantrags II
hinzugefügten Merkmale dahingehend zu verstehen, dass generell - also
unabhängig von den spezifischen Werten der Transformationskoeffizienten einer
Partition - die Anzahl der Datenelemente der Partition mit Ausnahme der
Datenelemente gleich null, die vor dem ersten und nach dem letzten von null
verschiedenen Datenelement liegen, mit einem Schwellenwert verglichen werden
soll.

                                        - 92 -



Diesem Argument kann bereits nicht gefolgt werden, weil es auf einer
einschränkenden Auslegung des Gegenstands von Patentanspruch 1 nach
Hilfsantrag II basiert. So betrifft Merkmal M1.2.3Hi II lediglich „eine“ nicht näher
spezifizierte Anzahl von modifizierbaren Datenelementen, die auch kleiner sein
kann als „die“ (Gesamt-)Anzahl der modifizierbaren Datenelemente.


Zudem wird mit Patentanspruch 1 nach Hilfsantrag II lediglich ein Verfahren
beansprucht, das zum Codieren eines in Partitionen unterteilten Bildes geeignet ist,
wobei hierfür die Schritte der Merkmale M1.2.3Hi II bis M1.6.1 zumindest einmal
ausgeführt werden (vgl. Merkmale M1.1 und M1.2.3Hi II). Der Ablauf dieses
Verfahrens kann also bereits dann verwirklicht sein, wenn ein einziger Block
anspruchsgemäß verarbeitet wird. Damit ist Patentanspruch 1 nach Hilfsantrag II
nicht zwangsläufig auf einen Gegenstand gerichtet, bei dem mehrere Blöcke
verarbeitet werden, für die der Schwellenwertvergleich „generell“ wie beansprucht
durchgeführt wird.


2.4   Mit Rücksicht auf die Ausführungen zum Hauptantrag ist der Gegenstand des
Patentanspruchs 1 gemäß Hilfsantrag II somit nicht patentfähig. Mit dem
Patentanspruch 1 fallen auch alle übrigen Patentansprüche des Hilfsantrags II.




3.    Entsprechendes gilt für den Hilfsantrag III.


Die Merkmale des Patentanspruchs 1 nach Hilfsantrag III ergeben sich aus einer
Kombination der Änderungen, die zu Patentanspruch 1 nach Hilfsantrag I bzw. II
führen, d. h. durch Aufnahme des Merkmals M1.2.4Hi I in den erteilten
Patentanspruch 1 und Ersetzung von Merkmal M1.2.3 durch Merkmal M1.2.3Hi II.


Für den Patentanspruch 1 nach Hilfsantrag III gelten die Ausführungen zu den
Hilfsanträgen I und II (s. o., Abschnitte III.1, III.2). Im Hinblick auf die Frage der

                                        - 93 -



Patentfähigkeit ist zudem nicht erkennbar, dass sich aus der Kombination der neuen
Anspruchsmerkmale ein besonderer Synergieeffekt ergibt.


Unter Berücksichtigung der Ausführungen zu den Hilfsanträgen I und II ist auch der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag III somit nicht patentfähig.
Mit seinem Patentanspruch 1 fallen auch alle übrigen Patentansprüche des
Hilfsantrags III.




4.     Hilfsantrag IV ist nicht günstiger zu beurteilen.


4.1    Patentanspruch 1 nach Hilfsantrag IV unterscheidet sich von dem erteilten
Patentanspruch 1 dadurch, dass Merkmal 1.2.3 durch das Merkmal


M1.2.3Hi IV    ledit procédé de codage étant caractérisé en ce
               un nombre des données de la partition courante à coder,
               qui sont modifiables,
               est comparé avec un seuil prédéterminé (TSIG)
               les données modifiables comprenant les données de ladite partition
               courante à coder à l’exception des données nulles situés avant la
               première donnée non nulle et des données nulles situés après la
               dernière donnée non nulle,
               et en ce que ledit procédé met en oeuvre, pour ladite partition
               courante, les étapes suivantes
               si le nombre est supérieur au seuil (TSIG):


bzw. auf Deutsch


M1.2.3Hi IV    wobei das Codierungsverfahren dadurch gekennzeichnet ist, dass
               eine Anzahl der Datenelemente der zu codierenden aktuellen
               Partition,

                                           - 94 -



               die modifizierbar sind,
               mit einem zuvor bestimmten Schwellenwert (TSIG) verglichen wird,
               wobei die modifizierbaren Datenelemente die Datenelemente der zu
               codierenden aktuellen Partition
               mit Ausnahme der Datenelemente gleich null, die vor dem ersten von
               null verschiedenen Datenelement liegen und die nach dem letzten von
               null verschiedenen Datenelement liegen,
               umfassen,
               und das Verfahren für diese aktuelle Partition die folgenden Schritte
               umsetzt,
               falls die Anzahl größer als der Schwellenwert (TSIG) ist:


und Merkmal M1.5 durch das Merkmal


M1.5Hi IV      en fonction du résultat de ladite comparaison, modification (S5) ou non
               d'au moins une des données modifiables de la partition courante


bzw. auf Deutsch


M1.5Hi IV      in Abhängigkeit vom Ergebnis des Vergleichens Modifizieren (S5)
               oder   Nicht-Modifizieren     wenigstens   eines   der modifizierbaren
               Datenelemente der aktuellen Partition,


ersetzt worden ist (Merkmalsbestandteile, die im Rahmen des Hilfsantrags IV neu
aufgenommen worden sind, sind unterstrichen wiedergegeben).


4.1.1 Die zu Merkmal M1.5Hi IV führende Änderung bringt zum Ausdruck, dass
wenigstens eines der modifizierbaren Datenelemente in Abhängigkeit vom Ergebnis
des in Merkmal M1.5 angesprochenen Vergleichs modifiziert oder nicht modifiziert
werden soll.

                                           - 95 -



4.1.2 Im Vergleich mit M1.2.3Hi II verlangt Merkmal M1.2.3Hi IV nun ausdrücklich,
dass      „eine    Anzahl“   von        modifizierbaren        Datenelementen    in   den
Schwellenwertvergleich eingeht. Diese Anzahl kann dem Merkmalswortlaut nach
„die“ (Gesamt-)Anzahl modifizierbarer Koeffizienten sein, oder aber auch „eine“
geringere Anzahl von modifizierbaren Datenelementen.


Die Anweisung „wobei die modifizierbaren Datenelemente die Datenelemente der
zu codierenden aktuellen Partition mit Ausnahme […]                umfassen“ in Merkmal
M1.2.3Hi IV definiert entweder - gemäß einer ersten Auslegungsalternative -
ausschließlich die in den Schwellenwertvergleich eingehende „eine Anzahl“ von
modifizierbaren Datenelementen (weil sich der Ausdruck „les données modifiables“
unmittelbar auf die vorher angesprochene „un nombre des données […], qui sont
modifiables“      beziehen   kann),       oder      legt   -     gemäß   einer    zweiten
Auslegungsalternative - allgemeiner fest, wodurch modifizierbare Datenelemente
generell charakterisiert sein sollen.


Für beide Auslegungsalternativen legt Merkmal M1.2.3Hi IV fest, dass die
modifizierbaren Datenelemente die Datenelemente zwischen dem ersten und
letzten Datenelement der zu codierenden aktuellen Partition (einschließlich dieser
beiden Datenelemente) umfassen sollen. Eine Modifikation der vor dem ersten von
null verschiedenen Koeffizienten angeordneten Null-Koeffizienten scheidet dabei
prinzipiell aus, weil sie zu Fehlern bei der Decodierung führt (s. o., Abschnitt
III.2.1.2).


4.2     Die Maßnahmen der Merkmale M1.2.3Hi IV und M1.5Hi IV können eine
erfinderische Tätigkeit nicht stützen.


4.2.1 So ist Merkmal M1.5Hi IV aus Druckschrift NK 1 bekannt.


Denn in dem dort beschriebenen Data-Hiding-Verfahren kann grundsätzlich jeder
von null verschiedene Koeffizient in Abhängigkeit des Vergleichs von berechnetem

                                          - 96 -



Funktionswert und Parität entweder modifiziert (und ist daher modifizierbar) oder
nicht modifiziert werden (s. o., Abschnitt II.2.1).


4.2.2 Ferner kann auch Merkmal M1.2.3Hi IV eine erfinderische Tätigkeit nicht
tragen.


Dies lässt sich auf zwei Weisen begründen:


a)     So ist das Merkmal M1.2.3Hi IV bereits dann verwirklicht, wenn der Fachmann
das in Druckschrift NK 1 beschriebene Data-Hiding in der in Abschnitt III.2.3
beschriebenen        Weise       zum      Verbergen          von     Vorzeichen       von
Transformationskoeffizienten      verwendet,       d. h.   die   Anzahl   der   von   null
verschiedenen Koeffizienten mit einem Schwellenwert vergleicht.


Denn bei der Codierung typischer Bildinhalte kommt es oftmals vor, dass in einem
Block quantisierter Transformationskoeffizienten zwischen dem ersten und letzten
von null verschiedenen Koeffizienten keine Koeffizienten liegen, die den Wert null
haben. In diesem Fall besteht die Menge der in den Schwellenwertvergleich
eingehenden modifizierbaren Koeffizienten des Blocks aus dem ersten und letzten
von null verschiedenen Koeffizienten sowie ggf. aus allen (Nicht-Null-)Koeffizienten,
die zwischen diesen angeordnet sind. Diese Menge beinhaltet die Null-Koeffizienten
vor dem ersten und nach dem letzten von null verschiedenen Koeffizienten nicht
und enthält ausschließlich modifizierbare Koeffizienten.


Damit liegt Merkmal M1.2.3Hi IV gemäß der ersten Auslegungsalternative vor.


Im Übrigen wird der Fachmann dabei selbstverständlich gewährleisten, dass der
erste von null verschiedene Koeffizient nicht zu null modifiziert wird. Denn
ansonsten kann der Decodierer den Koeffizienten, dessen Vorzeichen verborgen
worden ist, nicht korrekt ermitteln. Dies liegt daran, dass bei einer Modifikation des
ersten von null verschiedenen Koeffizienten zu null der erste (zweite, dritte, …) von

                                        - 97 -



null verschiedene Koeffizient der codierten Partition, die von dem Decodierer
empfangen wird, der zweite (dritte, vierte ...) von null verschiedene Koeffizient des
vom Codierer codierten aktuellen Blocks ist.


b)    Zudem schließt der Fachmann aus den Ausführungen der Druckschrift NK 1,
dass bereits Testrechnungen durchgeführt worden sind, bei denen auch
Koeffizienten modifiziert werden, die den Wert null haben (vgl. Seite 733, linke
Spalte, Satz nach Gleichung (7) sowie letzter Absatz - „The transform coefficients
equal to zero are not considered to avoid breaking the zero series. Indeed, such
modifications systematically provide a rate Rnwj increase and, in most cases, there
also increase the distortion Dnwj“). Denn nur so können die Autoren der Druckschrift
NK 1 zum Schluss gelangt sein, dass Modifikationen von Nullen zu einer
Ratenerhöhung und in den meisten Fällen auch zu einer Erhöhung der Verzerrung
führen. Ähnliche Testrechnungen, bei denen auch DCT-Koeffizienten mit Wert null
modifiziert werden, weil generell wenige Koeffizienten ungleich null zur Verfügung
stehen, sind ihm auch aus Druckschrift NK 4 bekannt (vgl. erste Seite, rechte
Spalte, erster vollständiger Absatz sowie zweite Seite, Abschnitt II.A).


Der Fachmann wird diese Testrechnungen nacharbeiten und dazu auf seinem
Rechner implementieren. Denn auf diese Weise kann er beurteilen, wie sich eine
Modifikation von Nullen quantitativ auf die Bitraten und Verzerrungen auswirkt, die
sich bei der Codierung seiner eigenen Bildinhalte (z. B. von Testvideos) ergeben,
und damit selbst ein „Gefühl“ für den Einfluss einer Modifikation von Nullen beim
Verbergen von Datenelementen bekommen.


In Zuge dessen wird er selbstverständlich Modifikationen der vor dem ersten von
null verschiedenen Koeffizienten angeordneten Null-Koeffizienten ausschließen,
weil der Decodierer in diesem Fall den Nicht-Null-Koeffizienten, dessen Vorzeichen
vom Codierer modifiziert worden ist, nicht mehr korrekt ermittelt. Hätte der Codierer
beispielsweise das Vorzeichen des ersten von null verschiedenen Koeffizienten
eines uncodierten Blocks verborgen und diesen Koeffizienten anschließend zu null

                                          - 98 -



modifiziert, würde der Decodierer feststellen, dass der erste von null verschiedene
Koeffizient des modifizierten Blocks an einer anderen Position angeordnet ist und
dieser    Position    fälschlicherweise   das      verborgene   Vorzeichen   zuordnen.
Entsprechendes gilt, wenn z. B. das Vorzeichen des zweiten oder dritten von null
verschiedenen Koeffizienten verborgen wird.


Somit kommt der Fachmann auf Basis fachüblicher Überlegungen unmittelbar zu
einer Lehre, bei der neben den Nicht-Null-Koeffizienten auch die nach dem ersten
Nicht-Null-Koeffizienten angeordneten Koeffizienten mit Wert null modifizierbar
sind. Die Menge von Koeffizienten, die generell modifiziert werden können, umfasst
damit alle Koeffizienten, die zwischen dem ersten und letzten von Null
verschiedenen Koeffizienten des zu codierenden Blocks liegen (diese beiden
Koeffizienten eingeschlossen). Dies entspricht der zweiten Auslegungsalternative
des Merkmals M1.2.3Hi IV.


Da es ferner für den Fachmann naheliegt, den Schwellenwertvergleich mit den
jeweils zur Verfügung stehenden modifizierbaren Koeffizienten durchzuführen
(s. o., Abschnitt III.2.2), gelangt der Fachmann zu Merkmal M1.2.3Hi IV gemäß der
zweiten Auslegungsalternative, ohne erfinderisch tätig zu werden.


4.3      Die Beklagte ist der Auffassung, Patentanspruch 1 nach Hilfsantrag IV
verlange, dass die Anzahl der Datenelemente einer Partition mit Ausnahme der
Datenelemente vor dem ersten und nach dem letzten von null verschiedenen
Datenelement mit einem Schwellenwert verglichen wird. Ausgehend von der
Druckschrift NK 1 würde der Fachmann hierfür nicht die im Allgemeinen hiervon
verschiedene Anzahl der von null verschiedenen Koeffizienten heranziehen.


4.3.1 Dem       ist   entgegenzuhalten,      dass     der   Anspruchswortlaut    einen
Schwellenwertvergleich betrifft, in den lediglich „eine” nicht näher definierte Anzahl
modifizierbarer Koeffizienten eingeht. Diese Anzahl muss nicht mit der Anzahl von

                                          - 99 -



Koeffizienten zwischen dem ersten und letzten von null verschiedenen (diese
beiden Koeffizienten eingeschlossen) übereinstimmen.


4.3.2 Abgesehen davon läge es nahe, lückenlose Nullreihen, die am Ende einer zu
codierenden aktuellen Partition (nach dem letzten von Null verschiedenen
Koeffizienten) angeordnet sind, von einer Modifikation auszuschließen, weil diese
sehr effizient entropiecodiert werden können. Auch ein solches Vorgehen ist
fachüblich. In diesem Fall würde die Menge der modifizierbaren Koeffizienten -
diese wird mit dem Schwellenwert verglichen - ausschließlich den ersten und letzten
Nicht-Null-Koeffizienten       sowie    die   dazwischenliegenden     modfizierbaren
Koeffizienten beinhalten. Dies gilt sowohl im Hinblick auf die Ausführungen unter
den Abschnitten II.2 und III.4.2.2 a) als auch unter Abschnitt III.4.2.2 b). Das
bedeutet, dass sämtliche Koeffizienten, die vor dem ersten und nach dem letzten
Nicht-Null-Koeffizienten angeordnet sind, nicht in den Schwellenwertvergleich
eingehen.


4.4   Unter Berücksichtigung der Ausführungen zum Hilfsantrag II ist der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag IV somit nicht patentfähig.
Mit seinem Patentanspruch 1 fällt der gesamte Hilfsantrag IV.




5.    Auch Hilfsantrag V hat keinen Erfolg.


5.1   Patentanspruch       1     nach    Hilfsantrag   V   unterscheidet   sich   von
Patentanspruch 1 nach Hilfsantrag IV durch die weitere Anweisung, dass der in
Merkmal 1.2.3Hi IV angesprochene Schwellenwert den Wert 4 besitzen soll („et le
seuil ayant une valeur de 4”).


5.2   Auch dieser Gegenstand ergibt sich in naheliegender Weise aus dem
aufgezeigten Stand der Technik.

                                             - 100 -



So wird im Streitpatent an genau zwei Textstellen darauf hingewiesen, dass der
Schwellenwert gleich 4 ist. Bei diesen Textstellen handelt es sich um die Absätze
[0094] und [0177] der Streitpatentschrift. Die Ausführungen des Streitpatents in
Hinblick auf gerade diesen Wert gehen nicht über die bloße Zahlenangabe hinaus.
Ausführungen       zu    etwaigen      mit   diesem    Wert   verbundenen   technischen
Besonderheiten sind dem Streitpatent nicht zu entnehmen. Aus Sicht des Senats
handelt es sich bei dem Schwellenwert gleich 4 um eine willkürliche Festlegung, die
im Belieben des Fachmanns liegt und keinen technischen Beitrag liefern kann.


5.3    Mit Rücksicht auf die Ausführungen zum Hilfsantrag IV ist der Gegenstand
des Patentanspruchs 1 gemäß Hilfsantrag V somit nicht patentfähig. Mit dem
Patentanspruch 1 fallen auch alle übrigen Patentansprüche des Hilfsantrags V.




6.     Hilfsantrag VI kann nicht günstiger beurteilt werden.


Die Merkmale des Patentanspruchs 1 nach Hilfsantrag VI ergeben sich aus einer
Kombination der Änderungen, die zu Patentanspruch 1 nach Hilfsantrag I bzw. V
führen.


6.1    Für den Patentanspruch 1 nach Hilfsantrag VI gelten die Ausführungen zu
Patentanspruch 1 in den Fassungen des Hauptantrags sowie der Hilfsanträge I und
V (s. o., Abschnitte II.2, III.1, III.5).


Im Hinblick auf die Beurteilung der Patentfähigkeit des Gegenstands von
Patentanspruch 1 nach Hilfsantrag VI ist ferner noch anzumerken, dass sich
Merkmal M1.2.4Hi I zwangsläufig aus fachüblichen Überlegungen ergibt, wenn der
Fachmann ausgehend von der Lehre der Druckschrift NK 1 zusätzlich eine
Modifikation von Null-Koeffizienten erwägt, die auf den ersten von null
verschiedenen Koeffizienten folgen (s. o., Abschnitt III.4.2.2 b)).

                                         - 101 -



In diesem Fall ist es nämlich zweckmäßig, das Vorzeichen des ersten von null
verschiedenen      Koeffizienten   zu   verbergen     (vgl.   Merkmal M1.2.4Hi I), um
Decodierungsfehler zu vermeiden. Denn falls das Vorzeichen eines anderen Nicht-Null-Koeffizienten verborgen wird, kann der Fall eintreten, dass ein möglicherweise
vor diesem Koeffizienten angeordneter Null-Koeffizient modifiziert wird. In diesem
Fall würde der Decodierer das verborgene Vorzeichen nicht dem anderen Nicht-Null-Koeffizienten zuordnen. Wenn z. B. der quantisierte Rest einer aktuellen zu
codierenden Partition die Form (0 0 2 0 3 2 4 0) hat und das Vorzeichen des zweiten
von Null verschiedenen Koeffizienten „3“ verborgen werden soll, erhält der
Decodierer bei einer Addition von +1 zu dem unmittelbar vor der „3“ angeordneten
Null-Koeffizienten einen zu decodierenden quantisierten Rest der Form (0 0 2 1 3
2 4 0). Aus diesem wird er - inkorrekterweise - ableiten, dass das zu verbergende
Vorzeichen zum Koeffizienten „1“ gehört, da dieser der zweite von null verschiedene
ist. Entsprechendes gilt, wenn das Vorzeichen des dritten oder vierten von null
verschiedenen Koeffizienten verborgen wird.


6.2    Mit Rücksicht auf die Ausführungen zu den Hilfsanträgen I und V ist der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag VI somit nicht patentfähig.
Mit dem Patentanspruch 1 fallen auch alle übrigen Patentansprüche des
Hilfsantrags VI.




7.     Hilfsantrag    VII   hat    keinen   Erfolg,   weil    der   Gegenstand   seines
Patentanspruchs 1 ausgehend von Druckschrift NK 1 nahegelegt ist.


7.1    Patentanspruch 1 nach Hilfsantrag VII ergibt sich aus dem erteilten
Patentanspruch 3 - dieser betrifft ein Verfahren zum Decodieren eines
Datensignals -, indem nach Merkmal M3.2.2 das Merkmal


M3.2.4Hi I   et la donnée affectée du signe étant la première donnée non nulle de
             la partition courante à décoder,

                                           - 102 -



bzw. auf Deutsch


M3.2.4Hi I   und es sich bei dem mit dem Vorzeichen behafteten Datenelement um
             das erste von null verschiedene Datenelement der zu decodierenden
             aktuellen Partition handelt,


eingeschoben wird.


Laut Merkmal M3.2.4Hi I soll es sich bei dem Datenelement, dessen Vorzeichen als
Ergebnis des beanspruchten Decodierverfahrens vorliegen soll, um das erste von
null verschiedene Datenelement der zu decodierenden aktuellen Partition handeln.


7.2    Mit dem Merkmal M3.2.4Hi I kann ein Vorliegen von erfinderischer Tätigkeit
nicht begründet werden.


So wurde in den Abschnitten III.1 und III.6 ausgeführt, dass das Verbergen des
Vorzeichens des ersten von null verschiedenen Koeffizienten ausgehend von dem
in Druckschrift NK 1 beschriebenen Codierverfahren eine erfinderische Tätigkeit
nicht begründen kann.


Da es in diesem Fall zwischen Codierer und Decodierer eine Vereinbarung darüber
geben muss, dass das Vorzeichen des ersten von null verschiedenen Koeffizienten
verborgen    wird    (s. o.,   Abschnitt    III.1.2),   realisiert   der   Fachmann   ein
Decodierverfahren gemäß Patentanspruch 1 nach Hilfsantrag VII, wenn er das in
Druckschrift NK 1 beschriebene Decodierverfahren zur Rekonstruktion des
Vorzeichens des ersten von null verschiedenen Koeffizienten unter Verwendung der
Parität der Summe der decodierten Transformationskoeffizienten einsetzt. Der
Fachmann wird dabei selbstverständlich sicherstellen, dass der erste von null
verschiedene Koeffizient des zu codierenden ursprünglichen Blocks nicht zu null
modifiziert wird, da der Decodierer ansonsten das verborgene Vorzeichen in
fehlerhafter Weise einem anderen Koeffizienten zuordnen würde.

                                       - 103 -



7.3    Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 3 beruht
die Lehre des Patentanspruchs 1 gemäß Hilfsantrag VII somit nicht auf einer
erfinderischen Tätigkeit und ist daher nicht patentfähig. Mit seinem Patentanspruch
1 fällt der gesamte Hilfsantrag VII.




8.     Auch die Beurteilung der Hilfsanträge VIII bis XII führt zu keinem anderen
Ergebnis. Denn der jeweilige Gegenstand ihres Patentanspruchs 1 ist jeweils
ausgehend von Druckschrift NK 1 nahegelegt.


8.1    Patentanspruch 1 nach Hilfsantrag XII beruht auf Patentanspruch 1 nach
Hilfsantrag VII, wobei Merkmal M3.2.3 durch das Merkmal


M3.2.3Hi V    ledit procédé de décodage étant caractérisé en ce qu’
              un nombre des données de la partition courante (Bi) à décoder,
              qui sont susceptibles d’avoir été modifies,
              est compare avec un seuil predetermine,
              les données susceptibles d’avoir été modifiés comprenant les
              données de ladite partition courante à décoder à l’exception des
              données nulles situés avant la première donnée non nulle    et   des
              données nulles situés après la dernière donnée non nulle,
              et le seuil ayant une valeur de 4,
              et ledit procédé comprend, pour ladite partition courante, les étapes
              suivantes
              si le nombre est supérieur au seuil (TSIG):


bzw. auf Deutsch


M3.2.3Hi V    wobei das Decodierungsverfahren dadurch gekennzeichnet ist, dass
              eine Anzahl von Datenelementen der zu decodierenden aktuellen
              Partition,

                                         - 104 -



                die modifiziert worden sein können,
                mit einem zuvor bestimmten Schwellenwert verglichen wird,
                wobei die Datenelemente, die modifiziert worden sein können, die
                Datenelemente der zu decodierenden aktuellen Partition
                mit Ausnahme der Datenelemente gleich null, die vor dem ersten von
                null verschiedenen Datenelement liegen und die nach dem letzten von
                null verschiedenen Datenelement liegen,
                umfassen,
                und wobei der Schwellenwert den Wert 4 hat,
                und das Verfahren für diese aktuelle Partition die folgenden Schritte
                umsetzt,
                falls die Anzahl größer als der Schwellenwert (TSIG) ist:


ersetzt wird.


Dieses neue Merkmal korrespondiert zu dem Merkmal M1.2.3Hi V der mit
Patentanspruch 1 nach Hilfsantrag V und VI beanspruchten Codierverfahren und
beschreibt einen Vergleich „einer Anzahl“ von Datenelementen einer zu
decodierenden aktuellen Partition mit einem zuvor bestimmten Schwellenwert
von 4. Demnach werden die Merkmale M3.3 bis M3.5.2, die die Rekonstruktion
eines verborgenen Vorzeichens betreffen, nur dann ausgeführt, wenn „eine Anzahl“
von Datenelementen, die modifiziert worden sein können, größer als 4 ist.


Im Unterschied zu den genannten Codierverfahren betrifft das mit Patentanspruch 1
nach   Hilfsantrag     XII   beanspruchte    Decodierverfahren    eine      Anzahl   von
Datenelementen, die modifiziert worden sein können, da es keine Informationen
über die Identität der tatsächlich modifizierten Datenelemente benötigt.


Ähnlich wie das Merkmal M1.2.3Hi IV erlaubt das Merkmal M3.2.3Hi V zwei
Auslegungsalternativen. So definiert die Anweisung „wobei die Datenelemente, die
modifiziert worden sein können, die Datenelemente der zu decodierenden aktuellen

                                      - 105 -



Partition mit Ausnahme […] umfassen“ entweder ausschließlich die in den
Schwellenwertvergleich eingehende „eine Anzahl“ von Datenelementen, die
modifiziert worden sein können (erste Auslegungsalternative), oder legt allgemeiner
fest, wodurch Datenelemente, die modifiziert worden sein können, charakterisiert
sein sollen (zweite Auslegungsalternative).


Merkmal M3.2.3Hi V verlangt, dass die Menge dieser Datenelemente die
Datenelemente zwischen dem ersten und letzten von null verschiedenen
Datenelementen (einschließlich dieser beiden Datenelemente) umfasst.


8.2   Mit dem Merkmal M3.2.3Hi V kann eine erfinderische Tätigkeit nicht begründet
werden.


So ist es eine Selbstverständlichkeit, Decodierverfahren „symmetrisch“ zu
Codierverfahren auszugestalten. Das bedeutet im vorliegenden Fall, dass der beim
Codierverfahren ausgeführte Schwellenwertvergleich mit Schwellenwert 4 auch im
Rahmen des zugehörigen Decodierverfahrens implementiert wird, so dass der
Decodierer feststellen kann, ob in einer codierten Partition das Vorzeichen eines
vorab bestimmten - z. B. des ersten von null verschiedenen - Koeffizienten
verborgen worden ist oder nicht.


Wird der Schwellenwertvergleich des Decodierverfahrens „symmetrisch“ zum
Schwellenwertvergleich des Codierverfahrens ausgeführt, gehen all diejenigen
Koeffizienten eines codierten Blocks in den Schwellenwertvergleich des
Decodierverfahrens ein, die vor dem Codieren modifizierbar sind und beim Codieren
modifiziert worden sein können. Aus welchen Koeffizienten die Menge dieser
Koeffizienten zusammengesetzt ist, muss auch dem Decodierer bekannt sein.


8.2.1 Merkmal M3.2.3Hi V ist bereits dann verwirklicht, wenn der Fachmann
typische Bildinhalte wie in Abschnitt III.4.2.2 a) beschrieben codiert und
anschließend dazu „symmetrisch“ decodiert.

                                       - 106 -



So werden bei dem aus Druckschrift NK 1 bekannten Codierverfahren
ausschließlich die Nicht-Null-Koeffizienten modifiziert. All diese sind aus Sicht des
Decodierers Koeffizienten, die modifiziert worden sein können.


In dem häufig vorkommenden Fall, dass in einem zu codierenden aktuellen Block
quantisierter Transformationskoeffizienten zwischen dem ersten und letzten von
null verschiedenen Koeffizienten keine Koeffizienten angeordnet sind, die den Wert
null haben (s. o., Abschnitt III.4.2.2 a)), beinhaltet ein derartiger Block genau eine
lückenlose Reihe von mindestens zwei Nicht-Null-Koeffizienten.


Insbesondere dann, wenn kein Nicht-Null-Koeffizient dieser Reihe von dem
Codierer modifiziert worden ist (weil die Parität der Summe dieser Koeffizienten der
Parität des verborgenen Vorzeichens bereits entspricht) oder durch eine
Modifikation den Wert null erhalten hat, gehen alle Koeffizienten dieser lückenlosen
Reihe in den „symmetrischen“ Schwellenwertvergleich des Decodierverfahrens ein.
Aus Sicht des Decodierers kann jeder dieser Nicht-Null-Koeffizienten modifiziert
worden sein.


In diesem Fall verwirklicht der Decodierer also Merkmal M3.2.3Hi V gemäß der ersten
Auslegungsvariante.


Dem steht nicht entgegen, dass genau einer der Nicht-Null-Koeffizienten der
lückenlosen Reihe von Nicht-Null-Koeffizienten durch eine Modifikation den Wert
null erhalten haben kann. In diesem Fall ist die vom Decodierer ermittelte Anzahl
von Koeffizienten, die modifiziert worden sein können, zwar um 1 kleiner als die
Anzahl von Koeffizienten, die in den Schwellenwertvergleich des Codierers eingeht.
Dadurch wird der im Rahmen des Decodierverfahrens durchgeführte Vergleich mit
einem Schwellenwert N (z. B. dem Wert N = 4) jedoch nur in dem Spezialfall
inkorrekt, wenn ein zu codierender Block eine lückenlose Reihe von N + 1 (z. B. von
5) Nicht-Null-Koeffizienten enthält. Der Fachmann wird auch in diesem Fall
selbstverständlich sicherstellen, dass das aus Druckschrift NK 1 bekannte

                                        - 107 -



Decodierverfahren zu keinen Decodierfehlern führt (z. B. dadurch, dass er bei der
Codierung keine Modifikationen von Koeffizienten zu null zulässt).


8.2.2 Außerdem wird Merkmal M3.2.3Hi V auch dann verwirklicht, wenn der
Fachmann ein Codier- und Decodierverfahren realisiert, bei dem Null-Koeffizienten
modifiziert werden können.


a)     Zieht der Fachmann nämlich ausgehend von dem in Druckschrift NK 1
beschriebenen Verfahren auch eine Modifikation von Null-Koeffizienten in Betracht,
bilden der erste von null verschiedene Koeffizient und alle darauffolgenden
Koeffizienten eines zu codierenden aktuellen Blocks eine Menge modifizierbarer
Koeffizienten, deren Anzahl in naheliegender Weise in den Schwellenwertvergleich
des Codierverfahrens eingeht (s. o., Abschnitt III.4.2.2 b)).


Da dem „symmetrisch“ zum Codierer arbeitenden Decodierer bekannt sein muss,
dass die Koeffizienten dieser Menge modifiziert worden sein können (s. o.), geht
dieselbe Anzahl von Koeffizienten in den „symmetrischen“ Schwellenwertvergleich
des   Decodierverfahrens      ein   wie    in     den   Schwellenwertvergleich   des
Codierverfahrens. Die Menge dieser Koeffizienten umfasst den ersten und letzten
von null verschiedenen Koeffizienten des zu decodierenden Blocks sowie ggf.
dazwischenliegende Koeffizienten, wie von Merkmal M3.2.3Hi V verlangt.


b)     Im Übrigen wäre es auch naheliegend, lückenlose Nullreihen am Ende einer
Partition von einer Modifikation auszunehmen (s. o., Abschnitt III.4.3.2). In diesem
Fall bestünde die Menge der Koeffizienten, die modifiziert worden sein können,
ausschließlich aus dem ersten und letzten von null verschiedenen Koeffizienten des
zu decodierenden Blocks sowie ggf. dazwischenliegenden modifizierbaren
Koeffizienten, so dass lückenlose Reihen von Null-Koeffizienten am Anfang und am
Ende einer Partition für den Schwellenwertvergleich nicht herangezogen werden.

                                      - 108 -



8.3    Mit Rücksicht auf die Ausführungen zum erteilten Patentanspruch 3 sowie zu
Patentanspruch 1 nach Hilfsantrag VII beruht die Lehre des Patentanspruchs 1
gemäß Hilfsantrag XII somit nicht auf einer erfinderischen Tätigkeit und ist daher
nicht patentfähig. Mit seinem Patentanspruch 1 fällt der gesamte Hilfsantrag XII.


8.4    Der jeweilige Gegenstand von Patentanspruch 1 in den Fassungen der
Hilfsanträge VIII bis XI geht inhaltlich nicht über den Gegenstand von
Patentanspruch 1 nach Hilfsantrag XII hinaus. Mit Rücksicht auf die Ausführungen
zu diesem Patentanspruch beruht der jeweilige Gegenstand des Patentanspruchs
1 in der Fassung eines der Hilfsanträge VIII bis XI daher nicht auf einer
erfinderischen Tätigkeit und ist somit ebenfalls nicht patentfähig. Mit ihrem
jeweiligen Patentanspruch 1 fallen auch die Hilfsanträge VIII bis XI jeweils als
Ganzes.




                                        IV.


Nachdem das Streitpatent aus den vorstehend ausgeführten Gründen in keiner
seiner durch die Beklagte verteidigten Fassungen Rechtsbestand haben kann, war
es somit für nichtig zu erklären.




                                        V.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                      - 109 -



                                        VI.

                             Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt schriftlich oder in elektronischer Form beim Bundesgerichtshof,
Herrenstraße 45a, 76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten.


Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des
angefochtenen Urteils vorgelegt werden.




Hartlieb     Dr. Forkel        Dr. Himmelmann        Dr. Städele         Dr. Harth
