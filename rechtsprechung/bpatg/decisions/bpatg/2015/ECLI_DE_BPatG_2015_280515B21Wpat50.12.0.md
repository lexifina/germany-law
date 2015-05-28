---
ecli: "ECLI:DE:BPatG:2015:280515B21Wpat50.12.0"
court: "Bundespatentgericht"
spruchkoerper: "21"
aktenzeichen: "21 W (pat) 50/12"
decided: "2015-05-28"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2015&Sort=1&Seite=23&nr=27296&anz=851&pos=354&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2015-05-28_21_W-pat_50_12_NA_0.txt"
cites_law: ["germany/bund/acts/dpmav_2004/0001.md", "germany/bund/acts/patg/0034.md", "germany/bund/acts/patg/0042.md", "germany/bund/acts/patg/0073.md", "germany/bund/acts/patv/0015.md"]
---

# Bundespatentgericht, 21 W (pat) 50/12 vom 2015-05-28

## Entscheidung

BUNDESPATENTGERICHT


 21 W (pat) 50/12                                                   Verkündet am
_______________                                                     28. Mai 2015
    (Aktenzeichen)                                                       …




                              BESCHLUSS

                            In der Beschwerdesache




                 betreffend die Patentanmeldung 101 27 269.3


…




hat der 21. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 28. Mai 2015 unter Mitwirkung des Vorsitzenden
Richters    Dipl.-Phys. Dr. Häussler   sowie     der    Richter   Heimen   und
Dipl.-Phys. Dr. Müller und der Richterin Dipl.-Phys. Zimmerer




BPatG 154
05.11

                                         -2-



beschlossen:


        Der Beschluss der Prüfungsstelle für Klasse A 61 B des Deutschen Patent- und Markenamts vom 12. März 2012 wird aufgehoben und das Patent 101 27 269 erteilt.


        Bezeichnung: Verfahren für die Computertomographie sowie Computertomographie (CT)-Gerät


        Anmeldetag: 5. Juni 2001.


        Patentansprüche 1 bis 36 vom 6. Februar 2012 mit der Maßgabe,
        dass der Rückbezug in Anspruch 18 wie folgt geändert wird: „Ansprüche 16 bis 17“ statt „Ansprüche 15 bis 16“


        Beschreibungsseiten 1 bis 29, vom 6. Februar 2012


        Figuren 1, 3, 4, gemäß Schriftsatz vom 22. September 2005
        sowie Figuren 2, 5 bis 7 gemäß Offenlegungsschrift.




                                    Gründe


                                          I


Die Patentanmeldung mit dem Aktenzeichen 101 27 269.3 wurde am 5. Juni 2001
unter   der   Bezeichnung   "Verfahren        für   die   Computertomographie   sowie
Computertomographie (CT)-Gerät" beim Deutschen Patent- und Markenamt von
der S… Aktiengesellschaft, in M… angemeldet. Die Offenlegung
erfolgte am 30. Januar 2003.

                                         -3-



Die Prüfungsstelle für Klasse A 61 B hat die Patentanmeldung mit Beschluss vom
12. März 2012 zurückgewiesen, da die Unterlagen den Anforderungen des § 34
Abs. 3, Abs. 6 PatG i. V. m. § 15 Abs. 3 Satz 1 PatV nicht genügten.


Im Prüfungsverfahren sind folgende Druckschriften genannt:


D1    DE 198 82 203 T5
D2    TAGUCHI K., ARADATE H.: Algorithm for image reconstruction in multislice helical CT. In: Medical Physics, 1998, Vol. 25, No. 4, 550-561.
D3    HU H.: Multi-slice helical CT: Scan and reconstruction. In: Medical Physics,
      1999, Vol. 26, No. 1, 5-18.
D4    SCHALLER S., FLOHR T., STEFFEN P.: New, efficient Fourierreconstruction method for approximate image reconstruction in spiral conebeam CT at small cone angles. In: SPIE Medical Imaging Conference,
      1997, Vol. 3032, 213-224.
