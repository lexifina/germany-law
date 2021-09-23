---
ecli: "ECLI:DE:BPatG:2021:230921B17Wpat29.19.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 29/19"
decided: "2021-09-23"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2021&Sort=1&Seite=28&nr=41896&anz=599&pos=432&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2021-09-23_17_W-pat_29_19_NA_0.txt"
---

# Bundespatentgericht, 17 W (pat) 29/19 vom 2021-09-23

## Entscheidung

BUNDESPATENTGERICHT



 17 W (pat) 29/19
_______________________

    (Aktenzeichen)




                                  BESCHLUSS

                                 In der Beschwerdesache


                betreffend die Patentanmeldung 10 2014 003 463.1


…
hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts am
23.    September          2021   unter   Mitwirkung   des   Vorsitzenden   Richters
Dipl.-Phys. Dr. Morawek, der Richterin Bayer, des Richters Dipl.-Ing. Baumgardt
und des Richters Dr.-Ing. Harth




ECLI:DE:BPatG:2021:230921B17Wpat29.19.0

                                      -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der
       Prüfungsstelle für Klasse G 06 T des Deutschen Patent- und
       Markenamts vom 27. September 2018 aufgehoben und die Sache
       zur weiteren Prüfung und Entscheidung an das Deutsche Patentund Markenamt zurückverwiesen.




                                   Gründe


                                       I.


Die vorliegende Patentanmeldung, welche die Priorität einer Voranmeldung in den
USA vom 14. März 2013 in Anspruch nimmt, wurde am 11. März 2014 beim
Deutschen Patent- und Markenamt in deutscher Sprache eingereicht. Sie trägt die
Bezeichnung:


               „ 3D-Graphik-Wiedergabe mit impliziter Geometrie “.


Die Anmeldung wurde durch Beschluss der Prüfungsstelle für Klasse G 06 T des
Deutschen Patent- und Markenamts in der Anhörung vom 27. September 2018 mit
der Begründung zurückgewiesen, dass auch nach Würdigung des Vorbringens der
Anmelderin im Prüfungsverfahren die Patentbegehren gemäß des Hauptantrags
und der (in der Anhörung geltenden) Hilfsanträge 1-9 nicht gewährbar seien, da
die Gegenstände der jeweiligen Patentansprüche 1 zumindest nicht als auf einer
erfinderischen Tätigkeit beruhend gälten. Ob die jeweils beanspruchten Gegenstände überhaupt ein konkretes technisches Problem mit technischen Mitteln

                                       -3-



lösten und damit den Patentierungsausschluss gemäß § 1 Abs. 3 i.V.m. Abs. 4
PatG überwänden, könne daher dahingestellt bleiben.


Gegen diesen Beschluss ist die Beschwerde der Anmelderin gerichtet. Sie reicht
mit ihrer Beschwerdebegründung neu formulierte Anspruchssätze in Form eines
Hauptantrags und eines Hilfsantrags ein und erläutert, dass jedenfalls für die
neuen Anträge das Technizitätserfordernis erfüllt sei und auch jeweils alle
Anspruchsmerkmale der Lösung eines technischen Problems mit technischen
Mitteln dienten, so dass sie bei der Prüfung auf erfinderische Tätigkeit vollständig
zu berücksichtigen seien.


Die Anmelderin stellt mit der Eingabe vom 27. August 2021 (sinngemäß) den
Antrag,


  A.1) den Zurückweisungsbeschluss aufzuheben und ein Patent mit den
          Ansprüchen 1 bis 19 gemäß Hauptantrag vom 11. Januar 2021 zu
          erteilen,


  A.2) hilfsweise, den Beschluss aufzuheben und die Anmeldung mit den
          Unterlagen gemäß Hauptantrag an das Deutsche Patent- und
          Markenamt zurückzuverweisen,


  A.3) weiter hilfsweise, den Beschluss aufzuheben und ein Patent mit
          den Ansprüchen 1 bis 24 gemäß Hilfsantrag vom 11. Januar 2021
          zu erteilen,


  B)      und, sofern weder dem Antrag gemäß A.1 noch dem Antrag
          gemäß A.2 im schriftlichen Verfahren stattgegeben werden kann,
          eine mündliche Verhandlung anzuberaumen.

                                          -4-



