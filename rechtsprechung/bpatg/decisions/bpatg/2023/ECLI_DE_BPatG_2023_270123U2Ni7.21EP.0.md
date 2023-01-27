---
ecli: "ECLI:DE:BPatG:2023:270123U2Ni7.21EP.0"
court: "Bundespatentgericht"
spruchkoerper: "2"
aktenzeichen: "2 Ni 7/21"
decided: "2023-01-27"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2023&Sort=1&Seite=2&nr=43641&anz=529&pos=32&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2023-01-27_2_Ni_7_21_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0001.md", "germany/bund/acts/patg/0014.md", "germany/bund/acts/patg/0081.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/patg/0110.md", "germany/bund/acts/patg/0125a.md", "germany/bund/acts/zpo/0002.md", "germany/bund/acts/zpo/0092.md", "germany/bund/acts/zpo/0100.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 2 Ni 7/21 vom 2023-01-27

## Entscheidung

BUNDESPATENTGERICHT

                      IM NAMEN DES VOLKES

                                 URTEIL
                                                        Verkündet am
 2 Ni 7/21 (EP)                                        27. Januar 2023
verbunden mit                                                 …
2 Ni 37/21 (EP)

(Aktenzeichen)



                      In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2023:270123U2Ni7.21EP.0

                                      -2-




             betreffend das europäische Patent EP 2 559 245
                           (DE 60 2011 018 663)




hat der 2. Senat (Nichtigkeitssenat) des Bundespatentgerichts aufgrund der
mündlichen Verhandlung vom 27. Januar 2023 durch die Vorsitzende Richterin
Hartlieb sowie die Richter Dipl.-Ing. Baumgardt, Dipl.-Ing. Univ. Hoffmann,
Dr. Himmelmann und Dipl.-Phys. Univ. Dr. Städele für Recht erkannt:



I.     Das europäische Patent EP 2 559 245 wird mit Wirkung für das
       Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig
       erklärt, dass seine Ansprüche 1 und 11 folgende Fassung erhalten:

-3-

-4-

                                       -5-




II.    Im Übrigen werden die Klagen abgewiesen.


III.   Die Kosten des Rechtsstreits tragen die Klägerinnen jeweils zu 1/2.


IV.    Das Urteil ist gegen Sicherheitsleistung in Höhe von 120 % des jeweils zu
       vollstreckenden Betrages vorläufig vollstreckbar.




                                 Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für die Bundesrepublik Deutschland
in englischer Verfahrenssprache erteilten europäischen Patents EP 2 559 245
(deutsches Aktenzeichen DE 60 2011 018 663) (Streitpatent), das am 8. April 2011
angemeldet worden ist und das die Bezeichnung „VIDEO CODING USING MULTI-TREE SUB-DIVISIONS OF IMAGES“ (MULTI-TREE UNTERTEILUNG VON

                                         -6-


BILDERN FÜR VIDEOKODIERUNG) trägt. Das Streitpatent geht auf die PCT-Anmeldung WO 2011/128269 zurück und nimmt die Prioritäten der EP-Anmeldung
EP 1015819.1 sowie der PCT-Anmeldung PCT/EP2010/054843, jeweils vom
13. April 2010, in Anspruch.


Das Streitpatent betrifft Codierungsschemata zum Codieren eines räumlich
abgetasteten Informationssignals unter Verwendung von Unterteilungen und
Codierungsschemata       zum      Codieren     einer   Unterteilungs-        oder    einer
Mehrbaumstruktur, wobei sich repräsentative Ausführungsformen auf Bildund/oder      Videocodierungsanwendungen           beziehen         (vgl.    Streitpatent,
Absatz [0001]). Gemäß dem Streitpatent werden bei der Bild- und Videocodierung
die Bilder oder bestimmte Sätze von Abtastwerte-Arrays für die Bilder üblicherweise
in Blöcke zerlegt, die bestimmten Codierparametern zugeordnet sind.


Das im Umfang der Patentansprüche 1 und 11 angegriffene Streitpatent umfasst 14
Patentansprüche, wobei Anspruch 1 auf einen Decodierer gerichtet ist. Der
nebengeordnete Anspruch 11 ist auf ein Decodierverfahren, der nebengeordnete
Anspruch 12 auf einen Codierer, der nebengeordnete Anspruch 13 auf ein
Verfahren zum Codieren und der nebengeordnete Anspruch 14 auf ein
computerlesbares digitales Speichermedium gerichtet. Die Unteransprüche 2 bis 10
beziehen sich direkt oder indirekt auf Anspruch 1.


Der erteilte Patentanspruch 1 lautet in der Verfahrenssprache Deutsch gemäß
EP 2 559      245   B1   (mit    an   die    Anlage    NK     III    der     X…     GmbH,
Düsseldorf,    angelehnter      Merkmalsgliederung,    wobei        einige    sprachliche
Klarstellungen vorgenommen wurden):


Patentanspruch 1:
a) Decodierer, der folgende Merkmale aufweist:
b) einen Extrahierer (102), der ausgebildet ist,
     b1)      um     eine       maximale       Regionsgröße          und      Mehrbaum-Unterteilungsinformationen aus einem Datenstrom zu extrahieren;

                                           -7-


     b2)     um untergeordnete Mehrbaum-Unterteilungsinformationen aus dem
             Datenstrom zu extrahieren (rekonstruieren); und
     b3)     um eine weitere maximale Regionsgröße aus dem Datenstrom zu
             extrahieren;
c) einen Unterteiler (104a), der ausgebildet ist,
       c1)    um ein Array von Informationsabtastwerten, die ein räumlich
              abgetastetes        Informationssignal      darstellen,       räumlich     in
              Baumwurzelregionen der maximalen Regionsgröße zu teilen und
              zumindest einen Teilsatz der Baumwurzelregionen gemäß einer
              Mehrbaum-Unterteilungsinformation in kleinere einfach verbundene
              Regionen mit unterschiedlichen Größen zu unterteilen, und zwar
              durch   rekursives      Mehrfachpartitionieren      des     Teilsatzes   von
              Baumwurzelregionen; und
d) einen Rekonstruierer (106), der ausgebildet ist,
       d1)    um das Array von Abtastwerten unter Verwendung der Unterteilung in
              die kleineren einfach verbundenen Regionen aus dem Datenstrom zu
              rekonstruieren; und
       d2)    um eine Vorhersage des Arrays von Informationsabtastwerten mit
              einer Granularität durchzuführen, die von der Unterteilung in kleinere
              einfach verbundene Regionen abhängt;
e) einen weiteren Unterteiler (104a), der ausgebildet ist,
       e1)    um         gemäß          den         untergeordneten            Mehrbaum-Unterteilungsinformationen zumindest einen Teilsatz der kleineren
              einfach verbundenen Regionen in noch kleinere einfach verbundene
              Regionen       zu    unterteilen,     und    zwar      durch      rekursives
              Mehrfachpartitionieren       des    Teilsatzes   der      kleineren   einfach
              verbundenen Regionen;
der Rekonstruierer ist ausgebildet,
       d3)    um eine Retransformation aus einem Spektral- in einen räumlichen
              Bereich in Einheiten der noch kleineren einfach verbundenen
              Regionen durchzuführen;
der weitere Unterteiler ist ausgebildet,

                                   -8-


e2)   um jede kleinere einfach verbundene Region, die die weitere
      maximale Regionsgröße überschreitet, in Baumwurzel-Teilregionen
      der weiteren maximalen Regionsgröße zu teilen und zumindest den
      Teilsatz der Baumwurzel-Teilregionen gemäß den untergeordneten
      Mehrbaum-Unterteilungsinformationen in die noch kleineren einfach
      verbundenen Regionen zu unterteilen;
e3)   um beim Unterteilen des Teilsatzes kleinerer einfach verbundener
      Regionen für jede kleinere einfach verbundene Region zu prüfen
      (402), ob die jeweilige kleinere einfach verbundene Region die weitere
      maximale Regionsgröße überschreitet, und wenn die jeweilige
      kleinere    einfach   verbundene         Region     die    weitere     maximale
      Regionsgröße      überschreitet,        die    jeweilige    kleinere     einfach
      verbundene      Region in Baumwurzel-Teilregionen                  der weiteren
      maximalen Regionsgröße zu teilen;
e4)   für jede Baumwurzel-Teilregion
      e4.1) die    untergeordneten       Mehrbaum-Unterteilungsinformationen
            dahin gehend zu prüfen (304), ob die jeweilige Baumwurzel-Teilregion partitioniert werden soll;
      e4.2) und wenn die jeweilige Baumwurzel-Teilregion partitioniert
            werden soll,
            e4.2.1)         die jeweilige Baumwurzel-Teilregion in Teil-Teilregionen zu partitionieren (306), und
            e4.2.2)         die Prüfung und Partitionierung (304, 306) für die
                            Teil-Teilregionen rekursiv zu wiederholen, bis
                            gemäß        den        untergeordneten        Mehrbaum-Unterteilungsinformationen            keine        weitere
                            Partitionierung mehr durchgeführt werden soll
                            oder eine weitere maximale Hierarchieebene
                            erreicht ist;
e5)   wobei für eine kleinere einfach verbundene Region, die die weitere
      maximale     Regionsgröße       nicht     überschreitet,     die     Teilung   in
      Baumwurzel-Teilregionen ausgelassen wird.

                                             -9-


Der erteilte Patentanspruch 11 lautet in der Verfahrenssprache Deutsch gemäß
EP 2 559      245     B1    (mit    an     die    Anlage     NK    III   der      X…   GmbH,
Düsseldorf,    angelehnter         Merkmalsgliederung,        wobei      einige    sprachliche
Klarstellungen vorgenommen wurden):


Patentanspruch 11:
a)    Decodierverfahren, das folgende Schritte aufweist:
b)    Extrahieren (102)
      b1)     einer        maximalen        Regionsgröße          und     von      Mehrbaum-Unterteilungsinformationen aus einem Datenstrom;
      b2)     von untergeordneten Mehrbaum-Unterteilungsinformationen aus dem
              Datenstrom; und
      b3)     von einer weiteren maximalen Regionsgröße aus dem Datenstrom;
c)    räumliches Teilen (104a)
      c1)     eines Arrays von Informationsabtastwerten, die ein räumlich
              abgetastetes Informationssignal darstellen, in Baumwurzelregionen
              der maximalen Regionsgröße und Unterteilen zumindest eines
              Teilsatzes der Baumwurzelregionen gemäß einer Mehrbaum-Unterteilungsinformation in kleinere einfach verbundene Regionen mit
              unterschiedlichen Größen durch rekursives Mehrfachpartitionieren
              des Teilsatzes von Baumwurzelregionen;
d)    Rekonstruieren (106)
      d1)     des Arrays von Abtastwerten aus dem Datenstrom unter Verwendung
              der Unterteilung in die kleineren einfach verbundenen Regionen,
      d2)     wobei die Rekonstruktion ein Vorhersagen des Arrays von
              Informationsabtastwerten mit einer Granularität aufweist, die von der
              Unterteilung in kleinere einfach verbundene Regionen abhängt;
e)    eine weitere Unterteilung (104a)
      e1)     zumindest eines Teilsatzes der kleineren einfach verbundenen
              Regionen             gemäß         den       untergeordneten         Mehrbaum-Unterteilungsinformationen in noch kleinere einfach verbundene
              Regionen durch rekursives Mehrfachpartitionieren des Teilsatzes der
              kleineren einfach verbundenen Regionen;

                                        - 10 -


wobei die Rekonstruktion aufweist
      d3)   ein Durchführen einer Retransformation aus einem Spektral- in einen
            räumlichen Bereich in Einheiten der noch kleineren einfach
            verbundenen Regionen;


wobei die weitere Unterteilung aufweist


      e2)   ein Teilen jeder kleineren einfach verbundenen Region, die die weitere
            maximale Regionsgröße überschreitet, in Baumwurzel-Teilregionen
            der weiteren maximalen Regionsgröße und ein Unterteilen zumindest
            des    Teilsatzes     der     Baumwurzel-Teilregionen                gemäß     den
            untergeordneten Mehrbaum-Unterteilungsinformationen in die noch
            kleineren einfach verbundenen Regionen;
      e3)   wobei das Unterteilen des Teilsatzes kleinerer einfach verbundener
            Regionen       folgende     Schritte      aufweist:         Prüfen     (402)   der
            untergeordneten      Mehrbaum-Unterteilungsinformationen                 für   jede
            kleinere einfach verbundene Region dahin gehend, ob die jeweilige
            kleinere   einfach    verbundene          Region      die    weitere    maximale
            Regionsgröße überschreitet, und wenn die jeweilige kleinere einfach
            verbundene       Region     die      weitere       maximale          Regionsgröße
            überschreitet, Teilen der jeweiligen kleineren einfach verbundenen
            Region in Baumwurzel-Teilregionen für die weitere maximale
            Regionsgröße;
      e4)   für jede Baumwurzel-Teilregion
            e4.1) Prüfen     (304),     ob    die     jeweilige    Baumwurzel-Teilregion
                   partitioniert werden soll;
            e4.2) wenn die jeweilige Baumwurzel-Teilregion partitioniert werden
                   soll,
                   e4.2.1)       Partitionieren (306) der jeweiligen Baumwurzel-Teilregion in Teil-Teilregionen, und
                   e4.2.2)       rekursives Wiederholen des Prüfens (304) und
                                 Partitionierens (306) für die Teil-Teilregionen, bis
                                 gemäß          den     untergeordneten            Mehrbaum-

                                        - 11 -


                                  Unterteilungsinformationen         keine       weitere
                                  Partitionierung durchgeführt werden soll oder
                                  (die) eine weitere maximale Hierarchieebene
                                  erreicht ist;
        e5)   wobei für eine kleinere einfach verbundene Region, die die weitere
              maximale    Regionsgröße      nicht   überschreitet,   die     Teilung   in
              Baumwurzel-Teilregionen ausgelassen wird.


