---
ecli: "ECLI:DE:BPatG:2023:160323U2Ni39.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 39/21"
decided: "2023-03-16"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=7&nr=43699&anz=529&pos=108&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-03-16_2_Ni_39_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0081.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 39/21 vom 2023-03-16

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                      Verkündet am
                                                      16. März 2023
2 Ni 39/21 (EP)                                            …

(Aktenzeichen)


                     In der Patentnichtigkeitssache



…




ECLI:DE:BPatG:2023:160323U2Ni39.21EP.0

                                       -2-




              betreffend das europäische Patent EP 2 777 270
                             (DE 60 2012 010 809)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts aufgrund der
mündlichen Verhandlung vom 16. März 2023 durch die Vorsitzende Richterin
Hartlieb sowie die Richter Dipl.-Phys. Univ. Dr. Forkel, Dr. Himmelmann, Dipl.-Phys.
Univ. Dr. Städele und Dr.-Ing. Harth für Recht erkannt:


      I.      Das europäische Patent EP 2 777 270 wird mit Wirkung für das
              Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


      II.     Die Kosten des Rechtsstreits trägt die Beklagte.


      III.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des zu
              vollstreckenden Betrages vorläufig vollstreckbar.




                                 Tatbestand




Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in französischer Verfahrenssprache erteilten europäischen Patents EP 2 777 270
(deutsches Aktenzeichen DE 60 2012 010 809) (Streitpatent), das am 6. November
2012 angemeldet und am 16. September 2015 veröffentlicht worden ist und das die

                                          -3-



Bezeichnung „PROCÉDÉ DE CODAGE ET DÉCODAGE D’IMAGES, DISPOSITIF
DE    CODAGE          ET      DÉCODAGE        ET     PROGRAMMES            D’ORDINATEUR
CORRESPONDANTS“ (Verfahren zur Kodierung und Dekodierung von Bildern,
Anordnung       zur        Kodierung   und         Dekodierung      und        entsprechende
Computerprogramme) trägt. Das Streitpatent geht zurück auf die am 6. November
2012 angemeldete internationale Patentanmeldung PCT/FR2012/052552. Die
Anmeldung       wurde         am    16. Mai    2013         unter    der       internationalen
Veröffentlichungsnummer WO 2013/068684 A1 veröffentlicht. Nach Eintritt in die
europäische Phase wurde die Anmeldung unter der europäischen Anmeldenummer
12794438.7 als europäische Anmeldung geführt. Das Streitpatent nimmt die
Priorität FR 1160109 vom 7. November 2011 in Anspruch und betrifft im
Allgemeinen das Gebiet der Bildverarbeitung, genauer die Codierung und
Decodierung von digitalen Bildern und von Sequenzen digitaler Bilder (Abs. [0001]
Streitpatentschrift).


Das in vollem Umfang angegriffene Streitpatent umfasst 6 Patentansprüche,
darunter den auf ein „Verfahren zum Codieren wenigstens eines in Partitionen
unterteilten Bildes“ gerichteten Patentanspruch 1 und den nebengeordneten, auf ein
„Verfahren zum Decodieren eines Datensignals“ gerichteten Patentanspruch 3. Mit
dem nebengeordneten Patentanspruch 2 wird eine „Vorrichtung zum Codieren
wenigstens eines in Partitionen unterteilten Bildes“, mit dem nebengeordneten
Patentanspruch 4 eine „Vorrichtung zum Decodieren eines Datensignals“
beansprucht.      Der         nebengeordnete        Patentanspruch         5    betrifft   ein
„Rechnerprogramm, das Befehle enthält, um das Codierungsverfahren nach
Anspruch 1 auszuführen“. Der nebengeordnete Patentanspruch 6 betrifft
dementsprechend         ein    „Rechnerprogramm,      das     Befehle     enthält,   um    das
Decodierungsverfahren nach Anspruch 3 auszuführen“.

                                          -4-



Die Merkmale des erteilten Patentanspruchs 1 in der Originalfassung können wie
folgt gegliedert werden:


Patentanspruch 1:


          Anspruch 1                               Übersetzung
 M1.1     Procédé de codage d´au moins une Verfahren zum Codieren wenigstens
          image decoupée en partitions, ledit eines        in   Partitionen    unterteilten
          procédé mettant en oeuvre les étapes Bildes, wobei das Verfahren die
          de:                                      folgenden Schritte ausführt:
 M1.2     prédiction (C2) des données d´une Vorhersagen (C2) von Daten einer
          partition courante en fonction d´au aktuellen Partition in Abhängigkeit
          moins une partition de référence déjà von       wenigstens      einer         bereits
          codée puis décodée, délivrant une codierten und dann decodierten
          partition prédite;                       Referenzpartition,         was         eine
                                                   vorhergesagte Partition ergibt;
 M1.3     détermination (C6) d´un ensemble de Bestimmen (C6) einer Gesamtheit
          données résiduelles par comparaison von Restdaten durch Vergleichen
          de données relatives à la partition von        auf    die    aktuelle     Partition
          courante et à la partition prédite, bezogenen               Daten       mit      der
          lesdites données résiduelles étant vorhergesagten Partition, wobei die
          associées        respectivement       à Restdaten jeweils unterschiedlichen
          différentes informations numériques digitalen Informationen zugeordnet
          qui sont destinées à subir un codage sind, die dazu bestimmt sind, einer
          entropique,                              entropischen Codierung unterworfen
                                                   zu werden,
 M1.3.1 l´ensemble de données résiduelles wobei die Gesamtheit von Restdaten
          étant un bloc de données résiduelles, ein Block von Restdaten ist,
 M1.4     élaboration d´un signal contenant Erstellen eines Signals, das die
          lesdites informations codées,            codierten Informationen enthält,

                                      -5-



        ledit   procédé   de   codage    étant wobei      das     Codierungsverfahren
        caractérisé en ce qu´il met en dadurch gekennzeichnet ist, dass
        oeuvre, préalablement à ladite étape es vor dem Schritt des Erstellens des
        d´élaboration de signal, les étapes Signals        die    folgenden      Schritte
        suivantes:                            ausführt:
M1.5    détermination (C71), à partir dudit anhand der bestimmten Gesamtheit
        ensemble de données résiduelles von Restdaten Bestimmen (C71)
        déterminé, d´un sous-ensemble         einer Untergesamtheit,
M1.5.1 contenant des données résiduelles die Restdaten enthält, die modifiziert
        aptes á être modifiées,               werden können,
M1.5.2 le sous-ensemble contenant données wobei             die       Untergesamtheit
        résiduelles partant d´une première Restdaten enthält, die einer Liste
        donnée résiduelle non nulle á un von             Restdaten,        die     beim
        dernière donnée résiduelle non nulle Durchlaufen des Blocks in einer im
        parmi un liste de données résiduelles Voraus       definierten     Reihenfolge
        obtenu lors du parcours dans un erhalten wird, von einem ersten von
        ordre prédéfini dudit bloc,           null      verschiedenen       Restdatenelement zu einem letzten von null
                                              verschiedenen         Restdatenelement
                                              laufen,
M1.6    calcul (C8) de la valeur d´une fonction Berechnen (C8) des Wertes einer
        représentative de la parité de la Funktion, die die Parität der Summe
        somme     des données résiduelles der          Restdaten     der   bestimmten
        dudit sous-ensemble déterminé,        Untergesamtheit repräsentiert,
M1.7    comparaison (C9) de ladite valeur Vergleichen (C9) des berechneten
        calculée à la parité d´au moins une Wertes mit der Parität wenigstens
        desdites informations numériques,     einer der digitalen Informationen,
M1.7.1 ladite au moins une information wobei die wenigstens eine digitale
        numérique correspondant au signe Information dem Vorzeichen eines

                                            -6-



         d´une donnée résiduelle du sous- Restdatenelements                       der       Unterensemble,                                   gesamtheit entspricht,
M1.8     en fonction du résultat de ladite in Abhängigkeit vom Ergebnis des
         comparaison, modification (C10) ou Vergleichendes Modifizieren (C10)
         non d´au moins une des données oder nicht Modifizieren wenigstens
         résiduelles dudit sous-ensemble,            eines     Restdatenelements               der
                                                     Restdaten der Untergesamtheit,
M1.9     en cas de modification, codage im                   Fall       des       Modifizierens
         entropique (C20) de l´ensemble de entropisches Codieren (C20) der
         données        résiduelles    comprenant Gesamtheit von Restdaten, die das
         ladite    au     moins       une   donnée wenigstens            eine         modifizierte
         résiduelle modifiée sans ladite au Restdatenelement enthält, ohne die
         moins une information numérique.            wenigstens eine digitale Information.




Patentanspruch 2 lautet mit einer denkbaren Gliederung versehen:


          Anspruch 2                                 Übersetzung
M2.1      Dispositif de codage (CO) d´au Vorrichtung (CO) zum Codieren
          moins une image découpée en wenigstens                      eines      in    Partitionen
          partitions, ledit dispositif comprenant: unterteilten        Bildes,        wobei    die
                                                     Vorrichtung Folgendes umfasst:
M2.2      des     moyens        (PRED_CO)         de Mittel (PRED CO) zum Vorhersagen
          prédiction     des      données     d´une von Daten einer aktuellen Partition in
          partition courante en fonction d´au Abhängigkeit von wenigstens einer
          moins une partition de référence déjà bereits             codierten         und     dann
          codée puis décodée, délivrant une decodierten Referenzpartition, was
          partition prédite,                         eine vorhergesagte Partition ergibt,
M2.3      des     moyens       (MT_CO,      MQ_CO, Mittel (MT_CO, MQ_CO, ML_CO)
          ML_CO)        de   détermination     d´un zum Bestimmen einer Gesamtheit

                                         -7-



         ensemble de données résiduelles von Restdaten, die Daten, die auf die
         aptes à comparer des données aktuelle Partition bezogen sind, mit
         relatives à la partition courante et à la der    vorhergesagten                Partition
         partition prédite, lesdites données vergleichen              können,      wobei      die
         résiduelles       étant        associées Restdaten jeweils unterschiedlichen
         respectivement       à       différentes digitalen Informationen zugeordnet
         informations numériques qui sont sind, die dazu bestimmt sind, einer
         destinées     à   subir   un     codage entropischen Codierung unterworfen
         entropique,                               zu werden,
M2.3.1   l´ensemble de données résiduelles wobei die Gesamtheit von Restdaten
         étant un bloc de données résiduelles, ein Block von Restdaten ist,
M2.4     des moyens (CF) d´élaboration d´un Mittel (CF) zum Erstellen eines
         signal        contenant          lesdites Signals,         dass    die         codierten
         informations codées,                      Informationen enthält,
         ledit dispositif de codage étant wobei               die     Codierungsvorrichtung
         caractérisé en ce qu´il comprend, dadurch gekennzeichnet ist, dass
         en       amont     desdits      moyens sie           den          Erstellungsmitteln
         d´élaboration,    des     moyens      de vorgeschaltete Verarbeitungsmittel
         traitement (MTR_CO) qui sont aptes (MTR_CO)                  umfasst,     die      dafür
         à:                                        ausgelegt sind:
M2.5     déterminer, à partir dudit ensemble anhand der bestimmten Gesamtheit
         de données résiduelles déterminé, von Restdaten eine Untergesamtheit
         d´un sous-ensemble                        zu bestimmen,
M2.5.1   contenant des données résiduelles die Restdaten enthält, die modifiziert
         aptes à être modifiées,                   werden können,
M2.5.2   le       sous-ensemble         contenant wobei             die     Untergesamtheit
         données résiduelles partant d´une Restdaten enthält, die in einer Liste
         première donnée résiduelle non nulle von             Restdaten,          die       beim
         à un dernière donnée résiduelle non Durchlaufen des Blocks in einer im
         nulle parmi un liste des données Voraus                definierten       Reihenfolge

                                           -8-



         résiduelles obtenu lors du parcours erhalten werden, von einem ersten
         dans un ordre prédéfini dudit bloc,          von null verschiedenen Restdatenelement zu einem letzten von null
                                                      verschiedenen       Restdatenelement
                                                      laufen,
M2.6     calculer la valeur d´une fonction den               Wert      einer        Funktion     zu
         représentative de la parité de la bestimmen, die die Parität der
         somme des données résiduelles Summe                        der    Restdaten            der
         dudit sous-ensemble déterminé,               bestimmten               Untergesamtheit
                                                      repräsentiert,
M2.7     comparer ladite valeur calculée à la den berechneten Wert mit der Parität
         parité d´au moins une desdites wenigstens                     einer        der    digitalen
         informations numériques,                     Informationen zu vergleichen,
M2.7.1   ladite au moins une information wobei die wenigstens eine digitale
         numérique correspondant au signe Information dem Vorzeichen eines
         d´une donnée résiduelle du sous- Restdatenelements                          der     Unterensemble,                                    gesamtheit entspricht,
M2.8     modifier ou non au moins une des in Abhängigkeit vom Ergebnis des
         données       résiduelles    dudit    sous- Modifizierens wenigstens eines der
         ensemble déterminé, en fonction du Restdatenelemente der bestimmten
         résultat de ladite modification,             Untergesamtheit          zu     modifizieren
                                                      oder nicht zu modifizieren,
M2.9     ainsi que des moyens (CE_CO) de sowie Mittel (CE_CO) umfasst, um
         codage entropique de l´ensemble de im Fall des Modifizierens durch die
         données       résiduelles    comprenant Verarbeitungsmittel die Gesamtheit
         ladite   au     moins       une      donnée von Restdaten, die das wenigstens
         résiduelle     modifiée,    en    cas    de eine modifizierte Restdatenelement
         modification par lesdits moyens de enthält, ohne die wenigstens eine
         traitement sans ladite au moins une digitale Information entropisch zu
         information numérique.                       codieren.

                                                -9-



Patentanspruch 3 des Streitpatents lautet in gegliederter Form wie folgt:


          Anspruch 3                                    Übersetzung
 M3.1     Procédé de décodage d´un signal de Verfahren zum Decodieren eines
          données (F) représentatif d´au moins Datensignals (F), dass wenigstens
          une image découpée en partitions qui ein in Partitionen unterteiltes Bild
          a       été    précédemment           codée, repräsentiert, das vorher codiert
          comprenant                                    worden ist, umfassend
 M3.2     une étape d´obtention (D2), par einen Schritt (D2) des Erhaltens
          décodage entropique de données durch entropisches Decodieren von
          dudit         signal,        d´informations Daten des Signals von digitalen
          numériques                                    Informationen,
 M3.2.1 associées à des données résiduelles die Restdaten zugeordnet sind, die
          relatives à au moins une partition auf wenigstens eine früher codierte
          précédemment codée,                           Partition bezogen sind,
 M3.2.2 les        données        résiduelles     étant wobei die Restdaten in einem Block
          arrangées en un bloc de données von Restdaten angeordnet sind,
          résiduelles,
          ledit procédé de décodage étant               wobei das Decodierungsverfahren
          caractérisé en ce qu´il comprend les dadurch gekennzeichnet ist, dass
          étapes suivantes:                             es die folgenden Schritte umfasst:
 M3.3     détermination,      à     partir   desdites anhand der Restdaten Bestimmen
          données       résiduelles,    d´un     sous- einer Untergesamtheit,
          ensemble
 M3.3.1 contenant des données résiduelles die Restdaten enthält, die während
          aptes à avoir été modifiées au cours einer           vorhergehenden     Codierung
          d´un codage précédent,                        modifiziert worden sein können,
 M3.3.2 le sous-ensemble contenant données wobei                   die     Untergesamtheit
          résiduelles partant d´une première Restdaten              aus   einer Liste     von
          donnée résiduelle non nulle à un Restdaten, die beim Durchlaufen

                                        - 10 -



          dernière donnée résiduelle non nulle des Blocks in einer im Voraus
          parmi un liste de données résiduelles definierten    Reihenfolge      erhalten
          obtenu lors du parcours dans un wird, enthält, die von einem ersten
          ordre prédéfini dudit bloc,            von null verschiedenen Restdatenelement zu einem letzten von null
                                                 verschiedenen     Restdatenelement
                                                 laufen,
 M3.4     calcul (D5) de la valeur d´une fonction Berechnen (D5) des Wertes einer
          représentative de la parité de la Funktion, die die Parität der Summe
          somme      des données résiduelles der       Restdaten    der    bestimmten
          dudit sous-ensemble déterminé,         Untergesamtheit repräsentiert,
 M3.5     reconstruction à partir de ladite parité anhand der berechneten Parität
          calculée                               Rekonstruieren
 M3.5.1 d´une valeur du signe d´une donnée eines Wertes des Vorzeichens eines
          résiduelle du sous-ensemble.           Restdatenelements        der    Untergesamtheit.




Der mit einer Merkmalsgliederung versehene Patentanspruch 4 des Streitpatents
lautet:


          Anspruch 4                             Übersetzung
 M4.1     Dispositif (DO) de décodage d´un Vorrichtung (DO) zum Decodieren
          signal de données représentatif d´au eines Datensignals, das wenigstens
          moins une image découpée en ein in Partitionen unterteiltes Bild
          partitions qui a été précédemment repräsentiert, das vorher codiert
          codée, comprenant des moyens worden ist, die Mittel (DE_DO)
          (DE_DO)                                umfasst,

                                          - 11 -



