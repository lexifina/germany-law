# Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der amtlich bestimmten Schnittstelle für Meldungen an das Bundeszentralamt für Steuern

- Herausgeber: Bundesministerium der Finanzen
- Datum: 2026-01-14
- Art: BMF-Schreiben
- Sachgebiet (BMF): Weitere_Steuerthemen / Organisation_Automation
- Quelle: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Organisation_Automation/2026-01-14-KStTG-amtl-vorgeschriebener-datensatz.html
- PDF: https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Weitere_Steuerthemen/Organisation_Automation/2026-01-14-KStTG-amtl-vorgeschriebener-datensatz.pdf?__blob=publicationFile&v=3
- Text: Textebene der amtlichen PDF-Datei, unverändert

---

Bundesministerium der Finanzen, 11016 Berlin
Nur per E-Mail Oberste Finanzbehörden der Länder nachrichtlich: Bundeszentralamt für Steuern

Wilhelmstraße 97 10117 Berlin Tel. +49 30 18 682-0 poststelle@bmf.bund.de www.bundesfinanzministerium.de 14. Januar 2026

Betreff: Gesetz über die Meldepflicht von Anbietern und den automatischen Austausch von Informationen in Steuersachen bei Kryptowerte-Dienstleistungen (KryptowerteSteuertransparenz-Gesetz – KStTG) Bekanntgabe des amtlich vorgeschriebenen Datensatzes und der amtlich bestimmten Schnittstelle für Meldungen an das Bundeszentralamt für Steuern
Anlagen: 1 GZ: IV D 3 - S 1316/00708/051/004 DOK: COO.7005.100.2.13689614 Seite 1 von 3
(bei Antwort bitte GZ und DOK angeben)
Durch das Gesetz über die Meldepflicht von Anbietern und den automatischen Austausch von Informationen in Steuersachen bei Kryptowerte-Dienstleistungen (KryptowerteSteuertransparenz-Gesetz – KStTG) wird die Richtlinie (EU) 2023/2226 des Rates vom 17. Oktober 2023 zur Änderung der Richtlinie 2011/16/EU über die Zusammenarbeit der Verwaltungsbehörden im Bereich der Besteuerung (ABl. L, 2023/2226, 24.10.2023) in nationales Recht umgesetzt. § 9 Absatz 1 Satz 1 des Kryptowerte-Steuertransparenz-Gesetzes (KStTG) verpflichtet Anbieter zur Meldung der in § 11 KStTG genannten Informationen an das Bundeszentralamt für Steuern (BZSt) gemäß den Vorgaben des § 12 Satz 1 KStTG. Dies gilt erstmalig für Informationen für das Kalenderjahr 2026, die in 2027 zu melden sind.
Die Meldung der Anbieter an das BZSt hat gemäß § 12 Satz 1 KStTG nach amtlich vorgeschriebenem Datensatz elektronisch im Wege der Datenfernübertragung über amtlich bestimmte Schnittstellen zu erfolgen.
Nähere Informationen zur Datenübermittlung nach dem allgemeinen Meldestandard können auf der Internetseite des BZSt (www.bzst.bund.de) sowie in den zukünftig dort abgelegten Kommunikationshandbüchern abgerufen werden.
Hiermit wird der amtlich vorgeschriebene Datensatz entsprechend § 87b Absatz 1 der Abgabenordnung und nach § 12 Satz 2 KStTG veröffentlicht. Das Datenschema wird nachfolgend

Seite 2 von 3 dargestellt und steht im Internet unter www.bzst.bund.de zur Ansicht und zum Abruf bereit. 1. Datenübermittlung über die DIP-Schnittstelle für Massendatenmelder Gesamtstruktur der Datenübermittlung (DIP) Der Aufbau der XML-Struktur für die Datenübermittlung entspricht der DIP-Schnittstelle (Digitaler Posteingang). Das Wurzelelement der gesamten zu übertragenden XML-Datei ist dip:dip. Dieses umschließt den dip:header-Abschnitt, der alle Informationen des Senders für die Fachverfahrens- und Sender-Zuordnung enthält. Darauf folgt der dip:body, der die eigentlichen Fachdaten beinhaltet. Für die korrekte Verarbeitung muss im dip:application-Element das Attribut code den Wert „CARF“ beinhalten.
Die zugehörigen XML Schema Definitionen sowie weitere Erläuterungen sind auf der Internetseite des BZSt (www.bzst.bund.de) in den dort abgelegten Kommunikationshandbüchern abrufbar. CARF-XML-Schema Version 1.5 Mit dieser Bekanntgabe wird die amtliche Datensatzbeschreibung für CARF-Meldungen in der Version 1.5 des CARF-XML-Schemas veröffentlicht. Das Datenschema ist entsprechend § 9 Absatz 1 Satz 1 in Verbindung mit § 21 KStTG für Daten zu verwenden, die ab dem erstmaligen Meldezeitraum vom 1. Januar 2026 bis zum 31. Dezember 2026 erhoben wurden und im Wege der Datenfernübertragung bis zum 31. Juli des dem Meldezeitraum folgenden Kalenderjahres zu übermitteln sind.

Seite 3 von 3
Das CARF-XML-Schema führt eine neue Datenart und entsprechende Wertelisten ein. Datenübermittler werden aufgefordert, ihre Systeme rechtzeitig auf die Schema-Version 1.5 vorzubereiten. Die detaillierten Spezifikationen aller Angaben sind der nachfolgenden amtlichen Datensatzbeschreibung zu entnehmen.
Sobald die CARF-spezifischen Kommunikationshandbücher verfügbar sind, wird auf der Internetseite des BZSt (www.bzst.bund.de) darüber informiert.
Aufbau der XML-Datei Die Datensatzbeschreibung für den Aufbau der zu meldenden Daten ist als Anlage beigefügt.
2. Datenübermittlung über das BZSt online.portal
Verwendung des Massendaten-XML-Uploads Das BZSt online.portal bietet neben dem Formular auch die Möglichkeit, eine XML-Datei manuell hochzuladen. Das Formular für den XML-Upload finden Sie nach dem Login im BZSt online.portal unter "Portal"/"Massendaten-Upload starten".
Im Gegensatz zur automatisierten Übermittlung über die DIP-Schnittstelle (Abschnitt I) darf beim manuellen Upload nur die Fachdaten-XML carf:CARF_OECD hochgeladen werden. Die Datei darf keinen DIP-Umschlag dip:dip enthalten.
Nähere Informationen zur Datenübermittlung über den Massendaten-XML-Upload können der Internetseite des BZSt (www.bzst.bund.de) entnommen werden.
3. Erstmalige Anwendung
Das Datenschema ist entsprechend des KStTG für Daten zu verwenden, die nach dem Meldestandard für den erstmaligen Meldezeitraum vom 1. Januar 2026 bis zum 31. Dezember 2026 erhoben wurden und im Wege der Datenfernübertragung an das BZSt bis zum 31. Juli 2027 zu übermitteln sind.
Dieses Schreiben steht ab sofort auf der Internetseite des Bundesministeriums der Finanzen und des BZSt zur Ansicht und zum Abruf bereit. Die Veröffentlichung erfolgt im Bundessteuerblatt Teil I.
Im Auftrag
Dieses Dokument wurde elektronisch erstellt und ist ohne Unterschrift gültig.

g Aufbau der zu meldenden Daten nach CARF-XML-Schema v1.5 der OECD
Stand 12.11.2025

Komplexe Datentypen
XML Attribute L-Spalte
Kardinalität -Spalte 1
1..n 0..1 0..n P O B - Spalte
P
O
B
Format - Spalte an n b d dt en

Legende
Komplexe Datentypen sind in der Datensatzbeschreibung an der entsprechenden Stelle mit Fettschrift gekennzeichnet und dort entsprechend zu ersetzen.
XML Attribute sind kursiv geschrieben
Ebene im XML
Erläuterung: Der Datentyp muss genau 1x verwendet werden. Der Datentyp muss mindestens 1x verwendet werden. Er kann danach beliebig oft wiederholt werden. Der Datentyp kann entfallen oder 1x verwendet werden. Der Datentyp kann entfallen oder beliebig oft wiederholt werden.
Erläuterung: Pflicht Dieses Gruppenelement oder Einzelfeld muss gefüllt sein. Option Dieses Gruppenelement oder Einzelfeld kann gefüllt sein. Bedingung Die Verwendung dieses Gruppenelements oder Einzelfeldes ist abhängig von einem anderen Gruppenelement oder Einzelfeld. Hinweise stehen in der Spalte Wertemenge / Erklärung.
Erläuterung: Alphanumerische Zeichen Numerische Zeichen incl. Punkt Boolsche Variable Datum Datum und Zeit Aufzählung

Datensatzbeschreibung Aufbau der zu meldenden Daten nach CARF-XML-Schema v1.5 der OECD
Stand 12.11.2025

Version 0.1 (Stand 12.11.2025)

Änderungshistorie
Änderungen Initiale Datensatzbeschreibung (Grundlage CARF-XML-Schema v.1.5 der OECD)

Bundeszentralamt für Steuern
Komplexe Datentypen
stf:DocSpec_Type stf:DocTypeIndic
stf:DocRefId
stf:CorrMessageRefId stf:CorrDocRefId

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

Deutsche Bezeichnung

1

P

en

stf:OECDDocTypeIndic_EnumType DocTypeIndic

1

P

an 1 200 stf:StringMin1Max200_Type

DocRefId

0..1 O

an 1 170 stf:StringMin1Max170_Type

0..1 O

an 1 200 stf:StringMin1Max200_Type

CorrMessageRefId CorrDocRefId

