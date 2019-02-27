---
ecli: "ECLI:DE:BPatG:2019:270219U6Ni27.17EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 27/17"
decided: "2019-02-27"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2019&Sort=1&Seite=9&nr=34575&anz=817&pos=140&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2019-02-27_6_Ni_27_17_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0083.md", "germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0263.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 27/17 vom 2019-02-27

## Entscheidung

BUNDESPATENTGERICHT

                     IM NAMEN DES VOLKES

                               URTEIL
                                                       Verkündet am
                                                      27. Februar 2019
6 Ni 27/17 (EP)                                              …

(Aktenzeichen)


                     In der Patentnichtigkeitssache



 …




 ECLI:DE:BPatG:2019:270219U6Ni27.17EP.0

                                       -2-



                 betreffend das europäische Patent 2 538 320
                              (DE 50 2011 005 524)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 27. Februar 2019 unter Mitwirkung der Vorsitzenden Richterin Friehe und der Richter Dipl.-Phys. Dr. Schwengelbeck, Jacobi, der
Richterin Dipl.-Phys. Dr. Otten-Dünnweber sowie des Richters Dipl.-Ing. Altvater




für Recht erkannt:


        1.   Das Europäische Patent 2 538 320 wird im Umfang der Ansprüche 1, 2, 6 sowie 11 bis 14 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland für nichtig erklärt.


        2.   Die Kosten des Verfahrens trägt die Beklagte.


        3.   Das Urteil ist vorläufig vollstreckbar gegen Sicherheitsleistung in Höhe von 110 % des jeweils zu vollstreckenden Betrages.




                                  I. Tatbestand


Die Beklagte ist Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 2 538 320 (Streitpatent).
Das am 22. Juni 2011 angemeldete Streitpatent ist in Kraft und wird beim Deutschen Patent- und Markenamt unter dem Aktenzeichen 50 2011 005 524 geführt
und trägt die Bezeichnung

                                       -3-



 „Verfahren und System zur Unterstützung einer Bedienung eines Computerprogramms“


und umfasst in der erteilten Fassung 14 Patentansprüche, die mit der am
16. August 2017 eingereichten Nichtigkeitsklage im Umfang der Patentansprüche 1, 2, 6 sowie 11 bis 14 angegriffen werden.


Die erteilten nebengeordneten Patentansprüche 1, 13 und 14 lauten wie folgt:


      1. Computer-implementiertes Verfahren zur Unterstützung eines Benutzers während einer Bedienung zumindest eines vorbestimmten Computerprogramms, wobei während der Ausführung des Computerprogramms zumindest ein Benutzeroberflächenobjekt des Computerprogramms auf einer Anzeigeeinrichtung zur Anzeige gebracht wird, wobei
          die Bedienung des Computerprogramms eine Anzahl auszuführender
          Prozessschritte umfasst, wobei jeder Prozessschritt durch eine vorbestimmte Benutzerinteraktion mit einem vorbestimmten Benutzeroberflächenobjekt (BOO) in einem vorbestimmten Kontext des Computerprogramms repräsentiert wird, wobei eine Navigationsdatei die für die
          Bedienung des Computerprogramms erforderlichen Benutzerinteraktionen mit dem Computerprogramm enthält, wobei die Benutzerinteraktionen als Prozessschritte in der Navigationsdatei gespeichert sind, und
          wobei für zumindest einen in der Navigationsdatei gespeicherten Prozessschritt


               - der zumindest eine gespeicherte Prozessschritt geladen wird
               (S0; S9),
               - der aktuelle Kontext des Computerprogramms ermittelt wird (S1),
               - geprüft wird, ob der aktuelle Kontext des Computerprogramms
               mit dem Kontext des geladenen Prozessschrittes übereinstimmt
               (S2),

                            -4-



     - falls der aktuelle Kontext des Computerprogramms mit dem
     Kontext des geladenen Prozessschrittes übereinstimmt, das an
     der Anzeigeeinrichtung angezeigte Benutzeroberflächenobjekt des
     Computerprogramms ermittelt wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen Prozessschrittes entspricht
     (S4), und
     - das ermittelte Benutzeroberflächenobjekt (BOO) des Computerprogramms auf der Anzeigeeinrichtung für den Benutzer hervorgehoben wird (S6),


dadurch gekennzeichnet, dass eine Benutzerinteraktion entgegengenommen wird und die entgegengenommene Benutzerinteraktion anhand von Regeln, welche der Benutzerinteraktion des geladenen Prozessschrittes zugeordnet sind, validiert wird (S7), wobei das Entgegennehmen und Validieren (S7) der Benutzerinteraktion zumindest folgende Schritte umfasst:


     - Erzeugen eines Systemhooks zum Abfangen von Benutzeingaben, bevor diese an das Computerprogramm weitergegeben werden (S7.1),
     - für jede Benutzeingabe, welche von dem Systemhook abgefangen wird


       - Überprüfen, ob der Aktionstyp der Benutzereingabe dem Aktionstyp des geladenen Prozessschrittes entspricht (S7.2),
       - sofern die Aktionstypen einander entsprechen, Validieren der
       Benutzereingabe (S7.3), wobei bei der Validierung der Benutzereingabe unterschieden wird zwischen einer Zeiger basierten
       Benutzereingabe und einer Tastatur basierten Benutzereingabe, wobei

                                        -5-



                      - bei einer Zeiger basierten Benutzereingabe überprüft wird,
                      ob die Eingabe von dem Benutzeroberflächenobjekt (BOO)
                      des    geladenen    Prozessschrittes   entgegengenommen
                      wurde (S7.3.1),
                      - bei einer Tastatur basierten Benutzereingabe überprüft
                      wird, ob der eingegebene Wert den dem geladenen Prozessschritt   zugeordneten    Eingabevorgaben     entspricht
                      (S7.3.2).


      13. System zur Unterstützung eines Benutzers während einer Bedienung
          zumindest eines vorbestimmten Computerprogramms, wobei das System Mittel zum Ausführen des Computerprogramms, eine Anzeigeeinrichtung zur Anzeige des sich in Ausführung befindlichen Computerprogramms, Eingabemittel zur Entgegennahme von Benutzereingaben,
          und Navigationsmittel, welche angepasst sind, ein Verfahren nach einem der vorhergehenden Ansprüche auszuführen, umfasst, wobei die
          Navigationsmittel über zumindest eine Objekterkennungsschnittstelle
          mit dem Computerprogramm koppelbar sind, um das Computerprogramm entsprechend der in der Navigationsdatei gespeicherten Prozessschritte zu überwachen und zu steuern.


      14. Computerprogrammprodukt mit Programmcode, welcher, wenn in eine
          Datenverarbeitungsanlage geladen, das Verfahren gemäß einem der
          Ansprüche 1 bis 12 zur Ausführung bringt.


Hintergrund der Nichtigkeitsklage ist ein zwischen den Parteien vor dem Landgericht Mannheim (Az 2 O 97/17) anhängiger Rechtsstreit.


Die Klägerin hat ursprünglich lediglich geltend gemacht, das Streitpatent sei wegen des Nichtigkeitsgrunds der mangelnden Patentfähigkeit für nichtig zu erklären.

                                           -6-



Dies stützt sie unter anderem auf die Druckschriften (Nummerierung und Kurzzeichen nach Klageschriftsatz):


D1                 Apple Computer Inc.: „Apple Guide Complete: Designing and Developing Onscreen Assistance“; Addison-Wesley, Februar 1995
D2                 US 5,535,422 A
D3                 WO 2006/029124 A2
D4                 US 6,307,544 B1



und die Softwareprodukte „i-net Designer“, „KNAppGuide“, „Guider JS“ umfassend
„jQuery“,      „tour.js“   sowie   „optimizely.appspot.com“.   Mit   Schriftsatz   vom
18. Januar 2019 macht sie weitergehend den Nichtigkeitsgrund der unzulässigen
Erweiterung geltend. Ferner argumentiert sie, hinsichtlich der Ansprüche 1, 2, 6,
11 und 12 sei eine Patentierbarkeit nach Art. 52 Abs. 2 und 3 EPÜ ausgeschlossen.


Die Klägerin beantragt,


        das europäische Patent 2 538 320 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland im Umfang der Ansprüche 1,
        2, 6 sowie 11 bis 14 für nichtig zu erklären.


Die Beklagte beantragt,


        die Klage abzuweisen,


        hilfsweise die Klage abzuweisen, soweit sie sich auch gegen eine
        der Fassungen des Streitpatents nach einem der 27 Hilfsanträge 0
        bis VIII c gemäß der dem Protokoll anliegenden Aufstellung richtet.


Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den Gegenstand des Streitpatents in der erteilten Fassung oder wenigstens in einer der

                                          -7-



verteidigten Fassungen für schutzfähig. Die Berufung der Klägerin auf den Nichtigkeitsgrund der unzulässigen Erweiterung rügt sie als verspätet.


Die 27 Hilfsanträge, aufgeführt in der beantragten Reihenfolge, haben folgenden
Inhalt:


   -      Hilfsantrag 0 ist der Hauptantrag „mit Fußnote“:

                                   -8-



-   Hilfsantrag I vom 18. Januar 2019 lautet:

-9-

- 10 -

- 11 -

- 12 -

- 13 -

                                  - 14 -




-   Hilfsantrag II vom 18. Januar 2019 lautet in den Patentansprüchen 2 bis
    13 wie Hilfsantrag I vom 18. Januar 2019; Patentanspruch 1 hat folgenden
    Wortlaut:

- 15 -

- 16 -

                                  - 17 -



-   Hilfsantrag III vom 18. Januar 2019 lautet in den Patentansprüchen 2 bis
    13 wie Hilfsantrag I vom 18. Januar 2019; Patentanspruch 1 hat folgenden
    Wortlaut:

- 18 -

                                  - 19 -




-   Hilfsantrag IV vom 18. Januar 2019 lautet in den Patentansprüchen 2 bis
    13 wie Hilfsantrag I vom 18. Januar 2019; Patentanspruch 1 hat folgenden
    Wortlaut:

- 20 -

                                 - 21 -




-   Hilfsantrag V vom 18. Januar 2019 entspricht in seinen Patentansprüchen 2 bis 14 dem erteilten Patent und hat in Patentanspruch 1 diesen
    Wortlaut:

- 22 -

                                  - 23 -




-   Hilfsantrag VI vom 18. Januar 2019 lautet in den Patentansprüchen 2 bis
    13 wie Hilfsantrag I vom 18. Januar 2019; Patentanspruch 1 hat den Wortlaut:

- 24 -

- 25 -

                                   - 26 -




-   Hilfsantrag VII vom 18. Januar 2019 entspricht in seinen Patentansprüchen 2 bis 10 dem erteilten Patent, Patentanspruch 11 entspricht dem erteilten Anspruch 13 und Patentanspruch 12 entspricht dem erteilten Anspruch 14 unter angepasstem Rückbezug auf die Ansprüche 1 bis 10; Patentanspruch 1 hat diesen Wortlaut:

- 27 -

- 28 -

                                 - 29 -




-   Hilfsantrag VIII vom 18. Januar 2019 entspricht in seinen Ansprüchen 2
    bis 12 dem Hilfsantrag VII vom 18. Januar 2019 und hat in Patentanspruch 1 den Wortlaut:

- 30 -

- 31 -

                                   - 32 -




-   Hilfsantrag I vom 27. Februar 2019
    entspricht Hilfsantrag I vom 18. Januar 2019 ohne die Unteransprüche 3 bis
    5 sowie 7 bis 10.


-   Hilfsantrag Ia vom 27. Februar 2019
    entspricht Hilfsantrag I vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.

                                   - 33 -



-   Hilfsantrag II vom 27. Februar 2019
    entspricht Hilfsantrag II vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag IIa vom 27. Februar 2019
    entspricht Hilfsantrag II vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.


-   Hilfsantrag III vom 27. Februar 2019
    entspricht Hilfsantrag III vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag IIIa vom 27. Februar 2019
    entspricht Hilfsantrag III vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.


-   Hilfsantrag IV vom 27. Februar 2019
    entspricht Hilfsantrag IV vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag IVa vom 27. Februar 2019
    entspricht Hilfsantrag IV vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.


-   Hilfsantrag V vom 27. Februar 2019
    entspricht Hilfsantrag V vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag Va vom 27. Februar 2019
    entspricht Hilfsantrag V vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.

                                   - 34 -



-   Hilfsantrag VI vom 27. Februar 2019
    entspricht Hilfsantrag VI vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag VIa vom 27. Februar 2019
    entspricht Hilfsantrag VI vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.