Die Klägerin 1 stützt ihre Klage auf den Nichtigkeitsgrund der mangelnden
Patentfähigkeit mit Blick auf fehlende erfinderische Tätigkeit. Die Klägerin 2 stützt
ihre Klage auf die Nichtigkeitsgründe der mangelnden Patentfähigkeit mit Blick auf
fehlende Neuheit und fehlende erfinderische Tätigkeit sowie darauf, dass das
Streitpatent die Erfindung nicht so deutlich und vollständig offenbare, dass ein
Fachmann sie ausführen könne.


Zur Stützung ihres Vorbringens hat die Klägerin 1 die folgenden Dokumente
genannt:
NK 1          EP 2 559 245 B1 (Streitpatentschrift);
NK 2          Verletzungsklage (Schriftsatz der Beklagten an das Landgericht
              Düsseldorf, Zivilkammer 4c, vom 3. September 2020,
              Geschäftsnummer 4 c O 42/20);
NK 3          DPMA: Registerauszug zum Aktenzeichen 60 2011 018 663.9, Stand
              am 17.12.2020;
NK 4          Merkmalsgliederung Anspruch 1;
NK 5          Merkmalsgliederung Anspruch 11;
NK 6          US 2010/0086031 A1;
NK 7          Recommendation ITU-T H.264, „Advanced video coding for generic
              audiovisual services“ (in Auszügen), mit Datumsangabe „11/2007“;
NK 8          US 5,999,655 A;
NK 9          US 5,241,395 A;
NK 10         US 5,021,891.

                                      - 12 -


Zur Stützung ihres Vorbringens hat die Klägerin 2 die folgenden Dokumente
genannt:
NK A         Schriftsatz der Beklagten an das Landgericht München I,
             Patentstreitkammer, vom 19. März 2021;
NK B         M…, Expert Opinion; November 12, 2022;
NK I-DE      Europäisches Aktenzeichen: 11 714 644.9; Videocodierung unter
             Verwendung von Mehrbaum-Unterteilungen von Abbildungen;
NK I         EP 2 559 245 B1 (Streitpatentschrift);
NK II        DPMA: Registerauszug zum Aktenzeichen 60 2011 018 663.9, Stand
             am 11.10.2021;
NK III       Merkmalsgliederung zu Patentansprüchen 1 und 11 des
             Europäischen Patents EP 2 559 245 B1;
NK IV        WO 2011/128269 A1;
NK V         PCT/EP2010/054843;
NK 1         EP 3 461 130 A1;
NK 2         EP 3 261 344 A1;
NK 2b-ÜS     PCT/KR2010/007257, beglaubigte Übersetzung aus der koreanischen Sprache;
NK 3         Cheng-Tie Chen, „Adaptive transform coding via quadtree-based
             variable block size DCT“, in: International Conference on Acoustics,
             Speech, and Signal Processing, 1989, S. 1854-1857;
NK 4         Jacques Vaisey und Allen Gersho, „Image compression with variable
             block size segmentation,“ IEEE Transactions on Signal Processing,
             1992, Ausgabe 40, Nr. 8, S. 2040-2060;
NK 5         JCTVC-A124;
NK 6         US 2010/0086031 A1.


Die Klägerinnen stellen den Antrag,
             das europäische Patent EP 2 559 245 mit Wirkung für das
             Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der
             Ansprüche 1 und 11 für nichtig zu erklären.

                                      - 13 -


Die Beklagte stellt den Antrag,
             die Klagen abzuweisen,
             hilfsweise
             das europäische Patent EP 2 559 245 unter Klageabweisung im
             Übrigen mit Wirkung für das Hoheitsgebiet der Bundesrepublik
             Deutschland insoweit für nichtig zu erklären, als seine Ansprüche 1
             und 11 über die Fassung eines der Hilfsanträge I vom 27. September
             2022, II vom 14. November 2022, III vom 27. September 2022 sowie
             IV bis XI vom 19. Dezember 2022 – in dieser Reihenfolge –
             hinausgehen.


Die Beklagte, die das Streitpatent mit einem Hauptantrag und hilfsweise beschränkt
mit elf Hilfsanträgen verteidigt, tritt der Argumentation der Klägerinnen in allen
wesentlichen Punkten entgegen. Sie vertritt die Auffassung, dass das beanspruchte
Verfahren und die beanspruchte Vorrichtung ursprünglich offenbart, also ausführbar
und sowohl neu seien als auch auf einer erfinderischen Tätigkeit des Fachmanns
beruhten. Die beanspruchte Lehre sei jedenfalls in einer der Fassungen der
Hilfsanträge patentfähig.


Zur Stützung ihres Vorbringens hat die Beklagte die folgenden Dokumente genannt:


ES 1a        PCT/KR2010/005436 (Priorität der NK 1 (Koreanisch));
ES 1b        Englische Übersetzung der Priorität der NK 1;
ES 2a        PCT/KR2010/007257 (Priorität der NK 2 (Koreanisch));
ES 2b        Englische Übersetzung der Priorität der NK 2;
ES 2c        Beglaubigte Übersetzung eines Ausschnitts der ES 2a.


Der Wortlaut des Hilfsantrags I vom 27. September 2022 ist dem Tenor unter I. zu
entnehmen.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.

                                          - 14 -


                              Entscheidungsgründe




Die Klagen, mit denen der Nichtigkeitsgrund der fehlenden Patentfähigkeit nach
Art. II § 6   Abs. 1 Satz 1    Nr.    1 IntPatÜbkG         i. V. m.   Art. 138   Abs. 1 lit. a)
EPÜ i. V. m. Art. 52, 54, 56 EPÜ und der Nichtigkeitsgrund der unzureichenden
Offenbarung nach Art. II § 6 Abs. 1 Satz 1 Nr. 2 IntPatÜG, Art. 138 Abs. 1 lit. b)
EPÜ i. V. m. Art. 83 EPÜ geltend gemacht werden, sind nach § 81 PatG zulässig.


Die Klagen sind insoweit begründet, als das Streitpatent im tenorierten Umfang für
nichtig zu erklären ist.




                                            I.



1.       Das Streitpatent betrifft Codierungsschemata zum Codieren eines räumlich
abgetasteten Informationssignals unter Verwendung von Unterteilungen und
Codierungsschemata         zum       Codieren      einer     Unterteilungs-      oder    einer
Mehrbaumstruktur (vgl. Streitpatentschrift, Absatz [0001]).


Gemäß dem Streitpatent werden bei der Bild- und Videocodierung die Bilder oder
bestimmte Sätze von Abtastwerte-Arrays für die Bilder üblicherweise in Blöcke
zerlegt, die bestimmten Codierparametern zugeordnet sind.
Die Bilder bestehen normalerweise aus mehreren Abtastwerte-Arrays. Diese
können in eine oder mehrere sogenannte Ebenengruppen gruppiert werden, wobei
jede Ebenengruppe aus einem oder mehreren Abtastewerte-Arrays besteht. Die
Ebenengruppen eines Bildes können unabhängig oder, wenn das Bild mehr als
einer Ebenengruppe zugeordnet ist, mit Prädiktion aus anderen Ebenengruppen
desselben Bildes codiert werden. Jede Ebenengruppe wird normalerweise in Blöcke
zerlegt. Die Blöcke werden entweder durch Zwischenbildvorhersage oder
Intrabildvorhersage vorhergesagt. Die Blöcke können unterschiedliche Größen
haben und entweder quadratisch oder rechteckig sein. Die Aufteilung eines Bildes

                                         - 15 -


in Blöcke kann entweder durch die Syntax festgelegt oder innerhalb des Bitstroms
signalisiert werden. Für alle Abtastwerte eines Blocks ist die Decodierung der
zugehörigen      Codierungsparameter       auf    bestimmte          Weise     spezifiziert.
Beispielsweise werden alle Samples in einem Block unter Verwendung desselben
Satzes von Vorhersageparametern vorhergesagt, wie z.B. Referenzindizes,
Bewegungsparametern, Parametern zum Spezifizieren des Interpolationsfilters,
Intra-Prädiktionsmodi usw. Es ist auch möglich, dass einem einzelnen Block mehr
als ein Satz bestimmter Vorhersageparameter (wie z.B. Referenzindizes und
Bewegungsparameter) zugeordnet ist. Die Differenz zwischen den Originalblöcken
und ihren Prädiktionssignalen, auch als Restsignal bezeichnet, wird üblicherweise
transformiert und quantisiert. Oftmals wird eine zweidimensionale Transformation
auf   das   Restsignal     angewendet.   Nach     der    Transformation      werden     die
resultierenden     Transformationskoeffizienten        quantisiert     und    sogenannte
Transformationskoeffizientenlevels         erhalten.         Die         Transformationskoeffizientenlevels sowie die Vorhersageparameter und, falls vorhanden, die
Unterteilungsinformationen sind entropiecodiert (vgl. Streitpatentschrift, Absatz
[0002]).
Weiter gibt das Streitpatent an, dass in Bild- und Videocodierungsstandards die
durch die Syntax vorgegebenen Möglichkeiten zur Unterteilung eines Bildes (oder
einer Ebenengruppe) in Blöcke sehr begrenzt sind. Üblicherweise kann nur
angegeben werden, ob und (evtl. wie) ein Block einer vordefinierten Größe in
kleinere Blöcke unterteilt werden kann. Beispielsweise ist die größte Blockgröße in
dem H.264-Standard 16x16. Die 16x16-Blöcke werden auch als Makroblöcke
bezeichnet und jedes Bild wird in einem ersten Schritt in Makroblöcke unterteilt. Für
jeden 16x16-Makroblock kann signalisiert werden, ob er als 16x16-Block, als zwei
16x8-Blöcke, als zwei 8x16-Blöcke oder als vier 8x8-Blöcke codiert ist. Wenn ein
16x16-Block in vier 8x8-Blöcke unterteilt wird, kann jeder dieser 8x8-Blöcke
entweder als ein 8x8-Block, als zwei 8x4-Blöcke, als zwei 4x8-Blöcke oder als vier
4x4-Blöcke codiert werden. Die geringe Menge an Möglichkeiten zur Spezifikation
der Aufteilung in Blöcke in modernen Bild- und Videocodierungsstandards hat den
Vorteil,    dass     die     Seiteninformationsrate        zur       Signalisierung     der
Unterteilungsinformationen klein gehalten werden kann. Es hat aber den Nachteil,
dass die zum Übertragen der Vorhersageparameter für die Blöcke erforderliche

                                        - 16 -


Bitrate erheblich werden kann. Ein Codierer bestimmt normalerweise die
Unterteilung, die zum Minimum eines bestimmten Ratenverzerrungskostenmaßes
führt. Dementsprechend ermöglicht eine Unterteilung eines Bildes in eine höhere
Anzahl kleinerer Blöcke eine räumlich feinere Einstellung der Codierparameter,
wodurch eine bessere Anpassbarkeit dieser Codierparameter an das Bild-
/Videomaterial ermöglicht wird. Andererseits bedeutet das Einstellen der
Codierparameter mit einer feineren Granularität eine höhere Belastung für die
Menge an Nebeninformationen, die erforderlich ist, um den Decodierer über die
erforderlichen Einstellungen zu informieren. Darüber hinaus erhöht die Freiheit für
den Codierer, das Bild/Video räumlich (weiter) in Blöcke zu unterteilen, die Menge
möglicher Codierparametereinstellungen enorm und dadurch wird im Allgemeinen
die Suche nach der Codierparametereinstellung, die zum besten Rate/Verzerrungs-Kompromiss führt, sogar noch schwieriger (vgl. Streitpatentschrift, Absätze [0003],
[0004]).
Schließlich verweist das Streitpatent noch auf den Stand der Technik, aus dem zum
einen ein Verfahren zum Segmentieren von Bildern in Regionen mit kohärenter
Bewegung hervorgeht, wobei ein Ansatz mit mehreren Auflösungen vor der
Bewegungsschätzungsphase verwendet wird. Zum anderen ist ein adaptiver
Transformationscodierungsalgorithmus       unter   Verwendung      einer   Quadtreebasierten DCT mit variabler Blockgröße bekannt (vgl. Streitpatentschrift, Absätze
[0005], [0006]).




2.         Vor diesem Hintergrund besteht die Aufgabe des Streitpatents darin, ein
Codierungsschema zum Codieren eines Arrays von Informationsabtastwerten
bereitzustellen, die ein räumlich abgetastetes Informationssignal darstellen, wie
etwa, aber nicht beschränkt auf, Bildern eines Videos oder Standbildern, was es
ermöglicht, einen besseren Kompromiss zwischen der Codierungskomplexität und
dem        erreichbaren   Ratenverzerrungsverhältnis    und/oder     ein   besseres
Ratenverzerrungsverhältnis zu erzielen (vgl. Streitpatentschrift, Absatz [0007]).

                                        - 17 -


