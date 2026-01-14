# Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der amtlich bestimmten Schnittstelle für Meldungen an das Bundeszentralamt für Steuern

- Herausgeber: Bundesministerium der Finanzen
- Datum: 2026-01-14
- Art: BMF-Schreiben
- Sachgebiet (BMF): Weitere_Steuerthemen / Organisation_Automation
- Quelle: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Organisation_Automation/2026-01-14-FKAustG-datensatz.html
- PDF: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Organisation_Automation/2026-01-14-FKAustG-datensatz.pdf?__blob=publicationFile&v=4
- Text: Textebene der amtlichen PDF-Datei, unverändert

---

Bundesministerium der Finanzen, 11016 Berlin
Nur per E-Mail Oberste Finanzbehörden der Länder nachrichtlich: Bundeszentralamt für Steuern

Wilhelmstraße 97 10117 Berlin Tel. +49 30 18 682-0 poststelle@bmf.bund.de www.bundesfinanzministerium.de 14. Januar 2026

Betreff: Gesetz zum automatischen Austausch von Informationen über Finanzkonten in Steuersachen (Finanzkonten-Informationsaustauschgesetz - FKAustG) Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der amtlich bestimmten Schnittstelle für Meldungen an das Bundeszentralamt für Steuern
Anlagen: 1 GZ: IV D 3 - S 1316/00708/051/005 DOK: COO.7005.100.3.13690654 Seite 1 von 3
(bei Antwort bitte GZ und DOK angeben)
§ 5 Absatz 1 des Finanzkonten-Informationsaustauschgesetzes (FKAustG) verpflichtet Finanzinstitute zur Meldung der in § 8 FKAustG genannten Informationen an das Bundeszentralamt für Steuern (BZSt). Durch das Gesetz zur Umsetzung der Richtlinie (EU) 2023/2226 wurde das FKAustG geändert und damit werden Finanzinstitute unter anderem ab dem Jahr 2027 zur Meldung zusätzlicher Informationen an das BZSt verpflichtet. Diese Änderungen sind am Tag nach der Verkündung im Bundesgesetzblatt in Kraft getreten.
Nach § 5 Absatz 1 Satz 1 FKAustG hat die Übermittlung der auszutauschenden Daten an das BZSt nach amtlich vorgeschriebenem Datensatz im Wege der Datenfernübertragung zu erfolgen. Aufgrund der gesetzlichen Änderungen hat sich die Notwendigkeit ergeben, auch diesen amtlich vorgeschriebenen Datensatz zu ändern und neu bekanntzugeben.
Nähere Informationen zur Datenübermittlung nach dem allgemeinen Meldestandard können auf der Internetseite des BZSt (www.bzst.bund.de) in den dort abgelegten Kommunikationshandbüchern abgerufen werden.
Hiermit wird der amtlich vorgeschriebene Datensatz entsprechend § 87b Absatz 1 der Abgabenordnung und nach § 5 Absatz 1 Satz 2 FKAustG veröffentlicht. Das Datenschema wird nachfolgend dargestellt und steht im Internet unter www.bzst.bund.de zur Ansicht und zum Abruf bereit.
1. Datenübermittlung über die DIP-Schnittstelle für Massendatenmelder

Seite 2 von 3
Gesamtstruktur der Datenübermittlung (DIP) Der Aufbau der XML-Struktur für die Datenübermittlung wird von der ELMA- auf die DIPSchnittstelle (Digitaler Posteingang) umgestellt. Das Wurzelelement der gesamten zu übertragenden XML-Datei ist nun dip:dip. Dieses umschließt den dip:header-Abschnitt, der alle Informationen des Senders für die Fachverfahrens- und Sender-Zuordnung enthält. Darauf folgt der dip:body, der die eigentlichen Fachdaten beinhaltet. Für die korrekte Verarbeitung muss im dip:application-Element das Attribut code den Wert „CRS“ beinhalten.
Die zugehörigen XML Schema Definitionen sowie weitere Erläuterungen sind auf der Internetseite des BZSt (www.bzst.bund.de) in den dort abgelegten CRS-spezifischen sowie allgemeinen DIP-Kommunikationshandbüchern abrufbar. Änderungen mit CRS-XML-Schema Version 3.0 Mit dieser Veröffentlichung wird die amtliche Datensatzbeschreibung für CRS-Meldungen auf die Version 3.0 des CRS-XML-Schemas aktualisiert. Die Umstellung des Schemas tritt zum 01.01.2027 in Kraft. Übermittlungen, die bis zum 31.12.2026 erfolgen, sind weiterhin nach dem bisherigen Schema in der Version 2.0 vorzunehmen. Für alle Datenübermittlungen ab dem 01.01.2027 ist ausschließlich die neue Schema-Version 3.0 zu verwenden. Die Schema-Version 3.0 führt neue Datenelemente und Wertelisten ein. Datenübermittler werden aufgefordert, ihre Systeme rechtzeitig auf die neue Schema-Version anzupassen. Die detaillierten Spezifikationen aller Änderungen sind der nachfolgenden amtlichen Datensatzbeschreibung zu entnehmen.

Seite 3 von 3
Sobald die CRS-spezifischen Kommunikationshandbücher entsprechend angepasst wurden, wird auf der Internetseite des BZSt (www.bzst.bund.de) darüber informiert.
Aufbau der XML-Datei Die Datensatzbeschreibung für den Aufbau der zu meldenden Daten ist als Anlage beigefügt.
2. Datenübermittlung über das BZSt online.portal
Verwendung des CRS-Formulars für Einzeldatenmelder Für Einzeldatenmelder steht zur Datenübermittlung ein CRS-Formular im BZSt online.portal (www.online.portal.bzst.de) zur Verfügung. Bei der Verwendung des CRS-Formulars sind die Datensätze einzeln in ein Webformular einzugeben.
Nähere Informationen zur Datenübermittlung über das Formular können dem Kommunikationshandbuch CRS Teil 2 entnommen werden, das auf der Internetseite des BZSt (www.bzst.bund.de) abrufbar ist.
Verwendung des Massendaten-XML-Uploads Das BZSt online.portal bietet neben dem Formular auch die Möglichkeit, eine XML-Datei manuell hochzuladen. Das Formular für den XML-Upload finden Sie nach dem Login im BZSt online.portal unter "Portal"/"Massendaten-Upload starten".
Im Gegensatz zur automatisierten Übermittlung über die DIP-Schnittstelle (Abschnitt I) darf beim manuellen Upload nur die Fachdaten-XML crs:CRS_OECD hochgeladen werden. Die Datei darf keinen DIP-Umschlag dip:dip enthalten.
Nähere Informationen zur Datenübermittlung über den Massendaten-XML-Upload können der Internetseite des BZSt (www.bzst.bund.de) entnommen werden.
3. Erstmalige Anwendung
Das Datenschema ist für Daten zu verwenden, die nach dem Meldestandard im Wege der Datenfernübertragung an das BZSt ab dem 1. Januar 2027 übermittelt werden.
Dieses Schreiben steht ab sofort auf der Internetseite des Bundesministeriums der Finanzen und des BZSt zur Ansicht und zum Abruf bereit. Die Veröffentlichung erfolgt im Bundessteuerblatt Teil I.
Im Auftrag
Dieses Dokument wurde elektronisch erstellt und ist ohne Unterschrift gültig.

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0 (Stand: 12.11.2025; gültig ab 1 Januar 2027) Datensatzbeschreibung
Nach § 5 FKAustG hat die Übermittlung der auszutauschenden Daten an das Bundeszentralamt für Steuern (BZSt) nach amtlich vorgeschriebenem Datensatz im Wege der Datenfernübertragung zu
erfolgen.
Hiermit wird der amtlich vorgeschriebene Datensatz entsprechend § 1 Absatz 2 der SteuerdatenÜbermittlungsverordnung und nach § 5 FKAustG veröffentlicht. Das Datenschema wird nachfolgend dargestellt und steht im Internet des BZSt unter www.bzst.bund.de zur Ansicht und zum Abruf bereit.

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Aufbau der zu meldenden Daten nach CRS-XML-Schema