-   Hilfsantrag VII vom 27. Februar 2019
    entspricht Hilfsantrag VII vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag VIIa vom 27. Februar 2019
    entspricht Hilfsantrag VII vom 27. Februar 2019 „mit Fußnote“ entsprechend
    Hilfsantrag 0.


-   Hilfsantrag VIII vom 27. Februar 2019
    entspricht Hilfsantrag VIII vom 18. Januar 2019 ohne die Unteransprüche 3
    bis 5 sowie 7 bis 10.


-   Hilfsantrag VIIIb vom 27. Februar 2019
    entspricht Hilfsantrag VIII vom 27. Februar 2019 „mit Fußnote“ entsprechend Hilfsantrag 0.


-   Hilfsantrag VIIIa vom 27. Februar 2019
    entspricht in seinen Unteransprüchen den Unteransprüchen des Hilfsantrags VII vom 18. Januar 2019 ohne die Unteransprüche 3 bis 5 und 7 bis
    10; Patentanspruch 1 hat folgenden Wortlaut:

- 35 -

- 36 -

                                       - 37 -




   -   Hilfsantrag VIIIc vom 27. Februar 2019
       entspricht Hilfsantrag VIIIa vom 27. Februar 2019 „mit Fußnote“ entsprechend Hilfsantrag 0.


Die Klägerin hält die Hilfsanträge bereits für unzulässig, soweit sie auch die nicht
angegriffenen Unteransprüche 3 bis 5 sowie 7 bis 10 enthalten. Jeder der nicht
angegriffenen Ansprüche sei direkt oder indirekt auf Anspruch 1 zurückbezogen,
der jeweils geändert werde. Aufgrund des Rückbezugs würden damit auch die
nicht angegriffenen Ansprüche geändert. Dies sei jedoch angesichts der gefestigten Rechtsprechung des Bundesgerichtshofs nicht zulässig. Nach dieser Recht-

                                       - 38 -



sprechung dürften Unteransprüche, die nicht im Streit stünden, im Nichtigkeitsverfahren auch im Weg der Selbstbeschränkung nicht geändert werden.


Der Senat hat den Parteien einen qualifizierten Hinweis vom 17. Dezember 2018
zugeleitet, auf den Bezug genommen wird.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                            II. Entscheidungsgründe


Die zulässige Klage ist begründet. Das Streitpatent ist für nichtig zu erklären, weil
ihm in sämtlichen Anspruchsfassungen der Nichtigkeitsgrund der mangelnden
Patentfähigkeit entgegensteht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138
Abs. 1 Buchst. a), Art. 52 bis 57 EPÜ). Die erteilte Fassung ist im Übrigen auch
wegen unzulässiger Erweiterung (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m. Art. 138
Abs. 1 Buchst. c) EPÜ) für nichtig zu erklären.




                                         A.


                   I.     Zum Gegenstand des Streitpatents
1.    Die Erfindung betrifft ausweislich Absatz 0001 der Streitpatentschrift
(EP 2 538 320 B1) ein Verfahren und ein System zur Unterstützung eines
Benutzers    während     einer   Bedienung        zumindest   eines   vorbestimmten
Computerprogramms, wobei während der Ausführung des Computerprogramms
zumindest ein Benutzeroberflächenobjekt des Computerprogramms auf einer
Anzeigeeinrichtung zur Anzeige gebracht wird und wobei die Bedienung des
Computerprogramms eine Anzahl auszuführender Prozessschritte umfasst.


Zum technischen Hintergrund der Erfindung führt die Streitpatentschrift in den
Absätzen 0002 bis 0005 u. a. Folgendes aus:

                                              - 39 -



Zur Unterstützung eines Benutzers während der Bedienung eines Computerprogramms oder zum Erlernen eines Computerprogramms sei es bekannt, dem
Benutzer ein Handbuch zur Verfügung zu stellen. Das Handbuch könne als
gedrucktes Handbuch oder als elektronisches Handbuch, etwa in Form einer in
dem Computerprogramm integrierten Hilfe bereitgestellt werden. Elektronische
Handbücher hätten dabei den Vorteil, dass bei Anforderung der Hilfe, etwa durch
Drücken einer Taste, das Computerprogramm automatisch den Hilfetext aus dem
elektronischen      Handbuch        zur     Anzeige     bringen     könne,     welcher    dem
Programmkontext, in dem sich das Computerprogramm befinde, zugeordnet sei.
Von Nachteil sei dabei, dass bei jedem Wechsel des Programmkontextes, etwa
wenn eine neue Bildschirmmaske aufgerufen werde, die Hilfe durch den Benutzer
erneut angefordert werden müsse, um den korrekten Hilfetext zur Anzeige zu
bringen. Auch sei eine interaktive Benutzerführung durch das Computerprogramm
nicht möglich.


Zur Unterstützung einer Benutzerführung durch ein Computerprogramm sei es
ferner      bekannt,      während       der    Bedienung      des      Computerprogramms
Bildschirmobjekte, sogenannte Benutzeroberflächenobjekte, hervorzuheben, um
dem Benutzer zu signalisieren, mit welchem Benutzeroberflächenobjekt eine
Interaktion zu erfolgen habe. Die Unterstützung könne auch in diesem Fall etwa
durch     Drücken      einer    Taste     angefordert   werden.     Das      hervorzuhebende
Benutzeroberflächenobjekt werde anhand vorbestimmter Bezugsmerkmale, etwa
die Position des Benutzeroberflächenobjektes in der Bildschirmmaske und/oder
die      Position   des        Benutzeroberflächenobjektes,       in      einer   Liste   von
Benutzeroberflächenobjekten lokalisiert.


Diese Form der Unterstützung habe allerdings den Nachteil, dass ein
entsprechendes Benutzeroberflächenobjekt nur dann korrekt hervorgehoben
werden könne, wenn sich die Bezugsmerkmale nicht änderten. Ändere sich
beispielsweise die Reihenfolge der Benutzeroberflächenobjekte in der Liste von
Benutzeroberflächenobjekten, wenn etwa das Computerprogramm von einem
Entwicklungssystem auf ein Produktivsystem portiert werde, könne dies dazu

                                        - 40 -



führen, dass ein falsches Benutzeroberflächenobjekt aus der Liste ausgewählt und
hervorgehoben     werde,    was     wiederum     zu   einer      Fehlbedienung     des
Computerprogramms durch den Benutzer führen könne. Ein weiterer Nachteil
bestehe darin, dass diese Art der Benutzerführung nicht kontextübergreifend
funktioniere, sodass der Benutzer bei jedem Wechsel des Kontextes des
Computerprogramms, etwa beim Wechsel von einer Eingabemaske zur nächsten
Eingabemaske, die Unterstützung erneut anfordern müsse.


Das Streitpatent definiert als Aufgabe (vgl. Streitpatent, Abs. 0006), ein Verfahren
und ein System zur Unterstützung eines Benutzers während einer Bedienung
eines Computerprogramms bereitzustellen, welche es erlauben, während der
Ausführung       des       Computerprogramms          kontextübergreifend          ein
Benutzeroberflächenobjekt     des   Computerprogramms         entsprechend       einem
vorbestimmten Programmablauf auch bei sich ändernden Bezugsmerkmalen des
Benutzeroberflächenobjektes auf einer Anzeigeeinrichtung hervorzuheben und die
Unterstützung auch während der Ausführung des Computerprogramms erst
anzufordern.


Der für die Lösung der Aufgabe zuständige Fachmann ist ein Ingenieur der
Informationstechnik mit Hochschulabschluss, der als Systementwickler oder
Programmierer über Berufserfahrung in der Entwicklung von Hilfesystemen
verfügt.




2.     Die Aufgabe soll erfindungsgemäß durch ein Verfahren und ein System zur
Unterstützung     eines     Benutzers     während     einer       Bedienung      eines
Computerprogramms gemäß den unabhängigen Ansprüchen gelöst werden (Abs.
0007 der Streitpatentschrift). Patentanspruch 1 in der Fassung des Hauptantrags
(erteilter Anspruch 1) kann dabei wie folgt gegliedert werden:


           1.1    Computer-implementiertes Verfahren zur Unterstützung eines
                  Benutzers während einer Bedienung zumindest eines vorbe-

                           - 41 -



        stimmten Computerprogramms,

1.1.1   wobei während der Ausführung des Computerprogramms zumindest ein Benutzeroberflächenobjekt des Computerprogramms auf einer Anzeigeeinrichtung zur Anzeige gebracht
        wird,

1.1.2   wobei die Bedienung des Computerprogramms eine Anzahl
        auszuführender Prozessschritte umfasst,

1.1.3   wobei jeder Prozessschritt durch eine vorbestimmte Benutzerinteraktion mit einem vorbestimmten Benutzeroberflächenobjekt
        (BOO) in einem vorbestimmten Kontext des Computerprogramms repräsentiert wird,

1.1.4   wobei eine Navigationsdatei die für die Bedienung des Computerprogramms erforderlichen Benutzerinteraktionen mit dem
        Computerprogramm enthält,

1.1.5   wobei die Benutzerinteraktionen als Prozessschritte in der Navigationsdatei gespeichert sind, und

1.2     wobei für zumindest einen in der Navigationsdatei gespeicherten Prozessschritt

1.2.1   - der zumindest eine gespeicherte Prozessschritt geladen wird
        (S0; S9),

1.2.2   - der aktuelle Kontext des Computerprogramms ermittelt wird
        (S1),

1.2.3   - geprüft wird, ob der aktuelle Kontext des Computerprogramms
        mit dem Kontext des geladenen Prozessschrittes übereinstimmt
        (S2),

1.2.4   - falls der aktuelle Kontext des Computerprogramms mit dem
        Kontext des geladenen Prozessschrittes übereinstimmt, das an
        der Anzeigeeinrichtung angezeigte Benutzeroberflächenobjekt
        des Computerprogramms ermittelt wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen Prozessschrittes
        entspricht (S4), und

1.2.5   - das ermittelte Benutzeroberflächenobjekt (BOO) des Computerprogramms auf der Anzeigeeinrichtung für den Benutzer hervorgehoben wird (S6),

        dadurch gekennzeichnet, dass

1.3     eine Benutzerinteraktion entgegengenommen wird und die entgegengenommene Benutzerinteraktion anhand von Regeln,

                                     - 42 -



                 welche der Benutzerinteraktion des geladenen Prozessschrittes
                 zugeordnet sind, validiert wird (S7), wobei das Entgegennehmen und Validieren (S7) der Benutzerinteraktion zumindest folgende Schritte umfasst:

        1.3.1    - Erzeugen eines Systemhooks zum Abfangen von Benutzeingaben, bevor diese an das Computerprogramm weitergegeben
                 werden (S7.1),

        1.3.2    - für jede Benutzeingabe, welche von dem Systemhook abgefangen wird,
                 - Überprüfen, ob der Aktionstyp der Benutzereingabe dem Aktionstyp des geladenen Prozessschrittes entspricht (S7.2),

        1.3.3    - sofern die Aktionstypen einander entsprechen, Validieren der
                 Benutzereingabe (S7.3), wobei bei der Validierung der Benutzereingabe unterschieden wird zwischen einer Zeiger basierten
                 Benutzereingabe und einer Tastatur basierten Benutzereingabe,
                 wobei

        1.3.4    - bei einer Zeiger basierten Benutzereingabe überprüft wird, ob
                 die Eingabe von dem Benutzeroberflächenobjekt (BOO) des
                 geladenen     Prozessschrittes   entgegengenommen        wurde
                 (S7.3.1),

        1.3.5    - bei einer Tastatur basierten Benutzereingabe überprüft wird,
                 ob der eingegebene Wert den dem geladenen Prozessschritt
                 zugeordneten Eingabevorgaben entspricht (S7.3.2).


3.    Einige Merkmale bedürfen näherer Erläuterung.


Patentanspruch 1 ist auf ein computer-implementiertes Verfahren gerichtet, das
gemäß der in Merkmal 1.1 gemachten Zweckangabe zur Unterstützung eines
Benutzers   während     einer   Bedienung     zumindest   eines   vorbestimmten
Computerprogramms geeignet sein soll. Als Unterstützung ist dabei jegliche
Hilfestellung, welche dem Benutzer in Form einer Information angeboten wird (vgl.
Streitpatent, Abs. 0002 - 0004), anzusehen. In Merkmal 1.1.1 wird als ein Schritt
des Verfahrens gefordert, dass während der Benutzung des Computerprogramms
ein Benutzeroberflächenobjekt (BOO), also etwa ein Eingabefeld in einer Maske
des Computerprogramms, eine Schaltfläche, eine Checkbox oder eine Tabelle
(vgl. Streitpatent, Abs. 0030) auf der Anzeige erscheint. Die folgenden Merkmale
1.1.2 und 1.1.3 definieren Eigenschaften des Computerprogramms, dessen

                                                 - 43 -