D5    SCHALLER S [u.a.]: Exact Radon Rebinning Algorithm for the Long Object
      Problem in Helical Cone-Beam CT. In: IEEE Transactions on Medical
      Imaging, 2000, Vol. 19, No. 5, 361-375.
D6    KUDO H., NOO F., DEFRISE M.: Cone-beam filtered-backprojection
      algorithm for truncated helical data. In: Physics in Medicine and Biology,
      1998, Vol. 43, 2885-2909.


Gegen den Beschluss richtet sich die Beschwerde der Anmelderin vom
28. März 2012, mit der sie sinngemäß beantragt


            den Beschluss der Prüfungsstelle für Klasse A61B des
             Deutschen Patent- und Markenamts aufzuheben und das
             Patent   mit   den     am    6. Februar 2012    eingereichten
             Ansprüchen 1 bis 36 zu erteilen
            hilfsweise die Patentanmeldung zur weiteren Prüfung an das
             Deutsche Patent- und Markenamt zurück zu verweisen.

                                        -4-



Der geltende Patentanspruch 1 lautet:


       1.   Verfahren für die Computertomographie, aufweisend die
            Verfahrensschritte
       a)   zur Abtastung eines Objekts mit einem von einem Fokus
            ausgehenden konusförmigen Strahlenbündel und mit einem
            matrixartigen    Detektorarray    zum      Detektieren   des
            Strahlenbündels wird der Fokus relativ zu dem Objekt auf
            einer Spiralbahn um eine Systemachse bewegt, wobei das
            Detektorarray der empfangenen Strahlung entsprechende
            Ausgangsdaten liefert,
       b)   die jeweils während der Bewegung des Fokus auf einem
            Spiralsegment mit zur Rekonstruktion eines CT-Bildes
            ausreichender Länge gelieferten Ausgangsdaten werden in
            Ausgangsdaten bezüglich Untersegmenten aufgeteilt, wobei
            die Länge der Untersegmente jeweils geringer als die zur
            Rekonstruktion eines CT-Bildes ausreichende Länge ist,
       c)   für die Untersegmente werden Segmentbilder mit bezüglich
            der Systemachse geneigter Bildebene rekonstruiert,
       d)   die jeweils zu einem Untersegment gehörigen Segmentbilder
            werden zu einem Teilbild bezüglich einer Zielbildebene
            zusammengefasst, und
       e)   die Teilbilder werden zu einem resultierenden CT-Bild
            bezüglich der Zielbildebene zusammengefasst.


Daran schließen sich die Unteransprüche 2 bis 18 an.


Der geltende Patentanspruch 19 lautet:


       19. Computertomographie(CT)-Gerät            aufweisend       eine
            Strahlungsquelle, von deren Fokus ein konusförmiges

                                     -5-



     Strahlenbündel ausgeht, ein matrixartiges Detektorarray zum
     Detektieren des Strahlenbündels, wobei das Detektorarray
     der empfangenen Strahlung entsprechende Ausgangsdaten
     liefert, Mittel zum Erzeugen einer Relativbewegung zwischen
     Strahlungsquelle und Detektorarray einerseits und einem
     Objekt   andererseits          und    einen    Rechner,   dem     die
     Ausgangsdaten zugeführt sind, wobei die Mittel zum
     Erzeugen einer Relativbewegung zur Abtastung des Objekts
     mit   dem   Strahlenbündel           und   dem    zweidimensionalen
     Detektorarray eine Relativbewegung des Fokus zu einer
     Systemachse derart bewirken, dass sich der Fokus relativ zu
     der Systemachse auf einer Spiralbahn um die Systemachse
     bewegt, und wobei die jeweils während der Bewegung des
     Fokus auf einem Spiralsegment gelieferten Ausgangsdaten
     einem Rechner zugeführt sind, wobei