Legende

Komplexe Datentypen sind in der Datensatzbeschreibung an der

Komplexe Datentypen

entsprechenden Stelle mit Fettschrift gekennzeichnet und dort entsprechend

zu ersetzen.

Element /Attribut E A
Kardinalität -Spalte 1
1..n
0..1 0..n

Element Attribut Erläuterung: Der Datentyp muss genau 1x verwendet werden. Der Datentyp muss mindestens 1x verwendet werden. Er kann danach beliebig oft wiederholt werden. Der Datentyp kann entfallen oder 1x verwendet werden. Der Datentyp kann entfallen oder beliebig oft wiederholt werden.

Bundeszentralamt für Steuern
Komplexe Datentypen
cfc:Address_Type
legalAddressType cfc:CountryCode cfc:AddressFree cfc:AddressFix
cfc:Street cfc:BuildingIdentifier cfc:SuiteIdentifier cfc:FloorIdentifier cfc:DistrictName cfc:POB cfc:PostCode cfc:City cfc:CountrySubentity
cfc:AddressFree crs:NamePerson_Type
nameType
crs:PrecedingTitle crs:Title
crs:FirstName xnlNameType
crs:MiddleName xnlNameType
crs:NamePrefix xnlNameType
crs:LastName xnlNameType
crs:GenerationIdentifier crs:Suffix crs:GeneralSuffix crs:PersonParty_Type crs:ResCountryCode crs:TIN
issuedBy
crs:Name

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Element Kardi/Attribut nalität Min Max Datentyp

Deutsche Bezeichnung

Wertemenge / Erklärung

A

0..1

cfc:Address_Type

stf:OECDLegalAddressType_Enum

Type

Art der Adresse

Komplexer Datentyp für die Adresse. Erlaubter Wertebereich siehe unten unter: stf:OECDLegalAddressType_EnumType

E

1

iso:CountryCode_Type

Länderkürzel

Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type

E

0..1 1 4000 stf:StringMin1Max4000_Type

Adresse ohne Formatvorgabe

An dieser Stelle muss entweder "AddressFree" oder "AddressFix" mit optional AddressFree angegeben werden. Die Folgeeintragungen sind

E

0..1

cfc:AddressFix_Type

Strukturierte Adresse

abhängig von dieser Auswahl.

E

0..1 1 200 stf:StringMin1Max200_Type

Strasse

E

0..1 1 200 stf:StringMin1Max200_Type

Hausnummer

E

0..1 1 200 stf:StringMin1Max200_Type

Wohnungsbezeichnung

E

0..1 1 200 stf:StringMin1Max200_Type

Etagenbezeichnung

E

0..1 1 200 stf:StringMin1Max200_Type

Verwaltungsbezirk

E

0..1 1 200 stf:StringMin1Max200_Type

Postfach

E

0..1 1 200 stf:StringMin1Max200_Type

Postleitzahl

E

1

1 200 stf:StringMin1Max200_Type

Stadt

E

0..1 1 200 stf:StringMin1Max200_Type

Bundesland

An dieser Stelle kann „AddressFree“ nur angegeben werden, wenn

E

0..1 1 4000 stf:StringMin1Max4000_Type

Adresse ohne Formatvorgabe zuvor auch „AddressFix“ angegeben wurde.

crs:NamePerson_Type

Komplexer Datentyp für eine natürliche Person.

A

0..1

stf:OECDNameType_EnumType Art des Namens

stf:OECDNameType_EnumType

Dem Titel vorangehender

E

0..1 1 200 stf:StringMin1Max200_Type

Namenszusatz

E

0..n 1 200 stf:StringMin1Max200_Type

Titel

Der "Vorname" ist ein Pflichtfeld. Beim Vorhandensein von entweder

Vor- oder Nachnamen ist das Feld "LastName" mit diesem zu

füllen und in "FirstName" "NFN" für „NoFirstName“

E

1

1 200 stf:StringMin1Max200_Type

Vorname

einzugeben.

A

0..1 1 200 stf:StringMin1Max200_Type

E

0..n 1 200 stf:StringMin1Max200_Type

Namensqualifizierer

A

0..1 1

stf:StringMin1Max200_Type

E

0..1 1 200 stf:StringMin1Max200_Type

Namenszusatz

A

0..1 1 200 stf:StringMin1Max200_Type

Der "Nachname" ist ein Pflichtfeld. Beim Vorhandensein von entweder

Vor- oder Nachnamen ist das Feld "LastName" mit diesem zu

füllen und in "FirstName" "NFN" für „NoFirstName“

E

1

1 200 stf:StringMin1Max200_Type

Nachname

einzugeben.

A

0..1 1 200 stf:StringMin1Max200_Type

E

0..n 1 200 stf:StringMin1Max200_Type

Generationskennzeichner

E

0..n 1 200 stf:StringMin1Max200_Type

Suffix

E

0..1 1 200 stf:StringMin1Max200_Type

Allgemeines Suffix

crs:PersonParty_Type

E

1..n

iso:CountryCode_Type

E

0..n 1 200 cfc:TIN_Type

A

0..1

iso:CountryCode_Type

E

1..n

crs:NamePerson_Type

Natürliche Person Steuerlicher Sitz Steuernummer Herausgegeben von

Komplexer Datentyp für eine natürliche Person Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type Steuernummer Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type Datengruppe "crs:Name" vom Datentyp "crs:NamePerson_Type " ist oben definiert und hier entsprechend zu ersetzen.

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Komplexe Datentypen

Element Kardi/Attribut nalität Min Max

crs:Address

E

crs:Nationality

E

crs:BirthInfo

E

crs:BirthDate

E

crs:City

E

crs:CitySubentity

E

crs:CountryInfo

E

crs:CountryCode

E