3.      Als zuständigen Fachmann, auf dessen Wissen und Können es für die
Auslegung des Streitpatents und für die Interpretation des Standes der Technik
ankommt, sieht der Senat einen Informatiker bzw. einen Elektrotechniker der
Fachrichtung Datenverarbeitung oder einen Physiker mit Universitätsabschluss an,
der über mehrjährige Berufserfahrung im Bereich der digitalen Bildverarbeitung
sowie der digitalen Videocodierung verfügt und mit den bei der digitalen
Videocodierung üblichen Techniken und Standards vertraut ist.




4.    Dieser Fachmann legt den Merkmalen des angegriffenen Patentanspruchs 1
des Streitpatents folgendes Verständnis zugrunde:


Gemäß Merkmal a) ist der Vorrichtungsanspruch auf einen Decodierer gerichtet.
Ein Decodierer stellt einen codierten Datenstrom wieder her, d.h. die ursprünglichen
Daten werden auf der Senderseite codiert (komprimiert), dann übertragen und auf
der Empfängerseite wieder decodiert. Der beanspruchte Decodierer umfasst einen
Extrahierer,   einen   Unterteiler,   einen      weiteren   Unterteiler   sowie   einen
Rekonstruierer.


Der Extrahierer (Merkmal b)) ist für das Extrahieren von Informationen (d.h. das
Auslesen von Informationen, welche die Codierung charakterisieren) aus dem
Datenstrom zuständig. Aus der Beschreibung ist zu entnehmen, dass diese
Informationen als „Seiteninformationen“ („side information“) übertragen werden.
Diese „Seiteninformationen“ sind Nebeninformationen im Datenstrom, die für jedes
Bild entsprechende Decodier-Informationen angeben (vgl. Streitpatentschrift,
Absätze [0043] und [0044]).


In den drei folgenden Merkmalen werden diese Informationen näher spezifiziert.


Zum einen umfassen die extrahierten Informationen eine maximale Regionsgröße
und Mehrbaum-Unterteilungsinformationen (Merkmal b1)).
Die maximale Regionsgröße kann die maximale Größe der Prädiktionsblöcke
angeben (vgl. Streitpatentschrift, Absatz [0175]). Unter Prädiktion ist dabei das

                                          - 18 -


Abschätzen bzw. das Vorhersagen von Elementen des Datenstroms zu verstehen.
Dies könnte bspw. mittels Zwischenbildvorhersage oder Intrabildvorhersage
erfolgen, wobei der Anspruchswortlaut die Art der Prädiktion offenlässt.
Die Mehrbaum-Unterteilungsinformationen geben eine erste Unterteilung bzw.
deren Granularität („erster“ Baum; „treeblock“ = Level 0, „sub-blocks“ = kleinere
einfach verbundene Regionen der Levels 1 bis 3 gemäß Merkmal c1)) an (vgl.
Streitpatentschrift, Absatz [0036] i.V.m. Fig.3A-3C).


Zum anderen werden untergeordnete Mehrbaum-Unterteilungsinformationen
(Merkmal b2)) extrahiert. Diese Informationen beschreiben die Granularität der
Unterteilung eines „zweiten“ Baumes. D.h. diese Informationen geben an, ob ein
Blatt des ersten Baumes als Wurzelknoten verwendet wird und (gemäß Merkmal
e2) und Merkmalskomplex e4)) ob und wie es weiter unterteilt wird (vgl.
Streitpatentschrift, Absätze [0050], [0052]).


Schließlich enthalten die Informationen eine weitere maximale Regionsgröße
(Merkmal b3)), welche für die Prüfung verwendet werden, ob eine jeweilige kleinere
einfach verbundene Region weiter in noch kleinere einfach verbundene Regionen
unterteilt wird (Merkmale e2) und e3)) oder ob eine „Auslassbedingung“ (Merkmal
e5)) erfüllt ist.


Somit wird ein „erster“ Baum für die Prädiktion und ein „zweiter“ Baum für die inverse
Transformation bzw. die Berechnung der „residual blocks“ auf der Ebene der noch
kleineren einfach verbundenen Regionen (vgl. Merkmal d3)) verwendet (vgl.
Streitpatentschrift, Absätze [0040], [0041]).
Gemäß den Merkmalen c) und c1) führt der (erste) Unterteiler die Aufteilung in
Regionen bzw. Blöcke anhand der extrahierten Informationen durch. Dabei wird ein
Array     von       Informationsabtastwerten,      die   ein   räumlich   abgetastetes
Informationssignal darstellen, in Blöcke mit der maximalen Regionsgröße unterteilt,
oder, wenn die Größe der Baumwurzel bereits der maximalen Regionsgröße
entspricht, wird diese nicht unterteilt. Bspw. könnte dieses Array in 4 Blöcke
unterteilt werden, wobei jede dieser 4 Regionen als Blatt bezeichnet wird (vgl.
Streitpatentschrift, Fig.4 „Level 1“). Anschließend werden u.U. einzelne dieser

                                           - 19 -


Regionen in weitere kleinere Blöcke unterteilt. Damit werden die maximalen Blöcke
oder auch nur ein Teil der maximalen Blöcke weiter unterteilt.
Unter einem Array von Informationsabtastwerten, die ein räumlich abgetastetes
Informationssignal darstellen, kann ein Bild aus Pixeln zu verstehen sein; gemäß
der Streitpatentschrift ist der Begriff „Array von Informationsabtastwerten“ aber nicht
auf Bilder beschränkt (vgl. Streitpatentschrift, Absätze [0001], [0007], [0157]).


Der Rekonstruierer (Merkmal d)) stellt die ursprünglichen Daten aus dem
Datenstrom wieder her. Dabei wird das Array von Abtastwerten unter Verwendung
der Unterteilung in die kleineren einfach verbundenen Regionen aus dem
Datenstrom rekonstruiert (Merkmal d1)) und es wird eine Vorhersage des Arrays
von Informationsabtastwerten mit einer Granularität durchgeführt, die von der
Unterteilung in kleinere einfach verbundene Regionen abhängt (Merkmal d2)). Dies
bedeutet, dass aus den Pixeln eines Blocks (Array von Abtastwerten) die
ursprünglichen Daten rekonstruiert werden, wobei eine Vorhersage dieser Daten
auf der Ebene der kleineren einfach verbundenen Regionen durchgeführt wird.


Mit dem Merkmal e) ist ein „weiterer Unterteiler“ beansprucht. Ob es sich hierbei
um einen real vorhandenen zweiten Unterteiler oder um die wiederholte
Verwendung des (ersten) Unterteilers handelt, lässt der Anspruch offen. Das
Merkmal gibt lediglich an, dass eine zusätzliche Unterteilung zumindest in einem
Teil der kleineren einfach verbundenen Regionen, d.h. der bereits in kleinere Blöcke
unterteilten Regionen (vgl. Streitpatentschrift, Absatz [0041]), stattfindet (Merkmal
e1)).
Der     Rekonstruierer   wird   nunmehr      dahingehend    konkretisiert,   dass   eine
Retransformation aus einem Spektral- in einen räumlichen Bereich in Einheiten der
noch kleineren einfach verbundenen Regionen durchgeführt wird (Merkmal d3)).
Damit     ist   die   Rücktransformation     der    Daten   aus   einem      bestimmten
Übertragungsformat (Spektralbereich) in das ursprüngliche Format (räumlicher
Bereich) beansprucht.


Der weitere Unterteiler teilt jede kleinere einfach verbundene Region, die die weitere
maximale Regionsgröße überschreitet, in Baumwurzel-Teilregionen der weiteren

                                        - 20 -


maximalen Regionsgröße und zumindest den Teilsatz der Baumwurzel-Teilregionen gemäß den untergeordneten Mehrbaum-Unterteilungsinformationen in
die noch kleineren einfach verbundenen Regionen (Merkmal e2)).
Dabei erfolgt gemäß Merkmal e3) die Unterteilung der kleineren einfachen
Regionen in noch kleinere Regionen, wenn eine Prüfung ergibt, dass die
Regionsgröße der kleineren einfachen Regionen die maximale Regionsgröße
überschreitet (vgl. Streitpatent, Absatz [0041]).


Mit dem folgenden Merkmalskomplex wird die Unterteilung der Baumwurzel-Teilregionen (Merkmal e4)) weiter ausgeführt (vgl. Streitpatent, Absatz [0041]).


Als    erstes   wird   die   untergeordnete         Mehrbaum-Unterteilungsinformation
dahingehend geprüft, ob die jeweilige Baumwurzel-Teilregion weiter partitioniert
(unterteilt) werden soll (Merkmal e4.1)).


Ergibt die Prüfung für die entsprechende Teilregion, dass eine Partitionierung
durchgeführt werden soll (Merkmal e4.2)), wird diese Region weiter partitioniert
(Merkmal e4.2.1)). Diese Prüfung und Partitionierung wird solange wiederholt, bis
keine weitere Partitionierung mehr durchgeführt werden soll bzw. eine weitere
maximale Hierarchieebene erreicht ist (Merkmal e4.2.2)). Dies bedeutet, dass die
Rekursion bis zum Erreichen eines Kriteriums wiederholt wird. Dabei ist das erste
Kriterium – keine weitere Partitionierung – eindeutig. Das zweite Kriterium gibt an,
dass ein Abbruch erfolgt, wenn eine weitere maximale Hierarchieebene, die
zusätzlich im Datenstrom codiert ist (vgl. Streitpatent, Absatz [0181], Fig.19),
erreicht ist.


Hingegen findet keine weitere Teilung einer kleineren einfach verbundenen Region
statt, wenn deren Größe die weitere maximale Regionsgröße nicht überschreitet
(Merkmal e5)). D.h. wenn eine kleinere einfach verbundene Region bereits für die
Retransformation geeignet ist (vgl. Streitpatent, Absatz [0041]), wird die kleinere
einfach verbundene Region nicht mehr weiter unterteilt. Somit werden die Schritte
der Merkmale e2) bis e4.2.2) für diese Region nicht ausgeführt.

                                        - 21 -




5.     Der auf ein Verfahren gerichtete Anspruch 11 geht inhaltlich nicht über den
Patentanspruch 1 hinaus. Zur Auslegung von dessen Merkmalen wird auf die
Ausführungen unter Abschnitt I.4 verwiesen.




6.     Dem Vorbringen der Klägerin 1 zur Auslegung der Merkmalsgruppen c) und
e) kann nur teilweise gefolgt werden.


Die Klägerin 1 gibt an, dass die Auslegung der Merkmalsgruppe c)
missverständlich sei. Sie verweist auf Sp.14 Z.14-20 der Streitpatentschrift, wonach
in Merkmal c1) zwei Schritte definiert sein sollen.
Weiterhin seien auch in der Merkmalsgruppe e) zwei Stufen beansprucht und
somit seien die Vorgaben gemäß Merkmal e2) nicht in Merkmal e3) enthalten.
Schließlich sei in Merkmal e5) nicht klar angegeben, was passiert, wenn ein
Prädiktionsblock die Maximalgröße nicht überschreitet. Diese Konstellation ließe
nicht den Schluss zu, dass ein derartiger Block nicht weiter unterteilt werden könne.


In Bezug auf Merkmal c1) ist der Klägerin 1 zuzustimmen. Denn in einem ersten
Schritt erfolgt eine Teilung in Baumwurzelregionen der maximalen Regionsgröße
und anschließend erfolgt für einen Teilsatz der Baumwurzelregionen eine Teilung
in kleinere einfach verbundene Regionen mit unterschiedlichen Größen, und zwar
durch rekursives Mehrfachpartitionieren des Teilsatzes von Baumwurzelregionen
(s. oben, Abschnitt I.4).


Ebenfalls ist der Klägerin 1 zuzustimmen, dass in den Merkmalen e2) und e3) zwei
Stufen beansprucht sind. Denn es erfolgt eine Unterteilung in kleinere einfach
verbundene Regionen und eine weitere Unterteilung eines Teilsatzes in noch
kleinere einfach verbundene Regionen (s. oben, Abschnitt I.4).
Inwieweit die Elemente von Merkmal e2) bereits in Merkmal e3) enthalten sind,
kann dahingestellt bleiben, da diese Frage keinerlei Einfluss auf die Beurteilung der
Patentfähigkeit hat.

                                        - 22 -


Den Ausführungen der Klägerin 1 zu Merkmal e5) kann nicht gefolgt werden. Das
Merkmal gibt eine eindeutige Abbruchbedingung an, wonach keine Unterteilung der
kleineren einfach verbundenen Regionen stattfindet, wenn diese bereits für die
Retransformation geeignet sind (s. oben, Abschnitt I.4).




7.      Das Streitpatent ist im Umfang der Patentansprüche 1 und 11 in seiner
erteilten Fassung für nichtig zu erklären.


7.1   Der    Gegenstand     des    Patentanspruchs   11      ist   vom   Patentschutz
ausgeschlossen. Bei dem beanspruchten Verfahren handelt es sich nämlich um
eine mathematische Methode als solche, Art. 52 Abs. 2 lit. a) EPÜ.