a)   der Rechner die jeweils während der Bewegung des Fokus
     auf einem Spiralsegment mit zur Rekonstruktion eines CT-Bildes ausreichender Länge gelieferten Ausgangsdaten in
     Ausgangsdaten bezüglich Untersegmenten aufteilt, wobei die
     Länge der Untersegmente jeweils geringer als die zur
     Rekonstruktion eines CT-Bildes ausreichende Länge ist,
b)   der Rechner für die Untersegmente Segmentbilder mit
     bezüglich        der        Systemachse       geneigter   Bildebene
     rekonstruiert,
c)   der Rechner die jeweils zu einem Untersegment gehörigen
     Segmentbilder          zu     einem    Teilbild    bezüglich    einer
     Zielbildebene zusammengefasst, und
d)   der Rechner die Teilbilder zu einem resultierenden CT-Bild
     bezüglich der Zielbildebene zusammengefasst.

                                          -6-



Daran schließen sich die Unteransprüche 20 bis 36 an.


Wegen der weiteren Einzelheiten wird auf den Akteninhalt Bezug genommen.




                                           II


Die Beschwerde ist zulässig, insbesondere ist sie statthaft sowie form- und fristgerecht eingelegt (§ 73 Abs. 1, Abs. 2 PatG).


Die Beschwerde ist auch begründet, denn das zweifelsohne gewerblich anwendbare Verfahren nach den geltenden Anspruch 1 und das Computertomographie(CT)-Gerät nach dem geltenden Anspruch 19 sind neu und beruhen auf einer
erfinderischen Tätigkeit. Die Unteransprüche betreffen vorteilhafte Ausgestaltungen und die übrigen Unterlagen erfüllen insgesamt die an sie zu stellenden Anforderungen.


1.
Die nebengeordneten Patentansprüche 1 und 19, sowie die Unteransprüche 2 bis
18 und 20 bis 38 sind zulässig, denn sie finden eine ausreichende Stütze in der
ursprünglichen Offenbarung.


Die nebengeordneten Patentansprüche 1 und 19 sind den ursprünglichen
Patentansprüchen 1     und    31,   sowie       der   ursprünglichen   Beschreibung,
insbesondere S. 14 Zeile 33, zu entnehmen.


Die Patentansprüche 2 bis 18 und 20 bis 36 gehen auf die ursprünglichen Patentansprüche 3 bis 5, 7, 9, 12 bis 17, 19 bis 21, 28 bis 31, 33 bis 35, 37, 39, 42
bis 47, 49 bis 51 und 58 bis 60 zurück.
In den geltenden Ansprüchen 3 und 21 wurde zur Klarstellung eingefügt, dass für
unterschiedliche z-Positionen die Bildebenen unterschiedlich geneigt sind. Dieses

                                       -7-



Merkmal ergibt sich beispielsweise aus der Beschreibung zur Fig. 4. Die übrigen
Unteransprüche enthalten lediglich Änderungen in den Rückbezügen.


2.
Die vorliegende Patentanmeldung betrifft ein Verfahren für die Computertomographie, aufweisend die Verfahrensschritte, dass zur Abtastung eines Objekts mit
einem von einem Fokus ausgehenden konusförmigen Strahlenbündel und mit einem matrixartigen Detektorarray zum Detektieren des Strahlenbündels der Fokus
relativ zu dem Objekt auf einer Spiralbahn um eine Systemachse bewegt wird,
wobei das Detektorarray der empfangenen Strahlung entsprechende Ausgangsdaten liefert, und dass aus jeweils während der Bewegung des Fokus auf einem
Spiralsegment gelieferten Ausgangsdaten Bilder mit relativ zu der Systemachse
geneigten Bildebene rekonstruiert werden (vgl. Offenlegungsschrift Absatz [0001]).