crs:FormerCountryName E

crs:OrganisationParty_Type

crs:ResCountryCode

E

crs:IN

E

issuedBy

A

INType

A

crs:Name

E

nameType

A

1..n 0..n 0..1 0..1 0..1 1 200 0..1 1 200 0..1 1
0..1 1 200
0..n 0..n 1 200 0..1 0..1 1 200 1..n 1 200
0..1

crs:Address stf:DocSpec_Type
stf:DocTypeIndic

E

1..n

E

1

Datentyp

Deutsche Bezeichnung

cfc:Address_Type iso:CountryCode_Type
xsd:date stf:StringMin1Max200_Type stf:StringMin1Max200_Type
iso:CountryCode_Type
stf:StringMin1Max200_Type crs:OrganisationParty_Type iso:CountryCode_Type crs:OrganisationIN_Type iso:CountryCode_Type stf:StringMin1Max200_Type cfc:NameOrganisation_Type
stf:OECDNameType_EnumType

Nationalität Geburtsangaben Geburtsdatum Geburtsort Ortsteil des Geburtsortes Informationen zum Staat Länderkürzel
Vormaliger Staatsname Organisation Steuerlicher Sitz Identifikationsnummer Herausgegeben von Art der Identifikationsnummer Name der Organisation
Art des Namens

cfc:Address_Type stf:DocSpec_Type

DocSpec

stf:OECDDocTypeIndic_EnumType Meldungsart

Wertemenge / Erklärung
Datengruppe "crs:Address" vom Datentyp "cfc:Address_Type " ist oben definiert und hier entsprechend zu ersetzen.
***Non CRS*** Gruppiert die Geburtsangaben Format: YYYY-MM-DD
Gruppiert die Informationen zum Staat Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type Falls "CountryInfo" angegeben wird, muss entweder "CountryCode" oder "FormerCountryName" angegeben werden. Komplexer Datentyp für die Organisation Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type Identifikationsnummer Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type
Pflichtangabe Erlaubter Wertebereich siehe unten unter: stf:OECDNameType_EnumType Datengruppe "crs:Address" vom Datentyp "cfc:Address_Type" ist oben definiert und an der Stelle entsprechend zu ersetzen. Komplexer Datentyp für DocSpec Erlaubter Wertebereich siehe unten unter: stf:OECDDocTypeIndic_EnumType

stf:DocRefId

E

stf:CorrMessageRefId

E

stf:CorrDocRefId

E

crs:CorrectableOrganisationParty_Type

crs:ResCountryCode

E

crs:IN

E

issuedBy

A

INType

A

crs:Name

E

nameType

A

Struktur: DE<Meldejahr><IN>FI<Bezeichner>

DE<Meldejahr><IN>FI<Bezeichner> entspricht: • <Meldejahr> entspricht dem Jahr aus "ReportingPeriod" im Format "YYYY" • <IN> entspricht einer Identifikationsnummer von FI • <Bezeichner> entspricht einem eindeutigen Bezeichner von FI.

1

1 200 stf:StringMin1Max200_Type

DocRefId

Die DocRefID dar 170 Zeichen enthalten

0..1 1 170 stf:StringMin1Max170_Type

CorrMessageRefId

Die Struktur entspricht der MessageRefId

0..1 1 200 stf:StringMin1Max200_Type

CorrDocRefId

Die Struktur und Zeichenlänge entspricht der DocRefId

crs:CorrectableOrganisationPart

y_Type

0..n

iso:CountryCode_Type

Steuerlicher Sitz

Länderkürzel . Alle ResCountryCodes müssen gleich „DE“ sein.

0..n

1 200 crs:OrganisationIN_Type

0..1

iso:CountryCode_Type

Identifikationsnummer Herausgegeben von

Identifikationsnummer Erlaubter Wertebereich siehe unten unter: iso:CountryCode_Type

0..1 1 200 stf:StringMin1Max200_Type

Art der Identifikationsnummer

1..n 1 200 cfc:NameOrganisation_Type

Name der Organisation

Erlaubter Wertebereich siehe unten unter:

0..1

stf:OECDNameType_EnumType Art des Namens

stf:OECDNameType_EnumType

Bundeszentralamt für Steuern
Komplexe Datentypen
crs:Address crs:DocSpec

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Element Kardi/Attribut nalität Min Max Datentyp

E

1..n

E

1

cfc:Address_Type stf:DocSpec_Type

Deutsche Bezeichnung Adresse DocSpec

Wertemenge / Erklärung
Datengruppe "crs:Address" vom Datentyp "cfc:Address_Type" ist oben definiert und an der Stelle entsprechend zu ersetzen. Datengruppe "crs:DocSpec" vom Datentyp"stf:DocSpec_Type" ist oben definiert und an der Stelle entsprechend zu ersetzen.

Bundeszentralamt für Steuern DIP

dip:dip

version
dip:header environment

dip:consignment dip:customerIdentifier
dip:identityProvider
dip:identifier dip:creationTime dip:transferticketId dip:referenceId dip:application code
dip:body dip:consignmentItem consignmentItemPosition
dip:bopAccountId dip:data

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Kardi- Mi nalität n Max Datentyp
1

1

xs:string

1

DipHeaderType

1

environmentType

1

ConsignmentType

1

CustomerIdentifierType

1

identityProviderType

1

1 16 identifierType

1

xs:dateTime

1

1 170 customTicketIdNumberType

0..1 1 170 customTicketIdNumberType

1

applicationType

1

1 12 applicationCodeType

1

DipBodyType

1..n

ConsignmentItemType

1

xs:unsignedLong

0..1 1 36 bopAccountIdType

1

xs:anyType

Deutsche Bezeichnung dip Version

Wertemenge / Erklärung
Digitaler Posteingang (dip) Wurzelverzeichnis Dieser Bestandteil ist stets über die Schemadefinition der dip.xsd zu überprüfen. Attribut zu dip:dip Version der dip Definition. Hier ist die Version 2.0 zu verwenden.

Zielumgebung Sendungsdaten

Attribut zu dip:header Es können nur die Werte - TEST - PROD verwendet werden. Aus Gründen des Datenschutzes dürfen Testdaten nur unter Verwendung des Wertes "TEST" und Produktivdaten nur unter Verwendung des Wertes "PROD" übermittelt werden.

Identifikationskennung

Identifikationskennung des Datenübermittlers, anhand dieser eindeutig verifiziert werden kann. I.d.R. ein dem Fachverfahren/Fachbereich bekannte Kennung z.B. ELSTER-Konto-ID oder BZSt-Zertifikats-Nummer.

Provider der Identifikationskennung Festlegung, welchem Provider die Identifikationskennung zuzuordnen ist:

BZST-CERT einem BZSt-Zertifikat, ELSTER einem ELSTER-Konto

Es können nur die Werte

- BZST-CERT

- ELSTER

verwendet werden.

Identifikationskennung

Identifikationskennung (alphanumerisch)

Erzeugungszeitpunkt

