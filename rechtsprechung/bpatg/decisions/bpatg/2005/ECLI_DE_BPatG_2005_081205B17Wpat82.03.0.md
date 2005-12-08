---
ecli: "ECLI:DE:BPatG:2005:081205B17Wpat82.03.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 82/03"
decided: "2005-12-08"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2005&Sort=1&Seite=123&nr=18470&anz=1972&pos=1857&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2005-12-08_17_W-pat_82_03_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0079.md"]
---

# Bundespatentgericht, 17 W (pat) 82/03 vom 2005-12-08

## Entscheidung

BUNDESPATENTGERICHT


 17 W (pat) 82/03                                                   Verkündet am
 _______________                                                 8. Dezember 2005
    (Aktenzeichen)                                                       …




                             BESCHLUSS

                           In der Beschwerdesache


               betreffend die Patentanmeldung 102 14 067.7-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 8. Dezember 2005 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Dr. Fritsch sowie der Richter Dipl.-Ing. Prasch, der
Richterin Eder und des Richters Dipl.-Ing. Baumgardt




BPatG 154
08.05

                                      -2-



beschlossen:


       Auf die Beschwerde der Anmelderin wird der Beschluss der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts vom 4. August 2003 aufgehoben und die Sache zur weiteren
       Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückverwiesen.


                                   Gründe


                                        I.


Die vorliegende Patentanmeldung ist beim Deutschen Patent- und Markenamt in
englischer Sprache angemeldet worden unter der Bezeichnung:


       "On-chip high speed data interface", übersetzt als "Hochgeschwindigkeitsdatenschnittstelle auf einem Chip".


Sie wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und
Markenamts durch Beschluss vom 4. August 2003 mit der Begründung zurückgewiesen, dass sich der Merkmalsumfang des Patentanspruchs 1 nicht auf erfinderische Weise vom bekannten Stand der Technik unterscheide. Dasselbe gelte für
die nebengeordneten Ansprüche 26 und 39.


Gegen diesen Beschluss wendet sich die Beschwerde der Anmelderin. Sie verfolgt die Anmeldung auf der Grundlage der in der mündlichen Verhandlung überreichten Patentansprüche 1 bis 43 weiter.

                                        -3-



Der geltende Anspruch 1, hier mit einer denkbaren Gliederung versehen, lautet:


       "Integrierter Schaltkreischip,


       a) umfassend eine erste und eine zweite Schaltungseinheit (300,
            330, 1100, 1130), wobei:


       b) die erste und zweite Schaltungseinheit Anforderungen an die
            jeweils andere erste bzw. zweite Schaltungseinheit senden
            können;


       c) die erste und zweite Schaltungseinheit eine Antwort zurücksenden können, wenn sie eine Anforderung empfangen, die
            eine Antwort erfordert;


       d) die erste Schaltungseinheit Daten bezüglich einer zu sendenden Anforderung speichern kann; und


       e) die zweite Schaltungseinheit keine Daten bezüglich einer
            empfangenen Anforderung speichern kann,


       f)   wobei die Daten bezüglich einer Anforderung Anforderungsdaten enthalten, die die Anforderung bilden,


       g) wobei die zweite Schaltungseinheit mit der ersten Schaltungseinheit verbunden ist, um ein Steuersignal an die erste Schaltungseinheit zu liefern, und wobei die erste Schaltungseinheit
            eingerichtet ist zum Verzögern des Sendens weiterer Anforderungsdaten, wenn das Steuersignal anzeigt, dass die zweite
            Schaltungseinheit nicht bereit zum Empfangen weiterer Anforderungsdaten ist, und

                                       -4-



        h) wobei die zweite Schaltungseinheit mit der ersten Schaltungseinheit verbunden ist, um ein Flush-Signal an die erste Schaltungseinheit zu liefern, und wobei die erste Schaltungseinheit
            eingerichtet ist zum Löschen ausstehender Anforderungsdaten, wenn das Steuersignal anzeigt, dass die zweite Schaltungseinheit nicht bereit zum Empfangen weiterer Anforderungsdaten ist, und wenn das Flush-Signal anzeigt, dass die
            ausstehenden Anforderungsdaten zu löschen sind."