M4.2     d´obtention,          par       décodage um durch entropisches Decodieren
         entropique de données dudit signal, von Daten des Signals digitale
         d´informations numériques                  Informationen zu erhalten,
M4.2.1   associées à des données résiduelles die Restdaten zugeordnet sind, die
         relatives à au moins une partition auf wenigstens eine vorher codierte
         précédemment codée,                        Partition bezogen sind,
M4.2.2   les   données         résiduelles    étant wobei die Restdaten in einem Block
         arrangées en un bloc de données von Restdaten angeordnet sind,
         résiduelles,
         ledit dispositif de décodage étant wobei die Decodierungsvorrichtung
         caractérisé en ce qu´il comprend dadurch gekennzeichnet ist, dass
         des     moyens          de      traitement sie Verarbeitungsmittel (MTR_DO)
         (MTR_DO) qui sont aptes à:                 umfasst, die dafür ausgelegt sind:
M4.3     déterminer,       à    partir    desdites anhand      der    Restdaten       eine
         données        résiduelles,     un   sous- Untergesamtheit zu bestimmen,
         ensemble
M4.3.1   contenant des données résiduelles die Restdaten enthält, die während
         aptes à avoir été modifiées au cours einer vorhergehenden Codierung
         d´un codage précédent,                     modifiziert worden sein können,
M4.3.2   le    sous-ensemble             contenant wobei       die     Untergesamtheit
         données résiduelles partant d´une Restdaten            aus einer Liste von
         première donnée résiduelle non nulle Restdaten, die beim Durchlaufen
         à un dernière donnée résiduelle non des Blocks in einer im Voraus
         nulle parmi un liste de données definierten             Reihenfolge     erhalten
         résiduelles obtenu lors du parcours wird, enthält, die von einem ersten
         dans un ordre prédéfini dudit bloc,        von null verschiedenen Restdatenelement zu einem letzten von null
                                                    verschiedenen     Restdatenelement
                                                    laufen,

                                       - 12 -



 M4.4     calculer la valeur d´une fonction den         Wert      einer      Funktion     zu
          représentative de la parité de la berechnen,          die    die    Parität    der
          somme des données résiduelles Summe                  der     Restdaten         der
          dudit sous-ensemble déterminé,         bestimmten Untergesamtheit repräsentiert,
 M4.5     reconstruction à partir de ladite parité anhand der berechneten Parität
          calculée,
 M4.5.1   d´une valeur du signe d´une donnée einen Wert des Vorzeichens eines
          résiduelle du sous-ensemble.           Restdatenelements           der    Untergesamtheit zu rekonstruieren.




Patentanspruch 5 des Streitpatents lautet mit einer denkbaren Gliederung:


          Anspruch 5                             Übersetzung
 M5.1     Programme d´ordinateur comportant Rechnerprogramm,                 das   Befehle
          des instructions pour mettre en enthält,           um       das     Codierungsoeuvre le procédé de codage selon verfahren           nach        Anspruch      1
          la revendication 1,                    auszuführen,
 M5.2     lorsque ledit procédé de codage est wenn das Codierungsverfahren auf
          exécuté sur un ordinateur.             einem Rechner ausgeführt wird.




Patentanspruch 6 des Streitpatents lautet:


          Anspruch 6                             Übersetzung
 M6.1     Programme d´ordinateur comportant Rechnerprogramm,                 das   Befehle
          des instructions pour mettre en enthält,                     um                das
          oeuvre le procédé de décodage Decodierungsverfahren                           nach
          selon la revendication 3,              Anspruch 3 auszuführen,

                                       - 13 -



 M6.2     lorsque ledit procédé de décodage wenn das Decodierungsverfahren
          est exécuté sur un ordinateur.          auf einem Rechner ausgeführt wird.




Die Klägerin stützt ihre Klage auf den Nichtigkeitsgrund der mangelnden
Patentfähigkeit mit Blick auf fehlende erfinderische Tätigkeit, den Nichtigkeitsgrund
der unzureichenden Offenbarung und den Nichtigkeitsgrund der unzulässigen
Erweiterung.


Zur Stützung ihres Vorbringens hat die Klägerin die folgenden Dokumente genannt:


NKA                  Verletzungsklage Landgericht München (D…
                     AB gegen T… GmbH);
NKI                  Streitpatent EP 2 777 270 B1;
NKI-DE               deutsche Übersetzung der Patentschrift EP 2 777 270 B1;
NKII                 Registerauszug zum Aktenzeichen 60 2012 010 809.6
                     (Stand am 11. Oktober 2021);
NKIII                Merkmalsgliederung der Patentansprüche 1 bis 4 des
                     Streitpatents;
NKIV                 WO 2013/068684 A1;
NKIV-DE              deutsche Maschinenübersetzung der WO 2013/068684 A1;
NKV                  Änderungen der erteilten Ansprüche gegenüber den
                     ursprünglichen Ansprüchen;
NK1                  Thiesse, Jean-Marc et al.: „Rate Distortion Data Hiding of
                     motion Vector Competition Information in Chroma and Luma
                     Samples for Video Compression“, IEEE Transactions on
                     circuits and systems for video technology, Vol. 21, No. 6,
                     June 2011;
NK2                  Thiesse, Jean-Marc et al.: „Data Hiding of Intra Prediction
                     Information in Chroma Samples for Video Compression”. In:

                           - 14 -



       2010 IEEE International Conference on Image Processing,
       26.-29. Sept. 2010;
NK3    Esen, Erin et al.: „Robust Video Data Hiding Using Forbidden
       Zone Data Hiding and Selective Embedding“, IEEE
       Transactions on circuits and systems for video technology,
       Vol. 21, No. 8, August 2011;
NK4    Paruchuri, Jithendra K. Et al.: „Joint Optimization of Data
       Hiding and Video Compression“;
NK5    Bossen, Frank et al.: „Video Coding using a Simplified Block
       Structure and Advanced Coding Techniques”. In: IEEE
       transactions on circuits and systems for video technology 20,
       Nr.12 (2010); S. 1667-1675;
NK6    Cohen, Robert et al.: „Low Complexity Embedding of
       Information in Transform Coefficients”. In: JCTVC-E428 r2,
       5th JCTVC Meeting 2011;
NK7    Marpe, Detlev et al.: „The H.264/MPEG4 Advanced Video
       Coding Standard and its Applications“, Standards Report,
       IEEE Communications Magazine, August 2006;
NK8    Wang, Yao et al.: „Video Processing and Communications“,
       Prentice Hall, Signal Processing Series;
NK9    Lee, Jinho et al.: „Mode dependent filtering for intra predicted
       sample“. In: JCTVC-F358, 6th JCTVC Meeting 2011;
NK9´   Bross, Benjamin et al.: „WD4: Working Draft 4 of High-Efficiency Video Coding”. In: JCTVC-F803_d5, 6th JVT-VC
       Meeting, Torino, Italy, 14-22 July, 2011;
NK10   Amonou, Isabelle et al.: „Description of video coding
       technology proposal by France Telecom, NTT, NTT
       DOCOMO, Panasonic and Technicolor“, Doc. Nr. JCTVC-A114, April 2010.

                                        - 15 -



Die Klägerin stellt den Antrag,
             das europäische Patent EP 2 777 270 mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für
             nichtig zu erklären.


Die Beklagte stellt den Antrag,
             die Klage abzuweisen,
             hilfsweise
             das europäische Patent EP 2 777 270 unter Klageabweisung im
             Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik
             Deutschland insoweit für nichtig zu erklären, als es über die Fassung
             eines der Hilfsanträge I bis IV vom 2. Januar 2023 – in dieser
             Reihenfolge – hinausgeht.


Die Beklagte tritt der Argumentation der Klägerin in allen wesentlichen Punkten
entgegen. Sie vertritt die Auffassung, dass die beanspruchte Lehre ursprünglich
offenbart sei, ausführbar sei und auf einer erfinderischen Tätigkeit des Fachmanns
beruhe. Die beanspruchte Lehre sei jedenfalls in einer der Fassungen der
Hilfsanträge patentfähig.


Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:


NB1        Urteil aus dem Nichtigkeitsverfahren 2 Ni 6/21 (EP);
NB2        „Advanced video coding forgeneric audiovisual services”. ITU-T H.264,
           Series H: Audiovisual and Multimedia Systems – Infrastructure of
           audiovisual services – Coding of moving video, 06/2011.


Die Beklagte hat in der mündlichen Verhandlung am 16. März 2023 erklärt, dass sie
die   Patentansprüche       gemäß   Hauptantrag   und   Hilfsanträgen   als   jeweils
geschlossene Anspruchssätze ansehe, die jeweils insgesamt beansprucht würden.

                                       - 16 -



Hilfsantrag I vom 2. Januar 2023 lautet:

- 17 -

- 18 -

- 19 -

                                       - 20 -



Hilfsantrag II vom 2. Januar 2023 lautet:

- 21 -

- 22 -

- 23 -

                                       - 24 -



Hilfsantrag III vom 2. Januar 2023 lautet:

- 25 -

- 26 -

- 27 -

                                      - 28 -



Hilfsantrag IV vom 2. Januar 2023 lautet:

- 29 -

- 30 -

                                     - 31 -




Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                           - 32 -



                                Entscheidungsgründe


Die Klage, mit der der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6     Abs. 1 Satz 1    Nr.   1 IntPatÜbkG   i. V. m.   Art. 138   Abs. 1 lit. a)
EPÜ i. V. m. Art. 52 und 56 EPÜ, der Nichtigkeitsgrund der unzureichenden
Offenbarung nach Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜG, Art. 138 Abs. 1 lit. b)
EPÜ i. V. m. Art. 83 EPÜ und der Nichtigkeitsgrund der unzulässigen Erweiterung
nach Art. II § 6 Abs. 1 Satz 1 Nr. 3 IntPatÜG, Art. 138 Abs. 1 lit. c) EPÜ i. V. m.
Art. 100 lit. c) EPÜ geltend gemacht wird, ist nach § 81 PatG zulässig.


Die Klage ist auch begründet. Das Streitpatent hat weder hinsichtlich des
Hauptantrags noch hinsichtlich der Hilfsanträge Bestand, weil den Patentansprüchen
des Streitpatents gemäß Hauptantrag und Hilfsanträgen der Nichtigkeitsgrund der
fehlenden Patentfähigkeit entgegensteht und das Streitpatent deshalb für nichtig zu
erklären ist.




                                             I.




1.     Das Streitpatent betrifft die Codierung von digitalen Bildern und Sequenzen
digitaler Bilder bzw. von Bewegtbildern (Videos) in einen Daten- bzw. Bitstrom für
die Übertragung an einen Empfänger sowie die entsprechende Decodierung
(Streitpatentschrift, Abs. [0001]). Insbesondere befasst sich das Streitpatent mit der
Einsparung von Bits in dem Bitstrom durch „Verstecken“ bestimmter Daten,
vorliegend eines Vorzeichens, in einem Wert einer Funktion von Daten, die in dem
Bitstrom codiert sind (Streitpatentschrift, Abs. [0059] bis [0063]).


Das Streitpatent geht aus von der digitalen Videocodierung, wie sie beispielsweise
aus den Standards MPEG oder H.264 bekannt ist. Die Videobilder sind in
Makroblöcke unterteilt, wobei jeder Makroblock wiederum in Blöcke unterteilt ist und

                                         - 33 -



jeder Block eine Mehrzahl von Bildpixeln beinhaltet. Die resultierenden Blöcke
werden dann einzeln unter Anwendung von Intra- oder Inter-Prädiktion
weiterverarbeitet, mit dem Ziel, für den aktuell zu codierenden Block die
Unterschiede zu einem Vorhersage- bzw. Prädiktionsblock zu bestimmen und nur
diese im Datenstrom zu codieren (vgl. Streitpatentschrift, Abs. [0003]). Für den zu
codierenden Block im aktuellen Bild stellt ein solcher Prädiktionsblock einen
möglichst ähnlichen Block entweder in demselben Bild oder in einem anderen
Referenzbild dar. Für jeden Block wird ein Restblock ermittelt, der die Differenz
zwischen dem zu codierenden Block und seinem Prädiktionsblock angibt, den
sogenannten Prädiktionsfehler. Die Restblöcke werden in den Frequenzraum
transformiert (z. B. mittels einer diskreten Kosinustransformation), d. h. die
jeweiligen Pixelwerte der Restblöcke werden in Transformationskoeffizienten
übersetzt, die dann noch quantisiert werden können. Anschließend werden die
Koeffizienten in einer Zick-Zack-Reihenfolge ausgelesen und dadurch in einer
eindimensionalen Liste, dem quantisierten Rest, angeordnet, an dessen Ende
wünschenswerterweise einige Koeffizienten gleich Null sind. Die Koeffizienten
können ein positives oder negatives Vorzeichen haben. Bei der weiteren Codierung
wird   der      quantisierte   Rest   einer    Entropiecodierung   unterzogen   (vgl.
Streitpatentschrift, Abs. [0004]).


Gemäß Streitpatent sind für die quantisierten Transformationskoeffizienten die
folgenden Informationen vorgesehen (vgl. Streitpatentschrift, Abs. [0005]):


   ·   Ein Datenelement, das den letzten von Null verschiedenen Koeffizienten der
       Liste angibt;
   ·   Für alle Koeffizienten bis zum letzten von Null verschiedenen Koeffizienten
       eine Information, die angibt, ob ein Koeffizient von Null verschieden ist oder
       nicht;
   ·   Eine Information, die für jeden von Null verschiedenen Koeffizienten angibt,
       ob dieser gleich Eins ist oder nicht;

                                           - 34 -



   ·   Ein Datenelement, das für jeden Koeffizienten ungleich Null mit Betrag
       ungleich 1 dessen Betrag abzüglich zwei angibt.
   ·   Eine Information, die für jeden von Null verschiedenen Koeffizienten sein
       Vorzeichen angibt. 0 zeigt ein positives Vorzeichen und 1 ein negatives
       Vorzeichen an.


Neben den Transformationskoeffizienten, die die Bildinformation darstellen, werden
Zusatzinformationen codiert, die die Art der Codierung eines Blocks betreffen, z. B.
der Modus der Prädiktion (Inter- oder Intra-Prädiktion) oder das verwendete
Transformationsverfahren      (z.    B.   diskrete   Kosinustransformation).   Codierte
Bilddaten und Zusatzinformationen bilden den codierten Datenstrom, der es dem
Decoder erlaubt, das ursprünglich codierte Bild zu rekonstruieren (vgl.
Streitpatentschrift, Abs. [0006]).


Um das Volumen der codierten Daten weiter zu verringern, ist aus dem Stand der
Technik ein Verfahren zum sogenannten „Verbergen von Daten“ („Data Hiding“)
bekannt (vgl. Streitpatentschrift, Abs. [0010]). Dieses erlaubt, die Codierung einer
einzelnen, als separates Syntaxelement des Bitstroms vorliegenden Information
einzusparen. Stattdessen wird eine solche Information (z. B. ein Bit mit dem Wert 1
bzw. 0) in der Parität der Summe der Beträge der Transformationskoeffizienten
„versteckt“, d. h. implizit ausgedrückt. Dabei meint Parität die Eigenschaft einer
ganzen Zahl, gerade oder ungerade zu sein. Eine gerade Summe (gerade Parität)
der Beträge stellt eine 0 dar, eine ungerade Summe eine 1 (vgl. Streitpatentschrift,
Abs. [0011]). Die Parität der Summe der Beträge kann dem zu repräsentierenden
Wert 0 oder 1 entweder entsprechen oder nicht. In letzterem Fall ist es notwendig,
den Betrag mindestens eines Transformationskoeffizienten zu modifizieren, damit
eine ungerade Summe der Transformationskoeffizienten gerade wird oder
umgekehrt. Der Decodierer bestimmt dann die Parität der Summe der aus dem
Bitstrom erhaltenen Beträge und erhält dadurch den „versteckten“ Wert 0 oder 1.
Während einerseits das Verstecken von einem Bit eine Datenersparnis mit sich
bringt, hat andererseits das Modifizieren quantisierter Transformationskoeffizienten

                                         - 35 -



eine Verzerrung der codierten Bildinformationen im Verhältnis zum Originalbild zur
Folge. In welchem Maß eine solche Verzerrung die Bildqualität des codierten
Videobildes beeinträchtigt, kann von der Wahl des oder der zu modifizierenden
Transformationskoeffizienten abhängen.