Bedienung auszuführende Prozessschritte umfasst, welche durch eine bestimmte
Benutzerinteraktion mit einem bestimmten Benutzeroberflächenobjekt in einem
bestimmten Kontext des Programms repräsentiert werden. Diese Merkmale
schränken das beanspruchte Verfahren nur insoweit ein, dass es geeignet ist, eine
Unterstützung für solcherart ausgestaltete Computerprogramme zu bieten, also für
Programme            mit     Benutzeroberflächenobjekten,           d. h.      etwa   mit   grafischen
Bedienoberflächen. Die Merkmale 1.1.4 und 1.1.5 beschreiben keine Schritte des
mit      Anspruch 1              beanspruchten    Verfahrens,           sondern       betreffen   eine
Navigationsdatei, in der die für die Bedienung des Programms erforderlichen
Benutzerinteraktionen als Prozessschritte abgespeichert sind. In Verbindung mit
Merkmal 1.1.3 legt die Navigationsdatei für jeden Prozessschritt des Programms
fest,       wie            die       Benutzerinteraktion          mit       dem        vorbestimmten
Benutzeroberflächenobjekt in einem vorbestimmten Kontext auszusehen hat. Die
Beschreibung führt hierzu aus, dass ein Prozessschritt durch das Tripel
Anwendungskontext,                  Benutzeroberflächenobjekt            und      Benutzerinteraktion
repräsentiert ist (vgl. Streitpatent, Abs. 0062).


Die Merkmalsgruppe 1.2 definiert mehrere Verfahrensschritte, wobei zunächst aus
der Navigationsdatei ein dort gespeicherter Prozessschritt geladen wird (Merkmal
1.2.1). Dann wird der aktuelle Kontext des Computerprogramms ermittelt, wobei
als Kontext eine vorbestimmte Benutzeroberfläche des Programms in einem
vorbestimmten Zustand bezeichnet wird, d. h. das aktuell aktive Fenster oder die
aktuell aktive Eingabemaske (Merkmal 1.2.2 / vgl. Abs. 0032 des Streitpatents).
Merkmal 1.2.3 fordert, dass geprüft wird, ob der aktuelle Kontext – also bspw. das
aktuell aktive Fenster des Programms – mit dem Kontext des in Merkmal 1.2.1
aufgeführten, aus der Navigationsdatei geladenen Prozessschritts übereinstimmt.
Für den Fall, dass diese Überprüfung „ja“ ergibt, erfolgt das in den Merkmalen
1.2.4 und 1.2.5 Aufgeführte: Für den geladenen Prozessschritt wird dabei ermittelt,
welches der angezeigten Benutzeroberflächenobjekte diesem entspricht und das
so      ermittelte     Benutzeroberflächenobjekt           wird    auf      der   Anzeigeeinrichtung
hervorgehoben, etwa durch eine Änderung der Helligkeit des Objekts im Vergleich
zum sonstigen Bildschirmhintergrund („highlighten“).

                                        - 44 -



Die den kennzeichnenden Teil von Anspruch 1 bildende Merkmalsgruppe 1.3
beschreibt, wie das Verfahren auf eine entgegengenommene Benutzerinteraktion
reagieren soll. Erzeugt wird ein Systemhook, der Benutzereingaben [korr.: im
Anspruchswortlaut: Benutzeingaben] abfängt, bevor diese an das Programm
weitergegeben     werden      (vgl.   Merkmal    1.3.1).   Für   jede    abgefangene
Benutzereingabe wird dann überprüft, ob der Aktionstyp dem Aktionstyp des
geladenen Prozessschritts entspricht; falls die Überprüfung eine Entsprechung
bestätigt („ja“), soll die Benutzereingabe validiert werden (Merkmale 1.3.2, 1.3.3),
wobei nach Zeiger und Tastatur basierten Eingaben unterschieden wird. Die
Merkmale 1.3.4 und 1.3.5 geben an, dass im Zuge der Validierung überprüft wird,
ob die Eingabe oder der eingegebene Wert von dem Benutzeroberflächenobjekt
des geladenen Prozessschritts entgegen genommen wurde bzw. dem dem
geladenen    Prozessschritt      zugeordneten     Wert     entspricht.   Mit   diesen
Validierungsschritten endet das Verfahren des Anspruchs 1.


Der Anspruch 1 umfasst somit von dem in der Figur 1 des Streitpatents
dargestellten Verfahrensablauf die Schritte S0, S1, S2, S4, S6 und S7, die Schritte
SYN, S3 und S5, S8, S9 hingegen sind nicht Gegenstand des Anspruchs 1.

                                      - 45 -




Der Anspruch 1 macht keine Angaben dazu, was nach dem Validieren der
abgefangenen    Benutzereingabe     passiert,   und   macht   –   entgegen   den
Ausführungen der Beklagten – auch keine Angaben dazu, die weitere Bedienung
des Programms solange zu unterbinden, bis eine korrekte Eingabe oder Aktion
erfolgt, oder dazu, wie sichergestellt werden kann, dass der Benutzer auf falsche
Eingaben hingewiesen wird. Ebenso macht der Anspruch keine Aussage darüber,
welche Schritte vorgenommen werden, wenn bei der in Merkmal 1.2.3 erfolgten
Prüfung festgestellt wird, dass der aktuelle Kontext des Programms nicht mit dem
Kontext des geladenen Prozessschritt übereinstimmt, da im erteilten Anspruch 1
eine Synchronisierung für den Fall, dass die in Merkmal 1.2.3 vorgenommene

                                        - 46 -



Überprüfung keine Übereinstimmung ergibt, nicht vorgesehen ist. Eine solche
Synchronisierung ist zwar in dem in der vorstehend wiedergegebenen Figur 1 des
Streitpatents dargestellten Ablauf aufgeführt (vgl. Block SYN, sowie Fig. 2 u.
Abs. 0041), wird aber erst im erteilten Unteranspruch 3 gefordert. Durch das mit
dem erteilten Anspruch 1 beanspruchte Verfahren wird somit entgegen den
Ausführungen    der   Beklagten   nicht    automatisch   sichergestellt,   dass   die
Unterstützung der Bedienung des Computerprogramms an jeder Stelle des
Workflows angefordert und auch geleistet werden kann, zumal eine solche
Anforderung nicht Gegenstand des Anspruchs ist. Der Senat vermag auch den
Ausführungen der Beklagten, der Workflow eines entsprechend unterstützten
Computerprogramms werde immer von Anfang bis Ende durchgeführt, nicht zu
folgen, da sich im Anspruch im Unterschied zu Figur 1 keinerlei Angaben zu einem
Ablaufschema mit mehreren, ggf. iterativ zu durchlaufenden Verfahrensschritten
eines mehrschrittigen Workflows finden lassen. Insbesondere ist Anspruch 1 nicht
zu entnehmen, dass ein weiterer Prozessschritt geladen wird. Unter den Anspruch
fallen vielmehr auch Verfahren, welche die in den Merkmalsgruppen 1.2 und 1.3
aufgeführten Verfahrensschritte nur einmal für einen einzigen, nach Merkmal 1.2.1
geladenen Prozessschritt durchlaufen.


Die Verfahrensschritte der Merkmalsgruppe 1.3 geben einen Ablauf nach Figur 9
des Streitpatents wieder.


In Anspruch 1 betreffen die Merkmale 1.1, 1.1.1 teilweise, 1.1.2 und 1.1.3 das
Computerprogramm, während dessen Bedienung eine Unterstützung angeboten
werden soll; die Merkmale 1.1.4 und 1.1.5 charakterisieren die Navigationsdatei.
Die das Verfahren charakterisierenden Merkmalsgruppen 1.2 und 1.3 sind durch
den Begriff eines geladenen Prozessschrittes und das dazu zu ermittelnde
Benutzeroberflächenobjekt zueinander in Beziehung gesetzt, welche auch eine
gewisse zeitliche Aufeinanderfolge beinhaltet (vgl. Merkmale 1.2.4 i. V. m. 1.2.5,
1.3.2, 1.3.4); darüber hinaus sind die Verfahrensschritte innerhalb der jeweiligen
Merkmalsgruppen 1.2 und 1.3 so zu verstehen, dass die angegebene Abfolge – im

                                       - 47 -



Sinne der Ablaufdiagramme der Figuren 1 und 9 – auch einen zeitlichen Ablauf
beinhaltet.


Die von der Erfindung gelöste objektive Aufgabe besteht somit darin, ein
Verfahren und ein System zur Unterstützung eines Benutzers während einer
Bedienung eines Computerprogramms bereitzustellen, welche es erlauben,
während der Ausführung des Computerprogramms ein Benutzeroberflächenobjekt
des Computerprogramms entsprechend einem vorbestimmten Programmablauf
bei übereinstimmendem Kontext auf einer Anzeigeeinrichtung hervorzuheben und
Benutzerinteraktionen, bevor sie an ein Computerprogramm weitergegeben
werden, zu validieren.


                             II.    Zum Hauptantrag


In der erteilten Fassung ist das Streitpatent sowohl wegen fehlender Patentfähigkeit (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a) EPÜ),
ausgehend vom Stand der Technik nach den Entgegenhaltungen D3 und D4, als
auch wegen unzulässiger Erweiterung (Art. II § 6 Abs. 1 Nr. 3 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. c) EPÜ) für nichtig zu erklären.


1.     Der Gegenstand des Anspruchs 1 nach Hauptantrag gilt gegenüber den
Druckschriften D3 und D4 als nicht auf einer erfinderischen Tätigkeit beruhend
(Art. 56 EPÜ).


Druckschrift D3 (WO 2006/029124 A2) betrifft Systeme und Verfahren zur
Unterrichtung eines Benutzers, der mit einem Computerprogramm mit einer
graphischen Benutzeroberfläche interagiert (vgl. Title und Abstract). Offenbart wird
dabei ein Verfahren zur Unterstützung eines Benutzers während der Bedienung
eines Computerprogramms (computer program 346), bei dem während der
Ausführung ein Benutzeroberflächenobjekt (graphical user interface objects) auf
einer Anzeigeeinrichtung (display device 118) zur Anzeige gebracht wird (vgl.
Abstract, Abs. 0030, 0059, 00104, Fig. 1, 2, 3A, 12A - 12E / Merkmale 1.1, 1.1.1).

                                             - 48 -



Die Bedienung des Computerprogramms umfasst mehrere auszuführende
Prozessschritte, die jeweils durch eine vorbestimmte Benutzerinteraktion mit
einem Benutzeroberflächenobjekt in einem bestimmten Fenster oder einer
Eingabemaske des Programms repräsentiert sind, wobei das Fenster oder die
Eingabemaske einen Kontext des Programms darstellen (vgl. Abs. 0059: … the
present invention instructs a user to provide specific input to perform a step of a
task within the computer program and awaits correct user input before providing
instructions related to the next step of the task… / Merkmale 1.1.2, 1.1.3). Als
Navigationsdatei, welche im anspruchsgemäßen Sinne die für die Bedienung des
Computerprogramms           erforderlichen    Benutzerinteraktionen      als      gespeicherte
Prozessschritte (programming instructions 347) enthält, ist eine Datensatz-Einheit
(entity map 345) anzusehen, welche mit einem Skript (script 344) zusammenwirkt
(vgl. Fig. 3B, Abs. 0065, 0064: … each item in the entity map 345 […] include a
name 349 for convenient reference to programming instructions 347 for accessing
the pertinent GUI object …, Abs. 0067: … the entity map 345 is stored as a distinct
file … / Merkmale 1.1.4, 1.1.5).


Druckschrift D3 beschreibt die Unterstützung eines Benutzers sowohl durch
Simulieren der erforderlichen Benutzereingaben in Form einer dem Benutzer
vorgeführten automatisch ablaufenden Instruktionsfolge als auch durch eine bloße
Anzeige der zugehörigen Hilfe bei der Ausführung bestimmter Bedienschritte
(Abs. 0061, 0062, Anspruch 1 bzw. Anspruch 12: … instructions indicating to a
user of the computer program how to perform the task …). Da bei beiden dieser in
D3 offenbarten Arten der Unterstützung die Datensatz-Einheit (entity map) in
Verbindung mit einem Skript zum Einsatz kommt (vgl. Abs. 0035), versteht der
Fachmann die Erläuterungen der Eigenschaften dieser Navigationsdatei so, dass
diese sowohl für eine automatisch ablaufende Simulation als auch für ein
Anzeigen von einzelnen Hilfeinformationen zur interaktiven Unterstützung des
Nutzers   gelten    (vgl.    Abs. 0062).      Dass    Druckschrift     D3,   entgegen     den
Ausführungen der Beklagten, nicht allein auf die Ausführungsform einer
Simulation,   bei     der      ein   Skript      Schritt-für-Schritt    abläuft     und    die
Benutzerinteraktionen automatisiert ausgeführt werden, zu reduzieren ist, ergibt

                                          - 49 -