Der formal nebengeordnete, jedoch rückbezogene Patentanspruch 23 lautet:


        "Southbridgebauelement, umfassend einen integrierten Schaltkreischip nach einem der Ansprüche 1 bis 22."


Der nebengeordnete Patentanspruch 24, hier ebenfalls mit einer Gliederung versehen, lautet:


        a) "Verfahren zum Betreiben eines integrierten Schaltkreischips,
            der eine erste und eine zweite Schaltungseinheit umfasst, umfassend:


        b) Senden (400 – 455, 1200 – 1265) von Anforderungen von der
            ersten oder zweiten Schaltungseinheit zu der jeweils anderen
            ersten bzw. zweiten Schaltungseinheit; und


        c) Senden (800 – 845, 1600 – 1650) einer Antwort von der jeweils anderen ersten bzw. zweiten Schaltungseinheit zurück
            zu der ersten bzw. zweiten Schaltungseinheit, wenn die Anforderung eine Antwort erfordert;

                                  -5-



wobei das Verfahren weiterhin umfasst:


d) Betreiben der ersten Schaltungseinheit, um Daten bezüglich
     einer Anforderung speichern, die von der ersten Schaltungseinheit zu senden ist; und


e) Betreiben der zweiten Schaltungseinheit, um keine Daten bezüglich einer von der zweiten Schaltungseinheit zu empfangenen Anforderung zu speichern,


f)   wobei die Daten bezüglich einer Anforderung Anforderungsdaten enthalten, die die Anforderung bilden,


wobei das Verfahren weiterhin umfasst:


g) Bereitstellen eines Steuersignals von der zweiten Schaltungseinheit für die erste Schaltungseinheit; und Betreiben der ersten Schaltungseinheit, um das Senden weiterer Anforderungsdaten zu verzögern, wenn das Steuersignal anzeigt, dass die
     zweite Schaltungseinheit nicht bereit zum Empfangen weiterer
     Anforderungsdaten ist, und


wobei das Verfahren weiterhin umfasst:


h) Bereitstellen eines Flush-Signals von der zweiten Schaltungseinheit für die erste Schaltungseinheit; und Betreiben der ersten Schaltungseinheit, um ausstehende Anforderungsdaten zu
     löschen, wenn das Steuersignal anzeigt, dass die zweite
     Schaltungseinheit nicht bereit zum Empfangen weiterer Anforderungsdaten ist, und wenn das Flush-Signal anzeigt, dass
     die ausstehenden Anforderungsdaten zu löschen sind."

                                      -6-



Wegen der übrigen Patentansprüche wird auf den Akteninhalt verwiesen.


Die Anmelderin trägt zur Begründung ihrer Beschwerde vor, dass mit dem nunmehr beanspruchten integrierten Schaltkreischip, dem darauf basierenden Southbridgebauelement und dem Verfahren nach Anspruch 24 die Leistung von On-Chip-Schnittstellen erhöht werde. Die nunmehr beanspruchten, durch neu aufgenommene Merkmale eingeschränkten Gegenstände seien für den Fachmann nicht
mehr nahe liegend.


Die Anmelderin stellte den Antrag,


       den angefochtenen Beschluss aufzuheben und das nachgesuchte
       Patent mit folgenden Unterlagen zu erteilen:


       Patentansprüche 1 – 43, überreicht in der mündlichen Verhandlung, Beschreibung S. 2, 4 und 16, überreicht in der mündlichen
       Verhandlung, S. 4a, 4b, eingegangen am 3. Juli 2003, S. 1, 3, 5-
       15, 17-20, eingegangen am 18. Juni 2002, sowie 12 Blatt Zeichnungen mit 20 Figuren, eingegangen am 18. Juni 2002.


                                       II.


