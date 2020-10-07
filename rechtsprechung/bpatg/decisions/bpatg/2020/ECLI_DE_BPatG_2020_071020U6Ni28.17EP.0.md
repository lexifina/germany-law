---
ecli: "ECLI:DE:BPatG:2020:071020U6Ni28.17EP.0"
court: "Bundespatentgericht"
spruchkoerper: "6"
aktenzeichen: "6 Ni 28/17"
decided: "2020-10-07"
typ: "U"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2020&Sort=1&Seite=34&nr=40435&anz=666&pos=522&Blank=1.pdf"
corpus_doc_id: "BPatG_Nichtigkeit_NA_2020-10-07_6_Ni_28_17_EP_0.txt"
cites_law: ["germany/bund/acts/patg/0084.md", "germany/bund/acts/patg/0099.md", "germany/bund/acts/zpo/0091.md", "germany/bund/acts/zpo/0709.md"]
---

# Bundespatentgericht, 6 Ni 28/17 vom 2020-10-07

## Entscheidung

BUNDESPATENTGERICHT

                        IM NAMEN DES VOLKES

                                    URTEIL
                                                           Verkündet am
                                                          7. Oktober 2020
6 Ni 28/17 (EP)                                                  …

(Aktenzeichen)


                         In der Patentnichtigkeitssache

…




ECLI:DE:BPatG:2020:071020U6Ni28.17EP.0

                                           -2-



                   betreffend das europäische Patent 2 538 323
                                 (DE 50 2012 002 017)


hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der
mündlichen Verhandlung vom 7. Oktober 2020 durch die Vorsitzende Richterin
Friehe, die Richterin Werner und die Richter Dipl.-Phys. Dr. Schwengelbeck,
Dipl.-Ing. Altvater sowie Dr.-Ing. Flaschke


für Recht erkannt:


        I.     Das Europäische Patent 2 538 323 wird im Umfang der
               Ansprüche 1, 10, 11, 12, 13 und 14 mit Wirkung für das
               Hoheitsgebiet der Bundesrepublik Deutschland für nichtig
               erklärt.


        II.    Die Kosten des Rechtstreits hat die Beklagte zu tragen.


        III.   Das Urteil ist gegen Sicherheitsleistung in Höhe von 110 %
               des zu vollstreckenden Betrages vorläufig vollstreckbar.



                                   Tatbestand


Die Beklagte ist eingetragene Inhaberin des aufgrund der Anmeldung vom
21. Juni 2012 unter Inanspruchnahme der Priorität der europäischen Anmeldung
11171107 vom 22. Juni 2011 auch mit Wirkung für das Hoheitsgebiet der
Bundesrepublik      Deutschland     erteilten    europäischen   Patents   2   538   323
(Streitpatent). Das Streitpatent ist in Kraft.


Das beim Deutschen Patent- und Markenamt unter dem Aktenzeichen
50 2012 002 017 geführte Streitpatent trägt die Bezeichnung

                                          -3-



                  „Verfahren und System zur Unterstützung einer
                     Bedienung eines Computerprogramms“


und umfasst in der erteilten Fassung vierzehn Patentansprüche, die die Klägerin mit
der am      16. August 2017    eingereichten Nichtigkeitsklage            im   Umfang der
Patentansprüche 1, 10, 11, 12, 13 und 14 angreift.


Die angegriffenen nebengeordneten Patentansprüche 1, 13 und 14 lauten:

 1. Computer-implementiertes Verfahren zur Unterstützung eines Benutzers
     während      einer     Bedienung      zumindest        eines         vorbestimmten
     Computerprogramms,         wobei      während         der         Ausführung    des
     Computerprogramms        zumindest    ein   Benutzeroberflächenobjekt           des
     Computerprogramms auf einer Anzeigeeinrichtung zur Anzeige gebracht
     wird, wobei die Bedienung des Computerprogramms eine Anzahl
     auszuführender Prozessschritte umfasst, wobei jeder Prozessschritt durch
     eine    vorbestimmte     Benutzerinteraktion    mit     einem        vorbestimmten
     Benutzeroberflächenobjekt (BOO) in einem vorbestimmten Kontext des
     Computerprogramms repräsentiert wird, wobei eine Navigationsdatei die für
     die      Bedienung        des        Computerprogramms                erforderlichen
     Benutzerinteraktionen mit dem Computerprogramm enthält, wobei die
     Benutzerinteraktionen     als   Prozessschritte   in        der     Navigationsdatei
     gespeichert sind, und wobei für zumindest einen in der Navigationsdatei
     gespeicherten Prozessschritt

     - der zumindest eine gespeicherte Prozessschritt geladen wird (S0; S9),
     - der aktuelle Kontext des Computerprogramms ermittelt wird (S1),
     - geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
        Kontext des geladenen Prozessschrittes übereinstimmt (S2),
     - falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
        geladenen Prozessschrittes übereinstimmt, das an der Anzeigeeinrichtung
        angezeigte Benutzeroberflächenobjekt des Computerprogramms ermittelt

                                     -4-



    wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen
    Prozessschrittes entspricht (S4),
und
- das ermittelte Benutzeroberflächenobjekt (BOO) des Computerprogramms
    auf der Anzeigeeinrichtung für den Benutzer hervorgehoben wird (S6),
dadurch gekennzeichnet, dass
das    angezeigte    Benutzeroberflächenobjekt        des    Computerprogramms,
welches      dem     Benutzeroberflächenobjekt        (BOO)         des     geladenen
Prozessschrittes entspricht, ermittelt wird, indem
-   für alle dem aktuellen Kontext des Computerprogramms zugeordneten
    Benutzeroberflächenobjekte

    - ermittelt     wird,    ob      der      Objekttyp        des         angezeigten
      Benutzeroberflächenobjektes       des   Computerprogramms              mit   dem
      Objekttyp des Benutzeroberflächenobjektes (BOO) des geladenen
      Prozessschrittes übereinstimmt (S4.1),
    - falls die Objekttypen übereinstimmen, ein Übereinstimmungswert (ÜW)
      für das angezeigte Benutzeroberflächenobjekt des Computerprogramms
      ermittelt wird (S4.2), wobei der Übereinstimmungswert (ÜW) für ein
      Benutzeroberflächenobjekt auf Basis der Objekteigenschaften (OE) des
      Benutzeroberflächenobjektes          bestimmt         wird,         wobei    die
      Objekteigenschaften (OE) des über die Objekterkennungsschnittstelle
      abgefragten      Benutzeroberflächenobjektes           (BOO)          mit    den
      entsprechenden              Objekteigenschaften               (OE)           des
      Benutzeroberflächenobjektes (BOO) des geladenen Prozessschrittes
      verglichen und bewertet werden und das Benutzeroberflächenobjekt des
      Computerprogramms zusammen mit dem Übereinstimmungswert (ÜW)
      in einer Ergebnisliste (EL) abgespeichert wird (S4.3), und
    - jenes Benutzeroberflächenobjekt aus der Ergebnisliste (EL) ausgewählt
      wird, welches ein vorbestimmtes Auswahlkriterium erfüllt (S4.4).

                                        -5-



 13. System zur Unterstützung eines Benutzers während einer Bedienung
     zumindest eines vorbestimmten Computerprogramms, wobei das System
     Mittel zum Ausführen des Computerprogramms, eine Anzeigeeinrichtung
     zur Anzeige des sich in Ausführung befindlichen Computerprogramms,
     Eingabemittel    zur     Entgegennahme      von    Benutzereingaben,      und
     Navigationsmittel, welche angepasst sind, ein Verfahren nach einem der
     vorhergehenden         Ansprüche   auszuführen,      umfasst,    wobei     die
     Navigationsmittel über zumindest eine Objekterkennungsschnittstelle mit
     dem Computerprogramm koppelbar sind, um das Computerprogramm
     entsprechend der in der Navigationsdatei gespeicherten Prozessschritte zu
     überwachen und zu steuern.


 14. Computerprogrammprodukt mit Programmcode, welcher, wenn in eine
     Datenverarbeitungsanlage geladen, das Verfahren gemäß einem der
     Ansprüche 1 bis 12 zur Ausführung bringt.


Die ebenfalls angegriffenen Patentansprüche 10, 11 und 12 sind auf
Patentanspruch 1 unmittelbar oder mittelbar rückbezogen.


Die Klägerin ist der Ansicht, das Streitpatent sei mangels Patentfähigkeit für nichtig
zu erklären. Dies stützt sie unter anderem auf die Druckschriften (Nummerierung
und Kurzzeichen nach Klageschriftsatz):
     D1     Apple Computer Inc.: „Apple Guide Complete: Designing and
            Developing Onscreen Assistance“; Addison-Wesley, Februar
            1995, ISBN: 0-201-48334-3 und

     D7     DE 10 2008 028 581 A1.


Mit Schriftsatz vom 18. Juli 2018 macht sie darüber hinaus den Nichtigkeitsgrund
der unzulässigen Erweiterung geltend sowie den Patentierungsausschluss nach
Art. 52 Abs. 2 und 3 EPÜ hinsichtlich der Patentansprüche 1, 10, 11 und 12.

                                        -6-



Die Klägerin beantragt,

       das europäische Patent 2 538 323 im Umfang der Ansprüche 1, 10,
       11, 12, 13 und 14 mit Wirkung für das Hoheitsgebiet der
       Bundesrepublik Deutschland für nichtig zu erklären.


Die Beklagte beantragt,

       die Klage abzuweisen,

       hilfsweise die Klage abzuweisen, soweit sie sich auch gegen eine
       der Fassungen des Streitpatents richtet nach den Hilfsanträgen 1
       bis 7 und 8 bis 15 aus dem Schriftsatz vom 13. Februar 2020, sowie
       nach den Hilfsanträgen 16 und 17 aus dem Schriftsatz vom
       12. August 2020, in dieser Reihenfolge.


Die Beklagte tritt der Argumentation der Klägerin entgegen und hält den
Gegenstand des Streitpatents in der erteilten Fassung oder wenigstens in einer der
verteidigten Fassungen für schutzfähig.


Der jeweilige Patentanspruch 1 nach den Hilfsanträgen, aufgeführt in der
beantragten Reihenfolge, hat folgenden Inhalt:


Der Patentanspruch 1 nach Hilfsantrag 1 umfasst zusätzlich zum Anspruch 1
gemäß Hauptantrag die Definition eines Benutzeroberflächenobjekts und lautet
unter Hervorhebung der Änderungen:


1. Computer-implementiertes Verfahren zur Unterstützung eines Benutzers
    während      einer    Bedienung        zumindest     eines     vorbestimmten
    Computerprogramms,         wobei      während      der    Ausführung      des
    Computerprogramms       zumindest     ein    Benutzeroberflächenobjekt    des
    Computerprogramms auf einer Anzeigeeinrichtung zur Anzeige gebracht wird,

                                       -7-



