# Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der Datensatzbeschreibung für die Übermittlung der Mindeststeuer-Berichte

- Herausgeber: Bundesministerium der Finanzen
- Datum: 2025-08-05
- Art: BMF-Schreiben
- Sachgebiet (BMF): Internationales_Steuerrecht / Allgemeine_Informationen
- Quelle: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Internationales_Steuerrecht/Allgemeine_Informationen/2025-08-05-datensatz-datensatzbeschr-mindeststeuer.html
- PDF: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Internationales_Steuerrecht/Allgemeine_Informationen/2025-08-05-datensatz-datensatzbeschr-mindeststeuer.pdf?__blob=publicationFile&v=3
- Text: Textebene der amtlichen PDF-Datei, unverändert

---

Bundesministerium der Finanzen, 11016 Berlin
Nur per E-Mail
Oberste Finanzbehörden der Länder
nachrichtlich:
Bundeszentralamt für Steuern

Wilhelm straße 97 10117 Berlin Tel. +49 30 18 682-0 poststelle@bmf.bund.de www.bundesfinanzministerium.de 5. August 2025

Betreff: Mindeststeuergesetz; Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der Datensatzbeschreibung für die Übermittlung der Mindeststeuer-Berichte Anlagen: 1 GZ: IV B 5 - S 1100/00001/002/121 DOK: COO.7005.100.2.12636923 Seite 1 von 2
(bei Antwort bitte GZ und DOK angeben)

Mit dem Gesetz zur Umsetzung der Richtlinie (EU) 2022/2523des Rates zur Gewährleistung einer globalen Mindestbesteuerung und weiterer Begleitmaßnahmen vom 21. Dezember 2023 (BGBl. 2023 I Nr. 397 vom 27. Dezember 2023) wurden die internationalen Vereinbarungen der globalen Mindestbesteuerung für Geschäftsjahre, die nach dem 30. Dezember 2023 beginnen, umgesetzt.
Ein Teil der administrativen Pflichten ist die Abgabe des Mindeststeuer-Berichts. Dieser istnach amtlich vorgeschriebenem Datensatz über die amtlich bestimmte Schnittstelle elektronisch zu übermitteln.
Hiermit wird der amtlich vorgeschriebene Datensatz gemäß § 75 Absatz 3 Satz 4 MinStG bekanntgegeben.Der aktuell amtlich vorgeschriebene Datensatz sowie zukünftig geänderte Versionen stehen aufder Internetseite des BZSt (www.bzst.bund.de) zur Ansicht und zum Abruf bereit. Darüber hinaus istdie Datensatzbeschreibung als Anlage beigefügt.
Nähere Informationen zur Übermittlung der Mindeststeuer-Berichte können auf der Internetseite des BZSt (www.bzst.bund.de) abgerufen werden. Der Datenaustausch erfolgt im XML-Formatund wird in einem automatisierten Verfahren über die DIP-Schnittstelle (Digitaler Posteingang – Schnittstelle) für Massendaten durchgeführt.

Seite 2 von 2 Die Veröffentlichung erfolgt im BundessteuerblattTeil I. Im Auftrag Bruns Die ses Dokument wurde elektronisch erstellt und ist ohne Unterschrift gültig.

Datensatzbeschreibung Aufbau der zu meldenden Daten nach GIR-XML-Schema v1.0 der OECD

Komplexe Datentypen
XML Attribute L-Spalte
Kardinalität-Spalte 1
1..n 0..1 0..n

Legende
Komplexe Datentypen sind in der Datensatzbeschreibung an der entsprechenden Stelle mit Fettschrift gekennzeichnet und dort entsprechend zu ersetzen.
XML Attribute sind kursiv geschrieben
Ebene im XML
Erläuterung: Der Datentyp muss genau 1x verwendet werden. Der Datentyp muss mindestens 1x verwendet werden. Er kann danach beliebig oft wiederholt werden. Der Datentyp kann entfallen oder 1x verwendet werden.
Der Datentyp kann entfallen oder beliebig oft wiederholt werden.

P O B - Spalte P
O
B
Format - Spalte an n b d dt en

Erläuterung: Pflicht Dieses Gruppenelement oder Einzelfeld muss gefüllt sein. Option Dieses Gruppenelement oder Einzelfeld kann gefüllt sein. Bedingung Die Verwendung dieses Gruppenelements oder Einzelfeldes ist abhängig von einem anderen Gruppenelement oder Einzelfeld. Hinweise stehen in der Spalte Wertemenge / Erklärung.
Erläuterung: Alphanumerische Zeichen Numerische Zeichen incl. Punkt Boolsche Variable Datum Datum und Zeit Aufzählung

Amtliche Datensatzbeschreibung Aufbau der zu meldenden Daten nach GIR-XML-Schema v1.0 der OECD
Stand 28.07.2025

Version 1.0 (Stand 28.07.2025)

Änderungshistorie
Änderungen Veröffentlichung der amtlichen Datensatzbeschreibung

Bundeszentralamt für Steuern

DIP - Digitaler Posteingang (Massendatenschnittstelle)

L1 dip:dip

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

version
dip:header environment

dip:consignment dip:customerIdentifier
dip:identityProvider
dip:identifier dip:creationTime dip:transferticketId dip:referenceId dip:application code
dip:body dip:consignmentItem
dip:bopAccountId dip:data

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

1

P

Deutsche Bezeichnung

Wertemenge / Erklärung
Digitaler Posteingang (dip) Wurzelverzeichnis Dieser Bestandteil ist stets über die Schemadefinition der dip.xsd zu überprüfen.

1

P

1

P

1

P

1

P

1

P

1

P

1

P

1

P

1

P

0..1 O

1

P

1

P

1

P

1..n P

an en
en
an 1 dt an 1 an 1 an 1

xs:string

dip Version

Attribut zu dip:dip

Version der dip Definition

DipHeaderType

environmentType

Zielumgebung

Attribut zu dip:header

Es können nur die Werte

• TEST

• PROD

verwendet werden.

Aus Gründen des Datenschutzes dürfen Testdaten nur unter Verwendung des

Wertes "TEST" und Produktivdaten nur unter Verwendung des Wertes "PROD"

übermittelt werden.

ConsignmentType

Sendungsdaten

CustomerIdentifierType

Identifikationskennung

Identifikationskennung des Datenübermittlers, anhand dieser eineindeutig

verifiziert werden kann. I.d.R. ein dem Fachverfahren/Fachbereich bekannte

Kennung z.B. ELSTER-Konto-ID oder BZST-Zertifikats-Nummer

identityProviderType

Provider der Identifier-

Festlegung, welchem Provider die Identifier-Kennung zuzuordnen ist: BZST-

Kennung

CERT einem BZSt-Zertifikat, ELSTER einem ELSTER-Konto

Es können nur die Werte

• BZST-CERT

• ELSTER

verwendet werden.

16 identifierType

Identifier-Kennung

Identifier-Kennung

xs:dateTime

Erzeugungszeitpunkt

Erzeugungszeitpunkt der Lieferung als Zeitstempel

170 customTicketIdNumberType Identifikationsnummer der Identifikationsnummer der Lieferung, eine eineindeutige Kennung dieser

Lieferung

Lieferung

170 customTicketIdNumberType Identifikationsnummer einer Identifikationsnummer einer Bezugs-Lieferung als Referenz auf die

Bezugs-Lieferung

transferticketId einer vorhergehende Lieferung

applicationType 12 applicationCodeType

Verfahrensbezeichnung

Bennenung des Ziel-Fachverfahrens, z.B. DAC7, DAC8, CESOP, CRS.

Fachverfahrensbezeichnung Attribut zu dip:application

Angabe zur Bezeichnung des Fachverfahrens

Hier ist der Wert "PILLAR_II" zu verwenden.

DipBodyType ConsignmentItemType

Inhalte der Lieferung Meldungen

Multiplizität zur Lieferung mehrerer Anträge/Meldungen in einer Lieferung Für PILLAR_II Lieferungen darf nur ein dip:consignmentItem übermittelt werden.

0..1 O

1

P

an 1 36 bopAccountIdType xs:anyType

Benutzerkennung Nutzdaten-XML

Benutzerkennung des Antragstellers im POSt 2.0 (BOPNeu) für Zustellung eines Verwaltungsaktes im Portal An dieser Stelle sind die Nutzdaten im Format des Fachverfahrens-XMLs anzugeben. Weitere Informationen zu diesem Schema sind unter PILLAR II - GIR Nutzdaten zu finden.

Seite 3 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

GLOBE_OECD

version

globe:MessageSpec

globe:SendingEntityIN
globe:TransmittingCountry globe:ReceivingCountry globe:MessageType
globe:Warning

globe:Contact

globe:MessageRefId
globe:MessageTypeIndic
globe:ReportingPeriod
globe:Timestamp globe:GLOBEBody
globe:FilingInfo globe:FilingCE

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp
1

0..1 O

an

1 10 stf:StringMin1Max10_Type

1P

globe:MessageSpec_Type

0..1 O

an

1P

en

1P

en

1P

en

0..1 O

an

1 200 stf:StringMin1Max200_Type

2

2 iso:CountryCode_Type

2

2 iso:CountryCode_Type

1

1 globe:MessageType_EnumType

1 4000 stf:StringMin1Max4000_Type

0..1 O

an

1 4000 stf:StringMin1Max4000_Type

1P

an

1 170 stf:StringMin1Max170_Type

1P

en

globe:MessageTypeIndic_EnumType

1P

d

1P

dt

1..n P

1P

1P

xsd:date
xsd:dateTime globe:GlobeBody_Type globe:FilingInfo

Deutsche Bezeichnung GIR-Version Kopfdaten Identifizierungsnummer des Datensenders Übermittelnder Staat Empfangender Staat Typ der Nachricht Warnung Kontakt
MessageRefId
Art der Meldung

Wertemenge / Erklärung (deut.)
Hier ist die Schemaversion anzugeben, in der die GIR-Mitteilung erstellt wurde. Derzeit ist der Wert "1.0" zu verwenden. Die Informationen in den Kopfdaten der Mitteilung geben Auskunft über den übermittelnden Staat, den Zeitpunkt der Erstellung der Mitteilung, den Meldezeitraum auf den sich die Mitteilung bezieht und die Art der Mitteilung (Original, Korrektur, Löschung etc.). Während diese Angabe nicht für den Austausch zwischen (COMPETENT AUTHORITIES) genutzt wird, kann die Angabe in dem Fall gemacht werden, in dem eine Abgabe an das BZSt durch eine inländische Geschäftseinheit vorgesehen ist. In solchen Fällen dient die Angabe zur Identifizierung der inländischen Geschäftseinheit, welche die Nachricht übergibt.
Durch dieses Datenelement kann die Jurisdiktion identifiziert werden, welche die Information übergibt. Diesem Element wird das alphabetische Staatenkürzel und der Name des Staates gemäß des ISO 3166-1 Alpha 2 Standard zugrunde gelegt. Durch dieses Datenelement können die Jurisdiktion identifiziert werden, welche gezielte Addressaten der Nachricht werden sollen. Dieses Datenelement spezifiziert, welcher Nachrichtentyp gesendet wird. Die einzig zulässige Angabe dieses Feldes lautet "GIR". Dieses Datenelement ist ein freies Textfeld, das es ermöglicht, spezifische Vorsichtsanweisungen zur Verwendung des GIR-Nachrichteninhalts einzugeben, z. B. die Bedingungen des Instruments oder der Konvention, unter denen die Daten ausgetauscht werden. Bei diesem Datenelement handelt es sich um ein freies Textfeld, in das spezifische Kontaktinformationen für den Absender der Nachricht eingegeben werden können. Bei der inländischen Berichterstattung kann es sich dabei um eine Einzelperson bei der jeweiligen berichtspflichtigen Geschäftseinheit der multinationalen Unternehmensgruppe handeln.
Dieses Datenelement ist ein freies Textfeld, das die eindeutige Nachrichtenkennung des Absenders (vom Absender erstellt) erfasst, die die gesendete Nachricht identifiziert. Der Identifikator ermöglicht sowohl dem Absender als auch dem Empfänger, die spezifische Nachricht später zu identifizieren, falls Fragen oder Korrekturen auftreten. Für den Austausch zwischen zuständigen Behörden muss die erste Komponente der Ländercode des sendenden Landes, die zweite Komponente das Berichtssteuerjahr sein, auf das sich die Daten beziehen (das idealerweise das Jahr ist, in dem der Berichtszeitraum beginnt, aber auch das Jahr, in dem er endet) und die dritte Komponente der Ländercode des empfangenden Landes, gefolgt von einer eindeutigen Kennung, die von dem sendenden Land erstellt wurde (der „nationale Teil“). Dieses Datenelement ermöglicht es dem Absender, den Typ der gesendeten Nachricht zu definieren. Dieses Element gibt an, ob es sich um neue oder korrigierte Daten handelt (siehe Anleitung zum Korrekturprozess unten). Nachrichten müssen alle neuen oder alle korrigierten/gelöschten Daten enthalten oder darauf hinweisen, dass keine Daten zu melden sind.
Siehe mögliche Werte unter globe:MessageTypeIndic_EnumType (GIR101 GIR103) unter Wertelisten für Aufzählungstypen

Meldezeitraum
Zeitstempel Meldungsinhalt Melder-Information Berichtspflichtige Geschäftseinheit

Dieses Datenelement identifiziert den letzten Tag des Berichtswirtschaftsjahres, auf das sich die Meldung im Format yyyy-MM-TT bezieht. Die Angabe erfolgt grundsätzlich auf Basis des Kalenderjahres in dem der Meldezeitraum endet. Es kann jedoch auch ein anderer geeigneter Meldezeitraum angegeben werden. Format: JJJJ-MM-TT Beispiel: Für das Meldejahr 2026 wäre somit die Angabe "2026-12-31" vorzunehmen.
Dieses Datenelement identifiziert das Datum und die Uhrzeit, zu der die Nachricht zusammengestellt wurde. Es wird erwartet, dass dieses Element automatisch vom Host-System ausgefüllt wird. Das Format für die Verwendung ist yyyy-MMTT'T'hh:mm:ss.nnn. Sekundenbruchteile können verwendet werden (in diesem Fall werden die Millisekunden in 3 Stellen angegeben, siehe ".nnn" im Format oben). Beispiele: 2027-03-15T09:45:30 oder 2027-03-15T09:45:30.789 (mit Millisekunden). Die Uhrzeit sollte im 24-Stunden-Format eingegeben werden. Das GloBE-Body-Element enthält Informationen zur berichtspflichtigen Geschäftseinheit, zur General Section, Summary Jurisdiction Section, und UTPRAttribution des GIR. Das Element „Filing Info“ identifiziert die berichtspflichtige Geschäftseinheit, die multinationale Unternehmensgruppe, die Buchhaltungsinformationen und das Berichtsjahr, auf das sich der GIR bezieht. Dieses Filing-CE-Element identifiziert die berichtspflichtige Geschäftseinheit, die den globalen Mindeststeuer-Bericht (GIR) einreicht. Wenn mehrere berichtspflichtige Geschäftseinheiten den globalen Mindeststeuer-Bericht einreichen, muss jede von ihnen einen separaten globalen Mindeststeuer-Bericht einreichen. Er besteht aus den folgenden vier Elementen.

Seite 4 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:ResCountryCode globe:Name

globe:TIN

globe:Role globe:AccountingInfo

globe:CFSofUPE

globe:FAS

globe:Currency globe:Period
globe:Start globe:End globe:NameMNE
globe:AdditionalInfo
globe:DocSpec
globe:GeneralSection

globe:RecJurCode

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1P

en

1P

an

2

2 iso:CountryCode_Type

1 200 stf:StringMin1Max200_Type

1P

an

1 200 globe:TIN_Type

1P

en

1P

globe:FilingCERole_EnumType

1P

en

globe:FilingCECofUPE_EnumType

1P

an

1 200 stf:StringMin1Max200_Type

1P

en

1P

1P

d

1P

d

1P

an

1O

an

1P

3

3 iso:currCode_Type

xsd:date xsd:date

1 200 stf:StringMin1Max200_Type

1 4000 stf:StringMin1Max4000_Type

stf:docspec_type

0..1 O

globe:GeneralSection_Type

1..n P

en

2

2 iso:CountryCode_Type

Deutsche Bezeichnung Ansässigkeitsstaat Name
Steueridentifikationsnummer
Rolle Buchhaltungsinformation
Definition von UPE Konzernabschlüssen
Rechnungslegungsstandard
Währung Zeitraum Start Ende Name der multinationalen Unternehmensgruppe Zusätzliche Informationen Dokumentenspezifikation Allgemeiner Teil
Empfängerstaaten-Code

Wertemenge / Erklärung (deut.)
Das Element „ResCountryCode“ gibt den zweistelligen alphabetischen Ländercode auf Grundlage des ISO 3166-1 Alpha 2-Standards für das Steuerhoheitsgebiet an, in dem sich die berichtspflichtige Geschäftseinheit befindet. Dieses Namenselement gibt den vollständigen gesetzlichen Namen der berichtspflichtigen Geschäftseinheit an.
Das TIN-Element gibt die Steueridentifikationsnummer (engl. tax identification number - TIN) der berichtspflichtigen Geschäftseinheit an. Die berichtspflichtige Geschäftseinheit muss ihre TIN angeben, die für Zwecke der erfassten Steuern im Einreichungsstaat verwendet wird, oder, falls keine TIN verfügbar ist, ein funktionales Äquivalent, z. B. eine Handelsregisternummer. Falls keine TIN eingegeben wird, ist der Wert NOTIN anzugeben. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.
Das Element „Role“ gibt die Rolle der berichtspflichtigen Geschäftseinheit an. Mögliche Werte sind: siehe globe:FilingCERole_EnumType (GIR401 - GIR405) unter Wertelisten für Aufzählungstypen
Wenn in diesem Element „GIR403“ oder „GIR404“ als Wert ausgewählt wird, wird davon ausgegangen, dass der GIR über eine lokale Einreichung bereitgestellt wird. Das Element „AccountingInfo“ spiegelt die Buchhaltungsinformationen in Bezug auf die UPE wider und besteht aus den nachfolgenden drei Elementen. Das Element „CFSofUPE“ bezeichnet den relevanten Unterabsatz (a), (b), (c) und (d) der Definition des Konzernabschlusses in Artikel 10.1, der für den Konzernabschluss der UPE gilt. Im Falle von Buchstabe (d) muss die berichtspflichtige Geschäftseinheit die Identifizierung der UPE mit angemessener Sorgfalt und nach Treu und Glauben durchführen . Mögliche Werte sind: siehe globe:FilingCECofUPE_EnumType (GIR501 - 504) unter Wertelisten für Aufzählungstypen
Das Element „FAS“ gibt den Rechnungslegungsstandard an, der für den Konzernabschluss der obersten Muttergesellschaft verwendet wird. Wenn die oberste Muttergesellschaft keinen Konzernabschluss erstellt, muss die berichtspflichtige Geschäftseinheit den anerkannten Rechnungslegungsstandard angeben, der entweder ein anerkannter Rechnungslegungsstandard oder ein anderer Rechnungslegungsstandard ist, der angepasst wurde, um erhebliche Vergleichbarkeitseinschränkungen zu vermeiden.
Das Element „Currency“ spiegelt den für den Konzernabschluss der obersten Muttergesellschaft (UPE) verwendeten iso:curCode_Type wider. Erstellt die UPE keinen Konzernabschluss, muss die berichtspflichtige Geschäftseinheit den ISOCode der Währung angeben, die für die Zwecke der GloBE-Regeln verwendet wird.
Die Beträge sind in vollen Einheiten, d. h. ohne Dezimalstellen, anzugeben. Der Code für die Währung, in der der Wert ausgedrückt wird, ist der ISO-Codeliste 4217 zu entnehmen und im Attribut „currCode“ hinzuzufügen. Dieses Element gibt das Start- und Enddatum des Berichtsgeschäftsjahres an und besteht aus den folgenden zwei Elementen. Das Startelement gibt das Startdatum des Berichtsgeschäftsjahres an. Das Endelement gibt das Enddatum des Berichtsgeschäftsjahres an. Das Element „Name MNE“ gibt den Namen der multinationalen Unternehmensgruppe an, der üblicherweise bei der Erstellung ihres Konzernabschlusses verwendet wird. Das optionale Element „AdditionalInfo“ kann verwendet werden, um den Steuerbehörden ad hoc zusätzliche Erläuterungen zum GIR bereitzustellen und sollte grundsätzlich nur auf Grundlage der entsprechenden Verwaltungsrichtlinien verwendet werden.
DocSpec identifiziert den jeweiligen Bericht innerhalb der übermittelten GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die korrigiert werden müssen (weitere Hinweise unter stf:docspec_type unter Komplexe Datentyp DAC9). Das optionale Element „General Section“ (Hinweis: Der Umfang des Begriffs ist im Vergleich zur Definition gemäß GIR MCAA eingeschränkt) enthält Informationen zur Unternehmensstruktur der Gruppe. Das Element gibt außerdem die relevanten Empfängerstaaten der GeneralSection für den Informationsaustausch an.
Der wiederholbare RecJurCode gibt die relevanten Empfängerstaaten der General Section für den Informationsaustausch an. Beabsichtigt die multinationale Unternehmensgruppe, den globalen Mindeststeuer-Bericht lokal einzureichen, muss der nationale Jurisdiktionscode in das Element eingetragen werden.
Die berichtspflichtige Geschäftseinheit muss die Steuerhoheitsgebiete angeben, in denen die Berichtspflichten der Geschäftseinheiten durch Informationsaustausch gemäß Artikel 8.1.2 erfüllt werden sollen.

Seite 5 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:CorporateStructure

globe:UPE globe:ExcludedUPE
globe:ExcludedUPEStatus
globe:Art10.3.5 globe:ID globe:OtherUPE
globe:Art10.3.5 globe:ID globe:CE globe:ID

globe:OwnershipChange globe:ChangeDate globe:PreGlobeStatus

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1P

globe:CorporateStructureType

1..n P 1B

1P

en

1 200 globe:ExcludedUPE_EnumType

0..1 O

en

1P 1B

2

2 iso:CountryCode_Type

globe:ExcludedUPE_ID_Type

0..1 O

en

1P

0..n O 1P

2

2 iso:CountryCode_Type

globe:ID_Type

globe:ID_Type

0..n O

1P

d

1..n P

en

xsd:date globe:IDGloBEStatus_EnumType

Deutsche Bezeichnung Unternehmensstruktur
oberste Muttergesellschaft ausgeschlossene oberste Muttergesellschaft Status von ausgeschlossener oberster Muttergesellschaft
Artikel 10.3.5 Identifikationsinformationen andere oberste Muttergesellschaft
Artikel 10.3.5 Identifikationsinformationen Geschäftseinheit Identifikationsinformationen
Eigentümerwechsel
Änderungsdatum
vorheriger Status der Geschäftseinheit

Wertemenge / Erklärung (deut.)
Das Element „Corporate Structure enthält Informationen zur Unternehmensstruktur der multinationalen Unternehmensgruppe.
Das wiederholbare „UPE“ Element enthält identifizierende Informationen zu obersten Muttergesellschaften (UPEs). Das Element ermöglicht die Auswahl der ausgeschlossenen UPE über eine Aufzählungsliste oder eine andere UPE mit IDTyp.
Wenn es sich bei der multinationalen Unternehmensgruppe um eine multinationale Unternehmensgruppe mit mehreren Muttergesellschaften handelt, muss die einreichende Unternehmenseinheit dieses UPE-Element für jede UPE ausfüllen.
Wenn die UPE eine ausgeschlossene Einheit ist, spiegelt dieses Feld ihre Art wider.
Mögliche Werte siehe globe:ExcludedUPE_EnumType (GIR601 - GIR606) unter Wertelisten für Aufzählungstypen Dieses Datenelement identifiziert das Steuerhoheitsgebiet, in der eine Muttergesellschaft gemäß Art. 10.3.5 eine anerkannte Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR) anwenden muss, auch wenn sich diese Muttergesellschaft für GloBE-Zwecke in einem anderen Steuerhoheitsgebiet befindet. Es verwendet den zweistelligen alphabetischen Ländercode und die Ländernamenliste basierend auf dem ISO 31661 Alpha 2-Standard. Das ID-Element enthält Informationen zur Identifizierung des ausgeschlossenen UPE und folgt dem ID-Typ, wie unter Komplexe Datentypen globe:ExcludedUPE_ID_Type beschrieben. Das Element „OtherUPE“ identifiziert die oberste Muttergesellschaft (mit Ausnahme einer ausgeschlossenen obersten Muttergesellschaft).
Dieses Datenelement identifiziert das Steuerhoheitsgebiet, in der eine Muttergesellschaft gemäß Art. 10.3.5 einen QIIR anwenden muss, auch wenn sich diese Muttergesellschaft für GloBE-Zwecke in einem anderen Steuerhoheitsgebiet befindet. Es verwendet den zweistelligen alphabetischen Ländercode und die Ländernamenliste basierend auf dem ISO 3166-1 Alpha 2-Standard. Das ID-Element enthält Informationen zur Identifizierung der anderen obersten Muttergesellschaft und folgt dem ID-Typ, siehe globe:ID_Type unter Komplexe Datentyp DAC9.
Das wiederholbare Element „CE“ enthält Identifizierungs- und Eigentumsinformationen zu Geschäftseinheiten und Mitgliedern von JV-Gruppen der multinationalen Unternehmensgruppe. Es besteht aus den folgenden fünf Elementen. Das „ID“ Element enthält identifizierende Informationen zu jeder Geschäftseinheit und JV-Gruppenmitglied und folgt dem ID-Typ, siehe globe:ID_Type unter Komplexe Datentyp DAC9.
Das Element „OwnershipChange“ muss nicht ausgefüllt werden, wenn die Geschäftseinheit (oder eine andere Geschäftseinheit der multinationalen Unternehmensgruppe) oder das Mitglied einer Joint Venture-Gruppe im Berichtsgeschäftsjahr keinen Änderungen unterlag. Das Element „OwnershipChange“ muss nur für Änderungen ausgefüllt werden, die sich zu irgendeinem Zeitpunkt im Berichtsgeschäftsjahr auf die Berechnung des effektiven Steuersatzes (z. B. für Geschäftseinheiten, die an der grenzüberschreitenden Verteilung von Einkünften oder Steuern beteiligt sind) oder auf die Berechnung oder Verteilung der Ergänzungssteuerbeträge (z. B. das Ausmaß der Anwendung der Primärergänzungssteuerregelung (engl. IIR) auf eine Gesellschaft) ausgewirkt haben. Das Element „OwnershipChange“ besteht aus den folgenden drei Elementen. Das Element „Change Date“ gibt das Datum des Inkrafttretens (im Format JJJJ-MMTT) aller Änderungen der Eigentumsstruktur oder des Status der Geschäftseinheit (oder einer anderen Einheit der multinationalen Unternehmensgruppe) oder eines Mitglieds einer Joint Venture-Gruppe an. Unterlag eine Geschäftseinheit (oder eine andere Einheit der multinationalen Unternehmensgruppe) oder ein Mitglied einer Joint Venture-Gruppe im Berichtsjahr mehreren Änderungen, ist jede Änderung separat darzustellen. Das Element „PreGlobeStatus“ gibt den für GloBE-Zwecke relevanten Status der Geschäftseinheit (oder einer anderen Einheit der multinationalen Unternehmensgruppe) oder des Mitglieds der JV-Gruppe am Tag unmittelbar vor dem Datum der Änderung an.
Mögliche Werte siehe globe:IDGloBEStatus_EnumType (GIR701–GIR721) unter Wertelisten für Aufzählungstypen

Seite 6 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:PreOwnership

globe:OwnershipType

globe:TIN

globe:PreOwnershipPercentage globe:Ownership
globe:OwnershipType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp
0..n O

1P

en

globe:OwnershipType_EnumType

1P

an

1 200 globe:TIN_Type

1P

n

1..n P

1

6 globe:percentage

1P

globe:OwnershipType_EnumType

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das wiederholbare Element „PreOwnership“ zeigt die Entitäten an, die Eigentumsanteile an der CE (oder einer anderen Entität) oder einem Mitglied der JVGruppe vor der ersten gemeldeten Änderung halten, sowie den Prozentsatz dieser Eigentumsanteile. Die berichtspflichtige Geschäftseinheit darf das Element PreOwnership nicht für ausgeschlossene Einheiten vervollständigen, die vor der Änderung ausgeschlossene vorherige Eigentumsverhältnisse Einheiten waren.

Eigentumstyp Steueridentifikationsnummer

Das Element „OwnershipType“ gibt die Art der Einheit an, die direkte Eigentumsanteile an der Geschäftseinheit oder einem Mitglied einer JV-Gruppe oder indirekte Eigentumsanteile an der Geschäftseinheit oder einem Mitglied einer JVGruppe über ausgeschlossene Einheiten oder Nicht-Gruppenmitglieder hält. Mögliche Werte siehe (nur einer auswählbar): globe:OwnershipType_EnumType (GIR801 - GIR806) unter Wertelisten für Aufzählungstypen
„Ausgeschlossene Einheiten (aggregiert)“ und „Nicht-Gruppenmitglieder (aggregiert)“ werden im Aggregat ausgewiesen. „Ausgeschlossene Einheiten (aggregiert)“ und „Nicht-Gruppenmitglieder (aggregiert)“ werden im Aggregat ausgewiesen. Nicht-Gruppenmitglieder sind Einheiten, die keine Gruppeneinheiten oder Mitglieder einer JV-Gruppe sind.
Das TIN-Element gibt die Steueridentifikationsnummer (TIN) der Geschäftseinheit, der Konzerneinheit, der ausgeschlossenen Einheit, des Mitglieds einer JV-Gruppe oder eines Nicht-Gruppenmitglieds an, die am Tag vor der Transaktion direkt Eigentumsanteile an der Geschäftseinheit (oder einer anderen Einheit der multinationalen Unternehmensgruppe) oder einem Mitglied einer JV-Gruppe hielt. Ausgeschlossene Einheiten, die nicht zur UPE gehören, und Nicht-Gruppenmitglieder sind aggregiert zu melden (d. h. „Ausgeschlossene Einheiten (aggregiert)“ und „NichtGruppenmitglieder (aggregiert)“).
Die berichtspflichtige Geschäftseinheit muss auch alle Geschäftseinheiten melden, die am Tag vor der Transaktion indirekt Eigentumsanteile an der Unternehmenseinheit (oder einer anderen Einheit der multinationalen Unternehmensgruppe) über ausgeschlossene Einheiten oder NichtGruppenmitglieder hielten. Falls keine TIN eingegeben wird, ist der Wert NOTIN anzugeben. Der TIN-Typ ist gemäß dem Komplexdatentyp „globe:TIN-Type“ auszufüllen.

vorheriger Eigentumsanteil Eigentum
Eigentumstyp

Das Element „PreOwnership Percentage“ gibt die Eigentumsanteile an, die an der Geschäftseinheit (oder einer anderen Einheit der multinationalen Unternehmensgruppe) oder einem Mitglied einer Joint-Venture-Gruppe von den oben genannten Geschäftseinheiten, ausgeschlossenen Einheiten, Mitgliedern von Joint-Venture-Gruppen und konzernfremden Mitgliedern an dem Tag gehalten werden, der dem Datum der Änderung unmittelbar vorausgeht, in Übereinstimmung mit den in Anmerkung 1.3.2.1.10 enthaltenen Leitlinien.
Wird eine Geschäftseinheit (oder ein anderes Unternehmen der multinationalen Unternehmensgruppe) oder ein Mitglied einer JV-Gruppe während des Berichtsgeschäftsjahres abgewickelt, meldet die berichtspflichtige Geschäftseinheit den entsprechenden Status für GloBE-Zwecke am Tag der Änderung vor der Transaktion im Element „PreGloBEStatus“ und „NichtGruppenmitglied“ im Element „GloBEStatus“. Die berichtspflichtige Geschäftseinheit gibt dann im Element PreOwnershipTypedie Unternehmen an, die am Tag der Änderung vor der TransaktionEigentumsanteile an der Geschäftseinheit (oder einem anderen Unternehmen der multinationalen Gruppe) oder einem Mitglied einer JV-Gruppe halten, und meldet im Element PreOwnershipPercentage die Eigentumsanteile, die jedes dieser Einh iten an der Geschäftseinheit (oder einem anderen Unternehmen der multinationalen Gruppe) oder einem Mitglied einer JV-Gruppe hält. Die berichtspflichtige Geschäftseinheit füllt jedoch das Element „OwnershipPercentage“ nicht aus. Das Element „Ownership“ spiegelt das Eigentum an den Geschäftseinheiten und Mitgliedern von Joint Ventures zum letzten Tag des Berichtsjahres wider. Es besteht aus den Elementen „Eigentumstyp“, „Steueridentifikationsnummer“ und „Eigentumsanteil“.
Das Element „Ownership Type“ gibt den Typ der Entität an, die direkte Eigentumsanteile an der Geschäftseinheit oder einem Mitglied einer JV-Gruppe oder indirekte Eigentumsanteile an der Geschäftseinheit oder einem Mitglied einer JVGruppe über ausgeschlossene Entitäten oder Nicht-Gruppenmitglieder hält. Die möglichen Werte sind (nur einer anwendbar): siehe globe:OwnershipType_EnumType (GIR801 - GIR806) unter Wertelisten für Aufzählungstypen „Ausgeschlossene Entitäten (Aggregat)“ und „Nicht-Gruppenmitglieder (Aggregat)“ werden im Aggregat gemeldet.

Seite 7 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TIN

globe:OwnershipPercentage
globe:QIIR
globe:POPE-IPE globe:Exception
globe:ExceptionRule globe:Art2.1.3

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1P

an

1 200 globe:TIN_Type

1P

n

1

6 globe:percentage

0..1 O

1P

en

0..1 O

1P

1B

b

globe:POPEIPE_EnumType

1

1 xsd:boolean

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Steueridentifikationsnummer

Das TIN-Element gibt die TIN (oder, wenn keine TIN verfügbar ist, ein funktionales Äquivalent, wie z. B. einen Geschäfts-/Firmenregistrierungscode/eine -nummer) der Geschäftseinheit, Joint Ventures oder Joint Venture-Tochtergesellschaften an, die Eigentumsanteile an der Geschäftseinheit, dem Joint Venture oder der Joint VentureTochtergesellschaft halten. Für ausgeschlossene Unternehmen, die nicht die UPE und Nicht-Gruppenmitglieder sind, muss keine TIN angegeben werden, da sie in der Gesamtheit angegeben werden (d. h. „Ausgeschlossene Unternehmen (Gesamtheit)“ und „Nicht-Gruppenmitglieder (Gesamtheit)“. Falls keine TIN eingegeben wurde, muss der Wert NOTIN angegeben werden. Der TIN-Typ muss entsprechend dem TIN-Typ ausgefüllt werden.

Eigentumsanteil

Das Element „Ownership Percentage“ gibt (in Prozent) die Eigentumsanteile an, die die unter „Eigentumsart“ angegebenen Geschäftseinheiten, ausgeschlossenen Einheiten und Nicht-Konzernmitglieder direkt an der Gesellschaftseinheit, dem Joint Venture oder der JV-Tochtergesellschaft halten. Die meldende Gesellschaft muss die Eigentumsanteile von Nicht-Konzernmitgliedern insgesamt melden. Halten mehrere ausgeschlossene Gesellschaften direkte Eigentumsanteile an einer Gesellschaftseinheit, einem Joint Venture oder einer JV-Tochtergesellschaft, ist der Gesamtbetrag aller ausgeschlossenen Gesellschaften anzugeben. Wenn eine Konzerneinheit, ein Joint Venture oder eine Joint-Venture-Tochtergesellschaft über eine oder mehrere ausgenommene Einheiten oder über Nicht-Konzernmitglieder indirekte Eigentumsanteile an einer Unternehmenseinheit, einem Joint Venture oder einer Joint-Venture-Tochtergesellschaft hält, muss die einreichende Unternehmenseinheit zusätzlich zu etwaigen Eigentumsanteilen, die diese Konzerneinheit, dieses Joint Venture oder diese Joint-Venture-Tochtergesellschaft direkt hält, die Eigentumsanteile melden, die sie indirekt über ausgenommene Einheiten oder Nicht-Konzernmitglieder hält. Um Doppelzählungen zu vermeiden, dürfen in diesem Fall die Eigentumsanteile, die von solchen ausgenommenen Einheiten oder Nicht-Konzernmitgliedern direkt an der Unternehmenseinheit, dem Joint Venture oder der Joint-Venture-Tochter gehalten werden und die bei der Berechnung des Eigentumsanteils dieser Konzerneinheit berücksichtigt werden, nicht separat gemeldet werden. Wenn es sich bei der Unternehmenseinheit um eine Betriebsstätte handelt, muss die einreichende Unternehmenseinheit die Haupteinheit unter „Eigentumsart“ identifizieren und unter „Eigentumsprozentsatz“ 100 % melden.

Das Element „QIIR“ enthält Informationen darüber, ob Geschäftseinheiten (CEs), die

in Teileigentum stehende Muttergesellschaften (POPEs) POPEs oder

zwischengeschaltete Muttergesellschaften sind, eine

Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR)

anwenden müssen. Das Element „QIIR“ ist in Bezug auf die Geschäftseinheit nur

auszufüllen, wenn in dem Steuerhoheitsgebiet, in dem sich die Geschäftseinheit

befindet, eine QIIR gilt und die Geschäftseinheit eine POPE oder eine

