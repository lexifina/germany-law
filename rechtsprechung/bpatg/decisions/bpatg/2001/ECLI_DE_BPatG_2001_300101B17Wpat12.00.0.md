---
ecli: "ECLI:DE:BPatG:2001:300101B17Wpat12.00.0"
court: "Bundespatentgericht"
spruchkoerper: "17"
aktenzeichen: "17 W (pat) 12/00"
decided: "2001-01-30"
typ: "B"
source_url: "https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bpatg&Art=en&Datum=2001&Sort=1&Seite=8&nr=21111&anz=1792&pos=123&Blank=1.pdf"
corpus_doc_id: "BPatG_TechnBeschw_NA_2001-01-30_17_W-pat_12_00_NA_0.txt"
cites_law: ["germany/bund/acts/patg/0004.md"]
---

# Bundespatentgericht, 17 W (pat) 12/00 vom 2001-01-30

## Entscheidung

BUNDESPATENTGERICHT

                                                                     Verkündet am
                                                                    30. Januar 2001
 17 W (pat) 12/00
                                                                           …
    (Aktenzeichen)




                               BESCHLUSS

                              In der Beschwerdesache


               betreffend die Patentanmeldung 195 26 801.6-53


…




hat der 17. Senat (Technischer Beschwerdesenat) des Bundespatentgerichts auf
die mündliche Verhandlung vom 30. Januar 2001 unter Mitwirkung des Vorsitzenden Richters Dipl.-Phys. Grimm, der Richter Dipl.-Ing. Bertl und Dipl.-Ing. Prasch
sowie der Richterin Püschel




BPatG 154
6.70

                                     - 2 -



beschlossen:


        Die Beschwerde wird zurückgewiesen.




                                  Gründe:


                                        I.


Die Patentanmeldung mit der Bezeichnung


        "Anordnung zur Steuerung der bidirektionalen, asynchronen und
        seriellen Übertragung von Datenpaketen und Verfahren zum Betrieb einer derartigen Anordnung"


wurde von der Prüfungsstelle für Klasse G 06 F des Deutschen Patent- und Markenamts zurückgewiesen. In den Gründen ist ausgeführt, daß der Patentanspruch 1 nicht gewährbar sei, da sein Gegenstand nicht auf einer erfinderischen
Tätigkeit beruhe.


Gegen diesen Beschluß richtet sich die Beschwerde der Anmelderin.


In der mündlichen Verhandlung wurde folgender Patentanspruch 1 nach Hauptantrag überreicht:


        "Verfahren zum Betrieb eines Controllers zur Steuerung der bidirektionalen, Asynchronen und seriellen Übertragung von Datenpaketen begrenzter Länge zwischen einer über einen Datenbus,
        einen Adreßbus und einen Steuersignalbus angeschlossenen
        Datenverarbeitungseinrichtung und einem an eine Busleitung eines prioritätspersistenten Bussystems, bei dem in demselben

                               - 3 -



Zeitfenster Datenelemente sendbar, empfangbar und zerstörbar
sind, angeschlossenen Bustreiber, mit mindestens einen Bitflußprozessor zur zeitlichen Koordination der Sende- und Empfangsprozesse entsprechend einem vorgebbaren Übertragungsprotokoll, dem eine Empfangseinrichtung, deren Eingang mit dem Bustreiber verbunden ist und die Selektionsmittel zur Auswahl von
Datenpaketen aus einem über die Busleitung übertragenen Datenstrom umfaßt, und eine Sendeeinrichtung, deren Ausgang mit
dem Bustreiber verbunden ist, zugeordnet sind, wobei der Empfangseinrichtung Puffermittel zur abrufbaren Zwischenspeicherung
von    empfangenen      Datenpaketen   nachgeordnet    und   der
Sendeeinrichtung Puffermittel zur abrufbaren Zwischenspeicherung von zu sendenden Datenpaketen vorgeschaltet sind, aufweist
und Mittel zur Steuerung dieser Komponenten und Mittel zur
Anpassung an den Datenbus, den Adreßbus und den Steuersignalbus      der   angeschossenen   Datenverarbeitungseinrichtung
umfaßt,
dadurch gekennzeichnet,
daß bei jeder Initiaisierung
-     die Sendeeinrichtung (43) deaktiviert inbetriebgenommen
      wird,
-     der über die Busleitung (1) aktuell übertragene Datenstrom
      ungefiltert empfangen und analysiert wird, wobei der Datenstrom unter vorgebbaren Zeitbedingungen abgetastet wird,
      und