Erzeugungszeitpunkt der Lieferung als Zeitstempel

Identifikationsnummer der Lieferung Identifikationsnummer der Lieferung, eine eineindeutige Kennung dieser Lieferung. (alphanumerisch)

Identifikationsnummer einer Bezugs- Identifikationsnummer einer Bezugs-Lieferung als Referenz auf die

Lieferung

transferticketId einer vorhergehenden Lieferung. (alphanumerisch)

Verfahrensbezeichnung

Benennung des Ziel-Fachverfahrens, z.B DAC7, CESOP, CRS

Fachverfahrensbezeichnung
Inhalte der Lieferung Meldungen

Attribut zu dip:application Angabe zur Bezeichnung des Fachverfahrens Hier ist der Wert "CRS" zu verwenden.
Multiplizität zur Lieferung mehrerer Anträge/Meldungen in einer Lieferung Für CRS-Lieferungen darf nur ein dip:consignmentItem übermittelt werden.

Position der Meldung

Attribut zu dip:consignmentItem Position, die auch bei der Rückgabe des Protokolls im PayloadResultType verwendet wird. Zeigt die Korrelation zwischen Lieferung und Rückgabe für ein ConsignmentItem an. Das erste consignmentItem hat die Position 0. Für DAC2-Lieferungen darf nur ein dip:consignmentItem übermittelt werden.

Benutzerkennung Nutzdaten-XML

Benutzerkennung des Antragstellers im POSt 2.0 (BOPNeu) für Zustellung eines Verwaltungsaktes im Portal. An dieser Stelle sind die Nutzdaten im Format des Fachverfahrens-XMLs crs:CRS_OECD der OECD und EU anzugeben. Weitere Informationen zu diesem Schema sind unter Nutzdaten CRS zu finden.

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Kardi-

Element

Attribut

nalität Min Max Datentyp

Deutsche Bezeichnung

Wertemenge / Erklärung

crs:CRS_OECD

Root Verzeichnis

version

version

0..1 1 10 stf:StringMin1Max10_Type

Der Inhalt muss gleich „3.0“ sein.

crs:MessageSpec

1

crs:MessageSpec_Type

MessageSpec

Gruppiert die Daten der Nachricht

Identifikationsnummer des

crs:SendingCompanyIN

0..1 1 200 stf:StringMin1Max200_Type

physikalischen Absenders

Pflicht: Steuernummer gemäß Kommunikationshandbuch CRS

crs:TransmittingCountry

1

iso:CountryCode_Type

Übermittelndes Land

Nur der feste Wert DE erlaubt

crs:ReceivingCountry

1

iso:CountryCode_Type

Empfangendes Land

Nur der feste Wert DE erlaubt

crs:MessageType

1

crs:MessageType_EnumType

Meldeart

Nur der feste Wert CRS erlaubt

crs:Warning

0..1 1 4000 stf:StringMin1Max4000_Type

Warnung

Freitextfeld

crs:Contact

0..1 1 4000 stf:StringMin1Max4000_Type

Kontaktinformation

Freitextfeld

Struktur: DE<Meldejahr>DE<Bezeichner>:

• <Meldejahr> entspricht dem Jahr aus "ReportingPeriod" im Format

"YYYY"

• <Bezeichner> entspricht einem eindeutigen Bezeichner des

Finanzinstituts z. B. die „SendingCompanyIN“ plus einer eindeutigen

crs:MessageRefId

1

1 170 stf:StringMin1Max170_Type

MessageRefID

Nummer oder Zeitstempel der Lieferung.

Erlaubter Wertebereich siehe unten unter:

crs:MessageTypeIndic

1

crs:CrsMessageTypeIndic_EnumType Lieferungsart

crs:CrsMessageTypeIndic_EnumType

crs:CorrMessageRefId

0..n 1 170 stf:StringMin1Max170_Type

CorrMessageRefID

Entspricht der Struktur der MessageRefID

Format: YYYY-MM-DD

crs:ReportingPeriod

1

xsd:date

Meldezeitraum

MM muss mit "12" und "DD" mit "31" gefüllt sein.

Angabe des Datums der Zusammenstellung mit Angabe von Stunde,

crs:Timestamp

1

xsd:dateTime

Zeitstempel der Lieferdatei Minute und Sekunde

crs:CrsBody

0..n

crs:CrsBody_Type

Diese Datengruppe darf nur einmal vorkommen.

crs:CorrectableOrganisationParty_Ty

crs:ReportingFI

1

pe

Meldendes Finanzinstitut

Gruppiert die Daten der meldenden Finanzinstitute

crs:ReportingGroup

1..n

Reportgruppe

Diese Datengruppe darf nur einmal vorkommen.

crs:CorrectableOrganisationParty_Ty

crs:Sponsor

0..1

pe

Verwaltender Rechtsträger ***Non CRS***

crs:CorrectableOrganisationParty_Ty

crs:Intermediary

0..1

pe

***Non CRS***

Gruppiert die Daten des Kontos

crs:AccountReport

0..n

crs:CorrectableAccountReport_Type Kontobericht

Datengruppe "crs:DocSpec" vom Datentyp "stf:DocSpec_Type" ist

crs:DocSpec

1

stf:DocSpec_Type

oben definiert und an der Stelle entsprechend zu ersetzen.

Kontonummer einfügen, sofern keine Kontonummer existiert, den Wert

crs:AccountNumber

1 200 crs:FIAccountNumber_Type

Kontonummer

"NANUM" angeben

Erlaubter Wertebereich siehe unten unter:

AcctNumberType

AcctNumberType 0..1

cfc:AcctNumberType_EnumType

Art der Kontonummer

cfc:AcctNumberType_EnumType

UndocumentedAccou

UndocumentedAccount nt

0..1

xsd:boolean

Undokumentiertes Konto

ClosedAccount

ClosedAccount

0..1

xsd:boolean

Geschlossenes Konto

DormantAccount

DormantAccount

0..1

xsd:boolean

Ruhendes Konto

crs:AccountHolder

1

crs:AccountHolder_Type

Kontoinhaber

Gruppiert die Daten des Kontoinhabers

crs:EquityInterestType

Identifiziert die Rolle bei legalen Vereinbarungen (z.B. Trust). Erlaubter

Wertebereich siehe unten unter:

0..n

crs:EquityInterestType_EnumType

Art der Beteiligung

crs:EquityInterestType_EnumType

crs:SelfCert

Gibt an, ob eine gültige Selbstauskunft vorliegt (True/False). Erlaubter

Wertebereich siehe unten unter:

1

crs:CrsSelfCert_EnumType

Selbstauskunft (Kontoinhaber) crs:CrsSelfCert_EnumType

Bundeszentralamt für Steuern

Element

Attribut

crs:Individual
crs:Organisation crs:AcctHolderType crs:ControllingPerson crs:Individual crs:CtrlgPersonType