zwischengeschaltete Muttergesellschaft ist. Diese Informationen sind nicht in Bezug

Anerkannte

auf Mitglieder von JV-Gruppen oder Unternehmen zu melden, die keine (direkten

Primärergänzungssteuerregelun oder indirekten) Eigentumsanteile an einer anderen Geschäftseinheiten besitzen, da

g

diese Gruppeneinheiten keine potenziellen Muttergesellschaften sind.

Das Element „POPE-IPE“ gibt die Art der betreffenden Muttergesellschaft an.

Mögliche Werte sind:

Siehe globe:POPEIPE_EnumType (GIR901 - GIR903) unter Wertelisten für

Aufzählungstypen

Art der Muttergesellschaft Ausnahme Ausnahmeregel
Artikel 2.1.3

Gemäß der Definition der in Teileigentum stehenden Muttergesellschaft ist die Muttergesellschaft eine im Teileigentum stehende Muttergesellschaft, wenn mehr als 20 % der Eigentumsanteile an ihren Gewinnen (direkt oder indirekt) von Personen gehalten werden, die keine Geschäftseinheiten der multinationalen Unternehmensgruppe (MNE) sind, und wenn sie (direkt oder indirekt) einen Eigentumsanteil an einer anderen Geschäftseinheit derselben multinationalen Unternehmensgruppe besitzt. Das Element „Exception“ spiegelt die Anwendung der Ausnahme gemäß Artikel 2.1.3 oder 2.1.5 wider. Das Element „ExceptionRule“ erfordert die Auswahl von entweder Artikel 2.1.3 oder 2.1.5 und besteht ebenfalls aus dem TIN-Element. Das Element „Art. 2.1.3“ gibt an, dass die zwischengeschaltete Muttergesellschaft die Primärergänzungssteuerregelung (IIR) nicht anwenden muss, da die oberste Muttergesellschaft (UPE) die IIR anwendet oder eine andere zwischengeschaltete Muttergesellschaft die IIR anwenden muss.

Seite 8 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

globe:Art2.1.5 globe:TIN globe:QUTPR
globe:Art9.3

1B

b

1

1 xsd:boolean

0..1 O

an

1 200 globe:TIN_Type

0..1 O

1P

b

1

1 xsd:boolean

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das Element „Art. 2.1.5“ besagt, dass eine im Teileigentum stehende Muttergesellschaft die Primärergänzungssteuerregelung (IIR) nicht anwenden muss, wenn sie sich im vollständigen Eigentum (direkt oder indirekt) einer anderen im Teileigentum stehenden Muttergesellschaft befindet, die für das Berichtsgeschäftsjahr eine qualifizierte IIR anwenden muss.

Artikel 2.1.5

Gemäß Artikel 2.1.5 ist eine in Teileigentum stehende Muttergesellschaft nicht zur Anwendung der IIR verpflichtet, wenn sie sich im vollständigen Eigentum (direkt oder indirekt) einer anderen im Teileigentum stehenden Muttergesellschaft befindet, die für das Berichtsgeschäftsjahr eine anerkannte Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR) anwenden muss. Trifft die Ausnahme in Artikel 2.1.5 zu, muss die berichtspflichtige Geschäftseinheit die für die erfassten Steuern verwendete Steueridentifikationsnummer (TIN) des Steuerhoheitsgebiets angeben, in der die andere im Teileigentum stehende Muttergesellschaft für GloBEZwecke ansässig ist. Falls keine Steueridentifikationsnummer verfügbar ist, muss sie ein funktionales Äquivalent wie z. B. eine Unternehmens/Firmenregistrierungsnummer angeben.
Das Validierungselement „TIN“ gibt die für erfasste Steuern verwendete TIN in dem Steuerhoheitsgebiet an, in dem die oberste Muttergesellschaft (engl. Ultimate Parent Entity - UPE), andere zwischengeschaltete Muttergesellschaft (engl. Intermediate Parent Entity - IPE) oder andere in Teileigentum stehende Muttergesellschaft (engl. Partially Owned Parent Entity - POPE) ansässig ist, die für GloBE-Zwecke eine qualifizierte IIR anwenden muss.

Falls keine TIN eingegeben wird, ist der Wert NOTIN anzugeben.

Steueridentifikationsnummer Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Das Element „QUTPR“ gibt an, ob die Sekundärergänzungssteuerregelung (engl.

Undertaxed Profit Rule - UTPR) für die Gesellschaft anwendbar ist und besteht aus

den folgenden drei Elementen.

Dieses Element gilt nicht in Fällen, in denen kein Steuerhoheitsgebeit gemäß der

Anerkannte

UTPR Besteuerungsrechte in Bezug auf das Steuerhoheitsgebiet hat, in dem sich die

Sekundärergänzungssteuerregel Geschäftseinheit befindet, oder in denen die Safe-Harbour-Bestimmungen der UTPR

ung

für dieses Steuerhoheitsgebiet gelten.

Das Element „Artikel 9.3“ gibt an, ob die Anfangsphase der internationalen Tätigkeit

(Artikel 9.3.1 oder Artikel 9.3.5(a)) vorliegt. Ist dies der Fall, sind die folgenden beiden

Elemente nicht auszufüllen.

Artikel 9.3

Die beiden Elemente sind ferner nicht auszufüllen, wenn die oberste Muttergesellschaft (UPE) verpflichtet ist, eine anerkannte Primärergänzugnssteuerregelung (QIIR) in Bezug auf die relevanten Geschäftseinheiten anzuwenden (einschließlich Geschäftseinheiten, die im Steuerhoheitsgebiet der UPE ansässig sind). In allen anderen Fällen muss die berichtspflichtige Geschäftseinheit diese beiden folgenden Elemente nur ausfüllen, wenn eine Muttergesellschaft, die eine QIIR in Bezug auf eine Geschäftseinheit anwenden muss, einen Eigentumsanteil von weniger als 100 % an dieser Geschäftseinheit behält.

Seite 9 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:AggOwnership
globe:UPEOwnership globe:ExcludedEntity
globe:Name globe:Change globe:Type
globe:UnreportChangeCorpStr globe:AdditionalDataPoint globe:DocSpec
globe:Summary

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

0..1 O

n

1

6 globe:percentage

0..1 O

b

0..n O

1P

an

1P

b

1P

en

1

1 xsd:boolean

1 200 stf:StringMin1Max200_Type

1

1 xsd:boolean

globe:ExcludedEntity_EnumType

0..1 O

b

0..n O

1P

1

1 xsd:boolean

stf:docspec_type

0..n O

globe:SummaryType

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

aggregierter Eigentumsanteil
Eigentumsanteil oberster Muttergesellschaft ausgeschlossene Einheit Name Änderung Typ ausgeschlossener Enität
ungemeldete Eigentumsänderung Zusätzlicher Datenpunkt Dokumentenspezifikation
Summary

Das Element „AggOwnership“ gibt die aggregierten Eigentumsanteile in Prozent der Gesamtheit der an dieser Geschäftseinheit gehaltenen Eigentumsanteile an. Die aggregierten (direkten und indirekten) Eigentumsanteile der Muttergesellschaften, die zur Anwendung einer QIIR verpflichtet sind, ergeben sich aus der Summe der Eigentumsanteile jeder Muttergesellschaft, die eine QIIR in Bezug auf die niedrig besteurten Geschäftseinheiten anwenden muss. Der Gesamtbetrag ist null, wenn keine Muttergesellschaft eine QIIR in Bezug auf die niedrig besteuerten Einkünfte der niedrig besteuerten Geschäftseinheit anwenden muss. Ist eine Muttergesellschaft (die indirekt über eine zwischengeschaltete Muttergesellschaft oder eine in Teileigentum stehende Muttergesellschaft, die nicht gemäß Artikel 2.1.3 oder 2.1.5 von der IIR ausgenommen ist, einen Eigentumsanteil an einer niedrig besteuerten Geschäftseinheit hält) zur Anwendung der IIR verpflichtet, werden die relevanten Eigentumsanteile für die Berechnung des Gesamtbetrags nur einmal gezählt.
Für Mitglieder einer Joint Venture-Gruppe gibt das Element „AggOwnership“ den aggregierten, zurechenbaren Anteil der Ergänzungssteuern des Mitglieds der Joint Venture-Gruppe in Prozent des Gesamtbetrags der Ergänzungssteuer für dieses Mitglied der Joint Venture-Gruppe an. Der aggregierte, zurechenbare Anteil der Ergänzungssteuern der Muttergesellschaften, die eine QIIR anwenden müssen, entspricht der Summe der zurechenbaren Anteile der Ergänzungssteuer jeder Muttergesellschaft, die eine QIIR in Bezug auf das niedrig besteuerte Joint Venture oder die JV-Tochtergesellschaft anwenden muss.
Der Gesamtbetrag ist null, wenn keine Muttergesellschaft eine QIIR in Bezug auf die niedrig besteuerten Einkünfte des Joint Ventures oder der JV-Tochtergesellschaft anwenden muss. Hält eine Muttergesellschaft indirekt über eine andere Muttergesellschaft, die die IIR anwenden muss, einen Eigentumsanteil an einem niedrig besteuerten Joint Venture oder einer JV-Tochtergesellschaft, wird der zurechenbare Anteil der Zusatzsteuern für die Berechnung des Gesamtbetrags nur einmal berücksichtigt. Das Element „UPEOwnership“ gibt an, ob alle Eigentumsanteile der obersten Muttergesellschaft (UPE) an der Geschäftseinheit (CE) direkt oder indirekt von Muttergesellschaften gehalten werden, die für diese Geschäftseinheit eine anerkannte Primärergänzungssteuerregelung (QIIR) insgesamt anwenden müssen (oder ob die zurücksetzbaren Anteile der Ergänzungssteuern der Muttergesellschaften, die für das Mitglied der JV-Gruppe eine QIIR anwenden müssen, die Ergänzungssteuer der JV-Gruppe reduzieren müssen). Das wiederholbare Element „Excluded Entity“ enthält Informationen zu ausgeschlossenen Einheiten zum letzten Tag des Berichtsgeschäftsjahres. Eine ausgeschlossene Einheit ist eine Gruppeneinheit gemäß Artikel 1.5.1 oder Artikel 1.5.2. Das Element besteht aus den folgenden drei Elementen. Das Element „Name“ gibt den Namen der ausgeschlossenen Einheit an. Das Element „Change“ zeigt alle Änderungen seit dem vorherigen Berichtsgeschäftsjahr in Bezug auf den Namen oder Typ der ausgeschlossenen Einheit an. Das Element „Type“ gibt den Typ jeder ausgeschlossenen Einheit an.
Mögliche Werte: siehe globe:ExcludedEntity_EnumType (GIR1001–GIR1008) unter Wertelisten für Aufzählungstypen
Die Elemente „UnreportChangeCorpStr“ geben an, ob während des Berichtsgeschäftsjahres aufgetretene Änderungen nicht unter dem Element „OwnershipChange“ gemeldet wurden, da sie zu keinem Zeitpunkt während des Berichtsgeschäftsjahres Auswirkungen auf die Berechnung des effektiven Steuersatzes (engl. Effective Taxrate - ETR), die Berechnung der Ergänzungssteuern oder die Zuweisung der Ergänzungssteuer hatten (z. B. wenn eine Geschäftseinheit, die nicht an einer grenzüberschreitenden Zuweisung von Einkünften oder Steuern beteiligt war, vor der Änderung im direkten und vollständigen Besitz der UPE war und auf eine andere Geschäftseinheit übertragen wird, die im direkten und vollständigen Eigentum der UPE ist). Das wiederholbare Element AdditionalDataPoint setzt sich aus den Elementen Description, Amount, Percentage und Text zusammen. Jedes Element und die entsprechenden Werte sind bei globe:AdditionalDataPointType unter Komplexe Datentypen einsehbar
DocSpec identifiziert den jeweiligen Bericht innerhalb der übermittelten GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die korrigiert werden müssen (weitere Hinweise unter stf:docspec_type unter Komplexe Datentypen). Das wiederholbare Element „Summary“ bietet eine allgemeine Zusammenfassung der Anwendung der GloBE-Regeln auf die multinationale Unternehmensgruppe für alle Steuerhoheitsgebiete, in denen die multinationale Unternehmensgruppe Geschäftseinheiten hat oder Mitglieder von Joint Ventures ansässig sind, sowie für alle Untergruppen, für die eine separate ETR- oder Ergänzungssteuerberechnung gilt. Diese zehn Elemente werden im Folgenden näher beschrieben.

Seite 10 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:RecJurCode globe:Jurisdiction
globe:JurisdictionName
globe:Subgroup

globe:TIN
globe:TypeofSubGroup globe:JurWithTaxingRights

globe:JurisdictionName

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1..n P

en

1P

1O

en

2

2 iso:CountryCode_Type

2

2 iso:CountryCode_Type

0..n O

1P

an

1 200 globe:TIN_Type

1P

en

0..n O

globe:TypeofSubGroup_EnumType

1O

en

2

2 iso:CountryCode_Type

Deutsche Bezeichnung
Empfängerstaaten-Code Jurisdiktion Jurisdiktionsname Untergruppe
Steueridentifikationsnummer
Typ der Untergruppe Steuerhoheitsgebiet(e) mit Besteuerungsrechten

Wertemenge / Erklärung (deut.)
Der wiederholbare RecJurCode gibt die relevanten Empfängerstaaten des Abschnitts „Summary“ für den Informationsaustausch an. Beabsichtigt die multinationale Unternehmensgruppe, den globalen Mindeststeuer-Bericht (engl. GloBE Information Return - GIR) lokal einzureichen, muss der nationale Jurisdiktionscode in das Element eingetragen werden.
Die berichtspflichtige Geschäftseinheit muss die Steuerhoheitsgebiete angeben, in denen die Berichtspflichten der Geschäftseinheiten durch den Informationsaustausch gemäß Artikel 8.1.2 erfüllt werden sollen.
Das Element „JurisdictionName“ gibt den zweistelligen alphabetischen Ländercode für das Steuerhoheitsgebiet an, in dem die MNE-Gruppe Geschäftseinheiten hat oder in dem sich Mitglieder von JV-Gruppen befinden (basierend auf dem Standard ISO 3166-1 Alpha 2). Das wiederholbare Element „Subgroup“ gilt, wenn der Umfang der GloBEBerechnung eine Untergruppe ist. Die berichtspflichtige Geschäftseinheit darf dieses Element nicht ausfüllen, wenn kein Steuerhoheitgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitgebiet besitzt. Das TIN Element gibt die Steueridentifikationsnummer der obersten Einheit in der Eigentümerstruktur jeder Untergruppe an, für die eine separate GloBE-Berechnung gilt. Falls keine Steueridentifikationsnummer angegeben ist, ist der Wert NOTIN anzugeben. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type im unter Komplexe Datentypen auszufüllen.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf asn im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt.
Das wiederholbare Element „TypeofSubGroup“ identifiziert den Typ der Untergruppe anhand der folgenden Optionen von globe:TypeofSubGroup_EnumType (GIR1101–GIR1106) unter Wertelisten für Aufzählungstypen.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt. Das wiederholbare Element „JurWithTaxingRights“ gibt die Namen der Steuerhoheitsgebiet(e) mit Besteuerungsrechten in Bezug auf das im Element „Jurisdiction“ angegebene Steuerhoheitsgebiet an.

Ansässigkeitsstaat

Das Element „JurisdikcionName“ identifiziert das Steuerhoheitsgebiet mit Besteuerungsrechten in Form zweistelliger alphabetischer Ländercodes gemäß ISO 3166-1 Alpha 2. Zu den Steuerhoheitsgebieten mit Besteuerungsrechten kann auch ein Steuerhoheitsgebiet gehören, das von einer Muttergesellschaft die Anwendung einer QIIR gemäß Art. 10.3.5 verlangt, selbst wenn diese Muttergesellschaft für GloBE-Zwecke in einem anderen Steuerhoheitsgebiet ansässig ist.
Ein Steuerhoheitsgebiet hat Besteuerungsrechte gegenüber einem anderen Steuerhoheitsgebiet, wobei gemäß der in den GloBE-Regeln festgelegten Reihenfolge die für dieses Steuerhoheitsgebiet berechnete Ergänzungssteuer zu einer Ergänzungssteuerschuld einer in dem erstgenannten Steuerhoheitsgebiet ansässigen Geschäftseinheit gemäß deren Steuerbestimmungen führen würde. Insbesondere ein QDMTT-Safe-Harbor-Steuerhoheitsgebiet oder ein Steuerhoheitsgebiet mit einer für inländische Einheiten geltenden Primärergänzungssteuerregelung (engl. Income Inclusion Rule - IIR) hat Besteuerungsrechte für sich selbst.
Darüber hinaus können mehrere Steuerhoheitsgebiete Besteuerungsrechte gegenüber demselben Steuerhoheitsgebiet haben. Dies kann beispielsweise der Fall sein, wenn sowohl die UPE als auch eine in Teileigentum stehende Muttergesellschaft die IIR auf eine in einem Drittstaat ansässige Geschäftseinheit anwenden müssen. In diesem Fall müssen sowohl das UPE-Steuerhoheitsgebiet als auch das der in Teileigentum stehenden Muttergesellschaft gemeldet werden. Ebenso hätten UTPR-Steuerhoheitsgebiete Besteuerungsrechte in Bezug auf die Steuerhoheitsgebiete, für die die Ergänzungssteuer gemäß Artikel 2.5 nicht auf Null reduziert wird.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet hat.

Seite 11 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:DiffDomesticTut globe:SafeHarbour

globe:ETRRange globe:SBIE
globe:NotApplicable globe:NoTut
globe:QDMTTut

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1O

en

globe:globeTuT_EnumType

0..1 O

en

globe:SafeHarbour_EnumType

0..1 P

en

globe:ETRRange_EnumType

1P

1P

b

1

1 xsd:boolean

1P

b

1

1 xsd:boolean

0..1 O

en

globe:QDMTTuT_EnumType

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Differenzbetrag Ergänzungssteuer
Safe-Harbour
ETR-Bereich Substanzbasierter Freibetrag Nicht anwendbar Keine Ergänzungssteuer
Anerkannte nationale Ergänzungssteuer

Sofern erforderlich, gibt das Element „DiffDomesticTut“ den Bereich an, in dem der durchschnittliche Betrag der nach nationalem Recht zu zahlenden Ergänzungssteuer liegt, sofern dieser Betrag von der im Element „GloBETut“ angegebenen GloBEErgänzungssteuer abweicht. Zur Berechnung des Durchschnitts werden die in 3.1.10 angegebenen Beträge mit dem nach den GloBE-Modellregeln berechneten Anteil der Ergänzungssteuer des jeweiligen Staates gewichtet.
Mögliche Werte: Siehe globe:globeTuT_EnumType (GIR1501–GIR1509) unter Wertelisten für Aufzählungstypen.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt.
Das wiederholbare Element „SafeHarbour“ gibt an, ob die Ergänzungssteuer für das in Abschnitt 1.4.1 genannte Steuerhoheitsgebiet oder die in Abschnitt 1.4.3 genannte relevante Untergruppe (sofern vorhanden) aufgrund der Anwendung eines SafeHarbour- oder De-minimis-Ausschlusses auf null reduziert wurde. Die berichtspflichtige Geschäftseinheit muss die für die Zwecke des Safe Harbour angewandte Option gemäß Anmerkung 2.2.1.1.1 angeben.
Mögliche Werte: siehe globe:SafeHarbour_EnumType (GIR1201 - GIR1209) unter Wertelisten für Aufzählungstypen
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte für das im Element „JurisdictionName“ genannte Steuerhoheitsgebiet besitzt.
Das Element „ETR-Range“ gibt den Bereich an, in dem der ETR des in Abschnitt 1.4.1 genannten Steuerhoheitsgebiet oder der in Abschnitt 1.4.3 (sofern vorhanden) genannten relevanten Untergruppe liegt, wie in Abschnitt 3.2.1.e angegeben:
Mögliche Werte: Siehe globe:ETRRange_EnumType (GIR1301–GIR1314) unter Wertelisten für Aufzählungstypen
Die berichtspflichtige Geschäftseinheiten füllt dieses Element nicht aus, wenn die multinationale Unternehmensgruppe (oder die relevante Untergruppe) in dem Steuergebiet einen GloBE-Verlust erleidet. Darüber hinaus füllt die einreichende Gesellschaft dieses Element nicht für Steuergebiete (oder Untergruppen) aus, für die Abschnitt 3 des GIR nicht ausgefüllt werden muss.
Die berichtspflichtige Geschäftseinheit füllt dieses Element nicht aus, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt.
Das Element „SBIE“ gibt den substanzbasierten Freibetrag (engl. Substance-based Income Exclusion - SBIE) in Bezug auf das unter 1.4.1 genannte Steuerhoheitsgebiet oder die unter 1.4.3 genannte relevante Untergruppe an, sofern dieser Ausschluss dazu geführt hat, dass in dem Steuerhoheitsgebiet keine Ergänzungssteuer anfällt. Das Element „NotApplicable“ gibt an, dass für das Steuerhoheitsgebiet oder die Untergruppe kein substanzbasierter Freibetrag (SBIE) berechnet wurde. Das Element „NoTut“ gibt an, dass für das Steuerhoheitsgebiet oder die Untergruppe keine Ergänzungssteuer aufgrund des SBIE anfällt.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte für das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet hat. Das Element „QDMTTut“ gibt den Bereich an, in dem die zu zahlende anerkannte nationale Ergänzungssteuer (engl. Qualified Domestic Minimum Top-up Tax QDMTT) für das in Abschnitt 1.4.1 genannte Steuerhoheitsgebiet oder die in Abschnitt 1.4.3 genannte relevante Untergruppe (falls vorhanden) liegt, wie in Abschnitt 3.3.1.f angegeben.
Mögliche Werte: Siehe globe:QDMTTuT_EnumType (GIR1401–GIR1409) unter Wertelisten für Aufzählungstypen
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte für das im Element „JurisdictionName“ genannte Steuerhoheitsgebiet besitzt.

Seite 12 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:GLOBETut globe:AdditionalDataPoint globe:DocSpec
globe:JurisdictionSection
globe:RecJurCode globe:Jurisdiction globe:JurWithTaxingRIghts
globe:JurisdictionName globe:Subgroup
globe:TIN

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O

en

0..n O

1P

globe:globeTuT_EnumType globe:AdditionalDataPointType stf:docspec_type

0..n O

1..n P

en

1P

en

2

2 iso:CountryCode_Type

2

2 iso:CountryCode_Type

0..n O

1P

en

2

2 iso:countrycode_Type

0..n O

1P

an

1 200 globe:TIN_Type

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
GloBE-Ergänzungssteuer Zusätzlicher Datenpunkt Dokumentenspezifikation
JurisdictionSection Empfängerstaaten-Code Jurisdiktion Steuerhoheitsgebiet(e) mit Besteuerungsrechten Juristiktions Name Untergruppe Steueridentifkationsnummer

Wertemenge / Erklärung (deut.)
Das Element GloBETut gibt den Bereich an, in dem die zu zahlende GloBEErgänzungssteuer in Bezug auf das unter 1.4.1 genannte Steuerhoheitsgebiet oder die entsprechende Untergruppe gemäß 1.4.3 (falls vorhanden) liegt, wie unter 3.3.1.e angegeben.
Mögliche Werte: Siehe globe:globeTuT_EnumType (GIR1501–GIR1509) unter Wertelisten für Aufzählungstypen
Wird in 3.1.10 ein anderer Betrag als der unter 3.3.1.f angegebene Betrag angegeben, muss die berichtspflichtige Geschäftseinheit sowohl den Bereich angeben, in dem die zu zahlende GloBE-Ergänzungssteuer (wie unter 3.3.1.f angegeben) liegt, als auch den Bereich, in dem der Gesamtbetrag der Ergänzungssteuer nach den nationalen Rechtsvorschriften jedes Steuerhoheitsgebiets mit Besteuerungsrechten liegt, in Bezug auf das unter 1.4.1 genannte Steuerhoheitsgebiet oder die entsprechende Untergruppe gemäß 1.4.3 (falls vorhanden) und wie unter 3.1.10 angegeben, mit denselben Optionen. Zur Berechnung des Durchschnitts werden die unter 3.1.10 angegebenen Beträge mit dem nach den GlobE-Modellregeln berechneten Anteil der Ergänzungssteuer des jeweiligen Steuerhoheitgebiets gewichtet.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt. Das wiederholbare Element AdditionalDataPoint setzt sich aus den Elementen Description, Amount, Percentage und Text zusammen. Jedes Element und die entsprechenden Werte sind unter globe:AdditionalDataPointType unter Komplexe Datentypen einsehbar
DocSpec identifiziert den jeweiligen Bericht innerhalb der übermittelten GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die korrigiert werden müssen (weitere Hinweise, siehe stf:DocSpec_Type unter Komplexe Datentypen).
Das wiederholbare Element „Jurisdiction Section“ enthält Angaben zu Steuerhoheitsgebieten, in denen relevante Safe-Harbours und Ausschlüsse gelten. Für Steuerhoheitsgebiete, in denen Safe-Harbours und Ausschlüsse nicht gelten, spiegelt es die Berechnungen des effektiven Steuersatzes (engl. Effective Taxrate ETR) wider, gefolgt von Berechnungen der Ergänzungssteuer, falls erforderlich, und schließlich die Zuordnung der Ergänzungssteuer, falls zutreffend.
Es besteht aus vier Unterelementen: RecJurCode, Jurisdiction, GloBE Tax und LowTaxJurisdiction. Das wiederholbare Element „RecJurCode“ gibt die vorgesehene(n) Empfängerjurisdiktion(en) jeder Jurisdiction Section an. Bei lokaler Einreichung des GIR ist der inländische Jurisdiktionscode in das Element einzutragen.
Die berichtspflichtige Geschäftseinheit muss die Steuerhoheitsgebiete angeben, in denen die Berichtspflichten der Geschäftseinheiten durch Informationsaustausch gemäß Artikel 8.1.2 erfüllt werden sollen. Das Element „Jurisdiction“ gibt das Steuerhoheitsgebiet an, für das die Jurisdiction Section erstellt wird. Bei der Meldung staatenloser Geschäftseinheiten ist der Code X5 zu verwenden.
Das wiederholbare Element „JurWithTaxingRights“ spiegelt die Steuerhoheitsgebiet(e) wider, die gemäß den GloBE-Regeln Besteuerungsrechte in Bezug auf das Steuerhoheitsgebiet haben, für die die Jurisdiction Section erstellt wird, zusammen mit den relevanten Elementen „ReportDifference“. Das Element „JurisdictionName“ spiegelt die Steuerhoheitsgebiet(e) wider, die gemäß den GloBE-Regeln Besteuerungsrechte in Bezug auf das Steuerhoheitsgebiet haben, für das die JurisdictionSection erstellt wird. Das wiederholbare Element „Untergruppe“ gilt, wenn der Umfang der GloBEBerechnung eine Untergruppe ist.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt. Das Element „TIN“ gibt die Steueridentifikationsnummer der obersten Einheit in der Eigentümerstruktur jeder Untergruppe an, für den eine separate GloBE-Berechnung gilt. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.
Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt.

Seite 13 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TypeofSubGroup

globe:ReportDifference globe:ETRDifference globe:AdjCoveredTaxDifference globe:AggCurrentTaxExpense
globe:QRTCExpense
globe:OtherTaxCredits globe:DeferTaxExpense globe:NetGloBEDifference globe:SBIEDifference globe:AddCurrentTuTDifference globe:TuTDifference globe:ElectionsDifference

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1..n P

en

globe:TypeofSubGroup_EnumType

0..1 O

0..1 O

n

0..1 O

0..1 O

n

1

6 globe:percentage

xsd:integer

0..1 O

n

xsd:integer

0..1 O

n

0..1 O

n

0..1 O

n

0..1 O

n

0..1 O

n

0..1 O

n

xsd:integer

xsd:integer

xsd:integer

2

2 xsd:integer

xsd:integer

2

2 xsd:integer

0..1 O

an

1 4000 stf:StringMin1Max4000_Type

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)
Das wiederholbare Element „TypeofSubgroup“ identifiziert den Typ der Untergruppen anhand der folgenden Optionen: Siehe globe:TypeofSubGroup_EnumType (GIR1101–GIR1106) unter Wertelisten für Aufzählungstypen

Untergruppentyp

Die berichtspflichtige Geschäftseinheit muss dieses Element nicht ausfüllen, wenn kein Steuerhoheitsgebiet Besteuerungsrechte in Bezug auf das im Element „JurisdictionName“ angegebene Steuerhoheitsgebiet besitzt.
Die berichtspflichtige Geschäftseinheit muss das Element „Report Differences“ und die Unterelemente für ein Steuerhoheitsgebiet ausfüllen, wenn zwischen den in diesem Bericht gemeldeten Informationen und den für die Steuerveranlagung an die Steuerhoheitsgebiete mit Besteuerungsrechten verwendeten Informationen eine meldepflichtige Differenz besteht. Eine meldepflichtige Differenz zwischen den in dieser Erklärung gemeldeten Informationen und den für die Steuerveranlagung an die Steuerhoheitsgebiete mit Besteuerungsrechten verwendeten Informationen besteht, wenn:

(i) der in Abschnitt 1.4.6 angegebene Bereich anders wäre, wenn er auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten ausgefüllt worden wäre; oder

Berichtsdifferenz
ETR Differenzen
Summe angepasster erfasster Steuern
Gesamtbetrag laufender Steueraufwand
Anpassungen in Bezug auf anerkannte erstattungsfähige steuerliche Zulagen

(ii) die in Abschnitt 1.4.7 angegebenen Informationen anders wären, wenn sie auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten ausgefüllt worden wären. Das ETR-Differenzelement enthält den effektiven Steuersatz für das Steuerhoheitsgebiet oder die Untergruppe, die auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten ermittelt wurde. Das Element „AdjCoveredTaxDifference“ enthält die Summe der angepassten erfassten Steuern, die für das jeweiligen Steuerhoheitsgebiet oder die jeweilige Untergruppe auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten berechnet wurden. Das Element „AggCurrentTaxExpense“ enthält den gesamten laufenden Steueraufwand in Bezug auf die unter das Übereinkommen fallenden Steuern nach den Zuweisungen in Artikel 4.3 für das identifizierte Steuerhoheitsgebiet oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten. Das Element „QRTCExpense“ enthält die gemäß Artikel 4.1.2(d) in Bezug auf anerkannte erstattungsfähige steuerliche Zulagen (engl. Qualified Refundable Tax Credits - QRTC) oder marktfähige und übertragbare steuerliche Zulagen vorgenommene Anpassung bei der Berechnung der angepassten erfassten Steuern für den Staat oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten.

Anpassung Berechnung erfasster Steuern

Das Element „OtherTaxCredits“ enthält die Anpassung, die bei der Berechnung der angepassten erfassten Steuern gemäß Artikel 4.1.3(b) in Bezug auf nicht anerkannte erstattungsfähige steuerliche Zulagen oder nicht marktfähige übertragbare steuerliche Zulagen oder sonstige steuerliche Zulagen vorgenommen wurde, die nicht als Minderung des laufenden Steueraufwands erfasst wurden (für das Steuerhoheitsgebiet oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten).

Betrag latenter Steueraufwand
Netto-GloBEEinkommensdifferenz
Betrag des substanzbasierten Freibetrags
Zusätzlicher laufender Steuererhöhungsbetrags
Differenzbetrag Ergänzungssteuer

Das Element „DeferTaxExpense“ gibt den Betrag des latenten Steueraufwands für das Steuerhoheitsgebiet oder die Untergruppe auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten an. Das Element Netto-GloBE-Einkommensdifferenz enthält das Netto-GloBEEinkommen oder den Netto-GloBE-Verlust für das Steuerhoheitsgebiet oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitgebiets mit Besteuerungsrechten Das Element „SBIEDifference“ enthält den Betrag des substanzbasierten Freibetrags (engl. Substance-based Income Exclusion - SBIE) für das Steuerhoheitsgebiet oder die Untergruppe auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten. Das Element „AddCurrentTutDifference“ enthält den zusätzlichen laufenden Steuererhöhungsbetrag für das Steuerhoheitsgebiet oder die Untergruppe auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten. Das Element „TuTDifference“ enthält den Betrag der Ergänzungssteuer des Steuerhoheitsgebiets für das Steuerhoheitsgebiet oder die Untergruppe auf Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten.

Wahldifferenz

Das Element „ElectionsDifference“ gibt an, ob ein Unterschied hinsichtlich der Anwendbarkeit der für ein Steuerhoheitsgbiet oder eine Untergruppe gemeldeten Wahlrechte und der Wahlrechte gemäß der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten besteht.

Seite 14 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:QRTCIncome globe:ExcessNegTaxCarryForw globe:TransitionDifference
globe:LocalCurrency
globe:GloBETax
globe:ETR globe:SubGroup globe:TIN

globe:TypeofSubGroup globe:ETRStatus
globe:ETRException
globe:Deminimis-SimplifiedNMCECalc

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

0..1 O

n

0..1 O

n

0..1 O

b

xsd:integer
xsd:integer xsd:boolean

0..1 O

en

3

3 Iso:currCode_Type

1P

globe:GLOBETax

0..n O

0..1 O

1P

an

1 200 globe:TIN_Type

1P

en

1P

1P

globe:ETRTypeofSubGroup_EnumType

0..1 O

Deutsche Bezeichnung
Anpassung nach Artikel 3.2.4 Überschüssiger negativer Steuervortragssaldo Übergangsjahr
Lokale Währung
GloBE-Steuer
ETR Untergruppe Steueridentifikationsnummer

Wertemenge / Erklärung (deut.)
Das Element „QRTCIncome“ enthält die gemäß Artikel 3.2.4 vorgenommene Anpassung in Bezug auf anerkannte erstattungsfähige steuerliche Zulagen oder marktfähige übertragbare steuerliche Zulagen bei der Berechnung des GloBEGewinns oder -Verlusts für das Steuerhoheitsgebiet oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten. Das Element „ExcessNegTaxCarryForw“ enthält den überschüssigen negativen Steuervortragssaldo, der für die Folgejahre für das Steuerhoheitsgebiet oder die Untergruppe auf der Grundlage der nationalen Gesetzgebung des jeweiligen Steuerhoheitsgebiets mit Besteuerungsrechten verbleibt. Das Element „TransitionDifference“ gibt an, dass das Berichtsgeschäftsjahr das Übergangsjahr für das Steuerhoheitsgebiet oder die Untergruppe ist. Das Element „LocalCurrency“ gibt den iso:curCode_Type an, der für die Einreichung in der lokalen Währung des jeweiligen Steuerhoheitsgebiets verwendet wird, sofern diese von der CFS-Präsentationswährung abweicht. Die Beträge sind in ganzen Einheiten, d. h. ohne Dezimalstellen, anzugeben. Der Code für die Währung, in der der Wert ausgedrückt wird, ist der ISO-Codeliste 4217 zu entnehmen und im Attribut „currCode“ hinzuzufügen. Das Element „GloBE Tax“ spiegelt die Offenlegungen in Bezug auf Steuerhoheitsgebiete wider, in denen relevante Safe-Harbours und Ausschlüsse gelten, sowie ETR-Berechnungen, in denen diese Safe-Harbours und Ausschlüsse nicht gelten. Es besteht aus den Elementen „InitialIntActivity“ und „ETR“. Das Element „GloBE Tax“ spiegelt die Offenlegungen in Bezug auf Steuerhoheitsgebiete wider, in denen relevante Safe-Harbours und Ausschlüsse gelten, sowie ETR-Berechnungen, in denen diese Safe-Harbours und Ausschlüsse nicht gelten. Es besteht aus den Elementen „InitialIntActivity“ und „ETR“. Das Element „Untergruppe“ gibt die Untergruppe an, für die die GloBE-Berechnung durchgeführt wird oder für die die geltenden Safe Harbour-Regelungen oder Ausschlüsse gelten. Das TIN-Element gibt die TIN der Einheit an, das in der Eigentümerstruktur jeder identifizierten Untergruppe an erster Stelle steht. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Typ der Untergruppe

Das wiederholbare Element „TypeofSubGroup“ gibt den Typ der Untergruppe an, die für den Umfang der GloBE-Berechnung identifiziert wurde. Unter diesem Element können mehrere Untergruppen identifiziert werden.
Mögliche Werte: Siehe globe:ETRTypeofSubGroup_EnumType (GIR1601–GIR1609) unter Wertelisten für Aufzählungstypen
Eigenständige MOCEs sind in Minderheitseigentum stehende Geschäftseinheiten, die keiner in Minderheitseigentum stehenden Gruppe angehören. Zu den Investmenteinheiten zählen auch Joint Ventures oder JV-Tochtergesellschaften, die als Investmenteinheiten gelten, jedoch nicht Investmenteinheiten, für die das Wahlrecht gemäß Artikel 7.5 ausgeübt wurde. In Minderheitseigentum stehende Untergruppen können aus Mitgliedern von Joint Ventures bestehen.
Staatenlose Geschäftseinheiten umfassen auch Mitglieder von Joint Ventures, die staatenlos sind. Die berichtspflichtige Geschäftseinheit muss die relevanten Informationen für jede Untergruppe melden.

ETR-Status

Das Element „ETR-Status“ spiegelt die Anwendung rechtlicher Safe-Harbours und Ausschlüsse bzw., sofern keine solchen Ausnahmen gelten, die ETR-Berechnung wider. Es besteht aus den Elementen „ETRException“ und „ETRComputation“.

ETR-Ausnahme