-     aus dem empfangenen Datenstrom die ihm zugrundeliegenden Übertragungsparameter ermittelt werden,
-     die Sendeeinrichtung (43) auf die ermittelten Übertragungsparameter eingestellt wird und

                                        - 4 -



        -     die Sendeeinrichtung (43) aktiviert wird."


Der ebenfalls in der mündlichen Verhandlung überreichte Patentanspruch 1 nach
Hilfsantrag lautet:


        "Verfahren für Anpassung eines Zwischen einer Datenverarbeitungseinrichtung und einem über einem Bustreiber an eine Busleitung eines bidirektionalen, asynchromen und seriellen Bussystem angeordneten Controllers, der mindestens einen Bitflußprozessor zur zeitlichen Koordination der Sende- und Empfangsprozesse entsprechend einem vorgebbaren Übertragungsprotokoll,
        eine Empfangseinrichtung und eine Sendeeinrichtung aufweist,
        dadurch gekennzeichnet,
        daß bei jeder Initialisierung
        -     die Sendeeinrichtung (43) deaktiviert inbetriebgenommen
              wird
        -     die über die Busleitung (1) aktuell empfangene Datenstrom
              ungefiltert empfangen und unter vorgebbaren Zeitbedingungen abgetastet wird,
        -     das empfangene Muster mit Mustern bekannter Übertragungsparameter verglichen wird,
        -     die Sendeeinrichtung (43) auf die ermittelten Übertragungsparameter eingestellt wird und
        -     die Sendeeinrichtung (43) aktiviert wird."


Der Anmeldung liegt die Aufgabe zugrunde, das destruktive Einfügen dominanter
Datenbit in ein aktuell übertragenes Datenpaket zu verhindern (Beschreibung
Seite 2, Zeilen 29 und 30).

                                      - 5 -



Wie die Anmelderin zur Begründung ihrer Beschwerde ausführt, handelt es sich
beim Anmeldungsgegenstand um ein Multiprotokoll-fähiges System. Durch die im
Patentanspruch 1 angegebenen Schritte könne sich ein hinzugefügtes Gerät, das
keine Information über das verwendete Protokoll habe, auf das verwendete Protokoll einstellen, ohne den Verkehr zu stören. Die hierfür beanspruchte Schrittfolge
sei nicht aus dem Stand der Technik bekannt. Vielmehr sei nach der Druckschrift
"Siemens AG: IC's for Communications, Data Book 1989/90, SAB 82525 ... SAF
82526, Seiten 688 bis 739" der Empfang stillgelegt, weshalb das Gerät nicht mithören könne. Das Verfahren nach dem Patentanspruch 1 ermögliche die Unterdrückung von dominanten Bits, so daß der Bus nicht gestört werde. Bei der Fassung des Patentanspruchs 1 nach dem Hilfsantrag werde im Oberbegriff auf
Merkmale verzichtet, die für das Verfahren nicht notwendig seien.


Die Anmelderin stellt den Antrag,


        den angefochtenen Beschluß aufzuheben und das nachgesuchte
        Patent mit folgenden Unterlagen zu erteilen:
        Patentansprüche 1 bis 3, überreicht in der mündlichen Verhandlung,
        ursprünglich eingereichte, noch anzupassende Beschreibung
        Seiten 1 bis 5,
        ursprünglich eingereichte 1 Blatt Zeichnung mit Figur 1,
        hilfsweise mit dem in der mündlichen Verhandlung überreichten
        Patentanspruch 1 gemäß Hilfsantrag, Unteransprüche und übrige
        Unterlagen wie Hauptantrag.

                                       - 6 -



                                            II.


Die frist- und formgerecht erhobene Beschwerde ist zulässig. Sie hat jedoch keinen Erfolg, da der Gegenstand des Patentanspruchs 1 weder nach Haupt- noch
nach Hilfsantrag auf einer erfinderischen Tätigkeit beruht und deshalb nach § 4
PatG nicht patentfähig ist.


Die Anmeldung betrifft ein Verfahren, mit dem an ein Bus-System, an das eine
Vielzahl von Teilnehmern angeschlossen sind, ein zusätzliches Gerät angeschlossen werden soll. Auf diesem Bus ist eine Datenübertragung mit verschiedenen Protokollen möglich. Ein Bitflußprozessor steuert Sende- und Empfangsvorgänge entsprechend dem verwendeten Busprotokoll. Das neue Gerät soll sich
automatisch anpassen.