Die Erfindung betrifft außerdem ein Computertomographie(CT)-Gerät aufweisend
eine Strahlungsquelle, von deren Fokus ein konusförmiges Strahlenbündel aus
geht, ein matrixartiges Detektorarray zum Detektieren des Strahlenbündels, wobei
das Detektorarray der empfangenen Strahlung entsprechende Ausgangsdaten
liefert, Mittel zum Erzeugen einer Relativbewegung zwischen Strahlungsquelle
und Detektorarray einerseits und einem Objekt andererseits und einen Bildrechner, dem die Ausgangsdaten zugeführt sind, wobei die Mittel zum Erzeugen einer
Relativbewegung zur Abtastung des Objekts mit dem Strahlenbündel und dem
zweidimensionalen Detektorarray eine Relativbewegung des Fokus zu einer Systemachse derart bewirken, dass sich der Fokus relativ zu der Systemachse auf
einer schraubenlinienförmigen Spiralbahn bewegt, deren Mittelachse der Systemachse entspricht, und wobei der Bildrechner aus jeweils während der Bewegung
des Fokus auf einem Spiralsegment gelieferten Ausgangsdaten Bilder mit relativ
zu der Systemachse geneigter Bildebene rekonstruiert (vgl. Offenlegungsschrift
Absatz [0001]).

                                        -8-



Nach den Ausführungen in der Beschreibungseinleitung sind insbesondere im Zusammenhang mit mehrere Zeilen von Detektorelementen aufweisenden Detektorarrays verschiedene CT-Verfahren unter Verwendung konusförmiger Röntgenstrahlenbündel bekannt geworden. Dabei wird dem infolge der konusförmigen Gestalt des Röntgenstrahlenbündels auftretenden Conewinkel in unterschiedlicher
Weise Rechnung getragen (vgl. Offenlegungsschrift Absatz [0002]).
In der Patentanmeldung werden bekannte Algorithmen genannt, die jedoch
Nachteile aufwiesen: So werden Conewinkel vernachlässigt, wodurch bei einer
großen Anzahl von Zeilen mit großem Conewinkel Artefakte auftreten. Weiter sei
beim sogenannten MFR-Algorithmus nachteilig, dass eine aufwendige Fourierrekonstruktion notwendig sei und die Bildqualität unbefriedigend sei. Außerdem
seien exakte Algorithmen bekannt, die jedoch extrem aufwendige Rekonstruktion
erforderten (vgl. Offenlegungsschrift Absatz [0003]-[0005]).
Weiter wird auf die US 5 802 134 verwiesen, bei der jedoch das Problem bestehe,
dass unterhalb des maximalen Pitch (d.h. des Vorschubs pro Umdrehung) eine
optimale Nutzung der zur Verfügung stehenden Detektorfläche und damit der dem
Patienten zugeführten Strahlendosis zur Bildgewinnung (Detektor- und damit Dosisnutzung) nicht möglich sei (vgl. Offenlegungsschrift Absatz [0006]-[0008]).


Vor dem Hintergrund des in der Beschreibungseinleitung genannten Standes der
Technik liegt der vorliegenden Erfindung die in der Patentanmeldung angegebene
Aufgabe zugrunde, ein Verfahren und ein CT-Gerät der eingangs genannten Art
so auszubilden, dass einerseits dem Conewinkel Rechnung getragen wird und
andererseits auch für Werte des Pitch unterhalb des maximalen Pitch die Voraussetzungen für eine optimale Detektor- und damit Dosisnutzung gegeben sind (Absatz [0009] der Offenlegungsschrift).


Als Lösung der Aufgabe wird ein Verfahren für die Computertomographie nach
Anspruch 1 und ein Computertomographie(CT)-Gerät nach Anspruch 19 vorgeschlagen (siehe geltende Patentansprüche).

                                      -9-



