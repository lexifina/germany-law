---
ecli: "ECLI:DE:BPatG:2003:020703B20Wpat73.02.0"
court: "Bundespatentgericht"
spruchkoerper: "20"
aktenzeichen: "20 W (pat) 73/02"
decided: "2003-07-02"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2003&Sort=1&Seite=69&nr=20134&anz=2047&pos=1043&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2003-07-02_20_W-pat_73_02_NA_0.txt"
---

# Bundespatentgericht, 20 W (pat) 73/02 vom 2003-07-02

## Entscheidung

BUNDESPATENTGERICHT


 20 W (pat) 73/02                                                Verkündet am
 _______________                                                  2. Juli 2003
    (Aktenzeichen)                                                     …




                            BESCHLUSS

                          In der Beschwerdesache


               betreffend die Patentanmeldung P 43 17 043.9-35


…




hat der 20. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 2. Juli 2003 durch den Vorsitzenden Richter
Dipl.-Phys. Dr. Anders sowie den Richter Dipl.-Ing. Obermayer, die Richterin
Martens und den Richter Dipl.-Phys. Dr. Zehendner




BPatG 154
6.70

                                         -2-



beschlossen:


         Der Beschluß des Patentamts vom 27. August 2002 wird aufgehoben und das Patent erteilt.


         Bezeichnung: Verfahren und Vorrichtung zur Echokompensation in Übertragungssystemen


         Anmeldetag:     21. Mai 1993.


         Der Erteilung liegen folgende Unterlagen zugrunde:


         Patentansprüche 1 und 2, überreicht in der mündlichen Verhandlung,
         2 Blatt Beschreibung, Spalten 1 bis 4, überreicht in der mündlichen Verhandlung,
         4 Blatt Zeichnungen (Figuren 1, 2, 3a, 3b, 4), gemäß Offenlegungsschrift.


                                   Gründe


                                          I


Die Anmeldung wurde zurückgewiesen, weil die Ansprüche 1 und 2 keine klare
technische Lehre vermittelten. Es sei aus ihnen nicht entnehmbar, wie die Korrektursignale gebildet werden.


Die Anmelderin beantragt wie entschieden.

                                        -3-



Der Anspruch 1 lautet:


       "1. Verfahren zur Echokompensation in Übertragungssystemen, bei dem zur selbsttätigen Identifikation der Übertragungseigenschaften der echoerzeugenden Systemmerkmale zur Schätzwertbildung (ZC) für das Echo (Z) mit Hilfe implementierbarer adaptiver NLMS - (Normalized Least Mean
           Square) Algorithmen eine Impulsantwort gebildet wird, welche die N Koeffizienten eines zur Systemnachbildung verwendbaren adaptiven Transversalfilters (HC) enthält, die in
           regelmäßigen Zeitabständen (Abtasttakt) nach Dekorrelieren der Eingangssignale (IN) mittels eines einen dekorrelierten Eingangssignalvektor (U1) erzeugenden ersten Dekorrelationsfilters (E1) durch einen Koeffizientenabgleich
           neu eingestellt werden und bei dem der jeweils ermittelte
           Schätzwert (ZC) für das Echo (Z) vom Echo (Z) des Übertragungssystems (H) subtrahiert wird, wobei von einem
           zweiten Dekorrelationsfilter (F2) eine Aktualisierungsgröße
           (U2) für den genauen Koeffizientenabgleich des adaptiven
           Transversalfilters (HC) erzeugt und entsprechend dem
           NLMS-Algorithmus mit dem dekorrelierten Eingangssignalvektor (U1) in einer Update-Einrichtung (UPD) verknüpft
           wird,
           d a d u r c h g e k e n n z e i c h n e t , daß fortlaufend Korrektursignale (Γ; γ1, ...γM) gebildet und zu dem als Subtraktionsergebnis erhaltenen und in der Folge mit den Koeffizienten (a1, ...aM) des zweiten Dekorrelationsfilters (F2) transformierten Fehlersignals (E) an Stellen (So; S1, ... SM) des
           zweiten Dekorrelationsfilters (F2) addiert werden, und daß
           die Korrektursignale (Γ; γ1, ...γM) aus dem Eingangssignal
           (IN), den Koeffizienten (a1, ... aM) des zweiten Dekorrela-

                                      -4-



            tionsfilters (F2) und einer in der Update-Einrichtung (UPD)
            gebildeten Größe (λ) gebildet werden."


Der Anspruch 2 lautet:


        "2. Vorrichtung eingerichtet zur Durchführung des Verfahrens
            nach Anspruch 1."


Folgende Entgegenhaltungen haben in der mündlichen Verhandlung eine Rolle
gespielt:


        (4) AT E 30 821 B,


        (12) US 4 672 665,


        (15) The Transactions of the IECE of JAPAN, Vol. E 62, No. 12,
             Dezember 1979, S 851 bis 857.


                                        II


