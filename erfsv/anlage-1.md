# Anlage 1 (zu § 1)Über die Schnittstellen des E-Rezept-Fachdienstes übermittelbare Daten

| Technisches Profil Datenfeld | Hersteller digitaler Gesundheitsan- wendungen | Gesetz- liche Kranken- versiche- rungen | Unter- nehmen der privaten Kranken- versicherung | Apotheken | Vertragsärzte und Vertragszahnärzte | Kranken- häuser | Vorsorge- und Reha- bilitations- einrich- tungen | Gesetz- liche Unfall- versiche- rungen |
| KBV_PR_FOR_ Coverage | teilweise | komplett | komplett | komplett | gar nicht | gar nicht | gar nicht | komplett |
| Type (Art des Kostenträgers) | nein | ja | ja | ja | nein | nein | nein | ja |
| Besondere Personengruppe | nein | ja | ja | ja | nein | nein | nein | ja |
| DMP-Kennzeichen (Disease-Management-Plan) | ja | ja | ja | ja | nein | nein | nein | ja |
| Versichertenart | nein | ja | ja | ja | nein | nein | nein | ja |
| WOP (Wohnortprinzip) | nein | ja | ja | ja | nein | nein | nein | ja |
| Payor (Bezahlende Person oder Versicherung) | nein | ja | ja | ja | nein | nein | nein | ja |
| Period (Start- und End-Zeitpunkt des Versicherungsschutzes) | nein | ja | ja | ja | nein | nein | nein | ja |
| KBV_PR_FOR_ Patient | teilweise | komplett | komplett | komplett | teilweise | teilweise | teilweise | komplett |
| Identifier (Versicherten-ID GKV/PKV) | nein | ja | ja | ja | nein | nein | nein | ja |
| Name | ja | ja | ja | ja | ja | ja | ja | ja |
| Geburtsdatum | nein | ja | ja | ja | ja | ja | ja | ja |
| Adresse | nein | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_FOR_ Practitioner | gar nicht | gar nicht | gar nicht | komplett | gar nicht | gar nicht | gar nicht | gar nicht |
| (Zahn-) Arztnummer | nein | nein | nein | ja | nein | nein | nein | nein |
| Name | nein | nein | nein | ja | nein | nein | nein | nein |
| Qualifikation | nein | nein | nein | ja | nein | nein | nein | nein |
| KBV_PR_FOR_ Organization | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht |
| Name | nein | nein | nein | nein | nein | nein | nein | nein |
| Adresse | nein | nein | nein | nein | nein | nein | nein | nein |
| Telecom (Kontaktdaten) | nein | nein | nein | nein | nein | nein | nein | nein |
| Identifier (Institutionskennzeichen, Betriebstättennummer, KVZ-Abrechnungsnummer) | nein | nein | nein | nein | nein | nein | nein | nein |
| KBV_PR_ERP_ Prescription | teilweise | komplett | teilweise | teilweise | teilweise | teilweise | teilweise | komplett |
| Zuzahlungsstatus | nein | ja | nein | ja | nein | nein | nein | ja |
| Notdienstgebühr | nein | ja | ja | ja | nein | nein | nein | ja |
| BVG (Bezug zum Bundesentschädigungsgesetz oder Bundesversorgungsgesetz) | nein | ja | ja | nein | nein | nein | nein | ja |
| Unfallinformationen | ja | ja | ja | ja | ja | ja | ja | ja |
| Mehrfachverordnung | ja | ja | ja | ja | ja | ja | ja | ja |
| Intent (Vorschlag, Plan, Anordnung) | ja | ja | ja | ja | ja | ja | ja | ja |
| authoredOn (Ausstellungsdatum) | ja | ja | ja | ja | ja | ja | ja | ja |
| note (zusätzliche Informationen) | ja | ja | ja | ja | ja | ja | ja | ja |
| dosageInstruction | ja | ja | ja | ja | ja | ja | ja | ja |
| quantity | ja | ja | ja | ja | ja | ja | ja | ja |
| substitution (erlaubt oder nicht) | ja | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_ERP_ PracticySupply | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht | gar nicht |
| KBV_PR_ERP_ Medication_PZN | komplett | teilweise | teilweise | komplett | komplett | komplett | komplett | teilweise |
| Arzneimittelkategorie | ja | ja | ja | ja | ja | ja | ja | ja |
| Impfstoff | ja | ja | ja | ja | ja | ja | ja | ja |
| Normgroesse | ja | ja | ja | ja | ja | ja | ja | ja |
| Code (PZN und Handelsname) | ja | ja | ja | ja | ja | ja | ja | ja |
| Form (powder, tablets, capsule) | ja | nein | nein | ja | ja | ja | ja | nein |
| Amount | ja | nein | nein | ja | ja | ja | ja | nein |
| Batch (number und expiration date) | ja | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_ERP_ Medication_ Ingredient | komplett | teilweise | teilweise | komplett | komplett | komplett | komplett | teilweise |
| Arzneimittelkategorie | ja | ja | ja | ja | ja | ja | ja | ja |
| Impfstoff | ja | ja | ja | ja | ja | ja | ja | ja |
| Normgroesse | ja | ja | ja | ja | ja | ja | ja | ja |
| Code (PZN und Handelsname) | ja | ja | ja | ja | ja | ja | ja | ja |
| Form (powder, tablets, capsule) | ja | nein | nein | ja | ja | ja | ja | nein |
| Amount | ja | nein | nein | ja | ja | ja | ja | nein |
| Ingredient (actual ingredient and strength) | ja | ja | ja | ja | ja | ja | ja | ja |
| Batch (number und expiration date) | ja | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_ERP_ Medication_ FreeText | komplett | komplett | komplett | komplett | komplett | komplett | komplett | komplett |
| Arzneimittelkategorie | ja | ja | ja | ja | ja | ja | ja | ja |
| Impfstoff | ja | ja | ja | ja | ja | ja | ja | ja |
| Code (Text der Freitextverordnung) | ja | ja | ja | ja | ja | ja | ja | ja |
| Form (Freitext) | ja | ja | ja | ja | ja | ja | ja | ja |
| Batch (number und expiration date) | ja | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_ERP_ Medication_ Compounding | teilweise | teilweise | teilweise | komplett | teilweise | teilweise | teilweise | teilweise |
| Arzneimittelkategorie | ja | ja | ja | ja | ja | ja | ja | ja |
| Impfstoff | ja | ja | ja | ja | ja | ja | ja | ja |
| Herstellungsanweisung | nein | nein | nein | ja | nein | nein | nein | nein |
| Verpackung | nein | nein | nein | ja | nein | nein | nein | nein |
| Code (Kennzeichnung Rezepturverordnung und Rezepturname) | ja | ja | ja | ja | ja | ja | ja | ja |
| Form (powder, tablets, capsule) | ja | nein | nein | ja | ja | ja | ja | nein |
| Amount | ja | nein | nein | ja | ja | ja | ja | nein |
| Ingredient •Item (actual ingredient or content)•Darreichungsform•strength | ja | nein | nein | ja | ja | ja | ja | nein |
| Batch (number und expiration date) | ja | ja | ja | ja | ja | ja | ja | ja |
| KBV_PR_ERP_ Composition | gar nicht | teilweise | komplett | teilweise | gar nicht | gar nicht | gar nicht | teilweise |
| Rechtsgrundlage | nein | ja | ja | ja | nein | nein | nein | ja |
| PKV-Tarif | nein | nein | ja | nein | nein | nein | nein | nein |