wobei die Bedienung des Computerprogramms eine Anzahl auszuführender
Prozessschritte umfasst, wobei jeder Prozessschritt durch eine vorbestimmte
Benutzerinteraktion mit einem vorbestimmten Benutzeroberflächenobjekt
(BOO) in einem vorbestimmten Kontext des Computerprogramms repräsentiert
wird,    wobei      ein    Benutzeroberflächenobjekt    ein    Objekt     an   einer
Benutzeroberfläche des Computerprogramms ist, über welches der Benutzer
mit dem Computerprogramm interagieren kann, wobei eine Navigationsdatei
die     für   die     Bedienung      des     Computerprogramms         erforderlichen
Benutzerinteraktionen mit dem Computerprogramm enthält, wobei die
Benutzerinteraktionen als Prozessschritte in der Navigationsdatei gespeichert
sind, und wobei für zumindest einen in der Navigationsdatei gespeicherten
Prozessschritt

 - der zumindest eine gespeicherte Prozessschritt geladen wird (S0; S9),

 - der aktuelle Kontext des Computerprogramms ermittelt wird (S1),

 - geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
      Kontext des geladenen Prozessschrittes übereinstimmt (S2),

 - falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
      geladenen Prozessschrittes übereinstimmt, das an der Anzeigeeinrichtung
      angezeigte Benutzeroberflächenobjekt des Computerprogramms ermittelt
      wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen
      Prozessschrittes entspricht (S4), und

 - das ermittelte Benutzeroberflächenobjekt (BOO) des Computerprogramms
      auf der Anzeigeeinrichtung für den Benutzer hervorgehoben wird (S6),

 dadurch gekennzeichnet, dass

 das     angezeigte       Benutzeroberflächenobjekt    des    Computerprogramms,
 welches      dem         Benutzeroberflächenobjekt    (BOO)     des      geladenen
 Prozessschrittes entspricht, ermittelt wird, indem
 - für alle dem aktuellen Kontext des Computerprogramms zugeordneten
      Benutzeroberflächenobjekte

                                               -8-



     - ermittelt      wird,         ob         der      Objekttyp        des      angezeigten
        Benutzeroberflächenobjektes des Computerprogramms mit dem Objekttyp
        des Benutzeroberflächenobjektes (BOO) des geladenen Prozessschrittes
        übereinstimmt (S4.1),

     - falls die Objekttypen übereinstimmen, ein Übereinstimmungswert (ÜW) für
        das angezeigte Benutzeroberflächenobjekt des Computerprogramms
        ermittelt wird (S4.2), wobei der Übereinstimmungswert (ÜW) für ein
        Benutzeroberflächenobjekt auf Basis der Objekteigenschaften (OE) des
        Benutzeroberflächenobjektes                  bestimmt       wird,       wobei      die
        Objekteigenschaften (OE) des über die Objekterkennungsschnittstelle
        abgefragten Benutzeroberflächenobjektes (BOO) mit den entsprechenden
        Objekteigenschaften (OE) des Benutzeroberflächenobjektes (BOO) des
        geladenen Prozessschrittes verglichen und bewertet werden und das
        Benutzeroberflächenobjekt des Computerprogramms zusammen mit dem
        Übereinstimmungswert (ÜW) in einer Ergebnisliste (EL) abgespeichert wird
        (S4.3), und

     - jenes Benutzeroberflächenobjekt aus der Ergebnisliste (EL) ausgewählt
        wird, welches ein vorbestimmtes Auswahlkriterium erfüllt (S4.4).



Patentanspruch 1 nach Hilfsantrag 2 präzisiert die in Hilfsantrag 1 ergänzte
Definition   um       die     Art        der     möglichen       Interaktion     mit    einem
Benutzeroberflächenobjekt.      Das        Merkmal      lautet   unter      Hervorhebung   der
Ergänzung:

  wobei ein Benutzeroberflächenobjekt ein Objekt an einer Benutzeroberfläche des
  Computerprogramms ist, über welches der Benutzer über ein Eingabegerät mit
  dem Computerprogramm interagieren kann,


Patentanspruch 1 nach Hilfsantrag 3 umfasst zusätzlich zu den Merkmalen des
Hilfsantrags 2 die folgenden hervorgehobenen Ergänzungen:

                                         -9-



     (…) und das Benutzeroberflächenobjekt des Computerprogramms zusammen
     mit dem Übereinstimmungswert (ÜW) in einer absteigend sortierten
     Ergebnisliste (EL) abgespeichert wird (S4.3), und
 -   jenes Benutzeroberflächenobjekt aus der Ergebnisliste (EL) ausgewählt wird,
     welches ein vorbestimmtes Auswahlkriterium erfüllt (S4.4), wobei das
     vorbestimmte      Auswahlkriterium       darin     besteht,     dass      das     erste
     Benutzeroberflächenobjekt der Ergebnisliste ausgewählt wird.


Patentanspruch 1 nach Hilfsantrag 4 umfasst zusätzlich zu den Merkmalen des
Hilfsantrags 2 die Spezifizierung der Navigationsdatei und des Kontextes:

  wobei die Navigationsdatei mit einem Aufzeichnungsmittel auf einer ersten
  Datenverarbeitungseinrichtung       erzeugt    wird     und      das   zu    bedienende
  Computerprogramm auf einer zweiten Datenverarbeitungseinrichtung ausgeführt
  wird,

  wobei die Navigationsdatei vor dem Ermitteln (S1) des aktuellen Kontextes des
  Computerprogramms           in      einen      Arbeitsspeicher         der         zweiten
  Datenverarbeitungseinrichtung geladen wird,

  wobei    die    Navigationsdatei    erzeugt    wird     durch     Verwendung         eines
  Aufzeichnungsverfahrens, bei welchem die Benutzerinteraktionen auf der ersten
  Datenverarbeitungseinrichtung durch einen Benutzer durchgeführt werden und
  jeweils die Benutzerinteraktion, der Kontext und das Benutzeroberflächenobjekt
  als Prozessschritte in der Navigationsdatei gespeichert werden,

  wobei     der     Kontext    eine     vorbestimmte         Benutzeroberfläche         des
  Computerprogramms in einem vorbestimmten Zustand kennzeichnet.

Patentanspruch 1 nach Hilfsantrag 5 umfasst zusätzlich zu den Merkmalen des
Hilfsantrags 2 eine Konkretisierung der Unterstützung:

  wobei das Verfahren einen Schritt (S3) zum Anzeigen von Informationen zu der
  von     dem     Benutzer    durchzuführenden          Benutzerinteraktion      auf     der
  Anzeigeeinrichtung umfasst, wobei die Informationen vorzugsweise ein Bild des

                                      - 10 -



  zu bedienenden Benutzeroberflächenobjektes und einen Beschreibungstext
  umfassen.


Patentanspruch 1 nach Hilfsantrag 6 ist eine Kombination der Hilfsanträge 3, 4 und
5 und lautet unter Hervorhebung der gegenüber dem Hauptantrag ergänzten
Merkmale:

1. Computer-implementiertes Verfahren zur Unterstützung eines Benutzers
   während einer Bedienung zumindest eines vorbestimmten Computerprogramms, wobei während der Ausführung des Computerprogramms
   zumindest ein Benutzeroberflächenobjekt des Computerprogramms auf einer
   Anzeigeeinrichtung zur Anzeige gebracht wird, wobei die Bedienung des
   Computerprogramms eine Anzahl auszuführender Prozessschritte umfasst,
   wobei jeder Prozessschritt durch eine vorbestimmte Benutzerinteraktion mit
   einem vorbestimmten Benutzeroberflächenobjekt (BOO) in einem vorbestimmten Kontext des Computerprogramms repräsentiert wird, wobei ein
   Benutzeroberflächenobjekt ein Objekt an einer Benutzeroberfläche des
   Computerprogramms        ist,   über   welches    der   Benutzer    mit   dem
   Computerprogramm interagieren kann, wobei eine Navigationsdatei die für die
   Bedienung des Computerprogramms erforderlichen Benutzerinteraktionen mit
   dem Computerprogramm enthält, wobei die Benutzerinteraktionen als
   Prozessschritte in der Navigationsdatei gespeichert sind, und wobei für
   zumindest einen in der Navigationsdatei gespeicherten Prozessschritt

     - der zumindest eine gespeicherte Prozessschritt geladen wird (S0; S9),

     - der aktuelle Kontext des Computerprogramms ermittelt wird (S1),

     - geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
       Kontext des geladenen Prozessschrittes übereinstimmt (S2),

     - falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
       geladenen Prozessschrittes übereinstimmt, das an der Anzeigeeinrichtung
       angezeigte Benutzeroberflächenobjekt des Computerprogramms ermittelt

                                   - 11 -



  wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen
  Prozessschrittes entspricht (S4), und

- das ermittelte Benutzeroberflächenobjekt (BOO) des Computerprogramms
  auf der Anzeigeeinrichtung für den Benutzer hervorgehoben wird (S6),

dadurch gekennzeichnet, dass

das   angezeigte      Benutzeroberflächenobjekt        des     Computerprogramms,
welches dem Benutzeroberflächenobjekt (BOO) des geladenen Prozessschrittes entspricht, ermittelt wird, indem

- für alle dem aktuellen Kontext des Computerprogramms zugeordneten
  Benutzeroberflächenobjekte

- ermittelt   wird,    ob    der   Objekttyp        des      angezeigten     Benutzeroberflächenobjektes des Computerprogramms mit dem Objekttyp des
  Benutzeroberflächenobjektes (BOO) des geladenen Prozessschrittes
  übereinstimmt (S4.1),

- falls die Objekttypen übereinstimmen, ein Übereinstimmungswert (ÜW) für
  das angezeigte Benutzeroberflächenobjekt des Computerprogramms
  ermittelt wird (S4.2), wobei der Übereinstimmungswert (ÜW) für ein
  Benutzeroberflächenobjekt auf Basis der Objekteigenschaften (OE) des
  Benutzeroberflächenobjektes        bestimmt        wird,     wobei   die     Objekteigenschaften       (OE)   des    über      die    Objekterkennungsschnittstelle
  abgefragten Benutzeroberflächenobjektes (BOO) mit den entsprechenden
  Objekteigenschaften (OE) des Benutzeroberflächenobjektes (BOO) des
  geladenen Prozessschrittes verglichen und bewertet werden und das
  Benutzeroberflächenobjekt des Computerprogramms zusammen mit dem
  Übereinstimmungswert (ÜW) in einer absteigend sortierten Ergebnisliste
  (EL) abgespeichert wird (S4.3), und