Wertemenge / Erklärung
Dieses Datenelement enthält Informationen zur Art der CARFDaten innerhalb des Datensatzes.
Dabei wird angegeben, ob es sich um eine Erstmeldung mit neuen Informationen handelt, oder um eine Folgemeldung, mit welcher bereits übermittelte Daten korrigiert und/oder gelöscht werden. Eine Verwendung verschieder DocTypeIndics innerhalb einer Meldung ist ausschließlich bei Korrekturmeldungen (MessageTypeIndic CARF702) mit den DocTypeIndics OECD2 und OECD3 möglich, wobei für den RCASP die Eintragung OECD0 zulässig ist, sofern das RCASP-Element weder geändert noch gelöscht werden soll.
Die Werte OECD10 bis OECD13 dürfen nur während abgestimmten Testzeiträumen oder auf Basis von bilateralen Abkommen über den Test ausgewählt werden. Hierdurch soll sichergestellt werden, dass Testdaten nicht mit Echtdaten vermischt werden.
Der Wertebereich des stf:OECDDocTypeIndic_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Dieses Datenelement enthält die Angabe zum eindeutigen Bezeichner (Referenz) einer bestimmten Datenelementgruppe, bzw. eines Teils eines Datensatzes der CARF-Meldung.
Für jeden Datensatz einer Korrektur oder Löschung muss demnach eine neue eindeutige DocRefId für zukünftige Referenzzwecke in Folgemeldungen vergeben werden.
Die DocRefId muss mit dem Staatencode des übermittelnden Staates beginnen. Danach folgt der Meldezeitraum und ein eindeutiger Bezeichner (frei zu vergebende Zeichenkombination). Beispiel: DE20261234567 Dieses Datenelement enthält bei Folgemeldungen die MessageRefId der vorherigen CARF-Meldung, die korrigiert oder gelöscht werden soll. Dieses Datenelement verweist bei Folgemeldungen auf die DocRefId der Datenelementgruppe einer vorherigen CARFMeldung, die korrigiert oder gelöscht werden soll.
Sie muss sich stets auf die letzte übermittelte Datensatzreferenz (DocRefID) beziehen. Auf diese Weise können mehrere Korrekturen oder Ergänzungen innerhalb einer Lieferkette bearbeitet werden, da jede Korrektur die vorherige(n) Angabe(n) vollständig ersetzt bzw. ersetzen.

Seite 3 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
carf:OrganisationParty_Type carf:ResCountryCode
carf:TIN
issuedBy unknown

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

1..n P

en 2 2

iso:CountryCode_Type

1..n P

an 1 200 carf:TIN_Type

0..1 B

en 2 2

iso:CountryCode_Type

0..1 B

b1 4

xsd:boolean

Deutsche Bezeichnung

Wertemenge / Erklärung

Ansässigkeitsstaat Steueridentifikationsnummer

Dieses wiederholbare Datenelement enthält den/die Ansässigkeitsstaat(en) des Rechtsträgers (KryptowerteNutzer oder meldender Anbieter, wenn es sich dabei um einen Rechtsträger handelt).
Werden mehrere Steueransässigkeitsstaaten ermittelt, sind alle diese Staaten zu melden.
Bei einem meldenden Anbieter, sollte der Ansässigkeitstaat mit demjenigen übereinstimmen, der auch im Meldungsteil des Nexus angegeben wurde.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zu den ISO-Types beschrieben. Dieses wiederholbare Datenelement enthält die Steueridentifikationsnummer (Tax Identification Number), die von der Steuerverwaltung, in welcher der Rechtsträger ansässig ist, verwendet wird.
Falls ein Rechtsträger als Kryptowerte-Nutzer keine TIN besitzt, weil eine solche vom Ansässigkeotsstaat nicht vergeben wird, sollte die Eintragung "NOTIN" vorgenommen werden und das Attribut "unknown" auf "true" gesetzt werden.
Falls die TIN zu einem Rechtsträger als meldender Anbieter, welche von der sendenden Behörde vergeben wurde, nicht bekannt ist, sollte die Eintragung "NOTIN" vorgenommen werden und das Attribut "unknown=true" gesetzt werden.
Wenn eine Eintragung zur TIN erfolgt, die nicht "NOTIN" lautet, kann dementsprechendnicht das Attribut mit dem Wert "unknown" zu diesem Rechtsträger enthalten sein.

Ausstellender Staat unbekannt

Attribut zu carf:TIN Dieses Attribut enthält die Angabe zu dem Staat, der die Steueridentifikationsnummer (TIN) ausgestellt hat. Die Angabe sollte immer erfolgen, wenn die Steueridentifikationsnummer nicht als unbekannt ("unknown") markiert ist.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zum iso:CountryCode_Type beschrieben. Attribut zu carf:TIN Dieses Attribut sollte angegeben werden, wenn keine Steueridentifikationsnummer (TIN) bekannt ist oder diese nicht existiert. Wird ein Wert für das Element carf:TIN angegeben, der nicht "NOTIN" lautet, und das Attribut "unknown" auf "true" gesetzt, erfolgt eine systemseitige Ablehnung.

Seite 4 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
noch carf:OrganisationParty_Type carf:IN
issuedBy
INType carf: IIN
issuedBy
carf:Name nameType
carf:Address

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

0..n O

an 1 200 carf:OrganisationIN_Type

0..1 O

en 2 2

iso:CountryCode_Type

1

O

en

carf:INType_EnumType

0..n O

an 1 200 carf: IndividualIN_Type

0..1 O

en 2 2

iso:CountryCode_Type

1..n P

an 1 200 stf:StringMin1Max200_Type

0..1 O

en

1..n P

stf:OECDNameType_EnumType carf:Address_Type

Deutsche Bezeichnung

Wertemenge / Erklärung

Entity Identification Number (EIN)

Dieses Datenelement kann weitere Identifikationsnummern enthalten. Dies können beispielsweise eine Registriernummer des meldenden Anbieters, oder die Handelsregisternummer (BRN) sein.

Weitere Identifikationsnummern zum Rechtsträger sollten angegeben werden, wenn diese vorhanden sind.

Ausstellender Staat

Attribut zu carf:IN Das Attribut enthält den Staat, der die Identifikationsnummer des Rechtsträgers ausgestellt hat. Ist dieser unbekannt soll das Element nicht angegeben werden.

Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zu den ISO-Types beschrieben.

Typ der Identifikationsnummer

Attribut zu carf:IN Dieses Attribut enthält Inforamtionen zur Art der Identifikationsnummer.

Individual Identification Number (IIN)

Der Wertebereich des carf:INType_EnumType wird im Wertebereich_Aufzählungstypen beschrieben. Dieses Datenelement enthält die individuelle Identifikationsnummer, die einem Kryptowerte-Betreiber im Rahmen des Registrierungsprozesses vergeben wird.

Ausstellender Staat

Die IIN zum Rechtsträger sollte angegeben werden, wenn diese vorhanden ist. Attribut zu carf:IIN Dieses Attribut enthält den Staat, der die Identifikationsnummer des Rechsträgers ausgestellt hat. Ist der ausstellende Staat nicht bekannt, sollte dieses Element nicht angegeben werden. (EU-spezifisch)

Name des Rechtsträgers
Typ des Namens
Anschrift des Sitzes/ Hauptanschrift

Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zum iso:CountryCode_Type beschrieben. Dieses Datenelement enthält den juristischen Namen des Rechtsträgers, einschließlich der inländischen Bezeichnung der Rechtsform, wie diese in der Satzung oder einem ähnlichen Dokument angegeben.
Attribut zu carf:Name Mit diesem Attribut kann der Typ des Namens angegeben werden, da in den Dokumenten mehrere Namen für die selbe Person vorliegen können.

Seite 5 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
carf:Address_Type legalAddressType
carf:CountryCode
carf:AddressFix carf:Street carf:BuildingIdentifier carf:SuiteIdentifier carf:FloorIdentifier carf:DistrictName carf:POB carf:PostCode carf:City carf:CountrySubentity
carf:AdditionalAddressInfo

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

Deutsche Bezeichnung

0..1 O

en

stf:OECDLegalAddressType_EnumTy Adresstyp pe

1

P

en 2 2

iso:CountryCode_Type

Staat

1

P

carf:AddressFix_Type

0..1 O

0..1 O

0..1 O

0..1 O

0..1 O

0..1 O

0..1 O

1

P

0..1 O

0..1 O

an 1 an 1 an 1 an 1 an 1 an 1 an 1 an 1 an 1 an 1

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 4000 stf:StringMin1Max4000_Type

Strukturierte Adresse
Straße Hausnummer Wohnungsbezeichnung Etagenbezeichnung Verwaltungsbezirk Postfach Postleitzahl Ort Bundesland/-staat Zusätzliche Adressangabe

Wertemenge / Erklärung
Attribut zu carf:Address_Type Das Attribut enthält den Typ der Adresse.
Der Wertebereich des stf:OECDLegalAddressType_EnumType wird in den Wertelisten für Aufzählungstypen beschrieben. Dieses Datenelement enthält den Ländercode, der mit der angegebenen Adresse verknüpft ist.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zu den ISO-Types beschrieben. Diese Datenelementgruppe mit einer strukturierten Adressangabe ist zu verwenden und muss mindestens die Angabe zum Ort enthalten. Informationen zur Straße sollten angegeben werden, wenn diese vorhanden sind. Informationen zur Hausnummer sollten angegeben werden, wenn diese vorhanden sind. Informationen zur Wohnungsbezeichnung sollten angegeben werden, wenn diese vorhanden sind. Informationen zur Etagenbezeichnung sollten angegeben werden, wenn diese vorhanden sind. Informationen zum Verwaltungsbezirk sollten angegeben werden, wenn diese vorhanden sind. Informationen zum Postfach sollten angegeben werden, wenn diese vorhanden sind. Informationen zur Postleitzahl sollten angegeben werden, wenn diese vorhanden sind. Informationen zum Ort müssen angegeben werden. Informationen zum Bundesland/-staat sollten angegeben werden, wenn diese vorhanden sind. Dieses Datenelement kann zusätzliche Informationen zur strukturierten Adressangabe (carf:AddressFix) enthalten, die in dem vorgegebenen Format nicht eingetragen werden konnten.

Seite 6 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
carf:PersonParty_Type carf:ResCountryCode
carf:TIN
issuedBy

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

1..n P

en 2 2

iso:CountryCode_Type

1..n P

an 1 200 carf:TIN_Type

0..1 O

en 2 2

iso:CountryCode_Type

Deutsche Bezeichnung

Wertemenge / Erklärung

Ansässigkeitsstaat Steueridentifikationsnummer Ausstellender Staat