Das Element „ETRException“ spiegelt die Anwendung von Safe-HarbourRegelungen und Ausschlüssen des Steuerhoheitsgebiets wider. Es besteht aus den Elementen „Deminimis“, „TransitionalCbCRSafeHarbour“ und „UTPRSafeHarbour“.

Das Element „Deminimis-SimplifiedNMCECalc“ spiegelt die Wahl des De-minimisAusschlusses sowie die vereinfachten Berechnungen für unwesentliche Geschäftseinheiten wider und besteht aus den Elementen „FinancialData“ und „Average“. Wird der De-minimis-Ausschluss in Bezug auf ein anspruchsberechtigtes Steuerhoheitsgebiet angewendet, sind die Abschnitte 3.2.4.6 (sofern zutreffend) und 3.3.3 (zusätzliche laufende Ergänzungssteuer) für das Steuerhoheitsgebiet auszufüllen.

Deminimis-Regelung zur vereinfachten Berechnung bei unwesentlichen Geschäftseinheiten

Wird die vereinfachte Berechnung für unwesentliche Geschäftseinheiten gemäß Option (a) in Abschnitt 2.2.1.1 genutzt und gelten die vereinfachten Berechnungen für unwesentliche Geschäftseinheiten nur für einige der Geschäftseinheiten der in Abschnitt 2.1.3 genannten Untergruppe, muss die berichtspflichtige Geschäftseinheit auch die Elemente „FinancialData“ und „Average“ ausfüllen.

Seite 15 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:Basis

globe:FinancialData
globe:Year globe:Revenue globe:GlobeRevenue globe:NetGlobeIncome globe:FANIL
globe:Average globe:Revenue globe:GlobeRevenue globe:NetGlobeIncome globe:FANIL
globe:TransitionalCbCRSafeHarbour
globe:Revenue
globe:Profit
globe:IncomeTax globe:UTPRSafeHarbour
globe:CITRate globe:ETRComputation

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

Deutsche Bezeichnung

1P

en

globe:DeminimisSimpleBasis_EnumType Basis

Wertemenge / Erklärung (deut.) Das Element „Basis“ gibt den Grund für das Ausfüllen dieses Abschnitts an.
Mögliche Werte: Siehe globe:DeminimisSimpleBasis_EnumType (GIR2901–GIR2902) unter Wertelisten für Aufzählungstypen

1..3 P

1..3 P

d

1O

n

1P

n

1P

n

1P

n

1P

1O

n

1P

n

1P

n

1P

n

0..1 O

1P

n

1P

n

1P

n

0..1 O

1P

n

0..1 O

xsd:date xsd:integer xsd:integer xsd:integer xsd:integer

xsd:integer xsd:integer xsd:integer xsd:integer

xsd:integer

xsd:integer

xsd:integer

1

6 globe:percentage

globe:ETRComputationType

Das wiederholbare Element „FinancialData“ enthält die für die Anwendung des Deminimis-Ausschlusses relevanten Datenpunkte und besteht aus den Elementen „Year“, „Revenue“, „GloBERevenue“, „NetGlobeIncome“ und „FANIL“.

Finanzdaten
Jahr Einnahmen GloBE-Umsatzerlöse Netto-GloBE-Einkommen

Dieses Element kann maximal viermal wiederholt werden, um alle drei Berichtsjahre zu erfassen: das Berichtsgeschäftsjahr, das erste vorangegangene Geschäftsjahr (falls zutreffend) und das zweite vorangegangene Geschäftsjahr (falls zutreffend) sowie den Durchschnitt der drei Jahre. Das Element „Year“ gibt das Jahr an, für das sich die übrigen Datenpunkte beziehen, d. h. das Berichtsgeschäftsjahr, das erste vorangegangene Geschäftsjahr (falls zutreffend) und das zweite vorangegangene Geschäftsjahr (falls zutreffend). Gegebenenfalls wird der Durchschnitt der drei Geschäftsjahre berechnet, indem die entsprechenden Umsatz- und Gewinn- (oder Verlust-)Berechnungen proportional zum Zeitraum des vorangegangenen Geschäftsjahres innerhalb eines Kalenderjahres angepasst werden. Das Element „Revenue“ gibt die Summe der Einnahmen der im Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder von Joint Venture-Gruppen vor etwaigen Anpassungen gemäß Kapitel 3 an. Das Element „GlobeRevenue“ gibt die Summe des GloBE-Umsatzerlöses der in dem Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder von Joint Venture-Gruppen an. Das Element „NetGlobeIncome“ gibt die Summe des GloBE-Gewinns oder -Verlusts von Geschäftseinheiten oder Mitgliedern von JV-Gruppen mit Sitz in dem Steuerhoheitsgebiet an.

Das Element „FANIL“ gibt den aggregierten FANIL der in dem Steuerhoheitsgebiet

FANIL

ansässigen Geschäftseinheiten oder Mitgliedern von JV-Gruppen an.

Das Element „Average“ enthält die Datenpunkte, die für die Anwendung des de-

minimis-Ausschlusses relevant sind, und setzt sich aus den Elementen Revenue,

GLOBE Revenue, Net Globe Income und FANIL zusammen. Dieses Element und

seine Unterelemente spiegeln die Durchschnittsbeträge der (bis zu) drei relevanten

Durchschnitt

Geschäftsjahre wider.

Das Element „Revenue“ gibt den durchschnittlichen Umsatz der im jeweiligen

Steuerhoheitsgebiet ansässigen Geschäftsseinheiten oder Mitglieder von Joint

Ertrag

Venture-Gruppen vor etwaigen Anpassungen gemäß Kapitel 3 an.

Das Element „GlobeRevenue“ gibt den Durchschnitt des GloBE-Umsatzeserlöses

der in dem Steuerhoheitsgebiet ansässigen Mitgliedsunternehmen oder Mitglieder

GloBE-Umsatzerlöse

von Joint Venture-Gruppen an.

Das Element „NetGlobeIncome“ gibt den Durchschnitt des GloBE-Gewinns oder -

Verlusts der in dem Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder

Netto-GloBE-Einkommen

Mitglieder von Joint Venture-Gruppen an.

Das Element „FANIL“ gibt den durchschnittlichen FANIL-Gesamtwert der in dem

Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder von Joint

FANIL

Venture-Gruppen an.

Das Element „Transitional CbCR Safe Harbour“ spiegelt die Anwendung des

Übergangs CbCR Safe-Harbour „Transitional CbCR Safe Harbour“ wider.

Das Element „Revenue“ gibt den Gesamtumsatz des jeweiligen Steuerhoheitsgebiets

an, wie er im CbC-Bericht des multinationalen Unternehmens (oder im qualifizierten

Jahresabschluss für Mitglieder von Joint Ventures) für das Berichtsgeschäftsjahr

ausgewiesen wird. Dieses Element muss nur ausgefüllt werden, wenn der De-

Gesamtumsatz

minimis-Test gilt.

Das Element „Gewinn“ gibt den Gewinn (Verlust) vor Einkommensteuer für das

Steuerhoheitsgebiet an, wie er im anerkannten CbC-Bericht der MNE-Gruppe (oder

in den qualifizierten Konzernabschluss für Mitglieder von JV-Gruppen) für das

Berichtsgeschäftsjahr und in Übereinstimmung mit den im Dokument „Safe Harbours

Gewinn

and Penalty Relief“ dargelegten Methoden ausgewiesen wird.

Einkommensteuer UTPR Safe-Harbour
Körperschaftssteuersatz

Das Element „IncomeTax“ gibt die vereinfachten erfassten Steuern der relevanten Geschäftseinheiten oder Mitgliedern von JV-Gruppen gemäß der Definition im Dokument „Safe Harbours and PenaltyRelief“ für das Berichtsgeschäftsjahr an. Dieses Element muss nur ausgefüllt werden, wenn der vereinfachte ETR-Test gilt. Das UTPRSafeHarbour-Element spiegelt die Anwendung des vorübergehenden UTPR Safe Harbours wider. Das Element „CITRate“ spiegelt den Körperschaftsteuersatz des Steuerhoheitsgebiets der obersten Muttergesellschaft gemäß dem vereinbarten SafeHarbour wider.

ETR-Berechnung

Das Element „ETR-Berechnung“ spiegelt die GloBE-Berechnungen sowohl auf Ebene des Steuerhoheitsgebiet als auch auf Ebene der Einheit wider. Es besteht aus den Elementen „CEComputation“, „OverallComputation“ und „Non-materialCE“.

Seite 16 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:CEComputation
globe:AdjustedFANIL globe:Total globe:FANIL globe:Adjustment
globe:MainEntityPEandFTE

globe:Basis globe:OtherTIN

globe:ResCountryCode globe:Additions globe:Reductions globe:CrossBorderAdjustments
globe:Basis
globe:OtherTIN

globe:ResCountryCode globe:Additions globe:Reductions globe:UPEAdjustments

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

0..n O

1P

1P

n

1P

n

0..1 O

0..1 O

1P

en

1P

an

1P

en

1P

n

1P

n

0..1 O

1P

en

1P

an

1P

en

1P

n

1P

n

0..1 O

xsd:integer xsd:integer

CE-Berechnung
Angepasstes FANIL Betrag FANIL Anpassung

Das wiederholbare Element „CE-Computation“ spiegelt die GloBE-Berechnungen auf Einheitsebene wider. Sofern der vereinfachte Übergangsrahmen für die Berichterstattung nach Steuerhoheitsgebiet angewendet wurde, ist dieser Abschnitt gemäß Hinweis 3.2.4.a.1 auszufüllen. Er umfasst die Elemente „AdjustedFANIL“, „NetGloBEIncome“, „AdjustedIncomeTax“, „AdjustedCoveredTax“, „TIN“, „Elections“ und „OtherFAS“. Das Element „AdjustedFANIL“ spiegelt die Anpassungen wider, die am FANIL des CE oder Mitglieds der JV-Gruppe vor der Berechnung des GloBE-Gewinns erforderlich sind, nämlich die grenzüberschreitende Aufteilung von Gewinnen oder Verlusten zwischen einem Stammhaus und einer PE und von einem FTE sowie grenzüberschreitende Anpassungen. Das Element „Total“ spiegelt den angepassten FANIL-Betrag wider. Das Element „FANIL“ gibt an, dass es sich um den FANIL des CE oder Mitglieds der JV-Gruppe vor den entsprechenden Anpassungen handelt. Das Element „Adjustment“ besteht aus den Elementen „MainEntityPEandFTE“, „CrossBorderAdjustments“ und „UPEAdjustments“.

Das Element „MainEntityPEandFTE“ gibt die grenzüberschreitende Aufteilung von

Grenzüberschreitende Aufteilung Gewinnen oder Verlusten zwischen einem Stammhaus und einer Betriebsstätte

von Gewinnen oder Verlusten sowie von einer transparenten Einheit (engl. Flow-through Entity - FTE) an.

Das Element „Basis“ gibt die Grundlage für die Anpassung an, nämlich Artikel 3.4,

Artikel 3.5.3, Artikel 3.5.1(a) und/oder Artikel 3.5.1(b). Für jede Anpassungsart ist die

jeweilige Erhöhung oder Reduzierung des FANIL der Geschäftseinheit oder des

Mitglieds der JV-Gruppe anzugeben. Bei mehreren Anpassungen ist für jede Option

eine Zeile anzugeben, und die relevanten Optionen sind in der folgenden Reihenfolge

anzugeben:

siehe globe:MainEntityPEandFTEBasis_EnumType (GIR1701–GIR1704) unter

globe:MainEntityPEandFTEBasis_EnumType Basis

Wertelisten für Aufzählungstypen

Das Element „OtherTIN“ gibt die TIN der anderen Geschäftseinheit oder Mitglieds der

JV-Gruppe an, das an der identifizierten Anpassung beteiligt ist. Ist keine TIN

verfügbar, muss die berichtspflichtige Geschäftseinheit ein funktionales Äquivalent

angeben, z. B. eine Handelsregisternummer.

1 200 globe:TIN_Type

Andere TIN

Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Das Element „ResCountryCode“ gibt das Steuerhoheitsgebiet (in Form eines zweistelligen alphabetischen Ländercodes gemäß ISO 3166-1 Alpha 2) der anderen Geschäftseinheit oder des Mitglieds der JV-Gruppe an. Die berichtspflichtige Geschäftseinheit muss für staatenlose Geschäftseinheiten den Status „staatenlos“ angeben.

2

2 iso:CountryCode_Type

xsd:integer

xsd:integer

Ansässigkeitsstaat
Ergänzungen
Kürzungen
Grenzüberschreitende Anpassungen

Bei Meldungen für staatenlose Geschäftseinheiten ist der Code „X5“ zu verwenden. Das Element „Additions“ gibt den Betrag einer Anpassung an, die das GloBEEinkommen des oben genannten CE oder Mitglieds der JV-Gruppe erhöht. Der Betrag „Reductions“ gibt den Betrag einer Anpassung an, die das GloBEEinkommen des oben genannten CE oder Mitglieds der JV-Gruppe verringert. Das Element „CrossBorderAdjustments“ spiegelt die für FANIL erforderlichen grenzüberschreitenden Anpassungen wider und besteht aus den folgenden Elementen. Die berichtspflichtige Geschäftseinheit muss angeben, ob sich die Anpassung auf Artikel 3.2.3 oder 3.2.7 bezieht.

globe:CrossBorderAdjustments_EnumType Basis

1 200 globe:TIN_Type

Andere TIN

Mögliche Werte: Siehe globe:CrossBorderAdjustments_EnumType (GIR1801–GIR1802) unter Wertelisten für Aufzählungstypen Das Element „Andere TIN“ gibt die TIN des anderen CE oder Mitglieds der JVGruppe an, das an der identifizierten Anpassung beteiligt ist. Wenn keine TIN verfügbar ist, muss die einreichende konstituierende Einheit ein funktionales Äquivalent angeben, z. B. einen Geschäfts-/Firmenregistrierungscode/eine Firmenregistrierungsnummer. Der TIN-Typ muss gemäß dem Abschnitt TIN-Typ ausgefüllt werden.

Das Element „ResCountryCode“ gibt das Steuerhoheitsgebiet (in Form eines zweistelligen alphabetischen Ländercodes gemäß ISO 3166-1 Alpha 2) der anderen an der Anpassung beteiligten Geschäftseinheit oder des Mitglieds der JV-Gruppe an.

iso:CountryCode_Type xsd:integer xsd:integer

Ansässigkeitsstaat Ergänzungen Kürzungen UPE Anpassungen

Die berichtspflichtige Geschäftseinheit muss für staatenlose Geschäftseinheiten den Status „Staatenlos“ angeben. Bei der Meldung staatenloser Geschäftseinheiten ist der Code „X5“ zu verwenden. Das Element „Additions“ gibt den Betrag einer Anpassung an, die das GloBEEinkommen des oben genannten CE oder Mitglieds der JV-Gruppe erhöht. Das Element „Reductions“ gibt den Betrag einer Anpassung an, die das GloBEEinkommen des oben genannten CE oder Mitglieds der JV-Gruppe verringert. Dieses wiederholbare Element „UPEAdjustments“ spiegelt Anpassungen des GloBEEinkommens der UPE gemäß Artikel 7.1 oder Artikel 7.2 wider.

Seite 17 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:Basis globe:Reductions
globe:Amount globe:Exception
globe:IdentificationOfOwners globe:OwnershipPercentage globe:IndOwners
globe:NumOfOwners
globe:ResCountryCode globe:TaxRate
globe:EntityOwner

globe:NetGlobeIncome globe:Total
globe:Adjustments

globe:TIN globe:ResCountryCode globe:TaxRate
globe:ExTypeOfEntity

globe:Amount globe:AdjustmentItem

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1P

en

1P

n

1B

n

1B

b

1..n P

1P

n

1B

1P

n

0..1 O

en

0..1 O

n

1B

globe:UPEAdjustmentsBasis_EnumType xsd:integer xsd:integer xsd:boolean

1

6 globe:percentage

xsd:integer

2

2 iso:CountryCode_Type

1

6 globe:percentage

1P

an

1P

en

0..1 O

n

1 200 globe:TIN_Type

2

2 iso:CountryCode_Type

1

6 globe:percentage

0..1 O

en

1P

1P

n

0..n O

globe:ExTypeOfEntity_EnumType xsd:integer

1..2 P

n

1P

en

xsd:integer globe:AdjustmentItem_EnumType

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)
Das Element „Basis“ gibt die Grundlage für die Anpassung an, d. h. Artikel 7.1.1, Artikel 7.1.2, Artikel 7.2.1 oder Artikel 7.2.2, zusammen mit dem entsprechenden Buchstaben und der Nummer des Unterabsatzes.

Mögliche Werte:

Siehe globe:UPEAdjustmentsBasis_EnumType (GIR1901–GIR1910) unter

Basis

Wertelisten für Aufzählungstypen

Das Element „Reductions“ setzt sich aus den Elementen „Amount“ und „Exception“

Kürzungen

zusammen.

Das Element „Amount“ gibt den Betrag einer Anpassung an, die das GloBE-

Betrag

Einkommen des oben genannten CE oder Mitglieds der JV-Gruppe verringert.

Das Element „Exception“ weist darauf hin, dass eine Ausnahme von der Meldung

Ausnahme

über Kürzungen gilt.

Das wiederholbare Element „IdentificationOfOwners“ enthält identifizierende

Informationen zu den Inhabern von Eigentumsanteilen. Es besteht aus dem

Eigentümeridentifikation

Eigentumsanteil und entweder den Elementen „IndOwners“ oder „EntityOwner“.

Das Element „OwnershipPercentage“ gibt die Eigentumsanteile (in Prozent) an, die

Eigentumsanteil

jeder in 3.2.4.1.d.3 genannte Inhaber direkt an der UPE hält.

Eigentumsanteile von natürlichen Das Element „IndOwners“ spiegelt wider, dass die Eigentumsanteile von natürlichen

Personen

Personen gehalten werden.

Das Element „NumOfOwners“ identifiziert die natürlichen Personen in der

Gesamtheit. Die berichtspflichtige Geschäftseinheit muss die Inhaber von

Eigentumsanteilen (bzw. Dividendenempfänger) identifizieren, für die eine

Anzahl Eigentümer

Reduzierung des GloBE-Gewinns gilt.

Das Element „ResCountryCode“ gibt das Steuerhoheitsgebiet des Wohnsitzes des

einzelnen Eigentümers an (in Form eines zweistelligen alphabetischen Ländercodes

Ansässigkeitsstaat

basierend auf dem Standard ISO 3166-1 Alpha 2).

Steuersatz

Das Element „TaxRate“ gibt den Steuersatz des Eigentümers an.

Das Element "Entity Owner" erleichtert die Identifizierung der Einheitseigentümer und

setzt sich aus den Elementen "TIN" und "ResCountryCode", "Tax Rate" und

Einheitseigentümer

"ExTypeofEntity" zusammen.

Wenn Artikel 7.1 oder 7.2 gelten, muss die berichtspflichtige Geschäftseinheit „UPE“

melden. Wenn Artikel 7.1.4 gilt, gibt das TIN-Element die TIN der Betriebsstätten an,

auf die Artikel 7.1 zutrifft, oder, falls keine TIN verfügbar ist, ein funktionales

Äquivalent, wie z. B. eine Handelsregisternummer. Wenn Artikel 7.2.3 gilt, gibt die

TIN der Geschäftseinheiten an, auf die Artikel 7.2 zutrifft, oder, falls keine TIN

verfügbar ist, ein funktionales Äquivalent, wie z. B. eine Handelsregisternummer.

Wenn Artikel 7.1 oder 7.2 auf Mitglieder einer Joint Venture-Gruppe zutrifft, muss die

berichtspflichtige Geschäftseinheit die TIN der Mitglieder der Joint Venture-Gruppe

melden.

Steueridentifikationsnummer
Ansässigkeitsstaat Steuersatz

Falls keine TIN eingegeben wird, muss der Wert NOTIN angegeben werden. Der TINTyp ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen. Das Element „ResCountryCode“ gibt den Sitzstaat des Einheitseigentümers an (in Form eines zweistelligen alphabetischen Ländercodes auf Grundlage des Standards ISO 3166-1 Alpha 2). Das Element „TaxRate“ gibt den Steuersatz des Eigentümers an.
Das Element „ExTypeOfEntity“ gibt den Grund an, warum der Eigentümer der Einheit eine ausgeschlossene Eeinheit ist.

Typ der ausgeschlossenen Einheit
Netto-Welteinkommen Gesamt
Anpassung

Mögliche Werte: siehe globe:ExTypeOfEntity_EnumType (GIR2801 - GIR2805) unter Wertelisten für Aufzählungstypen
Das Element „NetGlobeIncome“ bietet eine Aufschlüsselung aller Anpassungen, die am FANIL jeder Geschäftseinheit oder jedes Mitglieds der JV-Gruppe vorgenommen wurden. Es besteht aus den Elementen „Total“, „Adjustments“ und „International Shipping Income“. Das Element „Total“ ist das GloBE Nettoeinkommen nach den entsprechenden Anpassungen. Das wiederholbare Element „Adjustments“ spiegelt die Anpassungen wider, die gemäß Artikel 3.2 am Nettogewinn oder -verlust der Finanzbuchhaltung vorgenommen wurden. Es besteht aus den Elementen „Amount“ und „Adjustment Item“.

Betrag

Das Element „Amount“ gibt den Betrag der Anpassung an. Für jede Anpassung müssen Zu- und Abschläge separat ausgewiesen werden, es sei denn, es wurde der vereinfachte Übergangsrahmen für die Berichterstattung nach Steuerhoheitsgebiet angewendet. In diesem Fall können alle Anpassungen netto gemeldet werden. Für einen Zuschlag ist ein positiver Betrag anzugeben, für einen Abschlag ein negativer Betrag. Dieses Element kann bis zu zweimal wiederholt werden.

Anpassungselement

Das Element Adjustment Item spiegelt den Typ der Anpassung wider, der aus der folgenden Liste ausgewählt werden kann: siehe globe:AdjustmentItem_EnumType (GIR2001 - GIR2026) unter Wertelisten für Aufzählungstypen

Seite 18 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:IntShippingIncome globe:InternationalShipIncome globe:Total
globe:Category globe:Revenue globe:Costs globe:QualifiedAncShipIncome globe:Total

globe:Category globe:Revenue globe:Costs globe:SubstanceExclusion globe:PayrollCosts
globe:TangibleAssets globe:CoveredTaxes

globe:AdjustedIncomeTax globe:Total globe:IncomeTax
globe:CrossAllocation

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

0..1 O

1P

1P

n

1P

en

1P

n

1P

n

1P

1P

n

xsd:integer
globe:IntShipCategory_EnumType xsd:integer xsd:integer xsd:integer

1P

en

1P

n

1P

n

1P

1P

n

1P

n

1P

n

globe:AncShipCategory_EnumType xsd:integer xsd:integer
xsd:integer
xsd:integer xsd:integer

1P

1P

n

1P

n

0..n O

xsd:integer xsd:integer

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Einkünfte aus internationalem Seeverkehr Berechnung Einkünfte aus internationalem Seeverkehr Gesamt
Kategorie

Das Element „IntShippingIncome“ spiegelt die Anwendung des Ausschlusses für Einkünfte aus dem internationalen Seeverkehr wider. Es besteht aus den Elementen „International Shipping Income“, „QualifiedAncShipIncome“, „Substance Exclusion“ und „Covered Taxes“. Die Informationen sind unabhängig davon zu melden, ob die Wahl des vereinfachten Übergangsrahmens für die Berichterstattung nach Steuerhoheitsgebiet getroffen wurde. Das Element „InternationalShipIncome“ spiegelt die Berechnung der Einkünfte aus dem internationalen Seeverkehr wider. Es besteht aus den Elementen „Total“, „Category“, „Revenue“ und „Costs“. Das Element „Total“ spiegelt die gesamten Einkünfte aus dem internationalen Seeverkehr der Geschäftseinheit wider. Das wiederholbare Element „Category“ gibt die in Artikel 3.3.2 Unterabsätze (a) bis (f) genannten relevanten Tätigkeiten an, für die Einkünfte aus dem internationalen Seeverkehr erzielt wurden (mehrere Optionen sind möglich). Diese Optionen sind wie folgt: Siehe globe:IntShipCategory_EnumType (GIR2101–GIR2106) unter Wertelisten für Aufzählungstypen

Einnahmen

Die Elemente „Revenue“ und „Costs“ geben die Gesamteinnahmen und -kosten aller in Artikel 3.3.2 Unterabsätze (a) bis (f) genannten relevanten Aktivitäten an.

Kosten
Anerkannte Einkünfte aus Neben- und Hilfsgeschäften
Gesamt

Die Elemente „Revenue“ und „Costs“ geben die Gesamteinnahmen und -kosten aller in Artikel 3.3.2 Unterabsätze (a) bis (f) genannten relevanten Aktivitäten an. Das Element „QualifiedAncShipIncome“ spiegelt die Berechnung der Einkünfte aus anerkannten Neben- und Hilftsgeschäfte aus dem Seeverkehr wider und besteht aus den Elementen „Total“, „Category“, „Revenue“ und „Costs“. Das Element „Total“ gibt die gesamten Einkünfte von anerkannten Neben- und Hilfsgeschäften aus dem internationalen Seeverkehr der Geschäftseinheit an.
Das Element „Category“ gibt die in Artikel 3.3.3 Unterabsätze (a) bis (e) genannten relevanten Tätigkeiten an, für die Einkünfte aus anerkannten Neben- und Hilfsgeschäften aus dem Seeverkehr erzielt wurden (mehrere Optionen sind möglich).

Kategorie Einnahmen Kosten

Diese Optionen sind wie folgt: Siehe globe:AncShipCategory_EnumType (GIR2201–GIR2205) unter Wertelisten für Aufzählungstypen Die Elemente „Revenue“ und „Costs“ spiegeln die Gesamteinnahmen und die Kosten wider, die aus jeder der in Artikel 3.3.3 Unterabsätze (a) bis (e) genannten relevanten Aktivitäten erzielt werden. Die Elemente „Revenue“ und „Costs“ spiegeln die Gesamteinnahmen und die Kosten wider, die aus jeder der in Artikel 3.3.3 Unterabsätze (a) bis (e) genannten relevanten Aktivitäten erzielt werden.

Substanzbasierter Freibetrag Lohnaufwand
Materielle Vermögenswerte Erfasste Steuern
Anpassung erfasster Steuern Gesamt Erfasste Steuern Querzurechnung

Das Element „Substance Exclusion“ gibt die Auswirkung auf den substanzbasierten Freibetrag an. Es besteht aus den Elementen „PayRollCosts“ und „TangibleAssets“. Das Element „PayrollCosts“ gibt den Lohnaufwand an, der den Einkünften aus internationalen Seeverkehr oder Einkünften aus anerkannten Neben- und Hilfsgeschäften des internationalen Seeverkehrs zuzurechnen sind. Das Element „Tangible Assets“ gibt den Buchwert der materiellen Vermögenswerte an, die zur Erzielung von Einkünften aus dem internationalen Seeverkehr oder anerkannten Neben- und Hilfsgeschäften aus dem internationalen Seeverkehr verwendet werden (mit Ausnahme von Einkünften, die die Obergrenze für Einkünfte aus anerkannten Neben- und Hilfsgeschäften aus dem internationalen Seeverkehr überschreiten). Das Element „Covered Taxes“ gibt die erfassten Steuern an, die mit den ausgeschlossenen Einkünften aus dem internationalen Seeverkehr oder anerkannten Neben- und Hilfsgeschäften des internationalen Seeverkehrs in Zusammenhang stehen.
Das Element „Adjusted Income Tax“ enthält Informationen zur Querzurechnung erfasster Steuern von einer Geschäftseinheit (oder einem Mitglied einer Joint VentureGruppe) auf eine andere Geschäftseinheit (oder ein Mitglied einer Joint VentureGruppe). Es besteht aus dem Element „Total“ (das den laufenden Steueraufwand der Geschäftseinheit in Bezug auf erfasste Steuern nach den Zurechnungen widerspiegelt) sowie den Elementen „Income Tax" und "Cross Allocation“. Diese Informationen sind unabhängig davon zu melden, ob das vereinfachte Übergangsrahmenwerk für die Berichterstattung nach Steuerhoheitsgebiet angewendet wird. Das Element „Total“ gibt den laufenden Steueraufwand in Bezug auf erfasste Steuern nach der Querzurechnung an. Das Element „Income Tax“ gibt die erfassten Steuern der Geschäftseinheit (oder Mitglieds der JV-Gruppe) vor den Anpassungen an. Das wiederholbare Element „Cross Allocation“ spiegelt alle relevanten Querzurechnungs-Anpassungen wider. Es besteht aus den Elementen „Basis“, „Other TIN“, „ResCountryCode“, „Additions“ und „Reductions“.

Seite 19 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:Basis
globe:OtherTIN
globe:ResCountryCode globe:Additions globe:Reductions globe:AdjustedCoveredTax globe:Total globe:Adjustments globe:Amount globe:AdjustmentItem globe:DeferTaxAdjustAmt globe:Total
globe:DeferTaxExpense globe:Adjustment

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1..n P

en

globe:AdjustedBasis_EnumType

1P

an

1 200 globe:TIN_Type

1P

en

0..1 O

n

0..1 O

n

1P

1P

n

0..n O

1..2 P

n

1P

en

1P

1P

n

iso:countryCode_Type xsd:integer xsd:integer
xsd:integer
xsd:integer globe:CurrentAdjustedTax_EnumType xsd:integer

1P

n

0..n O

xsd:integer

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das wiederholbare Element „Basis“ identifiziert die relevanten Unterabsätze von Artikel 4.3.2, 4.3.3 oder 4.3.4, die auf der Grundlage der folgenden Optionen gelten: Siehe globe:AdjustedBasis_EnumType (GIR2301 - GIR2309) in Wertelisten für Aufzählungstypen

Basis
Andere Steueridentifikationsnummer

Wenn Artikel 4.3.2.c oder Artikel 4.3.2.d Anwendung findet, füllt die berichtspflichtige Geschäftseinheit für die Zwecke der Spalten 3.2.4.2.b.6 und 3.2.4.2.b.7 eine erste Zeile mit dem Betrag vor der Anpassung gemäß Art. 4.3.3 (unter Angabe des entsprechenden Unterabsatzes von Art. 4.3.2 in Spalte 3.2.4.2.b.3) und eine zweite Zeile mit dem Betrag nach der Anpassung gemäß Art. 4.3.3 (unter Angabe des entsprechenden Unterabsatzes von Art. 4.3.3 in Spalte 3.2.4.2.b.3 sowie der entsprechende Unterabsatz von Art. 4.3.2). Das Element „Other TIN“ gibt die Steueridentifikationsnummer der anderen Geschäftseinheit (oder des Mitglieds der JV-Gruppe) oder, falls keine Steueridentifikationsnummer verfügbar ist, ein funktionales Äquivalent, wie z. B. eine Geschäfts-/Firmenregistrierungsnummer, an.
Der TIN Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Für die Zurechnung der erfassten Steuer von einer Geschäftseinheit (oder einem Mitglied der JV-Gruppe) an eine andere Geschäftseinheit (oder ein Mitglied der JVGruppe) gibt das Element ResCountryCode das Steuerhoheitsgebiet (in Form eines zweistelligen alphabetischen Ländercodes auf der Grundlage des ISO 3166-1 Alpha 2-Standards) der anderen Geschäftseinheit (oder des Mitglieds der JV-Gruppe) an.

Ansässigkeitsstaat Hinzurechnungen Kürzungen Angepasste erfasste Steuern Gesamt Anpassungen
Betrag Anpassungselement Anpassung latenter Steueraufwand Gesamtbetrag der angepassten latenten Steuern
Latenter Steueraufwand Anpassungselement

Handelt es sich bei der anderen Geschäftseinheit um eine staatenlose Geschäftseinheit, so meldet die berichtspflichtige Geschäftseinheit „stateless“. Bei der Meldung in Bezug auf staatenlose Geschäftseinheiten ist der Code „X5“ zu verwenden. Das Element „Additions“ gibt die Hinzurechnungen zu den erfassten Steuern der Geschäftseinheit (oder des Mitglieds der JV-Gruppe) an. Die Querzurechnung der Steuern umfasst sowohl den laufenden Steueraufwand als auch den latenten Steueraufwand. Das Element „Reductions“ gibt die Kürzungen der erfassten Steuern der Geschäftseinheit (oder des Mitglieds der JV-Gruppe) an. Die Querzurechnung der Steuern umfasst sowohl den laufenden Steueraufwand als auch den latenten Steueraufwand. Das Element „Adjusted Covered Tax“ gibt die Berechnung der angepassten erfassten Steuern für die Geschäftseinheit oder das Mitglied einer JV-Gruppe an. Es setzt sich aus den Elementen „Total“, „Adjustments“ und „DeferTaxAdjustAmt“ zusammen. Das Element „Total“ gibt die angepassten erfassten Steuern des Geschäftseinheit oder des Mitglieds einer JV-Gruppe an. Bei Investmenteinheiten gibt das Element „Total“ die angepassten erfassten Steuern der Investmenteinheit gemäß Artikel 7.4.3 an. Das wiederholbare Element „Adjustments“ spiegelt die Anpassungen des laufenden Steueraufwands der Geschäftseinheit oder des Mitglieds der JV-Gruppe in der Rechnungslegung wider (nach Zurechnungen in Artikel 4.3). Es besteht aus den Elementen „Amount“ und „Adjustment Item“. Das Element „Amount“ gibt den Betrag jeder Anpassung des laufenden Steueraufwands an. Hinzurechnungen und Kürzungen für jede der Anpassungen sind getrennt anzugeben. Für eine Hinzurechnungsanpassung ist ein positiver Betrag und für eine Kürzung ein negativer Betrag anzugeben. Das Element kann bis zu zwei Mal wiederholt werden. Das Element „Adjustment Item“ gibt die Art der laufenden Steueranpassung wider, die aus der folgenden Liste auszuwählen ist: siehe globe:CurrentAdjustedTax_EnumType siehe (GIR2401 - GIR2417) in Wertelisten für Aufzählungstypen Das Element „DeferTaxAdjustAmt“ spiegelt die Anpassungen des latenten Steueraufwands wider. Es besteht aus den Elementen „Amount“ und „Adjustment Item“. Das Element „Total“ gibt den Gesamtbetrag der angepassten latenten Steuern für die Geschäftseinheit (oder das Mitglied der JV-Gruppe) an.
Das Element „DeferTaxExpense“ gibt den Betrag des latenten Steueraufwands für GloBE-Zwecke für die Geschäftseinheit (oder ein Mitglied der JV-Gruppe) vor allen Neuberechnungen und Anpassungen an. Falls der Buchwert eines Vermögensgegenstandes oder einer Verbindlichkeit für Rechnungslegungs- und GloBE-Zwecke voneinander abweicht, muss der Anteil des latenten Steueraufwands auf der Grundlage des GloBE-Buchwerts gemäß den entsprechenden Verwaltungsanweisungen berechnet werden. Wird der latente Steueraufwand zu Lasten des Kontos für latenten Steueraufwand berücksichtigt, ist der Betrag als positive Zahl auszuweisen. Wird der latente Steueraufwand als Gutschrift auf dem Konto für latenten Steueraufwand berücksichtigt, so ist der Betrag als negative Zahl auszuweisen. Das Element „Adjustment“ enthält die Elemente „Amount“, „Adjustment Item“, „Recast“, „Higher“ und „Lower“.

Seite 20 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TIN

globe:Amount
globe:AdjustmentItem globe:Recast
globe:Higher globe:Lower

globe:Elections
globe:Art1.5.3 globe:Status globe:ElectionYear

globe:RevocationYear
globe:SimplCalculations globe:Art3.2.1
globe:Art3.2.1b globe:Status globe:ElectionYear

globe:RevocationYear
globe:Art3.2.1c globe:Status globe:ElectionYear

globe:RevocationYear

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

1..2 P

n

1P

en

0..1 O

0..1 O

n

0..1 O

n

1P

an

xsd:integer globe:DeferredAdjustedTax_EnumType
xsd:integer xsd:integer 1 200 globe:TIN_Type

0..1 O

0..1 O

1P

b

1P

d

1

1 xsd:boolean

xsd:date

0..1 O

d

0..1 O

b

0..1 O

b

0..1 O

1P

b

1P

d

xsd:date

1

1 xsd:boolean

1

1 xsd:boolean

1

1 xsd:boolean

xsd:date

0..1 O

d

0..1 O

1P

b

1P

d

xsd:date

1

1 xsd:boolean

xsd:date

0..1 O

d

xsd:date

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das Element „Amount“ gibt den Betrag jeder Anpassung des latenten

Steueraufwands vor jeder Neuberechnung an. Hinzurechnungen (d. h. Anpassungen,

die zu einer Erhöhung des Gesamtbetrags der angepassten latenten Steuern führen)

und Kürzungen (d. h. Anpassungen, die zu einer Kürzung des Gesamtbetrags der

angepassten latenten Steuern führen) sind für jede der Anpassungen getrennt

anzugeben. Für eine Hinzurechnungsanpassung ist ein positiver Betrag und für eine

Betrag der angepassten latenten Kürzung ein negativer Betrag einzutragen. Das Element kann bis zu zwei Mal

Steuern

wiederholt werden.

Das Element „Adjustment Item“ gibt die Art der Anpassung der latenten Steuern an,

die aus der folgenden Liste zu wählen ist:

Anpassungsart der latenten