- jenes Benutzeroberflächenobjekt aus der Ergebnisliste (EL) ausgewählt
  wird, welches ein vorbestimmtes Auswahlkriterium erfüllt (S4.4), wobei das

                                        - 12 -



       vorbestimmte Auswahlkriterium darin besteht, dass das erste Benutzeroberflächenobjekt der Ergebnisliste ausgewählt wird,

       wobei das Verfahren einen Schritt (S3) zum Anzeigen von Informationen zu
       der von dem Benutzer durchzuführenden Benutzerinteraktion auf der
       Anzeigeeinrichtung umfasst, wobei die Informationen vorzugsweise ein Bild
       des     zu     bedienenden   Benutzeroberflächenobjektes          und     einen
       Beschreibungstext umfassen,

       wobei die Navigationsdatei mit einem Aufzeichnungsmittel auf einer ersten
       Datenverarbeitungseinrichtung erzeugt wird und das zu bedienende
       Computerprogramm auf einer zweiten Datenverarbeitungseinrichtung
       ausgeführt wird,

       wobei die Navigationsdatei vor dem Ermitteln (S1) des aktuellen Kontextes
       des     Computerprogramms        in     einen   Arbeitsspeicher   der   zweiten
       Datenverarbeitungseinrichtung geladen wird,

       wobei die Navigationsdatei erzeugt wird durch Verwendung eines
       Aufzeichnungsverfahrens, bei welchem die Benutzerinteraktionen auf der
       ersten Datenverarbeitungseinrichtung durch einen Benutzer durchgeführt
       werden und jeweils die Benutzerinteraktion, der Kontext und das
       Benutzeroberflächenobjekt als Prozessschritte in der Navigationsdatei
       gespeichert werden,

       wobei    der    Kontext   eine        vorbestimmte   Benutzeroberfläche    des
       Computerprogramms in einem vorbestimmten Zustand kennzeichnet.


Hilfsantrag 7 umfasst bei Streichung der Ansprüche 5 und 12 aus Konsistenzgründen in Patentanspruch 1 zusätzlich zu den Merkmalen der Hilfsanträge 3
und 4 die folgende hervorgehobene Ergänzung:

     - geprüft wird, ob sich das ermittelte Benutzeroberflächenobjekt (BOO)
       bereits in dem erwarteten Zustand befindet, welcher durch die dem
       aktuellen Prozessschritt zugeordnete Benutzerinteraktion herbeigeführt

                                           - 13 -



          werden soll, und nur, wenn die Prüfung ergibt, dass sich das ermittelte
          Benutzeroberflächenobjekt (BOO) nicht in dem erwarteten Zustand
          befindet,   das     ermittelte   Benutzeroberflächenobjekt    (BOO)     des
          Computerprogramms auf der Anzeigeeinrichtung für den Benutzer
          hervorgehoben wird (S6),


Die Hilfsanträge 8 bis 15 gelten für den Fall, dass das Gericht in der Beschränkung
des Anspruchs 1 durch das Merkmal 1.2.3 und durch die Bedingung in Merkmal
1.2.4 eine unzulässige Erweiterung erkennen sollte, und beinhalten, das
Streitpatent im Umfang des Hauptantrages oder eines der Hilfsanträge 1 bis 7
aufrechtzuerhalten mit der Maßgabe, dass aus dem Schritt der Überprüfung des
Kontextes und dem positiven Ergebnis hierbei in Anspruch 1 keine Rechte
hergeleitet werden, also folgende Merkmale bei der Frage der Validität des
Streitpatents unberücksichtigt bleiben:

 -     geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
       Kontext des geladenen Prozessschrittes übereinstimmt (S2),
 -     falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
       geladenen Prozessschrittes übereinstimmt,
               (Disclaimer)


Patentanspruch 1 nach Hilfsantrag 16 basiert auf Hilfsantrag 7 und enthält neben
der Definition des Schrittes S3 entsprechend Hilfsantrag 5 zusätzlich die folgende
hervorgehobene Beschränkung:

     wobei die Navigationsdatei während der Bedienung des Computerprogrammes
     auf Anforderung durch den Benutzer zunächst in einem Initialisierungsschritt (S0)
     vor dem Ermitteln (S1) des aktuellen Kontextes des Computerprogramms in
     einen Arbeitsspeicher der zweiten Datenverarbeitungseinrichtung geladen wird,

                                          - 14 -



Als Hilfsantrag 17 wird beantragt, das Streitpatent im Umfang des Hilfsantrags 16
aufrechtzuerhalten mit der Maßgabe, dass aus dem Schritt der Überprüfung des
Kontextes und dem positiven Ergebnis hierbei in Anspruch 1 keine Rechte
hergeleitet werden, also folgende Merkmale bei der Frage der Validität des
Streitpatents unberücksichtigt bleiben:

 -   geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
     Kontext des geladenen Prozessschrittes übereinstimmt (S2),
 -   falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
     geladenen Prozessschrittes übereinstimmt,
               (Disclaimer)


Wegen des weiteren Wortlauts der übrigen Patentansprüche nach den
Hilfsanträgen 1 bis 17 wird auf die Akte verwiesen.


Die Klägerin hält die Hilfsanträge bereits für unzulässig, soweit sie den nicht
angegriffenen Unteranspruch 5 aufnehmen, und im Übrigen jedenfalls für nicht
patentfähig.


Der Senat hat den Parteien einen qualifizierten Hinweis zugeleitet und hierin Fristen
zur Stellungnahme auf den Hinweis und auf etwaiges Vorbringen der jeweiligen
Gegenpartei gesetzt.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt verwiesen.




                         Entscheidungsgründe


Die zulässige Klage ist begründet.


Das Streitpatent ist im angegriffenen Umfang für nichtig zu erklären, weil ihm in
sämtlichen Anspruchsfassungen, soweit sie zulässig sind, der Nichtigkeitsgrund der

                                       - 15 -



mangelnden Patentfähigkeit entgegensteht (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. a), Art. 52 bis 57 EPÜ).


                                         A.


                   I.     Zum Gegenstand des Streitpatents

1.    Die Erfindung betrifft ausweislich Absatz 0001 der Streitpatentschrift
(EP 2 538 323 B1) ein Verfahren und ein System zur Unterstützung eines
Benutzers    während     einer   Bedienung      zumindest     eines   vorbestimmten
Computerprogramms, wobei während der Ausführung des Computerprogramms
zumindest ein Benutzeroberflächenobjekt des Computerprogramms auf einer
Anzeigeeinrichtung zur Anzeige gebracht wird und wobei die Bedienung des
Computerprogramms eine Anzahl auszuführender Prozessschritte umfasst.


Zum technischen Hintergrund der Erfindung führt die Streitpatentschrift u. a. aus
(vgl. Absätze 0002 bis 0005):


Zur   Unterstützung     eines    Benutzers      während     der   Bedienung   eines
Computerprogramms oder zum Erlernen eines Computerprogramms sei es
bekannt, dem Benutzer ein Handbuch zur Verfügung zu stellen. Das Handbuch
könne als gedrucktes Handbuch oder als elektronisches Handbuch, etwa in Form
einer in dem Computerprogramm integrierten Hilfe bereitgestellt werden.
Elektronische Handbücher hätten dabei den Vorteil, dass bei Anforderung der Hilfe,
etwa durch Drücken einer Taste, das Computerprogramm automatisch den Hilfetext
aus dem elektronischen Handbuch zur Anzeige bringen könne, welcher dem
Programmkontext, in dem sich das Computerprogramm befinde, zugeordnet sei.
Von Nachteil sei dabei, dass bei jedem Wechsel des Programmkontextes, etwa
wenn eine neue Bildschirmmaske aufgerufen werde, die Hilfe durch den Benutzer
erneut angefordert werden müsse, um den korrekten Hilfetext zur Anzeige zu

                                            - 16 -



bringen. Auch sei eine interaktive Benutzerführung durch das Computerprogramm
nicht möglich.


Zur Unterstützung einer Benutzerführung durch ein Computerprogramm sei es
ferner    bekannt,     während        der    Bedienung     des      Computerprogramms
Bildschirmobjekte, sogenannte Benutzeroberflächenobjekte, hervorzuheben, um
dem Benutzer zu signalisieren, mit welchem Benutzeroberflächenobjekt eine
Interaktion zu erfolgen habe. Die Unterstützung könne auch in diesem Fall etwa
durch    Drücken     einer    Taste   angefordert    werden.      Das   hervorzuhebende
Benutzeroberflächenobjekt       werde       anhand   vorbestimmter      Bezugsmerkmale
lokalisiert, etwa anhand der Position des Benutzeroberflächenobjektes in der
Bildschirmmaske und/oder in einer Liste von Benutzeroberflächenobjekten.


Diese Form der Unterstützung habe allerdings den Nachteil, dass ein
entsprechendes Benutzeroberflächenobjekt nur dann korrekt hervorgehoben
werden könne, wenn sich die Bezugsmerkmale nicht änderten. Ändere sich
beispielsweise die Reihenfolge der Benutzeroberflächenobjekte in der Liste von
Benutzeroberflächenobjekten, wenn etwa das Computerprogramm von einem
Entwicklungssystem auf ein Produktivsystem portiert werde, könne dies dazu
führen, dass ein falsches Benutzeroberflächenobjekt aus der Liste ausgewählt und
hervorgehoben        werde,    was     wiederum      zu   einer    Fehlbedienung   des
Computerprogramms durch den Benutzer führen könne. Ein weiterer Nachteil
bestehe darin, dass diese Art der Benutzerführung nicht kontextübergreifend
funktioniere, sodass der Benutzer bei jedem Wechsel des Kontextes des
Computerprogramms, etwa beim Wechsel von einer Eingabemaske zur nächsten
Eingabemaske, die Unterstützung erneut anfordern müsse.


Das Streitpatent nennt als Aufgabe (vgl. Streitpatentschrift, Abs. 0006), ein
Verfahren und ein System zur Unterstützung eines Benutzers während einer
Bedienung eines Computerprogramms bereitzustellen, welche es erlauben,
während der Ausführung des Computerprogramms kontextübergreifend ein

                                       - 17 -



Benutzeroberflächenobjekt     des    Computerprogramms       entsprechend   einem
vorbestimmten Programmablauf auch bei sich ändernden Bezugsmerkmalen des
Benutzeroberflächenobjektes auf einer Anzeigeeinrichtung hervorzuheben. Die
genannte Aufgabe entspricht nach dem Verständnis des Senats auch der objektiven
Problemstellung.


Als zuständigen Fachmann sieht der Senat einen Ingenieur der Informationstechnik
mit Hochschulabschluss, der als Systementwickler oder Programmierer über
Berufserfahrung in der Entwicklung von Hilfesystemen verfügt.


2.      Die Aufgabe soll durch ein Verfahren und ein System zur Unterstützung eines
Benutzers während einer Bedienung eines Computerprogramms insbesondere
gemäß den unabhängigen Ansprüchen gelöst werden (vgl. Streitpatent, Abs. 0007).


Patentanspruch 1 betrifft ein Computer-implementiertes Verfahren, Patentanspruch
13 ein System, welches auf einen der Verfahrensansprüche rückbezogen ist und
Anspruch 14 ein Computerprogrammprodukt, welches ebenfalls auf einen der
Verfahrensansprüche rückbezogen ist. Die weiteren mit der Klage angegriffenen
Ansprüche 10, 11 und 12 sind auf den Verfahrens-anspruch 1 unmittelbar oder
mittelbar rückbezogene Unteransprüche.


Patentanspruch 1 in der Fassung des Hauptantrags (erteilter Anspruch 1) kann
dabei wie folgt gegliedert werden:


1.1      Computer-implementiertes Verfahren zur Unterstützung eines Benutzers
         während     einer    Bedienung         zumindest   eines   vorbestimmten
         Computerprogramms,
1.1.1    wobei während der Ausführung des Computerprogramms zumindest ein
         Benutzeroberflächenobjekt des Computerprogramms auf einer             Anzeigeeinrichtung zur Anzeige gebracht wird,

                                       - 18 -