sich bereits aus Absatz 0034, in der beide Unterstützungsarten als gleichwertige
Alternativen beschrieben werden, sowie aus den Absätzen 00120 und 00121, in
denen hinsichtlich der Durchführung des Skripts 344 jeweils für beide
Unterstützungsarten Angaben zur Visualisierung der Hilfe gemacht werden. Auch
für die Implementierung als eine bloße interaktive Hilfeanzeige ist Druckschrift D3
somit zu entnehmen, dass aus der als Navigationsdatei anzusehenden Datensatz-Einheit ein Prozessschritt geladen wird (vgl. Abs. 0086) und für den Prozessschritt
ein   Bezugswert    ermittelt    wird,   der   ein   dem   geladenen   Prozessschritt
entsprechendes zugehöriges Benutzeroberflächenobjekt identifiziert, ohne dass
eine Kontextermittlung explizit genannt ist (vgl. Abs. 0065, 0087: reference or
handle / Merkmal 1.2.1, Merkmal 1.2.4 teilweise). Aus der Angabe, dass aus der
Datensatz-Einheit bzw. dem Skript dynamisch auf ein Benutzeroberflächenobjekt
referenziert werden soll, um den entsprechenden Text in einem graphischen
Overlay darzustellen, entnimmt der Fachmann ohne Weiteres, dass eine
Ermittlung des aktuellen Kontexts des Computerprogramms erforderlich ist (vgl.
Fig. 3A u. 12E, Abs. 00113 / Merkmal 1.2.2 teilweise). Auf der Anzeigeeinrichtung
wird in jedem Fall das dem Prozessschritt entsprechende und somit das ermittelte
Benutzeroberflächenobjekt hervorgehoben, wie auch aus den Figuren 12A bis 12E
ersichtlich (vgl. Abs. 00110: … button being highlighted … / Merkmal 1.2.5).


Unstreitig sind aus Druckschrift D3 Systemhooks (hooks) bekannt zum Abfangen
von Benutzereingaben (user input), bevor diese an das Computerprogramm
weitergegeben      werden,      wobei    die   Benutzerinteraktionen   anhand    von
zugeordneten Regeln gemäß Merkmal 1.3 validiert werden (vgl. Fig. 3,
Abs. 0098: … impose hooks upon system input devices 330 that block, filter, or
otherwise monitor all user input …; Abs. 0099: … the input monitor 343 captures
user input before the system input queue 320 …; Abs. 00133 / Merkmal 1.3.1). Die
Überwachung der abzufangenden Benutzereingaben umfasst dabei auch eine
Überprüfung des richtigen Aktionstyps, welcher zu dem hervorgehobenen
Benutzeroberflächenobjekt in Bezug gesetzt wird, und ein Validieren der
Benutzereingabe (vgl. Abs. 0099, 00101; Abs. 00133, 00134: … to ascertain
received user input …, … provide corrective … instruction to a user indicating the

                                            - 50 -



proper type of input … / Merkmale 1.3.2, 1.3.4). Die Überprüfung und Validierung
erfolgt   dabei   neben       offensichtlich     per     Mouse-Zeiger    durchgeführten
Benutzereingaben (user clicks) auch für andere Benutzereingaben (vgl. Fig. 3A
i. V. m. Abs. 0099, … verify if the input is allowed under the current conditions;
Abs. 00102: … once the user clicks on the appropiate area or provides other
appropriate input … / Merkmale 1.3.3, 1.3.5).


Die Klägerin hat ausgeführt, Druckschrift D3 offenbare in der Abfolge der Figuren
12A und 12B sowie 12C und 12D jeweils einen Kontextwechsel, welcher durch
einen Klick des Benutzers erfolge. Die dabei erfolgende Überprüfung des
jeweiligen Mausklicks, wie in Figur 13 durch den „point balloon“ erläutert, stelle
bereits eine Kontextüberprüfung gemäß Merkmal 1.2.3 dar. Dieser Argumentation
zur mangelnden Neuheit des beanspruchten Verfahrens gegenüber Druckschrift
D3 vermag der Senat nicht zu folgen, da sich aus den Merkmalen 1.3.2 und 1.3.4
durch die Nennung des geladenen Prozessschritts und des zugehörigen
Benutzeroberflächenobjekts zwingend ergibt, dass die Verfahrensschritte der
Merkmale 1.2.1, 1.2.3 und 1.2.4, also das Laden des Prozessschritts, die
Kontextüberprüfung           und      die       Bestimmung         des      zugehörigen
Benutzeroberflächenobjekts, vorher erfolgen müssen, wie die Beklagte ausgeführt
hat.


Druckschrift D3 stellt somit nicht die Neuheit des Gegenstands gemäß Anspruch 1
in Frage, offenbart aber ein Verfahren mit den Merkmalen 1.1 bis 1.2.1, 1.2.4
teilweise, 1.2.5 und 1.3 bis 1.3.5 und gibt Hinweise darauf, dass eine
Kontextermittlung – vgl. die Merkmale 1.2.2 und 1.2.3 – erforderlich ist.


Druckschrift D4 (US 6 307 544 B1) offenbart im Zusammenhang mit dem Anbieten
von    Unterstützung   für    einen    Benutzer        während   der   Bedienung   eines
Computerprogramms eine Kontextermittlung und damit einen Verfahrensschritt
entsprechend Merkmal 1.2.2 (vgl. Sp 2, Z. 8 - 14: … when an assistance window
is created, the assistance system manager looks back at the application that
created the assistance window and determines the context …; Sp. 4, Z. 56 - 58

                                            - 51 -



i. V. m. Sp. 5, Z. 8 - 13). Der Fachmann entnimmt durch die Angabe eines
dynamisch erzeugten Kontext-Objekts auch das Ermitteln eines entsprechenden
Benutzeroberflächenobjekts (vgl. Sp. 5, Z. 8 - 13; Sp. 7, Z. 17 - 32), wobei die
erforderlichen Benutzerinteraktionen in einer Datei vorgehalten werden (definition
repository), welche als eine Navigationsdatei im anspruchsgemäßen Sinne
anzusehen ist (vgl. Sp. 3, Z. 21 - 27 / Merkmal 1.2.4). Für den Fachmann ergibt
sich aus diesem Hinweis auf eine kontextsensitive Benutzerunterstützung und der
Angabe, dass der Programmcode zur Unterstützung separiert sein soll von dem
Code des Computerprogramms, für das Unterstützung angeboten werden soll,
dass ein Kontextvergleich gemäß Merkmal 1.2.3 zu erfolgen hat (vgl. Sp. 1, Z. 58 -
65 i. V. m. Sp. 1, Z. 9 - 13).


Ausgehend von Druckschrift D3, welche wie ausgeführt, hinsichtlich der
Kontextermittlung bereits einen Hinweis entsprechend den Merkmalen 1.2.2 bis
1.2.4 gibt (vgl. Abs. 0087 i. V. m. Abs. 00113, 00123), erkennt der Fachmann bei
der   Realisierung       einer   Hilfe,   wie   in   Druckschrift   D3    beschrieben,   für
fensterbasierte Betriebssysteme, dass, sofern eine Kontextüberprüfung nicht
vorgesehen ist, gegebenenfalls ein Benutzeroberflächenobjekt im falschen
Fenster hervorgehoben wird. Zur Lösung dieses Problems wird der Fachmann auf
aus dem Stand der Technik bekannte Verfahren zurückgreifen und auf
Druckschrift D4 stoßen, welche im Zusammenhang mit dem Anbieten von
Unterstützung      für     einen      Benutzer       während    der      Bedienung   eines
Computerprogramms eine Kontextermittlung erläutert, die eine dynamische,
interaktive Hilfe für den aktuellen Prozessschritt der vom Nutzer ausgeführten
Anwendung ermöglicht (vgl. insbes. Sp. 1, Z. 9 - 13 i. V. m. Sp. 1, Z. 58 - 65;
Sp. 2, Z. 8 - 14; Sp. 3, Z. 21 - 27; Sp. 4, Z. 56 - 58; Sp. 5, Z. 8 - 13; Sp. 7, Z. 17 -
32). Implementiert der Fachmann eine solche Überprüfung des Kontexts bei dem
aus Druckschrift D3 bekannten Verfahren, so wird der aktuelle Kontext des
Computerprogramms ermittelt (Merkmal 1.2.2). Dabei ist es dem Fachmann auch
nahegelegt, diese Kontextermittlung auch dafür zu verwenden, das durch den
Prozessschritt bestimmte Benutzeroberflächenobjekt zu ermitteln und dies im

                                         - 52 -



weiteren Verfahren zu verwenden (vgl. Druckschrift D3, Abs. 00113, 00123 /
Merkmale 1.2.3, 1.2.4, 1.2.5).


Dem Fachmann ist somit – ausgehend von Druckschrift D3 – in Kenntnis von
Druckschrift D4 ein Verfahren mit sämtlichen Merkmalen gemäß Anspruch 1
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hauptantrag nicht auf
einer erfinderischen Tätigkeit beruht.


Ob darüber hinaus auch gegenüber einer Zusammenschau von Druckschrift D1
mit Druckschrift D2 oder von Druckschrift D1 mit Druckschrift D3 die erfinderische
Tätigkeit in Frage steht, wie im qualifizierten Hinweis ausgeführt, bedarf hier keiner
weiteren Erörterung.


2.    Das Streitpatent ist darüber hinaus nach Art. II § 6 Abs. 1 Nr. 3 IntPatÜG
i. V. m. Art. 138 Abs. 1 Buchst. c) EPÜ auch deshalb für nichtig zu erklären, weil
der Gegenstand des Anspruchs 1 über den Inhalt der Anmeldung in der
ursprünglich eingereichten Fassung hinausgeht.


a)    Bei der nachträglichen Geltendmachung des Nichtigkeitsgrundes der
unzulässigen Erweiterung durch Schriftsatz der Klägerin vom 18. Januar 2019
handelt es sich um eine sachdienliche und damit zulässige Klageänderung, weil
dadurch die Erhebung einer weiteren Nichtigkeitsklage vermieden werden konnte
(§ 99 Abs. 1 PatG i. V. m. § 263 ZPO). Eine Zurückweisung dieses weiteren
Angriffs als verspätet, wie von der Beklagten gerügt, scheitert schon daran, dass
die Klageerweiterung vor Ablauf der Präklusionsfrist (15. Februar 2019) bei
Gericht eingegangen ist, so dass es schon an einem erst nach Ablauf dieser Frist
vorgebrachten Angriffsmittel mangelt (§ 83 Abs. 4 PatG).


b)    Der erteilte Anspruch 1 unterscheidet sich vom ursprünglichen Anspruch 1
durch die Merkmalsgruppe 1.3, welche dem ursprünglichen Anspruch 11
entstammt, sowie durch die nachfolgend aufgeführten Merkmale 1.2.3 und 1.2.4
(Änderungen gegenüber dem ursprünglichen Anspruch 1 hervorgehoben):

                                    - 53 -




        1.2.3    - geprüft wird, ob der aktuelle Kontext des Computerprogramms
                 mit dem Kontext des geladenen Prozessschrittes übereinstimmt
                 (S2),

        1.2.4    - falls der aktuelle Kontext des Computerprogramms mit dem
                 Kontext des geladenen Prozessschrittes übereinstimmt, das an
                 der Anzeigeeinrichtung angezeigte Benutzeroberflächenobjekt
                 des Computerprogramms ermittelt wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen Prozessschrittes
                 entspricht (S4), und