Siehe globe:DeferredAdjustedTax_EnumType (GIR2501 - GIR2516) unter

Steuern

Wertelisten für Aufzählungstypen

Das Element „Neuberechnung“ gibt den Betrag des latenten Steueraufwands an, der

mit dem Mindeststeuersatz neu berechnet wurde. Sie werden entweder den höheren

Neuberechnung

und/oder den niedrigeren Satz anwenden.

Das Element „Higher“ zeigt an, dass sich die Neuberechnung auf den latenten

Steueraufwand bezieht, der zu einem höheren Steuersatz als dem Mindeststeuersatz

Höher

erfasst wurde.

Das Element „Lower“ zeigt an, dass es sich bei der Neuberechnung um eine

Erhöhung des latenten Steueranspruchs zu einem niedrigeren Steuersatz als dem

Niedriger

Mindeststeuersatz handelt.

Steueridentifikationsnummer Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Das Element „Elections“ enthält Informationen zu den Wahlrechten, die für eine

einzelne Geschäftseinheit (oder ein Mitglied einer JV-Gruppe) gelten. Es besteht aus

mehreren Elementen, die verschiedene Wahlen gemäß den GloBE-Regeln

widerspiegeln. Dieses Element und jedes Unterelement unter dem übergeordneten

Wahlrechte

Element sind optional.

Das Element „Art. 1.5.3“ kennzeichnet die Ausübung des Wahlrechts gemäß Artikel

1.5.3, wobei die Einheit nicht als ausgeschlossene Einheit behandelt wird. Da es sich

um eine fünfjährige Wahl handelt, besteht sie aus den Elementen „Status“, „Election

Artikel 1.5.3

Year“ und „Revocation Year“.

Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“

oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Das Element „SimplCalculations“ identifiziert die Anwendung des Wahlrechts der

Vereinfachte Berechnungen bei vereinfachten Berechnungen bei unwesentlichen Geschäftseinheiten (engl. non-

unwesentlichen

material Constituent Entities - NMCEs) (Safe Harbour für vereinfachte Berechnungen

Geschäftseinheiten

- engl. Simplified Calculations Safe Harbour).

Das Element „Art3.2.1“ identifiziert die Ausübung des Wahlrechts des

Artikel 3.2.1

Schuldenerlasses.

Das Element „Art3.2.1b“ identifiziert die Ausübung des Wahlrechts, alle Dividenden in

Bezug auf Portfolio-Anteile einzubeziehen. Da es sich um eine fünfjährige Wahl

handelt, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation

Artikel 3.2.1b

Year“.

Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“

oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Das Element „Art.3.2.1c“ identifiziert die Ausübung des Wahlrechts,

Wechselkursgewinne oder -verluste aus Hedging-Geschäften als ausgenommene

Eigenkapitalgewinne oder -verluste zu behandeln. Da es sich um eine fünfjährige

Wahl handelt, besteht sie aus den Elementen „Status“, „Election Year“ und

Artikel 3.2.1c

„Revocation Year“.

Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“

oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Seite 21 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:Art6.3.4 globe:FYTriggerEvent

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B Format Min Max Datentyp

0..n O

1P

d

xsd:date

globe:Inclusion globe:Art6.3.4.c.i
globe:Art6.3.4.c.ii globe:AggregatedReporting
globe:TaxConsolGroupTIN
globe:EntityTIN globe:Art4.4.7
globe:Status globe:ElectionYear
globe:RevocationYear globe:Art4.5.6
globe:Status globe:ElectionYear
globe:RevocationYear globe:Art7.5
globe:Status globe:ElectionYear

1P

1B

b

1

1 xsd:boolean

1B

b

0..1 O

1P

an

1

1 xsd:boolean

1 200 globe:TIN_Type

1..n P

an

0..1 O

1P

b

1P

d

1 200 globe:TIN_Type

1

1 xsd:boolean

xsd:date

0..1 O

d

0..1 O

1P

b

1P

d

xsd:date

1

1 xsd:boolean

xsd:date

0..1 O

d

0..1 O

1P

b

1P

d

xsd:date

1

1 xsd:boolean

xsd:date

Seite 22 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Artikel 6.3.4 Auslöseereignis für das Geschäftsjahr

Wertemenge / Erklärung (deut.)
Das wiederholbare Element „Art6.3.4“ identifiziert die Ausübung des Wahlrechts zum beizulegenden Zeitwert gemäß Artikel 6.3.4. Es setzt sich aus den Elementen „FYTriggeringEvent“ und „Inclusion“ zusammen. Das Element „FYTriggerEvent“ gibt das Geschäftsjahr des Ereignisses an, das die Steueranpassung ausgelöst hat (d. h. das auslösende Ereignis). Das Element „Inclusion“ ermöglicht die Auswahl von Artikel 6.3.4(c)(i) oder (ii), d.h. Einbeziehung in das Geschäftsjahr des auslösenden Ereignisses bzw. Einbeziehung über fünf Jahre.

(i) ist zu melden, wenn der Nettobetrag der gemäß Artikel 6.3.4 (a) ermittelten Gesamtbeträge in die Berechnung des GloBE-Gewinns oder -Verlusts in dem Geschäftsjahr einbezogen wird, in dem das auslösende Ereignis eintritt.

Einbeziehung

(ii) ist zu melden, wenn ein Betrag, der dem Nettogesamtbetrag der Beträge geteilt durch fünf entspricht, in die Berechnung des GloBE-Gewinns oder -Verlusts in dem Geschäftsjahr, in dem das auslösende Ereignis eintritt, und in jedem der vier unmittelbar darauf folgenden Geschäftsjahre einbezogen wird.

Artikel 6.3.4.c.i

Art6.3.4.c.i ist zu melden, wenn der Nettobetrag der gemäß Artikel 6.3.4 (a) ermittelten Gesamtbeträge in die Berechnung des GloBE-Gewinns oder -Verlusts in dem Geschäftsjahr einbezogen wird, in dem das auslösende Ereignis eintritt.

Art6.3.4.c.ii ist zu melden, wenn ein Betrag, der dem Nettogesamtbetrag der Beträge

geteilt durch fünf entspricht, in die Berechnung des GloBE-Gewinns oder -Verlusts in

dem Geschäftsjahr, in dem das auslösende Ereignis eintritt, und in jedem der vier

Artikel 6.3.4.c.ii

unmittelbar darauf folgenden Geschäftsjahre einbezogen wird.

Das Element „AggregatedReporting“ identifiziert die Auswahl für aggregierte Berichte

für steuerlich konsolidierte Gruppen. Es besteht aus den Elementen

Aggregierte Berichterstattung „TaxConsolGroupTin“ und „EntityTIN“.

Das Element „TaxConsolGroupTIN“ gibt die Steueridentifikationsnummer (TIN) der

steuerlich konsolidierten Gruppe an, die für die Zwecke der erfassten Steuern in dem

Steueridentifikationsnummer der betreffenden Steuerhoheitsgebiet verwendet wird.

steuerlich konsolidierten Gruppe Der TIN Typ ist gemäß dem Komplexdatentyp globe:TIN_Type anzugeben.

Das wiederholbare Element „Entity TIN“ gibt die Steueridentifikationsnummern (TINs)

der Geschäftseinheiten oder der Mitglieder einer JV-Gruppe an, die in der steuerlich

konsolidierten Gruppe zusammengefasst sind, die für die Zwecke der erfassten

Steueridentifikationsnummer der Steuern im jeweiligen Steuerhoheitsgebiet verwendet wird.

Geschäftseinheiten

Der TIN Typ ist gemäß dem Komplexdatentyp globe:TIN_Type anzugeben.

Das Element „Art.4.4.7“ identifiziert die Ausübung des Fünfjahres-Wahlrecht für

„nicht geltend gemachte Abgrenzung“. Als Fünfjahreswahl besteht es aus den

Artikel 4.4.7

Elementen „Status“, „Election Year“ und „Revocation Year“.

Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“

oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Das Element „Art4.5.6“ identifiziert die Ausübung GloBE-Verlustwahlrechts. Da es

sich um eine Fünfjahreswahl handelt, besteht sie aus den Elementen „Status“,

Artikel 4.5.6

„Election Year“ und „Revocation Year“.

Das Statuselement ist ein Boolean-Element mit dem akzeptierten Eingabetyp True

oder False. Wenn True, müssen die Elemente ElectionYear und RevocationYear

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Artikel 7.5
Status Wahljahr

Das Element „Art.7.5“ identifiziert die Ausübung des Steuertransparenzwahlrechts bei Investmenteinheiten. Da es sich um eine Fünfjahreswahlmöglichkeit handelt, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“ oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:RevocationYear globe:CEOwnerTIN

globe:Art7.6 globe:Status globe:ElectionYear
globe:RevocationYear globe:ActualDeemedDist globe:LocalCreditableTaxGross
globe:ShareOfUndistNeteGlobeInc
globe:InvestmentEntityTIN

globe:OtherFAS globe:OverallComputation
globe:FANIL
globe:AdjustedFANIL globe:NetGlobeIncome
globe:Total

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O

d

xsd:date

1..n P

an

1 200 globe:TIN_Type

0..n O

1P

b

1P

d

1

1 xsd:boolean

xsd:date

0..1 O

d

1P

n

1P

n

xsd:date xsd:integer xsd:integer

1P

n

1

6 globe:percentage

1P

an

1 200 globe:TIN_Type

0..1 O

an

0..1 O

1P

n

1 200 stf:stringMin1Max200_Type xsd:integer

1P

n

1P

1P

n

xsd:integer xsd:integer

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung Widerrufsjahr