Laut Abs. [0011] der Streitpatentschrift braucht bei diesem bekannten Verfahren der
sog. MVComp-Index nicht explizit in das codierte Datensignal geschrieben zu
werden, sondern seine Information kann durch die Parität der Summe der
Koeffizienten des quantifizierten Rests transportiert werden. Der MVComp-Index
stellt   ein   Informationselement   dar,   das   ermöglicht,   den   Prädiktor   der
Vektorbewegung zu identifizieren, der für einen Block verwendet wird, der im Inter-Prädiktionsmodus vorhergesagt wird, und kann den Wert 0 oder 1 annehmen. Wenn
in diesem Schritt der Codierung die Parität der Summe der Koeffizienten des
quantifizierten Rests schon derjenigen des MVComp-Index entspricht, braucht
nichts weiter unternommen zu werden. Wenn sich diese Parität jedoch von der
Parität des Index unterscheidet, muss eine Modifikation von Daten des
quantifizierten Rests durchgeführt werden, um eine Übereinstimmung der Paritäten
zu erreichen; eine Möglichkeit besteht darin, einen oder mehrere Koeffizienten des
quantifizierten Rests mit einem ungeraden Wert (z. B. +1, -1, +3, -3, +5, -5 …) zu
inkrementieren oder zu dekrementieren. Danach entspricht die Parität der
Koeffizientensumme dem Index. Entsprechend Abs. [0012] der Streitpatentschrift
wird im Decodierer der MVComp-Index in dem an den Decodierer übertragenen
Signal nicht gelesen. Für den Decodierer reicht es aus, den Rest auf herkömmliche
Weise zu bestimmen. Wenn die Summe der Koeffizienten dieses Rests gerade ist,
wird der MVComp-Index auf 0 gesetzt. Wenn er ungerade ist, wird der MVComp-Index auf 1 gesetzt. Auf diese Weise wird der MVComp-Index also „verborgen“ und
dem Decodierer indirekt übermittelt.


2.       Vor diesem Hintergrund kritisiert das Streitpatent, dass die gemäß dem Stand
der Technik zu modifizierenden Transformationskoeffizienten nicht immer optimal
ausgewählt werden. Als Folge ruft die angewendete Modifikation in dem an den

                                           - 36 -



Decodierer übertragenen Signal Störungen hervor. Dies kann sich nachteilig auf die
Effektivität der Videokompression auswirken (vgl. Streitpatentschrift, Abs. [0013]).


Ausgehend von diesem Stand der Technik macht es sich das Streitpatent zur
Aufgabe, diesem Nachteil durch Angabe eines verbesserten Codier- und
Decodierverfahrens abzuhelfen (vgl. Streitpatentschrift, Abs. [0016]). Dabei soll die
Wahl der zu modifizierenden Transformationskoeffizienten möglichen Störungen
und Abstimmungsproblemen zwischen Codierer und Decodierer entgegenwirken
(vgl. Streitpatentschrift, Abs. [0019], [0020]). Außerdem soll sich die Auswahl zu
versteckender Parameter günstig auf die Rate-Verzerrung-Optimierung auswirken
(vgl. Streitpatentschrift, Abs. [0024]).


3.      Die oben genannte Aufgabe soll erfindungsgemäß gelöst werden durch ein
„Verfahren zum Codieren wenigstens eines in Partitionen unterteilten Bildes“ nach
Patentanspruch 1, eine „Vorrichtung zum Codieren wenigstens eines in Partitionen
unterteilten Bildes“ nach Patentanspruch 2, ein „Verfahren zum Decodieren eines
Datensignals“ nach Patentanspruch 3 und eine „Vorrichtung zum Decodieren eines
Datensignals nach Patentanspruch 4 sowie ein „Rechnerprogramm, das Befehle
enthält, um das Codierungsverfahren nach Anspruch 1 auszuführen“ nach
Patentanspruch 5 bzw. ein „Rechnerprogramm, das Befehle enthält, um das
Decodierungsverfahren nach Anspruch 3 auszuführen“ nach Patentanspruch 6.


Die Merkmale des erteilten Patentanspruchs 1 können wie folgt gegliedert werden
(mit Rechtschreibkorrekturen und teilweise verbesserter Übersetzung):


Patentanspruch 1:


           Anspruch 1                               Übersetzung
 M1.1      Procédé de codage d´au moins une Verfahren zum Codieren wenigstens
           image découpée en partitions, ledit eines      in   Partitionen   unterteilten

                                      - 37 -



       procédé mettant en oeuvre les étapes Bildes, wobei das Verfahren die
       de:                                       folgenden Schritte ausführt:
M1.2   prédiction (C2) des données d´une Vorhersagen (C2) von Daten einer
       partition courante en fonction d´au aktuellen Partition in Abhängigkeit
       moins une partition de référence déjà von        wenigstens         einer     bereits
       codée puis décodée, délivrant une codierten und dann decodierten
       partition prédite;                        Referenzpartition,         was        eine
                                                 vorhergesagte Partition ergibt;
M1.3   détermination (C6) d´un ensemble          Bestimmen (C6) einer Gesamtheit
       de données résiduelles par                von Restdaten durch Vergleichen
       comparaison de données relatives à        von auf die aktuelle Partition und die
       la partition courante et à la partition   vorhergesagte Partition bezogenen
       prédite, lesdites données résiduelles     Datenmit           der   vorhergesagten
       étant associées respectivement à          Partition,     wobei     die     Restdaten
       différentes informations numériques       jeweils unterschiedlichen digitalen
       qui sont destinées à subir un codage      Informationen zugeordnet sind, die
       entropique,                               dazu         bestimmt      sind,     einer
                                                 entropischen
                                                 CodierungEntropiecodierung
                                                 unterworfen zu werden,
M1.3.1 l´ensemble de données résiduelles wobei die Gesamtheit von Restdaten
       étant un bloc de données résiduelles, ein Block von Restdaten ist,
M1.4   élaboration d´un signal contenant Erstellen eines Signals, das die
       lesdites informations codées,             codierten Informationen enthält,
       ledit   procédé      de   codage   étant wobei        das     Codierungsverfahren
       caractérisé en ce qu´il met en dadurch gekennzeichnet ist, dass
       oeuvre, préalablement à ladite étape es vor dem Schritt des Erstellens des
       d´élaboration de signal, les étapes Signals            die     folgenden     Schritte
       suivantes:                                ausführt:

                                       - 38 -



M1.5    détermination (C71), à partir dudit anhand der bestimmten Gesamtheit
        ensemble de données résiduelles von Restdaten Bestimmen (C71)
        determiné, d´un sous-ensemble           einer Untergesamtheit,
M1.5.1 contenant des données résiduelles die Restdaten enthält, die modifiziert
        aptes á être modifiées,                 werden können,
M1.5.2 le sous-ensemble contenant données wobei             die       Untergesamtheit
        résiduelles partant d´une première Restdaten enthält, dieaus einer Liste
        donnée résiduelle non nulle á une von Restdaten enthält, die beim
        dernière donnée résiduelle non nulle Durchlaufen des Blocks in einer im
        parmi    une    liste     de   données Voraus      definierten       Reihenfolge
        résiduelles obtenue lors du parcours erhalten wirdworden ist, und die
        dans un ordre prédéfini dudit bloc,     Restdaten der Untergesamtheit von
                                                einem ersten von null verschiedenen
                                                Restdatenelement       der     Liste    zu
                                                einem       letzten         von        null
                                                verschiedenen       Restdatenelement
                                                der Liste laufen,
M1.6    calcul (C8) de la valeur d´une fonction Berechnen (C8) des Wertes einer
        représentative de la parité de la Funktion, die die Parität der Summe
        somme    des données résiduelles der          Restdaten       der    bestimmten
        dudit sous-ensemble déterminé,          Untergesamtheit repräsentiert,
M1.7    comparaison (C9) de ladite valeur Vergleichen (C9) des berechneten
        calculée à la parité d´au moins une Wertes mit der Parität wenigstens
        desdites informations numériques,       einer der digitalen Informationen,
M1.7.1 ladite au moins une information wobei die wenigstens eine digitale
        numérique correspondant au signe Information dem Vorzeichen eines
        d´une donnée résiduelle du sous- Restdatenelements                             der
        ensemble,                               Untergesamtheit entspricht,
M1.8    en fonction du résultat de ladite in Abhängigkeit vom Ergebnis des
        comparaison, modification (C10) ou Vergleichsendes Modifizieren (C10)

                                            - 39 -



         non d´au moins une des données oder Nicht-Modifizieren wenigstens
         résiduelles dudit sous-ensemble,               eines     Restdatenelements                der
                                                        Restdaten der Untergesamtheit,
M1.9     en cas de modification, codage im                      Fall       des       Modifizierens
         entropique (C20) de l´ensemble de entropisches
         données        résiduelles    comprenant CodierenEntropiecodieren (C20) der
         ladite    au     moins       une    donnée Gesamtheit von Restdaten, die das
         résiduelle modifiée sans ladite au wenigstens                      eine         modifizierte
         moins une information numérique.               Restdatenelement enthält, ohne die
                                                        wenigstens eine digitale Information.




Patentanspruch 2 gemäß Hauptantrag lautet (mit Korrekturen):


         Anspruch 2                                     Übersetzung
M2.1     Dispositif de codage (CO) d´au Vorrichtung (CO) zum Codieren
         moins une image découpée en wenigstens                          eines      in    Partitionen
         partitions, ledit dispositif comprenant: unterteilten            Bildes,        wobei     die
                                                        Vorrichtung Folgendes umfasst:
M2.2     des      moyens       (PRED_CO)             de Mittel (PRED CO) zum Vorhersagen
         prédiction      des      données      d´une von Daten einer aktuellen Partition in
         partition courante en fonction d´au Abhängigkeit von wenigstens einer
         moins une partition de référence déjà bereits                 codierten         und     dann
         codée puis décodée, délivrant une decodierten Referenzpartition, was
         partition prédite,                             eine vorhergesagte Partition ergibt,
M2.3     des      moyens      (MT_CO,       MQ_CO, Mittel (MT_CO, MQ_CO, ML_CO)
         ML_CO)         de   détermination      d´un zum Bestimmen einer Gesamtheit
         ensemble de données résiduelles von Restdaten, die Daten, die auf die
         aptes à comparer des données aktuelle                          Partition         und      die
         relatives à la partition courante et à la vorhergesagte             Partition         bezogen

                                         - 40 -



         partition prédite, lesdites données sind,            mit     der      vorhergesagten
         résiduelles       étant        associées Partition vergleichen können, wobei
         respectivement       à       différentes besagte             Restdaten             jeweils
         informations numériques qui sont unterschiedlichen                                digitalen
         destinées     à   subir   un     codage Informationen zugeordnet sind, die
         entropique,                                  dazu     bestimmt            sind,      einer
                                                      entropischen
                                                      CodierungEntropiecodierung
                                                      unterworfen zu werden,
M2.3.1   l´ensemble de données résiduelles wobei die Gesamtheit von Restdaten
         étant un bloc de données résiduelles, ein Block von Restdaten ist,
M2.4     des moyens (CF) d´élaboration d´un Mittel (CF) zum Erstellen eines
         signal        contenant          lesdites Signals,         dass      die      codierten
         informations codées,                         Informationen enthält,
         ledit dispositif de codage étant wobei               die     Codierungsvorrichtung
         caractérisé en ce qu´il comprend, dadurch gekennzeichnet ist, dass
         en       amont     desdits      moyens sie           den            Erstellungsmitteln
         d´élaboration,    des     moyens         de vorgeschaltete Verarbeitungsmittel
         traitement (MTR_CO) qui sont aptes (MTR_CO)                  umfasst,        die     dafür
         à:                                           ausgelegt sind:
M2.5     déterminer, à partir dudit ensemble anhand der bestimmten Gesamtheit
         de données résiduelles déterminé, von Restdaten eine Untergesamtheit
         d´un sous-ensemble                           zu bestimmen,
M2.5.1   contenant des données résiduelles die Restdaten enthält, die modifiziert
         aptes à être modifiées,                      werden können,
M2.5.2   le       sous-ensemble         contenant wobei             die       Untergesamtheit
         données résiduelles partant d´une Restdaten enthält, die inaus einer
         première donnée résiduelle non nulle Liste von Restdaten enthält, die
         à une dernière donnée résiduelle non beim Durchlaufen des Blocks in
         nulle parmi une liste des données einer              im          Voraus      definierten

                                             - 41 -



         résiduelles obtenue lors du parcours Reihenfolge erhalten werdenworden
         dans un ordre prédéfini dudit bloc,            ist,    und     die          Restdaten       der
                                                        Untergesamtheit von einem ersten
                                                        von           null            verschiedenen
                                                        Restdatenelement              der    Liste    zu
                                                        einem          letzten          von          null
                                                        verschiedenen           Restdatenelement
                                                        der Liste laufen,
M2.6     calculer la valeur d´une fonction den                  Wert         einer     Funktion       zu
         représentative de la parité de la bestimmen, die die Parität der
         somme des données résiduelles Summe                           der       Restdaten           der
         dudit sous-ensemble déterminé,                 bestimmten                   Untergesamtheit
                                                        repräsentiert,
M2.7     comparer ladite valeur calculée à la den berechneten Wert mit der Parität
         parité d´au moins une desdites wenigstens                       einer         der     digitalen
         informations numériques,                       Informationen zu vergleichen,
M2.7.1   ladite au moins une information wobei die wenigstens eine digitale
         numérique correspondant au signe Information dem Vorzeichen eines
         d´une donnée résiduelle du sous- Restdatenelements                                          der
         ensemble,                                      Untergesamtheit entspricht,
M2.8     modifier ou non au moins une des in Abhängigkeit vom Ergebnis des
         données         résiduelles    dudit    sous- ModifizierensVergleichs wenigstens
         ensemble déterminé, en fonction du eines der Restdatenelemente der
         résultat               de               ladite bestimmten           Untergesamtheit          zu
         modificationcomparaison,                       modifizieren          oder          nicht     zu
                                                        modifizieren,
M2.9     ainsi que des moyens (CE_CO) de sowie Mittel (CE_CO) umfasst, um
         codage entropique de l´ensemble de im Fall des Modifizierens durch die
         données         résiduelles    comprenant Verarbeitungsmittel die Gesamtheit
         ladite     au     moins       une      donnée von Restdaten, die das wenigstens

                                            - 42 -



          résiduelle     modifiée,     en      cas   de eine modifizierte Restdatenelement
          modification par lesdits moyens de enthält, ohne die wenigstens eine
          traitement sans ladite au moins une digitale Information entropisch zu
          information numérique.                         entropiecodieren.




Patentanspruch 3 des Streitpatents lautet in gegliederter Form wie folgt (mit
Korrekturen):


         Anspruch 3                                     Übersetzung
M3.1     Procédé de décodage d´un signal de Verfahren zum Decodieren eines
         données (F) représentatif d´au moins Datensignals (F), dass wenigstens
         une image découpée en partitions qui ein in Partitionen unterteiltes Bild
         a       été    précédemment            codée, repräsentiert, das vorher codiert
         comprenant                                     worden ist, umfassend
M3.2     une étape d´obtention (D2), par einen Schritt (D2) des Erhaltens
         décodage entropique de données durch Entropiedecodieren von Daten
         dudit         signal,       d´informations des         Signals      von    digitalen
         numériques                                     Informationen,
M3.2.1 associées à des données résiduelles die Restdaten zugeordnet sind, die
         relatives à au moins une partition auf wenigstens eine früher codierte
         précédemment codée,                            Partition bezogen sind,
M3.2.2 les        données        résiduelles     étant wobei die Restdaten in einem Block
         arrangées en un bloc de données von Restdaten angeordnet sind,
         résiduelles,
         ledit procédé de décodage étant                wobei das Decodierungsverfahren
         caractérisé en ce qu´il comprend les dadurch gekennzeichnet ist, dass
         étapes suivantes:                              es die folgenden Schritte umfasst:

                                           - 43 -



M3.3     détermination,    à      partir   desdites anhand der Restdaten Bestimmen
         données     résiduelles,     d´un    sous- einer Untergesamtheit,
         ensemble
M3.3.1 contenant des données résiduelles die Restdaten enthält, die während
         aptes à avoir été modifiées au cours einer         vorhergehenden        Codierung
         d´un codage précédent,                     modifiziert worden sein können,
M3.3.2 le sous-ensemble contenant données wobei                 die        Untergesamtheit
         résiduelles partant d´une première Restdaten            aus     einer Liste     von
         donnée résiduelle non nulle á une Restdaten               enthält,      die    beim
         dernière donnée résiduelle non nulle Durchlaufen des Blocks in einer im
         parmi      une   liste     de     données Voraus      definierten       Reihenfolge
         résiduelles obtenue lors du parcours erhalten wirdworden ist, enthält,und
         dans un ordre prédéfini dudit bloc,        die Restdaten der Untergesamtheit
                                                    von    einem        ersten    von    null
                                                    verschiedenen        Restdatenelement
                                                    der Liste zu einem letzten von null
                                                    verschiedenen        Restdatenelement
                                                    der Liste laufen,
M3.4     calcul (D5) de la valeur d´une fonction Berechnen (D5) des Wertes einer
         représentative de la parité de la Funktion, die die Parität der Summe
         somme      des données résiduelles der           Restdaten       der    bestimmten
         dudit sous-ensemble déterminé,             Untergesamtheit repräsentiert,
M3.5     reconstruction à partir de ladite parité anhand der berechneten Parität
         calculée                                   Rekonstruieren
M3.5.1 d´une valeur du signe d´une donnée eines Wertes des Vorzeichens eines
         résiduelle du sous-ensemble.               Restdatenelements                    der
                                                    Untergesamtheit.




Patentanspruch 4 des Streitpatents lautet in gegliederter Form wie folgt (mit
Korrekturen):

                                          - 44 -




         Anspruch 4                                 Übersetzung