Der Anspruch 11 ist gemäß Merkmal a) auf ein Decodierverfahren gerichtet. Ein
derartiges Verfahren gibt grundsätzlich die Rechenschritte bzw. den Algorithmus
an, mit dem Daten umgewandelt werden. Die Umwandlung / Umrechnung könnte
bspw. mit einem Rechner oder sogar händisch erfolgen.
Auch die weiteren Merkmale des Anspruchs sind lediglich auf einzelne
Rechenvorschriften    gerichtet.   So   werden   beim      Extrahieren   die   für   die
Rechenschritte verwendeten Parameter ausgelesen, bei der Rekonstruktion wird
eine Umrechnung aus einem Spektral- in einen räumlichen Bereich, d.h. eine
Transformation, ausgeführt und bei der Unterteilung wird eine Berechnung der
einzelnen Blockgrößen für die Rekonstruktion vorgenommen.


Nach der Rechtsprechung des BGH sind mathematische Methoden im Hinblick auf
§ 1 Abs. 3 Nr. 1 PatG nur dann patentierbar, wenn sie der Lösung eines konkreten
technischen Problems mit technischen Mitteln dienen. Dabei kann eine
mathematische Methode nur dann als nicht-technisch angesehen werden, wenn sie
im Zusammenhang mit der beanspruchten Lehre keinen Bezug zur gezielten
Anwendung von Naturkräften aufweist. Ein ausreichender Bezug zur gezielten
Anwendung von Naturkräften liegt vor, wenn eine mathematische Methode zu dem
Zweck herangezogen wird, anhand von zur Verfügung stehenden Messwerten
zuverlässigere Erkenntnisse über den Zustand eines Flugzeugs zu gewinnen und

                                       - 23 -


damit die Funktionsweise des Systems, das der Ermittlung dieses Zustands dient,
zu beeinflussen (vgl. BGH, Beschluss vom 30. Juni 2015, X ZB 1/15, GRUR 2015,
983 – Flugzeugzustand).


In dem beanspruchten Decodierverfahren des Anspruchs 11 sind keine
Anweisungen bzw. Merkmale zu erkennen, die der Lösung eines konkreten
technischen Problems mit technischen Mitteln dienen.


Wie bereits ausgeführt, zielen alle Merkmale des Anspruchs darauf ab, einen
Algorithmus vorzugeben, mit dessen Hilfe die Umrechnung von Daten bewerkstelligt
wird.
Das zugrundeliegende Problem liegt in der korrekten Umrechnung von Daten und
ist somit rein mathematischer Natur.


Aus dem Anspruch ist kein ausreichender Bezug zur gezielten Anwendung von
Naturkräften, wie bspw. zur Ermittlung von Messwerten, zu entnehmen.
Insbesondere liegen sämtliche Daten, die für die Umrechnung (Decodierung)
benötigt werden, bereits vor.


7.2       Der Gegenstand des erteilten Anspruchs 1 beruht nicht auf einer
erfinderischen Tätigkeit.


Der auf einen Decodierer, d.h. auf eine Vorrichtung gerichtete Anspruch 1 ist,
abgesehen von der Kategorie, identisch mit Anspruch 11.


Gemäß der Rechtsprechung des BGH kommt der Patentierungsausschluss nicht
auch für Vorrichtungen in Betracht. Für Vorrichtungen kann sich eine vergleichbare
Beurteilung vielmehr daraus ergeben, dass bei der Prüfung einer Erfindung auf
erfinderische Tätigkeit nur diejenigen Anweisungen berücksichtigt werden dürfen,
die die Lösung des technischen Problems mit technischen Mitteln bestimmen oder
zumindest beeinflussen (vgl. BGH, Beschluss vom 27. März 2018, X ZB 11/17,
juris).

                                       - 24 -


Bei der Prüfung, ob ein Ausschlusstatbestand vorliegt, ist darauf abzustellen, ob ein
konkretes technisches Problem mit technischen Mitteln gelöst wird (BGH,
Beschluss vom 22. April 2010, Xa ZB 20/08, in GRUR 2010, 613 - Dynamische
Dokumentengenerierung, BGH, Urteil vom 24. Februar 2011, X ZR 121/09, GRUR
2011, 610 – Webseitenanzeige).


Ein technisches Mittel zur Lösung eines technischen Problems liegt vor, wenn
Gerätekomponenten modifiziert oder grundsätzlich abweichend adressiert werden,
wenn       der     Ablauf      eines      zur      Problemlösung       eingesetzten
Datenverarbeitungsprogramms durch technische Gegebenheiten außerhalb der
Datenverarbeitungsanlage bestimmt wird oder wenn die Lösung gerade darin
besteht, ein Datenverarbeitungsprogramm so auszugestalten, dass es auf die
technischen Gegebenheiten der Datenverarbeitungsanlage Rücksicht nimmt (BGH,
a. a. O.   -     Dynamische     Dokumentengenerierung,        BGH,      a. a. O.   –
Webseitenanzeige).


Anspruch 1 betrifft einen Decodierer (Merkmal a)). Derartige Decodierer waren
jedoch vor dem Prioritätstag im Stand der Technik bspw. als Programm, als Gerät
oder als Umsetzungsschablone hinlänglich bekannt (vgl. z.B. NK6, Fig.3).


Der Decodierer umfasst einen Extrahierer (Merkmale b), b1) bis b3)). Mit dem
Extrahierer werden die Parameter für die folgenden Rechenschritte aus den
vorhandenen Daten ausgelesen. Das Auslesen von Daten ist eine bekannte
Funktion und begründet im vorliegenden Fall kein technisches Problem. Es ist aus
dem Anspruch auch nicht ersichtlich, dass für das Auslesen eine besonders
ausgestaltete Rechenvorrichtung oder eine Modifizierung von Gerätekomponenten
notwendig wäre.


Weiterhin ist ein Unterteiler (Merkmale c) und c1)) sowie ein weiterer Unterteiler
(Merkmalskomplex e)) vorgesehen. Der Unterteiler ist für die Abarbeitung der
durch einen Algorithmus vorgegebenen Unterteilungsschritte zuständig. Eine
besondere Rechenvorrichtung oder modifizierte Gerätekomponenten werden
jedoch nicht beansprucht.

                                       - 25 -




Schließlich ist ein Rekonstruierer beansprucht (Merkmale d), d1 bis d3)). Der
Rekonstruierer    ermöglicht   die   Rekonstruktion,   die   Vorhersage   und   die
Transformation von Daten und somit die Umrechnung vorhandener Daten auf der
Basis der vorgegebenen Rechenregeln. In diesen Merkmalen ist lediglich die bloße
Abarbeitung von Rechenschritten, aber keine Lösung eines technischen Problems
mit technischen Mitteln zu erkennen.
Es ist auch nicht festzustellen, dass die vom Decodierer, Unterteiler und
Rekonstruierer ausgeführten Verfahrensschritte auf technische Gegebenheiten
innerhalb oder außerhalb des Decodierers Rücksicht nehmen, die den Ablauf des
beanspruchten Verfahrens bestimmen.


Auch anderweitig ist nicht erkennbar, dass der anspruchsgemäße Einsatz des
Decodierers die Lösung eines konkreten technischen Problems mit technischen
Mitteln begründet.


Somit sind die Merkmale b) bis e5) von Patentanspruch 1 bei der Prüfung der
erfinderischen Tätigkeit nicht zu berücksichtigen, da sie nicht zur Lösung eines
konkreten technischen Problems mit technischen Mitteln beitragen (BGH, Urteil vom
26. Oktober 2010, X ZR 47/07, GRUR 2011, 125 – Wiedergabe topografischer
Informationen).


7.3   Die dagegen gerichteten Ausführungen der Beklagten greifen nicht durch.


7.3.1 Die Beklagte gibt an, es sei zutreffend, dass die Merkmale eines Anspruchs
dessen Patentfähigkeit unter dem Gesichtspunkt der erfinderischen Tätigkeit nur
insoweit stützen können, wie sie die Lösung eines technischen Problems mit
technischen Mitteln bestimmen oder zumindest beeinflussen.
Bei mathematischen Verfahren sei dies aber nur dann nicht der Fall, wenn die
Merkmale im Zusammenhang mit der beanspruchten Lehre keinen Bezug zur
gezielten Anwendung von Naturkräften aufweisen (BGH, a. a. O. – Flugzeugstand).
Weiterhin sei es gerade nicht maßgeblich, ob bereits der Anspruchswortlaut den
technischen Bezug aufweist (BGH, Urteil vom 25. August 2015, X ZR 110/13,

                                        - 26 -


GRUR 2015, 1184 – Entsperrbild). Gemäß dieser Entscheidung sei es gerade nicht
zu rechtfertigen, die technischen Wirkungen dieser Informationswiedergabe nur
deshalb nicht bei der Prüfung der erfinderischen Tätigkeit heranzuziehen, weil es
dem Patentanspruch an einem eindeutigen technischen Bezug fehle. Das
Erfordernis „Zusammenhang mit der beanspruchten Lehre“ sei also nicht auf eine
konkrete technische Zielsetzung im Anspruchswortlaut beschränkt. Damit solle bei
der Auslegung des Patentanspruchs nach den allgemeinen Auslegungsregeln
(insbesondere im Kontext der Beschreibung) deutlich werden, dass der
Patentanspruch einen Gegenstand definiert, der die Lösung eines technischen
Problems darstellt (auch wenn dies im Patentanspruch nicht schon anderweitig als
solches angegeben ist).


Dieser Darstellung kann nicht gefolgt werden.
Der Schutzbereich des Patents wird durch die Patentansprüche bestimmt. Die
Beschreibung    und   die    Zeichnungen         sind    jedoch   zur   Auslegung   der
Patentansprüche heranzuziehen (§ 14 PatG).
Dies hat der BGH in dem der Entscheidung „Entsperrbild“ zugrundeliegenden Fall
näher ausgeführt: „Das Kriterium, dass solche Anweisungen insoweit zu beachten
sind, als sie die Lösung eines technischen Problems jedenfalls beeinflussen,
erfordert indessen, dass informationsbezogene Merkmale eines Patentanspruchs
daraufhin zu untersuchen sind, ob die wiederzugebende Information sich zugleich
als Ausführungsform eines im Patentanspruch nicht schon anderweitig als solches
angegebenen technischen Lösungsmittels darstellt. In einem solchen Fall ist das
technische Lösungsmittel bei der Prüfung auf Patentfähigkeit zu berücksichtigen.
Denn   es   wäre   nicht    zu   rechtfertigen,    die   technischen    Wirkungen   der
Informationswiedergabe nur deshalb nicht in die Prüfung auf erfinderische Tätigkeit
einzubeziehen, weil sie im Patentanspruch nur in Gestalt der Wiedergabe einer
bestimmten Information beansprucht werden“.


In der genannten Entscheidung waren im Patentanspruch jedoch sowohl eine
Entsperrung als auch eine Anzeige als unmittelbare Konsequenz eines
Steuerbefehls angegeben: „Der in der Fingerbewegung liegende Steuerbefehl soll

                                      - 27 -


mit anderen Worten nicht nur die Entsperrung, sondern auch eine den Befehl und
den Fortgang seiner Ausführung symbolisierende Anzeige auslösen“.




Nachdem die der optischen Kenntlichmachung des Entsperrvorgangs dienende
Verbindung zwischen dem Steuerbefehl und der angezeigten Information bereits im
Patentanspruch enthalten war und einen technischen Bezug herstellte, lässt sich
die Argumentation der Beklagten, wonach aufgrund der genannten Entscheidung
die Beschreibung des Streitpatents den technischen Bezug für die Merkmale des
hier in Rede stehenden Anspruchs gewährleisten sollte, nicht nachvollziehen.


7.3.2 Weiter führt die Beklagte aus, dass das Decodieren von Daten einem
technischen Zweck diene. Gemeinsam mit dem Codieren diene das Decodieren der
Übermittlung von „Daten“ auf möglichst effiziente und bandbreitenschonende
Weise. Ob es sich bei diesen (effizienter übertragenen) Daten um Videodaten,
Audiodaten, Textdaten oder ähnliches handle, sei für das Erreichen des
technischen Zweckes – der Effizienzsteigerung – unerheblich.


Diese Ausführung greift zu kurz. Die bei der Codierung bzw. Decodierung
verwendeten mathematischen Methoden dienen meistens dem Zweck, ein
Verfahren zu verbessern, dessen Durchsatz zu erhöhen oder die Bandbreite zu
verringern. Da sich immer Methoden angeben lassen, die weniger leistungsfähig als
ein beanspruchtes Verfahren sind, kann ein allgemeiner Verweis auf eine solche
Methode nicht zur Begründung eines technischen Bezugs genügen. Im
vorliegenden Fall wird demnach durch die Wahl eines anderen Algorithmus kein
technischer Bezug hergestellt.
Das beanspruchte Verfahren geht daher nicht über eine reine mathematische
Methode hinaus.


7.3.3 Die Beklagte stellt weiter dar, dass der beanspruchte Datenstrom kein
abstraktes Konzept sei, sondern eine physische Anordnung von Daten und damit
technischen Charakter habe. Das Extrahieren von Werten, im Anspruch

                                       - 28 -


Regionsgrößen und Mehrbaum-Unterteilungsinformationen genannt, stelle somit
bereits für sich genommen einen technischen Vorgang dar.