Dazu wird die Sendeeinrichtung deaktiviert inbetriebgenommen und der über die
Busleitung (1) aktuell übertragene Datenstrom ungefiltert empfangen und analysiert, wobei der Datenstrom unter vorgebbaren Zeitbedingungen abgetastet wird.
Aus dem empfangenen Datenstrom werden die ihm zugrundeliegenden Übertragungsparameter ermittelt (nach Hilfsantrag wird hierzu das empfangene Muster
mit Mustern bekannter Übertragungsparameter verglichen). Nachdem die Sendeeinrichtung (43) auf die ermittelten Übertragungsparameter eingestellt worden ist,
wird die Sendeeinrichtung (43) aktiviert.


Im Prüfungsverfahren wurden folgende Druckschriften genannt, denen eine besondere Bedeutung zukommt:


        1.   Siemens AG: IC's for Communications, Data Book 1989/90, SAB
             82525 ... SAF 82526, Seiten 688 bis 739
        2.   Electronic Design, 30. Mai 1994, Seiten 108, 110, 112, 114, 116

                                     - 7 -



Druckschrift 1 ist das Datenblatt des Siemens Bausteins SAB 82526, der dem Intel
Baustein 82526 aus der Beschreibungseinleitung entsprechen dürfte.


Die Druckschrift 2 setzt sich mit SCSI-Bus-Standard auseinander.


Hauptantrag:


Das Verfahren nach dem Patentanspruch 1 ist neu, da keiner der beiden genannten Druckschriften die im Kennzeichen des Patentanspruchs 1 nach Hauptantrag genannten Merkmale in dieser Kombination direkt zu entnehmen sind.


Der Gegenstand des Patentanspruchs 1 beruht jedoch nicht auf einer erfinderischen Tätigkeit.


Bussysteme, auf denen das im Patentanspruch 1 angesprochene Verfahren ablaufen kann, sind dem Fachmann geläufig. So zeigt z.B. die Siemens Druckschrift,
daß der Bus mit verschiedenen Modi betrieben werden kann (vgl. insb. Seite 714
"mode register", Seite 724 "channel configuration register"). Auch aus der genannten Stelle aus Electronic Design (vgl. insb. Seite 116, linke Spalte, letzter
Absatz) geht hervor, daß auf dem dort beschriebenen Bus verschiedene Protokolle möglich sind. Die übrigen Merkmale des Oberbegriffs ergeben sich ebenfalls
aus dem Stand der Technik, z.B. aus der Siemens Druckschrift:


-     Der beschriebene Baustein 82526 wird zur Steuerung der bidirektionalen,
      und seriellen Übertragung von Datenpaketen begrenzter Länge verwendet,
      wie sich aus Seite 689 ergibt. Dabei ist es für den Anmeldungsgegenstand
      ohne Bedeutung, ob die Übertragung synchron oder asynchron erfolgt.
-     Die Datenpakete werden zwischen einer über einen Datenbus (D0-D7), einen Adreßbus (A0-A7) und einen Steuersignalbus angeschlossenen Datenverarbeitungseinrichtung (linke Seite der Figur auf Seite 698) und einem
      an einer Busleitung (rechte Seite der Figur auf Seite 698) eines priori-

                                   - 8 -



    tätspersistenten Bussystems (wie es mit der Konfiguration auf Seite 704
    unterste Figur möglich ist) angeschlossenen Bustreiber (muß für Signale
    RxDA und TxDA vorhanden sein) übertragen.
-   Bei dem Bussystem sind in demselben Zeitfenster Datenelemente sendbar,
    empfangbar und zerstörbar (ergibt sich, da ein Collision Detection Abschnitt
    vorhanden ist).
-   Die Anordnung weist als Komponenten mindestens einen Bitflußprozessor,
    eine Empfangseinrichtung und eine Sendeeinrichtung auf (alles in Data Link
    und LAP Controller).
-   Für den Fachmann ist es selbstverständlich, daß der Bitflußprozessor zur
    zeitlichen Koordination der Sende- und Empfangsprozesse entsprechend
    einem vorgebbaren Übertragungsprotokoll dient.
-   Dem Bitflußprozessor ist eine Empfangseinrichtung zugeordnet (in Data
    Link Controller), deren Eingang mit dem Bustreiber verbunden ist.