Wertemenge / Erklärung (deut.)
Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen wurde (sofern zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben.

Steueridentifkationsnummer

Das wiederholbare Element „CEOwnerTIN“ gibt die Steueridentifikationsnummern (TINs) der Geschäftseinheiten oder Mitglieder einer Joint Venture-Gruppe an, die in der steuerlich konsolidierten Gruppe zusammengefasst sind, die für Zwecke der erfassten Steuern in dem jeweiligen Steuerhoheitsgebiet verwendet wird. Es ist gemäß dem Komplexdatentyp globe:TIN_Type anzugeben.

Das Element „Art7.6“ identifiziert die Ausübung des Wahlrechts für steuerpflichtige

Ausschüttungen an. Da es sich um eine fünfjährige Wahl handelt, besteht es aus den

Elementen „Status“, „Election Year“ und „Revocation Year“. Es setzt sich außerdem

aus den Elementen „ActualDeemedDist“, „LocalCreditableTaxGross“ und

„ShareofUndistNetGloBEInc“ zusammen (siehe Anmerkungen 3.2.4.5.1 bis 3.2.4.5.5

Artikel 7.6

des GIR).

Das Element „Status“ ist ein Boolean-Wert mit den zulässigen Eingabetypen „True“

oder „False“. Bei „True“ müssen die Elemente „ElectionYear“ und „RevocationYear“

Status

ausgefüllt werden.

Wahljahr

Das Element „Election Year“ gibt das Wahljahr für das Wahlrecht an.

Das Element „Revocation Year“ gibt das Jahr an, in dem das Wahlrecht widerrufen

wurde (sofern zutreffend).

Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das

Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen

Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre

Widerrufsjahr

angeben.

Das Element „ActualDeemedDist“ gibt die Höhe der tatsächlichen Ausschüttungen

Tatsächliche und fiktive

und fiktiven Ausschüttungen des GloBE-Gewinns der Investmenteinheit an, die der

Ausschüttungen

Eigentümer der Geschäftseinheit erhalten hat.

Das Element „LocalCreditableTaxGross“ gibt den von der Investmenteinheit im Inland

anrechenbaren Steueraufschlag, der auf die Steuerschuld des Eigentümers der

Im Inland anrechenbare

Geschäftseinheit angerechnet werden kann, die im Zusammenhang mit einer

Steueraufschlag

Ausschüttung aus der Investmenteinheit entsteht.

Das Element „ShareOfUndistNetGlobeInc“ gibt an, dass, wenn die Investmenteinheit

für das geprüfte Jahr ein nicht ausgeschütteten Netto-GloBE-Gewinn hat, die

berichtspflichtige Geschäftseinheit den proportionalen Anteil des Eigentümers der

Anteil des nicht ausgeschütteten Geschäftseinheit am nicht ausgeschütteten Netto-GloBE-Gewinn der

Netto-GloBE-Gewinns

Investmenteinheit für das geprüfte Jahr melden muss.

Das Element „TIN“ gibt die Steueridentifikationsnummer (TIN) der Investmenteinheit

oder des Eigentümers der Geschäftseinheit (oder des Mitglieds einer JV-Gruppe) an,

die einen Eigentumsanteil hält und für die das Wahlrecht gemäß Artikel 7.6 ausgeübt

Steueridentifikationsnummer der wird.

Investmenteinheit

Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Das Element „OtherFAS“ gibt den von der Geschäftseinheit (oder einem Mitglied einer JV-Gruppe) verwendeten Rechnungslegungsstandard an, wenn die Geschäftseinheit (oder das Mitglied einer JV-Gruppe) einen anderen Rechnungslegungsstandard als den für den Konzernabschluss der obersten Muttergesellschaft (UPE) (oder des JV) gemäß Artikel 3.1.3 (oder Artikel 6.4.1(a)) verwendeten verwendet.

Die berichtspflichtige Geschäftseinheit muss den anerkannten

Rechnungslegungsstandard oder den zugelassenen Rechnungslegungsstandard

Anderer

angeben, der für die Berechnung des Jahresüberschusses oder -fehlbetrags der

Rechnungslegungsstandard

Gesellschaft, des JV oder der JV-Tochtergesellschaft verwendet wird.

Das Element „Overall Computation“ spiegelt die GloBE-Berechnungen des

Steuerhoheitsgebiets wider und besteht aus Elementen von „Adjusted FANIL“ bis

Gesamtberechnung

„Top-up Tax“.

Das Element „FANIL“ enthält Informationen zum Gesamtbetrag des buchhalterischen

Nettogewinns oder -verlusts, der bei der Erstellung des Konzernabschlusses der

Finanzbuchhaltung Nettogewinn UPE für alle im Steuerhohetsgebiet ansässigen Geschäftseingebiet (oder Mitglieder

oder -verlust

der JV-Gruppe) ermittelt wurde.

Angepasste Finanzbuchhaltung Nettogewinn oder -verlust
Netto-GloBE-Gewinn Gesamtbetrag Netto-GloBEGewinn / -Verlust

Das Element „Adjusted FANIL“ enthält Informationen über den Gesamtbetrag des buchhalterischen Nettogewinns oder -verlusts, der für alle Geschäftseinheiten (oder Mitglieder der JV-Gruppe), die in dem Steuerhoheitsgebiet ansässig sind, bei der Erstellung des konsolidierten Konzernabschluss der UPE nach den Zurechnungen in Artikel 3.4 und 3.5 ermittelt wurde. Das Element „Netto-GloBE-Income“ gibt den Netto-GloBE-Gewinn bzw. den NettoGloBE-Verlust für das jeweilige Steuerhoheitsgebiet an.
Das Element „Total“ ist der Gesamtbetrag des Netto-GloBE-Gewinns oder -Verlusts.

Seite 23 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:Adjustments
globe:Amount
globe:AdjustmentItem
globe:IntShippingIncome globe:Total
globe:TotalIntShipIncome globe:FiftyPercentCap

globe:TotalQualifiedAncIncome globe:ExcessOfCap
globe:IncomeTaxExpense globe:ETRRate globe:TopUpTaxPercentage globe:AdjustedCoveredTax
globe:Total globe:AggregrateCurrentTax

globe:Adjustments

globe:Amount globe:AdjustmentItem

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Kardinalität P O B Format Min Max Datentyp

0..n O

1P

n

1P

en

0..1 O

1P

n

1P

n

1P

n

xsd:integer globe:AdjustmentItem_EnumType
xsd:integer xsd:integer xsd:integer

1P

n

0..1 O

n

1P

n

1P

n

1P

n

0..1 O

1P

n

1P

n

xsd:integer xsd:integer

xsd:integer

1

6 globe:percentage

1

6 globe:percentage

xsd:integer xsd:integer

0..n O

1P

n

1P

en

xsd:integer globe:FinalAdjustedTax_EnumType

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Anpassungen
Betrag
Anpassungenselement Obergrenze für Auschluss von Gewinnen aus Neben- und Hilfsgeschäften des internationalen Seeverkehrs Gesamt
Gesamteinkünfte aus dem internationalen Seeverkehr Fünfzig-Prozent-Obergrenze
Gesamteinkünfte aus Nebenund Hilfsgeschäften Überschreitung der Obergrenze
Gesamtbetrag Steueraufwand Effektiver Steuersatz

Das wiederholbare Element „Adjustments“ spiegelt die Anpassungen wider, die am Netto-Gewinn oder -Verlust der Finanzbuchhaltung gemäß Artikel 3.2 vorgenommen wurden. Es besteht aus den Elementen „Amount“ und „Adjustment Item“. Das Element „Amount“ gibt die Höhe der Anpassung an. Für jede Anpassung müssen Hinzurechnungen und Kürzungen separat angegeben werden. Für eine Hinzurechnungsanpassung ist ein positiver Betrag und für eine Kürzung ein negativer Betrag anzugeben. Das Element „Adjustment Item“ spiegelt die Art der Anpassung wider, die aus der folgenden Liste ausgewählt werden kann: Siehe globe:AdjustmentItem_EnumType (GIR2001-GIR2026) unter Wertelisten für Aufzählungstypen
Das optionale Element „IntShippingIncome“ gibt die Obergrenze des Steuerhoheitsgebiet für den Ausschluss von Einkünften aus anerkannten Neben- und Hilfsgeschäften aus dem internationalen Seeverkehr an. Das Element „Total“ spiegelt die gesamten Einkünfte aus dem internationalen Seeverkehr wider. Das Element „TotalIntShipIncome“ enthält Informationen über die gesamten Einkünfte aus dem internationalen Seeverkehr für die in Abschnitt 3.1.3 identifizierten und im Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder der JVGruppe der jeweiligen Untergruppe. Das Element „FiftyPercentCap“ gibt die Höhe der 50%igen Obergrenze an. Das Element „TotalQualifiedAncIncome“ enthält Informationen über die gesamten anerkannten Einkünfte aus Neben- und Hilfsgeschäften aus dem internationalen Seeverkehr für alle in Abschnitt 3.1.3 identifizierten und in dem Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder der JV-Gruppe der betreffenden Untergruppe. Das optionale Element „ExcessOfCap“ gibt die Überschreitung der Obergrenze an, die nach bestimmten Regeln zu melden ist. Das Element „IncomeTaxExpense“ enthält Informationen über den Gesamtbetrag des Steueraufwands für Einkünfte, der in den Jahresabschlüssen der in dem betreffenden Steuerhoheitsgebiet ansässigen Geschäftseinheiten (oder Mitglieder der JV-Gruppe) ausgewiesen wird. Das Element „ETRRate“ gibt den effektiven Steuersatz (engl. effective tax rate ETR) an.

Prozentsatz Ergänzungssteuer Angepasste gedeckte Steuern

Das Element „TopUpTaxPercentage“ gibt den Prozentsatz der Ergänzungssteuer an. Das Element „AdjustedCoveredTax“ gibt die angepassten erfassten Steuern aller in dem Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder von JVGruppen an.

Gesamtbetrag der angepassten erfassten Steuern
Gesamter laufender Steueraufwand

Das Element „total“ gibt den Gesamtbetrag der angepassten erfassten Steuern an. Das Element „AggregrateCurrentTax“ gibt den gesamten laufenden Steueraufwand in Bezug auf die erfassten Steuern nach den Zuweisungen in Artikel 4.3 (aller Geschäftseinheiten im Steuerhoheitsgebiet) an.

Anpassungen

Das Element „Adjustments“ gibt an, dass die berichtspflichtige Geschäftseinheit die Minderung der angepassten erfassten Steuern in Bezug auf den verbleibenden Saldo des Vortrags überschüssiger negativer Aufwendungen gemäß Artikel 5.2.1 oder einer Wahl gemäß Artikel 4.1.5 in Übereinstimmung mit den diesbezüglich vereinbarten Verwaltungsleitlinien melden muss. Die Minderung entspricht dem unter 3.2.1.2.b.3 gemeldeten Betrag, darf jedoch den Betrag der angepassten erfassten Steuern nicht übersteigen, der sich aus den anderen Anpassungen ergibt.

Das Element „Amount“ gibt den Betrag der gemäß Artikel 4.1.2(d) vorgenommenen Anpassung in Bezug auf eine anerkannte erstattungsfähige steuerliche Zulage oder eine marktfähige steuerliche Zulage an, die als Verringerung des laufenden Steueraufwands (oder anderer erfasster Steuern) in dem Jahresabschluss erfasst wird.

Betrag Korrekturposition

Die berichtspflichtige Geschäftseinheit meldet den Betrag der gemäß Artikel 4.1.3(b) vorgenommenen Anpassung in Bezug auf eine nicht anerkannte erstattungsfähige steuerliche Zulage, eine nicht marktfähige steuerliche Zulage oder eine sonstige steuerliche Zulage, die in dem Jahresabschluss als Ertrag und nicht als Minderung des laufenden Steueraufwands (oder anderer gedeckter Steuern) verbucht wird. Das Element "Adjustment Item" gibt die Art der aktuellen Steueranpassung wieder, die aus der folgenden Liste auszuwählen ist: siehe globe:FinalAdjustedTax_EnumType (GIR2701 - GIR2720) unter Wertelisten für Aufzählungstypen

Seite 24 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

globe:PostFillingAdjust globe:DeferTaxAsset
globe:Total globe:AmountAttributed
globe:Year globe:Amount globe:CoveredTaxRefund
globe:Total globe:AmountAttributed
globe:Year
globe:Amount globe:DeemedDistTax
globe:Total globe:Election
globe:Recapture globe:Year globe:StartAmount globe:DDTYear-0 globe:DDTYear-1 globe:DDTYear-2 globe:DDTYear-3 globe:TotalDDT

0..1 O 1P

1P

n

0..n O

1P

d

1P

n

1P

1P

n

0..n O

1P

d

1P

n

0O

1P

n

0..1 O

1..n P

1P

d

1P

n

1P

n

1P

n

1P

n

1P

n

1P

n

xsd:integer
xsd:date xsd:integer
xsd:integer
xsd:date
xsd:integer
xsd:integer
xsd:date xsd:integer xsd:integer xsd:integer xsd:integer xsd:integer xsd:integer

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das Element „PostFilingAdjust“ bezieht sich auf die nach Einreichung der Erklärung erfolgenden Anpassungen gemäß Artikel 4.6.1. Die in dieser Tabelle aufgeführten nach Einreichung der Erklärung erfolgende Anpassungen umfassen nicht die Anpassungen, die für ein anderes Geschäftsjahr als das Berichtsgeschäftsjahr in Übereinstimmung mit einem ETR-Anpassungsartikel vorgenommen wurden.

Nach Einreichung der Erklärung erfolgende Anpassungen

Die nach Einreichung der Erklärung erfolgenden Anpassungen im Zusammenhang mit Artikel 4.6.1 sind die Anpassungen, die zu einer wesentlichen Verringerung der erfassten Steuern für ein vorangegangenes Geschäftsjahr führen, und die Anpassungen, die zu einer unwesentlichen Verringerung führen, wenn keine Wahl gemäß 4.6.1 getroffen wird.

Latente Steueransprüche
Gesamt Stornierte latente Steueransprüche Jahr Betrag Erstattung erfasster Steuern

Das Element „DeferTaxAsset“ spiegelt den Betrag der latenten Steueransprüche wider, die für frühere Geschäftsjahre als storniert behandelt werden sollen. Das Element „Total“ spiegelt den Gesamtbetrag der latenten Steueransprüche wider, die für frühere Geschäftsjahre als storniert behandelt werden sollen. Dieser Gesamtbetrag sollte auf einen Betrag begrenzt sein, der dem inländischen Steuerverlust multipliziert mit dem Mindestsatz gemäß den Absätzen 124-126 des Kommentars zu Artikel 4.6.1 entspricht. Das Element „AmountAttributed“ spiegelt die latenten Steueransprüche wider, die für jedes der vorherigen Geschäftsjahre, in die inländische Verluste zurückgetragen wurden, als storniert behandelt werden sollen. Dieses Element bezieht sich auf das vorherige Geschäftsjahr, dem das Element „Amount“ zugeordnet ist. Das Element „Amount“ spiegelt den Betrag der latenten Steueransprüche wider, der für ein früheres Geschäftsjahr, in das der inländische steuerliche Verlust zurückgetragen wurde, als storniert behandelt werden soll. Das Element „CoveredTaxRefund“ spiegelt die Rückerstattung erfasster Steuern im Zusammenhang mit inländischen Verlusten wider, die auf frühere Geschäftsjahre zurückgetragen wurden.

Das Element „Total“ gibt den Gesamtbetrag der Rückerstattung der erfassten

Steuern an. Dieser Gesamtbetrag entspricht dem Betrag der Steuerrückerstattung im

Gesamt

Hinblick auf Verlustrückträge, die im Berichtsgeschäftsjahr gewährt wurden.

Das Element „AmountAttributed“ spiegelt die Rückerstattung der erfassten Steuern

Rückerstattungsbetrag erfasster für jedes der vorherigen Geschäftsjahre wider, in die inländische Verluste

Steuern

zurückgetragen wurden.

Dieses Element bezieht sich auf das vorherige Geschäftsjahr, dem das Element

Jahr

„Amount“ zugeordnet ist.

Das Element „Amount“ spiegelt die Erstattung der erfassten Steuern im

Zusammenhang mit einem inländischen Steuerverlust wider, der auf ein früheres

Geschäftsjahr zurückgeführt wird. Die Höhe der Erstattung entspricht dem

inländischen Steuerverlust, der auf das vorangegangene Geschäftsjahr

Betrag

zurückübertragen wurde.

Das Element „DeemedDistTax“ identifiziert alle vorherigen Geschäftsjahre, für die ein

Nachversteuerungskonto für Nachversteuerungskonto für fiktive Ausschüttungen gebildet wird, und wird gemäß

fiktive Ausschüttungen

den Grundsätzen in Artikel 5.4.1 neu berechnet.

Gesamtbetrag der fiktiven

Ausschüttungssteuer

Das Element „Total“ gibt den Gesamtbetrag der fiktiven Ausschüttungssteuer an.

Wahlrechtsausübung zur fiktiven Das optionale Element „Election“ spiegelt das Wahlrecht der fiktiven

Ausschüttungssteuer

Ausschüttungssteuer gemäß Artikel 7.3.1 wider.

Nachversteuerungsmechanismu Das Element „Recapture“ spiegelt den Nachversteuerungsmechanismus für Artikel

s

7.3 wider.

Das Element „Year“ spiegelt das Geschäftsjahr wider, für das die berichtspflichtige

Geschäftseinheit den Betrag der gemäß Artikel 7.3.2 ermittelten fiktiven

Geschäftsjahr

Ausschüttungssteuer melden muss.

Nachversteuerungsbetrag zu Dieses Element gibt den Nachversteuerungsbetrag zu Beginn des Geschäftsjahres

Beginn des Geschäftsjahres an.

Betrag des

Das Element „DDTYear0“ spiegelt den Betrag der für das Berichtsgeschäftsjahr

Berichtsgeschäftsjahres

gezahlten oder verwendeten fiktiven Ausschüttungssteuer wider.

Betrag des

Das Element „DDTYear-1“ spiegelt den Betrag der im ersten vorangegangenen

Berichtsgeschäftjahres-1

Geschäftsjahr gezahlten oder verwendeten fiktiven Ausschüttungssteuer wider.

Betrag des Berichtsgeschäftenjahres-2 Betrag des Berichtsgeschäftsjahres-3 Gesamtbetrag der fiktiven Ausschüttungssteuer

Das Element „DDTYear-2“ spiegelt den Betrag der im zweiten vorangegangenen Geschäftsjahr gezahlten oder verwendeten fiktiven Ausschüttungssteuer wider. Das Element „DDTYear-3“ spiegelt den Betrag der im dritten vorangegangenen Geschäftsjahr gezahlten oder verwendeten fiktiven Ausschüttungssteuer wider. Das Element „TotalDDT“ spiegelt die gesamte gezahlte oder verwendete fiktive Ausschüttungssteuer wider.

Seite 25 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

globe:EndAmount
globe:Reduction globe:IncrementalTopUpTax
globe:Ratio globe:DeferTaxAdjustAmt
globe:Total
globe:DefTaxAmt globe:globe:DiffCarryValue globe:GloBEValue globe:BefRecastAdjust globe:TotalAdjust globe:PreRecast globe:Recast
globe:Higher
globe:Lower globe:Adjustments

1P

n

1P

n

1P

n

xsd:integer xsd:integer xsd:integer

1P

n

0..1 O

1P

n

1

6 globe:percentage

xsd:integer

1P

n

1P

n

1P

n

1P

n

1P

n

1P

n

0..1 O

xsd:integer
xsd:integer xsd:integer
xsd:integer xsd:integer xsd:integer

0..1 O

n

xsd:integer

0..1 O

n

0..n O

xsd:integer

Seite 26 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das Element „EndAmount“ spiegelt den offenen Saldo eines Nachversteuerungskontos für fiktive Auschüttungen wider. Am Ende jedes folgenden Geschäftsjahres werden die offenen Salden der Nachversteuerungskonten für fiktive Ausschüttungen gemäß Artikel 7.3.3 chronologisch, jedoch nicht unter Null, um die von den Geschäftseinheiten (oder Mitgliedern von Joint Ventures) gezahlten Steuern, den Betrag etwaiger Netto-GloBE-Verluste des jeweiligen Steuerhoheitsgebiets multipliziert mit dem Mindeststeuersatz und anschließend den Betrag des auf das laufende Geschäftsjahr angewendeten Verlustvortrags des Nachversteuerungskontos reduziert.

Minderung

Besteht am letzten Tag des vierten Geschäftsjahres nach dem Geschäftsjahr, für das das Konto eingerichtet wurde (erste Zeile dieser Tabelle), ein offener Saldo, gilt Artikel 7.3.5. Verlässt im Geschäftsjahr eine ausscheidende Geschäftseinheit (oder ein Mitglied eines Joint Ventures) die multinationale Unternehmensgruppe oder überträgt im Wesentlichen ihr gesamtes Vermögen, gilt Artikel 7.3.7. Anhand des Betrages wird ermittelt, ob die zusätzliche laufende Ergänzungssteuer anfällt und das Ergebnis wird in 3.3.3.1 dargestellt. Das Element „Reduction“ spiegelt die Minderung der angepassten erfassten Steuern für ein vorheriges Geschäftsjahr wider. Die berichtspflichtige Geschäftseinheit muss alle vorherigen Geschäftsjahre identifizieren, für die ein ausstehendes Nachversteuerungskonto für fiktive Ausschüttungen gemäß den Grundsätzen in Artikel 5.4.1 neu berechnet wird.

Weitere Ergänzungssteuer
Quotient nach Artikel 7.3.8 Anpassungsbetrag latente Steuern nach Artikel 4.1.1.(b) Gesamtbetrag
Gesamtbetrag latenter Steueraufwand Latenter Steueraufwand Buchwertdifferenz Latenter Steueraufwand nach GloBE-Buchwert

Das Element „IncrementalTopUpTax“ spiegelt die etwaige weitere Ergänzungssteuer wider. Es handelt sich um den Gesamtbetrag der Ergänzungssteuer, der gemäß Artikel 5.4.1 ermittelt wird, wenn Artikel 7.3.7 Anwendung findet. Das Element „Ratio“ spiegelt den Quotient für die Nachversteuerung im Veräußerungsfall wider. Der Quotient ist in Artikel 7.3.8 definiert und wird für jede ausscheidende Geschäftseinheit (Mitglied der JV-Gruppe) anhand der folgenden Formel ermittelt: GloBE-Gewinn der Geschäftseinheit (oder des Mitglieds der JV-Gruppe) / Nettogewinn des Steuerhoheitsgebiets. Der „DeferTaxAdjustAmt“ spiegelt den Gesamtbetrag der Anpassung um latente Steuern gemäß Artikel 4.1.1.(b) wider. Das Element „Total“ gibt den Gesamtbetrag der Anpassung um latente Steuern für das Steuerhoheitsgebiet an. Das Element „DefTaxAmt“ gibt den Gesamtbetrag des latenten Steueraufwands in den Jahresabschlüssen aller im jeweiligen Steuerhoheitsgebiet ansässigen Geschäftseinheiten oder Mitglieder von Joint Ventures an. Wird der latente Steueraufwand als Belastung auf dem Konto für latenten Steueraufwand verbucht, ist der Betrag als positive Zahl auszuweisen. Wird der latente Steueraufwand als Gutschrift auf dem Konto für latenten Steueraufwand verbucht, ist der Betrag als negativer Betrag auszuweisen. Das Element „DiffCarryValue“ gibt den latenten Steueraufwand in Bezug auf Vermögenswerte oder Schulden an, deren GloBE-Buchwert vom buchhalterischen Buchwert abweicht. Das Element „GloBEValue“ gibt den latenten Steueraufwand basierend auf dem GloBE-Buchwert von Vermögenswerten oder Schulden an.

Latenter Steueraufwand vor

Das Element „BefRecastAdjust“ gibt den latenten Steueraufwand für GloBE-Zwecke

Neuberechnung und Anpassung vor der Neuberechnung und Anpassung an.

Das Element „TotalAdjust“ gibt den Gesamtbetrag der vorgenommenen

Gesamtanpassungsbetrag

Anpassungen an.

Latenter Steueraufwand vor

Das Element „PreRecast“ gibt den latenten Steueraufwand für GloBE-Zwecke vor

Neuberechnung

einer Neuberechnung an.

Das Element „Recast“ gibt den Betrag des latenten Steueraufwands an, der zum

Mindeststeuersatz neu berechnet wurde. Sie wenden den höheren und/oder

Neuberechnung

niedrigeren Satz an.

Das Element „Higher“ gibt die Differenz zwischen dem latenten Steueraufwand, der

mit einem höheren Steuersatz als dem Mindeststeuersatz erfasst wurde, und dem

latenten Steueraufwand basierend auf dem Mindeststeuersatz an.

Wird der latente Steueraufwand für das Geschäftsjahr vor einer etwaigen

Neuberechnung als Gutschrift auf dem Konto für latenten Steueraufwand

berücksichtigt, ist die Differenz als positiver Betrag auszuweisen.

Wird der latente Steueraufwand für das Geschäftsjahr vor einer etwaigen

Neuberechnung als Belastung auf dem Konto für latenten Steueraufwand

Höherer Steuersatz

berücksichtigt, ist die Differenz als negativer Betrag auszuweisen.

Das Element „Lower“ gibt die Differenz zwischen dem latenten Steueraufwand für

einen GloBE-Verlust (Artikel 4.4.3.) an, der zu einem niedrigeren Steuersatz als dem

Mindeststeuersatz erfasst wurde, und dem latenten Steueraufwand basierend auf

dem Mindeststeuersatz. Die Differenz ist als negativer Betrag auszuweisen, wenn sie

auf die Erfassung eines latenten Steueranspruchs für einen GloBE-Verlust

zurückzuführen ist, und als positiver Betrag, wenn sie auf die Stornierung eines

Niedrigerer Steuersatz

solchen latenten Steueranspruchs zurückzuführen ist

Das wiederholbare Element „Adjustments“ spiegelt die Anpassungen wider, die am

Anpassungen

latenten Steueraufwand vorgenommen wurden.

Bundeszentralamt für Steuern

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

Kardinalität P O B Format Min Max Datentyp

globe:Amount

globe:AdjustmentItem globe:RecaptureDeferred

globe:DTLRFYMinus5

globe:RecapDTLRFYMinus5 globe:DTLRFY globe:AggregateDTL

globe:ReportingFiscalYear
globe:AmountPreTransition globe:AmountOutBalance globe:AmountUnjustified

globe:PriorFiscalYear

globe:AmountPreTransition globe:AmountOutBalance globe:AmountUnjustified

globe:Transition

globe:Year

1P

n

1P

en

1P

1P

n

1P

n

1P

n

1P

1P

1P

n

1P

n

1P

n

1P

1P

n

1P

n

1P

n

0..n O

1P

d

xsd:integer globe:DeferredAdjustedTax_EnumType
xsd:integer xsd:integer xsd:integer
xsd:integer xsd:integer xsd:integer
xsd:integer xsd:integer xsd:integer
xsd:date

globe:DeferredTaxLiabilityStart globe:DeferredTaxLiabilityRecast
globe:DeferredTaxAssets globe:Total

0..1 O

n

0..1 O

n

0..1 O

1P

n

xsd:integer xsd:integer
xsd:integer

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Betrag
Anpassungselement Gezahlte nachversteuerte latente Steuerschuld
DTLRFYMinus5

Das Element „Amount“ gibt den Anpassungsbetrag an, der vor einer Neuberechnung ermittelt wurde. Führt die Anpassung zu einer Erhöhung des Gesamtbetrags des angepassten latenten Steueraufwands, so ist der Betrag als positive Zahl anzugeben. Führt die Anpassung zu einer Verringerung des Gesamtbetrags des angepassten latenten Steueraufwands, wird der Betrag als negative Zahl angegeben. Das Element „Adjustment Item“ gibt die Art der der Anpassung des latenten Steueraufwands wieder, die aus der folgenden Liste auszuwählen ist: siehe globe:DeferredAdjustedTax_EnumType (GIR2501 - GIR2516) unter Wertelisten für Aufzählungstypen Das Element „RecaptureDeferred“ spiegelt die während des Geschäftsjahres beglichene nachversteuerte latente Steuerschuld wider. Das Element „DTLRFYMinus5“ gibt den Betrag der latenten Steuerschuld (engl. deferred tax liability - DTL) an, die im fünften Geschäftsjahr vor dem Berichtsgeschäftsjahr geltend gemacht wurde und der Nachversteuerungsregelung unterliegt.

Das Element „RecapDTLRFYMinus5“ gibt den Betrag der im Berichtsgeschäftsjahr

ermittelten nachversteuerten latenten Steuerschuld in Bezug auf das fünfte dem

RecapDTLRFYMinus5

Berichtsgeschäftsjahr vorausgehende Geschäftsjahr an.

Das Element „DTLRFY“ gibt den Betrag der latenten Steuerschuld an, die der

Nachversteuerungsregelung unterliegen und für das Berichtsjahr geltend gemacht

Betrag der latenten Steuerschuld wurden.

Das Element „AggregateDTL“ enthält die aggregierten Nachversteuerungskonten für

aggregierte DTL

latente Steuerschulden für das Berichtsgeschäftsjahr bzw. das vorangegangene

Rückgewinnungskonten

Geschäftsjahr.

Berichtsgeschäftsjahr

Das Element „ReportingFiscalYear“ gibt die aggregierten Nachversteuerungskonten für latente Steuerschulden für das Berichtsgeschäftsjahr an und besteht aus den Elementen „AmountPreTransition“, ‚AmountOutBalance‘ und „Amount Unjustified“.

Betrag latenter Steuerschulden Das Element „AmountPreTransition“ gibt den Betrag der latenten Steuerschulden vor

vor Übergangsjahr

dem Übergangsjahr an.

Saldobetrag

Das Element „AmountOutBalance“ gibt den Betrag des ausstehenden Saldos an.

Ungerechtfertigter Saldo

Das Element „AmountUnjustified“ gibt den Betrag des ungerechtfertigten Saldos an.

Vorheriges Geschäftsjahr Betrag vor Übergangjahr

Das Element „PriorFiscalYear“ gibt die aggregierten Nachversteuerungskonten für latente Steuerschulden für das vorherige Geschäftsjahr an und besteht aus den Elementen „AmountPreTransition“, „AmountOutBalance“ und „Amount Unjustified“. Das Element „AmountPreTransition“ gibt den Betrag der latenten Steuerschulden vor dem Übergangsjahr an.

Saldobetrag

Das Element „AmountOutBalance“ gibt den Betrag des ausstehenden Saldos an.

Ungerechtfertigter Saldo Übergang Übergangsjahr

Das Element „AmountUnjustified“ gibt den Betrag des ungerechtfertigten Saldos an. Das wiederholbare Element „Transition“ enthält zusätzliche Informationen, die zu melden sind, wenn das Berichtsgeschäftsjahr das Übergangsjahr in Bezug auf die multinationale Unternehmensgruppe und/oder ein bestimmtes Steuerhoheitsgebiet ist. Das Element „Year“ gibt das Übergangsjahr an, das jedes Jahr gemeldet werden muss, während alle anderen Informationen dieses Abschnitts nur dann in dem globalen Mindeststeuer-Bericht gemeldet werden müssen, wenn das Berichtsgeschäftsjahr auch das Übergangsjahr ist.

Das Element „DeferredTaxLiabilityStart“ spiegelt die latenten Steuerschulden zu Beginn des Übergangsjahres wider.

Startbetrag latente Steuerschulden
Neuberechnung latente Steuerschulden
Latente Steueransprüche Gesamtbetrag latenter Steueransprüche

Die latenten Steuerschulden zu Beginn des Übergangsjahres entsprechen dem Gesamtbetrag der latenten Steuerschulden, die zu Beginn des Übergangsjahres in dem Jahresabschluss in einem Steuerhoheitsgebiet erfasst wurden. Latente Steuerschulden aus Vermögensübertragungen zwischen Geschäftseinheiten oder Mitgliedern von Joint Ventures nach dem 30. November 2021 und vor Beginn eines Übergangsjahres sind darin nicht enthalten. Diese latenten Steuerschulden sind in der Tabelle zur Anwendung von Artikel 9.1.3 zu berücksichtigen. Das Element „DeferredTaxLiabilityRecast“ spiegelt die Neuberechnung der latenten Steuerschulden zum Mindeststeuersatz wider. Die Neuberechnung der latenten Steuerschulden zum Mindeststeuersatz gilt nicht, wenn der anwendbare inländische Steuersatz niedriger als der Mindeststeuersatz ist. Das Element „DeferredTaxAssets“ spiegelt die latenten Steueransprüche wider. Es handelt sich um den Nettobetrag der gesamten zuvor bestehenden latenten Steueransprüche oder -schulden auf die übertragenen Vermögenswerte, die in dem Jahresabschluss der veräußernden Geschäftseinheit (oder Geschäftseinheiten) ausgewiesen sind. Latente Steueransprüche sind als positive Zahl, latente Steuerschulden als negative Zahl auszuweisen.
Das Element „Total“ spiegelt den Gesamtbetrag der latenten Steueransprüche wider.

Seite 27 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:DeferredTaxAssetStart globe:DeferredTaxAssetRecast globe:DeferredTaxAssetExcluded
globe:Disposal globe:ResCountryCode globe:NetDTADTL

globe:CarryingValue globe:TaxPaid

globe:DTADTL globe:AltJurisdiction

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1P

n

1P

n

1P

n

xsd:integer xsd:integer xsd:integer

0..1 O

1P

en

1P

n

2

2 iso:CountryCode_Type

xsd:integer

1P

n

1P

n

xsd:integer xsd:integer

1P

n

1O

en

xsd:integer

2

2 iso:countrycode_Type

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Startbetrag latente Steueransprüche

Das Element „DeferredTaxAssetStart“ spiegelt die latenten Steueransprüche zu Beginn des Übergangsjahres wider. Die latenten Steueransprüche zu Beginn des Übergangsjahres entsprechen dem Gesamtbetrag der latenten Steueransprüche, die zu Beginn des Übergangsjahres in dem Jahresabschluss eines Steuerhoheitsgebiet erfasst wurden. Latente Steueransprüche aus einer Übertragung von Vermögenswerten zwischen Geschäftseinheiten oder Mitgliedern von Joint Ventures nach dem 30. November 2021 und vor Beginn eines Übergangsjahres sind hiervon ausgenommen. Diese latenten Steueransprüche sind in der Tabelle zur Anwendung von Artikel 9.1.3 zu berücksichtigen.

Neuberechnung

Das Element „DeferredTaxAssetRecast“ gibt an, dass die Neuberechnung zum Mindeststeuersatz nicht gilt, wenn der anwendbare inländische Steuersatz niedriger ist als der Mindeststeuersatz, es sei denn, es kann nachgewiesen werden, dass der latente Steueranspruch einem GloBE-Verlust zuzurechnen ist. In diesem Fall könnte der latente Steueranspruch, der zu einem niedrigeren Satz als dem Mindeststeuersatz erfasst wurde, zum Mindeststeuersatz neu berechnet werden.

Latente Steueransprüche aus ausgenommenen Posten

Das Element „DeferredTaxAssetExcluded“ spiegelt die latenten Steueransprüche wider, die sich aus ausgeschlossenen Posten gemäß Artikel 9.1.2 ergeben. Die latenten Steueransprüche aus Posten, die von der Berechnung des GloBE-Gewinns oder -Verlusts gemäß Kapitel 3 ausgenommen sind, sollten ausgeschlossen werden, wenn diese latenten Steueransprüche bei einer Transaktion entstehen, die nach dem 30. November 2021 stattfindet.

Veräußerung

Das optionale Element „Disposal“ gibt alle Steuerhoheitsgebiete an, in denen sich veräußernde Geschäftseinheiten oder Mitglieder von JV-Gruppen befinden, wenn diese Geschäftseinheiten oder Mitglieder von JV-Gruppen nach dem 30. November 2021 und vor Beginn eines Übergangsjahres Vermögenswerte an in diesem Steuerhoheitsgebiet ansässige Geschäftseinheiten oder Mitglieder von JV-Gruppen veräußert haben. Die Steuerhoheitsgebiete, in denen sich veräußernde Geschäftseinheiten oder Mitglieder von JV-Gruppen befinden, können mit den Steuerhoheitsgebieten der erwerbenden Einheiten identisch sein. Das Element „ResCountryCode“ gibt das Steuerhoheitsgebiet (in Form eines zweistelligen alphabetischen Ländercodes gemäß ISO 3166-1 Alpha 2) der veräußernden Gesellschaft oder des Mitglieds der JV-Gruppe an.

Ansässigkeitsstaat

Die berichtspflichtige Geschäftseinheit muss für staatenlose Geschäftseinheiten den Status „Staatenlos“ angeben. Bei Meldungen für staatenlose Geschäftseinheiten ist der Code „X5“ zu verwenden.

Das Element „CarryingValue“ spiegelt den Buchwert der übertragenen Vermögenswerte für GloBE-Zwecke wider. Es handelt sich um den Gesamtbetrag des Buchwerts der übertragenen Vermögenswerte, der zu Beginn des Übergangsjahres gemäß den GloBE-Regeln anzusetzen ist.

Buchwert

Dieser Betrag wird durch Anpassung des bilanziellen Buchwerts bei Veräußerung des übertragenen Vermögenswerts am Tag der Übertragung ermittelt. Der bilanzielle Buchwert bei Veräußerung wird gemäß Artikel 9.1.3 gegebenenfalls angepasst und zusätzlich um Investitionen, Amortisierungen oder Abschreibungen bereinigt, die nach der Transaktion und vor Beginn des Übergangsjahres erfasst wurden.

Gezahlter Steuerbetrag

Das Element „TaxPaid“ gibt den für die Transaktion(en) gezahlten Steuerbetrag an.

Das Element „DTADTL“ gibt an, dass der Nettobetrag der latenten Steueransprüche oder -schulden in Bezug auf die übertragenen Vermögenswerte für GloBE-Zwecke dem Nettobetrag der gesamten latenten Steueransprüche und -verbindlichkeiten entspricht, die zu Beginn des Übergangsjahres für die übertragenen Vermögenswerte gemäß den GloBE-Regeln angesetzt werden sollten.

Dieser Betrag wird ermittelt, indem der Nettobetrag der gesamten bereits bestehenden latenten Steueransprüche und -schulden, die vor der Übertragung im Jahresabschluss der veräußernden Einheit gebildet wurden, im Verhältnis zu den übertragenen Vermögenswerten angepasst wird.

Nettobetrag latenter Steueransprüche auf übertragene Vermögenswerte Steuerhoheitsgebiet mit alternativem Übergangsjahr

Der Nettobetrag der gesamten bereits bestehenden latenten Steueransprüche und schulden wird gemäß Artikel 9.1.3 gegebenenfalls angepasst. Latente Steueransprüche werden als positiver Wert, latente Steuerschulden als negativer Wert ausgewiesen. Gegebenenfalls gibt das Element „AltJurisdiction“ das Steuerhoheitsgebiet an, für das ein alternatives Übergangsjahr gilt.

Seite 28 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TransBlendCFC globe:CFCJur
globe:Jurisdiction globe:Allocation

globe:SubGroupTIN globe:AggAllocTax globe:Total
globe:SubstanceExclusion globe:Total

globe:PayrollCost globe:PayrollMarkUp

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O 1..n P

1P

en

1P

2

2 iso:CountryCode_Type

1P

an

1P

n

1P

n

1 200 globe:TIN_Type xsd:integer xsd:integer

0..1 O

1P

n

xsd:integer

1P

n

1P

n

xsd:integer

1

6 globe:percentage

Seite 29 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Gemischte Hinzurechnungsbesteuerung

Wertemenge / Erklärung (deut.)
Das Element „TransBlendCFC“ und die zugehörigen Unterelemente müssen ausgefüllt werden, wenn die Steuer der gemischten Hinzurechnungsbesteuerung (i) von einem Eigentümer einer Geschäftseinheit zugerechnet wird, der in diesem Steuerhoheitsgebiet ansässig ist und zu dieser Untergruppe gehört, oder (ii) an Geschäftseinheiten, die in diesem Steuerhoheitsgebiet ansässig sind und zu dieser Untergruppe gehören, gemäß Artikel 4.3.2(c) und den zugehörigen Verwaltungsrichtlinien.

Steuerhoheitsgebiet

Das Element „Jurisdiction“ gibt die Steuerhoheitsgebiet(e) an, in denen sich die Geschäftseinheiten befinden, denen im Rahmen der gemischten Hinzurechnungsbesteuerung ein Hinzurechnungssteuerbetrag zugewiesen wurde. Die Jurisdiktion(en) sind als zweistelliger alphabetischer Ländercode gemäß ISO 3166-1 Alpha 2 anzugeben.

Zuordnung zur Untergruppe

Das Element „Allocation“ enthält Informationen zur Steuer der gemischten Hinzurechnungsbesteuerung, die einer bestimmten Untergruppe zugewiesen wird.

Der TIN-Typ gibt die Steueridentifikationsnummer der obersten Muttergesellschaft (UPE), der Geschäftseinheit, des Joint Ventures oder der Tochtergesellschaft an, die für Zwecke der erfassten Steuern in dem Steuerhoheitsgebiet verwendet wird, in dem sie für GloBE-Zwecke ansässig ist. Falls keine Steueridentifikationsnummer (TIN) verfügbar ist, kann dies ein funktionales Äquivalent sein, z. B. eine Unternehmens-/Firmenregistrierungsnummer.

Steueridentifikationsnummer

Der TIN-Typ gibt außerdem die TIN (falls vorhanden) an, die der obersten Muttergesellschaft (UPE), der Geschäftseinheit, dem Joint Venture oder der Tochtergesellschaft von dem Steuerhoheitsgebiet ausgestellt wurde, in dem die Einreichung erfolgt („Berichtssteuerhoheitsgebiet“). Er besteht aus den folgenden Elementen: Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Zuordnung der Steuer der gemischten Hinzurechnungsbesteuerung Gesamtbetrag der Steuer der gemischten Hinzurechnungsbesteuerung

Das Element „AggAllocTax“ gibt die gemischte CFC-Steuer an, die für das Geschäftsjahr vom Eigentümer der Geschäftseinheit an die Geschäftseinheiten in dem im Element „CFCJur“ angegebenen Steuerhoheitsgebiet zugewiesen wird.
Das Element „Total“ gibt die gesamte für das Geschäftsjahr zugerechnete Steuer der gemischten Hinzurechnungsbesteuerung an.

Das Element „SubstanceExclusion“ spiegelt den substanzbasierten Freibetrag (engl. Substance-based Income Exclusion) für das jeweiligen Steuerhoheitsgebiet wider.

Füllt die berichtspflichtige Geschäftseinheit die Tabelle für das Steuerhoheitsgebiet

nicht aus, wird davon ausgegangen, dass sie sich gegen die Anwendung des

Substanzbasierter Freibetrag substanzbasierten Freibetrags gemäß 3.2.3.1.a.1.c entschieden hat.

Gesamtbetrag substanzbasierter

Freibetrag

Das Element „Total“ gibt den Gesamtbetrag des substanzbasierten Freibetrags an.

Lohnkosten Aufschlagsprozentsatz

Das Element „PayrollCost“ gibt an, dass die berücksichtigungsfähigen Lohnkosten von berücksichtigungsfähigen Beschäftigten, die in dem Steuerhoheitsgebiet tätig sind, keine Lohnkosten umfassen dürfen, die (i) aktiviert und im Buchwert der berücksichtigungsfähigen materiellen Vermögenswerte enthalten sind; oder (ii) den Erträgen des internationalen Seeverkehrs und dessen anerkannten Neben- und Hilfsgeschäften einer Geschäftseinheit zuzurechnen sind.
Übt ein Beschäftigter im Berichtsgeschäftsjahr 50 % oder weniger seiner Tätigkeit für die multinationale Unternehmensgruppe in dem Steuerhoheitsgebiet des Arbeitgebers aus, berücksichtigen die berücksichtigungsfähigen Lohnkosten berücksichtigungsfähiger Arbeitnehmer nur den Anteil der Lohnkosten, der gemäß den entsprechenden Verwaltungsrichtlinien auf die Arbeitszeit des Arbeitnehmers in dem Steuerhoheitsgebiet des Arbeitgebers entfällt. Die relevanten berücksichtigungsfähigen Lohnkosten berücksichtigungsfähiger Arbeitnehmer umfassen nicht den Betrag der berücksichtigungsfähigen Lohnkosten, der auf Einkünfte entfällt, die gemäß den entsprechenden Verwaltungsrichtlinien gemäß Artikel 7.2.1 vom GloBE-Gewinn der obersten Muttergesellschaft ausgeschlossen sind.
Wenn eine Einheit infolge der Übertragung direkter oder indirekter Eigentumsanteile an dieser Einheit eine Geschäftseinheit einer multinationalen Unternehmensgruppe wird oder aufhört, eine Geschäftseinheit einer multinationalen Unternehmensgruppe zu sein, werden bei der Berechnung der berücksichtigungsfähigen Lohnkosten des Zielunternehmens nur jene Kosten berücksichtigt, die im Konzernabschluss der obersten Muttergesellschaft gemäß Artikel 6.2.1(d) aufgeführt sind. Das Element „PayrollMarkUp“ gibt an, dass der entsprechende Aufschlagsprozentsatz für das Berichtsgeschäftsjahr angewendet wird.

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TangibleAssetValue globe:TangibleAssetMarkup globe:PEAllocation
globe:JurOfOwners
globe:ResCountryCode globe:UPE globe:NotApplicable globe:PayrollCost globe:Total globe:Allocation globe:TangibleAssetValue globe:Total globe:Allocation
globe:FTEAllocation

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1P

n

1P

n

0..n O 1P

xsd:integer

1

6 globe:percentage

1B

en

1B

b

1B

b

1P

1P

n

1P

n

1P

1P

n

1P

n

2

2 iso:CountryCode_Type

xsd:boolean

xsd:boolean

xsd:integer xsd:integer
xsd:integer xsd:integer

0..n O

Seite 30 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Das Element „TangibleAssetValue“ spiegelt den Buchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte im jeweiligen Steuerhoheitsgebiet wider. Der Buchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte im jeweiligen Steuerhoheitsgebiet umfasst nicht: (i) den Buchwert von Immobilien (einschließlich Grundstücken oder Gebäuden), die zum Verkauf, Finanzierungsleasing oder als Investition gehalten werden; und (ii) den Buchwert von materiellen Vermögenswerten, die zur Erzielung der Einkünfte aus internationalem Seeverkehr und aus dessen anerkannten Neben- und Hilfsgeschäften verwendet werden.

Befindet sich der materielle Vermögenswert während des Berichtsgeschäftsjahrs höchstens 50 % der Zeit im Steuerhoheitsgebiet ihres Eigentümers (bzw. gegebenenfalls des Leasingnehmers), berücksichtigt der Buchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte gemäß den entsprechenden Verwaltungsrichtlinien nur den Buchwert des Vermögenswerts, der dem Zeitpunkt zuzurechnen ist, zu dem sich der Vermögenswert im Steuerhoheitsgebiet des Eigentümers (bzw. gegebenenfalls des Leasingnehmers) befand. Der Buchwert der relevanten berücksichtigungsfähigen Vermögenswerte umfasst nicht den Buchwert der berücksichtigungsfähigen Sachanlagen, die anteilig den Einkünften zuzurechnen sind, die gemäß Artikel 7.2.1 gemäß den entsprechenden Verwaltungsrichtlinien vom GloBE-Gewinn der obersten Muttergesellschaft ausgeschlossen sind.

Buchwert Sachanlagen Aufschlagsprozentsatz
Betriebsstätten Zuordnung Ansässigkeitsstaat der Eigentümer

Wenn eine Einheit aufgrund der Übertragung direkter oder indirekter Eigentumsanteile an dieser Einheit eine Geschäftseinheit einer multinationalen Unternehmensgruppe wird oder nicht mehr ist, wird die Berechnung des Buchwerts der berücksichtigungsfähigen materiellen Vermögenswerte der Zielgeschäftseinheit proportional angepasst, um der Länge des jeweiligen Geschäftsjahres zu entsprechen, in dem die Zielgeschäftseinheit gemäß Artikel 6.2.1 Buchstabe e Mitglied der multinationalen Unternehmensgruppe war. Das Element „TangibleAssetMarkup“ gibt die Anwendung des entsprechenden Aufschlagsprozentsatzes für das Berichtsgeschäftsjahr an. Das wiederholbare Element „PEAllocation“ bezieht sich auf die Zuordnung der berücksichtigungsfähigen Lohnkosten und des Buchwerts der berücksichtigungsfähigen materiellen Vermögenswerte zu Betriebsstätten im Sinne des substanzbasierten Freibetrags. Das Element „JurOfOwners“ enthält weitere Informationen zum Ansässigkeitsstaat der Eigentümer. Es besteht aus den Elementen „ResCountryCode“, „UPE“ und „NotApplicable“.
Das Element „ResCountryCode“ gibt das Steuerhoheitsgebiet (als zweistelligen alphabetischen Ländercode nach ISO 3166-1 Alpha 2) an, in dem sich die Betriebsstätten für GloBE-Zwecke befinden. Die berichtspflichtige Geschäftseinheit füllt für jedes Steuerhoheitsgebiet, in dem sich Betriebsstätten befinden, denen gemäß Artikel 5.3.6 berücksichtigungsfähige Lohnkosten und der Buchwert berücksichtigungsfähiger materieller Vermögenswerte zugeordnet sind, eine separate Zeile aus.

Ansässigkeitsstaat Oberste Muttergesellschaft als Eigentümer
Nicht anwendbar
Berücksichtigungsfähige Lohnkosten Gesamtbetrag berücksichtigungsfähiger Lohnkosten
Zuordnung Gesamtbuchwert berücksichtigungsfähiger Vermögenswerte Gesamtbetrag Sachanlagevermög
Zuordnung

Die berichtspflichtige Geschäftseinheit meldet „Staatenlos“, wenn die Betriebsstätte für GloBE-Zwecke staatenlos ist. Bei der Meldung staatenloser Geschäftseinheiten ist der Code „X5“ zu verwenden. Das Element „UPE“ gibt an, ob der Eigentümer eine oberste Muttergesellschaft (engl. Ultimate Parent Entity - UPE) ist. Das Element „Not Applicable“ gibt an, dass keine Angaben zum Ansässigkeitsstaat des Eigentümers gemacht werden müssen. Das Element „PayrollCost“ gibt die gesamten relevanten berücksichtigungsfähigen Lohnkosten für alle im Steuerhoheitsgebiet belegenen Stammhäuser vor etwaigen Anpassungen an.
Das Element „Total“ gibt den Gesamtbetrag der gesamten relevanten berücksichtigungsfähigen Lohnkosten an. Das Element „Allocation“ gibt die gesamten relevanten berücksichtigungsfähigen Lohnkosten an, die den Betriebsstätten in den einzelnen Steuerhoheitsgebieten zugeordnet werden. Das Element „TangibleAssetValue“ gibt den Gesamtbuchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte für alle in dem Steuerhoheitsgebiet ansässigen Stammhäuser vor etwaigen Anpassungen an.
Das Element „Total“ gibt den Gesamtbetrag der materiellen Vermögenswerte an. Das Element „Allocation“ gibt den gesamten Wert der relevanten materiellen Vermögenswert an, der den in den einzelnen Steuerhoheitsgebieten belegenen Betriebsstätten zugeordnet wird.

Das Element „FTE Allocation“ bezieht sich auf die Zuordnung der berücksichtigungsfähigen Lohnkosten und des Buchwerts der berücksichtigungsfähigen materiellen Vermögenswerte einer transparenten Einheit Transparente Einheit Zuordnung (engl- Flow-through-Entity - FTE) zum Zwecke des substanzbasierten Freibetrags.

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:JurOfOwners

globe:ResCountryCode globe:UPE globe:NotApplicable globe:PayrollCost globe:Total globe:Allocation globe:TangibleAssetValue globe:Total globe:Allocation globe:ExcessProfits globe:AdditionalTopUpTax globe:NONArt4.1.5
globe:Articles
globe:Year globe:Previous

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp
1P

1B

en

1B

b

1B

b

1P

1P

n

1P

n

1P

1P

n

1P

n

1P

n

0..1 O 0..n O

2

2 iso:CountryCode_Type

xsd:boolean

xsd:boolean

xsd:integer xsd:integer
xsd:integer xsd:integer xsd:integer

1..n P

en

globe:NonArt415_EnumType

1P

d

1P

xsd:date

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Ansässigkeitsstaat der Eigentümer

Wertemenge / Erklärung (deut.)
Das Element „JurOfOwners“ enthält weitere Informationen zum Ansässigkeitsstaat der Eigentümer. Es besteht aus den Elementen „ResCountryCode“, „UPE“ und „NotApplicable“.

Ansässigkeitsstaat Oberste Muttergesellschaft als Eigentümer
Nicht anwendbar
Berücksichtigungsfähige Lohnkosten
Gesamtbuchwert berücksichtigungsfähiger Vermögenswerte

Das Element ResCountryCode gibt den zweistelligen alphabetischen Ländercode auf Grundlage des Standards ISO 3166-1 Alpha 2 für den Staat an, in dem sich die Eigentümer der Geschäftseinheit (oder Mitglieder der JV-Gruppe) für GloBE-Zwecke befinden. Die meldende Geschäftseinheit muss für jeden staatenlosen Eigentümer einer Geschäftseinheit „Staatenlos“ melden. Die meldende Geschäftseinheit muss für jeden Staat, in dem sich Eigentümer der Geschäftseinheit (oder Mitglieder der JVGruppe) befinden, denen gemäß Artikel 5.3.7 (a) förderfähige Lohnkosten und förderfähige Sachanlagen zugeschrieben werden, eine separate Zeile ausfüllen. Falls Artikel 5.3.7 (b) zutrifft, muss die einreichende Gesellschaft „UPE“ in einer separaten Zeile melden (für förderfähige Lohnkosten und förderfähige Sachanlagen, die der UPE nach Anwendung von Artikel 7.1.1 zugewiesen werden). Die meldende Geschäftseinheit muss für alle anderen erstattungsfähigen Lohnkosten und erstattungsfähigen Sachanlagen, die gemäß Artikel 5.3.7 Buchstabe c von der Berechnung des substanzbezogenen Einkommensausschlusses der multinationalen Unternehmensgruppe ausgeschlossen sind, „Nicht zutreffend“ angeben. Bei der Meldung staatenloser Geschäftseinheiten ist der Code „X5“ zu verwenden. Das Element „UPE“ gibt an, ob der Eigentümer eine oberste Muttergesellschaft (engl. Ultimate Parent Entity - UPE) ist. Das Element „Not Applicable“ gibt an, dass keine Angaben zum Ansässigkeitsstaat des Eigentümers gemacht werden müssen. Das Element „PayrollCost“ spiegelt die gesamten relevanten berücksichtigungsfähigen Lohnkosten für alle im Steuerhoheitsgebiet ansässigen transparenten Einheiten nach etwaigen Anpassungen gemäß Artikel 5.3.6 und vor etwaigen Anpassungen gemäß Artikel 5.3.7 wider. Das Element „Total“ gibt den Gesamtbuchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte für alle transparenten Einheiten in dem Steuerhoheitsgebiet nach etwaigen Anpassungen gemäß Artikel 5.3.6 und vor etwaigen Anpassungen gemäß Artikel 5.3.7 an.

Zuordnung Gesamtbuchwert nach Anpassungen Gesamtbetrag materielle Vermögenswerte
Zuordnung Übersteigender Gewinn Zusätzlicher Steuererhöhungsbetrag NonArt4.1.5
Anpassungsartikel

Das Element „Allocation“ gibt die gesamten relevanten berücksichtigungsfähigen Lohnkosten an, die den Eigentümern der Geschäftseinheiten (oder Mitgliedern von Joint Venture-Gruppen) in den einzelnen Steuerhoheitsgebieten zugewiesen werden. Das Element „TangibleAssetValue“ gibt den Gesamtbuchwert der relevanten berücksichtigungsfähigen materiellen Vermögenswerte für alle transparenten Einheiten in dem Steuerhoheitsgebiet nach etwaigen Anpassungen gemäß Artikel 5.3.6 und vor etwaigen Anpassungen gemäß Artikel 5.3.7 an.
Das Element „Total“ gibt den Gesamtbetrag der materiellen Vermögenswerte an. Das Element „Allocation“ gibt den Gesamtwert der relevanten berücksichtigungsfähigen Vermögenswerte an, der den Eigentümern der Geschäftseinheiten (oder Mitgliedern von Joint-Venture-Gruppen) in den einzelnen Steuerhoheitsgebieten zugeordnet wird. Das Element „ExcessProfits“ spiegelt den übersteigenden Gewinn für das Steuerhoheitsgebiet wider. Das Element „AdditionalTopUpTax“ gibt den zusätzlichen Steuererhöhungsbetrag für das Steuerhoheitsgebiet an. Der zusätzliche Steuererhöhungsbetrag entspricht der Differenz zwischen der zuvor gemeldeten Ergänzungssteuer und der neu berechneten Ergänzungssteuer. Das optionale Element „NonArt4.1.5“ gibt an, dass die Tabelle ausgefüllt werden muss, wenn ein ETR-Anpassungsartikel zutrifft. Dieses Element kann bei Bedarf wiederholt werden. Das Element „Artikel“ spiegelt die ETR-Anpassungsartikel wider, die eine Neuberechnung des ETR und der Ergänzungssteuer für ein vorheriges Geschäftsjahr gemäß Artikel 5.4.1 erfordern oder zulassen. Dieses Element kann bei Bedarf wiederholt werden. Die entsprechende(n) Option(en) sollten aus der folgenden Liste ausgewählt werden: siehe globe:NonArt415_EnumType (GIR2601 – GIR2606) unter „Wertelisten für Aufzählungstypen“

Geschäftsjahr Vorherige(s) Geschäftsjahr(e)

Das Element „Year“ gibt an, dass Artikel 4.4.4 nur ausgewählt werden soll, wenn das relevante Geschäftsjahr das fünfte vorangegangene Geschäftsjahr ist und der Betrag der zusätzlichen Steuererhöhungsbetrags auf der Grundlage der in Abschnitt 3.2.2.2 bereitgestellten Informationen bestimmt wird. Artikel 7.3.5 ist nur auszuwählen, wenn das relevante Geschäftsjahr das vierte vorangegangene Geschäftsjahr ist und der Betrag des zusätzlichen Steuererhöhungsbetrags auf der Grundlage der in Abschnitt 3.2.3.2.a bereitgestellten Informationen bestimmt wird. Das Element „Previous“ gibt das/die vorherige(n) Geschäftsjahr(e) an, auf das/die sich die in 3.3.3.1.1 aufgeführten ETR-Anpassungsartikel beziehen.

Seite 31 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:NetGlobeIncome globe:AdjustedCoveredTax globe:ETRRate globe:ExcessProfits globe:TopUpTaxPercentage globe:TopUpTax globe:Recalculated globe:NetGlobeIncome globe:AdjustedCoveredTax globe:ETRRate globe:ExcessProfits globe:TopUpTaxPercentage globe:TopUpTax globe:AdditionalTopUpTax
globe:Art4.1.5 globe:AdjustedCoveredTax globe:GlobeLoss globe:ExpectedAdjustedCoveredTax
globe:AdditionalTopUpTax
globe:QDMTT
globe:FAS
globe:Amount
globe:MinRate
globe:BasisforBlending
globe:SBIEAvailable
globe:DeMinAvailable
globe:Currency

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1P

n

1P

n

1P

n

1P

n

1P

1P

n

1P

1P

n

1P

n

1P

n

1P

n

1P

n

1P

n

1P

n

0..1 O

1P

n

1P

n

1P

n

1P

n

0..1 O

xsd:integer

xsd:integer

1

6 globe:percentage

xsd:integer

1

6 globe:percentage

xsd:integer

xsd:integer

xsd:integer

1

6 globe:percentage

xsd:integer

1

6 globe:percentage

xsd:integer

xsd:integer

xsd:integer xsd:integer xsd:integer
xsd:integer

1P

an

1P

n

0..1 P

n

0..1 P

an

1P

b

1P

b

1P

en

1 200 stf:StringMin1Max200_Type

xsd:integer

1

6 globe:percentage

1 4000 stf:StringMin1Max4000_Type

1

1 xsd:boolean

1

1 xsd:boolean

3

3 iso:currCode_Type

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung Netto-GloBE-Einkünfte

Wertemenge / Erklärung (deut.)
Das Element „NetGlobeIncome“ spiegelt den Netto-GloBE-Gewinn oder -verlust wider. Das Element enthält Informationen zum zuvor gemeldeten Betrag unter Berücksichtigung etwaiger Anpassungen, die gemäß den relevanten ETRAnpassungsartikeln im vorherigen Geschäftsjahr (sofern vorhanden) erforderlich waren. Der neu berechnete Betrag berücksichtigt etwaige Anpassungen, die gemäß den relevanten ETR-Anpassungsartikeln im vorherigen Geschäftsjahr (sofern vorhanden) und im Berichtsgeschäftsjahr erforderlich waren.

Angepassten erfassten Steuern
Effektiver Steuersatz Übersteigender Gewinn Ergänzungssteuersatz Ergänzungssteuer
Neuberechnung Netto-GloBE-Einkünfte

Das Element „AdjustedCoveredTax“ gibt die angepassten erfassten Steuern an. Das Element „ETRRate“ gibt den effektiven Steuersatz (engl. effective tax rate ETR) an. Das Element „ExcessProfits“ spiegelt den übersteigenden Gewinn wider. Das Element „TopUpTaxPercentage“ gibt den Ergänzungssteuersatz an. Das Element „TopUpTax“ gibt die Ergänzungssteuer an. Das Element „Recalculated“ gibt das/die vorherige(n) Geschäftsjahr(e) an, auf das/die sich die ETR-Anpassungen beziehen. Das Element „NetGlobeIncome“ gibt den Netto-GloBE-Gewinn oder -Verlust an.

Angepassten erfassten Steuern
Effektiver Steuersatz Übersteigender Gewinn Ergänzungssteuersatz Ergänzungssteuer Zusätzlicher Steuererhöhungsbetrag
Artikel 4.1.5
Angepassten erfassten Steuern

Das Element „AdjustedCoveredTax“ gibt die angepassten erfassten Steuern an. Das Element „ETRRate“ gibt den effektiven Steuersatz (engl. effective tax rate ETR) an. Das Element „ExcessProfits“ spiegelt den übersteigenden Gewinn wider. Das Element „TopUpTaxPercentage“ gibt den Ergänzungssteuersatz an. Das Element „TopUpTax“ gibt die Ergänzungssteuer an. Das Element „AdditionalTopIUpTax“ gibt den zusätzlichen Steuererhöhungsbetrag an. Das Element „Art. 4.1.5“ gibt den zusätzlichen Steuererhöhungsbetrag für die Zwecke von Artikel 4.1.5 an. Diese Tabelle muss nicht ausgefüllt werden, wenn die multinationale Unternehmensgruppe in dem Steuerhoheitsgebiet einen positiven Betrag an GloBE-Nettogewinn hat. Das Element „AdjustedCoveredTax“ gibt den Betrag der angepassten erfassten Steuern für das Steuerhoheitsgebiet an.

GloBE-Verlust Erwartete angepasste erfasste Steuern Zusätzlicher Steuererhöhungsbetrag nach Artikel 4.1.5 Anerkannte nationale Ergänzungssteuer
Rechnungslegungsstandard
Betrag der nationalen Ergänzungssteuer
Mindeststeuersatz Grundlage für die Zusammenlegung
Substanzbasierter Freibetrag
De-minimis-Ausschluss
Währung

Das Element „GlobeLoss“ gibt den GloBE-Verlust für das Steuerhoheitsgebiet an. Das Element „ExpectedAdjustedCoveredTax“ gibt die erwarteten angepassten erfassten Steuern für das Steuerhoheitsgebiet an.
Das Element „AdditionalTopUpTax“ gibt den zusätzlichen Steuererhöhungsbetrag gemäß Artikel 4.1.5 an. Das Element „QDMTT“ gibt die in dem Steuerhoheitsgebiet zu zahlende anerkannte nationale Ergänzungssteuer (engl. Qualified Domestic Minimum Top-Up Tax QDMTT) an. Das Element „FAS“ gibt den anerkannten Rechnungslegungsstandard an, der vom zugelassenen Standardsetzer in dem Steuerhoheitsgebiet zugelassen wurde, oder den zur Vermeidung erheblicher Vergleichbarkeitseinschränkungen angepassten anerkannten Rechnungslegungsstandard, der für die Berechnung der inländischen übersteigenden Gewinne gemäß der anerkannten nationalen Ergänzungssteuer (QDMTT) verwendet wird. Das Element „Amount“ gibt den gemäß der anerkannten nationalen Ergänzungssteuer (QDMTT) des Steuerhoheitsgebiet für das Berichtsgeschäftsjahr zu zahlenden Betrag an. Dieser Betrag ist in der unter 1.2.2.3 aufgeführten Währung anzugeben. Das Element „MinRate“ gibt den für Zwecke der anerkannten nationalen Ergänzungssteuer (QDMTT) geltenden Mindeststeuersatz an, sofern dieser über 15 % liegt. Das Element „BasisforBlending“ spiegelt die Grundlage für die Zusammenlegung von Einkünften und Steuern zum Zwecke der ETR-Berechnung wider, sofern diese von den GloBE-Regeln abweicht. Das Element „SBIEAVailable“ enthält Informationen zum substanzbasierten Freibetrag, der auch für Zwecke der anerkannten nationalen Ergänzungssteuer (QDMTT) verfügbar ist. Das Element „DeMinAvailable“ enthält Informationen zum für Zwecke der anerkannten nationalen Ergänzungssteuer (QDMTT) verfügbaren De-minimisAusschluss. Das Element „Currency“ spiegelt den iso:curCode_Type für die Währung wider, die für die Einreichung der QDMTT-Informationen verwendet wird. Der Code für die Währung, in der der Wert ausgedrückt wird, muss aus der ISO-Codeliste 4217 entnommen und im Attribut currCode hinzugefügt werden.

Seite 32 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:CurrencyElection globe:Status globe:ElectionYear
globe:RevocationYear
globe:Currency globe:TopUpTax globe:ExcessNegTaxExpense
globe:PriorYearBalance globe:GeneratedInRFY globe:UtilizedInRFY globe:Remaining globe:Non-MaterialCE globe:RFY
globe:TotalRevenue
globe:AggregateSimplified globe:RFY-1
globe:TotalRevenue globe:RFY-2

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O

1P

b

1P

d

1

1 xsd:Boolean

xsd:date

0..1 O

d

xsd:date

1P

en

1P

n

1P

1P

n

1P

n

1P

n

1P

n

0..n O

1P

globe:Currency_EnumType xsd:integer
xsd:integer xsd:integer xsd:integer xsd:integer

1P

n

0..1 O

n

0..1 O

xsd:integer xsd:integer

1P

n

0..1 O

xsd:integer

Seite 33 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)
Das Element „CurrencyElection“ gibt die Anwendung der Wahlmöglichkeit an, die Berechnungen der anerkannten nationalen Ergänzungssteuer (QDMTT) in der Darstellungswährung des Konzernabschlusses oder in der lokalen Währung durchzuführen. Diese Wahlmöglichkeit kann nur getroffen werden, wenn die Gesetzgebung zur anerkannten nationalen Ergänzungssteuer Berechnungen zur anerkannten nationalen Ergänzungssteuer nach dem lokalen Rechnungslegungsstandard vorschreibt und eine oder mehrere Geschäftseinheiten in dem Steuerhoheitsgebiet eine andere Währung als die lokale Währung als funktionale Währung verwenden.