Dieses wiederholbare Datenelement enthält den/die Ansässigkeitsstaat(en) der natürlichen Person (KryptowerteNutzer, beherrschende Person oder meldender Anbieter, wenn es sich dabei um eine natürliche Person handelt).
Bei Kryptowerte-Nutzern, bzw. beherrschenden Personen, sollte der/die Ansässigkeitstaat/en mit denjenigen übereinstimmen, die im Rahmen der Sorgfaltspflichten durch die Selbstaufkunft eingeholt wurden.
Werden mehrere Steueransässigkeitsstaaten ermittelt, sind alle diese Staaten zu melden.
Bei einem meldenden Anbieter, sollte der Ansässigkeitstaat mit demjenigen übereinstimmen, der auch im Meldungsteil des Nexus angegeben wurde.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten ISO-Type beschrieben. Dieses wiederholbare Datenelement enthält die Steueridentifikationsnummer (Tax Identification Number), die von der Steuerverwaltung, in welcher die natürliche Person ansässig ist, verwendet wird.
Falls eine natürliche Person als Kryptowerte-Nutzer oder beherrschende Person keine TIN besitzt, weil eine solche vom Ansässigkeitsstaat nicht vergeben wird, sollte die Eintragung "NOTIN" vorgenommen werden und das Attribut "unknown" auf "true" gesetzt werden.
Falls die TIN zu einer natürlichen Person, welche von der sendenden Behörde vergeben wurde, als meldender Anbieter nicht bekannt ist, sollte die Eintragung "NOTIN" vorgenommen werden und das Attribut "unknown=true" gesetzt werden.
Wenn eine Eintragung zur TIN erfolgt, die nicht "NOTIN" lautet, kann dementsprechendnicht das Attribut mit dem Wert "unknown" zu diesem Rechtsträger enthalten sein. Attribut zu carf:TIN Dieses Attribut enthält die Angabe zu dem Staat, der die Steueridentifikationsnummer (TIN) ausgestellt hat. Die Angabe sollte immer erfolgen, wenn die Steueridentifikationsnummer nicht als unbekannt ("unknown") markiert ist.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zum iso:CountryCode_Type beschrieben.

Seite 7 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
noch carf:PersonParty_Type unknown
carf: IIN
issuedBy
carf:Name nameType carf:PrecedingTitle carf:Title carf:FirstName
xnlNameType
carf:MiddleName xnlNameType

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

0..1 O

b1 4

xsd:boolean

0..n O

an 1 200 carf:IndividualIN_Type

0..1 O

en 2 2

iso:CountryCode_Type

1..n P

0..1 O

en

carf:NamePerson_Type stf:OECDNameType_EnumType

0..1 O

0..n O

1

P

an 1 an 1 an 1

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type

0..1 O

an 1 200 stf:StringMin1Max200_Type

0..n O 0..1 O

an 1 an 1

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type

Deutsche Bezeichnung unbekannt
Individuelle Identifikationsnummer (IIN)
Ausstellender Staat
Name Typ des Namens Vorangestellter Titel Titel Vorname
Typ des Vornamens
Zweitname (weitere Namen) Typ der weiteren Namen

Wertemenge / Erklärung
Attribut zu carf:TIN Dieses Attribut sollte angegeben werden, wenn keine Steueridentifikationsnummer (TIN) bekannt ist oder diese nicht existiert. Wird ein Wert für das Element carf:TIN angegeben, der nicht "NOTIN" lautet, und das Attribut "unknown" auf "true" gesetzt, erfolgt eine systemseitige Ablehnung. Dieses Datenelement enthält die individuelle Identifikationsnummer, die einem Kryptowerte-Betreiber im Rahmen des Registrierungsprozesses vergeben wird. (EUspezifisch)
Die IIN zur natürlichen Person sollte angegeben werden, wenn diese vorhanden ist. Attribut zu carf:IIN Dieses Attribut enthält den Staat, der die Identifikationsnummer der natürlichen Person ausgestellt hat. Ist der ausstellende Staat nicht bekannt, sollte dieses Element nicht angegeben werden. (EU-spezifisch)
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zum iso:CountryCode_Type beschrieben. Diese Datenelementgruppe ermöglicht die Angaben des Geburtsnamens und des Namens nach einer Heirat. Attribut zu carf:Name Mit diesem Attribut kann der Typ des Namens angegeben werden, da für die selbe Person mehrere Namen vorliegen können.
Dieses Datenelement enhält die Angabe zum Vornamen der natürlichen Person.
In Fällen in denen der übermittelnden Behörde kein Vorname vorliegt sollen die Initialen oder der Wert "NFN" ("No First Name") verwendet werden. Attribut zu carf:FirstName Mit diesem Attribut kann die Bedeutung des Vornamens definiert werden.
In einigen Ländern kann der Vorname ein Familienname oder ein Nachname sein. Dieses Datenelement kann den Zweitnamen bzw. weitere Namen der natürlichen Person enthalten. Attribut zu carf:MiddleName Mit diesem Attribut kann die Bedeutung des/der weiteren Namen definiert werden.

Seite 8 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
noch carf:PersonParty_Type carf:NamePrefix xnlNameType
carf:LastName
xnlNameType
carf:GenerationIdentifier carf:Suffix carf:GeneralSuffix carf:Address carf:Nationality carf:BirthInfo carf:BirthDate carf:BirthPlace
carf:City carf:CitySubentity carf:CountryInfo
carf:CountryCode

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

0..1 O 0..1 O

an 1 an 1

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type

1

P

an 1 200 stf:StringMin1Max200_Type

0..1 O

an 1 200 stf:StringMin1Max200_Type

0..n O 0..n O 0..1 O 1..n P 0..n O

1

P

1

P

0..1 B

an 1 an 1 an 1
en

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type
carf:Address_Type iso:CountryCode_Type

d

xsd:date

carf:BirthPlace_Type

1

P

0..1 O

1

P

an 1 an 1

200 stf:StringMin1Max200_Type 200 stf:StringMin1Max200_Type

0..1 B

en 2 2

iso:CountryCode_Type

Deutsche Bezeichnung Namenszusatz Typ des Namenszusatzes
Nachname
Typ des Nachnamens
Generationszusatz Titelzusatz Allgemeiner Zusatz Hauptanschrift Nationalität Angaben zur Geburt Geburtsdatum Geburtsort
Stadt Stadtteil Information zum Staat der Geburt
Staat

Wertemenge / Erklärung
Attribut zu carf:NamePrefix Mit diesem Attribut kann die Bedeutung des Namenszusatzes definiert werden. Dieses Datenelement enthält den offiziellen, rechtmäßigen Namen einer natürlichen Person (meldender Anbieter, Kryptowerte-Nutzer oder der beherrschenden Person).
Nach Möglichkeit sollte immer der Vorname und Nachname in den jeweiligen Elementen getrennt und nicht in einem der Elemente zusammen angegeben werden. Attribut zu carf:LastName Mit diesem Attribut kann die Bedeutung des Nachnamens definiert werden.
Dieses Datenelement enthält Informationen zur Nationalität der natürlichen Person. Diese Datenelementgruppe enthält Informationen zur Geburt der natürlichen Person. Dieses Datenelement enthält die Angabe des Geburtsdatum im Format: JJJJ-MM-TT. Dieses Datenelement enthält Informationen zum Geburtsort der natürlichen Person, sofern der meldende Anbieter nach innerstaatlichem Recht dazu verpflichtet ist, diesen zu erheben.
Wenn der Geburtsort angegeben wird, sollte die zugehörige Stadt, sowie der Staat (bestehender Staat oder ehemaliger, nicht mehr existierender Staat) angegeben werden.
Diese Datenelementgruppe ermöglicht die Auswahl zwischen der Angabe eines bestehenden Staates (gekennzeichnet durch einen zweistelligen Ländercode) oder eines ehemaligen Staatennamens (gekennzeichnet durch den Namen).
Dieses Datenelement ist verpflichtend anzugeben, wenn der Geburtsort angegeben wurde und keine Angabe zum Element "Ehemaliger Name des Staates" erfolgt.
Der Wertebereich des iso:CountryCode_Type wird in den Wertelisten zu den ISO-Types beschrieben.

Seite 9 von 35

Bundeszentralamt für Steuern
Komplexe Datentypen
carf:FormerCountryName

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Kardinalität
0..1

ForP O B mat Min Max

B

an 1 200

Datentyp stf:StringMin1Max200_Type

Deutsche Bezeichnung Ehemaliger Name des Staates

Wertemenge / Erklärung
Dieses Datenelement ist verpflichtend anzugeben, wenn der Geburtsort angegeben wurde und keine Angabe zum Element "Staat" erfolgt.

Die Auswahl des ehemaligen Staatenamens soll erfolgen, wenn die Person in einem Staat geboren ist, der nicht mehr existiert. Insoweit ist der ehemalige Name einzutragen.

Seite 10 von 35

DIP
L1 dip:dip

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12
version dip:header environment

dip:consignment dip:customerIdentifier
dip:identityProvider
dip:identifier dip:creationTime dip:transferticketId dip:referenceId dip:application code
dip:body dip:consignmentItem

Datensatzbeschreibung Aufbau der Daten nach DIP-XML-Schema

Kardi-

For-

nalität P O B mat Min Max Datentyp

1

P

1

P

an

xs:string

1

P

1

P

en

DipHeaderType environmentType

1

P

1

P

1

P

en

ConsignmentType CustomerIdentifierType
identityProviderType

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

an 1 16 identifierType

dt

xs:dateTime

an 1 170 customTicketIdNumberType

an 1 170 customTicketIdNumberType

applicationType an 1 12 applicationCodeType

1

P

1..n P

DipBodyType ConsignmentItemType

Deutsche Bezeichnung dip Version

Wertemenge / Erklärung
Digitaler Posteingang (dip) Wurzelverzeichnis Dieser Bestandteil ist stets über die Schemadefinition der dip.xsd zu überprüfen. Attribut zu dip:dip Version der dip Definition. Es ist nur der Wert 2.0 zulässig.

Zielumgebung

Attribut zu dip:header

Es können nur die Werte

• TEST

• PROD

verwendet werden.

Aus datenschutzrechtlichen Gründen dürfen Testdaten nur

unter Verwendung des Wertes "TEST" und Produktivdaten

nur unter Verwendung des Wertes "PROD" übermittelt

werden.

Sendungsdaten Identifikationskennung

Identifikationskennung des Datenübermittlers, anhand dieser

eineindeutig verifiziert werden kann. I.d.R. eine dem

Fachverfahren/Fachbereich bekannte Kennung z.B. 13-

stellige Steuernummer oder BZSt-Zertifikats-Nummer.

Provider der Identifier-

Festlegung, welchem Provider die Identifier-Kennung

Kennung

zuzuordnen ist: BZST-CERT einem BZSt-Zertifikat, ELSTER

einem ELSTER-Konto

Es können nur die Werte

• BZST-CERT

• ELSTER

verwendet werden.

Identifier-Kennung

BZSt-Nummer oder Steuernummer, entsprechend dem

gewählten Providertyp.