1.1.2   wobei    die     Bedienung    des   Computerprogramms       eine      Anzahl
        auszuführender Prozessschritte umfasst,
1.1.3   wobei jeder Prozessschritt durch eine vorbestimmte Benutzerinteraktion mit
        einem    vorbestimmten     Benutzeroberflächenobjekt     (BOO)   in   einem
        vorbestimmten Kontext des Computerprogramms repräsentiert wird,
1.1.4   wobei eine Navigationsdatei die für die Bedienung des Computerprogramms erforderlichen Benutzerinteraktionen mit dem Computerprogramm enthält,
1.1.5   wobei die Benutzerinteraktionen als Prozessschritte in der Navigationsdatei gespeichert sind, und

1.2     wobei für zumindest einen in der Navigationsdatei gespeicherten
        Prozessschritt
1.2.1   - der zumindest eine gespeicherte Prozessschritt geladen wird (S0; S9),
1.2.2   - der aktuelle Kontext des Computerprogramms ermittelt wird (S1),
1.2.3   - geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
        Kontext des geladenen Prozessschrittes übereinstimmt (S2),
1.2.4   - falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
        geladenen Prozessschrittes übereinstimmt, das an der Anzeigeeinrichtung
        angezeigte Benutzeroberflächenobjekt des Computerprogramms ermittelt
        wird, welches dem Benutzeroberflächenobjekt (BOO) des geladenen
        Prozessschrittes entspricht (S4), und
1.2.5   - das   ermittelte   Benutzeroberflächenobjekt   (BOO)    des    Computerprogramms auf der Anzeigeeinrichtung für den Benutzer hervorgehoben
        wird (S6),

                                                - 19 -



        dadurch gekennzeichnet, dass

1.3     das angezeigte Benutzeroberflächenobjekt des Computerprogramms,
        welches     dem          Benutzeroberflächenobjekt             (BOO)        des      geladenen
        Prozessschrittes entspricht, ermittelt wird, indem
1.3.1   - für alle dem aktuellen Kontext des Computerprogramms zugeordneten
        Benutzeroberflächenobjekte
             - ermittelt         wird,     ob      der         Objekttyp       des          angezeigten
             Benutzeroberflächenobjektes des Computerprogramms mit dem
             Objekttyp des Benutzeroberflächenobjektes (BOO) des geladenen
             Prozessschrittes übereinstimmt (S4.1),
1.3.2        - falls die Objekttypen übereinstimmen, ein Übereinstimmungswert
             (ÜW)      für        das      angezeigte      Benutzeroberflächenobjekt                des
             Computerprogramms ermittelt wird (S4.2),
1.3.3        wobei     der        Übereinstimmungswert             (ÜW)       für     ein     Benutzeroberflächenobjekt auf Basis der Objekteigenschaften (OE) des
             Benutzeroberflächenobjektes bestimmt wird,
1.3.4        wobei         die      Objekteigenschaften             (OE)        des         über     die
             Objekterkennungsschnittstelle               abgefragten          Benutzeroberflächenobjektes (BOO) mit den entsprechenden Objekteigenschaften (OE)
             des       Benutzeroberflächenobjektes                 (BOO)            des      geladenen
             Prozessschrittes            verglichen      und     bewertet      werden         und   das
             Benutzeroberflächenobjekt des Computerprogramms zusammen mit
             dem Übereinstimmungswert (ÜW) in einer Ergebnisliste (EL)
             abgespeichert wird (S4.3), und
1.3.5        - jenes    Benutzeroberflächenobjekt                aus    der    Ergebnisliste        (EL)
             ausgewählt wird, welches ein vorbestimmtes Auswahlkriterium erfüllt
             (S4.4).

                                          - 20 -



3.    Einige Merkmale der jeweiligen Patentansprüche 1 gemäß Hauptantrag bzw.
Hilfsanträgen 1 bis 7 und 16 bedürfen der Erläuterung.


Patentanspruch 1 nach Hauptantrag ist auf ein computer-implementiertes Verfahren
gerichtet, das gemäß der in Merkmal 1.1 genannten Zweckangabe zur
Unterstützung eines Benutzers während einer Bedienung zumindest eines
vorbestimmten Computerprogramms geeignet sein soll. Als Unterstützung ist dabei
jegliche Hilfestellung anzusehen, welche dem Benutzer in Form einer Information
angeboten wird (vgl. Streitpatent, Abs. 0002 - 0004). Das beanspruchte Verfahren
schließt dabei die Unterstützung innerhalb eines Programms (d. h. aus dem
unterstützten, vorbestimmten Programm heraus) ebenso mit ein wie die
Unterstützung des Benutzers mit Hilfe eines weiteren Programms, das dieses
Unterstützungsverfahren        bereitstellt    und        sich     vom   vorbestimmten
Computerprogramm unterscheidet. In Merkmal 1.1.1 ist vorgesehen, dass während
der Benutzung des Computerprogramms ein Benutzeroberflächenobjekt (BOO),
also etwa ein Eingabefeld in einer Maske des Computerprogramms, eine
Schaltfläche, eine Checkbox oder eine Tabelle auf der Anzeige erscheint (vgl.
Streitpatent, Abs. 0030). Die folgenden Merkmale 1.1.2 und 1.1.3 definieren
Eigenschaften des Computerprogramms, dessen Bedienung auszuführende
Prozessschritte umfassen, welche durch eine bestimmte Benutzerinteraktion mit
einem bestimmten Benutzeroberflächenobjekt (BOO) in einem bestimmten Kontext
des Programms repräsentiert sind. Abgesehen davon, dass dies bei einem durch
Benutzeroberflächenobjekte gesteuerten Programmablauf die übliche Bedienart
sein dürfte, schränken die Merkmale 1.1.2 und 1.1.3 das Verfahren nur insoweit ein,
dass es geeignet sein soll, eine Unterstützung für solcherart ausgestaltete
Computerprogramme         zu        bieten,        also      für     Programme     mit
Benutzeroberflächenobjekten, d. h. etwa mit grafischen Bedienoberflächen. Die
Merkmale 1.1.4 und 1.1.5 beschreiben ebenfalls keine Verfahrensschritte, sondern
betreffen die Eigenschaften einer Navigationsdatei, in der die für die Bedienung des
Programms erforderlichen Benutzerinteraktionen als Prozessschritte abgespeichert
sein sollen. In Verbindung mit Merkmal 1.1.3 folgt daraus, dass die Navigationsdatei

                                        - 21 -



für jeden Prozessschritt des Programms beschreibt, wie die Benutzerinteraktion mit
dem vorbestimmten Benutzeroberflächenobjekt in einem vorbestimmten Kontext
auszusehen hat. Das Streitpatent führt entsprechend aus, dass ein Prozessschritt
durch    das    Tripel   Anwendungskontext,       Benutzeroberflächenobjekt    und
Benutzerinteraktion repräsentiert wird (vgl. Streitpatent, Abs. 0062).


Die Merkmalsgruppe 1.2 definiert mehrere Verfahrensschritte: Zunächst soll ein
Prozessschritt geladen werden (Merkmal 1.2.1), ohne dass festgelegt ist, um
welchen Prozessschritt es sich dabei handelt. Es kann sich also um den ersten oder
auch einen beliebigen der in der Navigationsdatei gespeicherten Prozessschritte
handeln. Sodann soll der aktuelle Kontext des Computerprogramms ermittelt
werden (Merkmal 1.2.2). Bei dem Kontext des Computerprogramms bzw. dem
Anwendungskontext handelt es sich gemäß Absatz 0032 des Streitpatents um eine
vorbestimmte Benutzeroberfläche des vorbestimmten Computerprogramms, also
beispielsweise das aktuell aktive Fenster oder die aktuell aktive Eingabemaske, in
einem vorbestimmten Zustand. In Verbindung mit der Definition des Prozessschritts
durch das Tripel Anwendungskontext, Benutzeroberflächenobjekt und Benutzerinteraktion (vgl. Streitpatent, Abs. 0062) folgt daraus, dass es sich bei dem zu
überprüfenden Kontext um einen vorbestimmten Zustand und nicht um das
Benutzeroberflächenobjekt selbst oder die darauf gerichtete Benutzerinteraktion
selbst handelt. Merkmal 1.2.3 fordert, dass geprüft wird, ob der aktuelle Kontext,
also beispielsweise das aktuell aktive Fenster des Programms, mit dem Kontext des
nach Merkmal 1.2.1 geladenen Prozessschritts übereinstimmt. Für den Fall, dass
diese Überprüfung „ja“ ergibt, erfolgen die in den Merkmalen 1.2.4 und 1.2.5
aufgeführten Schritte: Für den geladenen Prozessschritt wird ermittelt, welches der
aktuell angezeigten Benutzeroberflächenobjekte diesem Prozessschritt entspricht.
Das so ermittelte Benutzeroberflächenobjekt wird auf der Anzeigeeinrichtung
hervorgehoben, etwa durch eine Änderung der Helligkeit des Objekts im Vergleich
zum sonstigen Bildschirmhintergrund (vgl. Streitpatent, Abs. 0019, 0102).

                                         - 22 -



Die den kennzeichnenden Teil von Anspruch 1 bildende Merkmalsgruppe 1.3
beschreibt, wie dasjenige hervorzuhebende Benutzeroberflächenobjekt, welches
dem Benutzeroberflächenobjekt des geladenen Prozessschritts entspricht, ermittelt
werden soll. Dazu erfolgt zunächst nach Merkmal 1.3.1 eine Überprüfung, ob die
Objekttypen übereinstimmen, was für alle dem aktuellen Kontext zugeordneten
Objekte ermittelt werden soll. Das heißt, es wird für alle zugeordneten Objekte
überprüft, ob der Objekttyp des Benutzeroberflächenobjekts des geladenen
Prozessschritts mit dem Objekttyp des jeweils gerade zu überprüfenden
Benutzeroberflächenobjekts übereinstimmt (vgl. Streitpatent, Abs. 0068). Falls
diese Überprüfung positiv ausfällt, die Objekttypen also übereinstimmen, legt
Merkmal 1.3.2 fest, dass für jedes dieser auf der Anzeigeeinrichtung angezeigten
Benutzeroberflächenobjekte ein Übereinstimmungswert ermittelt wird und die
Prozessschritte 1.3.3 und 1.3.4 durchgeführt werden. Der Übereinstimmungswert
soll   anhand   eines    Vergleichs     der   Objekteigenschaften    des   jeweiligen
Benutzeroberflächenobjekts mit dem Benutzeroberflächenobjekt des geladenen
Prozessschritts bestimmt und dann in einer Ergebnisliste abgespeichert werden.
Das Streitpatent gibt dazu an, dass „jeder verfügbaren Objekteigenschaft OE ein
Gewichtungsfaktor zugeordnet“ wird (vgl. Streitpatent, Abs. 0076, 0077). Zudem
listen sämtliche aufgeführten Beispiele (vgl. SP, Abs. 0095 - 0098) jeweils mehrere
Objekteigenschaften mit den ihnen zugeordneten Gewichtungsfaktoren auf.
Allerdings bezieht sich Merkmal 1.3.4 auf die Objekteigenschaften (OE) des über
die Objekterkennungsschnittstelle abgefragten Benutzeroberflächenobjekts, so
dass sich die zu berücksichtigenden Objekteigenschaften nicht zwangsläufig auf
alle   Eigenschaften    des   Objekts    beziehen,   sondern   nur   auf   diejenigen
Objekteigenschaften, die über die Objekterkennungsschnittstelle verfügbar sind
(vgl. Streitpatent, Abs. 0076, 0077 i. V. m. Abs. 0066). Soweit daher über die
Objekterkennungsschnittstelle nur eine Objekteigenschaft ermittelt werden kann,
also verfügbar ist, fällt auch eine Bestimmung des Übereinstimmungswertes anhand
einer einzigen Objekteigenschaft des Objekts unter den Anspruchswortlaut. Eine
beliebige Auswahl von zu berücksichtigenden Objekteigenschaften ist dem
Streitpatent dagegen nicht zu entnehmen. Als Objekteigenschaften für ein

                                        - 23 -