Zur Offenbarung dieser Merkmale hat die Beklagte verwiesen auf Seite 14,
Absatz 3 bis Seite 15, Absatz 1 der ursprünglich eingereichten Unterlagen (vgl.
Anlage N2, entsprechend den Abs. 0040 - 0042 der Offenlegungsschrift des
Streitpatents EP 2 538 320 A1). Beschrieben wird dort eine Überprüfung, ob der
aktuelle Kontext des Computerprogramms mit dem Kontext des Prozessschritts
übereinstimmt, allerdings verknüpft mit einer durchzuführenden Synchronisierung
für den Fall, dass die Überprüfung negativ ausfällt. Dies entspricht der in der
Figur 1 der Anmeldung und des Streitpatents dargestellten Abfolge der Blöcke S2
– SYN – S3. Als weitere Offenbarungsstellen hinsichtlich der in den Anspruch 1
aufgenommenen Kontextüberprüfung könnte Seite 4, Zeilen 4 bis 14 sowie der
ursprüngliche Anspruch 3 herangezogen werden, die allerdings ebenfalls eine
Kontextüberprüfung verknüpfen mit einer Synchronisierung für den Fall eines
negativen Ergebnisses der Überprüfung. Der erteilte Anspruch 1 hingegen macht
keine Angaben dazu, was im Falle eines negativen Ergebnisses bei der
Kontextüberprüfung erfolgen soll und umfasst somit auch Verfahren, die zwar
einen Schritt der Kontextüberprüfung vorsehen, die aber ohne jegliche
Synchronisierung des Kontexts des geladenen Prozessschritts mit dem aktuellen
Ausführungs-Kontext auskommen. Ein solches Verfahren kann der Fachmann den
ursprünglichen Anmeldeunterlagen nicht als zur Erfindung gehörend entnehmen,
weder aus den angegebenen Zitatstellen in der Beschreibung, noch aus den
Figuren oder den ursprünglichen Ansprüchen und der gesamten Beschreibung.
Die Gesamtoffenbarung der ursprünglichen Unterlagen liefert keinen Hinweis
darauf, nach einer Kontextüberprüfung mit negativem Ergebnis ohne eine
Synchronisierung fortzufahren, etwa indem alle vorherigen Verfahrensschritte

                                              - 54 -



nochmals durchlaufen werden, wie die Beklagte argumentiert hat. Von dem
beanspruchten Verfahren ist z. B. auch umfasst, dass die Hilfefunktion im Falle
eines abweichenden Kontextes abgebrochen wird. Auch wenn aus einem
Ausführungsbeispiel nicht zwingend alle Einzelmerkmale in einen Anspruch
aufgenommen           werden           müssen           (vgl.          BGH,              Urteil       vom
16. Oktober 2007 - X ZR 226/02, BlPMZ 2008, 109, Amtl. LS a), Rn. 27
ff - Sammelhefter II) oder, wie die Beklagte argumentiert hat, aus einer Figur nicht
der   komplette      Inhalt    aufgenommen             werden         muss,       ist     anhand      der
Gesamtoffenbarung       zu     entscheiden,       ob     die      Merkmalskombination                eines
Anspruchs für den Fachmann aus den ursprünglichen Unterlagen unmittelbar und
eindeutig   zu    entnehmen       war.   Vorliegend        offenbaren         die        ursprünglichen
Anmeldeunterlagen dem Fachmann, entgegen den Ausführungen der Beklagten,
eine Kontextüberprüfung nur im Zusammenhang mit einem durchzuführenden
Synchronisierungsschritt bei negativ ausfallender Überprüfung und geben keinerlei
Hinweis darauf, neben einer Synchronisierung bei abweichendem Kontext („nein“-
Fall in Schritt S2 von Figur 1) weitere alternative Lösungen vorzusehen oder
solche Fälle grundsätzlich ins Belieben des Fachmanns zu stellen. Der
Gegenstand des erteilten Anspruchs 1 geht somit durch die Aufnahme der
Merkmale 1.2.3 und 1.2.4 über den Inhalt der Anmeldung in der ursprünglich
eingereichten Fassung hinaus.


Nach dem Verständnis des Senats handelt es sich bei der Aufnahme der
Merkmale    1.2.3    und      1.2.4,   also    der     Kontextüberprüfung,                welche     ohne
Synchronisierung erfolgen soll, nicht um eine bloße Konkretisierung gegenüber
dem angemeldeten Gegenstand und auch nicht um eine Verallgemeinerung, die
unterschiedliche offenbarte Ausgestaltungen für diesen Fall zusammenfasst. In
den   ursprünglich     eingereichten      Unterlagen            ist   lediglich         offenbart,    eine
Kontextüberprüfung durchzuführen, welche mit einer Synchronisierung verknüpft
ist, oder aber gar keine Kontextüberprüfung durchzuführen, womit in Kauf
genommen wird, dass bei nicht passendem Kontext möglicherweise ein falscher
Hilfetext angezeigt wird, bzw. dass der Benutzer die Hilfe nicht an jeder Stelle im
Workflow    des     Computerprogramms             anfordern           kann    (vgl.       ursprüngliche

                                         - 55 -



Anmeldeunterlagen, Seite 4, dritter Absatz). Unter den erteilten Anspruch 1 jedoch
fallen, wie die Beklagte in der mündlichen Verhandlung erläutert hat, auch
Verfahren, bei denen nach einer Kontextüberprüfung mit negativem Ergebnis auf
eine andere Art als über eine Synchronisierung erwirkt wird, dass die weiteren
Verfahrensschritte ablaufen können, beispielsweise indem alle vorherigen
Verfahrensschritte      noch   einmal   durchlaufen      werden,   so    lange,    bis    die
Kontextüberprüfung ein positives Ergebnis zeigt. Da der Fachmann den
ursprünglichen Anmeldeunterlagen nur entnimmt, dass eine Überprüfung des
Kontextes nur dann erfolgt, wenn bei nichtübereinstimmendem Kontext als
nächster   Schritt      eine   Synchronisierung    der     Navigationsdatei       mit    dem
Computerprogramm erfolgt, stellt der mit dem erteilten Anspruch 1 beanspruchte
Verfahrensablauf keine bloße Einschränkung des angemeldeten Gegenstands dar
(vgl.   BGH,   Urteil    vom    17. Februar 2015    –     X ZR 161/12,    GRUR          2015,
573 - Wundbehandlungsvorrichtung, m. w. N.).

                                            - 56 -



3.     Hinsichtlich der Frage des Patentierungsverbots gemäß Art. 52 Abs. 2 und
3 EPÜ sieht der Senat die Technizität des Gegenstands von Anspruch 1 durch die
Funktion des in Merkmalsgruppe 1.3 aufgeführten Systemhooks als gegeben an.
Durch diesen Systemhook, durch welchen in die Programmausführung durch den
Prozessor eingegriffen wird, sowie durch die Validierung der dabei erfassten
Nutzereingabe soll zumindest im Ansatz eine fehlerhafte Bedienung verhindert
werden, was einen technischen Bezug über die reine Datenverarbeitung hinaus
darstellt   und      wodurch    der    Gegenstand       des    Anspruchs 1      auch   den
Patentierungsausschluss für Computerprogramme als solche überwindet. Die
Merkmalsgruppen 1.2 und 1.3 sind durch die aufgeführten Begriffe eines
geladenen Prozessschritts und eines zu ermittelnden Benutzeroberflächenobjekts
zueinander      in   Bezug     gesetzt.    Diese      Verknüpfung    verleiht   auch   der
Merkmalsgruppe        1.2   einen     technischen     Bezug,   so   dass    entgegen   der
Argumentation der Klägerin hinsichtlich Anspruch 1 alle Merkmale als technische
Merkmale bei der Prüfung der erfinderischen Tätigkeit zu berücksichtigen sind.


Dahingestellt     bleiben    kann,    ob   einzelne    Merkmale     der    Unteransprüche,
insbesondere die Merkmale von Unteranspruch 6, als nichttechnische Merkmale
bei der Prüfung auf erfinderische Tätigkeit unbeachtet bleiben können (vgl. BGH,
Urteil vom 26. Oktober 2010 – X ZR 47/07, GRUR 2011, 125, zweiter Leitsatz –
Wiedergabe topografischer Informationen; BGH, Beschluss vom 20. Januar 2009
– X ZB 22/07, GRUR 2009, 479, Abs. II.3. – Steuerungseinrichtung für
Untersuchungsmodalitäten).


4.     Die weiteren Patentansprüche des Hauptantrags bedürfen keiner weiteren,
isolierten Prüfung, weil die Beklagte sowohl schriftsätzlich als auch in der
mündlichen Verhandlung zu erkennen gegeben hat, dass sie den Hauptantrag als
geschlossenen Anspruchssatz versteht und das Streitpatent nur in der Reihenfolge des Hauptantrags und der Hilfsanträge in der gemäß der in der mündlichen
Verhandlung eingereichten Aufstellung jeweils als Ganzes verteidigt (vgl. BGH,
Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator).

                                       - 57 -



                           III.   Zu den Hilfsanträgen


Das Streitpatent ist auch in den Fassungen nach den Hilfsanträgen, mit denen die
Beklagte es beschränkt verteidigt, nach Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. a) EPÜ für nichtig zu erklären, weil der Gegenstand des
Anspruchs 1 von Hilfsantrag 0 nicht patentfähig ist, die Hilfsanträge I bis VIII vom
18. Januar 2019 nicht zulässig sind und die Gegenstände des jeweiligen Anspruchs 1 nach den Hilfsanträgen I bis VIIIc vom 27. Februar 2019 nicht patentfähig sind.


1.     Zu Hilfsantrag 0



Mit Hilfsantrag 0, den die Beklagte in Reaktion auf den von der Klägerin
vorgebrachten Nichtigkeitsgrund der unzulässigen Erweiterung gestellt hat, hat sie
auf   die   sogenannte     Fußnotenlösung       Bezug       genommen   (vgl.   BGH,
a. a. O. - Wundbehandlungsvorrichtung; BGH, Beschluss vom 21. Oktober 2010,
Xa ZB 14/09, GRUR 2011, 40, Rn. 14 u. 16 - Winkelmesseinrichtung) und
beantragt, dass bei der Frage der Validitäten folgendes Merkmal nicht zu
berücksichtigen sei (Kursivmarkierung senatsseitig hinzugefügt):


      M*     wobei        vor      dem          Ermitteln      des      angezeigten
             Benutzeroberflächenobjekts des Computerprogramms geprüft wird,
             ob der aktuelle Kontext des Computerprogramms mit dem Kontext
             des geladenen Prozessschrittes übereinstimmt, und, falls der
             aktuelle Kontext des Computerprogramms nicht mit dem Kontext des
             geladenen Prozessschritts übereinstimmt, eine Synchronisierung der
             Navigationsdatei mit dem Computerprogramm durchgeführt wird


a)     Antragsgemäß wäre aus dem erteilten Anspruch 1 das Merkmal M* im
Nichtigkeitsverfahren bei der Prüfung auf u. a. unzulässige Erweiterung, Neuheit
und erfinderische Tätigkeit zu streichen. Im erteilten Anspruch ist, wie die Klägerin
zutreffend ausgeführt hat, Merkmal M* aber nicht enthalten; Merkmal M* entspricht

                                         - 58 -



vielmehr – bis auf die Streichung der Bezugszeichen – dem Wortlaut des erteilten
Anspruchs 3, welcher mit der Klage nicht angegriffen ist und somit nicht
Gegenstand       des    Patentnichtigkeitsverfahrens           ist.   Insofern      ist    die
Nichtberücksichtigung von Merkmal M* entsprechend der Fußnote als Ganzes
nicht möglich.


Von dem in Merkmal M* Aufgeführten ist im erteilten Anspruch 1 lediglich die
vorstehend kursiv markierte Wortfolge, welche das Merkmal 1.2.3 bildet, zu finden.
Da der Rest der „Fußnote“ nicht Bestandteil von Anspruch 1 ist, kann dieser auch
nicht gesondert unberücksichtigt bleiben. Der Antrag kann daher allenfalls zur
Folge haben, dass Anspruch 1 gemäß Hilfsantrag 0 aus sämtlichen Merkmalen
des erteilten Anspruchs 1 besteht, bis auf das Merkmal 1.2.3. Wie ausgeführt,
beruht der Gegenstand des erteilten Anspruchs 1 gegenüber den Druckschriften
D3 und D4 nicht auf einer erfinderischen Tätigkeit (vgl. vorstehende Ausführungen
zum Hauptantrag in Abschnitt A. II. 1.). Dies gilt selbstverständlich ebenso für ein
Verfahren, welches das Merkmal 1.2.3, das den Verfahrensschritt einer
Kontextüberprüfung benennt, nicht aufweist. Der Gegenstand des Anspruchs 1
nach Hilfsantrag 0 ist dem Fachmann somit ebenfalls ausgehend von Druckschrift
D3 in Kenntnis von Druckschrift D4 nahegelegt, sodass der Gegenstand des
Anspruchs 1 nach Hilfsantrag 0 nicht auf einer erfinderischen Tätigkeit beruht.