Erzeugungszeitpunkt

Erzeugungszeitpunkt der Lieferung als Zeitstempel

Identifikationsnummer der Identifikationsnummer der Lieferung, eine eineindeutige

Lieferung

Kennung dieser Lieferung

Identifikationsnummer einer Identifikationsnummer einer Bezugs-Lieferung als Referenz

Bezugs-Lieferung

auf die transferticketId einer vorhergehende Lieferung

Verfahrensbezeichnung

Bennenung des Ziel-Fachverfahrens

Fachverfahrensbezeichnung Attribut zu dip:application

Angabe zur Bezeichnung des Fachverfahrens

Hier ist der Wert "CARF" zu verwenden.

Inhalte der Lieferung

Meldungen

Multiplizität zur Lieferung mehrerer Anträge/Meldungen in einer Lieferung

Für CARF-Lieferungen darf nur ein dip:consignmentItem

übermittelt werden.

Seite 11 von 35

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

consignmentItemPosition

dip:bopAccountId dip:data

Datensatzbeschreibung Aufbau der Daten nach DIP-XML-Schema

Kardi-

For-

nalität P O B mat Min Max Datentyp

1

P

n0

xs:unsignedLong

0..1 O

1

P

an 1 36 bopAccountIdType xs:anyType

Deutsche Bezeichnung Position
Benutzerkennung Nutzdaten-XML

Wertemenge / Erklärung
Attribut zu dip:consigmentItem Position, die auch bei der Rückgabe des Protokolls im PayloadResultType verwendet wird. Zeigt die Korrelation zwischen Lieferung und Rückgabe für ein ConsignmentItem an. Das erste consignmentItem hat die Position 0. Für CARFLieferungen darf nur ein dip:consignmentItem übermittelt werden. Benutzerkennung des Antragstellers im POSt 2.0 (BOPNeu) für Zustellung eines Verwaltungsaktes im Portal An dieser Stelle sind die Nutzdaten im Format des Fachverfahrens-XMLs carf:CARF_OECD der OECD und EU anzugeben. Weitere Informationen zu diesem Schema sind unter CARF-DAC8 Nutzdaten zu finden.

Seite 12 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:CARF_OECD version

carf:MessageSpec

carf:SendingEntityIN carf:TransmittingCountry carf:ReceivingCountry

carf:MessageType carf:Warning carf:Contact

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max Datentyp

1

P

0..1 O

an 1 10

stf:StringMin1Max10_Type

1

P

carf:MessageSpec_Type

0..1 O

an 1 200 stf:StringMin1Max200_Type

1

P

en 2 2

iso:CountryCode_Type

1

P

en 2 2

iso:CountryCode_Type

1

P

en

carf:MessageType_EnumType

0..1 O

an 1 4000 stf:StringMin1Max4000_Type

0..1 O

an 1 4000 stf:StringMin1Max4000_Type

Deutsche Bezeichnung CARF-Version Kopfdaten
Identifizierungsnummer des Datensenders Übermittelnder Staat Empfangender Staat
Typ der Meldung Warnung

Wertemenge / Erklärung
Wurzelelement zum CARF-Schema Dieser Bestandteil ist stets über die Schemadefinition der CARFXML_v1.0.xsd zu prüfen. Attribut zu carf:CARF_OECD Dieses Attribut enthält die Angabe zur verwendeten Schemaversion, in der die CARF-Mitteilung erstellt wurde. Derzeit ist der Wert "1.0" zu verwenden. Diese Datenelementgruppe enthält die Informationen über den übermittelnden Staat, den Zeitpunkt der Erstellung der Mitteilung, den Meldezeitraum auf den sich die Mitteilung bezieht und die Art der Mitteilung (Original, Korrektur, Löschung etc.). Dieses Datenelement enthält Angaben zu einer national festgelegten und eindeutigen Identifizierungsnummer des Datensenders. Dieses Datenelement enthält Angaben zum ISO-Code des Staates, der die CARF-Meldung übermittelt. Es ist der konstante Wert "DE" zu verwenden. Dieses Datenelement enthält Angaben zum ISO-Code des Staates, der die CARF-Meldung empfängt. Da allerdings nur eine Eintragung möglich ist und Informationen im Rahmen der Weiterleitung ggfs. an mehrere Länder verschickt werden müssen, ist hier der konstante Wert "DE" zu verwenden. Dieses Datenelement enthält Angaben zum Typ der CARFMeldung, die übermittelt wird. Der einzige zulässige Wert für den Austausch im Rahmen der OECD Model Rules ist “CARF”. Dieses Datenelement enthält ein Freitextfeld, in dem besondere Vorsichtshinweise zu Inhalten der CARF-Meldung und deren weiteren Verwendung mitgeteilt werden können.

Kontakt

Dieses Datenelement besteht aus einem Freitextfeld und enhält optionale Angaben zu einem technischen Kontakts des Datensenders, der als Ansprechperson der CARFMeldung mitgeteilt werden kann (z.B. Name, E-Mail-Adresse, etc.). Diese Angabe wird nicht an die empfangenden Staaten der CARF-Daten weitergeleitet. Sie wird nur für die interne Kommunikation zwischen dem Datensender und dem BZSt verwendet.

Seite 13 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:MessageRefId

carf:MessageTypeIndic

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

Kardi-

For-

nalität P O B mat Min Max

1

P

an 1 170

Datentyp stf:StringMin1Max170_Type

Deutsche Bezeichnung MessageRefId

1

P

en

carf:MessageTypeIndic_EnumType Art der Meldung

DCARF-XML-Schema v1.5 12.09.2025
Wertemenge / Erklärung Dieses Datenelement enthält die Angabe zum eindeutigen Bezeichner (Referenz) einer CARF-Meldung.
Für jede CARF-Meldung muss eine neue, eindeutige MessageRefId für zukünftige Referenzzwecke in Folgemeldungen vergeben werden.
Die MessageRefId muss mit dem Staatencode des übermittelnden Staates beginnen. Danach folgt der Meldezeitraum, der Staatencode des Empfängerstaates und ein eindeutiger Bezeichner (frei zu vergebende Zeichenkombination). Beispiel: DE2026DE1234567 Dieses Datenelement enthält Angaben zur Art der Meldung, z.B. ob es sich um neue Informationen, eine Korrektur, eine Löschung oder eine Leermeldung handelt.
Der Wertebereich des carf:MessageTypeIndic_EnumType wird in der Werteliste für Aufzählungstypen beschrieben.

carf:ReportingPeriod carf:Timestamp

1

P

d

xsd:date

1

P

dt

xsd:dateTime

Meldezeitraum Zeitstempel

Dieses Datenelement enthält Angaben zum letzten Tag des Meldezeitraums, auf den sich die Informationen der CARFMeldung beziehen. Die Angabe erfolgt auf Basis des Kalenderjahres in dem der Meldezeitraum endet. Format: JJJJ-MM-TT Beispiel: Für das Meldejahr 2026 wäre somit die Angabe "2026-12-31" vorzunehmen. Dieses Datenelement enthält Angaben zum Zeitpunkt zu dem die Nachricht erstellt wurde. Dieser Wert sollte üblicherweise automatisch durch das System erstellt werden. Teile von Sekunden können genutzt werden (in diesem Fall werden die Millisekunden in drei Stellen ".nnn" angegeben). Format: JJJJ-MM-TT’T’ss:mm:ss.nnn Beispiel: 2022-03-15T09:45:30 oder 2022-0315T09:45:30.789 (mit Millisekunden).

carf:CARFBody

1

P

carf:CARFBody_Type

Meldungsinhalt

Diese Datenelementgruppe enthält alle Angaben zum meldenden Anbieter von Kryptowerte-Dienstleistungen mit dem Bezug zum Meldestaat, sowie deren meldepflichtige Kryptowerte-Nutzer mit ihren relevanten Transaktionen.

carf:RCASP

1

P

carf:RCASP_Type

Typ des meldenden Anbieters von KryptoDienstleistungen

Diese Datenelementgruppe enthält alle Angaben zum Typ des meldenden Anbieter von Kryptowerte-Dienstleistungen dieser CARF-Meldung.

Seite 14 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:RCASP_ID

carf:Individual carf:Entity

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp

0..1 B 0..1 B

carf:PersonParty_Type carf:OrganisationParty_Type

Deutsche Bezeichnung Identifikationsdaten des meldenden Anbieters von Krypto-Dienstleistungen
Natürliche Person
Rechtsträger

Wertemenge / Erklärung
Diese Elementgruppe enthält Angaben zu Identifikationsdaten des meldenden Anbieters von Kryptowerte-Dienstleistungen mit dem Bezug zum Meldestaat. Es kann in den nachfolgenden Elementen entschieden werden, ob es sich um eine natürliche Person oder einen Rechtsträger handelt. Diese Datenelementgruppe legt die Art des meldenden Anbieters von Krypto-Dienstleistungen und die davon abhängigen Informationen fest. Es ist zwingend erfoderlich einen meldenden Anbieter von Kryptowerte-Dienstleistungen anzugeben. Dieser kann entweder eine natürliche Person (carf:PersonParty_Type) oder ein Rechtsträger (carf:OrganisationParty_Type) sein.
Die zulässigen, bzw. erforderlichen Angaben sind jeweils in der Übersicht zu komplexen Datentypen beschrieben.

carf:Nexus
carf:OtherNexus carf:Nexus carf:ResCountryCode

0..1 B

en

0..1 O

1

P

en

1

P

en

carf:Nexus_EnumType carf:Nexus_EnumType iso:CountryCode_Type

Nexus
Anderer Nexus Nexus Ansässigkeitsstaat

Dieses Datenelement enthält die Informationen, aus welchem Grund der meldende Anbieter von KryptowerteDienstleistungen die stärkste Verbindung zum übermittelnden Staat hat und dadurch mit seinen Melde- und Sorgfaltspflichten diesem Staat unterliegt. Wenn relevante Transaktionen gemeldet werden, ist diese Angabe verpflichtend.
Der Wertebereich des carf:Nexus_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Diese Datenelementgruppe enthält Informationen darüber, dass eine CARF-Meldung aufgrund eines stärkeren Nexus in einem anderen Staat übermittelt wurde.
Attribut zu carf:Nexus Dieses Attribut enthält die Informationen, aus welchem Grund der meldende Anbieter von KryptowerteDienstleistungen die stärkste Verbindung zu einem anderen Staat hat und dadurch dort mit seinen Melde- und Sorgfaltspflichten unterliegt.
Der Wertebereich des carf:Nexus_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Attribut zu carf:Nexus Dieses Attribut enthält die Informationen über den anderen Staat, in welchem die CARF-Meldung abgegeben wird.

