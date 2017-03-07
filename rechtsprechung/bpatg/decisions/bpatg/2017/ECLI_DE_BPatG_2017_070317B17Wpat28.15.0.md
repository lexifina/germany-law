---
ecli: "ECLI:DE:BPatG:2017:070317B17Wpat28.15.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 28/15"
decided: "2017-03-07"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2017&Sort=1&Seite=10&nr=29027&anz=809&pos=164&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2017-03-07_17_W-pat_28_15_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 28/15 vom 2017-03-07

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 28/15                                                  Verkündet am
_______________                                                    7. März 2017
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


             betreffend die Patentanmeldung 10 2013 016 378.1-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 7. März 2017 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Morawek,   der   Richterin   Eder,   der   Richterin
Dipl.-Phys. Dr. Thum-Rung und des Richters Dipl.-Ing. Hoffmann




BPatG 154
05.11

                                       -2-



beschlossen:


                      Die Beschwerde wird zurückgewiesen.




                                    Gründe


                                        I.


Die vorliegende Patentanmeldung wurde am 30. September 2013 beim Deutschen
Patent- und Markenamt eingereicht. Sie trägt die Bezeichnung:


       „Computer-implementiertes Aggregationsverfahren sowie Verfahren,
       Computersystem und Computerprogramm zur Betriebsüberwachung
                       von Chemieindustrieeinrichtungen“.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G06Q in der
Anhörung vom 30. April 2015 zurückgewiesen. Die Prüfungsstelle führt zur Begründung der Zurückweisung aus, dass der Gegenstand des Hauptanspruchs von
der Patentierbarkeit ausgeschlossen sei, da keine technischen Mittel zur Lösung
eines technischen Problems vorlägen.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet.


Der Vertreter der Anmelderin stellte den Antrag,


        den angegriffenen Beschluss aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:

                                       -3-



        gemäß Hauptantrag („Anspruchsreihe I“) mit
               Patentansprüchen 1–16 vom 28.05.2015,
               eingegangen am 01.06.2015,
               Beschreibung Seiten 1–43 und
               9 Blatt Zeichnungen mit Figuren 1–10, jeweils vom Anmeldetag;


        gemäß Hilfsantrag 1 („Anspruchsreihe II“) mit
               Patentansprüchen 1–15 vom 28.05.2015,
               eingegangen am 01.06.2015,
               im Übrigen wie Hauptantrag;


        gemäß Hilfsantrag 2 („Anspruchsreihe III“) mit
               Patentansprüchen 1–12 vom 28.05.2015,
               eingegangen am 01.06.2015,
               im Übrigen wie Hauptantrag;


        gemäß Hilfsantrag 3 („Anspruchsreihe IV“) mit
               Patentansprüchen 1–14 vom 21.02.2017,
               eingegangen am 22.02.2017,
               im Übrigen wie Hauptantrag;


        gemäß Hilfsantrag 4 („Anspruchsreihe V“) mit
               Patentansprüchen 1–13 vom 21.02.2017,
               eingegangen am 22.02.2017,
               im Übrigen wie Hauptantrag.


Der geltende Patentanspruch 1 nach Hauptantrag (hier mit einer denkbaren
Gliederung und der Berichtigung zweier offensichtlicher Fehler in den Merkmalen (a) und (b) versehen) lautet:

                                      -4-



(A) 1. Computer-implementiertes Verfahren zur Bildung und Speicherung zumindest einer Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines Massenstroms und/oder Energiestroms, der
   durch eine gerichtete Verbindung zwischen zwei Einheiten einer Chemieindustrieeinrichtung ﬂießt, für zumindest eine Einheit der Chemieindustrieeinrichtung,
   wobei das computer-implementierte Verfahren
     (a) mit einem Speicherinhalt in zumindest einem Speicher arbeitet, in
         dem die zu Chemieindustrieeinrichtung dadurch informationstechnisch modelliert ist,
             (a1)      dass der Speicherinhalt zumindest eine Block-Datenstruktur zur Speicherung zumindest eines Block-Datenelementes aufweist, das jeweils eine Einheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert, wobei
             (a2)      eine Hierarchie der Einheiten der Chemieeinrichtung
                       dadurch in der Block-Datenstruktur repräsentiert wird,
                       dass zumindest ein Block-Datenelement vorgesehen
                       ist, das ein übergeordnetes Block-Datenelement ist, das
                       wiederum zumindest ein untergeordnetes Block-Datenelement aufweist, wobei
             (a3)      das jeweilige übergeordnete Block-Datenelement jeweils eine übergeordnete Einheit der Chemieindustrieeinrichtung, und das jeweilige untergeordnete Block-Datenelement jeweils eine in der übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert,
                       und,
     (b) dass der Speicherinhalt zumindest eine Verbindungs-Datenstruktur
         zur Speicherung von zumindest einem Verbindungs-Datenelements
         aufweist, das jeweils einer gerichteten Verbindung zwischen jeweils

                             -5-



   zwei zueinander unterschiedlichen Block-Datenelementen entspricht,
   die eine jeweilige zugehörige gerichtete Verbindung zwischen den
   jeweiligen beiden entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert,
und wobei
(c) zumindest ein Massenstrom und/oder ein Energiestrom, der jeweils
   durch die jeweilige gerichtete Verbindung zwischen zwei Einheiten
   der Chemieindustrieeinrichtung ﬂießt, mit zumindest einer jeweiligen
   (Meß-)Größe erfaßt und jeweils als dieser gerichteten Verbindung
   abgespeichert wird, und
(d) anhand einer hierzu jeweils gespeicherten Aggregationsregel zumindest eine Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines der vorgenannten Massenströme und/
   oder Energieströme für zumindest eine Einheit der Chemieindustrieeinrichtung derart vorgenommen wird,
       (d1)     dass für die jeweilige Einheit der Chemieindustrieeinrichtung die Aggregation des ihr zugehörigen Zugangs-Stroms oder der ihr zugehörigen Zugangs-Ströme oder
                des ihr zugehörigen Abgangs-Stroms oder der ihr zugehörigen Abgangs-Ströme des zumindest einen vorgenannten Massenstromes oder Energiestromes anhand
                der in der Block-Datenstruktur gespeicherten Block-Datenelemente und anhand der in der Verbindungs-Datenstruktur   gespeicherten    Verbindungs-Datenelemente vorgenommen wird, indem
                (d1i)   jeder solche Massenstrom oder Energiestrom
                        der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Zugangs-Stromes verwendet wird, dessen zugehörige gerichtete Verbindung außerhalb der jeweiligen Einheit der Chemieindustrie-

                                      -6-



                                  einrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                  Teileinheiten beginnt und innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten
                                  endet, und ferner
                         (d1ii)   jeder solche Massenstrom oder Energiestrom
                                  der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Abgangs-Stroms verwendet wird, dessen zugehörige gerichtete Verbindung innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                  Teileinheiten beginnt und außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen Teileinheiten
                                  endet,
        und wobei
        (e) die jeweilige Aggregation entsprechend der Aggregationsregel für
            den jeweiligen Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des zumindest einen vorgenannten Massenstromes oder
            Energiestromes der jeweiligen Einheit der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert
            wird.


Zu den übrigen Ansprüchen wird auf die Akte verwiesen.

                                     -7-