b)    Auch mit der beantragten Fußnote ist die mangelnde Ursprungsoffenbarung
des Gegenstands gemäß Anspruch 1 nicht behoben. Denn selbst wenn aus dem
erteilten Anspruch 1 das dort aufgeführte Merkmal 1.2.3 gestrichen würde, so ist
von   dem      beanspruchten      Verfahren       jedenfalls    implizit    weiterhin     eine
Kontextüberprüfung umfasst. Denn gemäß Merkmal 1.2.4 erfolgt allein bei einer
Übereinstimmung zwischen dem Kontext des Computerprogramms und dem
geladenen        Prozessschritt      eine          Ermittlung         des        angezeigten
Benutzeroberflächenobjekts, die einen Vergleich – und somit eine Überprüfung –
voraussetzt.     Jeglicher   Vergleich        zwischen         Anwendungskontext          und
Prozessschrittkontext ist in der Ursprungsoffenbarung jedoch auch mit einer
Reaktion für den negativen Fall („nein“-Fall in Schritt S2 der Figur 1) in Form einer

                                      - 59 -



Synchronisierung verknüpft (vgl. wiederum S. 14, Abs. 3 - S. 15, Abs 1 der
ursprünglichen Anmeldeunterlagen). Der Gegenstand eines Anspruchs 1 unter
Nichtberücksichtigung von Merkmal 1.2.3 im Sinne der Fußnotenlösung geht somit
ebenfalls über den Inhalt der Anmeldung in der ursprünglich eingereichten
Fassung hinaus.


2.    Zu den Hilfsanträgen I bis VIII vom 18. Januar 2019


Die Hilfsanträge I bis VIII vom 18. Januar 2019 sind bereits unzulässig, weil eine
Änderung nicht im Streit stehender Patentansprüche, vorliegend der Ansprüche 3
bis 5 sowie 7 bis 9, im Nichtigkeitsverfahren auch im Weg der Selbstbeschränkung
nicht in Betracht kommt (vgl. BGH, Urteil vom 1. März 2017 – X ZR 10/15, GRUR
2017, 604, Rn. 27 – Ankopplungssystem m. w. N.). Ein Patent kann vom
Nichtigkeitsbeklagten nämlich nur in dem Umfang beschränkt verteidigt werden, in
dem es vom Nichtigkeitskläger angegriffen wird. Andernfalls wird das Streitpatent
der Sache nach im Umfang des nicht angegriffenen Unteranspruchs zur
gerichtlichen Überprüfung gestellt. Die Möglichkeit, das Patent beschränkt zu
verteidigen, dient aber allein der Verteidigung des Nichtigkeitsbeklagten
gegenüber dem vom Nichtigkeitskläger geführten Angriff auf die Wirksamkeit des
Patents und nicht auch der gerichtlichen Überprüfung des Patents im Übrigen. Die
beschränkte Verteidigung gegenüber einer Teilnichtigkeitsklage auch im Umfang
eines nicht angegriffenen Unteranspruchs hätte im Wesentlichen die Wirkung
einer Widerklage des Patentinhabers gegenüber dem Nichtigkeitskläger auf
Feststellung der Rechtsbeständigkeit des Streitpatents im Umfang des nicht
angegriffenen Unteranspruchs. Eine solche Klage ist aber im Gesetz nicht
vorgesehen und kann deshalb auch nicht Gegenstand einer beschränkten
Verteidigung des Nichtigkeitsbeklagten sein. Die Hilfsanträge I bis VIII vom
18. Januar 2019 begehren Klageabweisung, die gleichbedeutend wäre mit einer
Aufrechterhaltung des Patents mit den Ansprüchen 3 bis 5 sowie 7 bis 9 mit einem
Rückbezug auf einen geänderten Anspruch 1, nämlich von Hauptanspruch 1 wie
erteilt in Hauptanspruch 1 wie im jeweiligen Hilfsantrag vom 18.Januar 2019. Da

                                           - 60 -



sich dadurch der Gegenstand des jeweiligen Unteranspruchs ebenfalls ändert,
sind diese Hilfsanträge unzulässig.


Die Beklagte hat hierzu ausgeführt, aus dem Angriff der Klägerin auf Anspruch 14,
welcher sich auf alle Verfahrensansprüche rückbeziehe, ergebe sich, dass
Anspruch 14 und sämtliche von diesem inkludierten Ansprüche angegriffen seien.
Der    erteilte     Anspruch 14    ist   auf     ein   Computerprogrammprodukt      mit
Programmcode gerichtet, welcher das Verfahren gemäß einem der Ansprüche 1
bis 12 zur Ausführung bringt. Auch dieser Rückbezug des nebengeordneten
Anspruchs führt nicht dazu, dass der, wie die Klägerin richtig ausführt, eindeutige
Klageantrag, der sich allein gegen die Ansprüche 1, 2, 6, 11, 12, 13 und 14 richtet,
auf die nicht angegriffenen Unteransprüche 3 bis 5 und 7 bis 10 auszuweiten ist,
zu denen die Klägerin keinerlei Ausführungen gemacht hat. Die Hilfsanträge I bis
VIII vom 18. Januar 2019, die sämtlich beispielsweise den weder durch den
ausformulierten      Klageantrag    noch       durch   die   weiteren   Argumentationen
angegriffenen Unteranspruch 3 in einer, durch den Rückbezug auf den geänderten
Anspruch 1, geänderten Form enthalten, sind somit nicht zulässig.


3.     Zu Hilfsantrag I vom 27. Februar 2019


Der Gegenstand des Anspruchs 1 nach Hilfsantrag I vom 27. Februar 2019 beruht
gegenüber dem Stand der Technik gemäß Druckschrift D3 in Verbindung mit
Druckschrift D4 ebenfalls nicht auf einer erfinderischen Tätigkeit.


Mit Hilfsantrag I wird der erteilte Anspruch 1 um folgende Merkmale ergänzt:


      11.1        wobei die Navigationsdatei mit einem Aufzeichnungsmittel auf einer
                  ersten Datenverarbeitungseinrichtung erzeugt wird und das zu
                  bedienende       Computerprogramm           auf       einer   zweiten
                  Datenverarbeitungseinrichtung ausgeführt wird,

      11.2        wobei die Navigationsdatei vor dem Ermitteln (S1) des aktuellen

                                          - 61 -



              Kontextes des Computerprogramms in einen Arbeitsspeicher der
              zweiten Datenverarbeitungseinrichtung geladen wird


Diese Merkmale betreffen das Erzeugen der Navigationsdatei und das Laden
derselben in einen Arbeitsspeicher. Der erteilte Anspruch 1 ist auf ein computerimplementiertes Verfahren gerichtet, welches zur Unterstützung eines Benutzers
während einer Bedienung eines Computerprogramms dient (vgl. Merkmal 1.1) und
welches dazu aus einer Navigationsdatei dort gespeicherte Prozessschritte lädt
(vgl. Merkmale 1.1.4, 1.2.1). Wie diese Navigationsdatei erzeugt worden ist und
auf welcher Datenverarbeitungseinrichtung diese Erzeugung stattgefunden hat,
wird durch das Verfahren des Anspruchs 1, welches lediglich die Bedienung eines
Computerprogramms betrifft, nicht charakterisiert. Dies bedeutet, dass das
Merkmal 11.1, soweit es das Erzeugen der Navigationsdatei betrifft, das
beanspruchte Verfahren in keiner Weise beschränkt.


Die weiteren in den Merkmalen 11.1 und 11.2 aufgeführten Schritte, wonach das
zu bedienende Computerprogramm auf einer Datenverarbeitungseinrichtung
auszuführen     und   die    Navigationsdatei        in     den    Arbeitsspeicher   der
Datenverarbeitungseinrichtung zu laden ist, stellen das übliche Vorgehen bei
computerimplementierten Verfahren dar. Sowohl Druckschrift D3 (vgl. Abs. 0067:
the entity map 345 is stored … in RAM …; Abs. 0031: … displaying a graphical
overlay on top of an actual, non-simulated graphical user interface of the computer
program …; Abs. 00138: … the invention may operate in conjunction with … the
target application…) wie auch Druckschrift D4 (vgl. Ansprüche 16 u. 24, Sp. 3,
Z. 21 - 26) geben dem Fachmann den Hinweis, das Computerprogramm, für das
Unterstützung   benötigt    wird,   und     die    für    die   Unterstützung   benötigte
Navigationsdatei (D3: script i. V. m. entity map; D4: definition repository)
beispielsweise auf derselben Datenverarbeitungseinrichtung auszuführen und zu
laden (Merkmale 11.1, 11.2).


Darüber hinaus würde auch bei Berücksichtigung des Merkmals 11.1 als Ganzes
die erfinderische Tätigkeit gegenüber den Druckschriften D3 und D4 nicht

                                        - 62 -



gegeben sein, da aus Druckschrift D3 ein Aufzeichnen der Navigationsdatei auf
einer    anderen     Datenverarbeitungseinrichtung      als   der,   auf   der   das
Computerprogramm, für das Hilfe angeboten wird, bekannt ist (vgl. Abs. 00128 u.
00129: recording component 1610 i. V. m. Abs. 00137: … scripts provided to the
user … via the Internet / Merkmal 11.1).


Der Gegenstand des Anspruchs 1 nach Hilfsantrag I vom 27. Februar 2019 ist
dem Fachmann somit ebenfalls ausgehend von Druckschrift D3 in Kenntnis von
Druckschrift D4 nahegelegt.


4.      Zu Hilfsantrag Ia


Hilfsantrag Ia besteht aus Hilfsantrag I vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag I vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1 und 11.2 keinen weiteren Bezug zu Merkmal 1.2.3 oder einer
Synchronisierung herstellen, gelten bezüglich Anspruch 1 gemäß Hilfsantrag Ia
die Ausführungen zu Hilfsantrag 0 bzw. Hilfsantrag I vom 27. Februar 2019 in
gleicher Weise. Der Gegenstand des Anspruchs 1 nach Hilfsantrag Ia ist dem
Fachmann somit ebenfalls ausgehend von Druckschrift D3 in Kenntnis von
Druckschrift D4 nahegelegt, sodass der Gegenstand des Anspruchs 1 nach
Hilfsantrag Ia nicht auf einer erfinderischen Tätigkeit beruht.


5.      Zu Hilfsantrag II vom 27. Februar 2019


Der Gegenstand des Anspruchs 1 nach Hilfsantrag II vom 27. Februar 2019
beruht gegenüber dem Stand der Technik gemäß Druckschrift D3 in Verbindung
mit Druckschrift D4 ebenfalls nicht auf einer erfinderischen Tätigkeit.


Gegenüber Anspruch 1 gemäß Hilfsantrag I wurde Anspruch 1 um folgendes
weiteres Merkmal ergänzt:

                                       - 63 -



     11.3       wobei die Navigationsdatei erzeugt wird durch Verwendung eines
                Aufzeichnungsverfahrens, bei welchem die Benutzerinteraktionen
                auf der ersten Datenverarbeitungseinrichtung durch einen Benutzer
                durchgeführt werden


Auch dieses Merkmal betrifft die Erzeugung der Navigationsdatei und kann daher
das beanspruchte Verfahren zur Unterstützung eines Bedieners während einer
Bedienung des Computerprogramms nicht kennzeichnen (vgl. vorstehende
Ausführungen zu Anspruch 1 nach Hilfsantrag I).


Darüber hinaus ist es aus Druckschrift D3 auch bekannt, durch einen Benutzer
durchgeführte       Benutzerinteraktionen       mit   einem   Aufzeichnungsmittel
aufzuzeichnen (vgl. Abs. 00129: While the recording component 1610 is active,
user input directed to the computer program 346 is captured and recorded … /
Merkmal 11.3).


Der Gegenstand des Anspruchs 1 nach Hilfsantrag II vom 27. Februar 2019 ist
dem Fachmann somit ebenfalls ausgehend von Druckschrift D3 in Kenntnis von
Druckschrift D4 nahegelegt.


6.    Zu Hilfsantrag IIa


Hilfsantrag IIa besteht aus Hilfsantrag II vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag II vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1, 11.2 und 11.3 keinen weiteren Bezug zu Merkmal 1.2.3 oder einer
Synchronisierung herstellen, gilt für den Anspruch 1 gemäß Hilfsantrag IIa das zu
Hilfsantrag 0 bzw. Hilfsantrag II vom 27. Februar 2019 Gesagte. Der Gegenstand
des Anspruchs 1 nach Hilfsantrag IIa ist dem Fachmann somit ebenfalls
ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4 nahegelegt,
sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag IIa nicht auf einer
erfinderischen Tätigkeit beruht.

                                              - 64 -