Seite 15 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:DocSpec

carf:CryptoUsers
carf:UserID carf:Individual carf:Entity
carf:ControllingPerson

carf:Individual carf:CtrlgPersonType

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp stf:DocSpec_Type

0..n O

1

P

0..1 B 0..1 B 0..n O

carf:CryptoUsers_Type
carf:PersonParty_Type carf:OrganisationParty_Type carf:ControllingPerson_Type

1

P

1..n P

en

carf:PersonParty_Type carf:CtrlgPersonType_EnumType

Deutsche Bezeichnung DocSpec
Kryptowerte-Nutzer

Wertemenge / Erklärung Diese Datenelementgruppe enthält die eindeutige Referenz des entsprechenden Teils der CARF-Meldung. Für das spätere Korrekturverfahren kann dadurch die Zuordnung des zu ändernden bzw. zu löschenden Datensatzes erfolgen.
Die zulässigen, bzw. erforderlichen Angaben sind in der Übersicht zu komplexen Datentypen beschrieben.
Diese Datenelementgruppe enthält die Angaben zu einem Kryptowerte-Nutzer, sowie die Informationen der relevanten Transaktionen, sofern diese meldepflichtig sind.
Bei Rechträgern sind gegebenenfalls auch die Informationen zu beherrschenden Personen anzugeben.

Natürliche Person Rechtsträger

Die Datenelementgruppe enthält Angaben zu Identifikationsdaten des Kryptowerte-Nutzers. Es kann in den nachfolgenden Elementen entschieden werden, ob es sich um eine natürliche Person oder einen Rechtsträger handelt. Diese Datenelementgruppe legt die Art des KryptowerteNutzers und die davon abhängigen Informationen fest. Dieser kann entweder eine natürliche Person (carf:PersonParty_Type) oder ein Rechtsträger (carf:OrganisationParty_Type) sein.

Beherrschende Person(en)

Die zulässigen, bzw. erforderlichen Angaben sind in der Übersicht zu komplexen Datentypen beschrieben.
Diese Datenelementgruppe sollte Angaben zu beherrschenden Personen enthalten, wenn ein Rechtsträger als Kryptowerte-Nutzer angegeben wurde und über solche beherrschenden Personen verfügt.

Es sind ausschließlich natürliche Personen als beherrschende Personen zu melden.

Natürliche Person

Gibt es mehrere beherrschende Personen, ist die Datenelementgruppe entsprechend oft zu wiederholen. Diese Datenelementgruppe enthält die Informationen zur beherrschenden Person.

Rolle der beherrschenden Person

Die zulässigen, bzw. erforderlichen Angaben sind in der Übersicht zu komplexen Datentypen beschrieben. Das Datenelement enthält Informationen über die Verbindung der beherrschenden Person zum KryptowerteNutzer.

Der Wertebereich des carf:CarfCtrlgPersonType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben.

Seite 16 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:RelevantTransactions

carf:CryptoAsset

carf:CryptoToCryptoIn carf:ExchangeType carf:NumberofTransactions

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1..n P

Datentyp carf:RelevantTransactions_Type

1

P

1 200 stf:StringMin1Max200_Type

0..n B

0..1 O

en

carf:ExchangeType_EnumType

1

P

xsd:integer

Deutsche Bezeichnung
Meldepflichtige Transaktionen

Wertemenge / Erklärung
Diese Datenelementgruppe enthält die Informationen zu den relevanten Transaktionen des Kryptowerte-Nutzers innerhalb des Meldezeitraums.

Kryptowert

Die Datenelementgruppe ist für jeden relevanten Kryptowert, für den der Kryptowerte-Nutzer Transaktionen ausgeführt hat, entsprechend oft zu wiederholen. Dieses Datenelement enthält den Name des Kryptowertes, für welchen relevante Transaktion(en) im Meldezeitraum durchgeführt wurden.

Der Name des Kryptowertes sollte nach Möglichkeit in Übereinstimmung mit dem Digital Token Identifier angegeben werden. Genauere Spezifikationen zur Namenskonvention werden auf der Website der OECD veröffentlicht (Veröffentlichung steht bisher noch aus). Sofern der Kryptowert nicht auf der Website der OECD aufgeführt ist, können sich meldende Anbieter auf andere verfügbare, gebräuchliche Namenskonventionen stützen oder den Namen bei fehlender Namenskonvention als Freitext angeben.

Erwerb eines Kryptowertes (Tauschgeschäft)

Jeder Kryptowert, der im Meldezeitraum relevante Transaktionen für den Kryptowerte-Nutzer ausgelöst hat, ist nur einmal aufzuführen und die zugehörige(n) Transaktion(en) konsolidiert in den nachfolgenden Elementgruppen anzugeben.
Diese Datenelementgruppe enthält Informationen zum Erwerb des relevanten Kryptowertes gegen Hingabe anderer relevanter Kryptowerte (Tauschgeschäft).

Sollte diese Elementgruppe verwendet werden, ist auch zwingend eine korrespondierende Angabe zur Veräußerung von relevanten Kryptowerten gegen andere relevante Kryptowerte anzugeben (carf:CryptoToCryptoOut).

Austauschtyp

Dieses Datenelement kann eine Angabe zur Art des Sachverhalts enthalten, der zu den Transaktionen und dem Erwerb des Kryptowertes im Meldezeitraum geführt hat.

Der Wertebereich des carf:ExchangeType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben.

Anzahl der Transaktionen

Dieses Datenelement enthält die Anzahl der Transaktionen bei denen der betreffende Kryptowert gegen andere betreffende Kryptowerte erworben wurde.

Seite 17 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:Amount

currCode carf:NumberofUnits carf:CryptoToCryptoOut

carf:ExchangeType

carf:NumberofTransactions carf:Amount

currCode

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

0..n B

xsd:decimal

0..1 O

en

carf:ExchangeType_EnumType

1

P

1

P

xsd:integer carf:MonAmnt_Type

1

P

33

iso:currCode_Type

Deutsche Bezeichnung Betrag

Wertemenge / Erklärung
Dieses Datenelement enthält den aggregierten Marktwert des bzw. der erworbenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00

Währung

Attribut zu carf:Amount Das Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.

Anzahl der Einheiten
Veräußerung eines Kryptowertes (Tauschgeschäft)
Austauschtyp

Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die erworben wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Diese Datenelementgruppe enthält Informationen zur Veräußerung des relevanten Kryptowertes gegen andere relevante Kryptowerte (Tauschgeschäft). Sollte diese Elementgruppe verwendet werden, ist auch zwingend eine korrespondierende Angabe zum Erwerb von relevanten Kryptowerten gegen andere relevante Kryptowerte anzugeben (carf:CryptoToCryptoIn). Dieses Datenelement kann eine Angabe zur Art des Sachverhalts enthalten, der zu den Transaktionen und der Veräußerung des Kryptowertes im Meldezeitraum geführt hat.

Anzahl der Transaktionen

Der Wertebereich des carf:ExchangeType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Dieses Datenelement enthält die Anzahl der Transaktionen für die Veräußerung des relevanten Kryptowertes gegen einen anderen relevanten Kryptowert.

Betrag

Dieses Datenelement enthält den aggregierten Marktwert des bzw. der veräußerten, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00

Währung

Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.

Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben.

Seite 18 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:NumberofUnits

carf:CryptoFiatIn carf:ExchangeType

carf:NumberofTransactions carf:Amount

currCode carf:NumberofUnits carf:CryptoFiatOut carf:ExchangeType

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp xsd:decimal

0..n B

0..1 O

en

carf:ExchangeType_EnumType

1

P

1

P

xsd:integer carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

0..n B

0..1 O

en

xsd:decimal carf:ExchangeType_EnumType

Deutsche Bezeichnung Anzahl der Einheiten
Erwerb eines Kryptowertes

Wertemenge / Erklärung
Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die veräußert wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Diese Datenelementgruppe enthält Informationen zum Erwerb des relevanten Kryptowertes gegen eine Zahlung eines vereinbarten Kaufpreises in einer staatlichen Währung.

Austauschtyp

Dieses Datenelement kann eine Angabe zur Art des Sachverhalts enthalten, der zu den Transaktionen und der Veräußerung des Kryptowertes im Meldezeitraum geführt hat.

Anzahl der Transaktionen

Der Wertebereich des carf:ExchangeType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Dieses Datenelement enthält die Anzahl der Transaktionen für den Erwerb des relevanten Kryptowertes gegen Zahlung eines vereinbarten Kaufpreises.

Betrag
Währung
Anzahl der Einheiten Veräußerung eines Kryptowertes Austauschtyp

Dieses Datenelement enthält den aggregierten Marktwert des bzw. der erworbenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00
Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.
Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die erworben wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Diese Datenelementgruppe enthält Informationen zur Veräußerung des relevanten Kryptowertes gegen eine Zahlung eines vereinbarten Kaufpreises in einer staatlichen Währung. Dieses Datenelement kann eine Angabe zur Art des Sachverhalts enthalten, der zu den Transaktionen und der Veräußerung des Kryptowertes im Meldezeitraum geführt hat.
Der Wertebereich des carf:ExchangeType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben.

Seite 19 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:NumberofTransactions

carf:Amount

currCode carf:NumberofUnits carf:CryptoTransferIn

carf:TransferType
carf:NumberofTransactions carf:Amount

currCode

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp xsd:integer

1

P

carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

0..n B

xsd:decimal

1

P

en

1

P

1

P

carf:TransferType_EnumType
xsd:integer carf:MonAmnt_Type

1

P

33

iso:currCode_Type

Deutsche Bezeichnung Anzahl der Transaktionen Betrag
Währung
Anzahl der Einheiten Erhalt eines Kryptowertes durch Übertragung
Übertragungstyp
Anzahl der Transaktionen