Benutzeroberflächenobjekt benennt das Streitpatent als Beispiele die Position, die
Größe, den enthaltenen Text, die Farbe oder den Objekttyp (vgl. Streitpatent, Abs.
0064), sowie die Reihenfolge, die Hierarchie, ein Vorgängerobjekt oder ein nächstes
Objekt (vgl. Streitpatent, Abs. 0095 - 0098).


Der Übereinstimmungswert ist im Anspruch nicht näher definiert und kann damit
auch eine boolesche Variable sein, die lediglich zwei Werte (beispielsweise
„wahr“ oder „falsch“) annehmen kann. Merkmal 1.3.4 legt fest, dass das
Benutzeroberflächenobjekt zusammen mit dem Übereinstimmungswert in einer
Ergebnisliste abgespeichert wird, womit die Ergebnisliste unabhängig vom
ermittelten Übereinstimmungswert jeweils das Speichern beider Daten, also des
Benutzeroberflächenobjekts und des Übereinstimmungswertes fordert.


Das Ermitteln des nach Merkmal 1.2.5 für den Benutzer hervorzuhebenden
Benutzeroberflächenobjekts wird gemäß Merkmal 1.3.5 mit der Auswahl jenes
Benutzeroberflächenobjekt aus der Ergebnisliste abgeschlossen, welches ein
vorbestimmtes Auswahlkriterium erfüllt. Eine weitergehende Festlegung zu dem in
Merkmal 1.3.5 aufgeführten Auswahlkriterium trifft Anspruch 1 in der erteilten
Fassung (Hauptantrag) nicht.


Der Anspruch macht keine Aussage dazu, welche Schritte vorgenommen werden
sollen, wenn bei der in Merkmal 1.2.3 erfolgten Prüfung festgestellt wird, dass der
aktuelle Kontext des Programms nicht mit dem Kontext des geladenen
Prozessschritts übereinstimmt. Für diesen Fall lässt Anspruch 1 offen, ob weitere
Schritte zum Ermitteln und Hervorheben eines Benutzeroberflächenobjekts erfolgen
oder ob das Verfahren ohne Hervorhebung beendet wird. Eine Synchronisierung für
den Fall, dass die in Merkmal 1.2.3 vorgenommene Überprüfung keine
Übereinstimmung ergibt, ist erst im nicht angegriffenen Unteranspruch 3 gefordert
(vgl. auch Streitpatent, Fig. 1, Block SYN, sowie Fig. 2 und Abs. 0041).

                                      - 24 -



Auch Maßnahmen bzw. Verfahrensschritte zum Anfordern der Unterstützung für
den Benutzer (vgl. Streitpatent, Abs. 0038) sind vom Wortlaut des erteilten
Anspruchs 1 allenfalls indirekt umfasst, wobei das Verfahren gemäß Merkmal 1.1
zur Unterstützung eines Benutzers während der Bedienung eines Programms
geeignet sein soll.


In Anspruch 1 der Hilfsanträge 1 und 2 ist jeweils eine Definition des
Benutzeroberflächenobjekts ergänzt, welches „ein Objekt an einer Benutzeroberfläche des Computerprogramms ist, über welches der Benutzer mit dem
Computerprogramm interagieren kann“ bzw. „über ein Eingabegerät mit dem
Computerprogramm interagieren kann“. Damit wird das anspruchsgemäße
Benutzeroberflächenobjekt insoweit gegenüber anderen, auf einer grafischen
Bedienoberfläche dargestellten Objekten abgegrenzt, als dass es sich um Objekte
der   Benutzeroberfläche   handelt,   über     welche   der   Benutzer   mit   dem
Computerprogramm interagieren kann.


In Anspruch 1 des Hilfsantrags 3 ist zusätzlich die Auswahl des hervorzuhebenden
Benutzeroberflächenobjekts in den Merkmalen 1.3.4 und 1.3.5 durch die Angabe
einer Sortierung der Ergebnisliste und die Auswahl des ersten Objekts dieser
Ergebnisliste näher bestimmt.


Anspruch 1 nach Hilfsantrag 4 sind zusätzlich zum Hilfsantrag 2 Merkmale zur
Erzeugung der Navigationsdatei auf einer weiteren Datenverarbeitungseinrichtung
aufgenommen. Allerdings ist das Verfahren nach Anspruch 1 auf eine Unterstützung
des Benutzers während der Bedienung und Ausführung eines Computerprogramms
gerichtet (vgl. Merkmal 1.1). Verfahrensschritte, die als Vorbereitung auf einem
anderen Datenverarbeitungssystem erfolgen, beeinflussen nur insoweit das
Verfahren zur Unterstützung des Benutzers, als dass das Vorhandensein einer
Navigationsdatei zur Beschreibung von Prozessschritten vorausgesetzt wird und
diese selbstverständlich zur Verwendung im Datenverarbeitungssystems des
Benutzers vorliegen muss, also dort gelesen bzw. geladen ist. Hiervon ist jedoch

                                          - 25 -



bereits in Anspruch 1 gemäß Hauptantrag auszugehen. Soweit sich die in
Hilfsantrag 4 ergänzten Merkmale dagegen mit dem Erstellen bzw. Aufzeichnen der
Navigationsdatei in einem weiteren Datenverarbeitungssystem befassen, können
sie das beanspruchte Verfahren zur Unterstützung des Benutzers nicht
charakterisieren, da bei der Verwendung der Navigationsdatei im beanspruchten
Verfahren bei der Unterstützung des Benutzers während der Bedienung und
Ausführung des vorbestimmten Computerprogramms nicht erkennbar ist, wie oder
wo diese Datei erstellt wurde.


Anspruch 1 nach Hilfsantrag 5 umfasst zusätzlich zu den Merkmalen des
Hilfsantrags 2 die Konkretisierung der Unterstützung des Benutzers in Form des
Anzeigens von Informationen zu der von dem Benutzer durchzuführenden
Benutzerinteraktion auf der Anzeigeeinrichtung.


In Anspruch 1 nach Hilfsantrag 6 sind die Ergänzungen aus den Hilfsanträgen 3 bis
5 zusammengefasst.


Im Verfahren nach Anspruch 1 des Hilfsantrags 7 ist zusätzlich eine Prüfung
vorgesehen, ob sich das ermittelte Benutzeroberflächenobjekt (BOO) bereits in dem
erwarteten Zustand befindet, welcher durch die dem aktuellen Prozessschritt
zugeordnete Benutzerinteraktion herbeigeführt werden soll. Nur wenn dies noch
nicht   der   Fall   ist,   wird   das   ermittelte   Benutzeroberflächenobjekt   des
Computerprogramms auf der Anzeigeeinrichtung für den Benutzer hervorgehoben.


Das Verfahren nach Anspruch 1 des Hilfsantrags 16 basiert auf Hilfsantrag 7 und
umfasst einen zusätzlichen Initialisierungsschritt zum Laden der Navigationsdatei
auf Anforderung durch den Benutzer.

                                          - 26 -



                              II.     Zum Hauptantrag


In der erteilten Fassung ist das Streitpatent wegen fehlender Patentfähigkeit
ausgehend vom Stand der Technik nach den Druckschriften D1 und D7 für nichtig
zu erklären (Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a) EPÜ).


Der Gegenstand des Anspruchs 1 nach Hauptantrag beruht gegenüber den
Druckschriften D1 und D7 nicht auf einer erfinderischen Tätigkeit (Art. 56 EPÜ).


Aus   Druckschrift     D1    ist    ein   Computer-implementiertes     Verfahren    zur
Unterstützung eines Benutzers während einer Bedienung eines vorbestimmten
Computerprogramms bekannt (delivery of interactive onscreen instructions, vgl.
S. 1-3, dritter Abs. / Merkmal 1.1), bei dem während der Ausführung des
Computerprogramms           zumindest       ein    Benutzeroberflächenobjekt        des
Computerprogramms auf einer Anzeigeeinrichtung zur Anzeige gebracht wird (vgl.
item on the screen, beispielsweise a specific menu or menu item, oder an item in a
dialog box or other interface element in a window; vgl. S. 2-79, zweiter Abs. /
Merkmal 1.1.1). Dabei umfasst die Bedienung des Computerprogramms eine
Anzahl auszuführender Prozessschritte (sequence, vgl. beispielsweise S. C-25,
Figure C-4 und S. 2-86, Figure 2-58 / Merkmal 1.1.2). Diese Prozessschritte werden
jeweils durch eine vorbestimmte Benutzerinteraktion mit einem vorbestimmten
Benutzeroberflächenobjekt (item on the screen, beispielsweise a specific menu or
menu item, oder an item in a dialog box or other interface element in a window; vgl.
S. 2-79, zweiter Abs. i. V. m. Beschreibung von coachmark types, S. 2-80) in einem
vorbestimmten Kontext (vgl. Kapitel Using Context Checks, S. 2-83 f; beispielsweise
ActiveWindow, vgl. S. C-18, dritter Abs.) des Computerprogramms repräsentiert
(…each contain a step that the user should perform to accomplish the task, vgl.
Beschreibung zu Panels 2 and 3, S. 2-86 / Merkmal 1.1.3). Dabei ist eine
Navigationsdatei vorgesehen, die die für die Bedienung des Computerprogramms
erforderlichen Benutzerinteraktionen mit dem Computerprogramm enthält (Guide
File, vgl. S. 1-3, S. xix sowie beispielsweise S. C-1 und S. C-17, Listing C-10 /

                                        - 27 -



Merkmal 1.1.4), wobei die Benutzerinteraktionen als Prozessschritte in der
Navigationsdatei gespeichert sind (vgl. beispielsweise S. C-17, Listing C-10, i. V. m.
action panel, S. 2-53, le. Abs. / Merkmal 1.1.5).