Die in rechter Frist und Form erhobene Beschwerde ist auch im Übrigen zulässig.
Sie konnte jedoch nur zur Zurückverweisung der Sache zur weiteren Prüfung an
das Deutsche Patent- und Markenamt führen (§ 79 Abs. 3 Satz 1 Nr. 1 PatG).


1. Die in der mündlichen Verhandlung vorgelegten nebengeordneten Ansprüche 1,
23 und 24 unterscheiden sich von der ursprünglich eingereichten Fassung dieser
Ansprüche durch zusätzliche Merkmale aus Unteransprüchen.

                                       -7-



So ist der neue Hauptanspruch eine Zusammenfassung der ursprünglichen Ansprüche 1, 2, 4 und 6. Der neue Anspruch 23 entspricht dem ursprünglichen Anspruch 26 und dessen Unteransprüchen. Der neue Anspruch 24 ist aus den ursprünglichen Ansprüchen 39, 40, 41 und 43 zusammengesetzt.


Die Fassung der drei nebengeordneten Ansprüche ist daher zulässig.


2. Die Neuheit und erfinderische Tätigkeit des Schaltkreischips nach dem geltenden Anspruch 1 und des Verfahrens nach dem geltenden Anspruch 24 sind durch
die im bisherigen Verfahren genannten Druckschriften nicht in Frage gestellt. Anspruch 23 würde ggfls. allein durch seine Rückbeziehung auf Anspruch 1 getragen
und wird daher im Folgenden nicht weiter behandelt.


Im Prüfungsverfahren wurden zitiert:


        D1) US 6 266 715 B1
        D2) US 5 007 012 A
        D3) HyperTransport TM I/O Link Specification Rev. 1.03, Hyper-Transport Technology Consortium, S. 17, 18, 20, 21, 23-66,
             115.


Der Senat hat noch die folgenden, teilweise aus der Recherche zu einer US-Nachanmeldung bekannt gewordenen Druckschriften eingeführt:


        D4) US 6 151 651 A
        D5) US 5 764 933 A
        D6) US 6 353 867 B1.


2.1. Von diesen allen kommt Druckschrift D6) dem beanspruchten Schaltkreischip
und dem Verfahren nach Anspruch 24 am nächsten, da sie als einzige On-Chip-Schnittstellen beschreibt.

                                       -8-



In Übereinstimmung mit den Merkmalen a) bis d) des Anspruchs 1 ist aus dieser
Druckschrift ein integrierter Schaltkreischip bekannt, bei dem Schnittstellen zwischen virtuellen Baugruppen (VCs) auf dem Chip vorgesehen sind, siehe Spalte 1,
Zeile 13 – 31. Dafür werden standardisierte Interface-Baugruppen (SIs) vorgeschlagen, die gemäß Figur 10 / 11 für einen Sende- und Empfangsbetrieb als
Master oder Slave ausgelegt sind. Gemäß Spalte 4, Zeile 23 – 32, kann eine erste
Schaltungseinheit (Master) an eine zweite Schaltungseinheit (Slave) beispielsweise eine Leseanforderung senden, woraufhin die zweite Schaltungseinheit eine entsprechende Antwort zurücksendet. Gemäß Figur 11 sind Zwischenspeicher
(FIFOs 106, 118, 132, 136) für die Daten vorgesehen.


Darüber hinaus ist noch Spalte 6, Zeile 56 – 59, entnehmbar, dass eine Zwischenspeicherung von Daten im Slave nicht unbedingt nötig ist. Dies wird aufgegriffen in
Spalte 10, Zeile 33 – 39, wonach ganz konkret die Lese- (Empfangs-) FIFOs118,
132 weggelassen werden können. Damit ist ein Aspekt von Merkmal e) – dass
nämlich in der zweiten Schaltungseinheit (Slave) keine empfangenen Anforderungsdaten gespeichert werden können – vorweggenommen. Der Spalte 10, Zeile 40 – 46, kann der Fachmann noch die Anregung entnehmen, ggfls. auch den
Speicher für die zu sendenden Daten (Antwortdaten) in der zweiten Schaltungseinheit (Slave) wegzulassen ( = zweiter Aspekt von Merkmal e)).