Gemäß Hauptantrag lautet der geltende Patentanspruch 1, mit einer möglichen
Gliederung und mit Kennzeichnung der Unterschiede zum ursprünglichen Patentanspruch 18:


      S1       1. 18. Ray-Tracing System zum Rendern eines Bildes einer
               3-D Szene, wobei das Ray-Tracing System konfiguriert ist
               zum Prüfen eines Strahls auf einen Schnittpunkt mit einer
               impliziten Oberfläche einer implizit definierten Geometrie, die
               in der zu rendernden Szene enthalten ist und wobei das Ray-Tracing System umfasst umfassend:


      S2       einen Cluster von programmierbaren Ausführungseinheiten,
               die einen Schattierercode ausführen können, der während
               der Ausführung auf den Schnittpunkt in einer der 3D-Szene
               zu prüfende Strahlen emittiert;


      S3       mehrere Prüfzellen zum Prüfen von einem oder mehreren
               Strahlen   [auf   Schnittpunkte]   mit   Grundelementen,   die
               Objekte bilden, die in der 3D-Szene angeordnet sind;


      S4       mehrere lokale Speicher, die jeweiligen Prüfzellen zugeordnet sind; und


      S5       mehrere programmierbare Schaltungen, die mit jeweiligen
               Prüfzellen gekoppelt sind, wobei die programmierbaren
               Schaltungen ausgelegt werden können sind,


      S5a      um den Strahl iterativ schrittweise durch das 3-D Volumen in
               der 3D-Szene zu führen, wobei die Schrittweite des schrittweisen Führens jeweils basierend auf einem Strahldifferential oder einen Detailniveauindikator festgelegt ist,

                                       -5-



      S5b   und für die jeweils aktuelle 3D Position die Funktion auszuwerten, die die Anwesenheit oder Abwesenheit des Schnittpunkts des Strahls mit der implizit definierten Oberfläche
            innerhalb des Volumens angibt,


      S6    wobei die Auswertung der Funktion, die die Anwesenheit
            oder Abwesenheit des Schnittpunkts des Strahls mit der
            implizit definierten Oberfläche innerhalb des Volumens
            angibt, zum Rendern eines Bilds der Szene verwendet wird.



Der geltende Patentanspruch 5 des Hauptantrags lautet, mit Kennzeichnung der
Unterschiede zum ursprünglichen Anspruch 1 und angepasster Gliederung:


      M0    5. 1. Verfahren zum Rendern eines Bildes einer 3-D Szene
            mit einem Ray-Tracing System nach einem der Ansprüche 1
            bis 4, wobei das Verfahren umfasst:


      M1‘   Verfahren zum Prüfen eines Strahls auf einen Schnittpunkt
            mit einer impliziten Oberfläche einer implizit definierten
            Geometrie, die in der zu rendernden Szene enthalten ist,
            umfassend:


      M1a   wobei das Prüfen durch eine Berechnungseinheit des Ray-Tracing Systems erfolgt und wobei das Prüfen umfasst:


      M2‘   Eintreten in eine Oberfläche einer Hülle, die ein 3D-Volumen
            begrenzt, mit dem Strahl, wobei die Hülle eine maximale
            Ausdehnung für eine die implizit definierte Geometrie
            innerhalb der Hülle definiert;

                                       -6-



      M3    iteratives schrittweises Führen einer aktuellen 3D-Position
            des Strahls entlang seines Weges durch das 3D-Volumen,
            das von der Hülle definiert ist,


      M3a   wobei die Schrittweite des iterativen schrittweisen Führens
            basierend auf einem Strahldifferential oder einem Detailniveauindikator festgelegt ist;


      M4    für jede aktuelle 3D-Position:


      M4a   Projizieren der aktuellen 3D-Position des Strahls auf eine
            aktuelle 2D-Position auf einer explizit definierten Oberfläche,
            die in der Hülle begrenzt ist,


      M4b Erzeugen von Daten für die implizit definierte Geometrie
            unter Verwendung der aktuellen 2D-Position auf der explizit
            definierten Oberfläche, und


      M4c‘ Charakterisieren des Strahls als entweder die implizit
            definierte Geometrie in der aktuellen 3D-Position treffend
            oder verfehlend unter Verwendung der erzeugten Daten; und


      M5    Verwenden der Charakterisierung des Strahls als entweder
            die implizit definierte Geometrie in der aktuellen 3D-Position
            treffend oder verfehlend zum Rendern des Bilds der 3-D
            Szene.