7.       Zu Hilfsantrag III vom 27. Februar 2019


Der Gegenstand des Anspruchs 1 nach Hilfsantrag III vom 27. Februar 2019
beruht gegenüber dem Stand der Technik gemäß Druckschrift D3 in Verbindung
mit Druckschrift D4 ebenfalls nicht auf einer erfinderischen Tätigkeit.


Gegenüber Anspruch 1 gemäß Hilfsantrag II wurde Anspruch 1 um folgendes
weiteres Merkmal ergänzt:


     11.4       und   jeweils     die   Benutzerinteraktion,        der   Kontext       und   das
                Benutzeroberflächenobjekt              als      Prozessschritte         in    der
                Navigationsdatei gespeichert werden


Merkmal 11.4 beschreibt lediglich den Inhalt der Navigationsdatei, nämlich dass
die dort gespeicherten Prozessschritte, die Benutzerinteraktion, den Kontext und
das Benutzeroberflächenobjekt aufweisen. Dies ergibt sich bereits aus Merkmal
1.1.3 des erteilten Anspruchs 1.


Druckschrift D3 gibt an, dass bei der Ausführung des Skripts, welches auf die
entity    map   zugreift,   für   das    angezeigte          Benutzeroberflächenobjekt        des
Computerprogramms ein grafischer Overlay erzeugt wird, der Text oder Grafik
enthält, welche dem Benutzer die zugehörige Benutzerinteraktion aufzeigen (vgl.
Abs. 0031: The formulated script is executed by displaying a partial graphical
overlay on top of an actual, non-simulated graphical user interface of the computer
program. Each partial graphical overlay may include text, graphics, animation, or
video indicating to a user how to provide input to the associated graphical user
interface object of the computer program to perform a step of the task.). Aus der
Angabe, dass jeweils zu dem aktuellen Benutzeroberflächenobjekt die zugehörige
Overlay-Information anzuzeigen ist, ersieht der Fachmann, dass in der
Navigationsdatei        neben           der        Benutzerinteraktion            und         dem
Benutzeroberflächenobjekt auch der damit verbundene Kontext, also etwa die
Eingabemaske in einem vorbestimmten Zustand (vgl. Streitpatent, Abs. 0032)

                                        - 65 -



abgespeichert sein muss (Merkmal 11.4). Zu den weiteren Merkmalen ist auf die
Ausführungen zum Hauptantrag sowie zu den Hilfsanträgen I und II vom
27. Februar 2019 zu verweisen, die hier in gleicher Weise gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag III vom 27. Februar 2019 ist
dem Fachmann somit ebenfalls ausgehend von Druckschrift D3 in Kenntnis von
Druckschrift D4 nahegelegt.


8.    Zu Hilfsantrag IIIa


Hilfsantrag IIIa besteht aus Hilfsantrag III vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag III vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält und die hinzugefügten
Merkmale 11.1, 11.2, 11.3 und 11.4 keinen weiteren Bezug zu Merkmal 1.2.3 oder
einer Synchronisierung herstellen, gilt für den Anspruch 1 gemäß Hilfsantrag IIIa
das zu Hilfsantrag 0 bzw. Hilfsantrag III vom 27. Februar 2019 Gesagte. Der
Gegenstand des Anspruchs 1 nach Hilfsantrag IIIa ist dem Fachmann somit
ebenfalls ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag IIIa nicht
auf einer erfinderischen Tätigkeit beruht.


9.    Zu Hilfsantrag IV vom 27. Februar 2019


Auch der Gegenstand des Anspruchs 1 nach Hilfsantrag IV vom 27. Februar 2019
beruht gegenüber dem Stand der Technik gemäß Druckschrift D3 in Verbindung
mit Druckschrift D4 nicht auf einer erfinderischen Tätigkeit.


Gegenüber Hilfsantrag III wurde Anspruch 1 um folgendes Merkmal ergänzt:


     11.5     wobei der Kontext eine vorbestimmte Benutzeroberfläche des
              Computerprogramms          in      einem    vorbestimmten   Zustand
              kennzeichnet

                                     - 66 -



Die in Merkmal 11.5 gegebene Definition des Kontexts bezieht sich auf die in der
Navigationsdatei hinterlegte und damit vorbestimmte Beschreibung des Kontexts
und entspricht der bereits dem Hauptantrag zugrunde gelegten Auslegung. Sie
entspricht damit den Zusammenhängen, die dem Stand der Technik zu
entnehmen sind (vgl. Ausführungen zu Merkmal 1.2.2 in Abschnitt A. I. 3.). Dem
steht im Gegensatz zu der Auffassung der Beklagten nicht entgegen, dass
Druckschrift D4 bei der Kontextermittlung auf die Anwendung Bezug nimmt, da die
dort ebenfalls beschriebene Hervorhebung des Benutzeroberflächenobjekts durch
ein Assistenz-Fenster (assistance window) gerade auf den Zustand des aktuellen
Benutzeroberflächenobjekts Bezug nimmt (vgl. Druckschrift D4, Sp. 5, Z. 8 - 13
i. V. m. Sp. 2, Z. 8 - 14).


Der Gegenstand des Anspruchs 1 nach Hilfsantrag IV vom 27. Februar 2019 ist
somit aus den gleichen Gründen nicht patentfähig wie der Gegenstand des
Anspruchs 1 nach Hilfsantrag III vom 27. Februar 2019.


10.    Zu Hilfsantrag Iva


Hilfsantrag IVa besteht aus Hilfsantrag IV vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag IV vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1 bis 11.5 keinen weiteren Bezug zu Merkmal 1.2.3 oder einer
Synchronisierung herstellen, gilt für den Anspruch 1 gemäß Hilfsantrag IVa das zu
Hilfsantrag 0 bzw. Hilfsantrag IV vom 27. Februar 2019 Gesagte. Der Gegenstand
des Anspruchs 1 nach Hilfsantrag IVa ist dem Fachmann somit ebenfalls
ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4 nahegelegt,
sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag IVa nicht auf einer
erfinderischen Tätigkeit beruht.

                                              - 67 -



11.    Zu Hilfsantrag V vom 27. Februar 2019


In der Fassung gemäß Hilfsantrag V kann das Streitpatent ebenfalls keinen
Bestand haben.


Anspruch 1 gemäß Hilfsantrag V basiert auf Anspruch 1 gemäß Hauptantrag
(erteilter Anspruch 1), wobei nach Merkmal 1.1.3 das folgende Merkmal ergänzt
wurde:


      1.1.3.1     wobei      ein    Benutzeroberflächenobjekt        ein     Objekt     an       einer
                  Benutzeroberfläche des Computerprogramms ist, über welches
                  der Benutzer mit dem Computerprogramm interagieren kann,


und nach Merkmal 1.3.5 das folgende Merkmal angeschlossen wurde:


      1.3.6     wobei der Systemhook angepasst ist, bei einem negativen Ergebnis
                der Validierung die Benutzereingabe zu verwerfen und bei einem
                positiven Ergebnis die Benutzereingabe an das Computerprogramm
                weiterzugeben.


Merkmal       1.1.3.1    gibt      die    fachübliche   Definition     des       Begriffs        eines
Benutzeroberflächenobjekts;              Merkmal   1.3.6   definiert       für    den       in    der
Merkmalsgruppe 1.3 aufgeführten Systemhook, was in Abhängigkeit des
Ergebnisses der Validierung mit der Benutzereingabe passiert, nämlich entweder
die   Weitergabe        an   das     Computerprogramm        oder      das       Verwerfen        der
Benutzereingabe.


Die in den Druckschriften D3 und D4 offenbarten Benutzeroberflächenobjekte
stellen ebenfalls Objekte dar, über die der Benutzer mit dem Computerprogramm
interagieren kann (vgl. D3: Fig. 3A: GUI 310; Fig. 12A - 12D, Fig. 13; Abs. 0053,
Abs. 0055: The user manipulates the various input devices 126, 127, 128 to alter
and interact with the graphically displayed objects …; vgl. D4: Fig. 1 - 3; Sp. 3,

                                         - 68 -



Z. 21 - 24, Z. 55 - 60 / Merkmal 1.1.3.1). Zudem sind die aus Druckschrift D3
bekannten Systemhooks (hooks) angepasst, Benutzereingaben je nach dem
Ergebnis der Validierung zu blockieren oder zuzulassen, wobei die validierten
Benutzereingaben, also diejenigen mit positivem Ergebnis der Validierung, an die
Eingabe-Warteschlange und damit an das Computerprogramm weitergegeben
werden (vgl. D3, Abs. 0099: … hooks, … in order to block or allow all user input;
Abs. 00101: If the user input is incorrect, the input is ignored … If the user input is
correct, signals created by the input are sent 1140 to the input queue 320 … /
Merkmal 1.3.6). Für die weiteren Merkmale ist auf die Ausführungen zum
Hauptantrag zu verweisen, die hier in gleicher Weise gelten.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag V ist dem Fachmann somit
ebenfalls ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag V nicht auf
einer erfinderischen Tätigkeit beruht.


12.    Zu Hilfsantrag Va


Hilfsantrag Va besteht aus Hilfsantrag V vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag V vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 1.1.3.1 und 1.3.6 keinen weiteren Bezug zu Merkmal 1.2.3 oder einer
Synchronisierung herstellen, gilt für den Anspruch 1 gemäß Hilfsantrag Va das zu
Hilfsantrag 0 bzw. Hilfsantrag V vom 27. Februar 2019 Gesagte. Der Gegenstand
des Anspruchs 1 nach Hilfsantrag Va ist dem Fachmann somit ebenfalls
ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4 nahegelegt,
sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag Va nicht auf einer
erfinderischen Tätigkeit beruht.

                                        - 69 -



13.   Zu Hilfsantrag VI vom 27. Februar 2019


Anspruch 1 gemäß Hilfsantrag VI kombiniert die Merkmale von Anspruch 1 gemäß
Hilfsantrag IV mit den in Anspruch 1 gemäß Hilfsantrag V hinzugefügten
Merkmalen.     Aus   der    Kombination     von   Angaben     zur   Erzeugung   der
Navigationsdatei und zur Verwendung des Systemhooks mit den weiteren
Merkmalen ergeben sich für das beanspruchte computerimplementierte Verfahren
keine über die bloße Aneinanderreihung der zusätzlichen Merkmale weiteren
Effekte. Daher gilt hier ebenfalls das für die Hilfsanträge IV und V vom
27. Februar 2019 Ausgeführte.


Das Verfahren des Anspruchs 1 nach Hilfsantrag VI ist dem Fachmann somit
ebenso ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag VI
ebenfalls nicht auf einer erfinderischen Tätigkeit beruht.


14.   Zu Hilfsantrag Via


Hilfsantrag VIa besteht aus Hilfsantrag VI vom 27. Februar 2019 plus der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag VI vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1 bis 11.5, 1.1.3.1 und 1.3.6 keinen weiteren Bezug zu Merkmal
1.2.3 oder einer Synchronisierung herstellen, gilt für den Anspruch 1 gemäß
Hilfsantrag VIa das zu Hilfsantrag 0 bzw. Hilfsantrag VI vom 27. Februar 2019
Gesagte. Der Gegenstand des Anspruchs 1 nach Hilfsantrag VIa ist dem
Fachmann somit ebenfalls ausgehend von Druckschrift D3 in Kenntnis von
Druckschrift D4 nahegelegt, sodass der Gegenstand des Anspruchs 1 nach
Hilfsantrag VIa nicht auf einer erfinderischen Tätigkeit beruht.

                                          - 70 -



15.    Zu Hilfsantrag VII vom 27. Februar 2019


Auch in der Fassung gemäß Hilfsantrag VII kann das Streitpatent keinen Bestand
haben.


Gegenüber Anspruch 1 gemäß Hilfsantrag VI wurde Anspruch 1 um folgende
weitere Merkmale ergänzt:


      12.1    wobei das Verfahren ferner einen Schritt (S3) zum Anzeigen von
              Informationen    zu   der    von     dem   Benutzer   durchzuführenden
              Benutzerinteraktion auf der Anzeigeeinrichtung umfasst,
      12.2    wobei die Informationen vorzugsweise ein Bild des zu bedienenden
              Benutzeroberflächenobjektes          und    einen     Beschreibungstext
              umfassen