Der geltende Patentanspruch 1 nach Hilfsantrag 1 (hier ebenfalls mit einer
denkbaren Gliederung, der Berichtigung zweier offensichtlicher Fehler in den
Merkmalen (a) und (b), sowie der Kennzeichnung der Unterschiede zum Hauptanspruch des Hauptantrags versehen) lautet:


   (B) 1. Computer-implementiertes Verfahren zur Betriebsüberwachung von Chemieindustrieeinrichtungen vermittels zumindest einer Kenngröße, dadurch
      gekennzeichnet, dass anhand zumindest einer gespeicherten Kenngrößen-Ermittlungsregel aus der oder den nach einem Aggregationsverfahren
      gebildeten Aggregation(en) für einen jeweiligen Zugangs-Strom und/oder
      den jeweiligen Abgangs-Strom eines jeweiligen Massenstromes und/oder
      Energiestromes und/oder Informationsstromes von einer Einheit oder von
      Einheiten der Chemieindustrieeinrichtung zumindest eine Kenngröße zur
      Betriebsüberwachung der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert wird oder werden,
      wobei es sich bei dem Aggregationsverfahren um ein


      (A*) Computer-implementiertes Aggregationsverfahren zur Bildung und
      Speicherung zumindest einer Aggregation für einen Zugangs-Strom und/
      oder einen Abgangs-Strom zumindest eines Massenstroms und/oder Energiestroms, der durch eine gerichtete Verbindung zwischen zwei Einheiten
      der einer Chemieindustrieeinrichtung ﬂießt, für zumindest eine Einheit der
      Chemieindustrieeinrichtung handelt,
      wobei das computer-implementierte Aggregationsverfahren
        (a) mit einem Speicherinhalt in zumindest einem Speicher arbeitet, in
            dem die zu Chemieindustrieeinrichtung dadurch informationstechnisch modelliert ist,
                (a1)      dass der Speicherinhalt zumindest eine Block-Datenstruktur zur Speicherung zumindest eines Block-Datenelementes aufweist, das jeweils eine Einheit der Che-

                               -8-



                mieindustrieeinrichtung in der Datenstruktur repräsentiert, wobei
       (a2)     eine Hierarchie der Einheiten der Chemieeinrichtung
                dadurch in der Block-Datenstruktur repräsentiert wird,
                dass zumindest ein Block-Datenelement vorgesehen
                ist, das ein übergeordnetes Block-Datenelement ist, das
                wiederum zumindest ein untergeordnetes Block-Datenelement aufweist, wobei
       (a3)     das jeweilige übergeordnete Block-Datenelement jeweils eine übergeordnete Einheit der Chemieindustrieeinrichtung, und das jeweilige untergeordnete Block-Datenelement jeweils eine in der übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert,
                und,
(b) dass der Speicherinhalt zumindest eine Verbindungs-Datenstruktur
   zur Speicherung von zumindest einem Verbindungs-Datenelements
   aufweist, das jeweils einer gerichteten Verbindung zwischen jeweils
   zwei zueinander unterschiedlichen Block-Datenelementen entspricht,
   die eine jeweilige zugehörige gerichtete Verbindung zwischen den
   jeweiligen beiden entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert,
und wobei
(c) zumindest ein Massenstrom und/oder ein Energiestrom, der jeweils
   durch die jeweilige gerichtete Verbindung zwischen zwei Einheiten
   der Chemieindustrieeinrichtung ﬂießt, mit zumindest einer jeweiligen
   (Meß-)Größe erfaßt und jeweils als dieser gerichteten Verbindung
   abgespeichert wird, und
(d) anhand einer hierzu jeweils gespeicherten Aggregationsregel zumindest eine Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines der vorgenannten Massenströme und/

                           -9-



oder Energieströme für zumindest eine Einheit der Chemieindustrieeinrichtung derart vorgenommen wird,
   (d1)     dass für die jeweilige Einheit der Chemieindustrieeinrichtung die Aggregation des ihr zugehörigen Zugangs-Stroms oder der ihr zugehörigen Zugangs-Ströme oder
            des ihr zugehörigen Abgangs-Stroms oder der ihr zugehörigen Abgangs-Ströme des zumindest einen vorgenannten Massenstromes oder Energiestromes anhand
            der in der Block-Datenstruktur gespeicherten Block-Datenelemente und anhand der in der Verbindungs-Datenstruktur     gespeicherten     Verbindungs-Datenelemente
            vorgenommen wird, indem
            (d1i)      jeder solche Massenstrom oder Energiestrom
                       der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Zugangs-Stromes verwendet wird, dessen zugehörige gerichtete Verbindung außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                       Teileinheiten beginnt und innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten
                       endet, und ferner
            (d1ii)     jeder solche Massenstrom oder Energiestrom
                       der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Abgangs-Stroms verwendet wird, dessen zugehörige gerichtete Verbindung innerhalb der jeweiligen Einheit der Chemieindustrie-

                                      - 10 -



                                  einrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                  Teileinheiten beginnt und außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen Teileinheiten
                                  endet,
         und wobei
         (e) die jeweilige Aggregation entsprechend der Aggregationsregel für
             den jeweiligen Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des zumindest einen vorgenannten Massenstromes oder
             Energiestromes der jeweiligen Einheit der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert
             wird.


Zu den übrigen Ansprüchen wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 nach Hilfsantrag 2 (hier ebenfalls mit einer
denkbaren Gliederung, der Berichtigung dreier offensichtlicher Fehler in den Merkmalen (A*), (a) und (b), sowie der Kennzeichnung der Unterschiede zum Hauptanspruch des Hauptantrags versehen) lautet:


   (C) 1. Computersystem zur Betriebsüberwachung von Chemieindustrieeinrichtungen, wobei das Computersystem zumindest einen Computer und zumindest einen Prozessor und mindestens einen Computersystem-Speicher
      sowie zumindest eine Erfassungseinrichtung zur Erfassung von Massenströmen und/oder Energieströmen und/oder Informationsströmen, die durch
      eine jeweilige gerichtete Verbindung zwischen zwei Einheiten der Chemieindustrieeinrichtung ﬂießen, aufweist, dadurch gekennzeichnet, dass das
      Computersystem vermittels eines Computerprogramms zur Durchführung
      eines Aggregationsverfahrens eingerichtet ist,

                                   - 11 -



wobei es sich bei dem Aggregationsverfahren um ein
(A*) Computer-implementiertes Aggregationsverfahren zur Bildung und
    Speicherung zumindest einer Aggregation für einen Zugangs-Strom
    und/oder einen Abgangs-Strom zumindest eines Massenstroms und/
    oder Energiestroms, der durch eine gerichtete Verbindung zwischen
    zwei Einheiten der einer Chemieindustrieeinrichtung ﬂießt, für zumindest eine Einheit der Chemieindustrieeinrichtung handelt handet,
wobei das computer-implementierte Aggregationsverfahren
  (a) mit einem Speicherinhalt in zumindest einem Speicher arbeitet, in
      dem die zu Chemieindustrieeinrichtung dadurch informationstechnisch modelliert ist,
         (a1)       dass der Speicherinhalt zumindest eine Block-Datenstruktur zur Speicherung zumindest eines Block-Datenelementes aufweist, das jeweils eine Einheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert, wobei
         (a2)       eine Hierarchie der Einheiten der Chemieeinrichtung
                    dadurch in der Block-Datenstruktur repräsentiert wird,
                    dass zumindest ein Block-Datenelement vorgesehen
                    ist, das ein übergeordnetes Block-Datenelement ist, das
                    wiederum zumindest ein untergeordnetes Block-Datenelement aufweist, wobei
         (a3)       das jeweilige übergeordnete Block-Datenelement jeweils eine übergeordnete Einheit der Chemieindustrieeinrichtung, und das jeweilige untergeordnete Block-Datenelement jeweils eine in der übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert,
                    und,
  (b) dass der Speicherinhalt zumindest eine Verbindungs-Datenstruktur
      zur Speicherung von zumindest einem Verbindungs-Datenelements

                             - 12 -



   aufweist, das jeweils einer gerichteten Verbindung zwischen jeweils
   zwei zueinander unterschiedlichen Block-Datenelementen entspricht,
   die eine jeweilige zugehörige gerichtete Verbindung zwischen den
   jeweiligen beiden entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert,