M4.1     Dispositif (DO) de décodage d´un Vorrichtung (DO) zum Decodieren
         signal de données représentatif d´au eines Datensignals, das wenigstens
         moins une image découpée en ein in Partitionen unterteiltes Bild
         partitions qui a été précédemment repräsentiert, das vorher codiert
         codée, comprenant des moyens worden ist, die Mittel (DE_DO)
         (DE_DO)                                    umfasst,
M4.2     d´obtention,          par       décodage um           durch          entropisches
         entropique de données dudit signal, DecodierenEntropiedecodieren von
         d´informations numériques                  Daten      des     Signals     digitale
                                                    Informationen zu erhalten,
M4.2.1   associées à des données résiduelles die Restdaten zugeordnet sind, die
         relatives à au moins une partition auf wenigstens eine vorher codierte
         précédemment codée,                        Partition bezogen sind,
M4.2.2   les   données         résiduelles    étant wobei die Restdaten in einem Block
         arrangées en un bloc de données von Restdaten angeordnet sind,
         résiduelles,
         ledit dispositif de décodage étant wobei die Decodierungsvorrichtung
         caractérisé en ce qu´il comprend dadurch gekennzeichnet ist, dass
         des     moyens          de      traitement sie Verarbeitungsmittel (MTR_DO)
         (MTR_DO) qui sont aptes à:                 umfasst, die dafür ausgelegt sind:
M4.3     déterminer,       à    partir    desdites anhand      der     Restdaten      eine
         données        résiduelles,     un   sous- Untergesamtheit zu bestimmen,
         ensemble
M4.3.1   contenant des données résiduelles die Restdaten enthält, die während
         aptes à avoir été modifiées au cours einer vorhergehenden Codierung
         d´un codage précédent,                     modifiziert worden sein können,
M4.3.2   le    sous-ensemble             contenant wobei        die     Untergesamtheit
         données résiduelles partant d´une Restdaten             aus einer Liste von

                                       - 45 -



           première donnée résiduelle non nulle Restdaten            enthält,        die      beim
           à une dernière donnée résiduelle non Durchlaufen des Blocks in einer im
           nulle parmi une liste de données Voraus             definierten          Reihenfolge
           résiduelles obtenue lors du parcours erhalten wirdworden ist, enthält,und
           dans un ordre prédéfini dudit bloc,      die Restdaten von einem ersten von
                                                    null                        verschiedenen
                                                    Restdatenelement          der     Liste     zu
                                                    einem          letzten          von        null
                                                    verschiedenen          Restdatenelement
                                                    der Liste laufen,
 M4.4      calculer la valeur d´une fonction den            Wert     einer         Funktion     zu
           représentative de la parité de la berechnen,              die     die    Parität    der
           somme des données résiduelles Summe                     der       Restdaten         der
           dudit sous-ensemble déterminé,           bestimmten               Untergesamtheit
                                                    repräsentiert,
 M4.5      reconstruction à partir de ladite parité anhand der berechneten Parität
           calculée,
 M4.5.1    d´une valeur du signe d´une donnée einen Wert des Vorzeichens eines
           résiduelle du sous-ensemble.             Restdatenelements                          der
                                                    Untergesamtheit zu rekonstruieren.




4.      Als zuständiger Durchschnittsfachmann, der mit der Aufgabe betraut wird,
die zu übertragene Datenmenge für codierte Videos zu verringern und eine
effizientere Decodierung zu ermöglichen, ist ein Hochschul-Absolvent aus dem
Bereich der Informationstechnik, Informatik oder Elektrotechnik mit mehrjähriger
Berufserfahrung auf dem Gebiet der Entwicklung von digitaler Videocodierung und
–decodierung anzusehen, der mit den dabei zum Einsatz kommenden Techniken
und den wichtigen Standards vertraut ist und dem insbesondere die im Rahmen der
Standardisierungsprozesse      diskutierten      Beiträge    zur         Weiterentwicklung
bestehender Standards bekannt sind.

                                          - 46 -




5.       Zur Lehre des Streitpatents (Beschreibung)


Gemäß den Absätzen [0016] bis [0024] der Streitpatentschrift besteht die
eigentliche Leistung des Streitpatents darin, bei der Bild- bzw. Videocodierung als
in bekannter Weise zu verbergende Information das Vorzeichen irgendeines der zu
übertragenden Koeffizienten zu wählen und dabei das Verschleierungsverfahren
auf eine reduzierte Gesamtheit von Koeffizienten anzuwenden, die sich dazu
eignen, modifiziert zu werden. Laut Streitpatent bietet sich ein solches Vorzeichen
in besonderer Weise an, verborgen zu werden, weil die Wahrscheinlichkeit eines
Vorkommens        eines positiven oder negativen Vorzeichens gleichermaßen
wahrscheinlich ist, wodurch Signalisierungskosten erheblich reduziert werden
können.


5.1      Das Streitpatent hat offensichtliche Fehler.


      · In der Streitpatentschrift ist die deutsche Übersetzung des Merkmals M1.5.2
         des Patentanspruchs 1 missglückt. Eine verständlichere Übersetzung lautet:
         „wobei die Untergesamtheit Restdaten aus einer Liste von Restdaten enthält,
         die beim Durchlaufen des Blocks in einer im Voraus definierten Reihenfolge
         erhalten worden ist, und die Restdaten der Untergesamtheit von einem
         ersten von Null verschiedenen Restdatenelement der Liste zu einem letzten
         von Null verschiedenen Restdatenelement der Liste laufen,“
      · Entsprechendes gilt für die jeweiligen Merkmale M2.5.2, M3.3.2 und M4.3.2
         der Patentansprüche 2, 3 bzw. 4.
      · Weiterhin finden sich Fehler in der französischen Fassung von Merkmal
         M1.5.2. Dort muss es wohl heißen: „… partant d´une première donnée
         résiduelle non nulle à une dernière donnée résiduelle non nulle parmi une
         liste de données résiduelles obtenue lors du parcours …“. Dergleichen gilt
         für die Merkmale M2.5.2, M3.3.2 und M4.3.2.

                                           - 47 -



      · Eine verunglückte Übersetzung findet sich außerdem in Merkmal M1.8 von
         Patentanspruch 1. Dort muss es heißen: „in Abhängigkeit vom Ergebnis des
         Vergleichs Modifizieren (C10) oder Nicht-Modifizieren wenigstens eines
         Restdatenelements der Restdaten der Untergesamtheit,“.
      · Ferner hat sich in Merkmal M2.8 des Patentanspruchs 2 ein Fehler
         eingeschlichen. Sowohl in der französischen als auch deutschen Fassung
         des Merkmals M2.8 ist fälschlicherweise die Rede davon, dass in
         Abhängigkeit vom Ergebnis des Modifizierens („en fonction du résultat de
         ladite   modification“)    wenigstens      eines   der   Restdatenelemente   der
         bestimmten Untergesamtheit modifiziert oder nicht modifiziert werden soll. In
         Hinblick auf Merkmal M1.8 muss Merkmal M2.8 hingegen lauten: „modifier
         ou non au moins une des données résiduelles dudit sous-ensemble
         déterminé, en fonction du résultat de ladite comparaison,“ bzw. „in
         Abhängigkeit vom Ergebnis des Vergleichs wenigstens eines der
         Restdatenelemente der bestimmten Untergesamtheit zu modifizieren oder
         nicht zu modifizieren,“.


5.2     Die Idee des Verbergens eines Parameters in der Parität einer Summe von
Daten setzt voraus, dass wenn die Parität nicht stimmt (dies sollte beim Verbergen
von Vorzeichen von Transformationskoeffizienten in 50 % der Fälle passieren), ein
Koeffizient der Daten modifiziert werden muss (z. B. durch Addition von „+1“). Dies
bewirkt eine Verfälschung des übertragenen Bildes, welche der Decodierer nicht
korrigieren kann. Deshalb wird im Streitpatent vorgeschlagen, mehrmals
verschiedene Koeffizienten probeweise zu modifizieren und zu prüfen, welche
Modifikation die geringste Bildstörung hervorruft (vgl. z. B. Streitpatentschrift, Abs.
[0079], siehe „En conséquence, le module de traitement MTR_CO teste, au cours
de ladite étape C10, différentes modifications de coefficients de la sous-liste SE1,
visant toutes à changer la parité de la somme des coefficients.“; Abs. [0080], siehe
„Dans le mode préféré de réalisation, une telle sélection constitue la prédiction
optimale selon un critère de performance qui est par exemple le critère débit
distorsion bien connu de l´homme du métier.“).

                                        - 48 -




5.3     Wesentlich für die Lehre des Streitpatents sind die zwei Fragen, welches
Vorzeichen verborgen übertragen wird, und welcher Koeffizient dafür modifiziert
wird.


5.3.1 Welcher Koeffizient modifiziert werden soll, ist im Grunde beliebig.
Sinnvollerweise wären verschiedene Koeffizienten auszuwählen und zu prüfen,
wessen Modifikation die geringsten Auswirkungen auf die Bildqualität hat (siehe
oben). Der Fachmann wird verstehen, dass für jede einzelne Bild-Partition ein
anderer Koeffizient modifiziert werden kann, und dass der Decodierer keine
Möglichkeit hat, den jeweils modifizierten Koeffizienten herauszufinden (oder gar
noch zu „reparieren“).


5.3.2 Welches Vorzeichen verborgen übertragen wird, ist eine ganz wesentliche
Information, die der Decodierer kennen muss (sonst kann er das wiedergewonnene
Vorzeichen nicht richtig zuordnen). Hierzu verhält sich das Streitpatent auffallend
wenig. Der Fachmann liest aber mit, dass zwar grundsätzlich jedes beliebige
Vorzeichen aus der Menge der Koeffizienten auf diese Weise übertragen werden
kann; dass aber vorab eine Vereinbarung getroffen werden muss, die dem Codierer
und dem Decodierer bekannt ist, und die dann für jede Bild-Partition identisch ist –
einmal festgelegt, kann sie nicht mehr geändert werden. Das Streitpatent bevorzugt
die Festlegung „des Vorzeichens des ersten von Null verschiedenen Koeffizienten
(Streitpatentschrift, Abs. [0063], siehe „En outre, conformément audit mode de
réalisation préféré, c´est le signe du premier coefficient non nul qui est destiné à
être caché.“; Streitpatentschrift Abs. [0083] und [0085]).


5.4     Das Streitpatent geht an mehreren Stellen auf eine verborgene Übertragung
mehrerer Vorzeichen ein (Streitpatentschrift, z. B. Abs. [0098], [0102], [0103],
[0105], [0119]). Es ist jedoch unmittelbar einsichtig, dass mit der Parität der Summe
der Restdaten nur eine binäre Information übertragen werden kann – für mehrere

                                          - 49 -



Vorzeichen ist eine Anpassung der Verfahren erforderlich (vgl. Abs. [0103], siehe
„le reste modulo 2N de la somme des coefficients modifiables de la sous-liste SE1“).


5.5    Zusammenfassend ist festzustellen, dass um die Information „Vorzeichen
eines bestimmten Koeffizienten“ verborgen übertragen zu können, in rund der Hälfte
der Fälle ein Koeffizient verfälscht werden muss. Jeder beliebige der Koeffizienten
ungleich Null kann hierfür ausgewählt werden (solange dessen Modifikation nicht
zum Wert Null führt), entscheidend ist nur, dass die Summe aller Koeffizienten die
benötigte Parität hat.


6.     Die streitpatentgemäße Lehre ist aus Sicht des Fachmanns wie folgt zu
erläutern:


a)     Zum Begriff „Partition“ („la partition“):


Laut Absatz [0039] der Streitpatentschrift wird vor der eigentlichen Codierung einer
Bildsequenz jedes Bild in eine Vielzahl von „Partitionen“ unterteilt (vgl.
Streitpatentschrift, Figur 2). Wie weiterhin den Absätzen [0040] und [0041] zu
entnehmen ist, bezeichnet der Begriff „Partition“ eine Codierungseinheit („unité de
codage“ bzw. „coding unit“), wie sie aus dem HEVC/H.265-Standard bekannt ist.
Eine solche Codierungseinheit fasst Pixel zu Pixelgruppen mit rechteckiger oder
quadratischer Form zusammen („de forme rectangulaire ou carrée“), wie etwa
Blöcken oder Makroblöcken.


b)     Zum Begriff „Restdaten“ („les données résiduelles“)


Der Begriff „Restdaten“ nimmt entsprechend den Merkmalen M1.2 und M1.3 Bezug
auf eine Intra- oder Inter-Codierung, bei der Daten einer aktuellen Partition in
Abhängigkeit von wenigstens einer bereits codierten und dann decodierten
Referenzpartition vorhergesagt werden (vgl. Streitpatentschrift, Abs. [0050] bis
[0056]). Zwar geht aus dem Streitpatent nicht unmittelbar hervor, worin die

                                        - 50 -



anspruchsgemäßen Restdaten konkret bestehen sollen, allerdings ist bereits in
Absatz [0004] der Streitpatentschrift die Rede davon, dass in aktuellen
Videocodierern für jeden Block ein Restblock bzw. Vorhersagerest codiert wird, der
dem   ursprünglichen    Block   abzüglich    einer   Vorhersage    entspricht.   Nach
Transformation und anschließender Quantisierung wird eine eindimensionale Liste
mit Koeffizienten erhalten, die als quantisierter Rest bezeichnet wird. Ähnliches
ergibt sich aus den Absätzen [0053] bis [0056] der Streitpatentschrift. Dort wird
ausgeführt, dass eine Subtraktion eines vorhergesagten Blocks Bp1 von dem
aktuellen Block B1 vorgenommen wird, um einen Restblock Br1 zu erzeugen, der
mittels einer Transformationsoperation in einen transformierten Block Bt1
umgewandelt wird, dessen anschließende Quantisierung zu einem Block Bq1
quantisierter Koeffizienten führt. Das Streitpatent erläutert (Abs. [0056]), dass beim
Durchlaufen eines solchen Blocks in einer vordefinierten Reihenfolge eine
eindimensionale Liste E1 mit Koeffizienten erhalten wird, also eine Gesamtheit von
Daten, wobei jeder der Koeffizienten unterschiedlichen digitalen Informationen
zugeordnet ist, die dazu vorgesehen sind, einer Entropiecodierung unterzogen zu
werden. Außerdem geht aus den Absätzen [0065] bis [0067] der Streitpatentschrift
hervor, dass ausgehend von dieser Liste E1 eine Teilliste SE1 bestimmt wird, die die
Koeffizienten enthält, die modifiziert werden können und die somit eine
Untergesamtheit der Liste E1 bilden. Letztere beinhaltet diejenigen Koeffizienten
aus der Liste E1, die vom ersten bis zum letzten von Null verschiedenen
Koeffizienten laufen (Abs. [0066]) und für die der Wert einer für diese Koeffizienten
repräsentativen Funktion berechnet werden soll (Abs. [0070]).


Anhand der genannten Textstellen der Streitpatentschrift wird der Fachmann
erkennen, dass die Verfahrensschritte der Merkmale M1.3 bis M1.6 (Bestimmen
einer Gesamtheit bzw. Untergesamtheit, Berechnung des Funktionswerts) an einem
Block quantisierter Koeffizienten ausgeführt werden.


An keiner Stelle der Streitpatentschrift findet sich hingegen ein Hinweis dafür, dass
für den Restblock Br1, der den Prädiktionsfehler bzw. Vorhersagerest repräsentiert,

                                             - 51 -



oder für irgendeinen anderen, von Bq1 verschiedenen Block eine Untergesamtheit
und eine Summenparität i. S. d. Patentanspruchs 1 ermittelt werden sollen.


Nach allem handelt es sich bei den anspruchsgemäßen Restdaten um die
quantisierten Koeffizienten.


c)     Zum Begriff „Gesamtheit von Restdaten“ („l´ensemble de données
résiduelles“)


Entsprechend Merkmal M1.3.1 soll es sich bei der Gesamtheit von Restdaten um
einen Block von Restdaten handeln. Unter Berücksichtigung obiger Auslegung ist
mit der Gesamtheit von Restdaten ein Block quantisierter Koeffizienten gemeint, wie
er im Schritt C5 der Figur 1 der Streitpatentschrift erzeugt und dann im Schritt C6
auf eine eindimensionale Liste E1 abgebildet wird (vgl. Streitpatentschrift, Abs.
[0055], [0056]).


d)     Zum Begriff „Untergesamtheit“ („le sous-ensemble“)


Die Merkmale M1.5 bis M1.5.2 besagen, dass die Untergesamtheit Restdaten
enthält, die modifiziert werden können. Die anspruchsgemäße Untergesamtheit
entspricht   einer   Menge     SE1   modifizierbarer   Koeffizienten,   die   aus   der
eindimensionalen Liste E1 quantisierter Koeffizienten gewonnen wird und deren
Elemente vom ersten bis zum letzten von Null verschiedenen Koeffizienten der Liste
E1 laufen (vgl. Streitpatentschrift, Abs. [0065], [0066]). Insoweit bildet die
Untergesamtheit eine Teilmenge der Gesamtheit von Restdaten bzw. quantisierten
Koeffizienten.