crs:SelfCert crs:AccountBalance
currCode crs:Payment
crs:Type crs:PaymentAmnt
currCode
crs:DDProcedure
crs:AccountType crs:JointAccount
crs:Number crs:PoolReport

currCode currCode

ftc:DocSpec ftc:AccountCount

ftc:AccountPoolReportType ftc:PoolBalance

currCode

currCode

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Kardinalität Min Max Datentyp

0..1

crs:PersonParty_Type

Deutsche Bezeichnung Natürliche Person

Wertemenge / Erklärung
An dieser Stelle muss entweder "crs:Individual" für eine natürliche Person oder "crs:Organisation"für eine Organisation angegeben werden. Wenn eine Organisation angegeben wurde, muss auch AcctHolderType angegeben werden. Komplexer Datentypen sind oben definiert und an der Stelle entsprechend zu ersetzen.

0..1

crs:OrganisationParty_Type

Organisation

Erlaubter Wertebereich siehe unten unter:

0..1

crs:CrsAcctHolderType_EnumType

Art des Kontoinhabers

crs:CrsAcctHolderType_EnumType

0..n

crs:ControllingPerson_Type

Beherrschende Person

Gruppiert die Daten der Beherschenden Person

Komplexer Datentyp "crs:Individual" ist oben definiert und an der Stelle

1

crs:PersonParty_Type

Natürliche Person

entsprechend zu ersetzen.

Erlaubter Wertebereich siehe unten unter:

0..1

crs:CrsCtrlgPersonType_EnumType Art der beherrschenden Person crs:CrsCtrlgPersonType_EnumType

Gibt an, ob eine gültige Selbstauskunft für die beh. Person vorliegt

crs:CrsSelfCertforCtrlgPersonType_Enu

(True/False). Erlaubter Wertebereich siehe unten unter:

1

mType

Selbstauskunft (Beh. Person) crs:CrsSelfCertforCtrlgPersonType_EnumType

1

cfc:MonAmnt_Type

Kontostand

Zahl mit zwei Stellen nach dem Komma. Muss größer gleich 0 sein.

1

iso:currCode_Type

Währungskürzel

Erlaubter Wertebereich siehe unten unter: iso:currCode_Type

0..n

crs:Payment_Type

Zahlung

Gruppiert die Daten der Zahlung

Erlaubter Wertebereich siehe unten unter:

1

crs:CrsPaymentType_EnumType

Art

crs:CrsPaymentType_EnumType

1

cfc:MonAmnt_Type

Zahlungsbetrag

Zahl mit zwei Stellen nach dem Komma

1

iso:currCode_Type

Währungskürzel

Erlaubter Wertebereich siehe unten unter: iso:currCode_Type

Gibt an, ob es sich um ein Neu- oder Bestandskonto handelt. Erlaubter

1

crs:OpeningDate_EnumType

Sorgfaltspflichtverfahren

Wertebereich siehe unten unter: crs:OpeningDate_EnumType

Spezifiziert die Art des Finanzkontos. Erlaubter Wertebereich siehe unten

1

crs:CrsAccountType_EnumType

Kontoart

unter: crs:CrsAccountType_EnumType

0..1

Gemeinschaftskonto

Angabe für Gemeinschaftskonten.

1

1 200 xsd:integer

Anzahl (Gemeinschaftskonto) Anzahl der gemeinsamen Kontoinhaber.

0..n

ftc:CorrectablePoolReport_Type

Pool Bericht

***Non CRS*** Entspricht der Datengruppe "crs:DocSpec" vom Datentyp

stf:DocSpec_Type der oben definiert und an der Stelle entsprechend zu

ersetzen ist.

1

stf:DocSpec_Type

DocSpec

***Non CRS***

1

xsd:integer

Kontenanzahl

***Non CRS***

ftc:FatcaAcctPoolReportType_EnumTyp

1

e

Kontoart des Poolberichts

***Non CRS***

1

cfc:MonAmnt_Type

Kontostand des Poolberichts Zahl mit zwei Stellen nach dem Komma. ***Non CRS*** Erlaubter Wertebereich siehe unten unter: iso:currCode_Type

1

iso:currCode_Type

Währungskürzel

***Non CRS***

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

Typ

Wert

crs:CrsAcctHolderType_EnumType

CRS101 CRS102

cfc:AcctNumberType_EnumType
crs:CrsCtrlgPersonType_EnumType
crs:CrsMessageTypeIndic_EnumType crs:CrsPaymentType_EnumType crs:MessageType_EnumType
stf:OECDDocTypeIndic_EnumType

CRS103 OECD601 OECD602 OECD603 OECD604 OECD605 OECD606
CRS801 CRS802 CRS803 CRS804 CRS805 CRS806 CRS807 CRS808 CRS809 CRS810 CRS811 CRS812 CRS813 CRS800 CRS701 CRS702 CRS703 CRS501
CRS502
CRS503
CRS504
CRS OECD0 OECD1 OECD2 OECD3 OECD10 OECD11

Wertebereich für Typen
Englische Bezeichnung Passive Non-Financial Entity with one or more controlling person that is a Reportable Person

Deutsche Bezeichnung

CRS Reportable Person

Passive NFE that is a CRS Reportable Person IBAN OBAN ISIN OSIN Other Specified Electronic Money Product
CP of legal person - ownership CP of legal person - other means CP of legal person - senior managing official CP of legal arrangement - trust - settlor CP of legal arrangement - trust - trustee CP of legal arrangement - trust - protector CP of legal arrangement - trust - beneficiary CP of legal arrangement - trust - other CP of legal arrangement - other - settlor-equivalent CP of legal arrangement - other - trustee-equivalent CP of legal arrangement - other - protector-equivalent CP of legal arrangement - other - beneficiary-equivalent CP of legal arrangement - other - other-equivalent not reported The message contains new information The message contains corrections for previously sent information The message advises there is no data to report Dividends
Interest
Gross Proceeds / Redemptions
Other - CRS

Resend Data New Data Corrected Data Deletion of Data Resend Test Data New Test Data

CRS-XML Schema 12.11.2025
Wertemenge / Erklärung
***Non CRS*** ***Non CRS***

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

Typ

Wert

Englische Bezeichnung

OECD12 OECD13

Corrected Test Data Deletion of Test Data

stf:OECDLegalAddressType_EnumType

OECD301 OECD302 OECD303 OECD304 OECD305

residentialOrBusiness residential business registeredOffice unspecified

stf:OECDNameType_EnumType

OECD201 OECD202 OECD203 OECD204 OECD205 OECD206 OECD207 OECD208

SMFAliasOrOther indiv (individual) alias (alias) nick (nickname) aka (also known as) dba (doing business as) legal (legal name) atbirth (name at birth)

crs:EquityInterestType_EnumType

CRS401 CRS402 CRS403 CRS404 CRS405 CRS406 CRS407 CRS408 CRS409 CRS410