Zu den Unteransprüchen 2 bis 4 und 6 bis 19 wird auf die Akte verwiesen.


Zum Wortlaut des Hilfsantrags wird ebenfalls auf die Akte verwiesen.

                                        -7-



Eine konkrete Aufgabe ist in der Anmeldung nicht angegeben. In der Eingabe
vom 16. Oktober 2015 erklärt die Anmelderin (bezüglich des damals geltenden
Patentbegehrens): „Die Ansprüche sind darauf gerichtet das technische Problem
zu lösen, wie man eine hoch-detaillierte Geometrie beim Raytracing erreicht, wenn
man nur beschränkt viel Speicherplatz zur Verfügung hat, der benutzt wird, um
diese Geometrie zu speichern (einer von mehreren Vorteilen).“




                                         II.


Die rechtzeitig eingegangene und auch sonst zulässige Beschwerde führt zur
Aufhebung des angegriffenen Beschlusses und zur Zurückverweisung der Sache
an das Deutsche Patent- und Markenamt gemäß PatG § 79 Abs. 3 Satz 1 Nr. 1.


1.    Die vorliegende Anmeldung betrifft das Gebiet der Computergrafik, hier die
Bildsynthese und speziell das Berechnen („Rendern“) von photorealistischen
zweidimensionalen Bildern für dreidimensionale Szenen, die aus Computererzeugten Szenarien heraus entstehen, wie z.B. bei 3D-Architekturprogrammen
oder bei Computerspielen. In diesem Kontext wird bekanntermaßen die Verfolgung virtueller Lichtstrahlen durch eine virtuelle Szene hindurch („Ray-Tracing“)
zur Verdeckungsberechnung und z.B. Simulation von Lichtreflexionen eingesetzt,
wobei die Lichtstrahlen auf Schnittpunkte mit den computergenerierten Objekten,
welche die dreidimensionale Szene definieren, geprüft werden.


Das beanspruchte Ray-Tracing System soll konfiguriert sein zum Prüfen eines
(virtuellen) Strahls auf einen Schnittpunkt mit einer Oberfläche einer implizit definierten Geometrie, die in der zu rendernden Szene enthalten ist. Wie dem Fachmann geläufig war, benötigen Berechnungen auf Basis von expliziten Oberflächen, z.B. ausgehend von dreieckigen Grundelementen, relativ viel Speicher
und dementsprechend auch viel Rechenzeit. Sie bieten zwar u.U. Vorteile bei der

                                         -8-



Strahlverfolgung im Ray-Tracing, sind aber zu aufwändig für Bilder mit HD-Auflösung von virtuellen 3D-Szenen. Die Verwendung implizit definierter Oberflächen habe im Vergleich zu explizit definierten Oberflächen den Vorteil eines
geringeren Speicherverbrauchs (vgl. Offenlegungsschrift Absatz [0003]).


Solche implizit definierten Oberflächen können beispielsweise ausgehend von
einer Referenzgeometrie durch eine „Verlagerungsabbildung“ („displacement
mapping“) in Form einer Verschiebung explizit definierter Geometriedaten erzeugt
werden und bilden damit eine „verlagerte Geometrie“, die einfacher zu berechnen
sein kann als die explizite Geometrie (Absatz [0004]).