Zur Unterstützung eines Benutzers während einer Bedienung eines vorbestimmten
Computerprogramms wird für einen in der Navigationsdatei gespeicherten
Prozessschritt dieser eine gespeicherte Prozessschritt geladen (vgl. beispielsweise
S. C-17, Listing C-10 / Merkmale 1.2, 1.2.1). Der aktuelle Kontext des
Computerprogramms wird ermittelt und mit dem Kontext des geladenen
Prozessschrittes verglichen, um zu prüfen, ob der aktuelle Kontext des
Computerprogramms        mit   dem   Kontext      des   geladenen   Prozessschrittes
übereinstimmt (vgl. Kapitel Using Context Checks, S. 2-83 f und … verify whether
this condition is true, S. 2-87, erster Abs., sowie <Skip lf> and <Make Sure>
commands, S. C-17, S. C-18 / Merkmale 1.2.2, 1.2.3). Druckschrift D1 sieht vor,
dass ein dem Prozessschritt entsprechendes Benutzeroberflächenobjekt des
Computerprogramms auf der Anzeigeeinrichtung für den Benutzer hervorgehoben
wird (verschiedene Arten von Hervorhebungs-Typen - coachmark, vgl. S. 2-79 bis
2-83, S. C-25 bis S. C-26 / Merkmal 1.2.5). In diesem Zusammenhang entnimmt
der   Fachmann     der   Druckschrift   D1       außerdem,   dass   hervorzuhebende
Benutzeroberflächenobjekte anhand ihres Objekttyps oder ihrer Objektbezeichnung
(vgl. targetltem, S. 10-109, le. Abs. und S. 10-110), also anhand von
Objekteigenschaften, identifiziert werden (vgl. Merkmale 1.3.1, 1.3.4).


Der Senat stimmt der Beklagten zu, dass eine Ermittlung des hervorzuhebenden
angezeigten Benutzeroberflächenobjekts in Druckschrift D1 nicht ausdrücklich
beschrieben ist (vgl. Merkmal 1.2.4, Merkmalsgruppe 1.3). Der Fachmann entnimmt
Druckschrift D1 jedoch Hinweise, dass eine zuverlässige Identifizierung des
Benutzeroberflächenobjekts wichtig ist (vgl. insbesondere S. 2-79, Abs. Important
u. S. 10-107, Abs. Special considerations).

                                         - 28 -



Der Einwand der Beklagten bezüglich des Hervorhebungs-Typs object coach, bei
welchem die Applikation die hervorzuhebenden Objekte spezifizieren muss und
daher keine Ermittlung wie in Merkmal 1.2.4 gefordert erfolgt (vgl. S. 2-80:
Coachmarks Styles), gilt, wie die Klägerin ausführt, nicht für alle Hervorhebungs-Typen. Wie auf Seite 9-38 angegeben, kann das Hilfesystem – außer für die explizit
genannte Ausnahme für den Typ object coach – ohne Angaben vom
Anwendungsprogramm die Hervorhebung durchführen (vgl. S. 9-38: Apple Guide
can automatically draw coachmarks for menus, items, …, without assistance from
your application). Dieser Aussage entnimmt der Fachmann, dass dazu das
hervorzuhebende Benutzeroberflächenobjekt im Sinne der Merkmale 1.2.4 und 1.3
ermittelt werden muss. Druckschrift D1 weist zudem ausdrücklich auf die Gefahr
hin, dass es unter bestimmten Bedingungen zu einer falschen Identifizierung des
Benutzeroberflächenobjekts      kommen      kann   (S.   10-107,       Abschnitt   Special
Considerations) und dass es wichtig ist, das hervorzuhebende Element zu
identifizieren bzw. zu verifizieren (vgl. S. 2-79, Abschnitt Important).


Der Fachmann erhält daher aufgrund seines fachmännischen Verständnisses der
Anforderungen für die Hervorhebung eines Benutzeroberflächenobjekts bereits aus
Druckschrift D1 den Hinweis, dass bei Übereinstimmung des aktuellen und des im
Prozessschritt beschriebenen Kontextes das hervorzuhebende, aktuell angezeigte
Benutzeroberflächenobjekt des Computerprogramms ermittelt werden muss, das
diesem Prozessschritt entspricht (Merkmale 1.2.4, 1.3).


Entgegen der Auffassung der Beklagten hatte der Fachmann auch Veranlassung,
den Stand der Technik nach Anregungen zu durchsuchen, wie eine zuverlässige
Ermittlung   von   Benutzeroberflächenobjekten       möglich    ist.    Der   in   diesem
Zusammenhang geäußerten Auffassung der Beklagten, die Aufgabe des
Fachmanns müsse sich aus der Druckschrift D1 ableiten lassen, stimmt der Senat
nicht zu. Denn die objektive Aufgabe leitet sich nach der ständigen Rechtsprechung
des Bundesgerichtshofs gerade nicht aus einer als „nächstkommender Stand der
Technik“ bestimmten Druckschrift ab (vgl. BGH, Urteil vom 18. Juni 2009,

                                            - 29 -



Xa ZR 138/05     –     Fischbissanzeiger;     Urteil    vom    4.2.2010,    Xa    ZR      36/08
– Gelenkanordnung; Urteil vom 16.12.2008, X ZR 89/07 – Olanzapin, Rn. 51). Die
Aufgabe, vor die der Fachmann im vorliegenden Fall gestellt war, ist daher nicht,
das Verfahren nach Druckschrift D1 weiterzuentwickeln. Vorliegend ergibt sich die
Zielsetzung des Fachmanns bereits aus der im Streitpatent genannten Aufgabe, die
auch der objektiven, durch das beanspruchte Verfahren bzw. System gelösten
Problemstellung entspricht. Demnach sollen ein Verfahren und ein System zur
Unterstützung         eines     Benutzers     während         einer     Bedienung         eines
Computerprogramms bereitgestellt werden, welche es erlauben, während der
Ausführung      des     Computerprogramms            kontextübergreifend    ein    Benutzeroberflächenobjekt des Computerprogramms entsprechend einem vorbestimmten
Programmablauf auch bei sich ändernden Bezugsmerkmalen des Benutzeroberflächenobjektes auf einer Anzeigeeinrichtung hervorzuheben. Dabei hat der
Fachmann aufgrund der Hinweise auf mögliche Probleme im Hilfesystem gemäß
Druckschrift D1 (vgl. S. 2-79, Abschnitt Important; S. 10-107, Abschnitt Special
Considerations) eine Veranlassung, den weiteren Stand der Technik nach
Möglichkeiten zu durchsuchen, um eine möglichst fehlerfreie Unterstützung des
Benutzers zu entwickeln.


Dies steht auch nicht im Widerspruch dazu, dass nach Druckschrift D1 für
bestimmte      Hervorhebungs-Typen           (coachmark)        keine      Ermittlung      des
Benutzeroberflächenobjekts erforderlich ist (vgl. Beschreibung zu object coach,
S. 2-80).    Denn     ein     Benutzerhandbuch        wie   Druckschrift   D1     setzt    eine
Betriebssystem- und Programmumgebung voraus, bei der bestimmte Maßnahmen
nicht gesondert implementiert werden müssen, beispielsweise wenn das
Anwendungsprogramm oder das genutzte Betriebssystem bereits Informationen
über   den    Anwendungskontext         oder     aktive     Benutzeroberflächenelemente
bereitstellt. Gerade aufgrund dieser Abhängigkeit von der Betriebssystem- und
Programmumgebung wird der Fachmann nicht unreflektiert jedes Detail der
Druckschrift D1 übernehmen, insbesondere da er aufgrund der genannten Hinweise
auf mögliche Probleme oder besondere Randbedingungen, beispielsweise auch die

                                         - 30 -



dabei jeweils vorausgesetzte Betriebssystemumgebung oder Eigenschaften des
Anwendungsprogramms, die sich aus der Lehre der Druckschrift D1 ergeben,
hingewiesen wird. Für die angestrebte flexible Lösung zur Unterstützung des
Nutzers wird der Fachmann sich daher nicht darauf verlassen, dass das
Anwendungsprogramm          oder   Betriebssystem     bereits   alle     erforderlichen
Informationen liefert. Vielmehr erkennt er in Druckschrift D1, dass entsprechende
Informationen über die aktuell angezeigten Benutzeroberflächenobjekte erforderlich
sind, um die genannten Probleme zu überwinden.


In der zum Stand der Technik gehörenden Druckschrift D7 (DE 10 2008 028 581
A1) findet der Fachmann in den Absätzen 0003 bis 0005 und insbesondere den
Figuren 1, 6, 7, 8 u. 12 mit zugehöriger Beschreibung in den Absätzen 0033 und
0047     bis   0054   ein    Verfahren      zur   automatischen       Ermittlung   von
Benutzeroberflächenobjekten, welches nicht nur, wie die Beklagte anführt, zur
automatischen Erstellung von Dokumentationen dient, sondern allgemein bei
Computer-Anwendungen eingesetzt werden kann (vgl. Abs. 0004, 0005, 0026,
0046). Dabei werden Objekttypen von angezeigten Benutzeroberflächenobjekten
mit    vorgegebenen   Objekttypen    verglichen     und   bewertet,    so   dass   ein
Übereinstimmungswert ermittelt wird. In Druckschrift D7 sind die Steuerelemente 7
als Benutzeroberflächenobjekte, die Methodenobjekte als Objekttypen, die
Erkennungssicherheit als Übereinstimmungswert und die Kandidatenliste als
Ergebnisliste anzusehen (vgl. Abs. 0066 - 0068, 0081 - 0087, 0092, Fig. 7 u. 12 /
Merkmal 1.3.1). Wie von der Klägerin ausgeführt, kann die Überprüfung der IDs als
ein Überprüfen von Objekttypen angesehen werden, an das sich das Ermitteln eines
Übereinstimmungswerts (Erkennungssicherheit) und ein Abspeichern gemeinsam
mit dem extrahierten Objekt, welches nunmehr einen Kandidaten darstellt, in einer
Ereignisliste (Kandidatenliste) anschließt (vgl. Abs. 0079, letzte zwei Sätze: Ein
Kandidat 6 ist … ein potentiell erkanntes Steuerelement 7, das mit einer Maßzahl
verknüpft ist, die die Güte der Erkennung angibt.) Diese Maßzahl wird im Laufe der
Erkennung automatisch generiert, und zwar auf Basis der Objekteigenschaften (vgl.
Abs. 0056 / Merkmale 1.3.2, 1.3.3, 1.3.4). Im Hinblick auf Merkmal 1.3.5 sind weiter

                                         - 31 -



die Absätze 0092 und 0093 relevant, da das dort beschriebene Ordnen der
Kandidaten anhand der Güte der Erkennung (Maßzahl) die Grundlage für die
Auswahl eines Objekts aus der Liste bildet, wie sie in Merkmal 1.3.5 gefordert ist.
Der Fachmann entnimmt Druckschrift D7 somit die Merkmale 1.3.1 bis 1.3.5 für die
Anwendung in einem Online-Hilfesystem.