Zuzustimmen ist dem allenfalls insoweit, als der Datenstrom eine zeitliche Abfolge
von Daten (z.B. von Zahlen) ist. Jede mathematische Berechnung benötigt eine
Abfolge von Zahlen, die entweder elektronisch oder auf einem Blatt Papier vorliegen
können. Ein technischer Bezug, insbesondere ein Bezug zur gezielten Anwendung
von Naturkräften, wird durch den Begriff „Datenstrom“ nicht hergestellt.


7.3.4 Gemäß     den    Ausführungen    der      Beklagten   stelle   das   Array   von
Informationsabtastwerten ein räumlich abgetastetes Informationssignal dar, wobei
aus Wikipedia hervorgehe, dass diese Abtastung eine Registrierung von
Messwerten sei. Entsprechendes sei auch für die hier genannte „räumliche
Abtastung“ gültig, mit der aus einem räumlich kontinuierlichen Signal ein räumlich
diskretes Signal gewonnen wird.


Auch diese Ausführung greift zu kurz, da unter den Begriff „Abtastung für räumlich
kontinuierlich vorliegende Werte“ (d.h. bspw. für eine Linie oder für Werte einer
Funktion) eine rein mathematische Auswahl von Stützstellen mit anschließender
Interpolation ebenso fällt, wie eine Diskretisierung bei der numerischen Lösung von
Differentialgleichungen. Aus dem im Anspruch angegebenen räumlich abgetasteten
Informationssignal kann demnach nicht auf eine Abtastung von Messwerten
geschlossen werden. Das Signal repräsentiert eine Menge von Werten, die nicht
geeignet ist, einen hinreichenden Bezug zur gezielten Anwendung von Naturkräften
herzustellen.


7.3.5 In Bezug auf das Rekonstruieren gibt die Beklagte an, dass der Fachmann
im Kontext des beanspruchten Decodierverfahrens das Array von Abtastwerten aus
einem codierten Format wieder in das ursprüngliche Ausgangsformat, nämlich in
ein Array von Abtastwerten, gebracht wird. Bereits in dieser Allgemeinheit sei dies
ein technischer Prozess, der den zur Codierung verwendeten Prozess rückgängig
macht.

                                         - 29 -


Weiter sei die Vorhersage, z.B. die Inter-Prädiktion (räumlich-zeitlich) oder die Intra-Prädiktion (räumlich) bekannt, wobei sich die Differenz zwischen den Originalwerten
und den Vorhersagewerten mit einer geringeren Datenmenge codieren ließe als die
Originalwerte. Das Vorhersagen des Arrays von Informationsabtastwerten sei daher
klar ein technischer Vorgang, der einem technischen Zweck dient.
Ebenso sei die Retransformation aus einem Spektral- in einen räumlichen Bereich
ein technischer Vorgang, der einem technischen Zweck dient.


Diese   Darstellungen    überzeugen     nicht,    da   die   vorliegend   beanspruchte
Rekonstruktion das Umrechnen von Daten von einer Repräsentation in eine andere
und somit eine mathematische Methode betrifft. Das Ziel, eine effizientere
mathematische Methode zu verwenden, geht jedoch nicht über den Einsatz eines
rein mathematischen Algorithmus hinaus. Dementsprechend fehlt es auch hier am
Bezug zur gezielten Anwendung von Naturkräften.


7.3.6 Schließlich führt die Beklagte aus, dass eine verbesserte Anpassung der
Regionen für die Vorhersage und die Retransformation an das Array von
Abtastwerten erfolge. Damit werde das Ziel erreicht, einen besseren Kompromiss
zwischen    der   Codierkomplexität    einerseits und        einem erzielbaren    Rate-Verzerrungs-Verhältnis andererseits zu erzielen – und/oder aber (jedenfalls) ein
besseres Rate-Verzerrungs-Verhältnis. Damit würden diese Merkmale maßgeblich
zum technischen Charakter der beanspruchten Erfindung beitragen.


Auch diese Ausführung geht fehl. Die Anpassung der Regionen erfolgt gemäß dem
Anspruchswortlaut mit Hilfe eines mathematischen Algorithmus, der keine
Anpassung an die Größe der Abstastwerte beinhaltet. Somit werden die Regionen
auf Basis von vorgegebenen Regeln berechnet. Diese Eigenschaft kann einen
technischen Charakter jedoch nicht begründen.

                                        - 30 -


                                          II.


Die Fassung der Ansprüche 1 und 11 des Streitpatents nach Hilfsantrag I vom
27. September 2022 verteidigt die Beklagte erfolgreich. Der Hilfsantrag I ist zulässig
und ist nicht mehr vom Patentschutz ausgeschlossen. Die Erfindung ist in den
Ansprüchen 1 und 11 so deutlich und vollständig offenbart, dass ein Fachmann sie
ausführen kann. Der Gegenstand des Streitpatents in dieser verteidigten Fassung
erweist sich als rechtsbeständig, weil er patentfähig, insbesondere neu ist und auf
erfinderischer Tätigkeit beruht.




1.    Die Ergänzungen in den Ansprüchen 1 und 11 sind zulässig.


Die Änderung der Bezeichnung „Decodierer“ in „Videodecodierer“ in Anspruch 1,
sowie der Bezeichnung „Decodierverfahren“ in „Videodecodierverfahren“ in
Anspruch 11 gehen aus der Stammanmeldung (WO 2011/128269 A1, bspw. Titel,
S.1 Z.6-9) hervor.




2.    Ein Patentierungsausschluss liegt nicht vor.


2.1   Die in der erteilten Fassung von einem Technikbezug losgelöste
beanspruchte mathematische Formel weist durch die Angaben, wonach nunmehr
ein Videodecodierer bzw. ein Videodecodierverfahren beansprucht wird, einen
gezielten Bezug zur Anwendung von Naturkräften auf. Denn nunmehr wird eindeutig
ein Bezug der Daten zu einer Aufnahme von bewegten Bildern angegeben.


Die mathematischen Verfahrensschritte des Anspruchs 11 sind bei der Beurteilung
der Patentfähigkeit zu berücksichtigen, denn nicht berücksichtigungsfähig sind nur
Anweisungen, die ausschließlich Aspekte betreffen, die nach Art. 52 Abs. 2 lit. a)
bis lit. d) EPÜ von der Patentierung ausgenommen sind. Hingegen sind bei der
Prüfung, ob der Gegenstand einer Anmeldung auf erfinderischer Tätigkeit beruht,
diejenigen Anweisungen zu berücksichtigen, die die Lösung des technischen

                                       - 31 -


Problems mit technischen Mitteln bestimmen oder zumindest beeinflussen (vgl.
BGH, Urteil vom 18. Dezember 2012, X ZR 3/12, GRUR 2013, 275 Rn. 41 –
Routenplanung; EPA, Stellungnahme der Großen Beschwerdekammer vom 12. Mai
2010, G 3/08, ABl. 2011, 10 = GRUR Int. 2010, 608 Rn. 10.3 ff. –
Computerprogramme). Eine Beeinflussung der Lösung des technischen Problems,
mit   technischen   Mitteln einen   Videodatenstrom,    der   aus einer    Abfolge
aufgenommener Bilder besteht, zu decodieren, liegt hier aber offensichtlich vor.


Gleiches gilt für die Merkmale des Anspruchs 1.


2.2    Die Klägerin 2 führt aus, dass der Gegenstand des Anspruchs 11 vom
Patentschutz ausgeschlossen sei und die entsprechenden Merkmale des
Anspruchs 1 bei der Prüfung auf erfinderische Tätigkeit nicht berücksichtigt werden
dürften.


So fehle es dem anspruchsgemäßen mathematischen Algorithmus weiterhin an
dem Bezug auf ein physikalisches Objekt. Der Anspruch definiere nämlich keine
Beziehung zwischen dem zusätzlichen Merkmal „Video-“ und den weiterhin
bestehenden mathematischen Fachbegriffen bzw. den Schritten zur Verarbeitung
des mathematischen Objekts. Eine funktionale Beschränkung des Anspruchs auf
einen technischen Zweck sei den Änderungen gemäß Hilfsantrag I nicht zu
entnehmen. Zur Stützung Ihres Vorbringens verweist die Klägerin 2 auf eine
Entscheidung der großen Beschwerdekammer des EPA (T1227/05). Die Aufnahme
des Präfixes „Video-“ in den jeweiligen Oberbegriff der Patentansprüche 1 und 11
stelle die reine Möglichkeit dar, dass der beanspruchte Algorithmus zur Lösung
eines technischen Problems eingesetzt werden könnte. Eine funktionale
Beschränkung auf den technischen Zweck erfolge dadurch gerade nicht.


Diese Ausführung geht fehl. Denn durch die Aufnahme des Präfixes „Video“ wird
der technische Bezug der Merkmale der Ansprüche 1 und 11 dadurch erreicht, dass
sich diese nunmehr auf die Aufnahme und Verarbeitung von Videobildern beziehen.
Dies entspricht auch der Rechtsprechung des BGH. Der Bezug zur gezielten
Anwendung von Naturkräften ist durch die technische Angabe, wonach es sich um

                                       - 32 -


die Decodierung von Videobildern handelt, gegeben (vgl. BGH, a. a. O. –
Flugzeugzustand).




3.    Die Erfindung ist in den Ansprüchen 1 und 11 nach Hilfsantrag 1 so deutlich
und vollständig offenbart, dass ein Fachmann sie ausführen kann.


3.1   Die Klägerin 2 gibt an, dass die Patentansprüche 1 und 11 nicht patentfähig
seien, da ihr Gegenstand nicht so deutlich und vollständig offenbart sei, dass ein
Fachmann sie ausführen kann. Dies betreffe die Merkmale d2) und e4.2.2).


Sie führt aus, dass das Untermerkmal des Merkmals d2) „die von der Unterteilung
in kleinere einfach verbundene Regionen abhängt“ völlig offenlasse, was die
„Abhängigkeit“ bedeuten soll und welchen Einfluss somit die Unterteilung in kleinere
einfach   verbundene     Regionen     auf     die   Granularität   hat.   Auch   die
Patentbeschreibung versetze den Fachmann nicht in die Lage, zu entscheiden, mit
welcher Granularität eine Vorhersage des Arrays von Informationsabtastwerten
durchzuführen ist bzw. wie die Granularität bestimmt wird.
Damit sei aber das Merkmal d2) und somit der Gegenstand der Ansprüche 1 und
11 für den Fachmann nicht ausführbar.
Darüber hinaus sei Merkmal e4.2.2) des Anspruchs 1 nicht ausführbar offenbart:
die Prüfung und Partitionierung für die Teil-Teilregionen rekursiv zu wiederholen,
bis gemäß den untergeordneten Mehrbaum-Unterteilungsinformationen keine
weitere Partition mehr durchgeführt werden soll oder eine weitere maximale
Hierarchieebene erreicht ist.
Das   Untermerkmal      „weitere   maximale     Hierarchieebene“    werde   in   der
Patentbeschreibung überhaupt nicht aufgegriffen. Es sei somit dem Fachmann nicht
möglich, die „weitere maximale Hierarchieebene“ zu bestimmen.


3.2   Diese Ausführung greift zu kurz.
Denn das Merkmal d2) darf nicht „isoliert“ herausgegriffen werden; vielmehr ist der
Merkmalskomplex d), d1) und d2) gemeinsam zu betrachten (s. oben,
Auslegung). Hierzu ist im Streitpatent (Absätze [0036]-[0042]) die Unterteilung der

                                         - 33 -


Blöcke angegeben, wobei so weit unterteilt wird, bis ein optimaler Kompromiss
zwischen   einer   zu   feinen   Prädiktionsunterteilung   und   einer   zu   groben
Prädiktionsunterteilung gefunden ist (vgl. Streitpatentschrift, Absatz [0038]). D.h.
der Fachmann wird aufgrund seiner Kenntnisse und Erfahrungen diesen
Kompromiss erkennen und die Unterteilung bis zu der notwendigen Tiefe (von der
die Granularität abhängt) durchführen.


Gemäß dem Merkmal e4.2.2) werden zwei Abbruchbedingungen für die
Wiederholung der Teilung spezifiziert. Die Klägerin stellt auf die zweite Bedingung
ab, wonach die Unterteilung fortgeführt wird, bis gemäß den untergeordneten
Mehrbaum-Unterteilungsinformationen eine weitere maximale Hierarchieebene
erreicht ist. Aus dem Streitpatent (Absatz [0181]) ist zu entnehmen, dass eine
Information über diese Bedingung zusätzlich im Datenstrom codiert sein muss.
Nach dem Extrahieren dieser Information kann die zweite Bedingung überprüft
werden. Der Fachmann wird ohne erfinderisches Zutun diese Bedingung nutzen,
um die Unterteilung fortzuführen oder zu beenden.


Damit ist der Fachmann aufgrund dieser Angaben zu den Merkmalen d2) und
e4.2.2) im Streitpatent in der Lage, die Erfindung auszuführen. Denn eine „für die
Ausführbarkeit hinreichende Offenbarung ist gegeben, wenn der Fachmann ohne
erfinderisches Zutun und ohne unzumutbare Schwierigkeiten in der Lage ist, die
Lehre des Patentanspruchs aufgrund der Gesamtoffenbarung der Patentschrift in
Verbindung mit dem allgemeinen Fachwissen am Anmelde- oder Prioritätstag
praktisch so zu verwirklichen, dass der angestrebte Erfolg erreicht wird“ (vgl. BGH,
Urteil vom 3. Februar 2015, X ZR 76/13, GRUR 2015, 472 – Stabilisierung der
Wasserqualität; BGH, Urteil vom 13. Juli 2010, Xa ZR 126/07, GRUR 2010, 916,
918 – Klammernahtgerät; BGH, Urteil vom 11. Mai 2010, X ZR 51/06, GRUR 2010,
901 – Polymerisierbare Zementmischung).