Währungswahl Status Wahljahr
Widerrufsjahr
Währung

Da die Wahlmöglichkeit auf fünf Jahre angelegt ist, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation Year“ sowie dem Element „Currency“, um anzugeben, ob die Berechnungen der anerkannten nationalen Ergänzungssteuer in der Darstellungswährung des Konzernabschlusses oder in der lokalen Währung durchgeführt werden. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr für die Wahl an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem globalen Mindeststeuer-Bericht (engl. GloBE Information Return - GIR) für das Widerrufsjahr und in den globalen Mindeststeuer-Berichten für die vier darauf folgenden Geschäftsjahre angeben. Das Element „Currency“ gibt an, ob für die 5-Jahres-Wahl die lokale Währung oder die Konzernabschluss-Präsentationswährung gewählt wurde. Folgende Eingaben sind zulässig: Siehe globe:Currency_EnumType (GIR3101 - GIR3102) unter Wertelisten für Aufzählungstypen

Ergänzungssteuer
Überschüssiger negativer Steuervortrag Überschüssiger negativer Steuervortrag aus Vorjahr Im Berichtsjahr generierter Überschüssiger negativer Steueraufwand Im Berichtsjahr genutzter überschüssiger negativer Steueraufwand Verbleibender überschüssiger negativer Steueraufwand
Unwesentliche Geschäftseinhei
Berichtsgeschäftsjahr
Gesamtumsatz

Das Element „TopUpTax“ gibt die Ergänzungssteuer des Steuerhoheitsgebiets an. Das Element „ExcessNegTaxExpense“ besteht aus den Elementen „PriorYearBalance“, „GeneratedInRFY“, „UtilizedInRF“ und „Remaining“ in Bezug auf den überschüssigen negativen Steuervortrag. Das Element „PriorYearBalance“ enthält den Saldo des überschüssigen negativen Steuervortrags aus dem Vorjahr.
Das Element „GeneratedInRFY“ enthält den überschüssigen negativen Steueraufwand, der im Berichtsjahr generiert wurde.
Das Element „UtilizedInRFY“ enthält den überschüssigen negativen Steueraufwand, der im Berichtsjahr genutzt wurde. Das verbleibende Element enthält den überschüssigen negativen Steueraufwand, der am Ende des Berichtssteuerjahres verbleibt. Das Element „unwesentliche Geschäftseinheit“ gibt die vereinfachte Berechnung für unwesentliche Geschäftseinheiten an. Das Element „RFY“ gibt das Berichtsgeschäftsjahr (engl. Reporting Fiscal Year RFY) an. Das Element „TotalRevenue“ spiegelt den Gesamtumsatz für das meldepflichtige Geschäftsjahr wider. Wird die vereinfachte Berechnung für unwesentliche Geschäftseinheiten gemäß Option (a), (b) oder (c) in 2.2.1.1.1 verwendet, muss die berichtspflichtige Geschäftseinheit auch den Gesamtumsatz aller unwesentlichen Geschäftseinheiten mit Sitz in dem Steuerhoheitsgebiet gemäß der Definition im Dokument „Safe Harbours and Penalty Relief“ für das laufende Geschäftsjahr, das erste vorangegangene Geschäftsjahr (falls zutreffend) und das zweite vorangegangene Geschäftsjahr (falls zutreffend) sowie den Durchschnitt der drei Geschäftsjahre melden.

Das Element „AggregateSimplified“ spiegelt die aggregierte vereinfachte Steuer

wider. Wird die vereinfachte Berechnung für unwesentliche Geschäftseinheiten

gemäß Option (b) in 2.2.1.1.1 genutzt, muss die berichtspflichtige Geschäftseinheit

die aggregierte vereinfachte Steuer gemäß der Definition im Dokument „Safe

Harbours and Penalty Relief“ aller unwesentlichen Geschäftseinheiten im jeweiligen

Aggregierte vereinfachte Steuer Steuerhoheitsgebiet für das Berichtsgeschäftsjahr melden.

Erste vorangegangene

Das Element „RFY-1“ gibt das 1. vorangegangene Geschäftsjahr an (sofern

Geschäftsjahr

zutreffend).

Das Element „TotalRevenue“ spiegelt den Gesamtumsatz für das meldepflichtige

Geschäftsjahr wider. Wird die vereinfachte Berechnung für unwesentliche

Geschäftseinheiten gemäß Option (a), (b) oder (c) in 2.2.1.1.1 verwendet, muss die

berichtspflichtige Geschäftseinheit auch den Gesamtumsatz aller unwesentlichen

Geschäftseinheiten mit Sitz in dem Steuerhoheitsgebiet gemäß der Definition im

Dokument „Safe Harbours and Penalty Relief“ für das laufende Geschäftsjahr, das

erste vorangegangene Geschäftsjahr (falls zutreffend) und das zweite

vorangegangene Geschäftsjahr (falls zutreffend) sowie den Durchschnitt der drei

Gesamtumsatz

Geschäftsjahre melden.

Zweite vorangegangene

Das Element „RFY-2“ gibt das zweite vorangegangene Geschäftsjahr an (sofern

Geschäftsjahr

zutreffend).

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

globe:TotalRevenue globe:Average

1P

n

1P

xsd:integer

globe:TotalRevenue
globe:ID
globe:Election globe:Art3.2.6 globe:Art4.1.5 globe:Art4.6.1 globe:Art5.3.1
globe:Art3.2.2 globe:Status globe:ElectionYear
globe:RevocationYear globe:Art3.2.5
globe:Status globe:ElectionYear
globe:RevocationYear
globe:Art3.2.8 globe:Status globe:ElectionYear
globe:RevocationYear

1P

n

xsd:integer

1P

0..1 O

1O

b

1O

b

1O

b

1O

b

1O

1P

b

0..1 P

d

0..1 O

d

1O

1P

b

0..1 P

d

0..1 O

d

1O

1P

b

0..1 P

d

0..1 O

d

globe:ID_Type

1

1 xsd:boolean

1

1 xsd:boolean

1

1 xsd:boolean

1

1 xsd:boolean

1

1 xsd:boolean

xsd:date

xsd:date

1

1 xsd:boolean

xsd:date

xsd:date

1

1 xsd:boolean

xsd:date

xsd:date

Seite 34 von 64

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Gesamtumsatz Durchschnitt
Gesamtumsatz
ID
Wahl Artikel 3.2.6 Artikel 4.1.5 Artikel 4.6.1 Artikel 5.3.1 Artikel 3.2.2 Status Wahljahr
Widerrufsjahr Artikel 3.2.5 Status Wahljahr
Widerrufsjahr Artikel 3.2.8 Status Wahljahr
Widerrufsjahr

Wertemenge / Erklärung (deut.)
Das Element „TotalRevenue“ spiegelt den Gesamtumsatz für das meldepflichtige Geschäftsjahr wider. Wird die vereinfachte Berechnung für unwesentliche Geschäftseinheiten gemäß Option (a), (b) oder (c) in 2.2.1.1.1 verwendet, muss die berichtspflichtige Geschäftseinheit auch den Gesamtumsatz aller unwesentlichen Geschäftseinheiten mit Sitz in dem Steuerhoheitsgebiet gemäß der Definition im Dokument „Safe Harbours and Penalty Relief“ für das laufende Geschäftsjahr, das erste vorangegangene Geschäftsjahr (falls zutreffend) und das zweite vorangegangene Geschäftsjahr (falls zutreffend) sowie den Durchschnitt der drei Geschäftsjahre melden. Das Element „Average“ gibt den Durchschnitt der drei Geschäftsjahre an (falls zutreffend).
Das Element „TotalRevenue“ spiegelt den Gesamtumsatz für den Durchschnitt der drei Geschäftsjahre wider (sofern zutreffend). Wenn die vereinfachte Berechnung für unwesentliche Geschäftseinheiten gemäß Option (a), (b) oder (c) in 2.2.1.1.1 verwendet wird, muss die berichtspflichtige Geschäftseinheit auch den Gesamtumsatz, wie im Dokument „Safe Harbours and Penalty Relief“ definiert, aller unwesentlichen Geschäftseinheiten mit Sitz in dem Steuerhoheitsgebiet für das laufende Geschäftsjahr, das erste vorangegangene Geschäftsjahr (sofern zutreffend) und das zweite vorangegangene Geschäftsjahr (sofern zutreffend) sowie den Durchschnitt der drei Geschäftsjahre melden.
Das Element „ID“ definiert die Identifikationsinformationen, die in das GIR-XMLSchema in Bezug auf Geschäftseinheiten, Joint-Ventures, JV-Tochtergesellschaften und obersten Muttergesellschaften (UPEs) aufgenommen werden sollen. Das Element <globe:ID_Type> wird im gesamten Schema verwendet und ist unter Komplexe_Datentype DAC9 vollständig dargestellt.
Das Element „Election“ spiegelt die angewandten Regelungen des Steuerhoheitsgebiets wider (d. h. Wahlen, die für alle in einem Steuerhoheitsgebiet ansässigen Geschäftseinheiten (oder Mitglieder einer JV-Gruppe) gelten). Dieses Element und jedes Unterelement unter dem übergeordneten Element sind optional. Das Element „Art. 3.2.6“ weist auf die Anwendung der Wahlmöglichkeit zum Gesamtveräußerunsgewinn hin.
Das Element „Art. 4.1.5“ weist auf die Anwendung des negativen Steuervortrags hin. Das Element „Art. 4.6.1“ weist auf die Anwendung der Wahlmöglichkeit zur unwesentlichen Verringerung der erfassten Steuern hin. Das Element „Art. 5.3.1“ weist auf die Wahl hin, den substanzbasierten Freibetrag nicht anzuwenden. Das Element „Art.3.2.2“ weist auf die Anwendung der Wahlmöglichkeit für aktienbasierte Vergütung hin. Da es sich um eine Wahlmöglichkeit mit einer Laufzeit von fünf Jahren handelt, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht (engl. GIR) und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben. Das Element „Art.3.2.5“ weist auf die Anwendung der Wahl nach dem Realisationsprinzip hin. Da es sich um eine Fünfjahreswahl handelt, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht (engl. GIR) und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben. Das Element „Art.3.2.8“ weist auf die Anwendung der Wahlmöglichkeit für gruppeninterne Transaktionen hin. Da es sich um eine Fünfjahreswahlmöglichkeit handelt, besteht sie aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht (engl. GIR) und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben.

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:NoDefTaxAllocation
globe:Status globe:ElectionYear

globe:RevocationYear

globe:Art4.5 globe:Status globe:ElectionYear
globe:RevocationYear

globe:Art3.2.1.c globe:Status globe:ElectionYear
globe:RevocationYear
globe:QualOwnerIntentBalance globe:Additions
globe:Reductions
globe:OutstandingBalance globe:SimplifiedReporting

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B Format Min Max Datentyp

0..1 O

1P

b

0..1 P

d

1

1 xsd:boolean

xsd:date

0..1 O

d

xsd:date

1O

1P

b

0..1 P

d

0..1 O

d

1

1 xsd:boolean

xsd:date

xsd:date

1O

1P

b

1P

d

0..1 O

d

1P

n

1P

n

1P

n

1P

n

0..1 O

b

1

1 xsd:boolean

xsd:date

xsd:date

xsd:integer xsd:integer

xsd:integer

xsd:integer

1

1 xsd:boolean

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung Grenzüberschreitende latente Steuern Status Wahljahr
Widerrufsjahr
Artikel 4.5 Status Wahljahr
Widerrufsjahr

Wertemenge / Erklärung (deut.)
Das Element „NoDefTaxAllocation“ gibt die Anwendung der Wahlmöglichkeit zur Nichtzuweisung grenzüberschreitender latenter Steuern an. Da es sich um eine Wahlmöglichkeit mit einer Laufzeit von fünf Jahren handelt, besteht es aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht (engl. GIR) und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben. Das Element „Art. 4.5.“ weist auf die Anwendung der GloBE-Verlustwahl hin. Diese Wahl kann nur mit dem ersten globalen Mindeststeuer-Bericht getroffen werden, die das Steuerhoheitsgebiet enthält, für den die Wahl getroffen wird. Wird die Wahl später widerrufen, kann die berichtspflichtige Geschäftseinheit keine neue Wahl für dasselbe Steuerhoheitsgebiet treffen. Sie besteht aus den Elementen „Status“, „Election Year“ und „Revocation Year“. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in den für das Widerrufsjahr eingereichten globalen Mindeststeuer-Berichten und in den globalen Mindeststeuer-Berichten für alle auf das Widerrufsjahr folgenden Geschäftsjahre angeben.

Artikel 3.2.1.c Status Wahljahr
Widerrufsjahr

Das Element „Art. 3.2.1c“ kennzeichnet die Anwendung der Wahlmöglichkeit zur Einbeziehung von Beteiligungskapital. Da es sich um eine fünfjährige Wahlmöglichkeit handelt, umfasst sie die Elemente „Status“, „Election Year“ und „Revocation Year“. Sie umfasst außerdem die Elemente „QualOwnerIntentBalance“, „Additions“, „Reductions“ und „Outstanding Balance“, die die Einbeziehung von Beteiligungskapitalgewinnen oder -verlusten im Rahmen der Wahlmöglichkeit zur Einbeziehung von Beteiligungskapital kennzeichnen. Das Element „Status“ ist ein Boolescher Wert mit dem akzeptierten Eingabetyp „True“ oder „False“. Wenn „True“, müssen die Elemente „ElectionYear“ und „RevocationYear“ ausgefüllt werden. Das Element „Election Year“ gibt das Wahljahr an. Das Element „Revocation Year“ gibt das Jahr an, in dem die Wahl widerrufen wurde (falls zutreffend). Die berichtspflichtige Geschäftseinheit muss das Widerrufsjahr in dem für das Widerrufsjahr eingereichten globalen Mindeststeuer-Bericht und in den globalen Mindeststeuer-Berichten für die vier auf das Widerrufsjahr folgenden Geschäftsjahre angeben.

Eigentümer Investitionssaldo qualifizierter Eigentumsanteile aus früheren Jahren

Das Element „QualOwnerIntentBalance“ gibt den Saldo der Investition des Eigentümers in eine qualifizierte Beteiligung aus den Vorjahren an, d. h. den verbleibenden Betrag der Investition des Eigentümers in eine qualifizierte Beteiligung für das Steuerhoheitsgebiet, der nicht durch Einnahmen verringert wurde.

Erhöhungen Minderungen Ausstehender Saldo Vereinfachte Berichterstattung

Das Element „Additions“ gibt die Erhöhung der Investition des Eigentümers in eine qualifizierte Beteiligung für das Berichtsgeschäftsjahr für das Steuerhoheitsgebiet an. Das Element „Reducations“ gibt die Verringerung der Investition des Eigentümers in eine qualifizierte Beteiligung für das Berichtsgeschäftsjahr für das Steuerhoheitsgebiet gemäß den entsprechenden Verwaltungsleitlinien an. Die Minderung darf die Investition des Eigentümers nicht übersteigen und dazu führen, dass die Investition unter Null fällt. Das Element „Outstanding Balance“ gibt den ausstehenden Saldo der Investition des Eigentümers in eine qualifizierte Beteiligung an, d. h. die Summe des Saldos aus den Vorjahren und der Zugänge zu der Investition des Eigentümers in eine qualifizierte Beteiligung nach Abzug der Einnahmen in Bezug auf die qualifizierte Beteiligung für das Berichtsgeschäftsjahr. Das Element „Simplified Reporting“ gibt an, dass die Informationen in Bezug auf das Steuerhoheitsgebeit der vereinfachten Berichterstattung unterliegen. Als boolesches Element sind die akzeptierten Eingabetypen True oder False.

Seite 35 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:InitialIntActivity
globe:StartDate globe:ReferenceJurisdiction
globe:ResCountryCode globe:TangibleAssetValue globe:OtherJurisdiction
globe:ResCountryCode

globe:TangibleAssetValue globe:RFYNumberOfJurisdictions

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O

globe:InitialIntActivityType

1P

d

1P

1P

en

1P

n

xsd:date

2

2 iso:countrycode_Type

xsd:integer

1..n P

1P

en

iso:countrycode_type

1P

n

0..1 O

n

xsd:integer xsd:integer

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Erste internationale Aktivität
Start-Datum Referenzsteuerhoheitsgebiet Steuerhoheitsgebiet Nettobuchwert materielle Vermögenswerte Anderes Steuerhoheitsgebiet

Wertemenge / Erklärung (deut.)
Das Element „InitialIntActivity“ zeigt an, dass sich der multinationale Unternehmensgruppe in der Anfangsphase der internationalen Tätigkeit befindet, wodurch die Ergänzungssteuer für die Zwecke der Sekundärergänzungssteuerregelung der multinationalen Unternehmensgruppe auf Null reduziert wird.
Es besteht aus mehreren Elementen, die belegen, dass die multinationale Unternehmensgruppe für den Ausschluss in Frage kommt. Wenn Artikel 9.3 Anwendung findet und keine Einheit der Gruppe ein anerkannte Primärergänzungssteuerregelung (engl- QIIR) anwenden muss, braucht die berichtspflichtige Geschäftseinheit die Abschnitte 2.1, 2.2 oder 3 für die betreffenden Steuerhoheitsgebiete, für die die Ergänzungssteuer gemäß Artikel 9.3 auf Null reduziert wird, nicht auszufüllen. Das Element „StartDate“ gibt den ersten Tag des ersten Geschäftsjahres an, in dem die multinationale Unternehmensgruppe ursprünglich in den Anwendungsbereich der GOBE-Regeln fiel. Artikel 9.3 gilt nicht für Geschäftsjahre, die später als fünf Jahre nach dem ersten Tag des unter 2.3.1 angegebenen Geschäftsjahres beginnen. Für multinationale Unternehmensgruppen, die zum Zeitpunkt des Inkrafttretens der GloBE-Regeln in deren Anwendungsbereich fallen, wird das in 2.3.1 angegebene Datum durch das Datum des Inkrafttretens der Sekundärergänzungssteuer-Regeln ersetzt. Das Element „Reference Jurisdiction“ gibt das in Artikel 9.3.3 definierte Referenzsteuerhoheitsgebiet an. Es besteht aus den Elementen „ResCountryCode“ und „Tangible Asset Value“.
Das Element „ResCountryCode“ gibt den zweistelligen alphabetischen Ländercode auf der Grundlage des ISO 3166-1 Alpha 2-Standards des Steuerhoheitsgebiets an. Das Element „Tangible Asset Value“ gibt die Nettobuchwerte der materiellen Vermögenswerte aller im Steuerhoheitsgebiet ansässigen Geschäftseinheiten für das Geschäftsjahr an, in dem die multinationale Gruppe ursprünglich in den Anwendungsbereich der GOBE-Regeln fällt. Das wiederholbare Element „Other Jurisdiction“ enthält Informationen über die Nettobuchwerte der materiellen Vermögenswerte von Geschäftseinheiten, die außerhalb des Referenzsteuerhoheitsgebiet ansässig sind, für das Geschäftsjahr, in dem die multinationale Gruppe ursprünglich in den Anwendungsbereich der GloBERegeln fällt. Es setzt sich aus den Elementen „ResCountryCode“ und „Tangible Asset Value“ zusammen.

Steuerhoheitsgebiet

Das Element „ResCountryCode“ gibt den zweistelligen alphabetischen Ländercode auf der Grundlage des ISO 3166-1 Alpha 2-Standards für jedes Steuerhoheitsgebiet, außer dem Referenzsteuerhoheitsgebiet an, in dem die Geschäftseinheiten für das Geschäftsjahr ansässig sind, in dem die multinationale Gruppe ursprünglich in den Anwendungsbereich der GloBE-Regeln fällt. Die Anzahl der Steuerhoheitsgebiete, die nicht das Referenzgebiet sind, beträgt bis zu fünf. Der Standort von Joint Ventures und Joint-Venture-Tochtergesellschaften oder Investmenteinheiten, bei denen es sich nicht um ausgeschlossene Einheiten handelt, wird bei der Bestimmung der Anzahl der Steuerhoheitsgebiete, in denen die multinationale Unternehmensgruppe über Geschäftseinheiten verfügt, nicht mitberücksichtigt.

Nettobuchwert materielle Vermögenswerte

Das Element „Tangible Asset Value“ gibt den Nettobuchwert der materiellen Vermögenswerte aller Geschäftseinheiten an, die in einem anderen Steuerhoheitsgebiet als dem Referenzsteuerhoheitsgebiet ansässig sind, und zwar für das Geschäftsjahr, in dem die multinationale Unternehmensgruppe ursprünglich in den Anwendungsbereich der GOBE-Regeln fiel. Materielle Vermögenswerte von staatenlosen Geschäftseinheiten gelten als von Geschäftseinheiten gehalten, die in einem anderen Steuerhoheitsgebiet als dem Referenzsteuerhoheitsgebiet ansässig sind, es sei denn, die multinationale Unternehmensgruppe weist nach, dass sich diese materiellen Vermögenswerte physisch im Referenzsteuerhoheitsgebiet befinden. Materielle Vermögenswerte von Joint Ventures und Joint-VentureTochtergesellschaften oder Investmenteinheiten, die keine ausgeschlossenen Einheiten sind, werden bei der Ermittlung der Summe der Nettobuchwerte der materiellen Vermögenswerte aller Geschäftseinheiten, die in einem anderen Steuerhoheitsgebiet als dem Referenzsteuerhoheitsgebiet ansässig sind, nicht berücksichtigt.

Das Element „RFYNumberOfJurisdictions“ gibt die Anzahl der Steuerhoheitsgebiete

an, in denen die multinationale Unternehmensgruppe während des

Berichtsgeschäftsjahres Geschäftseinheiten hat. Handelt es sich bei dem

Berichtsgeschäftsjahr um das Geschäftsjahr, in dem die multinationale

Unternehmensgruppe ursprünglich in den Anwendungsbereich der GOBE-Regeln

Anzahl der Steuerhoheitsgebiete fällt, ist diese Information nicht zu melden, da sie aus den Informationen abgeleitet

im Berichtsgeschäftsjahr

werden kann, die unter dem Element „OtherJurisdiction" gemeldet werden.

Seite 36 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:RFYSumTangibleAssetValue
globe:LowTaxJurisdiction globe:TopUpTaxAmount globe:LTCE
globe:TIN
globe:IIR globe:NetGlobeIncome globe:TopUpTax globe:ParentEntity
globe:TIN
globe:ResCountryCode globe:OtherOwnershipAllocation globe:InclusionRatio globe.TopUpTaxShare
globe:IIROffSet globe:TopUpTax globe:UTPR globe:UTPRSafeHarbour globe:CITRate globe:UTPRCalculation

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

0..1 O

n

xsd:integer

0..1 O

1P

n

0..n O

globe:LowTaxJurisdictionType xsd:integer

1P

an

1 200 globe:TIN_type

1..n P

0..1 O

n

1P

n

0..n O

xsd:integer xsd:integer

1P

an

1 200 globe:TIN_Type

1P

en

1P

n

1P

n

1P

n

2

2 iso:CountryCode_Type

xsd:integer

6

6 globe:percentage

xsd:integer

1P

n

1P

n

0..1 O 1B

1B

n

1P

xsd:integer xsd:integer

6

6 globe:percentage

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)

Summe materielle Vermögenswerte im Berichtsgeschäftsjahr
Niedrigsteuerhoheitsgebiet Gesamtbetrag Steuererhöhungsbeträge

Das Element „RFYSumTangibleAssetValue“ gibt die Summe der Nettobuchwerte der materiellen Vermögenswerte aller Geschäftseinheiten an, die während des Berichtsgeschäftsjahres in anderen Steuerhoheitsgebieten als dem Referenzsteuerhoheitsgebiet ansässig waren. Handelt es sich bei dem Berichtsgeschäftsjahr um das Geschäftsjahr, in dem die multinationale Unternehmensgruppe ursprünglich in den Anwendungsbereich der GloBE-Regeln fiel, ist diese Information nicht zu melden, da sie aus den Informationen abgeleitet werden kann, die unter dem/den Element(en) „OtherJurisdiction“ gemeldet werden.
Dieses Element gibt für jedes Niedrigsteuerhoheitsgebiet den Betrag der zu zahlenden Ergänzungssteuer für jede niedrig besteuerte Geschäftseinheit (engl. lowtaxed Constituent Entity - LTCE) (oder Mitglied einer JV-Gruppe) an, für die eine anerkannte Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule QIIR) gilt, und identifiziert den zurechenbaren Anteil der Ergänzungssteuer jeder Muttergesellschaft. Es enthält außerdem weitere Details zur Berechnung des Betrags der Sekundärergänzungssteuerregelung (engl. Undertaxed Profit Rule - UTPR), sofern vorhanden. Es besteht aus den Elementen „TopUpTaxAmount“, „LTCE“ und „UTPR“. Das Element „TopUpTaxAmount“ spiegelt den Gesamtbetrag der Steuererhöhungsbeträge in Bezug auf das Niedrigsteuerhoheitsgebiet wider.

Unwesentliche Geschäftseinheit

Das Element „TIN“ gibt die Steueridentifikationsnummer (engl. tax identification number - TIN) der niedrig besteuerten Geschäftseinheit (engl. low-taxed Constituent Entity - LTCE) oder einem Mitglied der JV-Gruppe an.

Steueridentifikationsnummer Das Element ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen.

Das wiederholbare Element „IIR“ gibt den Steuerhöhungsbetrag an, der für jede

niedrig besteuerte Geschäftseinheit (oder Mitglied einer JV-Gruppe) zu zahlen ist, für

Primärergänzungssteuerregelun das eine anerkannte Primärergänzungssteuerregelung (engl. QIIR) gilt, und

g

identifiziert den zurechenbaren Anteil der Ergänzungssteuer jeder Muttergesellschaft.

Das Element „GlobeIncome“ spiegelt die GloBE-Einkünfte der niedrig besteuerten

Netto GloBE-Einkünfte

Geschäftseinheit oder Mitglieds der JV-Gruppe wider.

Das Element „TopUpTax“ gibt die Ergänzungssteuer der niedrig besteuerten

Ergänzungssteuer

Geschäftseinheit oder des Mitglieds der JV-Gruppe an.

Muttergesellschaft

Steueridentifikationsnummer Ansässigkeitsstaat

Das optionale (obligatorische) Element „TIN“ identifiziert die Steueridentifikationsnummer (engl. TIN) (oder, falls keine TIN verfügbar ist, ein funktionales Äquivalent, z. B. eine Handelsregisternummer) der Muttergesellschaft. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen. Das Element „ResCountryCode“ gibt die Steuerhoheitsgebiete in Form eines zweistelligen alphabetischen Ländercodes gemäß ISO 3166-1 Alpha 2 an, in denen Muttergesellschaften der multinationalen Unternehmensgruppe eine anerkannte Primärergänzungssteuerregelung (engl. QIIR) anwenden müssen. Bei Anwendung von Art. 10.3.5 muss die berichtspflichtige Geschäftseinheit das Steuerhoheitsgebiet angeben, in dem die Muttergesellschaft ihre Primärergänzungssteuerregelung anwenden muss.

Eigentumsanteile von nicht Muttergesellschaften

Das Element „OtherOwnershipAllocation“ gibt an, dass die Höhe des GloBEGewinns, das auf Eigentumsanteile entfällt, die von anderen Eigentümern als der jeweiligen Muttergesellschaft gehalten werden, gemäß Artikel 2.2.3 bestimmt wird.

Einbeziehungsquote Zuzurechnende Anteil am Steuererhöhungsbetrag

Das Element „InclusionRatio“ gibt die Einbeziehungsquote der Muttergesellschaft an. Das Element „TopUpTaxShare“ gibt den der Muttergesellschaft zurechenbaren Anteil am Steuererhöhungsbetrag an.

IIROffSet Ergänzungssteuer SekundärergänzungssteuerRegelung UTPR Safe-Harbour
Körperschaftssteuersatz UTPR Berechnung

Das Element „IIROffSet“ gibt an, dass der IIR-Offset der Betrag des Steuererhöhungsbetrags ist, der im Rahmen einer anerkannten Primärergänzungssteuerregelung (engl. QIIR) von einer in Teileigentum stehenden Muttergesellschaft (engl. POPE)oder einer zwischengeschalteten Muttergesellschaft erhoben wird, die sich auf einer niedrigeren Ebene der Eigentümerkette befindet. Das Element „TopUpTax“ gibt die von der Muttergesellschaft zu zahlende Ergänzungssteuer an. Das Element „UTPR“ spiegelt den gesamten Steuererhöhungsbetrag nach der Sekundärergänzungssteuer-Regelung (engl. Undertaxed Profits Rule - UTPR) in Bezug auf das Steuerhoheitsgebiet wider. Das Element „UTPRSafeHarbour“ spiegelt die Anwendung des vorübergehenden UTPR Safe-Harbours wider. Das Element „CITRate“ spiegelt den Körperschaftsteuersatz des Steuerhoheitsgebiets der obersten Muttergesellschaft gemäß dem vereinbarten Safe Harbor wider.

Seite 37 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:TotalUTPRTopUpTax globe:Article2.5.1TopUpTax globe:AdditionalDataPoint globe:DocSpec globe:UTPRAttribution
globe:RecJurCode globe:Attribution
globe:ResCountryCode
globe:UTPRTopUpTaxCarryForward globe:Employees globe:TangibleAssetValue

globe:UTPRPercentage

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema
Kardinalität P O B Format Min Max Datentyp

1P

n

1P

n

0..n O

1P 0..n O

xsd:integer xsd:integer
globe:AdditionalDataPointType
stf:docspec_type globe:UTPRAttributionType

1..n P

en

1..n P

1P

en

2

2 iso:countrycode_Type

2

2 iso:CountryCode_Type

1P

n

0..1 O

n

0..1 O

n

xsd:integer xsd:integer xsd:integer

1P

n

1

6 globe:percentage

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung

Wertemenge / Erklärung (deut.)
Das Element „TotalUTPRTopUpTax“ gibt den Gesamtbetrag der Sekundärergänzungssteuer für das Steuerhoheitsgebiet an.

Gesamtbetrag Sekundärergänzungssteuer Artikel 2.5.1 Ergänzungssteuer
Zusätzlicher Datenpunkt

Die Summe aller in Abschnitt 3.4.2.2 (Ergänzungssteuer gemäß Artikel 2.5.1) angegebenen Beträge ist für jeden niedrig besteuerte Geschöftseinheit und jedes Mitglied einer JV-Gruppe in einem Niedrigsteuerhoheitsgebiet sowie für jede staatenlose Geschäftseinheit mit einem in Abschnitt 3.4.2.2 angegebenen Betrag anzugeben. Gilt für eine niedrig besteuerte Geschäftseinheit (oder ein Mitglied einer JV-Gruppe), für den die Ergänzungssteuer berechnet wird, keine anerkannte Primärergänzungssteuer-Regeglung (engl. QIIR), wird als Ergänzungssteuer gemäß Artikel 2.5.1 die berechnete Ergänzungssteuer des Steuerhoheitsgebiets berücksichtigt. Das Element „Article2.5.1TopUpTax“ spiegelt die für Artikel 2.5.1 berücksichtigte Ergänzungssteuer wider. Das wiederholbare Element „AdditionalDataPoint“ besteht aus den Elementen „Description“, „Amount“, „Percentage“ und „Text “. Jedes Element und die zugehörigen Werte sind unter dem Komplexdatentyp globe:AdditionalDataPointType aufgeführt

Dokumentenspezifikation UTPR-Zuordnung

DocSpec identifiziert den jeweiligen Bericht innerhalb der übermittelten GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die korrigiert werden müssen (weitere Hinweise, siehe stf:DocSpec_Type unter Komplexe Datentypen). Dieser wiederholbare Abschnitt enthält Informationen zur Zuordnung der Aufstockungssteuer zu den relevanten Gerichtsbarkeiten, falls die UTPR anwendbar ist.

Das wiederholbare Element „RecJurCode“ gibt die relevanten Empfängersteuerhoheitsgebiete des Abschnitts „UTPRAttribution“ für den Informationsaustausch an. Beabsichtigt die multinationale Unternehmensgruppe, den globalen Mindeststeuer-Bericht (engl. GIR) lokal einzureichen, muss der nationale Code des Steuerhoheitsgebiet in das Element eingetragen werden.

Empfängerstaaten-Code

Die berichtspflichtige Geschäftseinheit muss die Steuerhoheitsgebiete angeben, in denen die Berichtspflichten der Geschäftseinheiten durch Informationsaustausch gemäß Artikel 8.1.2 erfüllt werden sollen.

Zuordnung Ansässigkeitsstaat

Das wiederholbare Element „Zuordnung“ gibt die Zuordnung der Ergänzungssteuer gemäß der Sekundärergänzungssteuer-Regelung (engl. UTPR) an. Das Element „ResCountryCode“ identifiziert die UTPR-Steuerhoheitsgebiete der multinationalen Unternehmensgruppe in Form eines zweistelligen alphabetischen Ländercodes basierend auf dem Standard ISO 3166-1 Alpha 2.

SekundärergänzungssteuerVortrag
Beschäftigte
Buchwert materieller Vermögenswerte

Das Element „UTPRTopUpTaxCarryForward“ gibt an, dass, wenn der einem Steuerhoheitsgebiet im vorherigen Geschäftsjahr zugewiesene Sekundärergänzungssteuerbetrag noch nicht zu einem entsprechenden zusätzlichen Steueraufwand für die in diesem Steuerhoheitsgebiet ansässigen Geschäftseinheiten geführt hat, der gemäß Artikel 2.4.2 vorzutragende Betrag in 3.4.3.2 anzugeben ist. Das Element „Employees“ gibt an, wie viele Beschäftigte einer Betriebsstätte (einschließlich derjenigen von transparenten Einheiten) bei der Berechnung des Sekundärergänzungssteuer-Prozentsatzes des Steuerhoheitsgebiets berücksichtigt werden, in dem sich diese Betriebsstätten befinden. Das Element „TangibleAssetValue“ gibt an, dass der Nettobuchwert der den Betriebsstätten zugewiesenen materiellen Vermögenswerten (einschließlich jener von transparenten Einheiten) bei der Berechnung des SekundärergänzungssteuerProzentsatzes des Steuerhoheitsgebiets berücksichtigt werden soll, in der sich diese Betriebsstätten befinden.

SekundärergänzungssteuerProzentsatz