Der Auffassung der Beklagten, dass Druckschrift D7 zusätzliche Vorarbeiten in
Form der Definition von so genannten Schablonen (Anwendungsschablone,
Objektschablone) voraussetze und daher nicht flexibel Benutzeroberflächenobjekte
identifizieren könne, kann ebenfalls nicht beigetreten werden. Denn auch das
anspruchsgemäße Verfahren setzt eine Beschreibung erwarteter Prozessschritte
des Anwendungsprogramms und den jeweils in einem bestimmten Kontext
hervorzuhebender Benutzeroberflächenobjekte voraus (vgl. Streitpatent: Anspruch
1, Merkmale 1.1.3 und 1.1.5 sowie Abs. 0062 i. V. m. Abs. 0009). Dass zum
Ermitteln eines Benutzeroberflächenobjekts eine Information über Eigenschaften
des bei einem Prozessschritt hervorzuhebenden Objekts, beispielsweise dessen
Typ, Bezeichnung oder ID, vorliegen muss, ergibt sich aus Druckschrift D7. Ein
Hinweis dazu findet sich – wie oben dargelegt – bereits in Druckschrift D1 (S. 10-
109 und 10-110). Diese weiteren Informationen, d. h. die Beschreibung erwarteter
Objekteigenschaften, ebenfalls in der Navigationsdatei zu hinterlegen, welche nach
Druckschrift D1 bereits die Beschreibung des Prozessschritts einschließlich der
Beschreibung        des       Kontexts            und   des     hervorzuhebenden
Benutzeroberflächenobjekts enthält, stellt eine fachübliche, wenn nicht sogar
selbstverständliche Maßnahme dar.


Der Gegenstand des Anspruchs 1 nach Hauptantrag ergibt sich demnach für den
Fachmann in naheliegender Weise aus der Zusammenschau der Druckschriften D1
und D7. Der Gegenstand des Anspruchs 1 gemäß Hauptantrag beruht daher nicht
auf einer erfinderischen Tätigkeit.

                                         - 32 -



                             III.   Zu den Hilfsanträgen

Das Streitpatent ist auch in den Fassungen nach den Hilfsanträgen, mit denen die
Beklagte es beschränkt verteidigt, nach Art. II § 6 Abs. 1 Nr. 1 IntPatÜG i. V. m.
Art. 138 Abs. 1 Buchst. a) EPÜ für nichtig zu erklären, weil der Gegenstand des
jeweiligen Anspruchs 1 nach den Hilfsanträgen 1 bis 6 nicht patentfähig ist, die
Hilfsanträge 7 und 16 nicht zulässig sind und die Hilfsanträge 8 bis 15 sowie 17
mangels Eintretens der dort formulierten prozessualen Bedingung nicht zu prüfen
sind.


1. Zu den Hilfsanträgen 1 und 2


Der jeweilige Gegenstand des Anspruchs 1 gemäß Hilfsantrag 1 und Hilfsantrag 2
beruht nicht auf einer erfinderischen Tätigkeit.


In Anspruch 1 des Hilfsantrags 1 ist das Verfahren nach Anspruch 1 des
Hauptantrags um die Definition des Begriffs „Benutzeroberflächenobjekt“ ergänzt,
wonach „ein Benutzeroberflächenobjekt ein Objekt an einer Benutzeroberfläche des
Computerprogramms ist, über welches der Benutzer mit dem Computerprogramm
interagieren kann“. Diese Definition ist in Anspruch 1 nach Hilfsantrag 2
dahingehend ergänzt, dass diese Interaktion „über ein Eingabegerät“ erfolgt.


Diese Definitionen geben allerdings nichts anderes als das fachübliche Verständnis
von Elementen grafischer Bedien- bzw. Benutzeroberflächen (GUI) wieder, die eine
Interaktion des Benutzers mit einem aktuell ablaufenden Computerprogramm
ermöglichen.    Da    auch     Druckschrift   D1   das   gleiche   Verständnis   von
Benutzeroberflächenobjekten zugrunde legt, die beispielsweise dazu dienen,
Informationen einzugeben (vgl. beispielsweise S. 2-79, zweiter Abs.), kann die
jeweilige Definition nach Hilfsantrag 1 bzw. Hilfsantrag 2 das beanspruchte
Verfahren nicht gegenüber dem aus Druckschrift D1 bekannten Hilfeverfahren
abgrenzen. Gleiches gilt für das Identifizieren von Benutzeroberflächenobjekten,

                                       - 33 -



wie es aus Druckschrift D7 bekannt ist (Steuerelemente, wie z. B. Schaltflächen,
Eingabemasken oder Auswahlfelder, vgl. beispielsweise Abs. 0004).


Soweit mit den Definitionen in Anspruch 1 auf den Einwand der Klägerin im Hinblick
auf den Patentierungsausschluss nach Art. 52 Abs. 2 und 3 EPÜ reagiert wurde,
wonach das beanspruchte Verfahren nur Datenobjekte vergleiche, kann dies
dahinstehen. Denn die Gegenstände der jeweiligen Ansprüche 1 nach Hilfsantrag 1
und Hilfsantrag 2 ergeben sich damit jeweils für den Fachmann in naheliegender
Weise aus der Zusammenschau der Druckschriften D1 und D7, wie dies vorstehend
zum Hauptantrag dargelegt ist.


2. Zu Hilfsantrag 3


Auch der Gegenstand des Anspruchs 1 gemäß Hilfsantrag 3 ergibt sich für den
Fachmann in naheliegender Weise aus der Zusammenschau der Druckschriften D1
und D7 und beruht damit nicht auf einer erfinderischen Tätigkeit.


In Anspruch 1 des Hilfsantrags 3 ist ausgehend von Anspruch 1 des Hilfsantrags 2
konkretisiert, dass das Benutzeroberflächenobjekt des Computerprogramms
zusammen mit dem Übereinstimmungswert in einer absteigend sortierten
Ergebnisliste abgespeichert wird und das vorbestimmte Auswahlkriterium zur
Auswahl des hervorzughebenden Benutzeroberflächenobjekts darin besteht, dass
das erste Benutzeroberflächenobjekt der Ergebnisliste ausgewählt wird.


Die Verwendung einer nach einem Bewertungskriterium (Übereinstimmungswert)
geordneten Liste zum Zweck der Auswahl eines Elements, welches ein
Auswahlkriterium möglichst gut erfüllt, ist dem Fachwissen des Fachmanns
zuzurechnen, der eine solche Auswahl als Computerprogramm implementieren soll.
Eine entsprechende Anregung entnimmt der Fachmann zudem der vergleichbaren
Auswahl aus einer Kandidatenliste in Druckschrift D7 (vgl. Abs. 0094, 0096).

                                       - 34 -



Zu den weiteren, gegenüber der Anspruchsfassung des Hilfsantrags 2
unveränderten Anspruchsmerkmalen wird auf die Ausführungen zum Hilfsantrag 2
verwiesen, die für den vorliegenden Anspruch in gleicher Weise gelten.


3. Zu Hilfsantrag 4


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 4 ergibt sich für den Fachmann
ebenfalls in naheliegender Weise aus der Zusammenschau der Druckschriften D1
und D7 und beruht nicht auf einer erfinderischen Tätigkeit.


In Anspruch 1 des Hilfsantrags 4 sind ausgehend von Anspruch 1 des Hilfsantrags
2 die Navigationsdatei und der Kontext näher spezifiziert.


Wie vorstehend im Rahmen der Auslegung bereits dargelegt, können der Ort und
die   Vorgehensweise     zum   Erzeugen     der   Navigationsdatei    (…mit    einem
Aufzeichnungsmittel auf einer ersten Datenverarbeitungseinrichtung erzeugt…;
erzeugt   wird   durch   Verwendung     eines     Aufzeichnungsverfahrens…)      das
beanspruchte Verfahren nicht charakterisieren. Denn das Verfahren nach Anspruch
1 ist auf die Unterstützung eines Benutzers während einer Bedienung zumindest
eines vorbestimmten Computerprogramms gerichtet und kann daher keine
Verfahrensschritte zur Erstellung der dabei vorausgesetzten Navigationsdatei auf
einem anderen Datenverarbeitungssystem umfassen. Bei der Verwendung der
Navigationsdatei zur Unterstützung des Benutzers während der Bedienung und
Ausführung    des   vorbestimmten    Computerprogramms        ist   außerdem    nicht
erkennbar, wie oder wo diese Datei erstellt wurde.


Dass diese Navigationsdatei dabei zur Verwendung im Datenverarbeitungssystem
des Benutzers gelesen werden muss, um dort verwendet zu werden, ist eine
selbstverständliche Voraussetzung, von der vorliegend bereits im Verfahren nach
Anspruch 1 des Hauptantrags zwangsläufig auszugehen ist (vgl. Abschnitt A.I.3. zur
Auslegung).

                                       - 35 -



Die im Zusammenhang mit den Merkmalen zur Erzeugung der Navigationsdatei
ergänzte    Definition,   nach   welcher        der   Kontext   eine   vorbestimmte
Benutzeroberfläche des Computerprogramms in einem vorbestimmten Zustand
kennzeichnet, ergibt sich bereits in Anspruch 1 gemäß Hauptantrag für den
entsprechend definierten Prozessschritt.


Damit gelten aber auch für Anspruch 1 nach Hilfsantrag 4 die vorstehenden
Ausführungen zu Anspruch 1 nach Hilfsantrag 2 in gleicher Weise.


4. Zu Hilfsantrag 5


Der Gegenstand des Anspruchs 1 nach Hilfsantrag 5 ergibt sich ebenfalls für den
Fachmann in naheliegender Weise aus der Zusammenschau der Druckschriften D1
und D7 und beruht nicht auf einer erfinderischen Tätigkeit.


In Anspruch 1 nach Hilfsantrag 5 ist ein weiterer Verfahrensschritt gegenüber dem
Anspruch 1 des Hilfsantrags 2 ergänzt, wonach das Verfahren einen Schritt zum
Anzeigen von Informationen zu der von dem Benutzer durchzuführenden
Benutzerinteraktion auf der Anzeigeeinrichtung umfasst, wobei die Informationen
vorzugsweise ein Bild des zu bedienenden Benutzeroberflächenobjektes und einen
Beschreibungstext umfassen.


Der erste Teilsatz des ergänzten Merkmals beinhaltet lediglich die Wiedergabe von
an den Benutzer gerichteten Informationen. Dazu ist auch Druckschrift D1 – neben
dem Hervorheben von Benutzeroberflächenobjekten – bereits die Anzeige von
Hinweisen zu Benutzerinteraktionen an den Benutzer zu entnehmen (vgl. Kap.
Designing Panel Types, S. 2-50 ff sowie Figure C-4, S. C-25).


Beim zweiten Teilsatz des Merkmals handelt es sich um ein fakultatives Merkmal
(insbesondere…), das den beanspruchten Gegenstand nicht beschränkt.

                                       - 36 -



Für die weiteren, mit Anspruch 1 nach Hilfsantrag 2 übereinstimmenden
Anspruchsmerkmale gelten die vorstehenden Ausführungen zu Anspruch 1 nach
Hilfsantrag 5 in gleicher Weise.


5. Zu Hilfsantrag 6


Auch der Gegenstand des Anspruchs 1 nach Hilfsantrag 6 ergibt sich für den
Fachmann in naheliegender Weise aus der Zusammenschau der Druckschriften D1
und D7 und beruht nicht auf einer erfinderischen Tätigkeit.


Die Änderungen des Hilfsantrags 6 umfassen die Änderungen der Hilfsanträge 3, 4
und 5, die wiederum die Änderungen des Hilfsantrags 2 umfassen.