e)     Zum Begriff „Parität“ („la parité“)


Die Parität ist die Eigenschaft ganzer Zahlen, gerade oder ungerade zu sein, was
durch die beiden Werte „0“ oder „1“ beschrieben werden kann (siehe oben). In

                                        - 52 -



diesem Sinne spricht das Streitpatent z. B. von einer Summe quantisierter
Koeffizienten, die bei einem geraden Zahlenwert mit einem MVComp-Index mit dem
Wert „0“ und bei einem ungeraden Zahlenwert mit einem MVComp-Index mit dem
Wert „1“ verknüpft wird (vgl. Streitpatentschrift, Abs. [0011], Spalte 3, Zeilen 9 bis
13, siehe „… la valeur paire du résidu quantifié est associée à l´index MVComp de
valeur 0, tandis que la valeur impaire du résidu quantifié est associée à l´index
MVComp de valeur 1.“). In Bezug auf das Vorzeichen eines quantisierten
Koeffizienten bzw. Restdatenelements versteht das Streitpatent unter Parität die
Eigenschaft, positiv oder negativ zu sein. Parität kann somit auch als Eigenschaft
des das Vorzeichen codierenden Bits aufgefasst werden, gleich Null (positives
Vorzeichen) oder gleich 1 (negatives Vorzeichen) zu sein (vgl. Streitpatentschrift, z.
B. Abs. [0073], siehe „Dans l´exemple proposé, ladite convention est telle qu´un
signe positif est associé à un bit de valeur égale à zéro, tandis qu´un signe négatif
est associé à un bit de valeur égale à un.”).


f)    Zur Lehre der erteilten Patentansprüche 1 und 2


Die auf ein Verfahren bzw. auf eine Vorrichtung zum Codieren wenigstens eines in
Partitionen unterteilten Bildes gerichteten Patentansprüche 1 und 2 unterscheiden
sich außer in ihrer Kategorie nur unwesentlich, so dass die Überlegungen zu
Patentanspruch 1 für Patentanspruch 2 gleichermaßen gelten; insoweit genügt es,
sich mit dem Verfahrensanspruch auseinanderzusetzen.


Gemäß Merkmal M1.1 betrifft das Verfahren ein „in Partitionen unterteiltes“
(digitales) Bild. Wie den Absätzen [0040] und [0041] der Streitpatentschrift zu
entnehmen ist, bezeichnet „Partition“ eine Codierungseinheit, wie sie etwa aus dem
HEVC/H.265-Standard bekannt ist, also einen Block von Pixeln.


Gemäß Merkmal M1.2 werden die Daten einer aktuellen Partition in Abhängigkeit
von einer bereits codierten und dann decodierten Partition vorhergesagt. Laut
Absatz [0049] der Streitpatentschrift handelt es sich bei dieser Vorhersage um Intra-

                                             - 53 -



Prädiktion bzw. Inter-Prädiktion („… il est procédé au codage prédictif du bloc
courant B1 par des techniques connues de prédiction intra et/ou inter, au cours
duquel le bloc B1 est prédit par rapport à au moins un bloc précédemment codé ou
décodé.“).


Merkmal M1.3 besagt, dass eine Gesamtheit von Restdaten bestimmt wird, bei der
es sich gemäß Merkmal M1.3.1 um einen Block von Restdaten handelt. Die
Restdaten werden bestimmt, indem auf die aktuelle Partition bezogene Daten mit
der       vorhergesagten    Partition   verglichen    werden.    In   Absatz   [0053]   der
Streitpatentschrift wird anhand der Figur 1 (Schritt C3) diesbezüglich ausgeführt,
dass der aktuelle Block B1 von seiner Prädiktion Bp1 abgezogen wird, um einen
Differenzblock bzw. Restblock Br1 zu erhalten („… au cours de cette étape, il est
procédé classiquement à la soustraction du bloc prédit Bp1 du bloc courant B1 pour
produire un bloc résidu Br1.“). Die Schritte C4 und C5 der Figur 1, die Transformation
und Quantisierung betreffen, führen ausgehend von Restblock Br1 zum Block Bq1
mit quantisierten Koeffizienten (Streitpatentschrift, Abs. [0054], [0055]). Demnach
hat zur Bestimmung der anspruchsgemäßen Gesamtheit von Restdaten, mit denen
entsprechend obiger Auslegung die quantisierten Koeffizienten gemeint sind,
lediglich der Vergleich von Daten eines aktuellen Blocks mit Daten des
vorhergesagten Blocks Eingang in den Patentanspruch 1 gefunden.


Ferner sieht Merkmal M1.3 vor, dass die Restdaten - also die quantisierten
Koeffizienten - jeweils unterschiedlichen digitalen Informationen zugeordnet sind,
die dazu bestimmt sind, einer Entropiecodierung unterworfen zu werden. Laut
Absatz [0056] bis [0058] der Streitpatentschrift sind diese Informationen z. B.


      ·    ein Bit, das angibt, ob ein Koeffizient gleich Null ist;
      ·    ein Bit, das für jeden Koeffizienten ungleich Null angibt, ob sein Betrag gleich
           eins oder größer als eins ist;
      ·    für jeden Koeffizienten ungleich Null mit Betrag ungleich eins ein
           Datenelement, das den Betrag vermindert um zwei angibt, sowie

                                          - 54 -



    ·   ein Bit, das angibt, ob der Koeffizient ein positives oder negatives
        Vorzeichen hat.


Gemäß Merkmal M1.4 wird ein Signal erstellt, das die codierten Informationen
enthält. Nach der in Merkmal M1.3 genannten Entropiecodierung wird also ein
Bitstrom erzeugt. Zuvor werden aber die im kennzeichnenden Teil definierten
Schritte aus den Merkmalen M1.5 bis M1.9 ausgeführt.


Die Merkmale M1.5 und M1.5.1 sehen vor, dass anhand der bestimmten
Gesamtheit von Restdaten eine Untergesamtheit bestimmt wird, die Restdaten
enthält, die modifiziert werden können.


Für die Codierung geht der Codierer von dieser Untergesamtheit modifizierbarer
Restdatenelemente aus, welche Restdaten enthält, die beim Durchlaufen des
Blocks in der vorgegebenen Reihenfolge von einem ersten bis zu einem letzten von
Null verschiedenen Restdatenelement laufen (Merkmal M1.5.2).


Gemäß Merkmal M1.6 wird der Wert einer Funktion berechnet, die die Parität der
Summe der Restdaten der bestimmten Untergesamtheit repräsentiert. Wie die
Parität berechnet bzw. welche Funktion hierzu angewendet wird, legt das Merkmal
nicht fest. Ebensowenig verlangt das Merkmal, dass die Funktion unmittelbar den
Wert der Parität („0“ bzw. „1“) darstellt. Vielmehr kann im Ablauf des Verfahrens
auch eine andere Darstellung verwendet werden, welche für die Parität steht bzw.
diese repräsentiert.


In den Merkmalen M1.7 und M1.7.1 wird beansprucht, dass der in Merkmal M1.6
ermittelte Wert mit wenigstens einer der digitalen Informationen verglichen wird,
wobei es sich bei der wenigstens einen digitalen Information um das Vorzeichen
eines Restdatenelements der Untergesamtheit handelt. Im Ausführungsbeispiel der
Figur 1 der Streitpatentschrift wird die berechnete Parität mit dem Vorzeichen eines
Listenelements der Unterliste bzw. Untergesamtheit von Restdaten verglichen. Die

                                         - 55 -



Parität bezeichnet also in Bezug auf das Vorzeichen die Eigenschaft, positiv oder
negativ zu sein, und kann auch als Eigenschaft des das Vorzeichen codierenden
Bits verstanden werden, gleich Null (gerade) oder gleich 1 (ungerade) zu sein
(Streitpatentschrift, Abs. [0072], siehe „… le module de traitement MTR_CO vérifie
si la parité de la valeur du signe à cacher correspond à la parité de la somme des
coefficients de la sous-liste SE1 …”).


In Abhängigkeit vom Ergebnis dieses Vergleichs wird gemäß Merkmal M1.8
wenigstens ein Restdatenelement modifiziert oder nicht. Diese Modifikation wird in
den Absätzen [0079] bis [0084] der Streitpatentschrift am Beispiel der Liste
SE1=(+9, -7, 0, 0, +1, 0, -1, +2, 0, 0, +1) erläutert. Dabei soll das Vorzeichen des
ersten von Null verschiedenen Listenelements, also von +9, versteckt werden. Da
die Summe der Listenelemente eine ungerade Parität hat (Summe gleich 5, also
ungerade), das zu versteckende Vorzeichen aber positiv ist, wird die Modifikation
eines Listenelements vorgenommen, z. B. wird das zweite von Null verschiedene
Listenelement, -7, durch Addition von +1 zu -6 abgeändert. Hierdurch ergibt sich
eine modifizierte Liste („la sous-liste modifiée“) SEm1=(+9, -6, 0, 0, +1, 0, -1, +2, 0,
0, +1). Die Summe der Elemente ist jetzt gleich +6 und weist somit eine gerade
Parität auf, was der Parität des zu versteckenden Vorzeichens entspricht.


Im Fall des Modifizierens wird die Gesamtheit von Restdaten mit dem wenigstens
einen modifizierten Restdatenelement entropiecodiert, und zwar ohne die
wenigstens eine digitale Information (Merkmal M1.9).


In Hinblick auf die Merkmale M1.7 bis M1.9 wird der Fachmann im Kontext der
Beschreibung des Streitpatents zusätzlich folgende weiterführende Auslegung
treffen:


Da die Parität eine binäre Information darstellt, kann in der Parität einer Summe von
Daten streng genommen nur genau ein Vorzeichen verborgen werden, wenn
ansonsten keine zusätzlichen Vereinbarungen getroffen werden. Dies bedeutet

                                           - 56 -



gleichzeitig, dass für alle Ausführungsbeispiele, welche die Übertragung mehrerer
Vorzeichen betreffen (vgl. Streitpatentschrift, Abs. [0098] bis [0105]; [0119])
Anpassungen vorgenommen werden müssen. Das Streitpatent schlägt in Hinblick
auf das Verstecken mehrerer Vorzeichen die Funktion Summe der Koeffizienten
modulo 2N vor („la somme modulo 2N des coefficients“), deren Werte für N=2 gemäß
Absatz [0101] der Streitpatentschrift insgesamt vier verschiedene Kombinationen
von zwei aufeinanderfolgenden Vorzeichen zugeordnet sind. Weil die möglichen
Werte der Funktion (0, 1, 2, 3) selbst die Eigenschaft haben, geradzahlig oder
ungeradzahlig zu sein, steht jeder einzelne Wert zugleich für die Parität der Summe
der Koeffizienten bzw. repräsentiert diese, so wie es Merkmal M1.6 fordert. Insoweit
ergibt es mathematisch durchaus Sinn, den mittels der Funktion Summe modulo 2N
ermittelten Wert bzw. die sich daraus gemäß Vereinbarung ergebenden
Vorzeichenfolgen mit mehreren zu versteckenden digitalen Informationen bzw.
Vorzeichen zu vergleichen und gegebenenfalls mehrere Koeffizienten zu
modifizieren. Die Gesamtheit der Koeffizienten wird dann natürlich ohne die zu
versteckenden digitalen Informationen codiert.


g)     Zur Lehre der erteilten Patentansprüche 3 und 4


Auch die auf ein Verfahren bzw. auf eine Vorrichtung zum Decodieren eines
Datensignals gerichteten Patentansprüche 3 und 4 unterscheiden sich außer in ihrer
Kategorie    nur   unwesentlich.    Hier    genügt   es   ebenfalls,    sich   mit   dem
Verfahrensanspruch 3 auseinanderzusetzen.


Gemäß Merkmal M3.1 betrifft das Verfahren zum Decodieren eines Datensignals
ein „in Partitionen unterteiltes“ (digitales) Bild, das vorher codiert worden ist.


Merkmal M3.2 besagt, dass digitale Informationen durch Entropiedecodierung von
Daten des Signals erhalten werden, wobei die Informationen Restdaten zugeordnet
sind. Diese Restdaten sind auf wenigstens eine früher codierte Partition bezogen

                                         - 57 -



(Merkmal M3.2.1) und sind in einem Block von Restdaten angeordnet (Merkmal
M3.2.2).


Die Merkmale M3.3 bis M3.4 entsprechen den Merkmalen M1.5 bis M1.6 des
Codierverfahrens gemäß Patentanspruch 1. Sie betreffen das Bestimmen einer
Untergesamtheit von Restdaten sowie das Berechnen der Parität der Summe der
Restdaten der Untergesamtheit.


Die Merkmale M3.5 und M3.5.1 sehen vor, anhand der berechneten Parität den
Wert eines Vorzeichens eines Restdatenelements der Untergesamtheit zu
rekonstruieren. Für das in der Beschreibung des Streitpatents angegebene Beispiel
ist die Summe der Elemente der Liste SEm1=(+9, -6, 0, 0, +1, 0, -1, +2, 0, 0, +1)
gleich +6, also gerade. Der Decodierer schließt daraus, dass das versteckte
Vorzeichen des ersten von Null verschiedenen Koeffizienten positiv ist
(Streitpatentschrift, Abs. [0082], [0130]).


h)     Zur Lehre der Patentansprüche 5 und 6


Die Patentansprüche 5 und 6 sind jeweils auf ein Rechnerprogramm gerichtet
(„programme d´ordinateur“), das Befehle enthält, um das Codierungsverfahren nach
Anspruch 1 bzw. das Decodierungsverfahren nach Anspruch 3 auszuführen. Sie
enthalten keine eigenständige technische Lehre und stehen oder fallen mit dem
jeweils in Bezug genommenen Patentanspruch.


7.     Zum jeweiligen Vorbringen von Klägerin und Beklagter zur Auslegung der
Merkmalsgruppen M1.5 und M3.3 („Untergesamtheit“ – „le sous-ensemble“) der
erteilten unabhängigen Patentansprüche ist Folgendes anzumerken:


7.1     Zwar ist der Klägerin darin zuzustimmen, dass entsprechend dem Wortlaut
von Merkmal M1.5.1 bzw. M3.3.1 die Untergesamtheit Restdaten enthält, die dazu
geeignet sind, modifiziert zu werden („contenant des données résiduelles aptes à

                                        - 58 -



être modifiées,“). Anhand der Absätze [0065] und [0120] sowie der Figuren 1 und 3
(siehe Schritt C71 bzw. D31) der Streitpatentschrift wird jedoch entgegen der
klägerseitigen Auffassung deutlich, dass die Untergesamtheit nur modifzierbare
Restdaten enthalten soll, also keine nicht-modifizierbaren Restdaten mit umfassen
soll (vgl. Streitpatentschrift, Abs. [0065], siehe „… d´une sous-liste SE1 contenant
des coefficients aptes à être modifiés ε´1, ε´2, …, , ε´M où M<L. De tels coefficients
seront appelés coefficients modifiables dans la suite de la description.“).


7.2     Betrachtet man Merkmal M1.5.2 bzw. M3.3.2, so ist die Formulierung
„données résiduelles partant d´une première donnée résiduelle non-nulle à une
derniére donnée résiduelle non-nulle parmi une liste de données résiduelles“ –
wenn man versucht, sich am bloßen Wortlaut des Merkmals zu orientieren –
allenfalls derart zu verstehen, dass die Restdaten der Untergesamtheit von dem
ersten Restdatenelement ungleich Null aus einer beliebigen Gruppe einer Liste von
Restdaten zu dem letzten Restdatenelement ungleich Null derselben Gruppe
laufen. Ein solches Verständnis führt nicht nur dazu, dass es pro Codierblock
mehrere solcher Gruppen geben kann, sondern dass es infolgedessen auch
mehrere erste und letzte Restdatenelemente ungleich Null gibt. Während der
Codierer laut Absatz [0066] der Streitpatentschrift so konfiguriert ist, dass er die
Restdatenelemente gleich Null vor dem ersten und nach dem letzten
Restdatenelement ungleich Null der Liste von Restdaten nicht modifiziert, um eine
Desynchronisierung mit dem Decodierer zu vermeiden, trifft Entsprechendes auf
das erste und letzte Restdatenelement ungleich Null einer beliebigen Gruppe der
Liste von Restdaten nicht ohne Weiteres zu, wenn keine zusätzlichen
Vereinbarungen zwischen Codierer und Decodierer getroffen werden. Ein
Verständnis, das lediglich vom Wortlaut der Merkmale M1.5.2 und M3.3.2 getragen
wird, hat in der Regel Synchronisationsprobleme zwischen Codierer und Decodierer
zur Folge und ist schon allein aus diesem Grunde nicht sachgerecht. Vielmehr ist
mit den Merkmalen M1.5.2 und M3.3.2 gemeint, dass die Restdaten der
Untergesamtheit von dem ersten zu dem letzten Restdatenelement ungleich Null
(inmitten) der Liste von Restdaten laufen.

                                     - 59 -




7.3    Entgegen der Auffassung der Beklagten vertritt der Senat die breite
Auslegung    des   Merkmals    M1.5.2,     wonach   in   der   anspruchsgemäßen
Untergesamtheit etwaige Restdatenelemente gleich Null nicht notwendigerweise
enthalten zu sein brauchen.