Hierfür soll das beanspruchte Ray-Tracing System einen Cluster von programmierbaren Ausführungseinheiten umfassen, die einen Schattierercode ausführen
können, der während der Ausführung auf den Schnittpunkt in der 3D-Szene zu
prüfende Strahlen emittiert; und mehrere Prüfzellen, mit jeweils zugeordneten
lokalen Speichern, zum Prüfen von einem oder mehreren Strahlen (gemeint ist
wohl: auf Schnittpunkte) mit Grundelementen, die Objekte bilden, die in der 3D-Szene angeordnet sind.


Dabei soll der einzelne Strahl iterativ schrittweise durch das 3-D Volumen in der
3D-Szene geführt werden, und für die jeweils aktuelle 3D-Position des Strahls soll
eine Funktion ausgewertet werden, die angibt, ob der Strahl die implizit definierte
Oberfläche innerhalb des Volumens schneidet oder nicht, wobei diese Auswertung
zum Rendern eines Bilds der Szene verwendet wird. Die Schrittweite des schrittweisen Führens soll jeweils basierend auf einem Strahldifferential oder einem
Detailniveauindikator festgelegt sein.


Wie die Anmelderin erläutert hat, gibt ein „Strahldifferential“ den Unterschied
zwischen benachbarten Schnittpunkten für benachbarte Strahlen an. Beispielsweise werde ein Strahl, der eine Oberfläche unter einem Winkel trifft, der nahezu
parallel zur Oberflächennormalen ist, ein geringeres Strahldifferential aufweisen

                                       -9-



als ein Strahl, der die Oberfläche nahezu senkrecht zur Oberflächennormalen trifft;
ein Schritt entlang des Strahls werde bei einem hohen Strahldifferential einem
größeren Schritt entlang einer Oberfläche entsprechen als bei einem relativ geringen Strahldifferential.


Ein „Detailniveauindikator“ gibt an, mit welchem Detailgrad die Geometrie gerendert wird. Bei einer Geometrie mit hohem Detailniveauindikator könnten mehr
Details zwischen aufeinander folgenden Schritten des Strahls bzw. entlang des
Strahls vorhanden sein.


Auf diese Weise sei es nach dem Vortrag der Anmelderin möglich, die Menge der
durch die programmierbaren Schaltungen vorzunehmenden Berechnungen
adäquat an die jeweiligen Erfordernisse anzupassen und unnötige Berechnungen
zu vermeiden, was die Rechenzeit verkürze und den Energieverbrauch des
Systems reduziere.


Als Fachmann, der mit der Aufgabe betraut wird, verbesserte Ray-Tracing-Verfahren mit geringerer Ressourcen-Belastung zu erarbeiten, sieht der Senat einen
Diplominformatiker mit mehrjähriger Berufserfahrung auf dem Gebiet der Entwicklung von Computergrafikalgorithmen und der Optimierung der dafür benötigten
Hardware an.



2.     Der geltende Patentanspruch 1 gemäß Hauptantrag ist zulässig. Auch die
übrigen Patentansprüche des Hauptantrags stoßen insoweit auf keine Bedenken,
mit Ausnahme des Unteranspruchs 9, der eine Überbestimmung darstellt.


2.1    Der geltende Patentanspruch 1 des Hauptantrags geht auf den ursprünglichen Anspruch 18 zurück. Die Ergänzungen in Merkmal S1 „Ray-Tracing System
zum Rendern eines Bildes einer 3-D Szene“ kann sich etwa auf Abs. [0002] der
Offenlegungsschrift stützen, in Verbindung mit dem Wissen des Fachmanns, dass
das z.B. in den Abs. [0002] bis [0004], Abs. [0032], Abs. [0078] / [0079] u.a. ge-

                                        - 10 -