EIH of legal arrangements - trust - settlor EIH of legal arrangements - trust - trustee EIH of legal arrangements - trust - protector EIH of legal arrangements - trust - beneficiary EIH of legal arrangements - trust - other EIH of legal arrangements - other - settlor-equivalent EIH of legal arrangements - other - trustee-equivalent EIH of legal arrangements - other - protector-equivalent EIH of legal arrangements - other - beneficiary-equivalent EIH of legal arrangements - other - other equivalent

crs:CrsSelfCert_EnumType

CRS901 CRS902 CRS900

TRUE FALSE not reported

rs:CrsSelfCertforCtrlgPersonType_EnumTyp

CRS1001 CRS1002 CRS1000

TRUE FALSE not reported

crs:CrsAccountType_EnumType

CRS1101 CRS1102 CRS1103 CRS1104 CRS1100

Depository Account Custodial Account Cash Value Insurance Contract or Annuity Contract Debt or Equity Interest in Investment Entity not reported

crs:OpeningDate_EnumType

CRS1201 CRS1202 CRS1200

New Account Preexisting Account not reported

iso:CountryCode_Type

Landesname s.u. Zwgeibuchstabiges Längderkürzel ,

g

iso:currCode_Type

Erlaubter Wert s.u Landeswährung

Deutsche Bezeichnung

Wertemenge / Erklärung
***Non CRS*** ***Non CRS***

***Non CRS***

Deutsche Währungsbezeichnung

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel
AF AX AL DZ AS AD AO

Englische Umschreibung des Länderkürzels
AFGHANISTAN ALAND ISLANDS ALBANIA ALGERIA AMERICAN SAMOA ANDORRA ANGOLA

AI

ANGUILLA

AQ

ANTARCTICA

AG

ANTIGUA AND BARBUDA

AR

ARGENTINA

AM

ARMENIA

AW

ARUBA

AU

AUSTRALIA

AT

AUSTRIA

AZ

AZERBAIJAN

BS

BAHAMAS

BH

BAHRAIN

BD

BANGLADESH

BB

BARBADOS

BY

BELARUS

BE

BELGIUM

BZ

BELIZE

BJ

BENIN

BM

BERMUDA

BT

BHUTAN

BO

BOLIVIA, PLURINATIONAL STATE OF

BQ

BONAIRE, SINT EUSTATIUS AND SABA

BA

BOSNIA AND HERZEGOVINA

BW

BOTSWANA

BV

BOUVET ISLAND

BR

BRAZIL

IO

BRITISH INDIAN OCEAN TERRITORY

BN

BRUNEI DARUSSALAM

BG

BULGARIA

BF

BURKINA FASO

BI

BURUNDI

KH

CAMBODIA

CM

CAMEROON

CA

CANADA

CV

CABO VERDE

KY

CAYMAN ISLANDS

CF

CENTRAL AFRICAN REPUBLIC

TD

CHAD

CL

CHILE

CN

CHINA

CX

CHRISTMAS ISLAND

CC

COCOS (KEELING) ISLANDS

CO

COLOMBIA

KM

COMOROS

CG

CONGO

CD

CONGO, THE DEMOCRATIC REPUBLIC OF THE

iso:currCode_Type:

Wert AED AFN ALL AMD ANG AOA ARS
AUD AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BOV BRL BSD BTN BWP BYN BYR BZD CAD CDF CHE CHF CHW CLF CLP CNY COP COU CRC CUC CUP CVE CZK DJF DKK DOP DZD EGP ERN ETB EUR FJD FKP

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

G3:G129UNITEDARABEMIRATES

UAE Dirham

AFGHANISTAN

Afghani

ALBANIA

Lek

ARMENIA

Armenian Dram

CURACAO;SINTMAARTEN(DUTCHPART)

Netherlands Antillean Guilder

ANGOLA

Kwanza

ARGENTINA

Argentine Peso

AUSTRALIA;CHRISTMASISLAND;COCOS(KEELING)ISLAN

DS;HEARDISLANDANDMcDONALDISLANDS;KIRIBATI;NAU

RU;NORFOLKISLAND;TUVALU

Australian Dollar

ARUBA

Aruban Florin

AZERBAIJAN

Azerbaijan Manat

BOSNIAANDHERZEGOVINA

Convertible Mark

BARBADOS

Barbados Dollar

BANGLADESH

Taka

BULGARIA

Bulgarian Lev

BAHRAIN

Bahraini Dinar

BURUNDI

Burundi Franc

BERMUDA

Bermudian Dollar

BRUNEIDARUSSALAM

Brunei Dollar

BOLIVIA,PLURINATIONALSTATEOF

Boliviano

BOLIVIA,PLURINATIONALSTATEOF

Mvdol

BRAZIL

Brazilian Real

BAHAMAS

Bahamian Dollar

BHUTAN

Ngultrum

BOTSWANA

Pula

BELARUS

Belarusian Ruble

BELARUS

Belarussian Ruble (Historic use)

BELIZE

Belize Dollar

CANADA

Canadian Dollar

CONGO,THEDEMOCRATICREPUBLICOF

Congolese Franc

SWITZERLAND

WIR Euro

LIECHTENSTEIN;SWITZERLAND

Swiss Franc

SWITZERLAND

WIR Franc

CHILE

Unidad de Fomento

CHILE

Chilean Peso

CHINA

Yuan Renminbi

COLOMBIA

Colombian Peso

COLOMBIA

Unidad de Valor Real

COSTARICA

Costa Rican Colon

CUBA

Peso Convertible

CUBA

Cuban Peso

CABOVERDE

Cabo Verde Escudo

CZECHIA

Czech Koruna

DJIBOUTI

Djibouti Franc

DENMARK;FAROEISLANDS;GREENLAND

Danish Krone

DOMINICANREPUBLIC

Dominican Peso

ALGERIA

Algerian Dinar

EGYPT

Egyptian Pound

ERITREA

Nakfa

ETHIOPIA

Ethiopian Birr

EU

Euro

FIJI

Fiji Dollar

FALKLANDISLANDS(MALVINAS)

Falkland Islands Pound

CRS-XML Schema 12.11.2025

Bundeszentralamt für Steuern

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel
CK CR CI HR CU CW CY CZ DK DJ DM DO EC EG SV GQ ER EE ET FK FO FJ FI FR GF PF TF GA GM GE DE GH GI GR GL GD GP GU GT GG GN GW GY HT HM VA HN HK HU IS IN ID IR

Englische Umschreibung des Länderkürzels
COOK ISLANDS COSTA RICA COTE D'IVOIRE CROATIA CUBA CURACAO CYPRUS CZECHIA DENMARK DJIBOUTI DOMINICA DOMINICAN REPUBLIC ECUADOR EGYPT EL SALVADOR EQUATORIAL GUINEA ERITREA ESTONIA ETHIOPIA FALKLAND ISLANDS (MALVINAS) FAROE ISLANDS FIJI FINLAND FRANCE FRENCH GUIANA FRENCH POLYNESIA FRENCH SOUTHERN TERRITORIES GABON GAMBIA GEORGIA GERMANY GHANA GIBRALTAR GREECE GREENLAND GRENADA GUADELOUPE GUAM GUATEMALA GUERNSEY GUINEA GUINEA-BISSAU GUYANA HAITI HEARD ISLAND AND MCDONALD ISLANDS HOLY SEE (VATICAN CITY STATE) HONDURAS HONG KONG HUNGARY ICELAND INDIA INDONESIA IRAN, ISLAMIC REPUBLIC OF

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