Denn die Ansprüche des Streitpatents lassen sich ohne weiteres auch auf solche
Ausführungsformen lesen, in denen die Untergesamtheit grundsätzlich keine
Restdatenelemente gleich Null enthält. Den Patentansprüchen sind keine
Einschränkungen entnehmbar, dass diese Ausführungsformen nicht unter das
Patent fallen sollen. Auch der Beschreibung ist eine Schutzbegrenzung auf
bestimmte Ausführungsformen, wonach die Untergesamtheit notwendigerweise
etwaige Restdatenelemente gleich Null enthalten muss, nicht zu entnehmen.




                                         II.




Das Streitpatent ist in der erteilten Fassung nicht rechtsbeständig, weil die
jeweiligen Gegenstände der unabhängigen Patentansprüche nicht patentfähig sind.


1.    Zum genannten Stand der Technik


Gemäß dem von der Klägerin genannten Stand der Technik war vor dem
Prioritätszeitpunkt des Streitpatents im Rahmen der Versuche, bekannte Video-Standards wie H.264/AVC zu verbessern, bereits mehrfach vorgeschlagen worden,
eine binäre Information, wie insbesondere ein Flag zur Steuerung der
Codierung/Decodierung, in den zu übertragenden Datenpaketen zu „verbergen“,
speziell als Parität einer Summe von Daten (siehe z. B. Druckschriften NK1, NK2).
Dazu musste ggf. ein Datenelement verfälscht werden, wobei versucht wurde, den
entstehenden Fehler zu minimieren. Keine der zitierten Druckschriften gibt jedoch

                                        - 60 -



explizit die Lehre, das Vorzeichen eines der zu codierenden Koeffizienten zu
„verbergen“ und auf die beschriebene Weise in Form einer Parität zu übertragen.
Mit Rücksicht auf den aus den angeführten Druckschriften bekannten Stand der
Technik ist der jeweilige Gegenstand der erteilten Patentansprüche 1 bis 6 sonach
neu.


2.     Ausgehend von Druckschrift NK1, die dem Streitpatentgegenstand am
nächsten kommt, beruht die Lehre des erteilten Patentanspruchs 1 jedoch nicht auf
erfinderischer Tätigkeit.


2.1    Druckschrift NK1 zeigt sämtliche Merkmale des erteilten Patentanspruchs 1
mit    Ausnahme    von      Merkmal   M1.7.1     betreffend   das   Vorzeichen   eines
Restdatenelements als zu verbergende Information.


Die Druckschrift NK1 betrifft die Codierung und Decodierung wenigstens eines in
Partitionen unterteilten Bildes, wobei eine zu codierende aktuelle Partition Daten
enthält, die die Koeffizienten einer diskreten Transformation sind. Dabei wird von
einem H.264/AVC-Hybrid-Videocodierer ausgegangen, der Intra- und Inter-Prädiktion verwendet, um räumliche und zeitliche Redundanzen auszunutzen. Für
jeden Makroblock stehen mehrere Intra- und Inter-Modi zur Verfügung bzw. in
Konkurrenz, die dem Decodierer zusammen mit anderen Informationen über
Restdaten oder Codierungstyp angezeigt werden müssen (Seite 729, rechte Spalte,
vorletzter Absatz, siehe „For each macroblock, several Intra modes … and Inter
modes … are in competition and need to be signaled to the decoder …“). Um die
Bitrate für die Wettbewerbsindizes („competition indices“) zu verringern, wird
zusätzlich vorgeschlagen, ein Data Hiding auf den Bewegungsvektor-Index
MVComp anzuwenden (Seite 730, linke Spalte, vierter Absatz). Merkmal M1.1 ist
damit offenbart.


Druckschrift NK1 lehrt die Codierung eines Makroblocks mit Intra- und Inter-Prädiktion, d. h. ein aktueller Makroblock wird in Abhängigkeit von wenigstens

                                       - 61 -



einem codierten und dann decodierten Referenzblock sowie einem Prädiktionsblock
vorhergesagt (Seite 729, rechte Spalte, letzter Absatz bis Seite 730, linke Spalte,
erster Absatz, siehe „The choice to encode a macroblock in Intra, Inter, or Skip, is
non-normative. … for each Intra or Inter mode, the best predictor is selected and
the difference between the selected predictor and the current block is transformed
with a 4x4 or 8x8 discrete cosine transform (DCT), quantized and entropy coded.“ –
Merkmal M1.2).


Durch Vergleich von Prädiktionsblock und aktuellem Block wird die Differenz des
Prädiktionsblocks und des aktuellen Blocks bzw. der Prädiktionsfehler ermittelt, die
bzw. der dann transformiert und quantisiert wird. Auf diese Weise wird eine
Gesamtheit von (transformierten und quantisierten) Luma- und Chroma-Restdaten
– die QDCT-Koeffizienten („QDCT Coefficients“) - erhalten, die wiederum
Wettbewerbsindizes und Bewegungsvektoren zugeordnet sind. Alle diese
Informationen werden entropiecodiert und im Bitstrom übertragen (Seite 730, Fig.
1; linke Spalte, erster Absatz, siehe „ … the difference between the selected
predictor and the current block is transformed with a 4x4 or 8x8 discrete cosine
transform (DCT), quantized and entropy coded. Luma and chroma residuals are
transmitted in this way.“; linke Spalte, zweiter Absatz, siehe „A large part of this
bitstream is composed of the competition indices, the other information are the
pixels and the motion vector residuals.”; linke Spalte, dritter Absatz, siehe „Also
context adaptive encoding is performed, so that indices are efficiently encoded.” –
Merkmal M1.3).


Die Gesamtheit von QDCT-Koeffizienten wird durch einen 4x4- oder 8x8-Block
repräsentiert (Seite 730, linke Spalte, erster Absatz, siehe „… and the difference
between the selected predictor and the current block is transformed with a 4x4 or
8x8 discrete cosine transform (DCT), quantized and entropy coded.” – Merkmal
M1.3.1).

                                        - 62 -



QDCT-Koeffizienten und Wettbewerbsindizes sind im Bitstrom codiert, d. h. es wird
ein Datensignal erzeugt, das codierte Informationen zur Rekonstruktion einer
Bildpartition enthält (Seite 730, linke Spalte, zweiter Absatz, siehe „A large part of
this bitstream is composed of the competition indices, the other information are the
pixels and the motion vector residuals.“ – Merkmal M1.4).


Bevor ein Datenstrom überhaupt erzeugt werden kann, sieht die Lehre der
Druckschrift   NK1    aber    noch   die   Durchführung     weiterer   nachfolgender
Verfahrensschritte vor.


Für eine Modifikation der QDCT-Koeffizienten im Rahmen des vorgestellten Data
Hidings wird unter den Abschnitten IV.A. Und IV.B. auf Seite 733 beispielhaft der kte Block betrachtet. Hierbei wird darauf hingewiesen, dass ausschließlich die
transformierten Koeffizienten des k-ten Blocks ungleich Null (an≠0) berücksichtigt
werden sollen (Seite 733, linke Spalte, vorletzter Absatz, siehe „We consider N
transform coefficients an, an≠0.“). Die N ausgewählten Koeffizienten an bilden
zusammen eine Teilmenge bzw. Untergesamtheit aller im k-ten Block enthaltenen
transformierten Koeffizienten. Darüber hinaus handelt es sich bei den Koeffizienten
an um modifizierbare Koeffizienten, da nur die ungeraden Werte mj zu diesen addiert
werden sollen (Seite 733, linke Spalte, vorletzter Absatz, siehe „For each coefficient,
six RD couples (Rwjn, Dwjn) are computed after addition of an odd value mj as follows:
…“ – Merkmale M1.5, M1.5.1).


Die ausgewählten Koeffizienten an gehen von einem ersten Koeffizienten ungleich
Null bis zu einem letzten Koeffizienten ungleich Null entsprechend dem Lauf-Index
n. Die im k-ten Block enthaltenen Koeffizienten gleich Null bleiben also an dieser
Stelle außer Betracht. Dass in Hinblick auf die Entropiecodierung zunächst aber
sämtliche Koeffizienten (auch diejenigen gleich Null) des k-ten Blocks dadurch
bestimmt werden müssen, dass der k-te Block in einer vordefinierten Reihenfolge
(üblicherweise eine Zickzack-Reihenfolge, vgl. NK9´, Seite 8, siehe „3.119 zig-zag
scan“; Seite 18, siehe „6.5.1 Zig-zag scanning array initialisation process“ u. a.)

                                        - 63 -



durchlaufen wird, um den ganzen Block auf eine eindimensionale Datenstruktur
bzw. Liste abzubilden, stellt eine Selbstverständlichkeit dar. Hierzu erläutert die
Druckschrift NK1, dass sich die transformierten Koeffizienten auf die Chroma- oder
Luma-Komponente des aktuellen Blocks beziehen sollen und dass der erste
Koeffizient a1 mit dem DC-Koeffizienten übereinstimmen soll (Seite 732, rechte
Spalte, Abschnitt IV.A., siehe „Let us note an the transform and quantized
coefficients before transmission relative to the chroma or luma component of the
current block, where a1 corresponds to the direct current (DC) value …“), der
bekanntlich den Grundton bzw. den Mittelwert der Pixelwerte der beschriebenen
Partition im Bild angibt. Dem Fachmann ist weiterhin geläufig, dass die Reihenfolge
der Koeffizienten an ungleich Null in der Untergesamtheit mit der vordefinierten
Reihenfolge des k-ten Blocks zur Abbildung aller Koeffizienten auf die
eindimensionale Datenstruktur bzw. Liste in Einklang stehen muss, damit die
Koeffizienten an ungleich Null auch nach der Codierung den richtigen Pixelwerten
zugeordnet bleiben. Nach allem geht auch Merkmal M1.5.2 aus der Druckschrift
NK1 hervor.


Anstelle eines Vorzeichens soll gemäß Druckschrift NK1 allerdings der
Bewegungsvektor-Index („MVComp index“) als binärer Parameter „verborgen“
übertragen werden (Seite 730, linke Spalte, vierter Absatz, siehe „…, we propose
to use data hiding knowledge for decreasing the rate cost of these competition
indices. In particular, we choose to deal with the motion information index generated
by the MVComp tool [4].“).


Das ist dem Codierer und dem Decodierer vorab bekannt, und der Codierer
berechnet dafür den Wert einer Funktion, die die Parität der Summe der
transformierten Koeffizienten der aktuellen Partition repräsentiert (Seite 732, rechte
Spalte, Abschnitt IV.A., siehe „In order to meet these requirements, we propose to
use the parity of the coefficients sum to mark the MVComp index.“). Die Funktion ist
konkret gegeben durch die Modulo-Funktion |Sk| mod 2 der Gleichung (5) auf Seite
732. Dabei wird die Summe Sk über sämtliche Koeffizienten an gebildet (Seite 732,

                                          - 64 -



Gl. (4), siehe Sk), zu der trivialerweise lediglich die Koeffizienten ungleich Null, d. h.
die Restdaten der bestimmten Untergesamtheit, beitragen.


Weil die Summe sämtlicher Koeffizienten der aktuellen Partition somit der Summe
der Koeffizienten der Untergesamtheit entspricht, ist Merkmal M1.6 in Druckschrift
NK1 offenbart.


Der Codierer vergleicht den berechneten Funktionswert mit der Parität des
MVComp-Flags i, das die Werte 0 oder 1, also „gerade“ oder „ungerade Parität“
annehmen kann.


In Abhängigkeit vom Ergebnis des Vergleichs wird entschieden, ob einer der
Koeffizienten an≠0 modifiziert werden muss, um die erforderliche Parität zu erhalten.


Vergleich und Modifikation i. S. d. Merkmale M1.7 und M1.8 gehen insbesondere
hervor aus Seite 732, rechte Spalte, Abschnitt IV.A., vorletzter Absatz (siehe Gl. (5))
sowie Seite 733, linke Spalte, Abschnitt IV.B. (siehe Gln. (7) und (8)) der
Druckschrift NK1.


Selbstverständlich werden die transformierten Koeffizienten der Partition dann
codiert, ohne das MVComp-Flag mitzucodieren. Dies kommt aber auch auf Seite
730 i. V. m. Seite 735 der NK1 direkt zum Ausdruck, wonach die Entropiecodierung
ohne den MVComp-Index erfolgt, der versteckt wird und daher nicht zur
Übertragung vorgesehen ist (Seite 730, linke Spalte, erster Absatz, siehe „… the
difference between the selected predictor and the current block is transformed …
quantized and entropy coded.“; Seite 735, linke Spalte, Abschnitt V.A., erster
Absatz, siehe „The 4x4 DCT transform is enabled and CABAC entropy coding
method, known to provide the best results, is selected. …“; Seite 735, rechte Spalte,
Abschnitt V.B., erster Absatz, siehe „Fig. 4 gives the percentage of predictor index
transmitted and those which are not transmitted thanks to either the predictors

                                        - 65 -



equality or the index hiding. … we can note that the percentage of non-transmitted
index is higher than 30% and reaches 90% at high bitrate.“ – Merkmal M1.9).


Damit finden sich in Druckschrift NK1 alle Merkmale des Patentanspruchs 1 mit
dem einzigen Unterschied, dass hier kein Vorzeichen (Merkmal M1.7.1), sondern
ein MVComp-Flag „verborgen“ übertragen wird.


2.2           Das    verbliebene     Unterschiedsmerkmal       M1.7.1     kann    eine
Patentfähigkeit nicht begründen.


Gemäß der Lehre der Druckschrift NK1 wird der MVComp-Index versteckt, d. h.
eine bestimmte Bewegungsvektorinformation aus dem MVComp-Tool. Die
Druckschrift NK1 weist aber darauf hin, dass der Nutzen beim Verstecken der
vorgeschlagenen Information eher gering und die Auswahl des MVComp-Index
lediglich beispielhaft ist (Seite 731, linke Spalte, erster vollständiger Absatz, siehe
„The most studied is to hide information in the nonzero DCT coefficients of a
compressed video stream“; Seite 731, rechte Spalte, letzter Absatz, siehe „Hiding
data in pixels residuals …“; Seite 732, linke Spalte, Abschnitt III.B., erster Absatz,
siehe „As a consequence, the data to be hidden can be all the competition
information generated for each macroblock …“; dritter Absatz, siehe „According to
these values, it is already known that the overall gain of the proposed approach will
remain low.“). Dementsprechend schlägt die Druckschrift NK1 in Abschnitt VII. vor,
das beschriebene Data Hiding auch auf andere Wettbewerbsindizes anzuwenden
und dabei auf dessen Einfluss auf die Chroma-Komponente achtzugeben (Seite
740, rechte Spalte, siehe „The proposed method consequently appears as a nice
and efficient way to reduce the cost of other more costly competition indices while
taking care of the impact on the chroma component.“). Gleichzeitig weist die
Druckschrift NK1 an mehreren Stellen auf die Bedeutung einer verbesserten
Codierung für die transformierten Koeffizienten hin (Seite 733, linke Spalte, zweiter
Absatz, siehe „It is important to notice that the proposed scheme has also the ability
to reduce the coding cost of the coefficients …“; Seite 736, linke Spalte, zweiter

                                       - 66 -



Absatz, siehe „… it is important to notice that the proposed scheme has potentially
a double impact on the coding efficiency: first, the decrease of the coding cost due
to the index non-transmission, and second, the improvement of transform
coefficients coding by the removal of useless coefficients.”) sowie darauf, dass
Bildinformationen in Pixelwerten verborgen werden können, die aus einer Wavelet-Transformation hervorgegangen sind (Seite 731, linke Spalte, dritter vollständiger
Absatz, siehe „The authors proposed to exploit data hiding to improve coding
efficiency by hiding the chrominance information in the wavelet domain of the
luminance component …“). Damit gibt die Druckschrift NK1 eine deutliche
Anregung, das Verbergen von Daten hinsichtlich verschiedener Aspekte weiter zu
untersuchen, und zwar nicht nur für Wettbewerbsindizes, sondern gleichermaßen
für die transformierten Koeffizienten. Da der Fachmann stets bestrebt ist, die
Codierkosten für die im Videodatenstrom organisierten Informationen bei
gleichbleibender Übertragungsqualität möglichst gering zu halten, bot es sich für ihn
an, insbesondere all diejenigen Informationen auf eine Eignung für ein Data Hiding
zu überprüfen, die nicht effizient entropiecodiert bzw. komprimiert werden können.
Dass solche schlecht codierbaren Informationen in Verbindung mit den
transformierten Koeffizienten zum Prioritätszeitpunkt des Streitpatents dem
Fachmann bekannt waren, wird u. a. durch den Tagungsbeitrag NK9´ belegt.