und wobei
(c) zumindest ein Massenstrom und/oder ein Energiestrom, der jeweils
   durch die jeweilige gerichtete Verbindung zwischen zwei Einheiten
   der Chemieindustrieeinrichtung ﬂießt, mit zumindest einer jeweiligen
   (Meß-)Größe erfaßt und jeweils als dieser gerichteten Verbindung
   abgespeichert wird, und
(d) anhand einer hierzu jeweils gespeicherten Aggregationsregel zumindest eine Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines der vorgenannten Massenströme und/
   oder Energieströme für zumindest eine Einheit der Chemieindustrieeinrichtung derart vorgenommen wird,
       (d1)     dass für die jeweilige Einheit der Chemieindustrieeinrichtung die Aggregation des ihr zugehörigen Zugangs-Stroms oder der ihr zugehörigen Zugangs-Ströme oder
                des ihr zugehörigen Abgangs-Stroms oder der ihr zugehörigen Abgangs-Ströme des zumindest einen vorgenannten Massenstromes oder Energiestromes anhand
                der in der Block-Datenstruktur gespeicherten Block-Datenelemente und anhand der in der Verbindungs-Datenstruktur    gespeicherten   Verbindungs-Datenelemente vorgenommen wird, indem
                (d1i)   jeder solche Massenstrom oder Energiestrom
                        der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Zugangs-Stromes verwendet wird, dessen zugehörige gerichtete Verbindung außer-

                                      - 13 -



                                  halb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                  Teileinheiten beginnt und innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten
                                  endet, und ferner
                         (d1ii)   jeder solche Massenstrom oder Energiestrom
                                  der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Abgangs-Stroms verwendet wird, dessen zugehörige gerichtete Verbindung innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                  Teileinheiten beginnt und außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen Teileinheiten
                                  endet,
        und wobei
        (e) die jeweilige Aggregation entsprechend der Aggregationsregel für
            den jeweiligen Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des zumindest einen vorgenannten Massenstromes oder
            Energiestromes der jeweiligen Einheit der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert
            wird.


Zu den übrigen Ansprüchen wird auf die Akte verwiesen.

                                     - 14 -



Der geltende Patentanspruch 1 nach Hilfsantrag 3 (hier ebenfalls mit einer
denkbaren Gliederung, der Berichtigung von offensichtlichen Fehlern in den Merkmalen (a), (b) und (e), sowie der Kennzeichnung der Unterschiede zum
Hauptanspruch des Hauptantrags versehen) lautet:


  (B) 1. Computer-implementiertes Verfahren zur Betriebsüberwachung von Chemieindustrieeinrichtungen vermittels zumindest einer Kenngröße, dadurch
      gekennzeichnet, dass anhand zumindest einer gespeicherten Kenngrößen-Ermittlungsregel aus der oder den nach einem Aggregationsverfahren gebildeten Aggregation(en) für einen jeweiligen Zugangs-Strom und/oder den
      jeweiligen Abgangs-Strom eines jeweiligen Massenstromes und/oder Energiestromes und/oder Informationsstromes von einer Einheit oder von Einheiten der Chemieindustrieeinrichtung zumindest eine Kenngröße zur Betriebsüberwachung der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert wird oder werden,
  wobei es sich bei dem Aggregationsverfahren um ein


      (A*) Computer-implementiertes Aggregationsverfahren zur Bildung und
           Speicherung zumindest einer Aggregation für einen Zugangs-Strom
           und/oder einen Abgangs-Strom zumindest eines Massenstroms und/
           oder Energiestroms, der durch eine gerichtete Verbindung zwischen
           zwei Einheiten der Chemieindustrieeinrichtung ﬂießt, für zumindest
           eine Einheit der Chemieindustrieeinrichtung handelt,
      wobei das computer-implementierte Aggregationsverfahren
         (a) mit einem Speicherinhalt in zumindest einem Speicher arbeitet, in
            dem die zu Chemieindustrieeinrichtung dadurch informationstechnisch modelliert ist,
                (a1)      dass der Speicherinhalt zumindest eine Block-Datenstruktur zur Speicherung zumindest eines Block-Datenelementes aufweist, das jeweils eine Einheit der Che-

                               - 15 -



                mieindustrieeinrichtung in der Datenstruktur repräsentiert, wobei
       (a2)     eine Hierarchie der Einheiten der Chemieeinrichtung
                dadurch in der Block-Datenstruktur repräsentiert wird,
                dass zumindest ein Block-Datenelement vorgesehen
                ist, das ein übergeordnetes Block-Datenelement ist, das
                wiederum zumindest ein untergeordnetes Block-Datenelement aufweist, wobei
       (a3)     das jeweilige übergeordnete Block-Datenelement jeweils eine übergeordnete Einheit der Chemieindustrieeinrichtung, und das jeweilige untergeordnete Block-Datenelement jeweils eine in der übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert,
                und,
(b) dass der Speicherinhalt zumindest eine Verbindungs-Datenstruktur
   zur Speicherung von zumindest einem Verbindungs-Datenelements
   aufweist, das jeweils einer gerichteten Verbindung zwischen jeweils
   zwei zueinander unterschiedlichen Block-Datenelementen entspricht,
   die eine jeweilige zugehörige gerichtete Verbindung zwischen den
   jeweiligen beiden entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert,
und wobei
(c) zumindest ein Massenstrom und/oder ein Energiestrom, der jeweils
   durch die jeweilige gerichtete Verbindung zwischen zwei Einheiten
   der Chemieindustrieeinrichtung ﬂießt, mit zumindest einer jeweiligen
   (Meß-)Größe erfaßt und jeweils als dieser gerichteten Verbindung
   abgespeichert wird, und
(d) anhand einer hierzu jeweils gespeicherten Aggregationsregel zumindest eine Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines der vorgenannten Massenströme und/

                         - 16 -



oder Energieströme für zumindest eine Einheit der Chemieindustrieeinrichtung derart vorgenommen wird,
   (d1)     dass für die jeweilige Einheit der Chemieindustrieeinrichtung die Aggregation des ihr zugehörigen Zugangs-Stroms oder der ihr zugehörigen Zugangs-Ströme oder
            des ihr zugehörigen Abgangs-Stroms oder der ihr zugehörigen Abgangs-Ströme des zumindest einen vorgenannten Massenstromes oder Energiestromes anhand
            der in der Block-Datenstruktur gespeicherten Block-Datenelemente und anhand der in der Verbindungs-Datenstruktur    gespeicherten   Verbindungs-Datenelemente vorgenommen wird, indem
            (d1i)    jeder solche Massenstrom oder Energiestrom
                     der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Zugangs-Stromes verwendet wird, dessen zugehörige gerichtete Verbindung außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                     Teileinheiten beginnt und innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten
                     endet, und ferner
            (d1ii)   jeder solche Massenstrom oder Energiestrom
                     der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Abgangs-Stroms verwendet wird, dessen zugehörige gerichtete Verbindung innerhalb der jeweiligen Einheit der Chemieindustrie-

                                     - 17 -



                                 einrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
                                 Teileinheiten beginnt und außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen Teileinheiten
                                 endet,
         und wobei
         (e) die jeweilige Aggregation entsprechend der Aggregationsregel für
            den jeweiligen Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des zumindest einen vorgenannten Massenstromes oder
            Energiestromes der jeweiligen Einheit der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert
            wird,.
         und wobei
         (f) als Aggregationsregel zur Aggregation des Zugangs-Stroms und/
            oder des Abgangs-Stroms des jeweiligen Massenstromes und/oder
            Energiestromes und/oder Informationsstromes der jeweiligen Einheit
            der Chemieindustrieeinrichtung eine Aufsummierung, eine Mittelwertbildung oder eine Extremwertbildung der jeweils erfaßten (Meß-)
            Größe der jeweils zur Aggregation zu verwendenden Masseströme
            und/oder Energieströme und/ oder Informationsströme vorgesehen
            ist.