4.    Der dem Streitpatent in der Fassung des Hilfsantrags I zu entnehmende
Gegenstand des Patentanspruchs 1 ist neu und beruht auch auf erfinderischer

                                           - 34 -


Tätigkeit (Art. 54 und Art. 56 EPÜ). Entsprechendes gilt für den nebengeordneten
Patentanspruch 11.


4.1     Stand der Technik
Aufgrund der unterschiedlichen Nummerierung der von den Klägerinnen im
Verfahren genannten Druckschriften geht der Senat für deren Beurteilung von
folgender Nummerierung aus:
        NK 1:        EP 3 461 130 A1
        NK 2:        EP 3 261 344 A1
        NK 3:        CHENG-TIE CHEN, ADAPTIVE TRANSFORM CODING VIA
                     QUADTREE-BASED VARIABLE BLOCKSIZE DCT
        NK 4:        JACQUES         VAISEY,        IMAGE   COMPRESSION       WITH
                     VARIABLE BLOCK SIZE SEGMENTATION
        NK 5:        Samsung`s Response to the Call for Proposals on Video
                     Compression Technology, JCTVC-A124
        NK 6:        US 2010/0086031 A1
        NK 7:        ITU-T H.264
        NK 8:        US 5 999 655 A
        NK 9:        US 5 241 395 A
        NK 10:       US 5 021 891


4.2     Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag I ist neu.


4.2.1 NK 1 und NK 2
Beide Druckschriften bilden keinen Stand der Technik (Art. 52 EPÜ).
Die beiden Druckschriften wurden erst nach dem Prioritätstag des Streitpatents
angemeldet (NK 1 am 17.08.2010; NK 2 am 22.10.2010). Jedoch beanspruchen
beide    Druckschriften     eine   Priorität.   Das   Anmeldedatum   dieser   beiden
Prioritätsschriften liegt vor dem Prioritätstag des Streitpatents (17.08.2009,
23.10.2009). Somit sind beide Druckschriften nur bei der Prüfung auf Neuheit zu
berücksichtigen, wobei dies nur dann statthaft ist, wenn beide Druckschriften die
jeweilige Priorität auch wirksam in Anspruch nehmen.

                                       - 35 -


Dementsprechend kann dahingestellt bleiben, ob beide Druckschriften sämtliche
Merkmale des Anspruchs 1 vorwegnehmen, da sämtliche Merkmale bereits aus den
zugehörigen Prioritätsdokumenten hervorgehen müssen. Deshalb werden im
Folgenden die beiden Prioritätsdokumente (ES 1b und ES 2b bzw. NK 2b-ÜS)
betrachtet.


4.2.1.1       ES 1b (Prioritätsdokument von NK 1)
Eine   weitere „untergeordnete Mehrbaum-Unterteilungsinformation“ und die
entsprechende weitere Unterteilung durch den „weiteren“ Unterteiler (Merkmale b2)
und e) bis e4.2.2) sind aus der Druckschrift nicht zu entnehmen.
Auch das Merkmal b3) ist nicht aus der Druckschrift zu entnehmen.


Die Klägerin 2 stellt dar, dass insbesondere die Merkmale b2), e) und e1) aus der
Druckschrift zu entnehmen seien und dementsprechend die NK 1 vollen Stand der
Technik bilde. Diese Merkmale gingen aus den Fig. 10A – 11 sowie aus der
Beschreibung, S.21, Z.9-17 und S.21, Z.22-29 hervor.


Dieser Darstellung ist nicht zu folgen, denn in der ES 1b ist lediglich eine
Unterteilung gemäß den Merkmalen b), b1), c) c1), d), d1) und d2) beschrieben.
D.h. es wird eine rekursive eine Unterteilung eines „ersten“ Baums in
Codiereinheiten     auf    der   Grundlage      einer   Regionsgröße   und     einer
Unterteilungsinformation durchgeführt (vgl. Fig. 9, 10A). Die so gewonnenen Blöcke
können dann mittels Intra- bzw. Inter-Bildvorhersage verarbeitet werden (vgl.
Fig.11). Eine weitere rekursive Unterteilung von Baumwurzel-Teilregionen in Teil-Teilregionen durch einen „weiteren“ Unterteiler gemäß den Merkmalen b2) und e)
bis e4.2.2) ist nicht gezeigt.


Ob das Merkmal b3) in der NK 1 (Absatz [0143]) gezeigt ist, kann dahingestellt
bleiben. Denn dieser Teil der Beschreibung ist in der ES 1b nicht enthalten.


4.2.1.2       ES 2b (Prioritätsdokument von NK 2 / NK 2b-ÜS)
Auch aus der ES 2b ist eine weitere „untergeordnete Mehrbaum-Unterteilungsinformation und die entsprechende weitere rekursive Unterteilung von Baumwurzel-

                                       - 36 -


Teilregionen in Teil-Teilregionen durch einen „weiteren“ Unterteiler (Merkmale b2)
und e) bis e4.2.2)) nicht zu entnehmen.


Ebenfalls ist das Merkmal b3) nicht aus dieser Druckschrift zu entnehmen.


In Bezug auf die ES 2b führt die Klägerin 2 aus, dass insbesondere die Merkmale
b2), e) und e1) zu entnehmen seien. Somit sei auch die NK 2 als voller Stand der
Technik zu betrachten.


Diese Ausführungen greifen auch in diesem Fall zu kurz. Die in der Druckschrift
gezeigte Unterteilung zeigt lediglich die Merkmale b), b1), c) c1), d), d1) und d2).
Denn auch in der ES 2b bzw. NK 2b-ÜS wird (analog zu ES 1b) eine rekursive
Unterteilung in Codiereinheiten auf der Grundlage einer Regionsgröße und einer
Unterteilungsinformation durchgeführt (vgl. Fig. 9, 10A). Die so gewonnenen Blöcke
können dann mittels Intra- bzw. Inter-Bildvorhersage rekonstruiert werden (vgl.
Fig.11).
Eine weitere „untergeordnete Mehrbaum-Unterteilungsinformation“ und eine
entsprechende weitere Unterteilung durch einen „weiteren“ Unterteiler (Merkmale
b2) und e) bis e4.2.2)) sind nicht gezeigt.


Schließlich ist aus der ES 2b bzw. NK 2b-ÜS auch das Merkmal b3) nicht zu
entnehmen. Denn die entsprechende, von der Klägerin 2 angegebene Stelle der
Beschreibung der NK 2 (Absatz [0144]) ist weder in der ES 2b noch in der NK 2b-ÜS zu finden.


4.2.2 Die NK 3 kann den Gegenstand von Anspruch 1 nicht vorwegnehmen.


4.2.2.1      Das Dokument beschreibt die Codierung eines Bildes mittels der
sogenannten Quadtree-Unterteilung mit variabler Blockgröße für die diskrete
Kosinustransformation („DCT“) (vgl. Titel und Abstract).


Obwohl das Dokument ausschließlich die Codierung beschreibt, liest der Fachmann
das umgekehrte Vorgehen, d.h. die Decodierung mit.

                                         - 37 -




Damit ist in der Druckschrift NK 3 ein Codierer/Decodierer (Abstract, Summary) für
die Codierung/Decodierung eines Bildes beschrieben (Merkmal a)).


Weiter ist angegeben, dass die Unterteilung der ersten (der obersten) Quadtree-Ebene fest vorgegeben ist und die Unterteilung der weiteren Ebenen mittels einer
„0“ bzw. einer „1“ angezeigt wird (S.1855, Sp.1 Abs. 1 und Abs. 3; Fig.2).
Der Teil, der das Extrahieren einer Unterteilungsinformation beschreibt, ist somit
gezeigt (Merkmal b1) teilweise).


Ein   rekursives    Unterteilen    der     Regionen    auf    Basis     der   ersten
Unterteilungsinformation geht aus der Druckschrift hervor (S.1855, Sp.1 Abs. 3 –
Merkmale c) und c1)).
Ebenfalls ist die Verwendung der Unterteilung für eine Codierung/Decodierung
mittels DCT gezeigt (S.1855, Sp.1 Abs. 4 bis Sp.2 Abs. 2 – Merkmale d) und d1)).


Aus der Druckschrift ist jedoch nicht das Extrahieren einer maximalen
Regionsgröße (restlicher Teil von Merkmal b1)) und auch kein Extrahieren einer
untergeordneten     Mehrbaum-Unterteilungsinformation        (Merkmal      b2))   zu
entnehmen.


Ebenso ist das Merkmal b3) nicht gezeigt, da keine weitere Information (etwa die
weitere maximale Regionsgröße) übertragen und extrahiert wird.
Aus der Druckschrift ist auch keine Vorhersage (Prädiktion) gemäß Merkmal d2) zu
entnehmen.


Da weder eine untergeordnete Mehrbaum-Unterteilungsinformation noch eine
weitere maximale Regionsgröße gemäß den Merkmalen b2) und b3) aus der
Druckschrift zu entnehmen sind, ist somit das auf diesen Merkmalen beruhende
Merkmal d3) und die Merkmalsgruppe e) ebenfalls nicht zu entnehmen.


4.2.2.2      Die Klägerin 2 stellt dar, dass auch die fehlenden Merkmale in der
Druckschrift gezeigt seien bzw. durch die Druckschrift nahegelegt seien.

                                           - 38 -


Sie verweist dabei im Wesentlichen auf S. 1854, Sp. 1 Abs. 2, S. 1855, Sp. 1 Abs. 1
und Abs. 3, und auf S. 1855, Sp.1 Abs. 4 – Sp. 2 Abs. 2.


4.2.2.3       Dieser Darstellung kann der Senat nur teilweise zustimmen.
So ergibt sich aus der NK 3 (S. 1855, Sp. 1 Abs. 1), dass eine
Unterteilungsinformation für eine rekursive Unterteilung der Regionen/Blöcke
vorliegt und eine entsprechende erste Unterteilung vorgenommen wird (erster Teil
von Merkmal b1)).
Der zweite Teil von Merkmal b1) ist jedoch nicht gezeigt. Denn die maximale
Regionsgröße ist in der NK 3 fest vorgegeben und somit findet keine Übertragung
und Extraktion dieser Information statt.


Aus S. 1855, Sp. 1 Abs. 4 – Sp. 2 Abs. 2 ist die Tiefe der Unterteilung dahingehend
spezifiziert, dass für kontrastreiche Bereiche die Granularität größer sein soll als für
Bereiche mit weniger Kontrast. Damit ist die Unterteilung mit einer bestimmten
Granularität zu entnehmen; die Durchführung einer Vorhersage (Prädiktion) geht
aber aus der Druckschrift nicht hervor. Merkmal d2) ist somit ebenfalls nur teilweise
gezeigt.


Die von der Klägerin angeführten Stellen der NK 3 zeigen auch nicht die Merkmale
b2) und b3). Denn nach Überzeugung des Senats ist nur eine erste
Unterteilungsinformation für die Aufteilung der Regionen gezeigt. Eine weitere
Information (untergeordnete Mehrbaum-Unterteilungsinformation) ist nicht zu
entnehmen. Da das Merkmal d3) und auch die Merkmalsgruppe e) auf dieser
Information aufbaut, sind all diese Merkmale in der NK 3 nicht realisiert.




4.2.3 Die NK 4 kann den Gegenstand des Anspruchs 1 nicht vorwegnehmen.


4.2.3.1       Gegenstand der Druckschrift ist die Bildkompression mit variabler
Segmentierung der Blockgröße. Dabei wird ein Codierschema in Abhängigkeit des
lokalen Charakters und der Wichtigkeit des zu codierenden Blocks bestimmt (vgl.
Titel und S. 2040, Sp. 1 Abs. 1 – Sp. 2 Abs. 1).

                                         - 39 -




Aus der Druckschrift ist ein Empfänger (Decodierer) zu entnehmen, der die Bilder
rekonstruiert (S. 2042, li. Sp. Mitte – „receiver“ – Merkmal a)).


Die rekursive Unterteilung (S. 2042, li. Sp. letzter Abs. – re. Sp. Abs. 1 und 2) ist
zwar beschrieben, jedoch in Verbindung mit einem Test und nicht mittels einer
Unterteilungsinformation (Merkmal c1) teilweise).


In Bezug auf den Rekonstruierer wird die Wiederherstellung der Bilder erläutert
(S.2042, li.Sp.). In Verbindung mit der Codierung in Blöcken unterschiedlicher
Größe ist somit das Merkmal d1) gezeigt.


Eine Spektraltransformation ist aus der Druckschrift zu entnehmen (S. 2050, li. Sp.
letzter Abs. – „TC“ = „transform coding“ – erster Teil von Merkmal d3)).


In der Druckschrift sind jedoch die Merkmale b1), b2), b3), d2), sowie der zweite
Teil von Merkmal d3), und die Merkmalsgruppe e) nicht gezeigt.


4.2.3.2 Die Klägerin 2 gibt an, dass die Merkmale b1), b2) und b3) aus der
Druckschrift (insbes. S. 2042, Sp. 1, Abs. 2, S. 2042, Sp. 1, letzter Abs. und Sp. 2,
Abs. 1 und 2) zu entnehmen seien.


4.2.3.3       Dieser Darstellung kann nicht zugestimmt werden.
Aus der NK 4 ist zu entnehmen, dass die Blockgröße zwischen 32x32 und 4x4 liegt
(S. 2040, re. Sp. und S. 2042, Sp. 1, Abs. 2). Damit ist die größte Blockgröße fest
vorgegeben und ein Extrahieren der maximalen Regionsgröße ist weder notwendig
noch offenbart. Merkmal b1) ist sonach nicht gezeigt.


Für die weitere Unterteilung wird jeweils ein Test durchgeführt und auf Basis des
Ergebnisses wird entschieden, ob der betreffende Block weiter (rekursiv) unterteilt
wird oder nicht (S. 2042, li. Sp. letzter Abs. – re. Sp. Abs. 1 und 2). Eine Information
innerhalb des Datenstroms, aus der letztendlich die weitere Unterteilung hervorgeht

                                       - 40 -


bzw. extrahiert werden kann, ist nicht gezeigt. Die Merkmale b2) und b3) sind somit
aus der Druckschrift nicht zu entnehmen.


4.2.3.4       Weiter stellt die Klägerin 2 dar, dass aus der Druckschrift (S. 2044,
Abs. 3) die Merkmale d2) und d3) zu entnehmen seien.


4.2.3.5       Der Darstellung der Klägerin 2 ist nur teilweise zuzustimmen.
Wie bereits angegeben, ist die Unterteilung in kleinere einfach verbundene
Regionen gezeigt (vgl. oben, 4.2.3.1). Nicht gezeigt ist hingegen die Vorhersage
von Arrays von Informationsabtastwerten mit einer Granularität durchzuführen, die
von der Unterteilung in kleinere einfach verbundene Regionen abhängt. Merkmal
d2) ist demnach nicht zu entnehmen.
Der erste Teil von Merkmal d3), d.h. die Spektraltransformation, geht aus der
Druckschrift hervor (vgl. oben, 4.2.3.1). Die Durchführung dieser Transformation in
Einheiten der noch kleineren einfach verbundenen Regionen ist hingegen nicht zu
entnehmen. Der zweite Teil von Merkmal d3) ist somit nicht gezeigt.


4.2.3.6       Ebenso gibt die Klägerin 2 an, dass die Merkmale e) und e1) aus der
Druckschrift (S.2042, Sp.2, Abs. 2) zu entnehmen seien.


4.3.2.7       Diese Ausführungen greifen zu kurz.
Die rekursive Unterteilung der Blöcke in mehreren Schritten, gemäß einer
untergeordneten Mehrbaum-Unterteilungsinformation (gemäß dem „zweiten“
Baum), ist nicht gezeigt. Damit geht Merkmal e1) aus NK 4 nicht hervor.


Nachdem bereits das Merkmal b2) nicht aus der NK 4 zu entnehmen ist, ist auch
das Merkmal d3) und die Merkmalsgruppe e), die auf dem Merkmal b2) basieren,
in der NK 4 nicht realisiert.


4.2.4 Die NK 5 kann den Gegenstand des Anspruchs 1 nicht vorwegnehmen.


Die Druckschrift zeigt einen Decodierer (S.5, Kap.2.1 „codec“). Der Begriff „codec“
bezeichnet eine Einheit aus einem Kodierer und einem Decodierer – Merkmal a).

                                       - 41 -




Weiter ist zu entnehmen, dass eine maximale Regionsgröße (LCU) in dem
Datenstrom übertragen wird (S.7, vorletzter Absatz – Merkmal b1)).


Zusätzlich werden weitere Parameter („split-flag“, „PU splitting“, „TU size“)
vorgegeben (S. 10, Abs. 2.2.4; Fig. 2-2). Aus diesen Parametern ist die Tiefe der
Hierarchie und die rekursive Unterteilung gemäß den Merkmalen c) und c1) zu
entnehmen (S. 7, Fig. 2-2 und Beschreibung).


Auch eine Rekonstruktion ist in der Druckschrift angesprochen (Fig. 2-1 mit
Beschreibung). Dazu wird eine Vorhersage auf Basis der untersten Ebene
durchgeführt (S. 8, Kap. 2.2.2). Die Vorhersage verwendet dabei verschiedene
bekannte Methoden, wie bspw. Intra-Prädiktion oder Inter-Prädiktion (S. 8,
Kap. 2.2.2, Fig. 2-4). Damit sind auch die Merkmale d), d1) und d2) aus der
Druckschrift zu entnehmen.


In der Druckschrift sind die Merkmale b2), b3) und e) bis e4.2.2) nicht gezeigt.


4.2.4.1      Die Klägerin 2 stellt dar, dass auch die Merkmale b2), b3) und e) bis
e4.2.2) in der Druckschrift gezeigt seien. Zu Merkmal b2) verweisen die
Klägerinnen auf S. 20, Kap. 2.5.1 und zur Merkmalsgruppe e) insbes. auf S. 5,
Kap. 2.1.


4.2.4.2      Diese Darstellung überzeugt jedoch nicht.
Aus der Beschreibung (Kap. 2.5.1) ist zu entnehmen, dass der H.264/AVC-Standard
nur Transformationsgrößen von 4x4 bzw. 8x8 unterstützt. Im Gegensatz dazu
können in dem Vorschlag gemäß der NK 5 auch größere Transformationsblöcke
verwendet werden.
Weiter wird beschrieben (Kap. 2.1), dass für die Unterteilung drei Blockkonzepte
(CU, PU und TU) verwendet werden und damit die Gesamtstruktur der Unterteilung.
Somit wird die rekursive Unterteilung auf der Grundlage einer Regionsgröße und
einer Unterteilungsinformation durchgeführt (vgl. Fig. 2.6). Die so gewonnenen

                                        - 42 -


Blöcke können dann mittels Intra- bzw. Inter-Bildvorhersage rekonstruiert werden
(vgl. Tab. 2-1).
Eine    weitere „untergeordnete Mehrbaum-Unterteilungsinformation“         und die
entsprechende weitere rekursive Unterteilung durch den „weiteren“ Unterteiler sind
demnach nicht gezeigt. Somit ist Merkmal b2) nicht zu entnehmen. Gezeigt ist nur
ein einziger Unterteilungsschritt (Fig. 2-6) und kein rekursives Unterteilen gemäß
den Merkmalen e2) bis e4.2.2).


4.2.5              Eine Neuheitsschädlichkeit weiterer im Verfahren befindlicher
Entgegenhaltungen wurde von den Klägerinnen nicht geltend gemacht und ist auch
nicht ersichtlich.


4.3     Der Gegenstand von Patentanspruch 1 nach Hilfsantrag I beruht gegenüber
dem genannten Stand der Technik auf einer erfinderischen Tätigkeit.


4.3.1 Der Gegenstand von Anspruch 1 ist durch die NK 5 nicht nahegelegt.


Die Klägerin 2 führt aus, dass der Gegenstand von Anspruch 1 nach Hilfsantrag 1
durch die NK 5 zumindest nahegelegt sei, da ausgehend von der LCU rekursiv in
CU, PU und TU unterteilt werde (S.5, letzter Absatz, Kap. 2.2.4 und Kap. 2.5.1).
Somit sei die weitere rekursive Unterteilung, gemäß den Merkmalen b2) und e) bis
e4.2.2) durch die NK 5 zumindest nahegelegt. Zur Stützung Ihres Vorbringens
verweist Sie zusätzlich auf ein Gutachten (Anlage NK B).


Die Ausführungen der Klägerin 2 greifen zu kurz. In der Druckschrift ist eine
rekursive Unterteilung auf der Grundlage einer Regionsgröße und einer
Unterteilungsinformation gezeigt (vgl. Fig. 2.6). Die so gewonnenen Blöcke können
dann mittels Intra- bzw. Inter-Bildvorhersage rekonstruiert werden (vgl. Tab. 2-1).
Eine weitere „untergeordnete Mehrbaum-Unterteilungsinformation“ und eine
entsprechende weitere rekursive Unterteilung durch den „weiteren“ Unterteiler sind
hingegen nicht gezeigt, und auch kein Prüfen, ob eine jeweilige kleinere einfach
verbundene Region eine weitere maximale Regionsgröße überschreitet, wie es die
Merkmale b2) und e2) bis e4.2.2) zum Ausdruck bringen.

                                            - 43 -




Aus der Druckschrift ist auch keine Anregung erkennbar, dass zusätzlich zur
gezeigten „ersten“ Unterteilung eine „weitere“ Unterteilung eingeführt und der
Prüfschritt des Merkmals e3) implementiert werden soll, da das dort gezeigte
Verfahren in sich bereits abgeschlossen ist (vgl. BGH, Urteil vom 6. November
2018, X ZR 13/17, juris).


Auch den Darstellungen in dem Gutachten war nicht zu folgen. Das Gutachten
beschreibt ebenfalls die in der NK 5 gezeigte „erste“ Unterteilung. Davon
ausgehend soll die Implementierung einer „weiteren“ Unterteilung für den
Fachmann nahegelegen haben. Nachdem sich jedoch weder eine Anregung noch
ein Hinweis aus der Druckschrift in Bezug auf die Einführung eines „weiteren“
Unterteilers entnehmen lässt, ist die Ausgestaltung gemäß den Merkmalen b2) und
e) bis e4.2.2) keinesfalls naheliegend.




4.3.2 Der Gegenstand von Anspruch 1 wird durch die Druckschrift NK 5 in
Verbindung mit der Druckschrift NK 8 nicht nahegelegt.


Die NK 8 betrifft eine Segmentierungskarte, d.h. eine Karte, mit der die Segmente
der Bildblöcke angezeigt werden (vgl. Abstract).
In NK 8 ist ausgeführt, dass ein Eingangssignal einer Transformationsschaltung
zugeführt wird, die Bildblöcke mit variabler Blockgröße einer Bildtransformation
unterzieht,   wodurch   Transformationskoeffizienten           gewonnen    werden.   Die
Transformationskoeffizienten werden quantisiert und durch einen Quantisierer und
Entropiecodierer verlustfrei codiert (vgl. Sp. 2 Z. 41-59). Zusätzlich wird das
Eingangssignal an eine Segmentierungsschaltung weitergegeben, die bestimmt,
welche Blockgröße für die Ratenverzerrung lokal optimal ist (vgl. Sp. 2 Z. 60-62).
Die   Empfangsstation       umfasst    einen         Demultiplexer   zum   Trennen   der
Transformationskoeffizienten          und        der       Segmentierungskarte.      Die
Transformationskoeffizienten werden einem Entropie-Decoder und inversen
Quantisierer zugeführt, der die inversen Operationen des Quantisierers und
Entropie-Codierens durchführt. Die decodierten Transformationskoeffizienten

                                      - 44 -


werden einer inversen Transformationsschaltung zugeführt, die ein Ausgangssignal
Xout erzeugt. Die Segmentierungskarte wird an eine Segmentierungskarten-Decoderschaltung angelegt, die die relevante Blockgröße an die inverse
Transformationsschaltung anlegt (vgl. Sp. 3 Z. 8-18).


Somit ist in der Druckschrift eine Unterteilung gemäß Merkmal b1) gezeigt. Denn
die Segmentierungskarte und das darauf aufbauende Unterteilen der Blöcke
entspricht einer ersten Unterteilung gemäß dem „ersten“ Baum. Ein Codieren bzw.
Extrahieren der untergeordneten Mehrbaum-Unterteilungsinformationen (Merkmal
b2)) ist nicht gezeigt. Entsprechend sind auch die Merkmale e4) bis e4.2.2) nicht
aus der Druckschrift zu entnehmen.


Die Klägerinnen geben an, dass ausgehend von der NK 5 die Implementierung
eines „zweiten“ Baumes für die Entropiecodierung / Entropiedecodierung gemäß
der NK 8 nahegelegen habe.


Eine derartige Abwandlung bedingt nach Auffassung des Senats jedoch mehrere
gedankliche Schritte. Die NK 5 gibt die Lehre, ausgehend von einer Unterteilung im
Sinne eines „ersten“ Baumes den Datenstrom mit den bekannten Verfahren zu
decodieren. Dieses Verfahren ist jedoch in sich abgeschlossen. Das in der NK 8
beschriebene Verfahren basiert ebenfalls auf einem „ersten“ Baum. Der Fachmann
müsste demnach den vorgegebenen (abgeschlossenen) Lösungsweg der NK 5
verlassen und die in der NK 8 gezeigte (ebenfalls abgeschlossene) Lösung in einer
Weise als „zweiten“ Baum in die NK 5 integrieren, die insbesondere den Prüfschritt
des Merkmals e3) umfasst. Da es für diese Schritte im Stand der Technik keine
konkrete Anregung gibt, gilt dies nicht mehr als naheliegend (vgl. BGH, Urteil vom
3. Mai 2006, X ZR 24/03, GRUR 2006, 930 – Mikrotom).


4.3.3 Der Gegenstand von Anspruch 1 wird durch die Druckschrift NK 5 in
Verbindung mit der Druckschrift NK 9 bzw. der NK 10 nicht nahegelegt.


Die NK 9 gibt als Aufgabe an, einen adaptiven Transformationscodieralgorithmus
bereitzustellen, der die Komprimierungsfähigkeit einer großen Blockgröße und die

                                        - 45 -


hohe visuelle Bildqualität einer kleinen Blockgröße nutzt, indem die geeignete
Blockgröße gemäß den Bildinhalten gewählt wird, um einen besseren Kompromiss
zwischen Bitrate und Bildqualität zu erreichen (Sp. 3 Z. 3-9).
Dabei wird ein Bild zunächst in relativ große Blöcke von Pixeln der Größe M x M
unterteilt. Jeder M x M-Block wird weiter (evtl. mehrmals) in gleich große Blöcke der
Größe N x N unterteilt, wobei N X N die Größe der kleinsten Blöcke angibt (Sp. 3
Z. 15-22). Ein M x M-Block kann als Wurzelknoten in einer Quadtree-Datenstruktur
betrachtet werden (Sp. 7 Z. 15-19).
Eine Transformation (DCT) kann auf einen M x M Block aber auch auf einen N x N
Block angewendet werden. Letzteres hängt davon ab, ob die Transformation (je
nach Bildinhalt) bereits auf den M x M-Block angewendet werden kann (Sp. 3 Z. 44-
54).
Die weitere Unterteilung der M x M-Blöcke hängt davon ab, ob das Bild Kanten mit
hohem Kontrast aufweist, oder ob es Bildbereiche aufweist, in denen das
menschliche Sehvermögen nicht empfindlich auf eine Verschlechterung reagiert
(Sp. 8 Z. 51-62).
Zur Rekonstruktion ist angegeben, dass der Empfänger über die Quadtree-Struktur,
die zum Partitionieren des Bildes verwendet wird, informiert wird. Jedem Knoten
wird ein Wert zugewiesen, der die weitere Unterteilung oder das Nicht-Unterteilen
angibt, wobei bei bekannter Anzahl der Ebenen diese Information nicht notwendig
ist (Sp. 9 Z. 15-28, Fig. 2).


Aus der Druckschrift sind demnach die Merkmale b1), c) bis d2) zu entnehmen.
Nicht gezeigt sind die Merkmale b2) und e) bis e4.2.2).


In der NK 10 ist ein adaptives Blockgrößen-DCT-Verfahren zu entnehmen, wobei
eine Unterteilung der 16 x 16-Blöcke in 8 x 8-, 4 x 4- bzw. 2 x 2-Blöcke verwendet
wird. Für jeden 4 x 4-Block wird die Bitanzahl, um den Block unter Verwendung von
vier 2 x 2-Unterblöcken innerhalb des 4 x 4-Blocks zu kodieren, geprüft. Wenn diese
Bitanzahl kleiner ist als die zur Codierung eines 4x4-Blocks erforderliche Bitanzahl,
wird der 4 x 4-Block durch vier 2 x 2-Blöcke ersetzt. Das gleiche gilt für die anderen
Blockgrößen, wodurch die Blockgrößenzuweisung optimiert wird (S. 7 Z. 31-49).
Jede Entscheidung, einen Block in kleinere Blöcke zu unterteilen, erfordert ein

                                       - 46 -


Informationsbit als Überhang (Sp. 7 Z. 62-66). Weiterhin können Blöcke auch in
nicht symmetrische Unterblöcke geteilt werden (Sp. 8 Z. 3-15). Für die Unterteilung
ist ein Register beschrieben, das die effiziente Unterteilung auf den Ebenen anzeigt
(Sp. 13 Z. 8-45).


Sonach ist auch aus der NK 10 keine Unterteilung, die über einen „ersten“ Baum
hinausgeht, zu erkennen.
Auch in dieser Druckschrift sind die Merkmale b2) und e) bis e4.2.2) nicht gezeigt.


Die Klägerinnen führen aus, dass die in der NK 5 gezeigte rekursive Unterteilung
durch die Aufnahme der in der NK 9 bzw. NK 10 gezeigten Unterteilung zu einem
„zweiten“ Baum gemäß den fehlenden Merkmalen führen würde. Ein erfinderisches
Zutun sei hierfür nicht notwendig.


Auch diesen Ausführungen ist nicht zu folgen. Denn auch diese Abwandlung
bedingt nach Auffassung des Senats mehrere gedankliche Schritte. Die NK 5 gibt
die Lehre, ausgehend von einer Unterteilung im Sinne eines „ersten“ Baumes, den
Datenstrom mit den bekannten Verfahren zu decodieren. Das Verfahren ist damit in
sich abgeschlossen. Die in der NK 9 bzw. NK 10 gezeigte Decodierung basiert
ebenfalls auf einer Unterteilung, wobei auch die Lehre dieser Druckschriften in sich
abgeschlossen       ist. Der Fachmann müsste demnach den vorgegebenen
(abgeschlossenen) Lösungsweg der NK 5 verlassen und die in der NK 9 bzw.
NK 10 gezeigte Lösung als „zweiten“ Baum in die NK 5 integrieren und dazu
insbesondere den Prüfschritt e3) einführen. Da es für diese Schritte im Stand der
Technik keine konkrete Anregung gibt, gilt dies nicht mehr als naheliegend (vgl.
BGH, a. a. O. – Mikrotom, BGH, a. a. O. – X ZR 13/17).


4.3.4 Der Gegenstand von Anspruch 1 wird durch die Druckschrift NK 6 weder in
Verbindung mit dem allgemeinen Fachwissen noch mit der Druckschrift NK 7
nahegelegt.


4.3.4.1       Gegenstand der NK 6 ist das Codieren und das Decodieren digitaler
Videodaten unter Verwendung großer Makroblöcke (Abstract, Absatz [0006]).

                                         - 47 -


Konkret ist ein Decodierer zu entnehmen, der große Makroblöcke (größer als
16x16) verarbeiten kann (Absatz [0006] – Merkmal a)).


Der    Decodierer     empfängt   Daten    und     Syntaxinformationen.   Von   einem
Syntaxdecoder werden aus den Syntaxinformationen die Angaben zur größten
Blockgröße, welche vom Codierer in den Datenstrom eingebettet wurden,
ausgelesen. Die codierten Informationen umfassen darüber hinaus Angaben zu den
Makroblocktypdaten (insbesondere eine maximale Blockgröße) sowie zu der Art der
Partitionierung des Makroblocks (Absätze [0024], [0025], [0059], [0205] –
Merkmale b) und b1)).


Weiterhin wird ein Unterteiler für ein rekursives Unterteilen der Blöcke bzw.
Regionen gemäß den Merkmalen c) und c1) beschrieben (Absätze [0024], [0126]
ff., [0175], Fig. 12, Fig. 5).


Ebenso ist die Codierung von Blöcken mittels Prädiktion gezeigt (Absätze [0115],
[0116], [0176]). Nachdem die Codierung der Blöcke beschrieben ist, ist der
umgekehrte Schritt, d.h. die Decodierung der Blöcke mittels Prädiktion mitzulesen.
Somit sind die Merkmale d), d1) und d2) gezeigt.


Die Merkmale b2), d3) und die Merkmalsgruppe e)) sind der NK 6 jedoch nicht
zu entnehmen.


4.3.4.2        Gegenstand des Standards (NK 7) sind die Grundlagen für die
Videocodierung bzw. die Videodecodierung.


Unumstritten ist dieser Standard dem Fachmann hinlänglich bekannt. Er ist somit
als allgemeines Fachwissen anzusehen.


Die in dem Standard gezeigte Unterteilung besteht aus einer einzigen
Hierarchieebene, in der eine Vorhersage (Prädiktion) möglich ist (vgl. Tab. 7-10 und
Tab. 7-11). Damit ist die Unterteilung gemäß einem „ersten“ Baum gezeigt. Eine

                                        - 48 -


rekursive weitere Unterteilung gemäß den Merkmalen d2) und e2) bis e4.2.2) ist
nicht gezeigt.


Die Klägerin 1 gibt an, dass mit Hilfe eines Flags angezeigt werde, ob ein Block
weiter unterteilt wird oder nicht (S. 76, „transform_8x8_mode_flag“; S. 90-91,
„transform_size_8x8_flag“). Dieses Flag sei als Information in dem Datenstrom
codiert und werde nicht ausgelesen. Somit unterscheide sich die NK 7 lediglich in
der festen Vorgabe der Maximalgröße der Transformationsblöcke von Anspruch 1.
Weiter führen die Klägerinnen aus, dass die in der NK 7 gezeigten
„Transformationsgrößen-Flags“        der         untergeordneten       Mehrbaum-Unterteilungsinformation entsprechen. Demnach wäre das Merkmal b2) gezeigt,
und die weitere Unterteilung (Merkmale e2) bis e4.2.2)) zumindest nahegelegt.


Dieser Argumentation kann sich der Senat nicht anschließen, denn die mit den
Transformationsgrößen-Flags     vorgegebene      Unterteilung   entspricht   keiner
rekursiven weiteren Unterteilung gemäß den Merkmalen e2) bis e4.2.2), sondern
der Unterteilung des „ersten“ Baums, mit der eine Vorhersage (Prädiktion) möglich
ist (vgl. Tab. 7-10 und Tab. 7-11). Damit ist auch ein Extrahieren von
untergeordneten Unterteilungsinformationen und einer weiteren Regionsgröße
(Merkmale b2) und b3)) nicht gezeigt.




4.3.5 Der Gegenstand von Anspruch 1 wird weder durch die Druckschrift NK 6 in
Verbindung mit der Druckschrift NK 8 noch durch die NK 6 in Verbindung mit der
NK 9 bzw. der NK 10 nahegelegt.


Die Klägerinnen stellen dar, dass sich der Gegenstand von Anspruch 1 in
naheliegender Weise aus der NK 6 in Verbindung mit der NK 8, NK 9 oder NK 10
ergebe. Die Argumentation beruht bezüglich der NK 8, NK 9 und der NK 10 auf
den gleichen Angaben, wie bei der Kombination der NK 5 mit diesen drei
Druckschriften.

                                        - 49 -


Diese Darstellung greift zu kurz. Da bereits die NK 6 nur einen „ersten“ Baum zeigt
(vgl. oben), gilt für die Kombination dieser Druckschrift mit einer der Druckschriften
NK 8, NK 9 oder NK 10 die bereits oben (vgl. II. 4.3.2, II. 4.3.3) ausgeführte
Argumentation.




5.    In Bezug auf den Patentanspruch 1 nach Hilfsantrag 1 (und analog auf den
nebengeordneten Anspruch 11) ist somit ein Nichtigkeitsgrund nicht ersichtlich.

Das Streitpatent ist somit in der Fassung nach Hilfsantrag 1 rechtsbeständig.

Auf die weiteren Hilfsanträge kam es daher nicht mehr an.




                                         III.


Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und Satz 2 Halbsatz 1 PatG
i. V. m. § 92 Abs. 2 Nr. 1 und § 100 Abs. 1 ZPO (vgl. Zöller/Herget,
Zivilprozessordnung, 34. Aufl. 2022, § 100 Rn. 1).
Vor dem Hintergrund, dass die Beklagte das Streitpatent mit der Fassung nach
Hilfsantrag 1 erfolgreich verteidigen konnte, und es sich dabei um eine lediglich
geringfügige Einschränkung des Streitpatents handelt, bewertet der Senat das
Unterliegen der Beklagten auf weniger als 1/10 des Gebührenstreitwerts. Da die
vorliegende Entscheidung damit nur sehr geringfügig hinter dem Antrag der
Beklagten zurückbleibt, erscheint eine vollständige Auferlegung der Kosten auf die
Klägerinnen nach § 92 Abs. 1 Nr. 2 ZPO gerechtfertigt und entspricht der Billigkeit.


Die Entscheidung über die vorläufige Vollstreckbarkeit beruht auf § 99 Abs. 1 PatG
i. V. m. § 709 Satz 1 und 2 ZPO.

                                              - 50 -


                                               IV.


                                  Rechtsmittelbelehrung


Gegen dieses Urteil ist das Rechtsmittel der Berufung gemäß § 110 PatG statthaft.


Die Berufung ist innerhalb eines Monats nach Zustellung des in vollständiger Form
abgefassten Urteils spätestens nach Ablauf von fünf Monaten nach Verkündung
durch einen in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder
Patentanwalt      schriftlich      beim       Bundesgerichtshof,     Herrenstraße    45a,
76133 Karlsruhe, einzulegen.


Die Berufungsschrift muss


-   die Bezeichnung des Urteils, gegen das die Berufung gerichtet ist, sowie
-   die Erklärung, dass gegen dieses Urteil Berufung eingelegt werde,


enthalten. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift
des angefochtenen Urteils vorgelegt werden.


Auf die Möglichkeit, die Berufung nach § 125a PatG in Verbindung mit § 2 der
Verordnung über den elektronischen Rechtsverkehr beim Bundesgerichtshof und
Bundespatentgericht        (BGH/BPatGERVV)             auf   elektronischem   Weg    beim
Bundesgerichtshof                      einzulegen,            wird            hingewiesen
(www.bundesgerichtshof.de/erv.html).




Hartlieb       Baumgardt                 Hoffmann        Dr. Himmelmann        Dr. Städele
            RiBPatG Baumgardt
            ist infolge Eintritts in
            den Ruhestand an der
            Unterschriftsleistung verhindert
               Hartlieb