Zu Merkmal f) hat die Anmelderin in der mündlichen Verhandlung erläutert, durch
"Daten bezüglich einer Anforderung" solle lediglich ein Bezug auf die "Daten" gemäß Merkmal d) und Merkmal e) hergestellt werden. Somit kommt hier zum Ausdruck, dass die Datenworte, die insgesamt die Anforderung nach Merkmal b) bilden, in der ersten Schaltungseinheit gespeichert und in der zweiten Schaltungseinheit nicht gespeichert werden können. Allerdings soll nach der Erläuterung der
Anmelderin der Begriff "Daten bezüglich einer Anforderung" nicht nur diese Anforderungsdaten, sondern auch die Antwortdaten gemäß geltendem Unteranspruch 5
umfassen.

                                       -9-



Nach dem Verständnis des Senats ist Merkmal f) bei dieser Auslegung bereits in
den Merkmalen b), d) und e) enthalten, ihm kommt daher keine eigene Bedeutung
zu.


Somit sind die Merkmale a) bis f) des neuen Anspruchs 1 durch Druckschrift D6)
zumindest nahe gelegt. Das Entsprechende gilt für die Merkmale a) bis f) des nebengeordneten Anspruchs 24.


2.2. Jedoch lassen sich die neu hinzugekommenen Merkmale g) und h) aus dem
vorliegenden Stand der Technik nicht zweifelsfrei herauslesen. Merkmal g) betrifft
ein Verzögerungs-Steuersignal, mit dem der Empfänger anzeigen kann, dass er
nicht bereit zum Empfangen von Anforderungsdaten ist, woraufhin der Sender zunächst keine weiteren Daten sendet. Dabei dürfte es sich um eine Art "READY"-
oder "BUSY"-Signal handeln, wie es in der Datenübertragung allgemein bekannt,
aber den vorliegenden Druckschriften im Zusammenhang mit dem Verzicht auf einen Empfangsdatenspeicher (Teilaspekt des Merkmals e) nicht entnehmbar ist.
Merkmal h) betrifft ein zusätzliches "Flush"-Signal, mit dem der Empfänger eine
Anforderung im Sender löschen kann. Ein solches Signal ist zwar grundsätzlich
aus Druckschrift D5) (vgl. Spalte 6, Zeile 17 ff.) vorbekannt, jedoch nicht in logischer Verknüpfung mit dem Verzögerungs-Steuersignal nach Merkmal g).


Auch die übrigen im Verfahren befindlichen Druckschriften geben hierzu keine Anregungen. Es ist daher anzuerkennen, dass der Schaltkreischip nach Anspruch 1
und das Verfahren nach Anspruch 24 durch den vorliegenden Stand der Technik
nicht nahe gelegt sind.


3. Die Anmelderin hat sonach mit der geltenden Fassung ihres Patentbegehrens
den zur Zurückweisung der Anmeldung führenden Mangel beseitigt. Weil aber im
Laufe des Beschwerdeverfahrens das Patentbegehren um wesentliche Merkmale
ergänzt wurde, ist davon auszugehen, dass das Deutsche Patent- und Markenamt

                                     - 10 -



über die Patentfähigkeit der geltenden Ansprüche noch nicht abschließend befunden hat.


Die Sache war daher nach § 79 Abs. 3 PatG zur weiteren Prüfung und Entscheidung an das Deutsche Patent- und Markenamt zurückzuverweisen.


Neben der Prüfung auf Patentfähigkeit wird die Prüfungsstelle auch noch die Formulierung der geltenden Ansprüche zu überprüfen haben, insbesondere ob das
Merkmal f) gestrichen werden kann, und ob das als wesentlich angesehene Merkmal, dass eine "On-Chip-Schnittstelle" beansprucht wird, durch die gewählte Formulierung "Integrierter Schaltkreischip, umfassend ..." hinreichend deutlich zum
Ausdruck kommt.




Dr. Fritsch               Prasch                Eder                 Baumgardt




                                                                             Pü