-   Die Empfangseinrichtung muß Selektionsmittel umfassen, zur Auswahl von
    Datenpaketen aus einem über die Busleitung übertragenen Datenstrom, um
    zu erkennen - üblicherweise aus dem Paketanfang - welches Datenpaket
    für welchen Teilnehmer bestimmt ist.
-   Dem Bitflußprozessor ist eine Sendeeinrichtung deren Ausgang mit dem
    Bustreiber verbunden ist, zugeordnet (in Data Link Controller).
-   Der Empfangseinrichtung sind Puffermittel (receive FIFO) zur abrufbaren
    Zwischenspeicherung von empfangenen Datenpaketen nachgeordnet.
-   Der Sendeeinrichtung sind Puffermittel (transmit FIFO) zur abrufbaren Zwischenspeicherung von zu sendenden Datenpaketen vorgeschaltet.
-   Die Anordnung umfaßt auch Mittel zur Steuerung dieser Komponenten und
    Mittel zur Anpassung an den Datenbus, den Adreßbus und den Steuersignalbus der angeschlossenen Datenverarbeitungseinrichtung (ergibt sich
    aus Seite 707).

                                       - 9 -



Bei einem derartigen Verfahren soll gemäß der Aufgabe das destruktive Einfügen
dominanter Datenbit in ein aktuell übertragenes Datenpaket verhindert werden
(Beschreibung Seite 2, Zeilen 29 und 30). Diese Aufgabe stellt sich für den
Fachmann von alleine, da er geltende Datenpakete nicht verfälschen darf.


Im Rahmen der Lösung dieser Aufgabe ergeben sich die im Kennzeichen
angegebenen Merkmale zwangsläufig. Zudem wird der Fachmann durch die
Druckschrift 2 (Electronic Design, vgl. insb. Seite 116, linke Spalte, letzter Absatz)
auch angeregt, die Parameter der Schnittstelle auf das Busprotokoll automatisch
einzustellen.


Um den laufenden Betrieb nicht zu stören, muß die Sendeeinrichtung (43) deaktiviert inbetriebgenommen werden. Für die automatische Anpassung an das auf
dem Bus verwendete Protokoll muß dieses zuerst erkannt werden. Dazu bietet es
sich an, den über die Busleitung (1) aktuell übertragenen Datenstrom ungefiltert zu
empfangen und zu analysieren, wobei der Datenstrom unter vorgebbaren Zeitbedingungen abgetastet werden muß, um aufgrund möglicher unterschiedlicher
Taktraten die Information zu erkennen. Dadurch können aus dem empfangenen
Datenstrom die ihm zugrundeliegenden Übertragungsparameter ermittelt werden
was die Voraussetzung dafür ist, daß die Sendeeinrichtung (43) auf diese Übertragung eingestellt werden kann. Nach der Anpassung der angeschlossenen Einheit an das Protokoll muß die Sendeeinrichtung (43) aktiviert werden, damit sie am
Datenaustausch teilnehmen kann, was letztlich Zweck ihres Anschließens ist.


Der Patentanspruch 1 nach Hauptantrag ist nach allem nicht gewährbar.


Hilfsantrag:


Der Patentanspruch 1 nach Hilfsantrag enthält - wie die Anmelderin ausführt - in
seinem Oberbegriff nur die Merkmale der Fassung nach Hauptantrag, die für das
beanspruchte Verfahren notwendig sind. Somit ergibt er sich ebenfalls aus dem

                                     - 10 -



Stand der Technik. Im Kennzeichen ist neben den Merkmalen des Patentanspruchs 1 nach Hauptantrag, zusätzlich noch das Merkmal enthalten, daß das
empfangene Muster mit Mustern bekannter Übertragungsparameter verglichen
wird. Auch dieses liegt für den Fachmann auf der Hand, da eine übliche Methode
für die Erkennung von Mustern der Vergleich mit bekannten Mustern ist. Bezüglich
der übrigen Merkmale wird auf die obigen Ausführungen zum Hauptantrag
hingewiesen. Nach allem ergibt sich das Verfahren nach dem Patentanspruch 1
gemäß Hilfsantrag für den Fachmann aus dem Stand der Technik, ohne daß er
erfinderisch tätig werden muß.


Der Patentanspruch 1 nach Hilfsantrag ist deshalb nicht gewährbar.


Mit den nicht gewährbaren Patentansprüchen 1 nach Haupt- bzw. Hilfsantrag fallen auch die auf sie rückbezogenen Patentansprüche 2 und 3.




Grimm                        Bertl              Prasch                  Püschel



                                                                            prö