Zu den übrigen Ansprüchen wird auf die Akte verwiesen.


Der geltende Patentanspruch 1 nach Hilfsantrag 4 (hier ebenfalls mit einer
denkbaren Gliederung, der Berichtigung von offensichtlichen Fehlern in den Merkmalen (a) und (b), sowie der Kennzeichnung der Unterschiede zum Hauptanspruch des Hauptantrags versehen) lautet:

                                       - 18 -



(B) 1. Computer-implementiertes Verfahren zur Betriebsüberwachung von Chemieindustrieeinrichtungen vermittels zumindest einer Kenngröße, dadurch
   gekennzeichnet, dass anhand zumindest einer gespeicherten Kenngrößen-Ermittlungsregel aus der oder den nach dem Aggregationsverfahren gebildeten Aggregation(en) für einen jeweiligen Zugangs-Strom und/oder den
   jeweiligen Abgangs-Strom eines jeweiligen Massenstromes und/oder Energiestromes und/oder Informationsstromes von einer Einheit oder von Einheiten der Chemieindustrieeinrichtung zumindest eine Kenngröße zur Betriebsüberwachung der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert wird oder werden,
wobei es sich bei dem Aggregationsverfahren um ein


   (A*) Computer-implementiertes Aggregationsverfahren zur Bildung und
        Speicherung zumindest einer Aggregation für einen Zugangs-Strom
        und/oder einen Abgangs-Strom zumindest eines Massenstroms und/
        oder Energiestroms, der durch eine gerichtete Verbindung zwischen
        zwei Einheiten der Chemieindustrieeinrichtung ﬂießt, für zumindest
        eine Einheit der Chemieindustrieeinrichtung handelt,
   wobei das computer-implementierte Aggregationsverfahren
      (a) mit einem Speicherinhalt in zumindest einem Speicher arbeitet, in
          dem die zu Chemieindustrieeinrichtung dadurch informationstechnisch modelliert ist,
             (a1)       dass der Speicherinhalt zumindest eine Block-Datenstruktur zur Speicherung zumindest eines Block-Datenelementes aufweist, das jeweils eine Einheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert, wobei
             (a2)       eine Hierarchie der Einheiten der Chemieeinrichtung
                        dadurch in der Block-Datenstruktur repräsentiert wird,
                        dass zumindest ein Block-Datenelement vorgesehen
                        ist, das ein übergeordnetes Block-Datenelement ist, das

                             - 19 -



                wiederum zumindest ein untergeordnetes Block-Datenelement aufweist, wobei
       (a3)     das jeweilige übergeordnete Block-Datenelement jeweils eine übergeordnete Einheit der Chemieindustrieeinrichtung, und das jeweilige untergeordnete Block-Datenelement jeweils eine in der übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung in der Datenstruktur repräsentiert,
                und,
(b) dass der Speicherinhalt zumindest eine Verbindungs-Datenstruktur
   zur Speicherung von zumindest einem Verbindungs-Datenelements
   aufweist, das jeweils einer gerichteten Verbindung zwischen jeweils
   zwei zueinander unterschiedlichen Block-Datenelementen entspricht,
   die eine jeweilige zugehörige gerichtete Verbindung zwischen den
   jeweiligen beiden entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert,
und wobei
(c) zumindest ein Massenstrom und/oder ein Energiestrom, der jeweils
   durch die jeweilige gerichtete Verbindung zwischen zwei Einheiten
   der Chemieindustrieeinrichtung ﬂießt, mit zumindest einer jeweiligen
   (Meß-)Größe erfaßt und jeweils als dieser gerichteten Verbindung
   abgespeichert wird, und
(d) anhand einer hierzu jeweils gespeicherten Aggregationsregel zumindest eine Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom zumindest eines der vorgenannten Massenströme und/
   oder Energieströme für zumindest eine Einheit der Chemieindustrieeinrichtung derart vorgenommen wird,
       (d1)     dass für die jeweilige Einheit der Chemieindustrieeinrichtung die Aggregation des ihr zugehörigen Zugangs-Stroms oder der ihr zugehörigen Zugangs-Ströme oder
                des ihr zugehörigen Abgangs-Stroms oder der ihr zuge-

             - 20 -



hörigen Abgangs-Ströme des zumindest einen vorgenannten Massenstromes oder Energiestromes anhand
der in der Block-Datenstruktur gespeicherten Block-Datenelemente und anhand der in der Verbindungs-Datenstruktur    gespeicherten   Verbindungs-Datenelemente vorgenommen wird, indem
(d1i)    jeder solche Massenstrom oder Energiestrom
         der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Zugangs-Stromes verwendet wird, dessen zugehörige gerichtete Verbindung außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
         Teileinheiten beginnt und innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten
         endet, und ferner
(d1ii)   jeder solche Massenstrom oder Energiestrom
         der jeweiligen Einheit der Chemieindustrieeinrichtung für die jeweilige Aggregation des zugehörigen Abgangs-Stroms verwendet wird, dessen zugehörige gerichtete Verbindung innerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen
         Teileinheiten beginnt und außerhalb der jeweiligen Einheit der Chemieindustrieeinrichtung einschließlich aller ihrer hierarchisch untergeord-

                                      - 21 -



                                  neten und in ihr enthaltenen Teileinheiten
                                  endet,
         und wobei
         (e) die jeweilige Aggregation entsprechend der Aggregationsregel für
             den jeweiligen Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des zumindest einen vorgenannten Massenstromes oder
             Energiestromes der jeweiligen Einheit der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert
             wird,
         und wobei
         (f) als Aggregationsregel zur Aggregation des Zugangs-Stroms und/
             oder des Abgangs-Stroms des jeweiligen Massenstromes und/oder
             Energiestromes und/oder Informationsstromes der jeweiligen Einheit
             der Chemieindustrieeinrichtung eine Aufsummierung, eine Mittelwertbildung oder eine Extremwertbildung der jeweils erfaßten (Meß-)
             Größe der jeweils zur Aggregation zu verwendenden Masseströme
             und/oder Energieströme und/ oder Informationsströme vorgesehen
             ist,
         und wobei
         (g) die Aggregation des Zugangs-Stroms und/oder des Abgangs-Stroms
             des jeweiligen Massenstromes und/oder Energiestromes und/oder
             Informationsstromes der jeweiligen Einheit der Chemieindustrieeinrichtung über einen zu wählenden Zeitraum erfolgt.


Zu den übrigen Ansprüchen wird auf die Akte verwiesen.


Im Verfahren wurde folgende Druckschrift genannt:


D1:   DE 10 2007 046 962 A1.