Wie in den vorstehenden Ausführungen zu den Hilfsanträgen 2 bis 5 dargelegt, sind
die jeweils ergänzten Merkmale nicht geeignet, eine erfinderische Tätigkeit zu
begründen. Aus deren Kombination ergibt sich keine weitergehende Wirkung. Es
wird daher auf die Ausführungen zu den vorgenannten Hilfsanträgen verwiesen, die
für Anspruch 1 des Hilfsantrags 6 in gleicher Weise gelten.


6. Zu den Hilfsanträgen 7 und 16


Die Hilfsanträge 7 und 16 sind bereits unzulässig, weil eine Änderung nicht im Streit
stehender Patentansprüche, vorliegend des Anspruchs 5, im Nichtigkeitsverfahren
auch im Weg der Selbstbeschränkung nicht in Betracht kommt.


Die beschränkte Verteidigung eines mit einer Teilnichtigkeitsklage angegriffenen
Patentanspruchs durch Kombination mit einem insoweit nicht angegriffenen
Unteranspruch oder mit einer von mehreren Varianten eines insoweit nicht
angegriffenen Unteranspruchs ist unzulässig (vgl. BGH, Urteil vom 1. März 2017
– X ZR 10/15, GRUR 2017, 604, Rn. 27 – Ankopplungssystem m. w. N.).

                                       - 37 -



Ein Patent kann vom Nichtigkeitsbeklagten nur in dem Umfang beschränkt verteidigt
werden, in dem es vom Nichtigkeitskläger angegriffen wird. Mit der beschränkten
Verteidigung eines teilweise angegriffenen Patents durch Kombination eines
angegriffenen Anspruchs mit einem auf diesen rückbezogenen, aber mit der
Nichtigkeitsklage nicht angegriffenen Unteranspruch wird das Streitpatent der
Sache nach im Umfang des nicht angegriffenen Unteranspruchs zur gerichtlichen
Überprüfung gestellt. Die Möglichkeit, das Patent beschränkt zu verteidigen, dient
aber allein der Verteidigung gegenüber dem vom Nichtigkeitskläger geführten
Angriff auf die Wirksamkeit des Patents und nicht auch der gerichtlichen
Überprüfung des Patents im Übrigen.


Für eine solche beschränkte Verteidigung ist ein Rechtsschutzbedürfnis selbst dann
nicht anzuerkennen, wenn der Nichtigkeitskläger die Rechtsbeständigkeit des mit
der Nichtigkeitsklage nicht angegriffenen Unteranspruchs in Zweifel zieht. Denn die
beschränkte Verteidigung gegenüber einer Teilnichtigkeitsklage auch im Umfang
eines nicht angegriffenen Unteranspruchs hätte im Wesentlichen die Wirkung einer
Widerklage des Patentinhabers gegenüber dem Nichtigkeitskläger auf Feststellung
der Rechtsbeständigkeit des Streitpatents im Umfang des nicht angegriffenen
Unteranspruchs. Eine solche Klage ist aber im Gesetz nicht vorgesehen und kann
deshalb   auch    nicht   Gegenstand    einer   beschränkten    Verteidigung    des
Nichtigkeitsbeklagten sein.


Der Gegenstand von Patentanspruch 1 in der Fassung des Hilfsantrags 7
unterscheidet sich von der erteilten Fassung durch folgende weitere Merkmale:
„dass (…) geprüft wird, ob sich das ermittelte Benutzeroberflächenobjekt (BOO)
bereits in dem erwarteten Zustand befindet, welcher durch die dem aktuellen
Prozessschritt zugeordnete Benutzerinteraktion herbeigeführt werden soll, und nur,
wenn die Prüfung ergibt, dass sich das ermittelte Benutzeroberflächenobjekt (BOO)
nicht in dem erwarteten Zustand befindet, das ermittelte Benutzeroberflächenobjekt
(BOO) des Computerprogramms auf der Anzeigeeinrichtung für den Benutzer
hervorgehoben wird (S6),“.

                                       - 38 -



Die hinzugefügten Merkmale sind identisch mit dem um weitere Merkmale
ergänzten Unteranspruch, weshalb die Beklagte selbst anregt, den bisherigen
Unteranspruch 5 zu streichen (vgl. Schriftsatz vom 13. Februar 2020, S. 26,
Abs. 128).


Die beschränkte Verteidigung des Streitpatents durch eine Kombination des
Patentanspruchs 1 mit dem von der Klägerin nicht angegriffenen Unteranspruch 5
ist damit unzulässig. Insoweit ist es auch unerheblich, dass von Unteranspruch 5
lediglich eine um ein weiteres Merkmal ergänzte und damit eigeschränkte Variante
in Patentanspruch 1 aufgenommen werden soll.


Unzulässig ist auch die Verteidigung des Gegenstands von Patentanspruch 1 in der
Fassung des Hilfsantrags 7, in dem der Patentanspruch 1 in der erteilten Fassung
mit Patentanspruch 5 nach der erteilten Fassung mit hinzugekommenen Merkmalen
kombiniert wird (vgl. BGH, Urteil vom 1. März 2017 – X ZR 10/15, GRUR 2017, 604,
Rn. 29 – Ankopplungssystem m. w. N.).


Der Umstand, dass Patentanspruch 1 in der Fassung des Hilfsantrags 7 neben
einem nicht angegriffenen Unteranspruch auch mit einem Merkmal kombiniert
werden soll, das nicht Gegenstand eines nicht angegriffenen Unteranspruchs ist,
ändert nichts daran,     dass die     Beklagte   das Streitpatent damit in    im
Nichtigkeitsverfahren unzulässiger Weise beschränken will.


Dies gilt demnach auch für Hilfsantrag 16, der auf Hilfsantrag 7 basiert und eine
zusätzliche Beschränkung enthält.


7.    Zu den Hilfsanträgen 8 bis 15 und 17


Eine Prüfung der Hilfsanträgen 8 bis 15 und 17 ist nicht veranlasst.

                                          - 39 -



Die Hilfsanträgen 8 bis 15 und 17 sind unter der zulässigen innerprozessualen
Bedingung (nur für den Fall) gestellt, dass das Gericht in der Beschränkung des
Anspruchs 1 durch das Merkmal 1.2.3 und durch die Bedingung in Merkmal 1.2.4
eine unzulässige Erweiterung erkennen sollte.


Dann soll das Streitpatent im Umfang des Hauptantrages oder eines der
Hilfsanträge 1 bis 7 aufrechterhalten werden mit der Maßgabe, dass aus dem Schritt
der Überprüfung des Kontextes und dem positiven Ergebnis hierbei in Anspruch 1
keine Rechte hergeleitet werden, also folgende Merkmale bei der Frage der Validität
des Streitpatents unberücksichtigt bleiben:
     - geprüft wird, ob der aktuelle Kontext des Computerprogramms mit dem
          Kontext des geladenen Prozessschrittes übereinstimmt (S2),
     - falls der aktuelle Kontext des Computerprogramms mit dem Kontext des
          geladenen Prozessschrittes übereinstimmt,
          (Disclaimer).


Wie ausgeführt, scheitert der Bestand des Gegenstands des jeweiligen Anspruchs
1 nach den Hilfsanträgen 1 bis 6 an deren mangelnder Patentfähigkeit, weil sie – wie
oben ausgeführt - aufgrund der Kombination der Druckschriften D1 und D7
nahegelegt sind. Infolgedessen war eine Prüfung der Frage der unzulässigen
Erweiterung des Anspruchs 1 durch das Einfügen des Merkmals 1.2.3 und der
Bedingung in Merkmal 1.2.4 nicht veranlasst. Die unter der Bedingung der Bejahung
dieser    Frage    gestellten   Anträge    sind    mangels   Bedingungseintritt   nicht
verfahrensgegenständlich geworden.


8.       Zu den angegriffenen Unteransprüchen


Mit den nicht patentfähigen jeweiligen Ansprüchen 1 nach Hauptantrag und nach
den Hilfsanträgen 1 bis 6 sind auch die abhängigen, auf die jeweiligen Ansprüche 1
direkt oder indirekt rückbezogenen Ansprüche des Hauptantrags und der
Hilfsanträge, soweit sie mit der Klage angegriffen sind, nicht schutzfähig, da weder

                                          - 40 -



geltend gemacht noch sonst ersichtlich ist, dass die in ihnen enthaltenen
zusätzlichen Merkmale zu einer anderen Beurteilung der Patentfähigkeit führen (vgl.
Urteil vom 29. September 2011 – X ZR 109/08, BlPMZ 2012, 64, Leitsatz –
Sensoranordnung).


Da sich somit das Streitpatent im angegriffenen Umfang weder in der erteilten
Fassung noch in der Fassung der Hilfsanträge als patentfähig erweist, war das
Streitpatent in diesem mit der Klage geltend gemachten Umfang für nichtig zu
erklären.


                             B.     Nebenentscheidungen


Die Kostenentscheidung beruht auf § 84 Abs. 2 PatG i. V. m. § 91 Abs. 1 ZPO.


Die Entscheidung über die vorläufige Vollstreckbarkeit folgt aus § 99 Abs. 1 PatG
i. V. m. § 709 ZPO.


                                           C.

                         Rechtsmittelbelehrung

Gegen dieses Urteil ist das Rechtsmittel der Berufung gegeben.

Die   Berufungsschrift       muss    innerhalb     eines    Monats   schriftlich   beim
Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht oder als
elektronisches Dokument nach Maßgabe der Verordnung über den elektronischen
Rechtsverkehr         beim        Bundesgerichtshof        und    Bundespatentgericht
(BGH/BPatGERVV) vom 24. August 2007 (BGBl. I S. 2130) in die elektronische
Poststelle   des       Bundesgerichtshofes         (www.bundesgerichtshof.de/erv.html)
übertragen werden. Die Berufungsfrist beginnt mit der Zustellung des in
vollständiger Form abgefassten Urteils, spätestens aber mit dem Ablauf von

                                        - 41 -



fünf Monaten nach der Verkündung. Die Frist ist nur gewahrt, wenn die Berufung
vor Fristablauf eingeht.


Die Berufungsschrift muss von einer in der Bundesrepublik Deutschland
zugelassenen Rechtsanwältin oder Patentanwältin oder von einem in der
Bundesrepublik Deutschland zugelassenen Rechtsanwalt oder Patentanwalt
unterzeichnet oder im Fall der elektronischen Einreichung mit einer qualifizierten
elektronischen Signatur nach dem Signaturgesetz oder mit einer fortgeschrittenen
elektronischen Signatur versehen sein, die von einer internationalen Organisation
auf dem Gebiet des gewerblichen Rechtsschutzes herausgegeben wird und sich zur
Bearbeitung durch das jeweilige Gericht eignet. Die Berufungsschrift muss die
Bezeichnung des Urteils, gegen das die Berufung gerichtet wird, sowie die Erklärung
enthalten, dass gegen dieses Urteil Berufung eingelegt werde. Mit der
Berufungsschrift   soll    eine   Ausfertigung   oder   beglaubigte   Abschrift   des
angefochtenen Urteils vorgelegt werden.




 Friehe            Werner         Dr. Schwengelbeck      Altvater     Dr. Flaschke

                                                                                  prö