Wertemenge / Erklärung Dieses Datenelement enthält die Anzahl der Transaktionen für die Veräußerung des relevanten Kryptowertes gegen Zahlung eines vereinbarten Kaufpreises.
Dieses Datenelement enthält den aggregierten Marktwert des bzw. der veräußerten, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00
Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.
Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die veräußert wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Diese Datenelementgruppe enthält Informationen zum Erhalt des relevanten Kryptowertes. Der meldende Anbieter kann aus den ihm vorliegenden Informationen nicht erkennen, dass der Kryptowerte-Nutzer als Gegenleistung einen bestimmten Betrag einer staatlichen Währung gezahlt, oder einen anderen Kryptowert übertragen hat.
Dieses Datenelement enthält eine Angabe zur Art des Sachverhalts, der zu den Transaktionen und dem Erhalt des Kryptowertes im Meldezeitraum geführt hat.
Der Wertebereich des carf:TransferType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Dieses Datenelement enthält die Anzahl der Transaktionen für den Erhalt des relevanten Kryptowertes.

Betrag Währung

Dieses Datenelement enthält den aggregierten Marktwert des bzw. der erhaltenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00
Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.
Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben.

Seite 20 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:NumberofUnits

carf:AltValuation

carf:CryptoTransferOut
carf:TransferType carf:NumberofTransactions carf:Amount
currCode carf:NumberofUnits

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp xsd:decimal

0..1 B

en

carf:AltValuation_EnumType

0..n B

1

P

en

1

P

1

P

carf:TransferOutType_EnumType
xsd:integer carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

xsd:decimal

Deutsche Bezeichnung Anzahl der Einheiten

Wertemenge / Erklärung
Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die erhalten wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind.

Alternative Bewertungsmethode

Dieses Datenelement enthält Informationen zu einer anderen Bewertungsmethode, sofern der meldende Anbieter eine alternative Methode gewählt hat. Wenn eine alternative Methode gewählt wurde, dann muss diese auch angegeben werden.

Abgabe eines Kryptowertes durch Übertragung

Der Wertebereich des carf:AltValuation_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Diese Datenelementgruppe enthält Informationen zur Abgabe des relevanten Kryptowertes. Der meldende Anbieter kann aus den ihm vorliegenden Informationen nicht erkennen, dass der Kryptowerte-Nutzer als Gegenleistung einen bestimmten Betrag einer staatlichen Währung oder einen anderen Kryptowert erhalten hat.

Übertragungstyp Anzahl der Transaktionen

Dieses Datenelement enthält eine Angabe zur Art des Sachverhalts, der zu den Transaktionen und der Abgabe des Kryptowertes im Meldezeitraum geführt hat.
Der Wertebereich des carf:TransferOutType_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Dieses Datenelement enthält die Anzahl der Transaktionen für die Abgabe des relevanten Kryptowertes.

Betrag Währung

Dieses Datenelement enthält den aggregierten Marktwert des bzw. der abgegebenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00
Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.

Anzahl der Einheiten

Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die abgegeben wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind.

Seite 21 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:AltValuation

carf:TransferWallet

carf:Amount currCode
carf:NumberofUnits carf:AltValuation carf:RRPT

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

0..1 B

en

Datentyp carf:AltValuation_EnumType

0..n B

1

P

carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

0..1 B

en

xsd:decimal carf:AltValuation_EnumType

0..n B

Deutsche Bezeichnung
Alternative Bewertungsmethode

Wertemenge / Erklärung
Das Element enthält Informationen zu einer anderen Bewertungsmethode, sofern der meldende Anbieter eine alternative Methode gewählt hat. Wenn eine alternative Methode gewählt wurde, dann muss diese auch angegeben werden.

Übertragung eines Kryptowertes an WalletAdressen, die weder VASP noch Finanzinstituten zugeordnet werden
Betrag

Der Wertebereich des carf:AltValuation_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Diese Datenelementgruppe enthält Informationen über Übertragungen des betreffenden Kryptowertes an WalletAdressen, von denen dem meldenden RCASP nicht bekannt ist, dass sie mit einem Anbieter von Dienstleistungen für virtuelle Vermögenswerte (VASP) oder einem Finanzinstitut verbunden sind. Eine explizite Gegenleistung darf dem RCASP ebenfalls nicht bekannt sein. Dieses Datenelement enthält den aggregierten Marktwert des bzw. der übertragenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00

Währung

Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.

Anzahl der Einheiten
Alternative Bewertungsmethode

Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die übertragen wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Dieses Datenelement enthält Informationen zu einer anderen Bewertungsmethode, sofern der meldende Anbieter eine alternative Methode gewählt hat.

Massenzahlungstransaktion

Der Wertebereich des carf:AltValuation_EnumType wird in der Werteliste für Aufzählungstypen beschrieben. Diese Datenelementgruppe enthält Informationen zur Abgabe des relevanten Kryptowertes im Rahmen einer Massenzahlungstransaktion.

Es handelt sich um eine meldepflichtige Massenzahlungstransaktion, wenn (mindestens) eine Übertragung eines relevanten Kryptowertes als Gegenleistung für Waren oder Dienstleistungen im Wert von mehr als 50.000 USD getätigt wurde, ungeachtet der Rundung.

Seite 22 von 35

Bundeszentralamt für Steuern

L1

L2 L3 L4 L5 L6 L7 L8 L9 L10 L11 L12

carf:NumberofTransactions

carf:Amount

currCode carf:NumberofUnits carf:DocSpec

Datensatzbeschreibung Aufbau der Daten nach CARF-XML-Schema der OECD

DCARF-XML-Schema v1.5 12.09.2025

Kardi-

For-

nalität P O B mat Min Max

1

P

Datentyp xsd:integer

1

P

carf:MonAmnt_Type

1

P

33

iso:currCode_Type

1

P

1

P

xsd:decimal stf:DocSpec_Type

Deutsche Bezeichnung Anzahl der Transaktionen

Wertemenge / Erklärung
DasDatenelement enthält die Anzahl der meldepflichtigen Massenzahlungstransaktionen im Meldezeitraum.

Betrag Währung Anzahl der Einheiten DocSpec

Dieses Datenelement enthält den aggregierten Marktwert des bzw. der abgegebenen, relevanten Kryptowerte(s) abzüglich Transaktionsgebühren. Der Marktwert wird mit zwei Nachkommastellen angegeben. Beispiel: 1000 USD = 1000.00
Attribut zu carf:Amount Dieses Attribut enthält die Angabe zur Währung des Marktwertes im dreistelligen ISO-Code.
Der Wertebereich des iso:currCode_Type wird in der Werteliste für ISO-Types beschrieben. Dieses Datenelement enthält die Angabe zur Anzahl der Einheiten des relevanten Kryptowertes, die im Rahmen der Massenzahlungstransaktion(en) abgegeben wurden. Die Anzahl ist mit bis zu sechs Nachkommastellen anzugegeben, sofern diese relevant sind. Diese Datenelementgruppe enthält die eindeutige Referenz des entsprechenden Teils der CARF Meldung. Für das spätere Korrekturverfahren kann dadurch die Zuordnung des zu ändernden bzw. zu löschenden Datensatzes erfolgen.
Die zulässigen, bzw. erforderlichen Angaben sind in der Übersicht zu komplexen Datentypen beschrieben.

Seite 23 von 35

Bundeszentralamt für Steuern
Wertelisten für Aufzählungstypen
Typ stf:OECDDocTypeIndic_EnumType
stf:OECDNameType_EnumType

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

Wert OECD0

Resend Data

Deutsche Bezeichnung Erneut übermittelte Daten

OECD1 OECD2 OECD3 OECD10
OECD11
OECD12
OECD13

New Data Corrected Data Deletion of Data Resent Test Data
New Test Data
Corrected Test Data
Deletion of Test Data

Neue Daten Korrigierte der Daten Löschung von Daten Erneut übermittelte Testdaten
Neue Testdaten
Korrigierte Testdaten
Löschung von Testdaten

OECD201 OECD202 OECD203 OECD204 OECD205 OECD206 OECD207 OECD208

SMFAliasOrOther indiv (individual) alias (alias) nick (nickname) aka (also known as) dba (doing business as) legal (legal name) atbirth (name at birth)

SMF Alias oder anderes individueller Name Alias Spitzname auch bekannt als Geschäfte tätigend als eingetragener Name Geburtsname

Seite 24 von 35

CARF-XML-Schema v1.5 12.09.2025
Wertemenge / Erklärung
Durch diese Meldeart wird gekennzeichnet, dass es sich um eine weitere Datenübermittelung eines bereits bekannten RCASP handelt. Diese Meldeart bezieht sich also nur auf weitere Datensätze eines meldenden Anbieters von Krypto-Dienstleistungen und kann demensprechend nur genutzt werden, wenn dieser bereits eine erfolgreich verarbeitete Meldung von für den betroffenen Meldezeitraum übermittelt hat.
Die erneute Übermittlung kann für neue, bisher noch nicht übermittelte Daten oder zu korrigierende/zu löschende Informationen zu meldenden Nutzern und/oder deren beherrschenden Personen und relevanten Transaktionen verwendet werden. Durch diese Meldeart wird gekennzeichnet, dass es sich um neue, erstmalig übermittelte Daten handelt. Durch diese Meldeart wird gekennzeichnet, dass es sich um Daten handelt, die korrigiert werden. Durch diese Meldeart wird gekennzeichnet, dass es sich um Daten handelt, die gelöscht werden.
Durch diese Meldeart wird gekennzeichnet, dass es sich um erneut übermittelte Daten innerhalb des Testsystems handelt. Durch diese Meldeart wird gekennzeichnet, dass es sich um neue, erstmalig übermittelte Daten innerhalb des Testsystems handelt. Durch diese Meldeart wird gekennzeichnet, dass es sich um Daten innerhalb des Testsystems handelt, die korrigiert werden. Durch diese Meldeart wird gekennzeichnet, dass es sich um Daten innerhalb des Testsystems handelt, die gelöscht werden.
Es ist möglich, dass mehrere Namen für dieselbe Person gemeldet werden könnten. Das Element ermöglich die Unterscheidung dieser und enthält Informationen über die Art des Namens. Dazu gehören bspw. Spitznamen („nick“), Namen, unter denen eine Person geschäftlich tätig ist („dba“ ein Kurzname für das Unternehmen oder ein Name, der für die Öffentlichkeit anstelle des offiziellen Geschäftsnamens verwendet wird) usw.

Bundeszentralamt für Steuern Typ stf:OECDLegalAddressType_EnumType carf:ExchangeType_EnumType carf:TransferType_EnumType
carf:TransferOutType_EnumType

Wert
OECD301 OECD302 OECD303 OECD304 OECD305
CARF401 CARF402 CARF403 CARF404
CARF501 CARF502 CARF503 CARF504 CARF505 CARF506 CARF507 CARF508 CARF509
CARF601 CARF602 CARF603
CARF604 CARF605 CARF606

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