nannte „Wiedergeben“ von Bildern mit dem Fachausdruck „Rendern“ bezeichnet
wird. Bei der weiteren Ergänzung „Schnittpunkt mit einer Oberfläche einer implizit
definierten Geometrie“ handelt es sich um eine Klarstellung, vgl. z.B. Abs. [0005].


Die Ergänzung in den Merkmalen S5a und S5b „um den Strahl iterativ schrittweise
durch das 3-D Volumen in der 3D-Szene zu führen… und für die jeweils aktuelle
3D Position die Funktion auszuwerten…“ entspricht den detaillierten Verfahrensschritten im ursprünglichen Verfahrensanspruch 1; die neue Beschränkung „wobei
die Schrittweite des schrittweisen Führens jeweils basierend auf einem Strahldifferential oder einen Detailniveauindikator festgelegt ist“ geht auf Abs. [0041]
zurück bzw. zum Teil auf den ursprünglichen Unteranspruch 5.


Das neue Merkmal S6 „wobei die Auswertung der Funktion, die die Anwesenheit
oder Abwesenheit des Schnittpunkts des Strahls mit der implizit definierten Oberfläche innerhalb des Volumens angibt, zum Rendern eines Bilds der Szene verwendet wird“ ergibt sich im vorliegenden Kontext für den Fachmann ganz zwangsläufig, vgl. etwa Abs. [0037] oder Abs. [0067].


2.2   Der Verfahrensanspruch 5 geht auf den ursprünglichen Anspruch 1 zurück.
Die Ergänzung durch Merkmal M0, dass das Prüfen eines Strahls auf
Schnittpunkte „zum Rendern eines Bildes einer 3-D Szene“ erfolgen soll, mittels
eines Ray-Tracing Systems, ergibt sich wie beim zuvor abgehandelten System-Anspruch (Merkmal S1) aus dem Wissen des Fachmanns. Ebenso stellen die
ergänzten Merkmale M1a und M5 lediglich einen Bezug auf die Anwendung
innerhalb eines technischen Systems her, der sich (wie oben für die Merkmale S1
und S6 des Anspruchs 1 ausgeführt) im vorliegenden Kontext für den Fachmann
ganz zwangsläufig ergibt.


Bei der Ergänzung in Merkmal M1‘ „Schnittpunkt mit einer Oberfläche einer implizit definierten Geometrie, die in der zu rendernden Szene enthalten ist“ handelt es
sich um eine Klarstellung, vgl. z.B. Abs. [0005].

                                       - 11 -



Die Beschränkung der beanspruchten Lehre durch das neue Merkmal M3a „wobei
die Schrittweite des iterativen schrittweisen Führens basierend auf einem Strahldifferential oder einen Detailniveauindikator festgelegt ist“ geht auf Abs. [0041]
zurück bzw. zum Teil auf den ursprünglichen Unteranspruch 5.


2.3   Die Unteransprüche 2, 3 und 4 entsprechen den (angepassten) ursprünglichen Ansprüchen 19, 20 bzw. 21.


Die Unteransprüche 6 bis 19 entsprechen den (angepassten) ursprünglichen
Ansprüchen 2 bis 15. Allerdings ist der geltende, auf den Verfahrensanspruch 5
zurückbezogene Unteranspruch 9 des Hauptantrags auf das „Festlegen einer
Schrittgröße, die beim iterativen schrittweisen Führen verwendet wird, gemäß
einer Detailniveauangabe“ gerichtet und stellt somit nach dem Verständnis des
Senats, da diese Lehre bereits im zweiten Teil des Merkmals M3a des übergeordneten Anspruchs 5 enthalten ist, eine Überbestimmung dar.


2.4   Der Senat geht davon aus, dass der oben definierte Durchschnittsfachmann
auf diesem Gebiet aufgrund seines Fachwissens auch in der Lage ist, die beanspruchte Lehre auszuführen. Etwaige Zweifel, z.B. hinsichtlich der Frage, was
genau durch das „iterativ“ des Merkmals S5a ausgedrückt werden soll, und wann
genau eine „implizit definierte Geometrie“ bzw. „implizit definierte Oberfläche“ vorliegt, können im weiteren Prüfungsverfahren behandelt werden.