Zu den Einzelheiten wird auf die Akte verwiesen.

                                       - 22 -



                                         II.


Die Beschwerde wurde frist- und formgerecht eingelegt und ist auch sonst zulässig. Sie hat jedoch keinen Erfolg, da das beanspruchte Verfahren nach Patentanspruch 1 des Hauptantrags und auch die jeweiligen beanspruchten Verfahren
nach Patentanspruch 1 der Hilfsanträge 1 bis 4 nicht auf einer erfinderischen
Tätigkeit beruhen (§ 1 i. V. m. § 4 Satz 1 PatG).




1.    Die vorliegende Patentanmeldung betrifft ein computer-implementiertes
Aggregationsverfahren zur Bildung und Speicherung zumindest einer Aggregation
für einen Zugangs-Strom (auch Input-Strom genannt) und/oder einen Abgangs-Strom (auch Output-Strom genannt) zumindest eines Massenstroms und/oder
Energiestroms, der durch eine gerichtete Verbindung zwischen zwei Einheiten
einer Chemieindustrieeinrichtung fließt für zumindest eine Einheit der Chemieindustrieeinrichtung, sowie ein hierauf aufbauendes computer-implementiertes Verfahren und ein ebenfalls hierauf aufbauendes Computersystem jeweils zur Betriebsüberwachung von Chemieindustrieeinrichtungen (Offenlegungsschrift, Absatz [0001]).


Aus dem Stand der Technik seien Kennzahlensysteme aus der Betriebswirtschaftslehre, die einen hierarchischen Bezug vorwiesen und komplexe Vorgänge
abzubilden suchten, bekannt. Ebenso seien Modellierungen von Verbundsystemen, der Einsatz von Optimierungs-Algorithmen, Manufacturing-Execution-Systeme und Energiemanagementsysteme bekannt (vgl. Offenlegungsschrift, Absätze
[0003]–[0011]).


Es existiere jedoch kein Verfahren und kein System, das es erlaube technische
Kenngrößen auf unterschiedlichen Hierarchieebenen einer als Verbundsystem
ausgestalteten Chemieindustrieeinrichtung zu erfassen, konsistent zu modellieren
und auf dieser Grundlage zunächst zur Überwachung der Chemieindustrieein-

                                        - 23 -



richtung, letztlich aber auch zur ihrer Steuerung und/oder Optimierung zur Verfügung zu stellen. Es werde nirgends der konkrete Einsatz von Kenngrößen in
einem hierarchischen Verbundsystem der chemischen Industrie beschrieben.
Auch sei aus dem Stand der Technik nicht zu entnehmen, ob solche Kenngrößen
in einer Chemieindustrieeinrichtung erfasst werden können, um die Einrichtung zu
überwachen und eine Prozesssteuerung und/oder Prozessoptimierung der Chemieindustrieeinrichtung vornehmen zu können (vgl. Offenlegungsschrift, Absätze
[0002], [0012]).


Der Anmeldung soll die Aufgabe zugrunde liegen, ein Verfahren und System zur
Überwachung der Chemieindustrieeinrichtung anzugeben, das in der Lage ist, auf
Einheiten unterschiedlicher Hierarchieebenen einer als Verbundsystem ausgestalteten Chemieindustrieeinrichtung bezogene technische Kenngrößen zu bilden und
so die Chemieindustrieeinrichtung, vorzugsweise im Hinblick auf deren Ressourceneffizienz anhand dieser technischen Kenngrößen zu überwachen (Offenlegungsschrift, Absatz [0016]).


Zur Lösung dieser Aufgabe schlägt der Patentanspruch 1 nach Hauptantrag ein
computer-implementiertes Verfahren zur Bildung und Speicherung einer Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom eines Massenstroms
und/oder Energiestroms, der durch eine gerichtete Verbindung zwischen zwei Einheiten einer Chemieindustrieeinrichtung ﬂießt, vor (Merkmal (A)).


Das Verfahren arbeitet mit dem Inhalt eines Speichers, in dem die Chemieindustrieeinrichtung informationstechnisch modelliert ist,
wobei der Speicherinhalt eine Block-Datenstruktur aufweist, in der ein Block-Datenelement eine Einheit der Chemieindustrieeinrichtung repräsentiert, und in der
eine Hierarchie der Einheiten der Chemieeinrichtung durch mindestens ein übergeordnetes Block-Datenelement und mindestens ein untergeordnetes Block-Datenelement dargestellt wird, welche eine übergeordnete Einheit und eine in der

                                        - 24 -



übergeordneten Einheit enthaltene untergeordnete Teileinheit der Chemieindustrieeinrichtung repräsentieren (Merkmale (a), (a1) – (a3)).
Weiterhin weist der Speicherinhalt eine Verbindungs-Datenstruktur zur Speicherung mindestens eines Verbindungs-Datenelements auf, welches einer gerichteten
Verbindung zwischen zwei Block-Datenelementen entspricht und die Verbindung
zwischen den entsprechenden in der Block-Datenstruktur repräsentierten Einheiten der Chemieindustrieeinrichtung repräsentiert (Merkmal (b)).
Das Verfahren erfasst den Massenstrom und/oder den Energiestrom, der durch
die gerichtete Verbindung zwischen zwei Einheiten ﬂießt, und speichert diese
(Meß-)Größe ab (Merkmal (c)).
Aus diesen (Meß-)Größen wird mit einer gespeicherten Aggregationsregel eine
Aggregation für einen Zugangs-Strom und/oder einen Abgangs-Strom eines der
Massenströme und/oder Energieströme für eine Einheit der Chemieindustrieeinrichtung vorgenommen (Merkmal (d)), wobei die Aggregation des zu der jeweiligen Einheit gehörigen Zugangs-Stroms oder des ihr zugehörigen Abgangs-Stroms
anhand der Block-Datenelemente und anhand der Verbindungs-Datenelemente
vorgenommen wird (Merkmal (d1)). Dazu wird für die Aggregation des Zugangs-Stromes jeder Massenstrom oder Energiestrom der jeweiligen Einheit der Chemieindustrieeinrichtung verwendet, dessen zugehörige gerichtete Verbindung außerhalb der jeweiligen Einheit einschließlich aller ihrer hierarchisch untergeordneten
und in ihr enthaltenen Teileinheiten beginnt und innerhalb der jeweiligen Einheit
einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenden Teileinheiten endet, und für die Aggregation des Abgangs-Stromes wird jeder Massenstrom oder Energiestrom der jeweiligen Einheit verwendet, dessen zugehörige
gerichtete Verbindung innerhalb der jeweiligen Einheit einschließlich aller ihrer hierarchisch untergeordneten und in ihr enthaltenen Teileinheiten beginnt und außerhalb der jeweiligen Einheit einschließlich aller ihrer hierarchisch untergeordneten
und in ihr enthaltenen Teileinheiten endet (Merkmale (d1i) und (d1ii)).
Die jeweilige Aggregation wird entsprechend der Aggregationsregel für den Zugangs-Strom und/oder den jeweiligen Abgangs-Strom des vorgenannten Massen-

                                      - 25 -



stromes oder Energiestromes der Einheit der Chemieindustrieeinrichtung gebildet
und zur Weiterverarbeitung oder Anzeige gespeichert (Merkmal (e)).