Die dortigen Ausführungen zur arithmetischen Codierung bzw. CABAC-Systematik
geben wieder, dass auf die jeweiligen Vorzeichen der transformierten Koeffizienten
aufgrund ihrer gleichmäßigen Wahrscheinlichkeitsverteilung nur ein vereinfachtes,
unvollständiges Codierverfahren („Bypass“) angewendet werden kann (vgl. NK9´,
Seite 195/196, siehe „NOTE“; Seite 182, Tabelle 9-46, letzte Zeile; Seite 76/77,
Abschnitt 7.4.10, siehe „coeff_sign_flag[n]“), was mit Lehrbuchwissen aus der
Informationstheorie in Einklang steht, wonach eine willkürliche Information, deren
Auftrittswahrscheinlichkeit nahezu gleichverteilt ist, nicht effizient codiert bzw.
komprimiert werden kann (vgl. NK8, Seite 227, erster Absatz).

                                        - 67 -



In Kenntnis der bekannten CABAC-Systematik lag es für den Fachmann auf der
Hand, in der Lehre der Druckschrift NK1 anstelle eines Konkurrenzindex die
bitwertige   Information   betreffend   das      Vorzeichen   eines    transformierten
Koeffizienten mit Hilfe des Data Hidings zu verstecken, um auf diese Weise eine
unvollständige   arithmetische   Codierung       zu   umgehen    und    dadurch    die
Codiereffizienz deutlich zu steigern. Mit der Entscheidung für die Wahl des
Vorzeichens als zu verschleiernder digitaler Information steht außerdem eine
Mehrzahl gleichwertiger Varianten für ein Data Hiding zur Verfügung, da die
transformierten Koeffizienten im Allgemeinen über mehrere Koeffizienten ungleich
Null verfügen, deren jeweiliges Vorzeichen versteckt werden kann.


Nach allem hat Merkmal M1.7.1 sonach nahegelegen.


2.3     Die Argumentation der Beklagten hält einer näheren Überprüfung nicht
stand. Im Einzelnen:


2.3.1    Zur Merkmalsgruppe M1.5 („Untergesamtheit“ – „le sous-ensemble“)


Zwar trifft die Ansicht der Beklagten zu, dass der Codierer der Druckschrift NK1 nur
die von Null verschiedenen Koeffizienten eines Blocks modifizieren kann, wobei
eine Modifikation von Nullkoeffizienten ausdrücklich ausgeschlossen ist.


Demgegenüber ist aber darauf hinzuweisen, dass die Druckschrift NK1
insbesondere dann eine Untergesamtheit bestehend aus N von Null verschiedenen
Transformationskoeffizienten offenbart, wenn beim Durchlaufen eines Codierblocks
in einer vordefinierten Reihenfolge zwischen dem ersten und dem letzten von Null
verschiedenen Koeffizienten an keinerlei Koeffizienten gleich Null angeordnet sind.
Gerade in einem solchen Fall kann es für die Vorwegnahme des Merkmals M1.5.2
durch die Druckschrift NK1 dahingestellt sein, ob etwaige Koeffizienten mit dem
Wert Null zwischen dem ersten und letzten von Null verschiedenen Koeffizienten in
der anspruchsgemäßen Untergesamtheit enthalten sein müssen oder nicht.

                                           - 68 -




2.3.2   Zu    Merkmal       M1.7.1   („Vorzeichen      eines    Restdatenelements    der
Untergesamtheit“ – „le signe d´une donnée résiduelle du sous-ensemble“)


2.3.2.1 Wie die Beklagte richtig bemerkt, wird in der Druckschrift NK1 das Data
Hiding angewendet, um Konkurrenzindizes zu übertragen. Dabei wird der MVComp-Index als Beispiel eines Konkurrenzindex verwendet (vgl. NK1, Seite 730, linke
Spalte, vierter Absatz; Seite 732, linke Spalte, vorletzter Absatz).


Die Druckschrift NK1 kommt aber zu dem Schluss, dass die durch das Data Hiding
erzielten Biteinsparungen eher gering sind, weil der Anteil des Konkurrenzindex in
der Gesamtübertragung gering ist (vgl. NK1, Seite 740, linke Spalte, letzter Absatz
und rechte Spalte, erster Absatz, siehe „These results are closely related to the
index proportion in the total bitrate which is also low (2% in average) and …“).
Da diese Feststellung ganz allgemein für die Konkurrenzindizes gilt, weil diese nicht
häufig übertragen werden müssen, hatte der Fachmann Veranlassung, nach einer
anderen 1-bitwertigen Information als Alternative zu suchen, auf die ein Data Hiding
gewinnbringend angewandt werden kann. Da in der Druckschrift NK1 an mehreren
Textstellen    auf    die      Bedeutung       einer    effizienten    Codierung     der
Transformationskoeffizienten hingewiesen wird (vgl. NK1, Seite 733, linke Spalte,
zweiter Absatz, siehe „… the proposed scheme changes coefficients to zero in most
cases and the transform coefficients are consequently less costly.“; Seite 736, linke
Spalte, zweiter Absatz, siehe „… it is important to notice that the proposed scheme
has potentially a double impact on the coding efficiency: first the decrease of the
coding cost due to the index non-transmission, and second, the improvement of
transform coefficients coding by the removal of useless coefficients.”), hat es für den
Fachmann        nahegelegen,         den        1-bitwertigen      Bestandteil      eines
Transformationskoeffizienten – d. h. dessen Vorzeichen – für das Data-Hiding-Verfahren in Betracht zu ziehen.

                                              - 69 -



2.3.2.2 Die Beklagte argumentiert, dass die Lehre über die verbesserte Codierung
für die Koeffizienten in der Druckschrift NK1 lediglich im Zusammenhang mit der
Übertragung einer verlängerten Reihe von Nullen (aufgrund der Modifizierung eines
Koeffizienten im Data-Hiding-Verfahren) offenbart sei. Ein Hinweis darauf, Daten
der Transformationskoeffizienten und insbesondere Vorzeichen per Data Hiding zu
übermitteln, lasse sich hieraus nicht entnehmen.


Nach Ansicht des Senats können die oben unter Abschnitt 2.3.2.1 genannten
Textstellen der Druckschrift NK1 aber zumindest belegen, dass der Verbesserung
der Codierung der Transformationskoeffizienten eine besondere Bedeutung
zukommt,         was    u.     a.    darauf            zurückzuführen   ist,   dass   die
Transformationskoeffizienten in jedem Codierblock enthalten sind und damit einen
großen Anteil an der Datenmenge codierter Daten darstellen. Auch dieser Grund
spricht aus Sicht des Fachmannes dafür, die Transformationskoeffizienten auf ihre
Eignung für das Data-Hiding-Verfahren zu untersuchen.


2.3.3 Zur Frage „Wahrscheinlichkeitsverteilung und Data Hiding“


2.3.3.1 Dem Fachmann war vor dem Prioritätstag bekannt, dass das Vorzeichen
eines Transformationskoeffizienten mit besonders hohen Kosten der Signalisierung
verknüpft ist und deshalb nicht effizient entropiecodiert werden kann (vgl. NK9´
i. V. m. NK8).


Die Argumentation der Beklagten, dass es zur Begründung des Naheliegens der
Auswahl eines bestimmten Vorzeichens als verborgen zu übertragende Information
erforderlich sei, dass die zugrundeliegenden Überlegungen im Stand der Technik
im Zusammenhang mit der Verbesserung der Bild-Kodierung konkret dokumentiert
sind, woran es hier fehle, trifft nicht zu.


So untersucht die Druckschrift NK1, welchen Einfluss das Verbergen eines
Konkurrenzindex auf die Bitrate hat („bitrate change“). In diesem Zusammenhang

                                              - 70 -



wird auf Seite 732, Abschnitt IV.A. der Druckschrift NK1 unter Punkt 1) eine
Bedingung für die Anwendung des Data Hiding formuliert, die die durch das Data
Hiding erzielte Änderung der Bitrate in Beziehung setzt zu den Kosten der
Indexsignalisierung,       welche    wiederum          ein    Maß    für   die   Entropie   bzw.
Gleichverteilung des betreffenden Index darstellen. Aus der Bedingung wird klar,
dass das Data Hiding insbesondere dann problemlos angewendet werden kann,
wenn die Änderung der Bitrate klein bleibt gegenüber den Kosten der
Indexsignalisierung, was ja bei hohen Signalisierungskosten häufig und leicht erfüllt
ist. Der Fachmann wird erkennen, dass sich infolgedessen gerade Syntaxelemente
mit       hohen      Codierkosten,      wie       z.         B.     das    Vorzeichen       eines
Transformationskoeffizienten, dazu eignen, in den Transformationskoeffizienten per
Data Hiding verborgen zu werden.


2.3.3.2           Die Beklagte führt aus, dass ein Ziel des Data Hiding der Druckschrift
NK1 darin bestehe, durch die Modifikation von Transformationskoeffizienten
(insbesondere zu Null) Codiergewinne zu erzielen. Sie führt das Beispiel an, dass
die Modifikation eines Koeffizienten mit dem Wert „5“ auf den Wert „0“ insgesamt 6
Bits einsparen könne. Im Vergleich zu dieser Ersparnis sei die Ersparnis, die aus
dem Verstecken eines nicht weiter komprimierten Bits resultiert, eher gering und
wäre daher vom Fachmann als nicht entscheidend angesehen worden.


Die Argumentation der Beklagten geht bereits deswegen fehl, weil das hierzu in
Bezug genommene Beispiel nicht den Regelfall betrifft, sondern laut Druckschrift
NK1 die Modifikationen von Koeffizienten mit dem Wert „+/-5“ zu Null hin eine
Ausnahme darstellen (vgl. NK1, Seite 738, rechte Spalte, Table VIII; Seite 738,
rechte Spalte, erster Absatz, siehe „Finally, the modification mj = +/- 5 is rarely
selected because it induces reconstructed pixels too much different from the original
ones.“).


Weiterhin legt die Druckschrift NK1 dem Fachmann nahe, in dem bekannten
Codierverfahren zwei verschiedene Aspekte zu betrachten: Verbesserungen bei der

                                        - 71 -



Codierung von Koeffizienten einerseits sowie Einsparung durch die Nicht-Übertragung des versteckten Bits andererseits (vgl. NK1, Seite 736, linke Spalte,
zweiter Absatz, siehe „… it is important to notice that the proposed scheme has
potentially a double impact on the coding efficiency: first, the decrease of the coding
cost due to the index non-transmission, and second, the improvement of transform
coefficients coding by the removal of useless coefficients.“). Demnach wird der
zusätzliche Vorteil, Transformationskoeffizienten zu Null zu modifizieren, den
Fachmann nicht davon abhalten, nach weiteren Einsparmöglichkeiten zu suchen.


2.3.3.3       Ferner argumentiert die Beklagte, dass die streitpatentgemäße Lehre
im Gegensatz zur Druckschrift NK1 auch die Modifikation von Nullkoeffizienten
vorsehe, die somit nach der Modifikation einen von Null verschiedenen Wert
aufwiesen und mittels zusätzlicher Bits codiert werden müssten. Im Fall einer
solchen Modifikation komme es darauf an, dass der modifizierte Wert effizient
entropiecodiert werden könne und dass dies für den verborgenen Wert nicht
möglich   sei.   Somit   sollte   die   Wahrscheinlichkeitsverteilung    (unter   dem
Gesichtspunkt der Codiereffizienz bei einer Entropiecodierung) v. a. bei möglichen
Modifikationen von Nullkoeffizienten berücksichtigt werden, die in der Druckschrift
NK1 aber per se ausgeschlossen werden.


Hierzu ist zu bemerken, dass eine Modifikation von Koeffizienten mit dem Wert Null
nicht Gegenstand der Patentansprüche ist. Außerdem ist nicht ersichtlich, warum
ein Ausschließen der Modifikationen von Null-Koeffizienten den Fachmann davon
abhalten sollte, die Wahrscheinlichkeitsverteilung als Kriterium bei der Festlegung
auf ein zu versteckendes Datenelement heranzuziehen.


2.3.4 Zum Punkt „Überwindung von Schwierigkeiten“


Die von der Beklagten angeführten Schwierigkeiten, um vom im zitierten Stand der
Technik offenbarten Data Hiding-Verfahren zur Lehre des Streitpatents zu
gelangen, bestehen nach Ansicht des Senats nicht.

                                      - 72 -




2.3.4.1 Eine Schwierigkeit besteht nach Ansicht der Beklagten in der Festlegung
eines Transformationskoeffizienten, dessen Vorzeichen versteckt werden soll. Wie
sie weiter argumentiert, hätte der Fachmann einen Koeffizienten an einer festen
Position wie den ersten Koeffizienten eines Blocks nehmen können. Der Umstand,
dass der Koeffizient an einer festen Position den Wert Null annehmen kann, hätte
den Fachmann nach Ansicht der Beklagten davon abgehalten, das Data Hiding auf
ein Vorzeichen anzuwenden.


Der Einwand greift nicht durch. Selbstverständlich versucht der Fachmann nur die
Datenelemente zu verstecken, die sonst im Bitstrom übermittelt werden müssten.
Das Data Hiding dient ja gerade dazu, das explizite Übermitteln von
Datenelementen im Bitstrom zu vermeiden. Damit bieten sich nur die im Bitstrom zu
übermittelnden Vorzeichen der von Null verschiedenen Koeffizienten für das Data
Hiding an. Diese werden separat von den Koeffizienten im Bitstrom übermittelt.


2.3.4.2      Als weitere Schwierigkeit führt die Beklagte eine Desynchronisation
zwischen Codierer und Decodierer an, die auftreten würde, wenn das Vorzeichen
des ersten von Null verschiedenen Koeffizienten verborgen werde und
ausgerechnet dieser Koeffizient bei der Modifikation zu Null geändert werde. Die
Desynchronisation würde dann darin bestehen, dass der Decodierer einem falschen
von Null verschiedenen Koeffizienten das versteckte Vorzeichen zuweisen würde.


Hierzu ist zu bemerken, dass dem Fachmann die Desynchronisation als mögliche
Fehlerquelle im Zusammenhang mit dem Verstecken eines Konkurrenzindex
bekannt war, genauso wie die Vermeidung bestimmter Modifikationen zu ihrer
Behebung.


Denn auch die Druckschrift NK1 lehrt Regeln, die Änderungen an den
Transformationskoeffizienten zu beschränken. So wird in der Druckschrift NK1
darauf hingewiesen, dass ein Koeffizient nicht zu Null geändert werden kann, wenn

                                        - 73 -



der Block nur diesen einen von Null verschiedenen Koeffizienten enthält (vgl. NK1,
Seite 733, linke Spalte, erster Absatz, siehe „For the blocks which only contain one
non-null coefficient, this coefficient cannot be changed to zero in order to avoid the
transmission of only zeroes coefficients which will induce decoding error: … As a
result, a wrong parsing will be performed to read the index.”). Für den Fachmann
hat es daher nahegelegen, ausgehend von der Druckschrift NK1 die dort
offenbarten Regeln zur Vermeidung von Desynchronisation auf das Data Hiding
eines Vorzeichens eines Koeffizienten zu übertragen.


2.3.5 Zum Punkt „Separate Codierung des Vorzeichens“


Die Beklagte argumentiert, dass die Vorzeichenbits jedenfalls gemäß dem
H.264/AVC-Standard nicht als separate Gruppe codiert würden. Sie verweist dazu
auf ein Codefragment der Anlage NB2, wonach sich Vorzeichenbits und
Absolutwertbits im Datenstrom abwechseln würden (vgl. NB2, Seite 61, Abschnitt
7.3.5.3.3). Selbst wenn die Vorzeichen als separate Gruppe codiert würden, sei
nicht ersichtlich, dass dies dem Fachmann nahelegen könnte, anstelle eines
Konkurrenzindex das Vorzeichen eines Transformationskoeffizienten mittels Data
Hiding zu übermitteln. Ferner weist die Beklagte darauf hin, dass die Auswahl des
Vorzeichens eines Koeffizienten als mittels Data Hiding zu übermittelnde
Information auf die hierfür ggfs. erforderlichen Modifikationen der Koeffizienten
zurückwirke. Dies stelle eine Besonderheit dar, die beim Data Hiding eines
Konkurrenzindex nicht auftrete.


Die Ausführungen der Beklagten überzeugen nicht. So zeigt der von der Klägerin
vorgelegte Standardisierungsbeitrag NK9´, der sich mit dem neuen H.265-Standard
(HEVC-Standard) befasst, dass Vorzeichenbits und Datenelemente für die
Absolutbeträge als eigene Gruppen separat im Bitstrom transportiert werden. Dies
folgt unmittelbar aus der CABAC-Syntax der Seite 45, wo Syntaxelemente für
Vorzeichenbits und Beträge der Koeffizienten in aufeinanderfolgenden For-Schleifen ausgelesen werden. Da sich der Fachmann am Prioritätstag bereits mit

                                        - 74 -



dem HEVC-Standard befasst hat, hat er die Vorzeichen als gewöhnliche Flags und
eben nicht als Bestandteil der Koeffizienten betrachtet. Weiterhin ist der Druckschrift
NK1 zu entnehmen, dass das Verstecken eines Konkurrenzindex u. U. zur
Desynchronisation führt, was die Durchführbarkeit von Modifikationen an den
Koeffizienten einschränkt (siehe Abschnitt 2.3.4.2). Insoweit beeinflusst die
Auswahl des Konkurrenzindex als zu versteckende Information die Modifikationen
an den Koeffizienten, wirkt auf diese also zurück. Das Rückwirken des Versteckens
von Informationen auf die Modifikation von Transformationskoeffizienten stellt damit
keine Besonderheit des Streitpatents dar.