residentialOrBusiness residential business registeredOffice unspecified

Deutsche Bezeichnung
Geschäfts- oder Wohnadresse Wohnadresse Geschäftsadresse Eingetragener Sitz nicht näher bezeichnet

Wertemenge / Erklärung
Das Attribut zu einer Adresseangabe dient zur Angabe/Präzisierung des rechtlichen Charakters dieser Adresse (Wohn-, Geschäftsadresse usw.).

Staking
Crypto Loan
Wrapping Collateral

Staking Krypto-Darlehen Wrapping Sicherheit

Sofern die Informationen dem meldenden Anbieter zur Verfügung stehen, kann durch die Informationen in dem Element mitgeteilt werden, in welchem Zusammenhang die Kryptowerte erworben oder veräußert wurden.

Airdrop

Airdrop

Staking income

Erträge aus Staking

Mining income

Erträge aus Mining

Crpyto loan

Krypto-Darlehen

Transfer from another RCASP Übertragung von einem anderen meldepflichtigen Kryptowerte-

Anbieter

Sale of goods or services

Verkauf von Waren oder Dienstleistungen

Collateral

Sicherheit

Other

Sonstige

Unknown (to be selected as the Unbekannt (als Standardwert auszuwählen, wenn der meldende

default value where the

Krypto-Asset-Dienstleister keine Kenntnis über die Übertragungsart

Reporting Crypto-Asset Service hat)

Provider has no knowledge on

the Transfer Type)

Bei Erhalt, ist dem meldenden Anbieter nicht bekannt, dass der Kryptowerte-Nutzer als Gegenleistung einen bestimmten Betrag einer staatlichen Währung gezahlt, oder einen anderen Kryptowert übertragen hat. Das Element enthält Informationen darüber, in welchem Zusammenhang die Kryptowerte erhalten wurden.

Transfer to another RCASP
Crypto Loan Purchase of goods or services, to be used in respect of transactions other than those already reported as Reportable Retail Payment Transactions

Übertragung zu einem anderen meldepflichtigen Kryptowerte-

Bei Abgabe, ist dem meldenden Anbieter nicht bekannt, dass

Anbieter

der Kryptowerte-Nutzer als Gegenleistung einen bestimmten

Krypto-Darlehen

Betrag einer staatlichen Währung erhalten, oder einen

Kauf von Waren oder Dienstleistungen, die für andere

anderen Kryptowert übertragen bekommen hat. Das Element

Transaktionen, als die bereits als meldepflichtige

enthält Informationen darüber, in welchem Zusammenhang

Massenzahlungstransaktionen gemeldeten, verwendet werden sollen die Kryptowerte übertragen wurden.

Collateral

Sicherheit

Other

Sonstige

Unknown (to be selected as the Unbekannt (als Standardwert auszuwählen, wenn der meldende

default value where the

Krypto-Asset-Dienstleister keine Kenntnis über die Übertragungsart

Reporting Crypto-Asset Service hat)

Provider has no knowledge on

the Transfer Type)

Seite 25 von 35

Bundeszentralamt für Steuern Typ carf:MessageTypeIndic_EnumType
carf:CarfCtrlgPersonType_EnumType

Wert
CARF701 CARF702
CARF703
CARF801 CARF802 CARF803 CARF804 CARF805 CARF806 CARF807 CARF808 CARF809 CARF810 CARF811 CARF812 CARF813

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Deutsche Bezeichnung

The message contains new information The message contains corrections/deletions for previously sent information.

Die Mitteilung enthält neue Informationen
Die Mitteilung enthält Korrekturen/Löschungen für bereits übermittelte Informationen.

The message advises that there Die Mitteilung weist darauf hin, dass keine Daten zu melden sind. is no data to report.

Wertemenge / Erklärung Das Element enthält Angaben zur Art der übermittelten Informationen, d. h., ob es sich um neue Informationen handelt oder ob die Nachricht darauf abzielt, zuvor gesendete Informationen zu korrigieren oder zu löschen. Die CARF-Meldung enthält die Information, dass neue Daten übermittelt wurden. Die CARF-Meldung enthält die Information, dass Korrekturen/Löschungen für zuvor übermittelte Daten übermittelt wurden, aber es sind keine neue Daten enthalten.
Die CARF-Meldung enthält die Information, dass es keine meldepflichtigen Daten beim meldenden Anbieter zu melden gibt (Leermeldung).
In diesem Fall werden nur Angaben zum Meldungsteil des meldenden Anbieters übermittelt.

CP of legal person - ownership CP of legal person - other means CP of legal person - senior managing official CP of legal arrangement - trust - settlor CP of legal arrangement - trust - trustee CP of legal arrangement - trust - protector CP of legal arrangement - trust - beneficiary CP of legal arrangement - trust - other CP of legal arrangement - other - settlor-equivalent CP of legal arrangement - other - trustee-equivalent CP of legal arrangement - other - protector-equivalent CP of legal arrangement - other - beneficiary-equivalent CP of legal arrangement - other - other-equivalent

Beherrschende Person eines Rechtsträgers - Eigentum Beherrschende Person eines Rechtsträgers - Sonstiges Beherrschende Person eines Rechtsträgers - Leitender Angestellter Beherrschende Person einer Rechtsvereinbarung - Treugeber Beherrschende Person einer Rechtsvereinbarung - Treuhänder Beherrschende Person einer Rechtsvereinbarung - Treuhand Protektor Beherrschende Person einer Rechtsvereinbarung - Treuhand Begünstigter Beherrschende Person einer Rechtsvereinbarung - Treuhand Sonstiges Beherrschende Person einer Rechtsvereinbarung - Sonstiges Treugeberäquivalent Beherrschende Person einer Rechtsvereinbarung - Sonstiges Treuhänderäquivalent Beherrschende Person einer Rechtsvereinbarung - Sonstiges Protektoräquivalent Beherrschende Person einer Rechtsvereinbarung - Sonstiges Begünstigtenäquivalent Beherrschende Person einer Rechtsvereinbarung - Sonstiges Äquivalent

Seite 26 von 35

Bundeszentralamt für Steuern Typ carf:Nexus_EnumType

Wert CARF901 CARF902

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD
Deutsche Bezeichnung

Tax Residence Incorporation

steuerliche Ansässigkeit Gründung

CARF903 CARF904 CARF905 CARF906
CARF907

Management Place of Business Branch Authorisation
Remote Services

Verwaltung Sitz der Geschäftsleitung Niederlassung Genehmigung nach MiCA
Remote-Dienste (Registrierung)

CARF-XML-Schema v1.5 12.09.2025
Wertemenge / Erklärung Das Element enthält Informationen über den stärksten Nexus, aufgrund dessen der meldende Anbieter seine CARFMeldung abgibt. Dieser Wert zeigt an, dass der meldende Anbieter die CARFMeldung in dem Staat abgibt, in dem er steuerlich ansässig ist.
Dieser Wert zeigt an, dass der meldende Anbieter die CARFMeldung in dem Staat abgibt, in dem er eingetragen oder organisiert ist und entweder in diesem Staat Rechtspersönlichkeit besitzt oder verpflichtet ist, bei den Steuerbehörden dieses Staates Steuererklärungen oder Steuerauskünfte in Bezug auf die Einkünfte einzureichen. Dieser Wert zeigt an, dass der meldende Anbieter die CARFMeldung in dem Staat abgibt, in dem er verwaltet wird.
Dieser Wert zeigt an, dass der meldende Anbieter die CARFMeldung in dem Staat abgibt, in dem er einen regulären Geschäftssitz hat. Dieser Wert zeigt an, dass der meldende Anbieter die CARFMeldung in dem Staat abgibt, in dem er eine Niederlassung unterhält. Dieser Wert gibt an, dass der meldende Anbieter die CARFMeldung in dem EU-Mitgliedstaat abgibt, in dem er gemäß der Verordnung (EU) 2023/1114 zugelassen ist. (EUspezifisch)
Dieser Wert gibt an, dass der meldende Anbieter, der nicht gemäß der Verordnung (EU) 2023/1114 zugelassen ist, idie CARF-Meldung in dem EU-Mitgliedstaat abgibt, in dem er die Registrierung nach DAC8 vorgenommen hat. (EU-spezifisch)

Seite 27 von 35

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel AF AX AL DZ AS AD AO AI

Englische Umschreibung des Länderkürzels
Afghanistan Aland Islands Albania Algeria American Samoa Andorra Angola Anguilla

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

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert AED AFN ALL AMD ANG AOA ARS AUD
AWG AZN BAM BBD BDT BGN BHD BIF BMD BND BOB BOV BRL BSD BTN BWP BYN BYR BZD CAD CDF CHE CHF CHW CLF CLP CNY COP COU CRC CUC CUP CVE CZK DJF DKK DOP DZD EGP ERN ETB

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet
United Arab Emirates Afghanistan Albania Armenia Curacao; Sint Maarten (Dutch Part) Angola Argentina Australia; Christmas Island; Cocos (Keeling) Islands; Heard Island And Mcdonald Islands; Kiribati; Nauru; Norfolk Island; Tuvalu
Aruba Azerbaijan Bosnia And Herzegovina Barbados Bangladesh Bulgaria Bahrain Burundi Bermuda Brunei Darussalam Bolivia, Plurinational State Of Bolivia, Plurinational State Of Brazil Bahamas Bhutan Botswana Belarus Belarus Belize Canada Congo, The Democratic Republic Of Switzerland Liechtenstein; Switzerland Switzerland Chile Chile China Colombia Colombia Costa Rica Cuba Cuba Cabo Verde Czechia Djibouti Denmark; Faroe Islands; Greenland Dominican Republic Algeria Egypt Eritrea Ethi

Währungs-/Sprachbezeichnung
UAE Dirham Afghani Lek Armenian Dram Netherlands Antillean Guilder Kwanza Argentine Peso Australian Dollar
Aruban Florin Azerbaijan Manat Convertible Mark Barbados Dollar Taka Bulgarian Lev Bahraini Dinar Burundi Franc Bermudian Dollar Brunei Dollar Boliviano Mvdol Brazilian Real Bahamian Dollar Ngultrum Pula Belarusian Ruble Historic use Belarussian Ruble Belize Dollar Canadian Dollar Congolese Franc WIR Euro Swiss Franc WIR Franc Unidad de Fomento Chilean Peso Yuan Renminbi Colombian Peso Unidad de Valor Real Costa Rican Colon Peso Convertible Cuban Peso Cabo Verde Escudo Czech Koruna Djibouti Franc Danish Krone Dominican Peso Algerian Dinar Egyptian Pound Nakfa Ethiopian Birr