In Patentanspruch 1 nach Hilfsantrag 1 ist zusätzlich zu Patentanspruch 1 nach
Hauptantrag am Anfang des Anspruchs angegeben, dass es sich um ein computer-implementiertes Verfahren zur Betriebsüberwachung von Chemieindustrieeinrichtungen mit einer Kenngröße handelt, bei dem anhand einer gespeicherten
Kenngrößen-Ermittlungsregel aus der nach einem Aggregationsverfahren gebildeten Aggregation für einen Zugangs-Strom und/oder den Abgangs-Strom eines
Massenstromes und/oder Energiestromes und/oder Informationsstromes von einer
Einheit oder von Einheiten der Chemieindustrieeinrichtung eine Kenngröße zur
Betriebsüberwachung der Chemieindustrieeinrichtung gebildet und zur Weiterverarbeitung oder Anzeige gespeichert wird (Merkmal (B)).
Weiterhin ist in Merkmal (A*) gegenüber dem ursprünglichen Merkmal (A) präzisiert, dass es sich um ein Aggregationsverfahren handelt.


In Patentanspruch 1 nach Hilfsantrag 2 ist zusätzlich zu Patentanspruch 1 nach
Hauptantrag am Anfang des Anspruchs angegeben, dass es sich um ein Computersystem zur Betriebsüberwachung von Chemieindustrieeinrichtungen handelt,
wobei das Computersystem einen Computer, einen Prozessor und einen Computersystem-Speicher sowie eine Erfassungseinrichtung zur Erfassung von Massenströmen und/oder Energieströmen und/oder Informationsströmen, die durch eine
jeweilige gerichtete Verbindung zwischen zwei Einheiten der Chemieindustrieeinrichtung ﬂießen, aufweist und wobei das Computersystem vermittels eines Computerprogramms zur Durchführung eines Aggregationsverfahrens eingerichtet ist.
Zusätzlich ist in Merkmal (A*) gegenüber dem ursprünglichen Merkmal (A) präzisiert, dass es sich um ein Aggregationsverfahren handelt.


Patentanspruch 1 nach Hilfsantrag 3 basiert auf Patentanspruch 1 nach Hilfsantrag 1 und enthält zusätzlich, dass als Aggregationsregel zur Aggregation des
Zugangs-Stroms und/oder des Abgangs-Stroms des jeweiligen Massenstromes

                                        - 26 -



und/oder Energiestromes und/oder Informationsstromes der Einheit der Chemieindustrieeinrichtung eine Aufsummierung, eine Mittelwertbildung oder eine Extremwertbildung der jeweils erfassten (Meß-)Größe der zur Aggregation zu verwendenden Masseströme und/oder Energieströme und/ oder Informationsströme vorgesehen ist (Merkmal (f)).


Patentanspruch 1 nach Hilfsantrag 4 basiert auf Patentanspruch 1 nach Hilfsantrag 3 und enthält zusätzlich, dass die Aggregation des Zugangs-Stroms und/
oder des Abgangs-Stroms des Massenstromes und/oder Energiestromes und/oder
Informationsstromes der Einheit der Chemieindustrieeinrichtung über einen zu
wählenden Zeitraum erfolgt (Merkmal (g)).


Als Fachmann, der mit der Aufgabe betraut wird, ein Verfahren zur Überwachung
von Chemieindustrieeinrichtungen zu verbessern, ist ein Programmierer oder
Informatiker mit mehrjähriger Berufserfahrung in der Systemmodellierung im Bereich der Anlagensteuerung anzusehen.




2.     Das jeweilige Verfahren nach Patentanspruch 1 des Hauptantrags sowie
der Hilfsanträge 1 bis 4 beruht nicht auf einer erfinderischen Tätigkeit.


Diese Verfahren waren nämlich für den Fachmann durch die Druckschrift D1
nahegelegt, aus der eine intelligente Steuerungs- und Simulationsumgebung zu
entnehmen ist, welche die Integration und Aktualisierung von Simulationsaktivitäten in einem Online-Steuerungssystem auf einer Systemebene der Prozessanlagen-Steuerungsarchitektur ermöglicht.


2.1.   Das Verfahren des Patentanspruchs 1 nach Hauptantrag beruht nicht auf
einer erfinderischen Tätigkeit.
Aus der D1 ist ein Ausführungsprogramm (Computer-implementiertes Verfahren)
zu entnehmen, mit dem Durchfluss- und Massenbilanzen innerhalb einer Prozess-

                                       - 27 -



anlage berechnet werden können (Absätze [0125], [0126], Fig. 10), wobei es sich
bei den betrachteten Prozessen auch um die Prozesse einer Chemieanlage handeln kann (Absatz [0003]).


In D1 wird die Anlage mit ihren einzelnen Abschnitten mit Hilfe von Prozessobjekten modelliert, die in einem Computersystem (d. h. in einer Speichereinrichtung
des Computersystems) gespeichert sind (Absatz [0010] – Merkmal (a)).


Intelligente, konfigurierbare Prozessobjekte werden hierbei realen Objekten innerhalb der Prozessanlage zugeordnet (Absätze [0031], [0033], [0034] und Fig. 2).
Jedes intelligente Prozessobjekt kann eine Bibliothek mit vom Benutzer veränderbaren Algorithmen, Verfahren und/oder Regeln beinhalten, welche etwa zur Berechnung von Massenbilanzen herangezogen werden können (Absätze [0037] bis
[0040]). Ein oder mehrere Prozessobjekte können zu Prozessmodulen und mehrere Prozessmodule können zu übergeordneten Prozessmodulen zusammengefasst werden, wobei die Prozessmodule in einem Prozessmodulspeicher (Fig. 2:
„46“) abgelegt sind (Absätze [0031], [0087] bis [0091]). So zeigt Fig. 5 eine Ansicht
mit übergeordneten Modulen, die einen größeren Teil einer Prozessanlage abbilden, während in Fig. 6 eine feinere Einteilung eines dieser Module (100) in untergeordnete Elemente dargestellt ist, welche untergeordneten realen Objekten (Einheiten) der Prozessanlage entsprechen. Damit ist eine hierarchische Struktur mit
über- und untergeordneten Elementen (Block-Datenelemente in der Nomenklatur
der vorliegenden Anmeldung) vorhanden, die in der Speichereinrichtung des
Computersystems abgelegt ist, und die eine Struktur der Einheiten der Prozessanlage repräsentiert – Merkmale (a1), (a2), (a3).


Gemäß Absatz [0011] erhält jedes Prozessmodul Eingänge und erzeugt Ausgänge entsprechend den Mengen an Flüssigkeit, Gas oder anderer Materialien,
die die Anlage durchlaufen. Somit kann die Arbeitsweise der zugehörigen Einheit
innerhalb der Anlage und ihr Einfluss auf die Bewegung der Flüssigkeit oder ande-

                                      - 28 -



rer Materialien in der Anlage simuliert werden. Es können auch (Mess-)Daten aus
der tatsächlichen Anlage abgerufen und dargestellt werden.


Um die Verbindungen zwischen den Prozessobjekten (und damit zwischen den
realen Objekten der Anlage) zu modellieren, können intelligente Verbindungsobjekte (Verbindungs-Datenelemente in der Nomenklatur der vorliegenden Anmeldung) genutzt werden, was bei der Erzeugung eines Modells des Betriebs der
Anlage mit ihrem Materialfluss hilfreich ist (Absatz [0012]). Intelligente Verbindungsobjekte können den Strom durch den Verbinder modellieren und die mögliche Richtung des Stroms beschreiben (Absatz [0044]). Dass die Verbindungsobjekte mit ihrer durch die Anlage vorgegebenen Struktur ebenso wie die Prozessobjekte und -module in einem zugeordneten Speicher abgelegt sind, liest der
Fachmann in D1 mit – Merkmal (b).