3.    Für die geltende Anspruchsfassung gemäß Hauptantrag liegt ein genereller
Patentierungsausschluss gemäß PatG § 1 Abs. 3 i.V.m. Abs. 4 nicht vor. Ebensowenig können einzelne Merkmale von der Berücksichtigung ausgeschlossen
werden mit der Begründung, dass sie zur Lösung eines konkreten technischen
Problems mit technischen Mitteln nicht beitrügen.


3.1   Ein genereller Patentierungsausschluss gemäß PatG § 1 Abs. 3 i.V.m.
Abs. 4 ist schon deshalb nicht gerechtfertigt, weil die beanspruchte Lehre Anwei-

                                       - 12 -



sungen enthält, die der Lösung eines konkreten technischen Problems mit technischen Mitteln dienen (BGH GRUR 2011, 610 – Webseitenanzeige, Leitsatz a)).


Welches technische Problem durch eine Erfindung gelöst wird, ist objektiv danach
zu bestimmen, was die Erfindung tatsächlich leistet (BGH GRUR 2005, 141 –
Anbieten interaktiver Hilfe, II. 4 b)). Im vorliegenden Fall bewirken der konkret beschriebene technische Aufbau eines Ray-Tracing Systems mit programmierbaren
Ausführungseinheiten, die als Shader eingerichtet sind und virtuelle Lichtstrahlen
emittieren, sowie in bestimmter Weise ausgelegte Prüfzellen zum Prüfen der virtuellen Strahlen auf Schnittpunkte mit Objekten der 3D-Szene einerseits, sowie andererseits ein bestimmtes Arbeitsverfahren zum iterativ schrittweisen Führen der
virtuellen Strahlen durch die 3D-Szene, insgesamt ein schnelleres Rendern des
zweidimensionalen Bildes zur Darstellung auf einem Bildschirm. Damit wird eine
konkrete technische Aufgabe gelöst.


3.2   Es ist auch nicht feststellbar, dass einzelne Anspruchsmerkmale zur
Lösung des genannten Problems nicht beitragen würden.


Im vorliegenden Fall gelingt nach dem Verständnis des Senats die Lösung des
technischen Problems erst durch das Zusammenwirken aller Merkmale des auf
ein Ray-Tracing System gerichteten Anspruchs 1 wie auch des auf ein dieses
konkret beschriebene System nutzendes Verfahren gerichteten Anspruchs 5.


3.3   Die Auffassung der Prüfungsstelle, dass die Lösung durch einen verbesserten Algorithmus bewirkt werde und dieser nicht als Beitrag zur Lösung eines technischen Problems anerkannt werden könne, kann angesichts der Rechtsprechung
des Bundesgerichtshofs keinen Bestand haben.


Die Prüfungsstelle hat im Zurückweisungsbeschluss beispielsweise argumentiert,
eine durch die Lehre bestimmter Merkmale vielleicht erreichte Zeitersparnis erfolge jedoch ausschließlich aus dem verwendeten Datenverarbeitungsalgorithmus
heraus (im Beispiel: aus der Verwendung von Volumenausschlusselementen).

                                      - 13 -



Dies könne nicht als Beitrag zur Lösung eines konkreten technischen Problems
mit technischen Mitteln angesehen werden, da die Anweisungen der genannten
Merkmale auf keinerlei konkrete innerhalb oder außerhalb einer Datenverarbeitungsanlage vorliegende technische Gegebenheiten Rücksicht nähmen. Daher
seien die genannten Merkmale bei der Prüfung auf erfinderische Tätigkeit nicht zu
berücksichtigen.


Dieser Argumentation kann nicht gefolgt werden.