Der Anspruch 1 ist gewährbar, sein Gegenstand patentfähig.


1. Der Gegenstand des Anspruchs 1 gilt als neu.


Die lineare Echoverzerrung nach (12) und (15) stimmt lediglich in den Verfahrensschritten nach dem Oberbegriff des Anspruchs 1 mit der Erfindung überein. Das
zweite Dekorrelationsfilter 5, 8 bzw LP, TDL dekorreliert nicht das am Subtrahiererausgang anstehende Fehlersignal, sondern das Echo ((12) Fig 1, (15) Fig 2).
Oder aber, wenn dem zweiten Dekorrelationsfilter ein Vorhersagefehlersignal zugeführt wird, so liefert es keine Aktualisierungsgröße für die Update-Einrichtung 27, sondern das Fehlersignal am Ausgang 19 ((12) Fig 2).

                                       -5-



Der adaptive Echokompensator nach (4) bestimmt die Koeffizienten des zur Systemnachbildung verwendeten Transversalfilters 110 nicht aus Vorhersagefehlern
für das Eingangssignal - ein dekorreliertes Eingangssignal -, sondern aus dem
Eingangssignal (Fig 1).


2. Der Gegenstand des Anspruchs 1 gilt als auf einer erfinderischen Tätigkeit beruhend.


Wenn der Fachmann bei der Echoentzerrung nach (15) dem zweiten Dekorrelationsfilter LP, TDL das Fehlersignal e (t) zuführte und die dekorrelierte Ausgangsgröße, mit einer geeigneten Korrektur versehen, als Aktualisierungsgröße der Update-Einrichtung CL zuführte, so würde letztlich immer noch die Maßnahmen fehlen, erfolgsbedingend die Korrektursignale der Lehre des Anspruchs 1 gemäß zu
erzeugen.


Die Entgegenhaltung (4) zeigt zwar einen Korrektursignalgenerator 114. Als Eingangsgröße dienen dabei aber nur das Eingangssignal Xjund das Fehlersignal
ej. Er erzeugt lediglich eine Aktualisierungsgröße für die Echonachbildung 110,
stellt somit eine Update-Einrichtung dar, die einen Koeffizientenabgleich mit Hilfe
des Fehlersignals und des Eingangssignals vornimmt. Mit Dekorrelierung hat dies
nichts zu tun.


Die übrigen im Prüfungsverfahren noch genannten Entgegenhaltungen bringen
nicht mehr als die abgehandelten.


3. Die Anmeldung genügt PatG § 34.


Der Anspruch 1 gibt die entscheidende Richtung an. Die Angaben, die der Fachmann zur Ausführung der Erfindung benötigt, müssen nicht im Patentanspruch
enthalten sein. Es genügt, wenn sie sich aus dem Inhalt der Anmeldung ergeben
(BGH GRUR 2003, 223 - Kupplungsvorrichtung II).

                                        -6-



Die Erfindung ist in der Anmeldung so deutlich und vollständig offenbart, daß ein
Fachmann sie ausführen kann. Die Beschreibung läßt erkennen, wie er die Korrektursignale bilden kann.


Die Addition mit dem dekorrelierten Fehlersignal E zeigen ihm Fig 2, 3a und 3b.


Wie man die Korrektursignale gewinnen kann, zeigt Fig 4. Die hierfür nötigen Eingangsgrößen, nämlich das Eingangssignal in Form der Kurzzeit-AKF-Werte rµ, ν,
die Koeffizienten a1, ... aM des zweiten Dekorrelationsfilters und die Größe λ ergeben sich aus der ursprünglichen Anmeldungsbeschreibung und dem Fachwissen,
das anhand der in ihr am Anmeldetag dargestellten Literaturstelle (15) belegt ist.


Die Kurzzeit-AKF-Werte rµ, ν werden aus dem Eingangssignal berechnet (Sp 3
Z 45 bis 48). Die Koeffizienten a1, ... aM liefert der NMLS-Algorithmus durch lineare
Vorhersage ((15) Teil LP, Abschnitt 2.2). Dabei wird in der Update-Einrichtung die
Größe λ gemäß Gleichung (5) ((15) S 852) erzeugt, um entsprechend dem NMLS-Algorithmus den Update-Vektor hj+1 für das Transversalfilter zu erhalten (Offenlegungsschrift Sp 3 Z 39 bis 44).


4. Der Anspruch 2 ist gleichfalls gewährbar.


Das oben Gesagte gilt sinngemäß auch für ihn. Durch die auf den Anspruch 1 bezugnehmende Zweckangabe wird mittelbar umschrieben, daß die Vorrichtung derart im einzelnen ausgebildet ist, daß sie alle im Verfahrensanspruch 1 im einzelnen angegebenen Funktionen ausführen kann (BPatGE 40, 219).


Dr. Anders             Obermayer               Martens                Dr. Zehendner


                                                                               br/Be