Es können Messelemente auf Verbindungselemente gesetzt werden, um z. B. den
Durchfluss von Material in einer Rohrleitung zu messen (Absätze [0053], [0054]).
Im Online-Modus kann der Wert der Messung im Grafikdisplay unmittelbar am
Messelement angezeigt werden (Absatz [0066]).
Somit kann der Strom durch die gerichtete Verbindung zwischen zwei durch Prozessmodule modellierten Einheiten der Anlage messtechnisch erfasst und (etwa
zur Anzeige) gespeichert werden – Merkmal (c).


Zudem werden intelligente Stromobjekte bereitgestellt, welche Materialströme
innerhalb der Anlage zugeordnet sind, wobei die Eigenschaften der Ströme durch
die durchlaufenen Prozesselemente beeinflusst werden (Absatz [0013]). Stromelemente können am Eingang oder am Ende eines Prozessmoduls definiert werden und beinhalten u. a. die Richtung des Stroms sowie Messgrößen wie Durchfluss, Druck und Temperatur; beispielsweise kann der Ausgangsstrom in einem
Prozessmodul den Eingangsstrom eines anderen Prozessmoduls bilden (Absatz
[0050]).

                                      - 29 -



Mit dem System der D1 können Durchfluss- und Massenbilanzen sowie Verluste
innerhalb der Anlage berechnet und verfolgt werden (Absatz [0125]).


Das System der D1 ist dafür ausgelegt, Ströme in unterschiedlichen Hierarchieebenen zu repräsentieren und zu verfolgen, wobei die Bezeichnung eines Stroms
innerhalb des gesamten Systems unverwechselbar sein soll (Absätze [0087] bis
[0089], Fig. 4 und 5). Damit bot es sich für den Fachmann an, zur Berechnung von
Strombilanzen und -verlusten zumindest für jedes Prozessmodul einer oberen Hierarchieebene (d. h. für die dadurch repräsentierte Einheit der Anlage, einschließlich der zugehörigen Untereinheiten) eine Bilanz der einzelnen Ströme zu erstellen, die dann für alle diese Module zu einer Gesamtbilanz zusammengefasst oder
auch für jedes Modul einzeln ausgewertet werden können. Wie dem in der Modellierung von Chemieanlagen bewanderten Fachmann bewusst war, werden hierbei
Zugangsströme und Abgangsströme getrennt behandelt, d. h. Ströme, die in der
jeweiligen Einheit (einschließlich ihrer jeweiligen Untereinheiten) beginnen oder
enden; vgl. D1 Absatz [0050], wonach Stromelemente für den Eingang und Stromelemente für den Ausgang eines Prozessmoduls definiert werden können, wobei
z. B. der Ausgangsstrom in einem Prozessmodul den Eingangsstrom eines anderen Prozessmoduls bilden kann – Merkmale (d1i), (d1ii).


Zur Erstellung einer Bilanz für die Zugangs- bzw. Abgangsströme eines Moduls
muss dann für jeden Materialfluss eine Aggregation vorgenommen werden, etwa
als eine Summierung der gemessenen Durchflusswerte über die Zugangs- bzw.
Abgangsströme für das jeweilige Modul (einschließlich seiner Untermodule); hierfür können in der zugehörigen Bibliothek gespeicherte Verfahren und Regeln verwendet werden (Absätze [0037] bis [0040]) – Merkmal (d) sowie Merkmal (f) in der
Alternative „Aufsummierung“. Dass hierbei die in der Block-Datenstruktur gespeicherten Block-Datenelemente und ebenso die in der Verbindungs-Datenstruktur
gespeicherten Verbindungs-Datenelemente berücksichtigt werden, welche die hierarchische Struktur der Chemieanlage mit ihren Einheiten und Untereinheiten
sowie deren Verbindungen wiedergeben, versteht sich von selbst – Merkmal (d1).

                                        - 30 -



Insgesamt war damit ein Verfahren nahegelegt, um für zumindest eine Einheit
einer Chemieindustrieeinrichtung eine Aggregation für einen Zugangsstrom und
für einen Abgangsstrom zumindest eines Massenstroms, der durch eine gerichtete
Verbindung zwischen zwei Einheiten einer Chemieindustrieeinrichtung fließt, zu
bilden. Dass die Ergebnisse der Aggregation in dem verwendeten Computersystem gespeichert werden, z. B. für eine Anzeige, ist für den Fachmann selbstverständlich – Merkmale (A), (A*) und (e).


Die dargestellte Argumentation beinhaltet jeweils die Alternative „Massenstrom“
des Anspruchs 1 gemäß Hauptantrag. Im Übrigen wäre die Anwendung auf Energieströme für den Fachmann ebenfalls naheliegend.


Damit gelangte der Fachmann ausgehend von D1 in naheliegender Weise zum
Gegenstand des Patentanspruchs 1 nach Hauptantrag.


2.2.   Ebenso beruht das Verfahren des Patentanspruchs 1 nach Hilfsantrag 1
nicht auf einer erfinderischen Tätigkeit.


Bei der Beurteilung der erfinderischen Tätigkeit werden im Folgenden nur das
Merkmal (B) sowie die Änderungen in Merkmal (A*) betrachtet. Zu den übrigen
Merkmalen wird auf die Ausführungen zum Patentanspruch 1 des Hauptantrags
verwiesen.


In der D1 ist ein Applikationspaket beschrieben, das aus mehreren Applikationen
(Softwareanwendungen) besteht, die auf einem Prozessor ausgeführt werden. Mit
Hilfe dieser Softwareanwendungen werden auf Basis von Werten der Anlage
Daten erzeugt und einem Benutzer entsprechende Informationen angezeigt, die
sich auf den Betrieb der Anlage sowie deren Elemente und somit auf die Überwachung der Anlage beziehen. Wie bereits bei Anspruch 1 nach Hauptantrag ausgeführt, entsprechen die Werte Daten aus der realen Anlage mit denen Durchfluss- und Massenbilanzen aus den Eingangs- und Ausgangswerten ermittelt wer-

                                        - 31 -



den. Diese Daten werden gemeinsam mit Daten aus einem Verfahrensspeicher
(Kenngrößen der Einheiten) auch für die Überwachung von Zuständen oder für die
Feststellung von Abweichungen und deren Anzeige verwendet (Absätze [0028],
[0029], [0036] – Merkmal (B)).


Merkmal (A) des Patentanspruchs 1 nach Hauptantrag und Merkmal (A*) des
Patentanspruchs 1 nach Hilfsantrag 1 besagen inhaltlich dasselbe und sind somit
durch D1 nahegelegt (s. oben).


Der Fachmann gelangte ausgehend von D1 somit auch in naheliegender Weise
zum Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1.


2.3.   Auch das Verfahren des Patentanspruchs 1 nach Hilfsantrag 2 beruht
nicht auf einer erfinderischen Tätigkeit.


Im Folgenden wird bei der Beurteilung der erfinderischen Tätigkeit nur das Merkmal (C) betrachtet. Zu den übrigen Merkmalen wird auf die Ausführungen zum
Patentanspruch 1 des Hilfsantrags 1 verwiesen.


Die D1 zeigt ein auf Rechnern basierendes Computersystem, welches für die
Betriebsüberwachung verwendet wird und eine Workstation (Computer), einen
Speicher und einen Prozessor umfasst. Die Verwendung des Systems zur Erfassung von Werten und der darauf basierenden Ermittlung von Durchfluss- und Massenbilanzen innerhalb einer Prozessanlage ist ebenso gezeigt (Zusammenfassung, Absätze [0028], [0029], [0036], [0125], [0126], Fig. 1, Fig. 10 – Merkmal (C)).