Zwar beruft sich die Prüfungsstelle zu Recht auf die Rechtsprechung des Bundesgerichtshofs, dass bei der Prüfung einer Erfindung auf erfinderische Tätigkeit nur
diejenigen Anweisungen zu berücksichtigen sind, die die Lösung des technischen
Problems mit technischen Mitteln bestimmen oder zumindest beeinflussen (BGH
GRUR 2011, 125 – Wiedergabe topografischer Informationen, Leitsatz b).


Hierzu wurde allerdings später einschränkend festgestellt, dass es dabei nicht
darauf ankommt, ob bestimmte Merkmale „für sich genommen“ technisch sind und
ein technisches Problem lösen; sondern entscheidend ist, ob sie im Kontext der
erfindungsgemäßen Lehre zur Lösung des dieser zugrundeliegenden Problems
beitragen (BGH GRUR 2017, 57 – Datengenerator, III. 1. b) aa)).


In diesem Sinne sind geometrische Verfahren zwar „an sich“ („als solche“) nicht
patentierbar – wohl aber dann, wenn sie in einem technischen Kontext zur Lösung
eines konkreten technischen Problems eingesetzt werden (vgl. auch BGH GRUR
2015, 983 – Flugzeugzustand, III. 2. a) und b): „Die Anwendung solcher [mathematischer] Methoden zur Erzielung eines bestimmten technischen Erfolgs ist deshalb ihrerseits dem Gebiet der Technik zuzuordnen. Als nicht-technisch kann eine
mathematische Methode nur dann angesehen werden, wenn sie im Zusammenhang mit der beanspruchten Lehre keinen Bezug zur gezielten Anwendung von
Naturkräften aufweist.“).

                                       - 14 -



So ist auch im vorliegenden Fall die Anwendung der beanspruchten Methoden
dem Gebiet der Technik zuzuordnen, weil ein schnelles, ressourcenschonendes
Rendern von zweidimensionalen Bildern einer 3D-Szene ein „konkretes technisches Problem“ darstellt. Auch wenn die Lösung im Wesentlichen durch einen
verbesserten Algorithmus erfolgen mag, so leistet dieser im Kontext des Ray-Tracing für das Rendern von 3D-Szenen doch zweifelsfrei einen Beitrag zur
Lösung des zugrundeliegenden Problems. Ein „Bezug zur gezielten Anwendung
von Naturkräften“ liegt beim beanspruchten Verfahren zumindest deshalb vor, weil
es ein in bestimmter Weise daran angepasstes technisches System nutzt. Der
verbesserte Algorithmus ist zwar „als solcher“ nicht patentierbar, wohl aber in
seiner konkreten Anwendung für ein bestimmtes Ray-Tracing System zum
Rendern eines Bildes einer 3D-Szene.



4.    Der bisher ermittelte Stand der Technik steht dem Patentanspruch 1 gemäß
Hauptantrag nicht patenthindernd entgegen.