Das Merkmal 12.2 benennt lediglich fakultativ, was die Informationen umfassen
sollen, und schränkt das beanspruchte Verfahren somit nicht ein. Aus Druckschrift
D3 ist es bekannt, bei dem Verfahren zur Unterstützung eines Benutzers während
der Bedienung auch vorzusehen, Informationen zu der durchzuführenden
Benutzerinteraktion anzuzeigen (vgl. Fig. 12A - 12E, Fig. 15: display partial
graphical overlay 1515; Abs. 0059, Abs. 00121: Each partial graphical overlay
visually indicates to the user to provide input to cause the computer program 346
to perform a step of the task …; Abs. 00122 / Merkmal 12.1). Für die übrigen
Merkmale gilt das zu Hilfsantrag VI Ausgeführte ebenso. Auch der Gegenstand
des Anspruchs 1 nach Hilfsantrag VII vom 27. Februar 2019 beruht daher
gegenüber dem Stand der Technik gemäß Druckschrift D3 in Verbindung mit
Druckschrift D4 nicht auf einer erfinderischen Tätigkeit.


16.    Zu Hilfsantrag VIIa


Hilfsantrag VIIa besteht aus Hilfsantrag VII vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag VII vom

                                            - 71 -



27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1 bis 11.5, 1.1.3.1, 1.3.6, 12.1 und 12.2 keinen weiteren Bezug zu
Merkmal 1.2.3 oder einer Synchronisierung herstellen, gilt für den Anspruch 1
gemäß Hilfsantrag VIIa das zu Hilfsantrag 0 bzw. Hilfsantrag VII vom
27. Februar 2019 Gesagte. Der Gegenstand des Anspruchs 1 nach Hilfsantrag
VIIa ist dem Fachmann somit ebenfalls ausgehend von Druckschrift D3 in
Kenntnis von Druckschrift D4 nahegelegt, sodass der Gegenstand des
Anspruchs 1 nach Hilfsantrag VIIa nicht auf einer erfinderischen Tätigkeit beruht.


17.    Zu Hilfsantrag VIII vom 27. Februar 2019


Hilfsantrag VIII ist ebenfalls nicht patentfähig.


Gegenüber Anspruch 1 gemäß Hilfsantrag VII wurde Anspruch 1 um folgende
weitere Merkmale ergänzt, welche vor Merkmal 11.5 eingeschoben sind:


      11.6     wobei     beim    Erzeugen        der    Navigationsdatei       ferner   für    ein
               Benutzeroberflächenobjekt             eines     Prozessschritts     über       eine
               Objekterkennungsschnittstelle                  des         Computerprogramms
               Objekteigenschaften         des     Benutzeroberflächenobjekts           ermittelt
               werden
      11.7     und [Objekteigenschaften] in der Navigationsdatei gespeichert
               werden,       wobei   die   Objekteigenschaften           den   Objekttyp       des
               Benutzeroberflächenobjekts umfassen


Das Merkmal 11.6 betrifft wiederum allein das Erzeugen der Navigationsdatei und
kann das Verfahren des Anspruchs 1, welches zur Unterstützung eines Benutzers
während      der   Bedienung     eines     Computerprogramms             dient, folglich      nicht
charakterisieren (vgl. u. a. die Ausführungen zu Anspruch 1 nach Hilfsantrag I vom
27. Februar 2019).     Mit     Merkmal      11.7       wird    angegeben,       dass    in     der
Navigationsdatei       Objekteigenschaften             des          Benutzeroberflächenobjekts
gespeichert werden und eine dieser Objekteigenschaften der Objekttyp des

                                        - 72 -



Benutzeroberflächenobjekts ist, worunter im Streitpatent beispielsweise ein
Eingabefeld oder eine Schaltfläche verstanden werden (vgl. Streitpatent,
Abs. 0060).


Bei dem aus Druckschrift D3 bekannten Verfahren wird in der entity map 345,
welche Teil der Navigationsdatei ist, unter anderem auch ein Typ für jedes Objekt
gespeichert (vgl. Abs. 0080: … basic type of entity (e.g. a window, button, toolbar,
or menu type entity) …), wie auch aus der nachfolgend wiedergegebenen Figur 3B
ersichtlich, welche die abgespeicherten Objekttypen Buttons und Menues nennt:




Damit enthält die aus Druckschrift D3 bekannte Navigationsdatei auch als
Objekteigenschaften den Objekttyp des Benutzeroberflächenobjekts gemäß
Merkmal 11.7. Zu den weiteren Merkmalen gilt das zum Hauptantrag und zu
Hilfsantrag VII Gesagte gleichermaßen.


Der Gegenstand des Anspruchs 1 nach Hilfsantrag VIII ist dem Fachmann somit
ebenfalls ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag VIII nicht
auf einer erfinderischen Tätigkeit beruht.


Darüber hinaus hat die Klägerin bezüglich Hilfsantrag VIII auch zur mangelnden
Ursprungsoffenbarung ausgeführt; die Beklagte hat zur Offenbarung verwiesen
auf die Absätze 0063 und 0064 des Streitpatents (welche identisch zu den
Absätzen 0063 und 0064 der Offenlegungsschrift sind). Die Klägerin hat
argumentiert, beide Absätze offenbarten nicht, dass als einzige Objekteigenschaft

                                       - 73 -



zu einem Benutzeroberflächenobjekt der Objekttyp in der Navigationsdatei
gespeichert werde, was von Anspruch 1 nach Hilfsantrag VIII jedoch umfasst sei.
Ob die Angabe einer Objekteigenschaft – im Singular – in Anspruch 1 eine
unzulässige Erweiterung darstellt, da in den ursprünglichen Unterlagen und im
Streitpatent allein offenbart ist, dass „die Objekteigenschaften“, sprich alle
Objekteigenschaften oder jedenfalls mehrere, bzw. Objekteigenschaften als Tupel
abgespeichert werden, kann jedoch dahingestellt bleiben, da der Gegenstand des
Anspruchs 1 nach Hilfsantrag VIII jedenfalls nicht auf einer erfinderischen Tätigkeit
beruht.


18.   Zu Hilfsantrag VIIIb


Hilfsantrag VIIIb besteht aus Hilfsantrag VIII vom 27. Februar 2019 mit der zu
Hilfsantrag 0 angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag VIII vom
27. Februar 2019 ebenfalls nicht das Merkmal M* enthält, und die hinzugefügten
Merkmale 11.1 bis 11.5, 1.1.3.1, 1.3.6, 12.1, 12.2. 11.6 und 11.7 keinen weiteren
Bezug zu Merkmal 1.2.3 oder einer Synchronisierung herstellen, gilt für den
Anspruch 1 gemäß Hilfsantrag VIIIb das zu Hilfsantrag 0 bzw. Hilfsantrag VIII vom
27. Februar 2019 Gesagte. Der Gegenstand des Anspruchs 1 nach Hilfsantrag
VIIIb ist dem Fachmann somit ebenfalls ausgehend von Druckschrift D3 in
Kenntnis von Druckschrift D4 nahegelegt, sodass der Gegenstand des
Anspruchs 1 nach Hilfsantrag VIIIb nicht auf einer erfinderischen Tätigkeit beruht.


19.   Zu Hilfsantrag VIIIa


Die in Anspruch 1 gemäß Hilfsantrag VIIIa vorgenommene Änderung kann die
Patentfähigkeit des beanspruchten Gegenstands ebenfalls nicht herstellen.


Anspruch 1 gemäß Hilfsantrag VIIIa unterscheidet sich von Anspruch 1 gemäß
Hilfsantrag VIII vom 27. Februar 2019 darin, dass Merkmal 12.2 wie folgt lautet:

                                       - 74 -



      12.2*   wobei die Informationen vorzugsweise ein Bild des zu bedienenden
              Benutzeroberflächenobjektes       und    einen     Beschreibungstext
              umfassen


Durch die Streichung des Wortes „vorzugsweise“ ist das Merkmal nun nicht mehr
fakultativ.


Ob dieses Merkmal, welches den Inhalt der dem Benutzer anzuzeigenden
Informationen als Bild oder Text festlegt, dem Patentschutz zugänglich ist oder als
nichttechnische Vorgabe bei der Prüfung auf erfinderische Tätigkeit außer
Betracht bleiben kann, wie die Klägerin ausgeführt hat, kann dahingestellt bleiben.
Denn aus Druckschrift D3 ist auch bereits bekannt, dem Benutzer während der
Bedienung eines Computerprogramms Informationen zu dem zu bedienenden
Benutzeroberflächenobjekt anzuzeigen (vgl. Abs. 0059: … instruct the user to
provide such interaction.; Abs. 00121; Abs. 00122: The partial graphical overlay
may include text, graphics, animation or video indicating to a user how to provide
input to the associated graphical user interface object of the computer program
346.), womit sowohl eine textliche Darstellung wie auch eine grafische Darstellung
mittels eines Bildes umfasst sind (vgl. auch die Fig. 12A - 12E / Merkmal 12.2*).
Da für die übrigen Merkmale das zu Hilfsantrag VIII vom 27. Februar 2019
Ausgeführte ebenso gilt, beruht auch der Gegenstand des Anspruchs 1 nach
Hilfsantrag VIIIa gegenüber dem Stand der Technik gemäß Druckschrift D3 in
Verbindung mit Druckschrift D4 nicht auf einer erfinderischen Tätigkeit.


20.    Zu Hilfsantrag VIIIc


Hilfsantrag VIIIc besteht aus Hilfsantrag VIIIa plus der zu Hilfsantrag 0
angegebenen Fußnote. Da der Anspruch 1 von Hilfsantrag VIIIa ebenfalls nicht
das Merkmal M* enthält, und die hinzugefügten Merkmale 11.1 bis 11.5, 1.1.3.1,
1.3.6, 12.1, 12.2* und 11.6, 11.7 keinen weiteren Bezug zu Merkmal 1.2.3 oder
einer Synchronisierung herstellen, gilt für den Anspruch 1 gemäß Hilfsantrag VIIIc
das zu Hilfsantrag 0 bzw. Hilfsantrag VIIIa vom 27. Februar 2019 Gesagte. Der

                                        - 75 -



Gegenstand des Anspruchs 1 nach Hilfsantrag VIIIc ist dem Fachmann somit
ebenfalls ausgehend von Druckschrift D3 in Kenntnis von Druckschrift D4
nahegelegt, sodass der Gegenstand des Anspruchs 1 nach Hilfsantrag VIIIc nicht
auf einer erfinderischen Tätigkeit beruht.


21.   Mit den nicht patentfähigen jeweiligen Ansprüchen 1 nach Hauptantrag und
nach den 27 Hilfsanträgen sind auch die abhängigen, auf die jeweiligen
Ansprüche 1 direkt oder indirekt rückbezogenen Ansprüche des Hauptantrags und
der Hilfsanträge, soweit sie von der Klage angegriffen sind, nicht schutzfähig, da
weder geltend gemacht noch sonst ersichtlich ist, dass die in ihnen enthaltenen
zusätzlichen Merkmale zu einer anderen Beurteilung der Patentfähigkeit führen
(vgl. BGH, Urteil vom 29. September 2011 – X ZR 109/08, BlPMZ 2012, 64,
Leitsatz – Sensoranordnung).


Da sich somit das Streitpatent im angegriffenen Umfang weder in der erteilten
Fassung noch in der Fassung der Hilfsanträge als patentfähig erweist, war das
Streitpatent in diesem mit der Klage geltend gemachten Umfang für nichtig zu
erklären.




                          B.     Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO, die
Entscheidung über die vorläufige Vollstreckbarkeit auf § 99 Abs. 1 PatG i. V. m.
§ 709 ZPO.

                                       - 76 -



                                        C.

                       Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die Berufungsschrift muss innerhalb eines Monats schriftlich beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als elektronisches
Dokument nach Maßgabe der Verordnung über den elektronischen Rechtsverkehr
beim Bundesgerichtshof und Bundespatentgericht (BGH/BPatGERVV) vom
24. August 2007 (BGBl. I S. 2130) in die elektronische Poststelle des Bundesgerichtshofes (www.bundesgerichtshof.de/erv.html) übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in vollständiger Form abgefassten Urteils,
spätestens aber mit dem Ablauf von fünf Monaten nach der Verkündung. Die Frist
ist nur gewahrt, wenn die Berufung vor Fristablauf eingeht.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen elektronischen Signatur versehen sein, die von einer internationalen Organisation auf
dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich zur
Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung
enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der Berufungsschrift soll eine Ausfertigung oder beglaubigte Abschrift des angefochtenen Urteils
vorgelegt werden.



Friehe       Dr. Schwengelbeck     Jacobi       Dr. Otten-Dünnweber       Altvater

                                                                                prö