iso:currCode_Type:

Wert
GBP GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD MMK MNT MOP MRO MRU MUR MVR MWK MXN MXV

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

GUERNSEY;ISLEOFMAN;JERSEY;UNITEDKINGDOMOFGR

EATBRITAINANDNORTHERNIRELAND

Pound Sterling

GEORGIA

Lari

GHANA

Ghana Cedi

GIBRALTAR

Gibraltar Pound

GAMBIA

Dalasi

GUINEA

Guinean Franc

GUATEMALA

Quetzal

GUYANA

Guyana Dollar

HONGKONG

Hong Kong Dollar

HONDURAS

Lempira

CROATIA

Kuna

HAITI

Gourde

HUNGARY

Forint

INDONESIA

Rupiah

ISRAEL

New Israeli Sheqel

BHUTAN;INDIA

Indian Rupee

IRAQ

Iraqi Dinar

IRAN,ISLAMICREPUBLICOF

Iranian Rial

ICELAND

Iceland Krona

JAMAICA

Jamaican Dollar

JORDAN

Jordanian Dinar

JAPAN

Yen

KENYA

Kenyan Shilling

KYRGYZSTAN

Som

CAMBODIA

Riel

COMOROS

Comorian Franc

KOREA,DEMOCRATICPEOPLEâ€™SREPUBLICOF

North Korean Won

KOREA,REPUBLICOF

Won

KUWAIT

Kuwaiti Dinar

CAYMANISLANDS

Cayman Islands Dollar

KAZAKHSTAN

Tenge

LAOPEOPLEâ€™SDEMOCRATICREPUBLIC

Lao Kip

LEBANON

Lebanese Pound

SRILANKA

Sri Lanka Rupee

LIBERIA

Liberian Dollar

LESOTHO

Loti

LITHUANIA

Lithuanian Litas (Historic use)

LATVIA

Latvian Lats (Historic use)

LIBYA

Libyan Dinar

MOROCCO;WESTERNSAHARA

Moroccan Dirham

MOLDOVA,REPUBLICOF

Moldovan Leu

MADAGASCAR

Malagasy Ariary

MACEDONIA,THEFORMERYUGOSLAVREPUBLICOF

Denar

MYANMAR

Kyat

MONGOLIA

Tugrik

MACAO

Pataca

MAURITANIA

Ouguiya (Historic use)

MAURITANIA

Ouguiya

MAURITIUS

Mauritius Rupee

MALDIVES

Rufiyaa

MALAWI

Malawi Kwacha

MEXICO

Mexican Peso

MEXICO

Mexican Unidad de Inversion (UDI)

CRS-XML Schema 12.11.2025

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel
IQ IE IM IL IT JM JP
JE JO KZ KE KI KP KR KW KG LA LV LB LS LR LY LI LT LU MO MK MG MW MY MV ML MT MH MQ MR MU YT MX FM MD MC MN ME MS MA MZ MM

Englische Umschreibung des Länderkürzels
IRAQ IRELAND ISLE OF MAN ISRAEL ITALY JAMAICA JAPAN
JERSEY JORDAN KAZAKHSTAN KENYA KIRIBATI KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF KOREA, REPUBLIC OF KUWAIT KYRGYZSTAN LAO PEOPLE'S DEMOCRATIC REPUBLIC LATVIA LEBANON LESOTHO LIBERIA LIBYA LIECHTENSTEIN LITHUANIA LUXEMBOURG MACAO NORTH MACEDONIA MADAGASCAR MALAWI MALAYSIA MALDIVES MALI MALTA MARSHALL ISLANDS MARTINIQUE MAURITANIA MAURITIUS MAYOTTE MEXICO MICRONESIA, FEDERATED STATES OF MOLDOVA, REPUBLIC OF MONACO MONGOLIA MONTENEGRO MONTSERRAT MOROCCO MOZAMBIQUE MYANMAR

iso:currCode_Type:

Wert
MYR MZN NAD NGN NIO NOK NPR
NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD SSP STD STN SVC SYP SZL THB TJS TMT TND TOP TRY TTD TWD TZS UAH UGX

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

MALAYSIA MOZAMBIQUE NAMIBIA NIGERIA NICARAGUA BOUVETISLAND;NORWAY;SVALBARDANDJANMAYEN NEPAL

Malaysian Ringgit Mozambique Metical Namibia Dollar Naira Cordoba Oro Norwegian Krone Nepalese Rupee

COOKISLANDS;NEWZEALAND;NIUE;PITCAIRN;TOKELAU OMAN PANAMA PERU PAPUANEWGUINEA PHILIPPINES PAKISTAN POLAND PARAGUAY QATAR ROMANIA SERBIA RUSSIANFEDERATION RWANDA SAUDIARABIA SOLOMONISLANDS SEYCHELLES SUDAN SWEDEN SINGAPORE SAINTHELENA,ASCENSIONANDTRISTANDACUNHA SIERRALEONE SOMALIA SURINAME SOUTHSUDAN SAOTOMEANDPRINCIPE SAOTOMEANDPRINCIPE ELSALVADOR SYRIANARABREPUBLIC ESWATINI THAILAND TAJIKISTAN TURKMENISTAN TUNISIA TONGA TURKEY TRINIDADANDTOBAGO TAIWAN,PROVINCEOFCHINA TANZANIA,UNITEDREPUBLICOF UKRAINE UGANDA

New Zealand Dollar Rial Omani Balboa Sol Kina Philippine Peso Pakistan Rupee Zloty Guarani Qatari Rial Romanian Leu Serbian Dinar Russian Ruble Rwanda Franc Saudi Riyal Solomon Islands Dollar Seychelles Rupee Sudanese Pound Swedish Krona Singapore Dollar Saint Helena Pound Leone Somali Shilling Surinam Dollar South Sudanese Pound Dobra (Historic use) Dobra El Salvador Colon Syrian Pound Lilangeni Baht Somoni Turkmenistan New Manat Tunisian Dinar Paâ€™anga Turkish Lira Trinidad and Tobago Dollar New Taiwan Dollar Tanzanian Shilling Hryvnia Uganda Shilling

CRS-XML Schema 12.11.2025

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

CRS-XML Schema 12.11.2025

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel

Englische Umschreibung des Länderkürzels

NA

NAMIBIA

NR

NAURU

NP

NEPAL

NL

NETHERLANDS

NC

NEW CALEDONIA

NZ

NEW ZEALAND