Somit gelangte der Fachmann ausgehend von D1 auch in naheliegender Weise
zum Gegenstand des Patentanspruchs 1 nach Hilfsantrag 2.

                                        - 32 -



2.4.   Ebenso beruht das Verfahren des Patentanspruchs 1 nach Hilfsantrag 3
nicht auf einer erfinderischen Tätigkeit.


Im Folgenden wird bei der Beurteilung der erfinderischen Tätigkeit nur das Merkmal (f) betrachtet. Zu den übrigen Merkmalen wird auf die Ausführungen zum
Patentanspruch 1 des Hilfsantrags 1 verwiesen.


Die D1 beschreibt die Berechnung der Massenbilanzen, Energiebilanzen, Durchflüsse und weiterer Parameter, mit Hilfe von vorgegebenen bzw. vom Benutzer
eingebbarer Algorithmen (Absätze [0037]–[0040]). Für den Fachmann lag es auf
der Hand für die genannten Berechnungen übliche Algorithmen wie bspw. eine
zeitliche Mittelwertbildung oder eine Aufsummierung zu verwenden. Somit war
Merkmal (f) durch die Druckschrift zumindest nahegelegt.


Damit gelangte der Fachmann ausgehend von D1 in naheliegender Weise zum
Gegenstand des Patentanspruchs 1 nach Hilfsantrag 3.


2.5.   Schließlich beruht auch das Verfahren des Patentanspruchs 1 nach
Hilfsantrag 4 nicht auf einer erfinderischen Tätigkeit.


Für die Beurteilung der erfinderischen Tätigkeit wird im Folgenden nur das Merkmal (g) betrachtet. Zu den übrigen Merkmalen wird auf die Ausführungen zum
Patentanspruch 1 des Hilfsantrags 3 verwiesen.


Aus D1 ist die Berechnung von Werten (Aggregation) zu einem bestimmten Zeitpunkt und über einen bestimmten Zeitraum zu entnehmen (Absätze [0120], [0121],
Fig. 9 – Merkmal (g)).


Der Fachmann gelangte somit ausgehend von D1 auch in naheliegender Weise
zum Gegenstand des Patentanspruchs 1 nach Hilfsantrag 4.

                                       - 33 -



2.6.   Der Vertreter der Anmelderin stellt als Vorteil des anmeldungsgemäßen
Verfahrens dar, dass damit eine Chemieindustrieeinrichtung, welche als ein Verbundsystem mehrerer Anlagen eines Unternehmens zu verstehen sei, überwacht
und optimiert werden könne. Bei einem derartigen Verbund seien bspw. die einzelnen Ströme zwischen den Anlagen miteinander verknüpft und erstrecken sich
über mehrere Hierarchieebenen. Damit sei eine Überwachung bis auf die Unternehmensebene, d. h. die oberste Hierarchieebene, möglich, da keine Steuerung
der einzelnen Anlage betrachtet werde, sondern die Entwicklung aller Ströme aller
Anlagen über die Zeit.


Zur Beurteilung der erfinderischen Tätigkeit wendet der Vertreter der Anmelderin
ein, dass aus der D1 keine Überwachung bzw. Steuerung einer Anlage, sondern
nur ein reines Simulationssystem zu entnehmen sei. Insbesondere sei keine zwingende Erfassung der Messwerte aus der Anlage gezeigt und auch die angegebene Block-Struktur sei nicht offenbart.


Dies kann jedoch keine erfinderische Tätigkeit begründen, da in D1 ein Modellieren (Abbilden) und Simulieren einer Anlage beschrieben ist, um bspw. die Arbeitsweise eines Elements auf einer Anzeige für den Operator darzustellen und somit
eine Überwachung der Anlage zu ermöglichen (Absätze [0010], [0011]). Ebenso
ist ausgeführt, dass reale Daten oder Werte für die Berechnungen in den Prozessmodulen verwendet werden, wodurch die Steuerungsmodule im Online- bzw.
Steuerungsbetrieb oder in einer Simulation verwendet werden (Absätze [0049],
[0108]). Weiterhin ist die Abbildung von Elementen auf Blöcke in Steuerungsmodulen, welche eine Hierarchie aufweisen und in Klassenbibliotheken eingeordnet
sind, beschrieben (Absätze [0026], [0041], [0086]).


Der Vertreter der Anmelderin wendet außerdem ein, dass aus der D1 keine Aggregation im Sinne der Anmeldung zu entnehmen sei. Dabei ist gemäß der Anmeldung unter der Bezeichnung „Aggregation“ im Wesentlichen eine Zusammenfassung von Messwerten für die Ein- und Ausgänge (z. B. Summierung, Mittelwert-

                                      - 34 -



bildung) zu verstehen (vgl. Offenlegungsschrift Absätze [0075] ff., insbes. Absätze
[0076] und [0077] und Merkmal (f)).


Die beanspruchte Aggregation erfolgt in D1 z. B. über die Summierung der Messgrößen des jeweiligen Massenstroms (s. Offenlegungsschrift Absätze [0075] ff.).
Dass dies für den Fachmann nahelag, wurde bereits oben unter 2.1 erläutert.


Darüber hinaus macht der Vertreter der Anmelderin geltend, dass aus der D1 nur
die Simulation einer Einzelprozessanlage zu entnehmen sei, bei der die Betrachtung der Ströme außerhalb dieser Anlage fehle. Somit sei aus der Druckschrift
keine Aggregation und auch keine Erfassung von Strömen über Hierarchieebenen
und über mehrere Anlagen von Verbundsystemen hinweg zu entnehmen.


Auch dieser Argumentation kann nicht gefolgt werden, da in D1 (Absatz [0088],
Fig. 5, Fig. 6) die Abschnitte einer gesamten Prozessanlage gezeigt sind, die mehrere Einheiten mit Untereinheiten umfasst, wie es der jeweilige Anspruch 1 des
Hauptantrags und der Hilfsanträge erfordert. Dass dabei mehrere, etwa räumlich
über ein großes Gebiet verteilte Einzelanlagen zu einem Verbundsystem zusammengefasst und gemeinsam überwacht werden sollen, verlangt der jeweilige Anspruch 1 nicht.


2.7.   Da sich der Gegenstand der Hauptansprüche aller Anträge in naheliegender Weise aus dem Stand der Technik ergibt, erübrigt es sich darauf einzugehen,
ob das Verfahren gemäß § 1 Abs. (3) und (4) PatG vom Patentschutz ausgeschlossen ist, oder ob zumindest ein Teil der in diesen Ansprüchen aufgeführten
Merkmale nicht zur Lösung eines technischen Problems mit technischen Mitteln
beiträgt.

                                            - 35 -



3.      Ebenso wie der jeweilige Anspruch 1 nach Hauptantrag und nach den Hilfsanträgen 1 bis 4 sind auch die weiteren Ansprüche 2 bis 16 nach Hauptantrag, 2
bis 15 nach erstem Hilfsantrag, 2 bis 12 nach zweitem Hilfsantrag, 2 bis 14 nach
drittem Hilfsantrag und 2 bis 13 nach viertem Hilfsantrag nicht gewährbar, da über
einen Antrag nur einheitlich entschieden werden kann (BGH GRUR 1997, 120
– Elektrisches Speicherheizgerät).




Rechtsmittelbelehrung


Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass


     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit
        Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
        sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
        zugestimmt hat,
     5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
        Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
     6. der Beschluss nicht mit Gründen versehen ist.

                                         - 36 -



Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                 Eder             Dr. Thum-Rung                   Hoffmann




                                                                                   Fa