2.4    Damit ergibt sich der Gegenstand des erteilten Patentanspruchs 1 in
naheliegender Weise aus dem aufgezeigten Stand der Technik.


3.     Der erteilte Patentanspruch 2 kann nicht günstiger als Patentanspruch 1
beurteilt werden, da er inhaltlich nicht über diesen hinausgeht. Entsprechendes gilt
für Patentanspruch 5.


4.     Auch der Gegenstand des erteilten Patentanspruchs 3 beruht nicht auf
erfinderischer Tätigkeit.


Der auf ein „Verfahren zum Decodieren eines Datensignals“ gerichtete
Patentanspruch 3 korrespondiert in seinem Oberbegriff mit den Merkmalen M1.1,
M1.2 und M1.3.1, die Merkmale M3.3 bis M3.4 des kennzeichnenden Teils
entsprechen den Merkmalen M1.5 bis M1.6. Zur Vermeidung von Wiederholungen
sei an dieser Stelle lediglich auf die entsprechenden Ausführungen unter Abschnitt
2. hingewiesen.


Darüber hinaus lehrt die Druckschrift NK1, dass der Wert des MVComp-Index, d. h.
der Wert der versteckten Information, aus der Parität der Summe über die
decodierten transformierten Koeffizienten wiederhergestellt wird, die lediglich aus
den Koeffizienten ungleich Null bestehen. Naturgemäß bilden diese eine Teilmenge

                                        - 75 -



aller Koeffizienten des k-ten Blocks, wobei Absolutbeträge für die Koeffizienten
gleich Null nicht entropiecodiert werden (Seite 733, linke Spalte, dritter Absatz,
siehe „Finally, the index extraction at the decoder side is expressed as follows: i =
|Sk| mod 2 where i represents the extracted index of the kth block and Sk is the sum
of the decoded transform coefficients an … ). Damit sind Merkmal M3.5 und ein Teil
von Merkmal M3.5.1 offenbart.


Von der Lehre der Druckschrift NK1 unterscheidet sich die Lehre des erteilten
Patentanspruchs    3   letztendlich   nur     noch   dadurch,   dass   anstelle   eines
Wettbewerbsindex – wie in der Druckschrift NK1 – das Vorzeichen eines
transformierten Koeffizienten rekonstruiert wird (restlicher Teil von Merkmal
M3.5.1). Dass das verbliebene Unterschiedsmerkmal nahegelegen hat, ergibt sich
aber aus den vorherigen Ausführungen zu Merkmal M1.7.1.


5.    Der auf eine „Vorrichtung zum Decodieren eines Datensignals“ gerichtete
Patentanspruch 4 kann nicht günstiger als Patentanspruch 3 beurteilt werden, da er
inhaltlich nicht über diesen hinausgeht. Entsprechendes gilt für Patentanspruch 6.


6.    Da dem Streitpatent in seiner erteilten Fassung der Nichtigkeitsgrund der
mangelnden Patentfähigkeit entgegensteht, kann dahingestellt bleiben, ob die
weiter geltend gemachten Nichtigkeitsgründe der unzulässigen Erweiterung und der
mangelnden Ausführbarkeit gegeben sind.




                                            III.




Auch die Hilfsanträge bleiben ohne Erfolg.

                                         - 76 -



Der Nichtigkeitsgrund der mangelnden Patentfähigkeit besteht in den Fassungen
der Hilfsanträge I bis IV unverändert fort. Im Hinblick darauf kann dahingestellt
bleiben, ob die Fassungen jeweils zulässig sind.


1.    Hilfsantrag I kann keinen Erfolg haben, da die darin vorgenommenen
Änderungen eine Patentfähigkeit nicht begründen können.


1.1   Gemäß Hilfsantrag I ist der erteilte Patentanspruch 1 dadurch weiter
beschränkt, dass Merkmal M1.7.1 durch Merkmal Hi1M1.7.1 ersetzt werden soll
(Änderungen gegenüber Hauptantrag markiert):




Hi1M1.7.1    „ladite au moins une information numérique correspondant au signe
             d´une de la première donnée résiduelle non-nulle du sous-ensemble
             de ladite liste de données résiduelles,”


             Auf Deutsch:


H1M1.7.1     „wobei die wenigstens eine digitale Information dem Vorzeichen eines
             des   ersten   von   Null    verschiedenen   Restdatenelements   der
             Untergesamtheit Liste von Restdaten entspricht,“


1.2   Patentanspruch 1 gemäß Hilfsantrag I enthält die Merkmale seiner erteilten
Fassung sowie die zusätzliche Angabe, dass es sich bei dem verborgenen
Vorzeichen eines Restdatenelements der Untergesamtheit um das Vorzeichen des
ersten von Null verschiedenen Restdatenelements der Listendarstellung des Blocks
handelt.


Die Patentansprüche 2 bis 4 werden entsprechend geändert.

                                          - 77 -



1.3    Mit Rücksicht auf den aus der Druckschrift NK1 bekannten Stand der Technik
beruht der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag I nicht auf
erfinderischer Tätigkeit.


Dass der streitpatentgemäße Decodierer das zu rekonstruierende Datenelement
überhaupt ermitteln kann, macht es naturgemäß erforderlich, dass es zwischen
Codierer und Decodierer eine Vereinbarung darüber gibt, welches Vorzeichen eines
Transformationskoeffizienten verborgen werden soll. Demnach kann die Festlegung
auf ein spezielles Datenelement nicht über die Merkmale des Hauptantrags hinaus
zur erfinderischen Tätigkeit von Hilfsantrag I beitragen.


Nichts Anderes gilt, wenn die Lehre der Druckschrift NK1 auf das Verstecken eines
Vorzeichens angewendet wird. Es muss dann zwangsläufig derjenige Koeffizient
festgelegt werden, dessen Vorzeichen verborgen wird, damit Codierer und
Decodierer synchronisiert sind. Trivialerweise kommt dafür auch nur ein Koeffizient
ungleich Null in Frage, weil Null-Koeffizienten kein Vorzeichen haben. Die
Vorzeichenbits für einen Codierblock sind dabei als Gruppe von Bits codiert (vgl.
NK9´), wobei die Festlegung auf einen ganz bestimmten Koeffizienten für das zu
versteckende Vorzeichen, z. B. den ersten, zweiten oder dritten Koeffizienten, im
vorliegenden Fall eine Patentfähigkeit nicht begründen kann. Vielmehr ist das
Festlegen    auf   das      „Vorzeichen    des     ersten   von   Null   verschiedenen
Restdatenelements der Liste von Restdaten“ als eine letztlich „beliebige“
Maßnahme zu verstehen, die keine erkennbaren Vor- oder Nachteile hat, sondern
eher ohne bestimmten Grund getroffen worden ist. Dem Streitpatent ist keine
Begründung oder Erläuterung zu dieser Maßnahme oder Angabe besonderer
Vorteile entnehmbar. Damit ist sie entsprechend der Entscheidung BGH, Urteil vom
24. September 2003, X ZR 7/00, GRUR 2004, 47 – Blasenfreie Gummibahn I zu
beurteilen: „Eine von einem bestimmten Zweck oder Ergebnis losgelöste, letztlich
nach Belieben getroffene Auswahl ist für sich grundsätzlich nicht geeignet, eine
erfinderische Tätigkeit zu begründen.“ (vgl. auch BGH, Urteil vom 22. Mai 2007,
X ZR 56/03, GRUR 2008, 56 – injizierbarer Mikroschaum).

                                       - 78 -



Selbst wenn davon ausgegangen würde, dass der erste und letzte Koeffizient
ungleich Null der Untergesamtheit für ein Verstecken des Vorzeichens im Rahmen
des Data Hidings deshalb in besonderer Weise geeignet sind, weil sie trivialerweise
stets zur Verfügung stehen (zumindest gilt dies für eine Untergesamtheit mit
wenigstens zwei Koeffizienten ungleich Null), so würde doch die Festlegung auf
einen dieser beiden Koeffizienten auf Zweckmäßigkeitserwägungen beruhen und
letztendlich auch ins Belieben des Fachmannes gestellt sein, was wiederum eine
erfinderische Tätigkeit nicht begründen könnte.


Darüber hinaus ist generell auch nicht erkennbar, dass die Wahl des Koeffizienten,
dessen Vorzeichen versteckt werden soll, in irgendeiner Weise auf „technische“
Überlegungen zurückgeht oder irgendeinen Beitrag zur Lösung eines technischen
Problems leistet. Außer Frage steht, dass es eine Vereinbarung zwischen Codierer
und Decodierer darüber geben muss, welches der Vorzeichen verborgen werden
soll; ob man hierfür aber aus einer Menge an sich gleichwertiger Koeffizienten den
ersten oder irgendeinen anderen Koeffizienten heranzieht, bedarf keiner
„technischen“ Überlegungen, sondern ist im Grunde ins Belieben des Fachmanns
gestellt. Weil aufgrund der Streitpatentschrift kein technischer Bezug hergestellt
werden kann, ist dieser Aspekt des Merkmals H1M1.7.1 bei der Prüfung auf
erfinderischer Tätigkeit nicht zu berücksichtigen (entspr. BGH, Urteil vom
26. Oktober 2010, X ZR 47/07, GRUR 2011, 125 – Wiedergabe topografischer
Informationen; BGH, Urteil vom 18. Dezember 2012, X ZR 3/12, GRUR 2013, 275
– Routenplanung: Bei der Prüfung auf erfinderische Tätigkeit sind nur diejenigen
Anweisungen zu berücksichtigen, die die Lösung des technischen Problems mit
technischen Mitteln bestimmen oder zumindest beeinflussen.).


1.4   Unter Berücksichtigung der Ausführungen zum Hauptantrag ist auch der
Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag I nicht patentfähig, da er
nicht auf erfinderischer Tätigkeit beruht. Mit dem Patentanspruch 1 fallen auch alle
übrigen Patentansprüche des Hilfsantrags I.

                                       - 79 -



2.    Hilfsantrag II ist nicht günstiger zu beurteilen, da der Gegenstand seines
Patentanspruchs 1 nicht patentfähig ist.


2.1   Der auf das Codierverfahren gerichtete Patentanspruch 1 gemäß Hilfsantrag
II geht aus vom erteilten Patentanspruch 1 und gibt zusätzlich an, dass das
Verfahren den folgenden Schritt umfasst:


Hi2M1.5.2a „comparaison du nombre des données résiduelles du sous-ensemble
             avec un seuil prédéterminé (TSIG),“


             Auf Deutsch:


Hi2M1.5.2a „Vergleichen der Anzahl der Restdatenelemente der Untergesamtheit
             mit einem vorbestimmten Schwellenwert (TSIG),“


Weiterhin legt der Patentanspruch jetzt fest, dass die Schritte gemäß den Merkmale
M1.6 bis M1.9 (Berechnung der Summenparität, Vergleich mit dem Vorzeichen,
Modifikation und Codierung ohne das Vorzeichen) ausgeführt werden nach
Maßgabe des Merkmals Hi2M1.5.2b:


Hi2M1.5.2b „si le nombre des données résiduelles du sous-ensemble est
             supérieur au seuil (TSIG), ledit procédé de codage mettant en oeuvre
             les étapes de:“


             Auf Deutsch:


Hi2M1.5.2b „wobei das Codierungsverfahren die folgenden Schritte umfasst, wenn
             die Anzahl der Restdatenelemente der Untergesamtheit größer als der
             Schwellenwert (TSIG) ist:“

                                        - 80 -



Der auf das Decodierverfahren gerichtete Patentanspruch 3 sowie die auf die
Vorrichtungen gerichteten Patentansprüche 2 und 4 werden entsprechend dem
Verfahrensanspruch 1 geändert. Die Patentansprüche 5 und 6 entsprechen den
erteilten Patentansprüchen 5 und 6.


2.2     Die   vorgenommenen Änderungen            können     eine    Patentfähigkeit der
beanspruchten Lehre nicht begründen, da sie aus dem Stand der Technik
nahegelegt sind.


So beschreibt die Druckschrift NK1 an mehreren Textstellen, dass sich die Anzahl
zur Verfügung stehender Transformationskoeffizienten auf das Data Hiding auswirkt
und insbesondere das Verbergen in den Transformationskoeffizienten ineffizienter
wird, wenn weniger Transformationskoeffizienten zum Modifizieren zur Verfügung
stehen. Diese Textpassagen sind
Seite 734, rechte Spalte, Abschnitt C, erster Absatz: „… a key feature of the
proposed scheme is to have enough transform coefficients to easily balance
between rate and distortion modification.”;
Seite 736, linke Spalte, zweiter Absatz:         „Indeed, due to the decrease of the
transform coefficients available for hiding, the efficiency of the scheme decreases
for lower bitrates and becomes quasi-negligible for very low bitrates …”
sowie
Seite 736, linke Spalte, dritter Absatz: „The efficiency of the proposed scheme is
related to the number of transform coefficients available.”.


Angesichts der angeführten Textstellen wird der Fachmann durch die Druckschrift
NK1 unmittelbar veranlasst, die aus der Druckschrift NK1 bekannte Lehre derart zu
modifizieren, dass das Durchführen des Data-Hiding-Verfahrens von der Anzahl der
verfügbaren    Transformationskoeffizienten       abhängt.     Die    Einführung   eines
Schwellenwerts, mit dem die Anzahl modifizierbarer Koeffizienten verglichen wird,
hat in diesem Zusammenhang für den Fachmann zumindest nahegelegen.

                                          - 81 -



2.4   Unter Berücksichtigung der Ausführungen zum Hauptantrag ist somit auch
der Gegenstand des Patentanspruchs 1 in der Fassung des Hilfsantrags II nicht
patentfähig,   da    er   nicht   auf   erfinderischer   Tätigkeit   beruht.   Mit   dem
Patentanspruch 1 fallen auch die übrigen Patentansprüche des Hilfsantrags II.


3.    Hilfsantrag III kann keinen Erfolg haben, weil der Gegenstand seines
Patentanspruchs 1 durch die Druckschrift NK1 nahegelegt ist.


3.1   Hilfsantrag III ist eine Kombination der Hilfsanträge I und II.


3.2   Es gelten die Ausführungen zu Hilfsantrag I und II. Demnach beruht die Lehre
des Patentanspruchs 1 gemäß Hilfsantrag III nicht auf erfinderischer Tätigkeit.


4.    Hilfsantrag IV bleibt ohne Erfolg, weil sein Patentanspruch 1 nichts
Zusätzliches enthält, was eine Patentfähigkeit tragen könnte.


4.1   Der Hilfsantrag IV legt zusätzlich zu den Merkmalen des Hilfsantrags III den
Schwellenwert auf „4“ fest. So enthält Patentanspruch 1 gemäß Hilfsantrag IV noch
das Merkmal Hi4M1.5.2i, das zwischen den Merkmalen Hi4M1.5.2a und
Hi4M1.5.2b eingeschoben wird:


Hi4M1.5.2i     „le seuil ayant une valeur de 4,“


               Auf Deutsch:


Hi4M1.5.2i     „wobei der Schwellenwert den Wert 4 hat,“


Eine entsprechende Änderung wurde in den Patentansprüchen 2 bis 4
vorgenommen.

                                         - 82 -



4.2   Der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag IV ergibt sich in
naheliegender Weise aus dem aufgezeigten Stand der Technik.


So wird im Streitpatent an genau zwei Textstellen darauf hingewiesen, dass der
Schwellenwert gleich „4“ ist. Bei diesen Textstellen handelt es sich um die Absätze
[0068] und [0124] der Streitpatentschrift. Die Ausführungen des Streitpatents in
Hinblick auf gerade diesen Wert gehen nicht über die bloße Zahlenangabe hinaus.
Ausführungen     zu   etwaigen     mit   diesem   Wert   verbundenen   technischen
Besonderheiten sind dem Streitpatent nicht zu entnehmen. Aus Sicht des Senats
handelt es sich bei dem Schwellenwert gleich „4“ um eine willkürliche Festlegung,
die im Belieben des Fachmannes liegt und keinen technischen Beitrag liefern kann.


4.3   Mit Blick auf die Ausführungen zum Hauptantrag sowie Hilfsantrag I und II
beruht auch der Gegenstand des Patentanspruchs 1 gemäß Hilfsantrag IV nicht auf
erfinderischer Tätigkeit und ist sonach nicht patentfähig. Mit seinem Patentanspruch
1 fällt der gesamte Hilfsantrag IV.


5.    Aus diesen Gründen war das Streitpatent, das somit in keiner seiner durch
die Beklagte verteidigten Fassungen bestandsfähig ist, insgesamt für nichtig zu
erklären.




                                          IV.




Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                        - 83 -



                                         V.


                                Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt      schriftlich   beim   Bundesgerichtshof,      Herrenstraße     45a,
76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht         (BGH/BPatGERVV)      auf   elektronischem   Weg    beim
Bundesgerichtshof einzulegen, wird hingewiesen (www.bundesgerichtshof.de/
erv.html).




Hartlieb       Dr. Forkel        Dr. Himmelmann         Dr. Städele        Dr. Harth