Das Element „UTPRPercentage“ gibt an, dass, wenn der SekundärergänzungssteuerProzentsatz in 3.4.3.5 für ein Sekundärergänzungssteuer-Steuerhoheitsgebiet aufgrund der Anwendung von Artikel 2.6.3 null ist, die Anzahl der Beschäftigten und die materiellen Vermögenswerte der im Steuerhoheitsgebiet ansässigen Geschäftseinheiten von der Gesamtsumme (d. h. dem Nenner der Formel für Zwecke des Verteilungsschlüssels) ausgeschlossen werden. Dieser Ausschluss von der Gesamtsumme (und dem Nenner) gilt nicht, wenn alle Sekundärergänzungssteuer-Steuerhoheitsgebiete im Berichtsgeschäftsjahr einen Sekundärergänzungssteuer-Prozentsatz von null aufweisen (Artikel 2.6.4).
Der Sekundärergänzungssteuer-Prozentsatz wird gemäß Artikel 2.6.1 berechnet. Liegt für ein Sekundärergänzungssteuer-Steuerhoheitsgebiet gemäß 3.4.3.2 ein Sekundärergänzungssteuervortrag vor, beträgt der SekundärergänzungssteuerProzentsatz dieses Steuerhoheitsgebiets null (Artikel 2.6.3), es sei denn, alle Sekundärergänzungssteuer-Steuerhoheitsgebiete weisen im Berichtsjahr einen Sekundärergänzungssteuer-Prozentsatz von null auf (Artikel 2.6.4). Der in dieser Spalte angegebene Sekundärergänzungssteuer-Prozentsatz entspricht dem nach Anwendung von Artikel 2.6.4 berechneten Sekundärergänzungssteuer-Prozentsatz.

Seite 38 von 64

Bundeszentralamt für Steuern

PILLAR II - GIR Nutzdaten

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12 L13

L14

L15

globe:UTPRTopUpTaxAttributed

globe:AddCashTaxExpense

globe:UTPRTopUpTaxCarriedForward globe:AdditionalDataPoint globe:DocSpec

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B Format Min Max Datentyp

1P

n

xsd:integer

1P

n

xsd:integer

1P 0..n O
1P

globe:AdditionalDataPointType stf:docspec_type

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Sekundärergänzungssteuer Zurechnung
Zusätzlicher steuerlicher Zahlungsaufwand
Vorgetragene Sekundärergänzungssteuer
Zusätzlicher Datenpunkt Dokumentenspezifikation

Wertemenge / Erklärung (deut.)
Das Element „UTPRTopUpTaxAttributed“ gibt an, dass der gesamte Sekundärergänzungssteuerbetrag, der den Sekundärergänzungssteuerhoheitsgebieten zuzurechnen ist, die Summe aller gesamten Sekundärergänzungssteuerbeträge für jedes in Tabelle 3.4.3 angegebene Steuerhoheitsgebiet ist. Das Element „AddCashTaxExpense“ spiegelt wider, dass der zusätzliche steuerliche Zahlungsaufwand, die den Geschäftseinheiten in dem Sekundärergänzungssteuerhoheitsgebiet entstehen, der Betrag der gemäß Sekundärergänzungssteuer-Regelung fälligen Steuer zusätzlich zu dem Steuerbetrag ist, der ansonsten gemäß den normalen Steuervorschriften zu zahlen wäre. Das Element „UTPRTopUpTaxCarriedForward“ gibt an, dass die verbleibende Sekundärergänzungssteuer, die übertragen werden kann, die positive Differenz zwischen dem dem Sekundärergänzungs-Steuerhoheitsgebiet für das Berichtsgeschäftsjahr zugeschriebenen Sekundärergänzungssteuer-Betrag und den zusätzlichen steuerlichen Zahlungsaufwand ist, die den Geschäftseinheiten in dem Sekundärergänzungs-Steuerhoheitsgebiet entstanden sind und in 3.4.3.7 gemeldet wurden. Das wiederholbare Element „AdditionalDataPoint“ besteht aus den Elementen „Description“, „Amount“, „Percentage“ und „Text “. Jedes Element und die zugehörigen Werte sind unter dem Komplexdatentyp globe:AdditionalDataPointType aufgeführt
DocSpec identifiziert den jeweiligen Bericht innerhalb der übermittelten GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die korrigiert werden müssen (weitere Hinweise, siehe stf:DocSpec_Type unter Komplexe Datentypen).

Seite 39 von 64

Bundeszentralamt für Steuern
Komplexe Datentypen
globe:ID_Type globe:Name globe:ResCountryCode globe:TIN
globe:Rules
globe:GlobeStatus globe:ExcludedUPE ID_Type
globe:Name globe:ResCountryCode globe:TIN
globe:Rules

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B For-mat Min Max Datentyp

Deutsche Bezeichnung

1

P

an

1 200 stf:StringMin1Max200_Type

Name

1..n P

en

1..n P

an

2 2 iso:CountryCode_Type 1 200 globe:TIN_Type

Ansässigkeitsstaat

1..n P

en

globe:IDTypeRules_EnumType

Ergänzungssteuerregelung

1..n P

en

globe:IDTypeGloBEStatus_EnumType Status

1

P

an

1 200 stf:StringMin1Max200_Type

Name

0..n O

en

1..n P

an

2 2 iso:CountryCode_Type 1 200 globe:TIN_Type

Ansässigkeitsstaat Steueridentifikationsnummer

0..n O

en

globe:IDTypeRules_EnumType

Ergänzungssteuerregelung

GIR-XML-Schema v1.0 28.07.2025
Wertemenge / Erklärung (deut.) Der ID-Typ definiert die identifizierenden Informationen, die in das GIR-XML-Schema in Bezug auf Geschäftseinheiten, JVs und JV-Tochtergesellschaften aufgenommen werden. Er wird an mehreren Stellen im GIR-XML-Schema verwendet und folgt immer der unten stehenden Struktur. Es besteht aus den folgenden Elementen (einschließlich des TIN-Typs), die weiter unten näher erläutert werden. Das Element „Name“ gibt den vollständigen rechtlichen Namen der Geschäftseinheiten, des Joint Ventures und der JV-Tochtergesellschaft an. Das wiederholbare Element „ResCountryCode“ gibt den/die Ländercode(s) des Steuerhoheitsgebiets an, in dem die Geschäftseinheit (außer der obersten Muttergesellschaft), das Joint Venture oder die Tochtergesellschaft des Joint Ventures für GloBE-Zwecke ansässig ist. Der ResCountryCode basiert auf der ISO 3166-1-Länderliste, die durch den X5 Code für staatenlose Geschäftseinheiten ergänzt wird. Der TIN-Typ ist gemäß dem Komplexdatentyp globe:TIN_Type auszufüllen. Das Element „Rules“ gibt an, ob das Steuerhoheitsgebiet der Geschäftseinheit für das Berichtsgeschäftsjahr eine anerkannte Primär-, Sekundär- oder nationale Ergänzungssteuerregelung (engl. QIIR, QUTPR, QDMTT) in Kraft hat. Die möglichen Werte sind: siehe globe:IDTypeRules_EnumType (GIR201 - GIR205) unter Wertelisten für Aufzählungstypen Wenn mehr als eine Option relevant ist, müssen alle relevanten Optionen ausgewählt werden.
Das wiederholbare Element „Globe Status“ gibt den Status der Geschäftseinheit für GloBE-Zwecke an. Die möglichen Werte sind: siehe globe:IDTypeGloBEStatus_EnumType (GIR301 - GIR318) unter Wertelisten für Aufzählungstypen
Wenn mehr als eine Option relevant ist, müssen alle relevanten Optionen ausgewählt werden. Die meldende Geschäftseinheit muss das Element ID separat für die Eigentümer der Geschäftseinheit (falls vorhanden) ausfüllen, für die der Status der Geschäftseinheit, des JV oder der JV-Tochtergesellschaft von dem im Element GloBE Status angegebenen Status abweicht (z. B. Wenn eine transparente Einheit von einem der Eigentümer der Geschäftseinheit als steuerlich transparente Einheit und vom anderen als umgekehrt hybride Einheit behandelt wird, muss die meldende Geschäftseinheit die Tabelle für dieselbe transparente Einheit zweimal ausfüllen: einmal in Bezug auf den Eigentümer, der die transparente Einheit als steuerlich transparentes Einheit behandelt, und ein weiteres Mal in Bezug auf den Eigentümer, der sie als umgekehrt hybride Einheit behandelt).
Der Typ „UPE ID“ definiert die identifizierenden Informationen, die in das GIR-XMLSchema in Bezug auf oberste Muttergesellschaften (engl. Ultimate Parent Entities UPEs) aufgenommen werden. Er wird an mehreren Stellen innerhalb des GIR-XMLSchemas verwendet und folgt immer der nachstehenden Struktur. Das Element „Name“ gibt den vollständigen rechtlichen Namen der UPE an.
Das wiederholbare Element „ResCountryCode“ gibt den/die Ländercode(s) des Steuerhoheitsgebiets an, in dem die UPE für GloBE-Zwecke ansässig ist. Diese Information muss nicht für UPEs angegeben werden, die ausgeschlossene Einheiten sind. Der ResCountryCode basiert auf der ISO 3166-1-Länderliste, die durch den X5 Code für staatenlose Einheiten ergänzt wird. Das Element „TIN“ folgt dem Komplexdatentyp globe:TIN_Type. Das Element „Rules“ gibt an, ob für das Steuerhoheitsgebiet der obersten Muttergesellscahft im Berichtsgeschäftsjahr eine anerkannte Primär-, Sekundärund/oder nationale Ergänzungssteuerregelung (engl. QIIR, QUTPR, QDMTT) in Kraft ist. Mögliche Werte sind: Siehe globe:IDTypeRules_EnumType (GIR201–GIR205) unter Wertelisten für Aufzählungstypen
Wenn mehr als eine Option relevant ist, müssen alle relevanten Optionen ausgewählt werden. Diese Information muss nicht für oberste Muttergesellschaften gemeldet werden, die als ausgeschlossene Einheiten gelten.

Seite 40 von 64

Bundeszentralamt für Steuern
Komplexe Datentypen
globe:GlobeStatus
globe:TIN_Type issuedBy unknown
TypeOfTIN
globe:AdditionalDataPointType globe:Description globe:Amount globe:Percentage globe:Text globe:Boolean
stf:DocSpec_Type

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B For-mat Min Max Datentyp

Deutsche Bezeichnung

1..n P

en

globe:IDTypeGloBEStatus_EnumType

0..1 O

en

0..1 O

b

2 2 iso:CountryCode_Type 1 1 xsd:Boolean

0..1 O

en

globe:TIN_EnumType

0..1 O

an

0..1 O 0..1 O

0..1 O

an

0..1 O

b

1 170 stf:StringMin1Max170_Type
xsd:integer 1 6 globe:percentage
1 4000 stf:StringMin1Max4000_Type 1 1 xsd:boolean

GIR-XML-Schema v1.0 28.07.2025
Wertemenge / Erklärung (deut.) Das wiederholbare Element „Globe Status“ zeigt den Status der obersten Muttergesellschaft für GloBE-Zwecke an. Die möglichen Werte sind: Siehe Globe:IDTypeGloBEStatus_EnumType (GIR301 - GIR318) unter Wertelisten für Aufzählungstypen
Der TIN-Typ gibt die Steueridentifikationsnummer der UPE, der Geschäftseinheit, des JV oder der JV-Tochtergesellschaft an, die für die Zwecke der erfassten Steuern in dem Land verwendet wird, in dem sie für GloBE-Zwecke ansässig ist, oder, wenn die Geschäftseinheit keine Steueridentifikationsnummer hat, ein funktionales Äquivalent, wie z. B. eine Geschäfts-/Firmenregisternummer. Zur Identifizierung von staatenlosen Geschäftseinheiten muss die meldende Geschäftseinheit das Steueridentifikationsmerkmal oder ihr funktionales Äquivalent angeben, das für die Zwecke der erfassten Steuern in dem Land verwendet wird, in dem die Geschäftseinheit gegründet wurde. Sie wird an mehreren Stellen im GIR-XML-Schema verwendet und folgt immer der unten stehenden Struktur. Der TIN-Typ gibt auch die TIN (falls vorhanden) an, die der UPE, der Geschäftseinheit, dem JV oder der JV-Tochtergesellschaft von dem Steuerhoheitsgebiet ausgestellt wurde, in der die Einreichung erfolgt (die „Einreichungshoheit“). Sie besteht aus den folgenden Elementen. Falls die Einheit keine TIN hat, ist der Wert NOTIN anzugeben. Dieses Attribut beschreibt das Steuerhoheitsgebiet, das die Steueridentifikationsnummer ausgestellt hat. Es sollte immer angegeben werden, es sei denn, das Element ist als „unbekannt“ gekennzeichnet.
Dieses Attribut kann als wahr „1“ angegeben werden, wenn die Steueridentifikationsnummer nicht existiert. Jeder Wert, der für eine als unbekannt gekennzeichnete Steueridentifikationsnummer angegeben wird, wird verworfen. Das Element TIN-Typ legt den Typ der angegebenen TIN oder der entsprechenden Nummer fest.
Mögliche Werte sind: siehe globe:TIN_EnumType (GIR3001 - GIR3004) unter Wertelisten für Aufzählungstypen
Das wiederholbare Element AdditionalDataPoint setzt sich aus den Elementen Description, Amount, Percentage und Text zusammen. Jedes Element und die entsprechenden Werte werden nachstehend beschrieben und sollten nur auf der Grundlage genehmigter staatlicher Leitlinien und gemäß den darin enthaltenen Anweisungen ausgefüllt werden. Das Beschreibungselement dient zur Beschreibung des zusätzlich bereitgestellten Datenpunkts. Das Element amount wird verwendet, wenn der zusätzliche Datenpunkt ein Betrag oder eine Zahl ist. Das Prozent-Element wird zur Angabe eines Prozentsatzes verwendet. Das Element text wird verwendet, wenn der zusätzliche Datenpunkt in einem Textformat bereitgestellt werden soll. Das Boolean Element wird verwendet, wenn der zusätzliche Datenpunkt eine wahre oder falsche Antwort erfordert.
DocSpec identifiziert den jeweiligen Bericht innerhalb der zu übermittelnden GIRNachricht. Es ermöglicht die Identifizierung von Berichten, die einer Korrektur bedürfen. Das DocSpec-Element setzt sich wie folgt zusammen:

Seite 41 von 64

Bundeszentralamt für Steuern
Komplexe Datentypen
stf:DocTypeIndic stf:DocRefId stf:CorrDocRefId

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

Kardinalität P O B For-mat Min Max Datentyp

Deutsche Bezeichnung

1

P

en

1

P

an

stf:OECDDocTypeIndic_EnumType 1 200 stf: StringMin1Max200_Type

0..1 O

an

0 200 stf: StringMin1Max200_Type

GIR-XML-Schema v1.0 28.07.2025
Wertemenge / Erklärung (deut.)
Eine Nachricht kann entweder neue Datensätze (OECD1) oder Berichtigungen und/oder Löschungen (OECD2 und OECD3) enthalten, sollte aber keine Mischung aus beidem enthalten. Die Option zum erneuten Senden (OECD0) kann nur für das Element Filing Info verwendet werden, wenn das Element Filing Info bereits gesendet wurde. Dieses Element gibt die Art der zu übermittelnden Daten an. Zulässige Einträge sind: siehe stf:OECDDocTypeIndic_EnumType (OECD0 - OECD13) unter Wertelisten für Aufzählungstypen Die Codes OECD10 bis OECD13 dürfen nur während vereinbarter Testzeiträume oder auf der Grundlage einer bilateralen Vereinbarung über Tests verwendet werden. Damit soll sichergestellt werden, dass die zuständigen Behörden vermeiden, dass Testdaten mit „echten“ Daten vermischt werden. Die DocRefID ist ein eindeutiger Bezeichner für das Dokument (d. h. einen Datensatz und alle seine untergeordneten Datenelemente). Ein Element, das eine Korrektur (oder Löschung) enthält, muss eine neue eindeutige DocRefID für zukünftige Referenzen haben. Die CorrDocRefID verweist auf die DocRefID des zu korrigierenden oder zu löschenden Elements. Sie muss sich immer auf die letzte Referenz der gesendeten Lieferung (DocRefID) beziehen. Die letzte Referenz der gesendeten Lieferung (DocRefID) muss Teil der letzten Nachricht sein, in der die Lieferung gesendet wurde. Auf diese Weise kann eine Reihe von Korrekturen oder Änderungen verarbeitet werden, da jede Korrektur die vorherige Version vollständig ersetzt.

Seite 42 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ stf:OECDDocTypeIndic_EnumType
globe:MessageTypeIndic_EnumType globe:IDTypeRules_EnumType
globe:IDTypeGloBEStatus_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert OECD0 OECD1 OECD2 OECD3 OECD10 OECD11 OECD12 OECD13
GIR101 GIR102
GIR103
GIR201
GIR202
GIR203
GIR204
GIR205
GIR301

Deutsche Bezeichnung
Erneut gesendete Daten Neue Daten Korrigierte Daten Löschung von Daten Erneut gesendete Testdaten Neue Testdaten Korrigierte Testdaten Löschung von Testdaten

Wertemenge / Erklärung
Resent Data New Data Corrected Data Deletion of Data Resent Test Data New Test Data Corrected Test Data Deletion of Test Data

Die Nach enthält ausschließlich neue

The message only contains new information

Informationen

Die Meldung enthält Korrekturen/Löschungen für The message contains corrections/deletions

zuvor übermittelte Informationen

for previously sent information

Die Mieldung weist darauf hin, dass keine meldepflichtigen Daten vorliegen

The message advises there is no data to report

Eine anerkannte

QIIR applicable to Low-Taxed Constituent

Primärergänzungssteuerregelung (engl. Qualified Entities located in other jurisdictions only

Income Inclusion Rule - QIIR) ist nur auf

niedrigbesteuerte Geschäftseinheiten in anderen

Jurisdiktionen anwendbar

Eine anerkannte

QIIR applicable to both Low-Taxed

Primärergänzungssteuerregelung (engl. Qualified Constituent Entities located in other

Income Inclusion Rule - QIIR) ist sowohl auf

jurisdictions and in the jurisdiction of the

niedrigbesteuerte Geschäftseinheiten in anderen Parent Entity

Jurisdiktionen und in der Jurisdiktion der

Muttergesellschaft anwendbar

Anerkannte Sekundärergänzungssteuerregelung QUTPR

(engl. Qualified Undertaxed Profit Rule - QUTPR)

Anerkannte nationale Ergänzungssteuer (engl. Qualified Domestic Minimum Top-up Tax QDMTT)
Nicht anwendbar

QDMTT Not applicable

Geschäftseinheit

Constituent Entity

Seite 43 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:FilingCERole_EnumType globe: FilingCECofUPE_EnumType globe:ExcludedUPE_EnumType

Wert GIR302
GIR303
GIR304 GIR305 GIR306 GIR307
GIR308
GIR309
GIR310 GIR311 GIR312 GIR313 GIR314 GIR315 GIR316 GIR317
GIR318
GIR401 GIR402 GIR403 GIR404 GIR405
GIR501 GIR502 GIR503 GIR504
GIR601

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung Transparente Einheit – steuerlich transparent

Wertemenge / Erklärung Flow-through Entity – Tax Transparent

Transparente Einheit – umgekehrt hybrid

Flow-through Entity – Reverse Hybrid

Hybride Einheit Betriebsstätte Stammhaus In Minderheitseigentum stehende Muttergesellschaft In Minderheitseigentum stehende Tochtergesellschaft
In Minderheitseigentum stehende Geschäftseinheit Investmenteinheit Versicherungsinvestmenteinheit Verbriefungseinheit Joint Venture (JV) JV-Tochtergesellschaft Unwesentliche Geschäftseinheit Ausgeschlossene Einheit Muttergesellschaft, die zur Anwendung einer anerkannten Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR) nach Artikel 10.3.5 verpflichtet ist Nicht zur Gruppe gehörende Einheit

Hybrid Entity Permanent Establishment Main Entity Minority-Owned Parent Entity
Minority-Owned Subsidiary
Minority-Owned Constituent Entity
Investment Entity Insurance Investment Entity Securitisation Entity Joint Venture (JV) JV Subsidiary Non-Material Constituent Entity Excluded Entity Parent Entity required to apply a QIIR under Article 10.3.5
Non-group Member

Oberste Muttergesellschaft Benannte meldende Geschäftseinheit Benannte lokale Geschäftseinheit Geschäftseinheit Andere

Ultimate Parent Entity Designated Filing Entity Designated Local Entity Constituent Entity Other

Buchstabe a Buchstabe b Buchstabe c Buchstabe d

subparagraph a subparagraph b subparagraph c subparagraph d

Staatliche Einheit

Governmental Entity

Seite 44 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ globe:IDGloBEStatus_EnumType
globe:OwnershipType_EnumType

Wert GIR602 GIR603 GIR604 GIR605
GIR606
GIR701 GIR702
GIR703
GIR704 GIR705 GIR706 GIR707
GIR708
GIR709
GIR710 GIR711 GIR712 GIR713 GIR714 GIR715 GIR716 GIR717 GIR718 GIR719 GIR720
GIR721
GIR801 GIR802

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Deutsche Bezeichnung
Internationale Organisation Organisation ohne Erwerbszweck Pensionseinheit Investmentvehikel, das die oberste Muttergesellschaft ist Immobilien-Investmentvehikel, das die oberste Muttergesellschaft ist

Wertemenge / Erklärung International Organisation Non-profit Organisation Pension fund Investment Fund that is the UPE
Real Estate Investment Vehicle that is the UPE

Geschäftseinheit Transparente Einheit – steuerlich transparent

Constituent Entity Flow-Through Entity – Tax Transparent

Transparente Einheit – umgekehrt hybrid

Flow-Through Entity – Reverse Hybrid

Hybride Einheit Betriebsstätte Stammhaus In Minderheitseigentum stehende Muttergesellschaft
In Minderheitseigentum stehende Tochtergesellschaft
In Minderheitseigentum stehende Geschäftseinheit Investmenteinheit Versicherungsinvestmenteinheit Verbriefungseinheit Joint Venture (JV) JV-Tochtergesellschaft Unwesentliche Geschäftseinheit In Teileigentum stehende Muttergesellschaft Zwischengeschaltete Muttergesellschaft Oberste Muttergesellschaft Ausgeschlossene Einheit Muttergesellschaft, die zur Anwendung einer anerkannten Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR)
Nicht zur Gruppe gehörende Einheit

Hybrid Entity Permanent Establishment Main Entity Minority-Owned Parent Entity
Minority-Owned Subsidiary
Minority-Owned Constituent Entity
Investment Entity Insurance Investment Entity Securitisation Entity Joint Venture (JV) JV Subsidiary Non-Material Constituent Entity POPE (Partially-owned Parent Entity) Intermediate Parent Entity Ultimate Parent Entity Excluded Entity Parent Entity required to apply a QIIR under Article 10.3.5
Non-group Member

Oberste Muttergesellschaft Geschäftseinheiten

UPE Constituent Entities

Seite 45 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ globe:POPEIPE_EnumType globe:ExcludedEntity_EnumType
globe:TypeofSubGroup_EnumType
globe:SafeHarbour_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
GIR803 GIR804 GIR805 GIR806

Deutsche Bezeichnung
Gemeinschaftsunternehmen (JV) JV-Tochtergesellschaften Ausgeschlossene Einheiten (aggregiert) Nicht zur Gruppe gehörende Einheiten (aggregiert)

Wertemenge / Erklärung
JV's (Joint Ventures) JV Subsidiaries Excluded Entities (aggregate) Non-Group members (aggregate)

GIR901 GIR902 GIR903

In Teileigentum stehende Muttergesellschaft Zwischengeschaltete Muttergesellschaft Muttergesellschaft, die zur Anwendung einer anerkannten Primärergänzungssteuerregelung (engl. Qualified Income Inclusion Rule - QIIR)

POPE (Partially-owned Parent Entity) Intermediate Parent Entity Parent Entity required to apply a QIIR under Article 10.3.5

GIR1001 GIR1002 GIR1003 GIR1004 GIR1005 GIR1006
GIR1007
GIR1008

Staatliche Einheit Internationale Organisation Organisation ohne Erwerbszweck Pensionseinheit Investmentvehikel, das die oberste Immobilien-Investmentvehikel, das die oberste Muttergesellschaft ist Einheit im Eigentum von ausgeschlossenen Einheiten gemäß Artikel 1.5.2 (a)

Governmental Entity International Organisation Non-profit Organisation Pension fund Investment Fund that is an UPE Real Estate Investment Vehicle that is an UPE Entity owned by Excluded Entities under Article 1.5.2 (a)

Einheit im Eigentum von ausgeschlossenen Einheiten gemäß Artikel 1.5.2 (b)

Entity owned by Excluded Entities under Article 1.5.2 (b)

GIR1101 GIR1102 GIR1103
GIR1104 GIR1105 GIR1106
GIR1201

Geschäftseinheiten

Constituent Entities

In Minderheitseigentum stehende Untergruppe Minority-Owned Subgroup

Eigenständige In Minderheitseigentum stehende Standalone MOCEs (Minority-Owned

Geschäftseinheit

Constituent Entity)

Investmenteinheit

Investment Entity

Joint-Venture-Gruppe

JV Group (Joint Venture Group)

Staatenlose Geschäftseinheit

Stateless Constituent Entity

De-minimis-Ausschluss (Wesentlichkeitsgrenze) De minimis Exclusion

Seite 46 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe: ETRRange_EnumType
globe:QDMTTuT_EnumType globe:globeTuT_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR1202
GIR1203
GIR1204 GIR1205
GIR1206 GIR1207 GIR1208 GIR1209

Deutsche Bezeichnung

Wertemenge / Erklärung

Safe-Harbour bei anerkannter nationaler

QDMTT safe harbour

Ergänzungssteuer

Übergangs-CbCR-Safe-Harbour – De-minimisTest (Wesentlichkeitsgrenze) Übergangs-CbCR-Safe-Harbour – ETR-Test Übergangs-CbCR-Safe-Harbour –

Transitional CbCR Safe Harbour – De minimis test Transitional CbCR Safe Harbour – ETR test Transitional CbCR Safe Harbour – Routine

Routinegewinntest Übergangs-UTPR-Safe-Harbour

profit test Transitional UTPR Safe Harbour

Permanenter Safe-Harbour – De-minimis-Test Permanent Safe Harbour – De minimis test

Permanenter Safe-Harbour – ETR-Test

Permanent Safe Harbour – ETR test

Permanenter Safe-Harbour – Routinegewinntest Permanent Safe Harbour – Routine profit

test

GIR1301 GIR1302 GIR1303 GIR1304 GIR1305 GIR1306 GIR1307 GIR1308 GIR1309 GIR1310 GIR1311 GIR1312 GIR1313 GIR1314
GIR1401 GIR1402 GIR1403 GIR1404 GIR1405 GIR1406 GIR1407 GIR1408 GIR1409

unter 2,5 % 2,5 % oder mehr, aber unter 5 % 5 % oder mehr, aber unter 7,5 % 7,5 % oder mehr, aber unter 10 % 10 % oder mehr, aber unter 12,5 % 12,5 % oder mehr, aber unter 15 % 15 % oder mehr, aber unter 17,5 % 17,5 % oder mehr, aber unter 20 % 20 % oder mehr, aber unter 22,5 % 22,5 % oder mehr, aber unter 25 % 25 % oder mehr, aber unter 27,5 % 27,5 % oder mehr, aber unter 30 % 30 % oder mehr Abschnitt 3.2 nicht erfüllt

below 2.5% 2.5% or above but below 5% 5% or above but below 7.5% 7.5% or above but below 10% 10% or above but below 12.5% 12.5% or above but below 15% 15% or above but below 17.5% 17.5% or above but below 20% 20% or above but below 22.5% 22.5% or above but below 25% 25% or above but below 27.5% 27.5% or above but below 30% 30% or above Section 3.2 not completed

keine Ergänzungssteuer zahlbar unter 1 Million EUR 1 Million EUR bis unter 5 Millionen EUR 5 Million EUR bis unter 25 Millionen EUR 25 Million EUR bis unter 50 Millionen EUR 50 Million EUR bis unter 75 Millionen EUR 75 Million EUR bis unter 100 Millionen EUR 100 Million EUR bis unter 250 Millionen EUR 250 Millionen EUR oder mehr.

No Top-up Tax payable Below EUR 1 million EUR 1 million to below EUR 5 million EUR 5 million to below EUR 25 million EUR 25 million to below EUR 50 million EUR 50 million to below EUR 75 million EUR 75 million to below EUR 100 million EUR 100 million to below EUR 250 million EUR 250 million or above.

Seite 47 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:ETRTypeofSubGroup_EnumType
globe:MainEntityPEandFTEBasis_EnumType globe:CrossBorderAdjustments_EnumType globe:UPEAdjustmentsBasis_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR1501 GIR1502 GIR1503 GIR1504 GIR1505 GIR1506 GIR1507 GIR1508 GIR1509
GIR1601 GIR1602 GIR1603
GIR1604 GIR1605 GIR1606 GIR1607
GIR1608
GIR1609
GIR1701 GIR1702 GIR1703 GIR1704
GIR1801 GIR1802
GIR1901 GIR1902 GIR1903 GIR1904 GIR1905 GIR1906 GIR1907

Deutsche Bezeichnung
keine Ergänzungssteuer zahlbar unter 1 Million EUR 1 Million EUR bis unter 5 Millionen EUR 5 Million EUR bis unter 25 Millionen EUR 25 Million EUR bis unter 50 Millionen EUR 50 Million EUR bis unter 75 Millionen EUR 75 Million EUR bis unter 100 Millionen EUR 100 Million EUR bis unter 250 Millionen EUR 250 Millionen EUR oder mehr.

Wertemenge / Erklärung
No Top-up Tax payable below EUR 1 million EUR 1 million to below EUR 5 million EUR 5 million to below EUR 25 million EUR 25 million to below EUR 50 million EUR 50 million to below EUR 75 million EUR 75 million to below EUR 100 million EUR 100 million to below EUR 250 million EUR 250 million or above.

Geschäftseinheiten

Constituent Entities

In Minderheitseigentum stehende Untergruppe Minority-Owned Subgroup

Eigenständige In Minderheitseigentum stehende Standalone MOCEs (Minority-Owned

Geschäftseinheit

Constituent Entity)

Investmenteinheiten

Investment Entities

Joint-Venture-Gruppe

JV Group (Joint Venture Group)

Staatenlose Geschäftseinheit

Stateless Constituent Entity

Übergangs-CbCR-Safe-Harbor-

Transitional CbCR Safe Harbour-Constituent

Geschäftseinheiten

Entities

Übergangs-CbCR-Safe-Harbor-Joint-Venture- Transitional CbCR Safe Harbour- JV Group

Gruppe (bitte spezifizieren welche JV-Gruppe) (specify which JV Group)

Übergangs-UTPR-Safe-Harbour

Transitional UTPR Safe Harbour

Artikel 3.4 Artikel 3.5.3 Artikel 3.5.1(a) Artikel 3.5.1(b)

Article 3.4 Article 3.5.3 Article 3.5.1(a) Article 3.5.1(b).

Artikel 3.2.3 Artikel 3.2.7

Article 3.2.3 Article 3.2.7

Artikel 7.1.1 (a) (i) Artikel 7.1.1 (a) (ii) Artikel 7.1.1 (b) Artikel 7.1.1 (c) Artikel 7.2.1 (a) (i) Artikel 7.2.1 (a) (ii) Artikel 7.2.1 (a) (iii)
Seite 48 von 64

Article 7.1.1 (a) (i) Article 7.1.1 (a) (ii) Article 7.1.1 (b) Article 7.1.1 (c) Article 7.2.1 (a) (i) Article 7.2.1 (a) (ii) Article 7.2.1 (a) (iii)

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:AdjustmentItem_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR1908 GIR1909 GIR1910
GIR2001 GIR2002 GIR2003 GIR2004
GIR2005
GIR2006 GIR2007 GIR2008 GIR2009 GIR2010 GIR2011 GIR2012 GIR2013 GIR2014
GIR2015 GIR2016 GIR2017 GIR2018

Deutsche Bezeichnung
Artikel 7.2.1 (b) Artikel 7.2.1 (c) Artikel 7.2.2

Wertemenge / Erklärung
Article 7.2.1 (b) Article 7.2.1 (c) Article 7.2.2

Nettosteueraufwand – Artikel 3.2.1 (a)

Net Taxes Expense - Article 3.2.1 (a)

Ausgenommene Dividenden – Artikel 3.2.1 (b) Excluded Dividends – Article 3.2.1 (b)

Ausgenommener Eigenkapitalgewinn oder -

Excluded Equity Gain or Loss – Article 3.2.1

verlust – Artikel 3.2.1 (c)

(c)

Nach der Neubewertungsmethode

Included Revaluation Method Gain or Loss –

berücksichtigter Gewinn oder Verlust – Artikel Article 3.2.1 (d)

3.2.1 (d)

Gemäß Artikel 6.3 ausgenommener Gewinn oder Gain or loss from disposition of assets and

Verlust aus der Veräußerung von

liabilities excluded under Article 6.3 – Article

Vermögenswerten und Verbindlichkeiten – Artikel 3.2.1 (e)

3.2.1 (e )

Asymmetrische Wechselkursgewinne oder -

Asymmetric Foreign Currency Gains or

verluste – Artikel 3.2.1 (f)

Losses – Article 3.2.1 (f)

Grundsätzlich unzulässige Aufwendungen –

Policy Disallowed Expenses – Article 3.2.1

Artikel 3.2.1 (g)

(g)

Fehler aus früheren Perioden – Artikel 3.2.1 (h) Prior Period Errors – Article 3.2.1 (h)

Fehler aus der Vorperiode oder Änderungen der Changes in Accounting Principles – Article

Rechnungslegungsgrundsätze – Artikel 3.2.1(h) 3.2.1(h)

Abgegrenzter Pensionsaufwand – Artikel 3.2.1 (i) Accrued Pension Expense – Article 3.2.1 (i)

Schuldenerlasse – Artikel 3.2.1 Aktienbasierte Vergütung – Artikel 3.2.2 Anpassungen zum Fremdvergleichsgrundsatz – Artikel 3.2.3 Anerkannte auszahlbare Steuergutschrift oder marktfähige übertragbare Steuergutschrift – Artikel 3.2.4 Wahlmöglichkeit für Gewinne und Verluste nach dem Realisationsprinzip – Artikel 3.2.5 Wahlmöglichkeit für angepasste Veräußerungsgewinne – Artikel 3.2.6 Aufwendungen für gruppeninterne Finanzierungsvereinbarungen – Artikel 3.2.7 Wahlmöglichkeit für konzerninterne Transaktionen in ein und demselben Steuerhoheitsgebiet – Artikel 3.2.8

Debt releases - Article 3.2.1 Stock-based compensation – Article 3.2.2 Arm’s length adjustments – Article 3.2.3
Qualified Refundable Tax Credit or Marketable Transferable Tax Credit – Article 3.2.4 Election for Gains and losses using realisation principle – Article 3.2.5 Election for Adjusted Asset Gain – Article 3.2.6 Intragroup Financing Arrangement expense – Article 3.2.7 Election for intragroup transactions in same jurisdiction – Article 3.2.8

Seite 49 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:IntShipCategory_EnumType globe:AncShipCategory_EnumType globe:AdjustedBasis_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2019
GIR2020
GIR2021
GIR2022
GIR2023
GIR2024 GIR2025 GIR2026
GIR2101 GIR2102 GIR2103 GIR2104 GIR2105 GIR2106

Deutsche Bezeichnung
Versicherungssteuern, die den Versicherungsnehmern in Rechnung gestellt werden – Artikel 3.2.9

Wertemenge / Erklärung
Insurance company taxes charged to policyholders – Article 3.2.9

Erhöhung/Verminderung des Eigenkapitals, das auf gezahlte/zahlbare oder erhaltene/einforderbare Ausschüttungen an zusätzliches Kernkapital zurückzuführen ist – Artikel 3.2.10

Increase/decrease to equity attributed to Additional Tier One and Restricted Tier One Capital distributions paid/payable or received/receivable – Article 3.2.10

Geschäftseinheiten, die einer multinationalen Unternehmensgruppe beitreten oder diese verlassen – Artikel 3.2.11 und 6.2

Constituent Entities joining and leaving an MNE Group – Article 3.2.11 and 6.2

Reduzierung des GloBE-Einkommens der UPE, die eine transparente Einheit ist – Artikel 3.2.11 und 7.1 Reduzierung des GloBE-Einkommens der UPE, die einer Regelung für abzugsfähige Dividenden unterliegt – Artikel 3.2.11 und 7.2 Wahlrecht für steuerpflichtige Ausschüttungen – Artikel 3.2.11 und 7.6 Einkünfte aus internationalem Seeverkehr – Artikel 3.3

Reduction of GloBE Income of the UPE that is a Flow-through Entity – Article 3.2.11 and 7.1 Reduction of GloBE Income of the UPE that is subject to a Deductible Dividend Regime – Article 3.2.11 and 7.2 Taxable Distribution Method election – Article 3.2.11 and 7.6 International Shipping Income – Article 3.3

Transaktionen zwischen Geschäftseinheiten – Transactions between Constituent Entities –

Artikel 9.1.3

Article 9.1.3

Article 3.3.2.a Article 3.3.2.b Article 3.3.2.c Article 3.3.2.d Article 3.3.2.e Article 3.3.2.f

Article 3.3.2.a Article 3.3.2.b Article 3.3.2.c Article 3.3.2.d Article 3.3.2.e Article 3.3.2.f

GIR2201 GIR2202 GIR2203 GIR2204 GIR2205

Artikel 3.3.3.a Artikel 3.3.3.b Artikel 3.3.3.c Artikel 3.3.3.d Artikel 3.3.3.e

Article 3.3.3.a Article 3.3.3.b Article 3.3.3.c Article 3.3.3.d Article 3.3.3.e

Seite 50 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:CurrentAdjustedTax_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
GIR2301 GIR2302 GIR2303 GIR2304 GIR2305 GIR2306 GIR2307 GIR2308 GIR2309