NI

NICARAGUA

NE

NIGER

NG

NIGERIA

NU

NIUE

NF

NORFOLK ISLAND

MP

NORTHERN MARIANA ISLANDS

NO

NORWAY

OM

OMAN

PK

PAKISTAN

PW

PALAU

PS

PALESTINE, STATE OF

PA

PANAMA

PG

PAPUA NEW GUINEA

PY

PARAGUAY

PE

PERU

PH

PHILIPPINES

PN

PITCAIRN

PL

POLAND

PT

PORTUGAL

PR

PUERTO RICO

QA

QATAR

RE

REUNION

RO

ROMANIA

RU

RUSSIAN FEDERATION

RW

RWANDA

BL

SAINT BARTHELEMY

SH

SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA

KN

SAINT KITTS AND NEVIS

LC

SAINT LUCIA

MF

SAINT MARTIN (FRENCH PART)

PM

SAINT PIERRE AND MIQUELON

VC

SAINT VINCENT AND THE GRENADINES

WS

SAMOA

iso:currCode_Type:

Wert
USD USN USS UYI UYU UYW UZS VEF VES VND VUV WST
XAF XAG XAU XBA XBB XBC XBD
XCD XDR XFU
XOF XPD
XPF XPT
XSU
XUA XXX YER ZAR ZMW ZWL

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

AMERICANSAMOA;BONAIRE;SINTEUSTATIUSANDSABA;

BRITISHINDIANOCEANTERRITORY;ECUADOR;ELSALVAD

OR;GUAM;HAITI;MARSHALLISLANDS;MICRONESIA,FEDE

RATEDSTATESOF;NORTHERNMARIANAISLANDS;PALAU;

PANAMA;PUERTORICO;TIMOR-

LESTE;TURKSANDCAICOSISLANDS;UNITEDSTATES;UNI

TEDSTATESMINOROUTLYINGISLANDS;VIRGINISLANDS(

BRITISH);VIRGINISLANDS(US)

US Dollar

UNITEDSTATES

US Dollar (Next day)

UNITEDSTATES

US Dollar (Same day) Historic use

URUGUAY

Uruguay Peso en Unidades Indexadas (UI)

URUGUAY

Peso Uruguayo

URUGUAY

Unidad Previsional

UZBEKISTAN

Uzbekistan Sum

VENEZUELA,BOLIVARIANREPUBLICOF

Bolivar (Historic use)

VENEZUELA,BOLIVARIANREPUBLICOF

BolÃ-var Soberano

VIETNAM

Dong

VANUATU

Vatu

SAMOA

Tala

CAMEROON;CENTRALAFRICANREPUBLIC;CHAD;CONGO

;EQUATORIALGUINEA;GABON

CFA Franc BEAC

ZZ11_Silver

Silver

ZZ08_Gold

Gold

ZZ01_BondMarketsUnitEuropean_EURCO

Bond Markets Unit European Composite Unit (EURCO)

ZZ02_BondMarketsUnitEuropean_EMU-6

Bond Markets Unit European Monetary Unit (E.M.U.-6)

ZZ03_BondMarketsUnitEuropean_EUA-9

Bond Markets Unit European Unit of Account 9 (E.U.A.-9)

ZZ04_BondMarketsUnitEuropean_EUA-17

Bond Markets Unit European Unit of Account 17 (E.U.A.-17)

ANGUILLA;ANTIGUAANDBARBUDA;DOMINICA;GRENADA;

MONTSERRAT;SAINTKITTSANDNEVIS;SAINTLUCIA;SAIN

TVINCENTANDTHEGRENADINES

East Caribbean Dollar

INTERNATIONALMONETARYFUND(IMF)

SDR (Special Drawing Right)

ZZ05_UIC-Franc

UIC-Franc (Historic use)

BENIN;BURKINAFASO;COTED'IVOIRE;GUINEA-

BISSAU;MALI;NIGER;SENEGAL;TOGO

CFA Franc BCEAO

ZZ09_Palladium

Palladium

FRENCHPOLYNESIA;NEWCALEDONIA;WALLISANDFUTU

NA

CFP Franc

ZZ10_Platinum

Platinum

SISTEMAUNITARIODECOMPENSACIONREGIONALDEPAG

OSSUCRE

Sucre

MEMBERCOUNTRIESOFTHEAFRICANDEVELOPMENTBA

NKGROUP

ADB Unit of Account

ZZ07_No_Currency

The codes assigned for transactions where no currency is involved

YEMEN

Yemeni Rial

LESOTHO;NAMIBIA;SOUTHAFRICA ZAMBIA

Rand Zambian Kwacha

ZIMBABWE

Zimbabwe Dollar

Bundeszentralamt für Steuern

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel
SM ST SA SN RS SC SL SG SX SK SI SB SO ZA GS SS ES LK SD SR SJ SZ SE CH SY TW TJ TZ TH TL TG TK TO TT TN TR TM TC TV UG UA AE GB
US UM UY UZ VU VE VN VG VI WF EH

Englische Umschreibung des Länderkürzels
SAN MARINO SAO TOME AND PRINCIPE SAUDI ARABIA SENEGAL SERBIA SEYCHELLES SIERRA LEONE SINGAPORE SINT MAARTEN (DUTCH PART) SLOVAKIA SLOVENIA SOLOMON ISLANDS SOMALIA SOUTH AFRICA SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS SOUTH SUDAN SPAIN SRI LANKA SUDAN SURINAME SVALBARD AND JAN MAYEN ESWATINI SWEDEN SWITZERLAND SYRIAN ARAB REPUBLIC TAIWAN, PROVINCE OF CHINA TAJIKISTAN TANZANIA, UNITED REPUBLIC OF THAILAND TIMOR-LESTE TOGO TOKELAU TONGA TRINIDAD AND TOBAGO TUNISIA TURKEY TURKMENISTAN TURKS AND CAICOS ISLANDS TUVALU UGANDA UKRAINE UNITED ARAB EMIRATES UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND
UNITED STATES UNITED STATES MINOR OUTLYING ISLANDS URUGUAY UZBEKISTAN VANUATU VENEZUELA, BOLIVARIAN REPUBLIC OF VIET NAM VIRGIN ISLANDS, BRITISH VIRGIN ISLANDS, U.S. WALLIS AND FUTUNA WESTERN SAHARA

iso:currCode_Type:

Wert

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

CRS-XML Schema 12.11.2025

Bundeszentralamt für Steuern

iso:CountryCode_Type
Zweibuchstabiges Länderkürzel
YE ZM ZW XK

Englische Umschreibung des Länderkürzels
YEMEN ZAMBIA ZIMBABWE KOSOVO

Aufbau der zu meldenden Daten nach CRS-XML-Schema Version 3.0

iso:currCode_Type:

Wert

Englische Bezeichnung des Landes, welche die Währung

als Landeswährung verwendet

Währungsbezeichnung

CRS-XML Schema 12.11.2025