Hierbei werden zunächst das Spiralsegment in Untersegmente aufgeteilt und bezüglich dieser Untersegmente Segmentbilder rekonstruiert, wodurch die Abweichungen der Bildebenen der Segmentbilder von der Spiralbahn längs der Untersegmente sehr klein sind, so dass die Segmentbilder nur sehr geringe durch Abweichungen der Bildebenen der Segmentbilder von der Spiralbahn längs der Untersegmente verursachte Fehler enthalten und somit die bei der Erzeugung des
resultierenden CT-Bildes zu erwartende Bildqualität hoch ist. Die maximale Neigung der Bildebenen der Segmentbilder bestimmt sich aus der Bedingung, dass
an beiden Enden eines Untersegments innerhalb des Messfeldes Strahlen für die
Bildebene des jeweiligen Segmentbildes vorhanden sein müssen (vgl. Offenlegungsschrift Absatz [0011]-[0012]).


Die Figur 4 der Patentanmeldung zeigt die Bildebenen der zu einem Untersegment gehörigen Segmentbilder:




3.
Die Vorrichtungen nach den Patentansprüchen 1 und 19 sind gegenüber dem im
Verfahren befindlichen Stand der Technik neu und ergeben sich für den
Fachmann, einem berufserfahrenen Diplom-Physiker mit Erfahrung in der

                                       - 10 -



Entwicklung von Röntgencomputertomographiegeräten und Verfahren hierzu auch
nicht in nahe liegender Weise.


3.1
Wie bereits im Prüfungsverfahren festgestellt und vom Senat im Einzelnen geprüft,
ist den im Verfahren befindlichen Druckschriften D1 bis D6 kein Verfahren gemäß
Anspruch 1 zu entnehmen ist und diese Druckschriften legen weder einzeln noch
in ihrer Zusammenschau dem Fachmann ein derartiges Verfahren nahe. Dies gilt
analog auch für die Vorrichtung nach Anspruch 19.


3.2
Die Unteransprüche 2 bis 18 und 20 bis 36 betreffen vorteilhafte Ausgestaltungen
der Ansprüche 1 und 19, und die übrigen Unterlagen erfüllen insgesamt die an sie
zu stellenden Anforderungen.


4.
Im vorliegenden Fall stützt sich der Zurückweisungsbeschluss auf § 15 Abs. 1
Satz 1 PatV, wonach der Anmelder im Einzelnen anzugeben hat, an welcher
Stelle die in den neuen Unterlagen beschriebenen Erfindungsmerkmale in den
ursprünglichen Unterlagen offenbart sind. Die Prüfungsstelle verweist darauf, dass
dies eine notwendige Verfahrensvoraussetzung für die Prüfung der im
Patentgesetz festgelegten Patentierungsvoraussetzungen darstellt, so dass eine
Verletzung dieser Vorschrift die Zurückweisung der Anmeldung tragen könne.


Die Prüfungsstelle verweist auf die Entscheidung BPatG München, Beschluss vom
17. März 2010 – 7 W (pat) 33/04. Hiernach ist die Vorschrift des § 42 PatG i. V. m.
§ 34 Abs. 6, § 1 Abs. 2 DPMAV und §§ 1 ff. PatV verfassungskonform so
auszulegen,    dass   nur    die    Verletzung   solcher     Formvorschriften   eine
Zurückweisung aus formellen Gründen tragen können, die entweder im Gesetz
ausdrücklich   bestimmt     sind,   oder   zu    deren     Normierung   durch   den
Verordnungsgeber das Gesetz ausdrücklich ermächtigt oder die für die

                                        - 11 -