Deutsche Bezeichnung
Artikel 4.3.2 (a) Artikel 4.3.2 (b) Artikel 4.3.2 (c) Artikel 4.3.2 (d) Artikel 4.3.2 (e) Artikel 4.3.3 (a) Artikel 4.3.3 (b) Artikel 4.3.4 Artikel 4.3.2(c) – Gemischte CFC-Regelung (gemischte Hinzurechnungsbesteuerung)

Wertemenge / Erklärung
Article 4.3.2 (a) Article 4.3.2 (b) Article 4.3.2 (c) Article 4.3.2 (d) Article 4.3.2 (e) Article 4.3.3 (a) Article 4.3.3 (b) Article 4.3.4 Article 4.3.2(c) – Blended CFC regime

GIR2401 GIR2402
GIR2403 GIR2404 GIR2405 GIR2406

Erfasste Steuern, die bei der Ermittlung des

Covered Tax accrued as an expense in the

Gewinns vor Steuern im Abschluss als Auf-

profit before taxation in the financial

wand abgegrenzt wurden – Artikel 4.1.2 (a)

accounts - Article 4.1.2 (a)

Erfasste Steuern, die im Geschäftsjahr entrichtet Covered Taxes for uncertain tax position

wurden und mit Unsicherheiten

recorded as a reduction to Covered Taxes in

bezüglich der steuerlichen Behandlung

prior year – Article 4.1.2 (c)

zusammenhängen, sofern die betreffenden

Beträge in einem vorangegangenen

Geschäftsjahr als Kürzung der erfassten Steuern

gemäß Artikel 4.1.3 Buchstabe d behandelt

wurden - Artikel 4.1.2 (c)

Gutschriften oder Erstattungen in Bezug auf

Qualified Refundable Tax Credit or

anerkannte auszahlbare Steuergutschriften,

Marketable Transferable Tax Credits

die als Kürzung des laufenden Steueraufwands recorded as a reduction to current tax

erfasst wurden – Artikel 4.1.2 (d)

expense – Article 4.1.2 (d)

Qualifizierte Durchflusssteuervorteile

Qualified Flow-through Tax Benefits of

qualifizierter Eigentumsanteile – Artikel 3.2.1 (c) Qualified Ownership Interests – Article 3.2.1

(c)

Laufender Steueraufwand in Bezug auf Erträge, Current tax expense on income excluded

die bei der Berechnung des GloBE-

from GloBE Income or Loss – Article 4.1.3

Gewinns oder -Verlusts ausgenommen werden - (a)

Nicht qualifizierte erstattungsfähige

Non-Qualified Refundable Tax Credit, Non-

Steuergutschriften, nicht marktfähige

Marketable Transferable Tax Credit or Other

übertragbare Steuergutschriften oder andere Tax Credits not recorded as a reduction to

Steuergutschriften, die nicht als Reduzierung der current tax expense – Article 4.1.3 (b)

laufenden Steueraufwendungen erfasst wurden

– Artikel 4.1.3 (b)

Seite 51 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:DeferredAdjustedTax_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2407
GIR2408 GIR2409 GIR2410 GIR2411 GIR2412 GIR2413 GIR2414

Deutsche Bezeichnung

Wertemenge / Erklärung

Erstattete oder gutgeschriebene erfasste Steuern (außer qualifizierte erstattungsfähige Steuergutschriften oder marktfähige übertragbare Steuergutschriften), die nicht als Anpassung der laufenden Steueraufwendungen behandelt werden – Artikel 4.1.3 (c)

Covered Taxes refunded or credited (except for any Qualified Refundable Tax Credit, or Marketable Transferable Tax Credits) not treated as an adjustment to current tax expense – Article 4.1.3 (c)

Laufender Steueraufwand, der mit Unsicherheiten bezüglich der steuerlichen Behandlung zusammenhängt - Artikel 4.1.3. (d) Laufender Steueraufwand, der voraussichtlich nicht binnen drei Jahren nach Ende des Geschäftsjahrs bezahlt wird – Artikel 4.1.3 (e) Nach Einreichung der Erklärung erfolgende Anpassungen und Steuersatzänderungen – Artikel 4.6.1.

Current tax expense related to uncertain tax position– Article 4.1.3 (d)
Current tax expense not expected to be paid within three years – Article 4.1.3 (e)
Post-filing adjustments – Article 4.6.1.

Erfasste Steuern in Bezug auf Nettovermögensgewinn oder Nettovermögensverlust – Artikel 3.2.6

Covered Taxes relating to Net Asset Gain or Net Asset Loss – Article 3.2.6

Reduzierung der erfassten Steuern der obersten Reduction of Covered Taxes of the UPE that Muttergesellschaft, die eine transparente Einheit is a Flow-through Entity – Article 7.1 ist – Artikel 7.1

Erfasste Steuern für GloBE-Einkommen der UPE, die durch eine abzugsfähige Dividendenregelung reduziert werden - Artikel 7.2.2 Fiktive Ausschüttungssteuer - Artikel 7.3

Covered Taxes for GloBE Income of the UPE that is reduced under a Deductible Dividend Regime – Article 7.2.2
Deemed Distribution Tax – Article 7.3

GIR2415 GIR2416 GIR2417

Wahlrecht für steuerpflichtige Ausschüttungen – Taxable Distribution Method election –

Artikel 7.6.2 (b)

Article 7.6.2 (b)

Gesamtbetrag der Anpassung um latente

Total Deferred Tax Adjustment Amount –

Steuern – Artikel 4.4.1 (b)

Article 4.4.1 (b)

Im Eigenkapital oder im sonstigen Ergebnis

Increase or decrease in Covered Taxes

berücksichtigte Zu- oder Abnahmen der

recorded in equity or Other Comprehensive

erfassten Steuern im Zusammenhang mit gemäß Income relating to amounts included in

inländischen Steuervorschriften zu

GloBE Income or Loss that will be subject to

versteuernden Beträgen, die in die Berechnung tax under local tax rules – Article 4.1.1 (c)

des GloBE-Gewinns oder -Verlusts

einfließen - Artikel 4.1.1 (c)

Seite 52 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2501
GIR2502 GIR2503 GIR2504
GIR2505 GIR2506
GIR2507 GIR2508
GIR2509 GIR2510 GIR2511 GIR2512

Deutsche Bezeichnung

Wertemenge / Erklärung

Latenter Steueraufwand in Bezug auf Posten, die Deferred tax expense related to items

bei der Berechnung des GloBE-Gewinns

excluded from GloBE Income or Loss –

oder -Verlusts nach Kapitel 3 ausgenommen Article 4.4.1 (a)

werden – Artikel 4.4.1 (a)

Latenter Steueraufwand in Bezug auf nicht anerkannte Abgrenzungen – Artikel 4.4.1 (b)

Deferred tax expense related to Disallowed Accruals– Article 4.4.1 (b)

Latenter Steueraufwand in Bezug auf nicht geltend gemachte Abgrenzungen – Artikel 4.4.1 (b) Auswirkungen von Wertberichtigungen und Ansatzanpassungen in Bezug auf einen latenten Steueranspruch – Artikel 4.4.1 (c)

Deferred tax expense related to Unclaimed Accruals – Article 4.4.1 (b)
Valuation adjustment or accounting recognition adjustment related to a deferred tax asset – Article 4.4.1 (c)

Neu bemessener latenter Steueraufwand aufgrund einer Änderung des geltenden inländischen Steuersatzes – Artikel 4.4.1 (d) Latenter Steueraufwand im Zusammenhang mit der Entstehung und Nutzung von Steuergutschriften – Artikel 4.4.1 (e)

Deferred tax expense arising from a remeasurement related to changes in the tax rate – Article 4.4.1 (d) Deferred tax expense related to the generation and use of tax credits – Article 4.4.1 (e)

Ersatzverlustvortrag DTA oder fiktiver Ersatzverlustvortrag DTA – Artikel 4.4.1 (e)
Nicht anerkannte Rückstellungen oder nicht beanspruchte Rückstellungen, die während des Geschäftsjahres gezahlt wurden – Artikel 4.4.2 (a)

Substitute Loss Carry Forward DTA or deemed Substitute Loss Carry Forward DTA – Article 4.4.1 (e) Disallowed Accruals or Unclaimed Accruals paid during the fiscal year – Article 4.4.2 (a)

Rückforderung latenter Steuerverbindlichkeiten, Recapture Deferred Tax Liability paid during

die während des Geschäftsjahres gezahlt

the fiscal year– Article 4.4.2 (b)

wurden – Artikel 4.4.2 (b)

Erfassung eines Verlusts Latenter

Recognition of a loss Deferred Tax Asset not

Steueranspruch, der nicht in den Finanzzahlen included in the financials – Article 4.4.2 (c)

enthalten ist – Artikel 4.4.2 (c)

Anpassung des latenten Steueraufwands

Deferred tax expense adjustment resulting

aufgrund einer Steuersatzsenkung – Artikel 4.6.2 from a reduction to a tax rate – Article 4.6.2

Anpassung des latenten Steueraufwands aufgrund einer Steuersatzerhöhung – Artikel 4.6.3

Deferred tax expense adjustment resulting from an increase to a tax rate – Article 4.6.3

Seite 53 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:NonArt415_EnumType
globe:FinalAdjustedTax_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2513
GIR2514 GIR2515
GIR2516

Deutsche Bezeichnung

Wertemenge / Erklärung

Mitglieder einer multinationalen

Constituent Entities joining and leaving an

Unternehmensgruppe beitreten oder diese verlassen – Artikel 6.2

MNE Group – Article 6.2

Latenter Steueraufwand der obersten

Deferred tax expense of the UPE that is a

Muttergesellschaft, die eine transparente Einheit Flow-through Entity – Article 7.1

Latenter Steueraufwand der obersten

Deferred tax expense of the UPE that is

Muttergesellschaft, die dem System der

subject to Deductible Dividend Regime –

abzugsfähigen Dividenden unterliegt – Artikel 7.2 Article 7.2

Anpassung latenter Steuern aufgrund von

Deferred tax adjustment resulting from

Transaktionen zwischen Mitgliedern – Artikel transactions between Constituent Entities –

9.1.3

Article 9.1.3

GIR2601 GIR2602 GIR2603 GIR2604 GIR2605 GIR2606

Artikel 3.2.6 Artikel 4.4.4 Artikel 4.6.1 Artikel 4.6.4 Artikel 7.3.5 Artikel 7.3.7

Article 3.2.6 Article 4.4.4 Article 4.6.1 Article 4.6.4 Article 7.3.5 Article 7.3.7

GIR2701 GIR2702 GIR2703
GIR2704

Erfasste Steuern, die bei der Ermittlung des Gewinns vor Steuern im Abschluss als Aufwand abgegrenzt wurden – Artikel 4.1.2 (a)

Covered Tax accrued as an expense in the profit before taxation in the financial accounts - Article 4.1.2 (a) GloBE Loss Deferred Tax Asset established under Article 4.5.1 or used – Article 4.1.2 (b) combined with Article 4.5.3

Erfasste Steuern, die im Geschäftsjahr entrichtet Covered Taxes for uncertain tax position

wurden und mit Unsicherheiten

recorded as a reduction to Covered Taxes in

bezüglich der steuerlichen Behandlung

prior year – Article 4.1.2 (c)

zusammenhängen, sofern die betreffenden

Beträge in einem vorangegangenen

Geschäftsjahr als Kürzung der erfassten Steuern

gemäß Artikel 4.1.3 Buchstabe d behandelt

wurden - Artikel 4.1.2 (c)

Gutschriften oder Erstattungen in Bezug auf

Qualified Refundable Tax Credit or

anerkannte auszahlbare Steuergutschriften,

Marketable Transferable Tax Credits

die als Kürzung des laufenden Steueraufwands recorded as a reduction to current tax

erfasst wurden – Artikel 4.1.2 (d)

expense – Article 4.1.2 (d)

Seite 54 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2705 GIR2706 GIR2707
GIR2708
GIR2709 GIR2710 GIR2711 GIR2712 GIR2713 GIR2714
GIR2715 GIR2716 GIR2717

Deutsche Bezeichnung

Wertemenge / Erklärung

Qualifizierte Durchflusssteuervorteile

Qualified Flow-through Tax Benefits of

qualifizierter Eigentumsanteile – Artikel 3.2.1 (c) Qualified Ownership Interests – Article 3.2.1

(c)

Laufender Steueraufwand in Bezug auf Erträge, Current tax expense on income excluded

die bei der Berechnung des GloBE-

from GloBE Income or Loss – Article 4.1.3

Gewinns oder -Verlusts ausgenommen werden - (a)

Nicht qualifizierte erstattungsfähige

Non-Qualified Refundable Tax Credit, Non-

Steuergutschriften, nicht marktfähige

Marketable Transferable Tax Credit or Other

übertragbare Steuergutschriften oder andere Tax Credits not recorded as a reduction to

Steuergutschriften, die nicht als Reduzierung der current tax expense – Article 4.1.3 (b)

laufenden Steueraufwendungen erfasst wurden

– Artikel 4.1.3 (b)

Erstattete oder gutgeschriebene erfasste Steuern (außer qualifizierte erstattungsfähige Steuergutschriften oder marktfähige übertragbare Steuergutschriften), die nicht als Anpassung der laufenden Steueraufwendungen Laufender Steueraufwand, der mit Unsicherheiten bezüglich der steuerlichen Behandlung zusammenhängt - Artikel 4.1.3. (d)

Covered Taxes refunded or credited (except for any Qualified Refundable Tax Credit, or Marketable Transferable Tax Credits) not treated as an adjustment to current tax expense – Article 4.1.3 (c) Current tax expense related to uncertain tax position– Article 4.1.3 (d)

Laufender Steueraufwand, der voraussichtlich nicht binnen drei Jahren nach Ende des Geschäftsjahrs bezahlt wird – Artikel 4.1.3 (e)

Current tax expense not expected to be paid within three years – Article 4.1.3 (e)

Nach Einreichung der Erklärung erfolgende Anpassungen und Steuersatzänderungen – Artikel 4.6.1. Erfasste Steuern in Bezug auf Nettovermögensgewinn oder Nettovermögensverlust – Artikel 3.2.6 Latenter Steueraufwand des UPE, der ein FlowThrough-Unternehmen ist – Artikel 7.1 Erfasste Steuern für GloBE-Einkommen der UPE, die durch eine abzugsfähige Dividendenregelung reduziert werden - Artikel 7.2.2 Fiktive Ausschüttungssteuer - Artikel 7.3 Wahlrecht für steuerpflichtige Ausschüttungen – Artikel 7.6.2 (b) Gesamtbetrag der Anpassung um latente Steuern – Artikel 4.4.1 (b)

Post-filing adjustments – Article 4.6.1.
Covered Taxes relating to Net Asset Gain or Net Asset Loss – Article 3.2.6
Reduction of Covered Taxes of the UPE that is a Flow-through Entity – Article 7.1 Covered Taxes for GloBE Income of the UPE that is reduced under a Deductible Dividend Regime – Article 7.2.2
Deemed Distribution Tax – Article 7.3 Taxable Distribution Method election – Article 7.6.2 (b) Total Deferred Tax Adjustment Amount – Article 4.4.1 (b)

Seite 55 von 64

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ
globe:ExTypeOfEntity_EnumType
globe:DeminimisSimpleBasis_EnumType globe:TIN_EnumType globe:Currency_EnumType

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert GIR2718
GIR2719 GIR2720
GIR2801 GIR2802 GIR2803 GIR2804 GIR2805
GIR2901 GIR2902
GIR3001 GIR3002 GIR3003 GIR3004
GIR3101 GIR3102

Deutsche Bezeichnung

Wertemenge / Erklärung

Im Eigenkapital oder im sonstigen Ergebnis

Increase or decrease in Covered Taxes

berücksichtigte Zu- oder Abnahmen der

recorded in equity or Other Comprehensive

erfassten Steuern im Zusammenhang mit gemäß Income relating to amounts included in

inländischen Steuervorschriften zu

GloBE Income or Loss that will be subject to

versteuernden Beträgen, die in die Berechnung tax under local tax rules – Article 4.1.1 (c) des GloBE-Gewinns oder -Verlusts einfließen - Artikel 4.1.1 (c)

Überschüssiger negativer Steueraufwandsvortrag generiert - Artikel 4.1.5 und 5.2.1

Excess Negative Tax Expense Carry Forward generated – Article 4.1.5 and 5.2.1

Senkung der erfassten Steuern (jedoch nicht unter Null) um den verbleibenden Saldo des

Decrease in Covered Taxes (but not below zero) by the remaining balance of the Excess

Vortrags überschüssiger negativer

Negative Tax Expense Carry-forward –

Steueraufwendungen - Artikel 4.1.5 und 5.2.1 Article 4.1.5 and 5.2.1

Staatliche Einheit Internationale Organisation
Organisation ohne Erwerbszweck
Pensionseinheit
Pensionseinheit, die keine PensionsDienstleistungseinheit ist

Government Entity International Organisation
Non-profit Organisation
Pension Fund
Pension Fund that is not a Pension Services Entity

De minims Wahl (Wesentlichkeitsgrenze) Vereinfachte Berechnung für unwesentliche Geschäftseinheiten

De minimis election Simplified Calculation for Non-material Constituent Entities

Steuerliche Identifikationsnummer Funktional gleichwertige Nummer Vereinbarte, GIR-spezifische Nummer Muss nicht gemeldet werdem

Tax Identification Number Functionally equivalent number Agreed GIR designated number Not required to be reported

Lokal CFS

Local CFS

Seite 56 von 64

Bundeszentralamt für Steuern

Werteliste zum iso:CountryCode_Type

Zweibuchstabiges

Englische Umschreibung

Länderkürzel

des Länderkürzels

AF

Afghanistan

AX

Aland Islands

AL

Albania

DZ

Algeria

AS

American Samoa

AD

Andorra

AO

Angola

AI

Anguilla

AQ

Antarctica

AG

Antigua And Barbuda

AR

Argentina

AM

Armenia

AW

Aruba

AU

Australia

AT

Austria

AZ

Azerbaijan

BS

Bahamas

BH

Bahrain

BD

Bangladesh

BB

Barbados

BY

Belarus

BE

Belgium

BZ

Belize

BJ

Benin

BM

Bermuda

BT

Bhutan

BO

Bolivia, Plurinational State Of

BQ

Bonaire, Sint Eustatius And Saba

BA

Bosnia And Herzegovina

BW

Botswana

BV

Bouvet Island

BR

Brazil

IO

British Indian Ocean Territory

BN

Brunei Darussalam

BG

Bulgaria

BF

Burkina Faso

BI

Burundi

KH

Cambodia

CM

Cameroon

CA

Canada

CV

Cabo Verde

KY

Cayman Islands

CF

Central African Republic

TD

Chad

CL

Chile

CN

China

CX

Christmas Island

CC

Cocos (Keeling) Islands

CO

Colombia

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Werteliste zum iso:currCode_Type

Englische Bezeichnung des Landes, welche die Währung/Sprache als

Wert

Landeswährung verwendet

AED United Arab Emirates AFN Afghanistan

ALL Albania AMD Armenia ANG Curacao; Sint Maarten (Dutch Part)

AOA ARS AUD

Angola Argentina Australia; Christmas Island; Cocos (Keeling) Islands; Heard Island And Mcdonald Islands; Kiribati; Nauru; Norfolk Island; Tuvalu

AWG Aruba AZN Azerbaijan

BAM Bosnia And Herzegovina BBD Barbados BDT Bangladesh

BGN Bulgaria BHD Bahrain BIF Burundi

BMD Bermuda BND Brunei Darussalam BOB Bolivia, Plurinational State Of

BOV BRL BSD

Bolivia, Plurinational State Of Brazil Bahamas

BTN Bhutan BWP Botswana BYN Belarus

BYR BZD CAD

Belarus Belize Canada

CDF CHE CHF

Congo, The Democratic Republic Of Switzerland Liechtenstein; Switzerland

CHW Switzerland CLF Chile CLP Chile

CNY China COP Colombia COU Colombia

CRC Costa Rica CUC Cuba CUP Cuba

CVE Cabo Verde

CZK Czechia DJF Djibouti

DKK Denmark; Faroe Islands; Greenland

DOP Dominican Republic DZD Algeria

EGP Egypt

ERN Eritrea

ETB Ethi

Währungs-/Sprachbezeichnung
UAE Dirham Afghani Lek Armenian Dram Netherlands Antillean Guilder Kwanza Argentine Peso Australian Dollar
Aruban Florin Azerbaijan Manat Convertible Mark Barbados Dollar Taka Bulgarian Lev Bahraini Dinar Burundi Franc Bermudian Dollar Brunei Dollar Boliviano Mvdol Brazilian Real Bahamian Dollar Ngultrum Pula Belarusian Ruble Historic use Belarussian Ruble Belize Dollar Canadian Dollar Congolese Franc WIR Euro Swiss Franc WIR Franc Unidad de Fomento Chilean Peso Yuan Renminbi Colombian Peso Unidad de Valor Real Costa Rican Colon Peso Convertible Cuban Peso Cabo Verde Escudo Czech Koruna Djibouti Franc Danish Krone Dominican Peso Algerian Dinar Egyptian Pound Nakfa Ethiopian Birr

Seite 57 von 64

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel KM

Comoros

Englische Umschreibung des Länderkürzels

CG

Congo

CD

Congo, The Democratic Republic Of The

CK

Cook Islands

CR

Costa Rica

CI

Cote D'Ivoire

HR

Croatia

CU

Cuba

CW

Curacao

CY

Cyprus

CZ

Czechia

DK

Denmark

DJ

Djibouti

DM

Dominica

DO

Dominican Republic

EC

Ecuador

EG

Egypt

SV

El Salvador

GQ

Equatorial Guinea

ER

Eritrea

EE

Estonia

ET

Ethiopia

FK

Falkland Islands (Malvinas)

FO

Faroe Islands

FJ

Fiji

FI

Finland

FR

France

GF

French Guiana

PF

French Polynesia

TF

French Southern Territories

GA

Gabon

GM

Gambia

GE

Georgia

DE

Germany

GH

Ghana

GI

Gibraltar

GR

Greece

GL

Greenland

GD

Grenada

GP

Guadeloupe

GU

Guam

GT

Guatemala

GG

Guernsey

GN

Guinea

GW

Guinea-Bissau

GY

Guyana

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert EUR
FJD FKP GBP
GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung

Aland Islands; Andorra; Austria; Belgium; Cyprus; Estonia; European Union; Finland; Euro France; French Guiana; French Southern Territories; Germany; Greece;

Guadeloupe; Holy See (Vatican City State); Ireland; Italy; Latvia; Lithuania; Luxembourg; Malta; Martinique; Mayotte; Monaco; Montenegro; Netherlands; Portugal; Reunion; Saint Barthelemy; Saint Martin (French Part); Saint Pierre And

Miquelon; San Marino; Slovakia; Slovenia; Spain; Vatican City State (Holy See)

Fiji Falkl Guernsey; Isle Of Man; Jersey; United Kingdom Of Great Britain And Northern Ireland

Fiji Dollar Falkland Islands Pound Pound Sterling

Georgia Ghana Gibraltar

Lari Ghana Cedi Gibraltar Pound

Gambia Guinea Guatemala

Dalasi Guinean Franc Quetzal

Guyana Hong Kong Honduras

Guyana Dollar Hong Kong Dollar Lempira

Croatia Haiti Hungary

Kuna Gourde Forint

Indonesia Israel Bhutan; India

Rupiah New Israeli Sheqel Indian Rupee

Iraq Iran, Islamic Republic Of Iceland

Iraqi Dinar Iranian Rial Iceland Krona

Jamaica Jordan Japan

Jamaican Dollar Jordanian Dinar Yen

Kenya Kyrgyzstan Cambodia

Kenyan Shilling Som Riel

Comoros Korea, Democratic People’s Republic Of Korea, Republic Of

Comorian Franc North Korean Won Won

Kuwait Cayman Islands Kazakhstan

Kuwaiti Dinar Cayman Islands Dollar Tenge

Lao People’s Democratic Republic

Lao Kip

Lebanon Sri Lanka

Lebanese Pound Sri Lanka Rupee

Liberia

Liberian Dollar

Lesotho Lithuania

Loti Historic use Lithuanian Litas

Latvia

Historic use Latvian Lats

Libya Morocco; Western Sahara

Libyan Dinar Moroccan Dirham

Moldova, Republic Of

Moldovan Leu

Madagascar Macedonia, The Former Yugoslav Republic Of

Malagasy Ariary Denar

Seite 58 von 64

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
HT HM VA HN HK HU IS IN ID IR IQ IE IM IL IT JM JP JE JO KZ KE KI KP KR KW KG LA LV LB LS LR LY LI LT LU MO MK MG MW MY MV ML MT MH MQ MR MU YT MX FM MD MC

Englische Umschreibung des Länderkürzels
Haiti Heard Island And Mcdonald Islands Holy See (Vatican City State) Honduras Hong Kong Hungary Iceland India Indonesia Iran, Islamic Republic Of Iraq Ireland Isle Of Man Israel Italy Jamaica Japan Jersey Jordan Kazakhstan Kenya Kiribati Korea, Democratic People's Republic Of Korea, Republic Of Kuwait Kyrgyzstan Lao People'S Democratic Republic Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macao North Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Marshall Islands Martinique Mauritania Mauritius Mayotte Mexico Micronesia, Federated States Of Moldova, Republic Of Monaco

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
MMK MNT MOP MRO MRU MUR MVR MWK MXN MXV MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD SSP STD STN SVC SYP SZL THB TJS TMT TND TOP

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet
Myanmar Mongolia Macao Mauritania Mauritania Mauritius Maldives Malawi Mexico Mexico Malaysia Mozambique Namibia Nigeria Nicaragua Bouvet Island; Norway; Svalbard And Jan Mayen Nepal Cook Islands; New Zealand; Niue; Pitcairn; Tokelau Oman Panama Peru Papua New Guinea Philippines Pakistan Poland Paraguay Qatar Romania Serbia Russian Federation Rwanda Saudi Arabia Solomon Islands Seychelles Sudan Sweden Singapore Saint Helena, Ascension And Tristan Da Cunha Sierra Leone Somalia Suriname South Sudan Sao Tome And Principe Sao Tome And Principe El Salvador Syrian Arab Republic Eswatini Thailand Tajikistan Turkmenistan Tunisia Tonga

Währungs-/Sprachbezeichnung
Kyat Tugrik Pataca Historic use Ouguiya Ouguiya Mauritius Rupee Rufiyaa Malawi Kwacha Mexican Peso Mexican Unidad de Inversion (UDI) Malaysian Ringgit Mozambique Metical Namibia Dollar Naira Cordoba Oro Norwegian Krone Nepalese Rupee New Zealand Dollar Rial Omani Balboa Sol Kina Philippine Peso Pakistan Rupee Zloty Guarani Qatari Rial Romanian Leu Serbian Dinar Russian Ruble Rwanda Franc Saudi Riyal Solomon Islands Dollar Seychelles Rupee Sudanese Pound Swedish Krona Singapore Dollar Saint Helena Pound Leone Somali Shilling Surinam Dollar South Sudanese Pound Historic use Dobra Dobra El Salvador Colon Syrian Pound Lilangeni Baht Somoni Turkmenistan New Manat Tunisian Dinar Pa’anga

Seite 59 von 64

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
MN ME MS MA MZ MM NA

Mongolia Montenegro Montserrat Morocco Mozambique Myanmar Namibia

Englische Umschreibung des Länderkürzels

NR

Nauru

NP

Nepal

NL

Netherlands

NC

New Caledonia

NZ

New Zealand

NI

Nicaragua

NE

Niger

NG

Nigeria

NU

Niue

NF

Norfolk Island

MP

Northern Mariana Islands

NO

Norway

OM

Oman

PK

Pakistan

PW

Palau

PS

Palestine, State Of

PA

Panama

PG

Papua New Guinea

PY

Paraguay

PE

Peru

PH

Philippines

PN

Pitcairn

PL

Poland

PT

Portugal

PR

Puerto Rico

QA

Qatar

RE

Reunion

RO

Romania

RU

Russian Federation

RW

Rwanda

BL

Saint Barthelemy

SH

Saint Helena, Ascension And Tristan Da Cunha

KN

Saint Kitts And Nevis

LC

Saint Lucia

MF

Saint Martin (French Part)

PM

Saint Pierre And Miquelon

VC

Saint Vincent And The Grenadines

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert TRY TTD TWD TZS UAH UGX USD
USN USS UYI UYU UYW UZS VEF VES VND VUV WST XAF

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet
Turkey Trini Taiwan, Province Of China Tanzania, United Republic Of Ukraine Uganda American Samoa; Bonaire; Sint Eustatius And Saba; British Indian Ocean Territory; Ecuador; El Salvador; Guam; Haiti; Marshall Islands; Micronesia, Federated States Of; Northern Mariana Islands; Palau; Panama; Puerto Rico; Timor-Leste; Turks And Caicos Islands; United States; United States Minor Outlying Islands; Virgin Islands (British); Virgin Islands (US) United States United States Uruguay Uruguay Uruguay Uzbekistan Venezuela, Bolivarian Republic Of Venezuela, Bolivarian Republic Of Viet Nam Vanuatu Samoa Beac Cameroon; Central African Republic; Chad; Congo; Equatorial Guinea; Gabon

Währungs-/Sprachbezeichnung Turkish Lira Trinidad and Tobago Dollar New Taiwan Dollar Tanzanian Shilling Hryvnia Uganda Shilling US Dollar
US Dollar (Next day) Historic use US Dollar (Same day) Uruguay Peso en Unidades Indexadas (UI) Peso Uruguayo Unidad Previsional Uzbekistan Sum Historic use Bolivar Bolívar Soberano Dong Vatu Tala CFA Franc

XAG XAU XBA XBB XBC XBD XCD
XDR XFU
XOF XPD XPF XPT XSU XUA XXX

Zz11_Silver Zz08_Gold Zz01_Bond Markets Unit European_Eurco Zz02_Bond Markets Unit European_Emu-6 Zz03_Bond Markets Unit European_Eua-9 Zz04_Bond Markets Unit European_Eua-17 Anguilla; Antigua And Barbuda; Dominica; Grenada; Montserrat; Saint Kitts And Nevis; Saint Lucia; Saint Vincent And The Grenadines International Monetary Fund (Imf) Zz05_Uic-Franc Bceao Benin; Burkina Faso; Cote D'Ivoire; Guinea-Bissau; Mali; Niger; Senegal; Togo Zz09_Palladium French Polynesia; New Caledonia; Wallis And Futuna Zz10_Platinum Sistema Unitario De Compensacion Regional De Pagos "Sucre" Member Countries Of The African Development Bank Group Zz07_No_Currency

YER ZAR ZMW ZWL

Yemen Lesotho; Namibia; South Africa Zambia Zimbabwe

Silver Gold Bond Markets Unit European Composite Unit (EURCO) Bond Markets Unit European Monetary Unit (E.M.U.-6) Bond Markets Unit European Unit of Account 9 (E.U.A.-9) Bond Markets Unit European Unit of Account 17 (E.U.A.-17) East Caribbean Dollar
SDR (Special Drawing Right) UIC-Franc CFA Franc
Palladium CFP Franc Platinum Sucre ADB Unit of Account The codes assigned for transactions where no currency is involved Yemeni Rial Rand Zambian Kwacha Zimbabwe Dollar

Werteliste zum iso:LanguageCode_Type AA AB AF

Afar Abkhazian Afrikaans

Seite 60 von 64

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
WS SM ST SA SN RS SC SL SG SX SK SI SB SO ZA GS SS ES LK SD SR SJ SZ SE CH SY

Englische Umschreibung des Länderkürzels
Samoa San Marino Sao Tome And Principe Saudi Arabia Senegal Serbia Seychelles Sierra Leone Singapore Sint Maarten (Dutch Part) Slovakia Slovenia Solomon Islands Somalia South Africa South Georgia And The South Sandwich Islands South Sudan Spain Sri Lanka Sudan Suriname Svalbard And Jan Mayen Eswatini Sweden Switzerland Syrian Arab Republic

TW

Taiwan, Province Of China

TJ

Tajikistan

TZ

Tanzania, United Republic Of

TH

Thailand

TL

Timor-Leste

TG

Togo

TK

Tokelau

TO

Tonga

TT

Trinidad And Tobago

TN

Tunisia

TR

Turkey

TM

Turkmenistan

TC

Turks And Caicos Islands

TV

Tuvalu

UG

Uganda

UA

Ukraine

AE

United Arab Emirates

GB

United Kingdom Of Great Britain And Northern Ireland

US

United States

UM

United States Minor Outlying Islands

UY

Uruguay

UZ

Uzbekistan

VU

Vanuatu

VE

Venezuela, Bolivarian Republic Of

VN

Viet Nam

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
AK SQ AM AR AN HY AS AV AE AY AZ BA BM EU BE BN BH BI BS BR BG MY CA CH CE ZH CU
CV KW CO CR CS DA DV NL DZ EN EO ET EE FO FJ FI FR FY FF KA DE GD GA GL

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Akan Albanian Amharic Arabic Aragonese Armenian Assamese Avaric Avestan Aymara Azerbaijani Bashkir Bambara Basque Belarusian Bengali Bihari languages Bislama Bosnian Breton Bulgarian Burmese Catalan; Valencian Chamorro Chechen Chinese Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic Chuvash Cornish Corsican Cree Czech Danish Divehi; Dhivehi; Maldivian Dutch; Flemish Dzongkha English Esperanto Estonian Ewe Faroese Fijian Finnish French Western Frisian Fulah Georgian German Gaelic; Scottish Gaelic Irish Galician

Seite 61 von 64

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
VG VI WF EH YE ZM ZW XK

Englische Umschreibung des Länderkürzels
Virgin Islands, British Virgin Islands, U.S. Wallis And Futuna Western Sahara Yemen Zambia Zimbabwe Kosovo

Werteliste zum iso:MSCountryCode_Type [EU Specific]

AT

Austria

BE

Belgium

BG

Bulgaria

CY

Cyprus

CZ

Czechia

DK

Denmark

EE

Estonia

FI

Finland

FR

France

DE

Germany

GR

Greece

HU

Hungaria

HR

Croatia

IE

Ireland

IT

Italy

LV

Latvia

LT

Lithuania

LU

Luxembourg

MT

Malta

NL

Netherlands

PL

Poland

PT

Portugal

RO

Romania

SK

Slovakia

SI

Slovenia

ES

Spain

SE

Sweden

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
GV EL GN GU HT HA HE HZ HI HO HR HU IG IS IO II IU IE IA ID IK IT JV JA KL KN KS KR KK KM KI RW KY KV KG KO KJ KU LO LA LV LI LN LT LB LU LG MK MH ML MI MR

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Manx Greek Guarani Gujarati Haitian; Haitian Creole Hausa Hebrew Herero Hindi Hiri Motu Croatian Hungarian Igbo Icelandic Ido Sichuan Yi; Nuosu Inuktitut Interlingue; Occidental Interlingua (International Auxiliary Language Association) Indonesian Inupiaq Italian Javanese Japanese Kalaallisut; Greenlandic Kannada Kashmiri Kanuri Kazakh Central Khmer Kikuyu; Gikuyu Kinyarwanda Kirghiz; Kyrgyz Komi Kongo Korean Kuanyama; Kwanyama Kurdish Lao Latin Latvian Limburgan; Limburger; Limburgish Lingala Lithuanian Luxembourgish; Letzeburgesch Luba-Katanga Ganda Macedonian Marshallese Malayalam Maori Marathi

Seite 62 von 64

Bundeszentralamt für Steuern
Zweibuchstabiges Länderkürzel

Englische Umschreibung des Länderkürzels

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
MS MG MT MN NA NV NR ND NG NE NN NB NO NY OC OJ OR OM OS PA FA PI PL PT PS QU RM RO RN RU SG SA SI SK SL SE SM SN SD SO ST ES SC SR SS SU SW SV TY TA TT TE

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Malay Malagasy Maltese Mongolian Nauru Navajo; Navaho Ndebele, South; South Ndebele Ndebele, North; North Ndebele Ndonga Nepali Norwegian Nynorsk; Nynorsk, Norwegian Bokmål, Norwegian; Norwegian Bokmål Norwegian Chichewa; Chewa; Nyanja Occitan; Provençal Ojibwa Oriya Oromo Ossetian; Ossetic Panjabi; Punjabi Persian Pali Polish Portuguese Pushto; Pashto Quechua Romansh Romanian; Moldavian; Moldovan Rundi Russian Sango Sanskrit Sinhala; Sinhalese Slovak Slovenian Northern Sami Samoan Shona Sindhi Somali Sotho, Southern Spanish; Castilian Sardinian Serbian Swati Sundanese Swahili Swedish Tahitian Tamil Tatar Telugu

Seite 63 von 64

Bundeszentralamt für Steuern
Zweibuchstabiges Länderkürzel

Englische Umschreibung des Länderkürzels

Amtliche Datensatzbeschreibung Aufbau der Daten nach dem GIR-XML-Schema

GIR-XML-Schema v1.0 28.07.2025

Wert
TG TL TH BO TI TO TN TS TK TR TW UG UK UR UZ VE VI VO CY WA WO XH YI YO ZA ZU

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Tajik Tagalog Thai Tibetan Tigrinya Tonga (Tonga Islands) Tswana Tsonga Turkmen Turkish Twi Uighur; Uyghur Ukrainian Urdu Uzbek Venda Vietnamese Volapük Welsh Walloon Wolof Xhosa Yiddish Yoruba Zhuang; Chuang Zulu

Seite 64 von 64