4.1   Im Laufe des Verfahrens sind folgende Druckschriften entgegengehalten
worden:


      D1    FRIEDRICH, H.: Ray Tracing Techniques for Computer
            Games and Isosurface Visualization. Thesis, University of
            Saarland,     Saarbrücken,     Germany    (veröffentlicht   am
            3. August 2012 – http://scidok.sulb.uni-saarland.de/volltexte/
            2012/4917/)
      D2     „Bounding    Volume    Hierarchy“,   Wikipedia-Artikel     vom
            13.2.2013 – https://en.wikipedia.org/w/index.php?title= Bounding_volume_hierarchy&oldid=538071764
      D3    US 2009 / 262 132 A1
      D4    SZIRMAY-KALOS, L. [et al.]: Displacement Mapping on the
            GPU - State of the Art. Computer Graphics Forum, Vol. 27,
            2008, S. 1567-1592

                                     - 15 -



      D5    HIRCHE, J. [et al.]: Hardware accelerated per-pixel displacement mapping. Proceedings of Graphics Interface, 2004,
            S. 153-160
      D6    MANTLER, S. [et al.]: Interactive landscape visualization
            using GPU ray casting. Proceedings of the 4th international
            conference on Computer graphics and interactive techniques
            in Australasia and Southeast Asia, 2006, S. 117-126
      D7    PORUMBESCU, S. D. [et al.]: Shell Maps. ACM Transactions on Graphics, Vol. 24, 2005, S. 626-633
      D8    TEVS, A. [et al.]: Maximum Mipmaps for Fast, Accurate, and
            Scalable Dynamic Height Field Rendering. Proceedings of
            the 2008 symposium on Interactive 3D graphics and games
            (I3D '08), Redwood City, Kalifornien, USA, 2008, S. 183-190


Wie die Anmelderin berechtigterweise ausführt, lassen sich keiner dieser Druckschriften die neuen Anspruchsmerkmale hinsichtlich der Schrittweite der für das
Ray-Tracing erzeugten Strahlen entnehmen, insbesondere keine Berücksichtigung
eines Strahldifferentials oder des Detailniveaus der 3D-Objekte. Darüber hinaus
kann die Anmelderin keine „implizite Geometrie“ im Sinne der Anmeldung wiederfinden.


Derzeit ist für den Senat nicht ersichtlich, wie der Durchschnittsfachmann ausgehend allein von diesen Druckschriften zur Lehre des auf ein Ray-Tracing
System gerichteten Patentanspruchs 1 des Hauptantrags und des (darauf zurückbezogenen) Verfahrensanspruchs 5 hätte gelangen können.



5.    Die genannten Patentansprüche 1 und 5 des Hauptantrags wurden jedoch
erst mit der Beschwerdebegründung neu eingereicht. Sie wurden bisher vom
Deutschen Patent- und Markenamt noch nicht geprüft, insbesondere hat noch
keine darauf gerichtete Recherche stattgefunden.

                                         - 16 -



Weil das Deutsche Patent- und Markenamt somit noch nicht in der Sache selbst
entschieden hat, war die Anmeldung gemäß § 79 Abs. 3 Satz 1 Nr. 1 dorthin
zurückzuverweisen (siehe z.B. Schulte, PatG, 10. Auflage (2017), § 79 Rdnr. 21).



6.      Da die grundsätzliche Frage der Patentierbarkeit des Hauptantrags noch
offen ist, hat der Senat sich mit dem Hilfsantrag nicht weiter befasst.




                                Rechtsmittelbelehrung

Gegen diesen Beschluss steht den am Beschwerdeverfahren Beteiligten das Rechtsmittel
der Rechtsbeschwerde zu. Da der Senat die Rechtsbeschwerde nicht zugelassen hat, ist
sie nur statthaft, wenn gerügt wird, dass

     1. das beschließende Gericht nicht vorschriftsmäßig besetzt war,
     2. bei dem Beschluss ein Richter mitgewirkt hat, der von der Ausübung des
        Richteramtes kraft Gesetzes ausgeschlossen oder wegen Besorgnis der
        Befangenheit mit Erfolg abgelehnt war,
     3. einem Beteiligten das rechtliche Gehör versagt war,
     4. ein Beteiligter im Verfahren nicht nach Vorschrift des Gesetzes vertreten war,
        sofern er nicht der Führung des Verfahrens ausdrücklich oder stillschweigend
        zugestimmt hat,
     5. der Beschluss aufgrund einer mündlichen Verhandlung ergangen ist, bei der die
        Vorschriften über die Öffentlichkeit des Verfahrens verletzt worden sind, oder
     6. der Beschluss nicht mit Gründen versehen ist.

Die Rechtsbeschwerde ist innerhalb eines Monats nach Zustellung des Beschlusses beim
Bundesgerichtshof, Herrenstr. 45 a, 76133 Karlsruhe, durch einen beim Bundesgerichtshof zugelassenen Rechtsanwalt als Bevollmächtigten schriftlich einzulegen.




Dr. Morawek                  Bayer                  Baumgardt              Dr. Harth