Gewährung des staatlichen Schutzes der angemeldeten Erfindung, also für die
Sachprüfung und die Patenterteilung, unumgänglich sind.
Dies ist jedoch im vorliegenden Einzelfall nicht gegeben. Der Sachprüfung und der
Patenterteilung steht nicht entgegen, dass die Anmelderin nicht im Einzelnen die
Textstelle auf der die Änderungen beruhen, angegeben hat. Die Anmelderin
erläuterte zu den Änderungen in der Eingabe vom 20. September 2005, dass der
überarbeitete Anspruch 4 dem bisherigen Anspruch 4 entspricht, „welcher zum
besseren Verständnis dahingehend umformuliert wurde, dass deutlich wird, dass
für jedes Untersegment Segmentbilder für eine Anzahl n ima von geneigten
Bildebenen rekonstruiert werden, wobei für unterschiedliche z-Positionen zima die
Bildebenen unterschiedlich geneigt sind.“ Mit dieser Angabe und den ursprünglich
eingereichten Unterlagen ist die Prüfungsstelle in der Lage zu beurteilen, ob der
geänderte Anspruch unzulässig erweitert wurde. Hierfür reichen die vorgelegten
Ansprüche und die ursprüngliche Beschreibung aus. Ob und mit welcher
Anspruchsfassung     der   begehrte     Schutz   tatsächlich   gewährbar   ist,    ist
demgegenüber eine Frage der Sach- und nicht der Formalprüfung. Die Angabe
der Textstellen ist im vorliegenden Fall für die Sachprüfung nicht unumgänglich.


Eine Prüfung auf unzulässige Erweiterung wird durch eine fehlende oder
ungenaue Angabe der zugrundeliegenden Textstellen lediglich erschwert und führt
gegebenenfalls zur Rechtsfolge der unzulässigen Erweiterung. Somit kann die
fehlende oder ungenaue Angabe der Offenbarung der Änderung in einer
Anspruchsfassung keine Zurückweisung der Patentanmeldung tragen.


5.
Die Änderung des Anspruchs 18 durch den Senat, wonach


        der Rückbezug in Anspruch 18 wie folgt geändert wird: „Ansprüche 16 bis 17“ statt „Ansprüche 15 bis 16“


behebt einen offensichtlichen Fehler.

                                      - 12 -



Der im Anspruch 18 verwendete Begriff „homogene Pixelmatrix“ wurde in
Unteranspruch 16 erstmalig als Teil des Verfahrens beansprucht:


        16. Verfahren nach einem Anspruch 15, bei dem die Komprimierung im
        Zuge der Zusammenfassung der Teilbilder zu einem eine homogene
        Pixelmatrix aufweisenden resultierenden CT-Bild aufgehoben wird.


Offensichtlich kann sich das Verfahren nach Anspruch 18, das diese homogene
Pixelmatrix präzisiert, somit lediglich auf Unteranspruch 16 und den sich darauf
bezogenen Anspruch 17, beziehen.
Die vorgenommene geänderte Rückbeziehung in Patentanspruch 18 auf die
Patentansprüche 16 bis 17 stellt daher eine bloße Korrektur einer offensichtlichen
Unrichtigkeit dar.




                                        III


                       Rechtsmittelbelehrung


Gegen diesen Beschluss ist für jede am Beschwerdeverfahren beteiligte Person
das Rechtsmittel der Rechtsbeschwerde gegeben, wenn gerügt wird, dass


1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der Befangenheit mit Erfolg abgelehnt war,
3. einem Beteiligten das rechtliche Gehör versagt war,
4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
  sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
  zugestimmt hat,

                                      - 13 -



5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
  Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
6. der Beschluss nicht mit Gründen versehen ist.


Die Rechtsbeschwerdeschrift muss von einer beim Bundesgerichtshof zugelassenen Rechtsanwältin oder von einem beim Bundesgerichtshof zugelassenen
Rechtsanwalt unterzeichnet und innerhalb eines Monats nach Zustellung des Beschlusses beim Bundesgerichtshof, Herrenstraße 45a, 76133 Karlsruhe eingereicht werden. Die Frist ist nur gewahrt, wenn die Rechtsbeschwerde vor Fristablauf beim Bundesgerichtshof eingeht. Die Frist kann nicht verlängert werden.




Dr. Häußler                Heimen                  Dr. Müller            Zimmerer


                                                                               prö