Seite 28 von 35

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
KM

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

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert EUR
FJD FKP GBP
GEL GHS GIP GMD GNF GTQ GYD HKD HNL HRK HTG HUF IDR ILS INR IQD IRR ISK JMD JOD JPY KES KGS KHR KMF KPW KRW KWD KYD KZT LAK LBP LKR LRD LSL LTL LVL LYD MAD MDL MGA MKD

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung

Aland Islands; Andorra; Austria; Belgium; Cyprus; Estonia; European Union; Finland; Euro

France; French Guiana; French Southern Territories; Germany; Greece;

Guadeloupe; Holy See (Vatican City State); Ireland; Italy; Latvia; Lithuania;

Luxembourg; Malta; Martinique; Mayotte; Monaco; Montenegro; Netherlands;

Portugal; Reunion; Saint Barthelemy; Saint Martin (French Part); Saint Pierre And

Miquelon; San Marino; Slovakia; Slovenia; Spain; Vatican City State (Holy See)

Fiji

Fiji Dollar

Falkl

Falkland Islands Pound

Guernsey; Isle Of Man; Jersey; United Kingdom Of Great Britain And Northern Ireland

Pound Sterling

Georgia

Lari

Ghana

Ghana Cedi

Gibraltar

Gibraltar Pound

Gambia

Dalasi

Guinea

Guinean Franc

Guatemala

Quetzal

Guyana

Guyana Dollar

Hong Kong

Hong Kong Dollar

Honduras

Lempira

Croatia

Kuna

Haiti

Gourde

Hungary

Forint

Indonesia

Rupiah

Israel

New Israeli Sheqel

Bhutan; India

Indian Rupee

Iraq

Iraqi Dinar

Iran, Islamic Republic Of

Iranian Rial

Iceland

Iceland Krona

Jamaica

Jamaican Dollar

Jordan

Jordanian Dinar

Japan

Yen

Kenya

Kenyan Shilling

Kyrgyzstan

Som

Cambodia

Riel

Comoros

Comorian Franc

Korea, Democratic People’s Republic Of

North Korean Won

Korea, Republic Of

Won

Kuwait

Kuwaiti Dinar

Cayman Islands

Cayman Islands Dollar

Kazakhstan

Tenge

Lao People’s Democratic Republic

Lao Kip

Lebanon

Lebanese Pound

Sri Lanka

Sri Lanka Rupee

Liberia

Liberian Dollar

Lesotho

Loti

Lithuania

Historic use Lithuanian Litas

Latvia

Historic use Latvian Lats

Libya

Libyan Dinar

Morocco; Western Sahara

Moroccan Dirham

Moldova, Republic Of

Moldovan Leu

Madagascar Macedonia, The Former Yugoslav Republic Of

Malagasy Ariary Denar

Seite 29 von 35

Bundeszentralamt für Steuern

Zweibuchstabiges Länderkürzel
HT HM VA HN HK HU IS IN ID IR IQ IE IM IL IT JM JP JE JO KZ KE KI KP KR KW KG LA LV LB LS LR LY LI LT LU MO MK MG MW MY MV ML MT MH MQ MR MU YT MX FM MD MC

Englische Umschreibung des Länderkürzels
Haiti Heard Island And Mcdonald Islands Holy See (Vatican City State) Honduras Hong Kong Hungary Iceland India Indonesia Iran, Islamic Republic Of Iraq Ireland Isle Of Man Israel Italy Jamaica Japan Jersey Jordan Kazakhstan Kenya Kiribati Korea, Democratic People's Republic Of Korea, Republic Of Kuwait Kyrgyzstan Lao People'S Democratic Republic Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macao North Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Marshall Islands Martinique Mauritania Mauritius Mayotte Mexico Micronesia, Federated States Of Moldova, Republic Of Monaco

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert
MMK MNT MOP MRO MRU MUR MVR MWK MXN MXV MYR MZN NAD NGN NIO NOK NPR NZD OMR PAB PEN PGK PHP PKR PLN PYG QAR RON RSD RUB RWF SAR SBD SCR SDG SEK SGD SHP SLL SOS SRD SSP STD STN SVC SYP SZL THB TJS TMT TND TOP

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet
Myanmar Mongolia Macao Mauritania Mauritania Mauritius Maldives Malawi Mexico Mexico Malaysia Mozambique Namibia Nigeria Nicaragua Bouvet Island; Norway; Svalbard And Jan Mayen Nepal Cook Islands; New Zealand; Niue; Pitcairn; Tokelau Oman Panama Peru Papua New Guinea Philippines Pakistan Poland Paraguay Qatar Romania Serbia Russian Federation Rwanda Saudi Arabia Solomon Islands Seychelles Sudan Sweden Singapore Saint Helena, Ascension And Tristan Da Cunha Sierra Leone Somalia Suriname South Sudan Sao Tome And Principe Sao Tome And Principe El Salvador Syrian Arab Republic Eswatini Thailand Tajikistan Turkmenistan Tunisia Tonga

Währungs-/Sprachbezeichnung
Kyat Tugrik Pataca Historic use Ouguiya Ouguiya Mauritius Rupee Rufiyaa Malawi Kwacha Mexican Peso Mexican Unidad de Inversion (UDI) Malaysian Ringgit Mozambique Metical Namibia Dollar Naira Cordoba Oro Norwegian Krone Nepalese Rupee New Zealand Dollar Rial Omani Balboa Sol Kina Philippine Peso Pakistan Rupee Zloty Guarani Qatari Rial Romanian Leu Serbian Dinar Russian Ruble Rwanda Franc Saudi Riyal Solomon Islands Dollar Seychelles Rupee Sudanese Pound Swedish Krona Singapore Dollar Saint Helena Pound Leone Somali Shilling Surinam Dollar South Sudanese Pound Historic use Dobra Dobra El Salvador Colon Syrian Pound Lilangeni Baht Somoni Turkmenistan New Manat Tunisian Dinar Pa’anga

Seite 30 von 35

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

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

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

Seite 31 von 35

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

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert
AK SQ AM AR AN HY AS AV AE AY AZ BA BM EU BE BN BH BI BS BR BG MY CA CH CE ZH CU
CV KW CO CR CS DA DV NL DZ EN EO ET EE FO FJ FI FR FY FF KA DE GD GA GL

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Akan Albanian Amharic Arabic Aragonese Armenian Assamese Avaric Avestan Aymara Azerbaijani Bashkir Bambara Basque Belarusian Bengali Bihari languages Bislama Bosnian Breton Bulgarian Burmese Catalan; Valencian Chamorro Chechen Chinese Church Slavic; Old Slavonic; Church Slavonic; Old Bulgarian; Old Church Slavonic Chuvash Cornish Corsican Cree Czech Danish Divehi; Dhivehi; Maldivian Dutch; Flemish Dzongkha English Esperanto Estonian Ewe Faroese Fijian Finnish French Western Frisian Fulah Georgian German Gaelic; Scottish Gaelic Irish Galician

Seite 32 von 35

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

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert
GV EL GN GU HT HA HE HZ
HI
HO
HR HU IG IS IO II IU IE IA ID IK IT JV JA KL KN KS KR KK KM KI RW KY KV KG KO KJ
KU LO LA LV LI LN LT LB LU LG MK MH ML MI MR

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Manx Greek Guarani Gujarati Haitian; Haitian Creole Hausa Hebrew Herero
Hindi
Hiri Motu
Croatian Hungarian Igbo Icelandic Ido Sichuan Yi; Nuosu Inuktitut Interlingue; Occidental Interlingua (International Auxiliary Language Association) Indonesian Inupiaq Italian Javanese Japanese Kalaallisut; Greenlandic Kannada Kashmiri Kanuri Kazakh Central Khmer Kikuyu; Gikuyu Kinyarwanda Kirghiz; Kyrgyz Komi Kongo Korean Kuanyama; Kwanyama
Kurdish Lao Latin Latvian Limburgan; Limburger; Limburgish Lingala Lithuanian Luxembourgish; Letzeburgesch Luba-Katanga Ganda Macedonian Marshallese Malayalam Maori Marathi

Seite 33 von 35

Bundeszentralamt für Steuern
Zweibuchstabiges Länderkürzel

Englische Umschreibung des Länderkürzels

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert
MS MG MT MN NA NV NR ND NG NE NN NB NO NY OC OJ OR OM OS PA FA PI PL PT PS QU RM RO RN RU SG SA SI SK SL SE SM SN SD SO ST ES SC SR SS SU SW SV TY TA TT TE

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Malay Malagasy Maltese Mongolian Nauru Navajo; Navaho Ndebele, South; South Ndebele Ndebele, North; North Ndebele Ndonga Nepali Norwegian Nynorsk; Nynorsk, Norwegian Bokmål, Norwegian; Norwegian Bokmål Norwegian Chichewa; Chewa; Nyanja Occitan; Provençal Ojibwa Oriya Oromo Ossetian; Ossetic Panjabi; Punjabi Persian Pali Polish Portuguese Pushto; Pashto Quechua Romansh Romanian; Moldavian; Moldovan Rundi Russian Sango Sanskrit Sinhala; Sinhalese Slovak Slovenian Northern Sami Samoan Shona Sindhi Somali Sotho, Southern Spanish; Castilian Sardinian Serbian Swati Sundanese Swahili Swedish Tahitian Tamil Tatar Telugu

Seite 34 von 35

Bundeszentralamt für Steuern
Zweibuchstabiges Länderkürzel

Englische Umschreibung des Länderkürzels

Datensatzbeschreibung Aufbau der Daten nach dem CARF-XML-Schema der OECD

CARF-XML-Schema v1.5 12.09.2025

Wert
TG TL TH BO TI TO TN TS TK TR TW UG UK UR UZ VE VI VO CY WA WO XH YI YO ZA ZU

Englische Bezeichnung des Landes, welche die Währung/Sprache als Landeswährung verwendet

Währungs-/Sprachbezeichnung
Tajik Tagalog Thai Tibetan Tigrinya Tonga (Tonga Islands) Tswana Tsonga Turkmen Turkish Twi Uighur; Uyghur Ukrainian Urdu Uzbek Venda Vietnamese Volapük Welsh Walloon Wolof Xhosa Yiddish Yoruba Zhuang; Chuang Zulu

Seite 35 von 35
