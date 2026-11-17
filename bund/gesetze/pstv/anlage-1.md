# Anlage 1 (zu § 11)Datenfelder in den Personenstandsregistern

| Nr. | Datenfelder | Anmerkungen | Verwendung |
|  |  |  | Haupteintrag | Folgebeurkundung | Hinweis | Suchfeld | Beschränkung1 |
|  | Allgemeine Registerangaben für alle Register |  |  |  |  |  |  |
| 0001 | Name des Standesamts |  | X |  |  | X |  |
| 0010 | Standesamtsnummer | z. B. 06412001 für das Standesamt Frankfurt am Main, ggf. ergänzt um ein Suffix für ein verwaltetes Standesamt | X |  |  | X |  |
| 0011 | Art des Registers | G = Geburtenregister E = Eheregister L = Lebenspartnerschaftsregister S = Sterberegister | X |  |  | X |  |
| 0012 | Eintragsnummer | z. B. „334“ für die 334. Beurkundung einer Geburt eines Jahres; bei Stilllegung des Eintrags z. B. 334-1 für die erneute Beurkundung zu dieser Eintragsnummer | X |  |  | X |  |
| 0013 | Jahr des Eintrags | Bei Nacherfassung Jahr der ursprünglichen Beurkundung | X |  |  | X |  |
| 0014 | Nummer der Erst- und Folgebeurkundung | Beispiele: „0“ bei Erstbeurkundung, „3“ für die 3. Folgebeurkundung zu einem Haupteintrag | X | X |  |  |  |
| 0015 | Nummer eines Hinweises | Technisches Datum, Nummer |  |  | X |  |  |
| 0020 | Anlass der Beurkundung | z. B. Geburt, Namensänderung, Vaterschaftsanerkennung, Wiederannahme des Geburtsnamens, Berichtigung | X | X |  |  |  |
| 0030 | Anlass eines Hinweises |  |  |  | X |  | 1) |
| 0040 | Datum der Wirksamkeit | Wirksamkeit einer Folgebeurkundung |  | X |  |  |  |
| 0045 | Datum der Stilllegung | Wirksamkeit einer Stilllegung des Personenstandseintrags |  |  |  |  | 1) |
| 0048 | Sperrvermerk |  |  |  |  |  | 1) |
| 0049 | Datum Sperrvermerk | Datum des Fristablaufs eines Sperrvermerks |  |  |  |  | 1) |
| 0050 | Ort der Beurkundung |  | X | X |  |  |  |
| 0051 | Datum der Beurkundung |  | X | X |  |  |  |
| 0052 | Name der Urkundsperson |  | X | X |  |  |  |
| 0053 | Funktionsbezeichnung | Unterscheidung nach männlichen oder weiblichen Standesbeamten | X | X |  |  |  |
__________
| Nr. | Datenfelder | Anmerkungen | Verwendung |
|  |  |  | Haupteintrag | Folgebeurkundung | Hinweis | Suchfeld | Beschränkung1 |
|  | Geburtenregister |  |  |  |  |  |  |
|  | Angaben zur Geburt |  |  |  |  |  |  |
| 1040 | Tag der Geburt |  | X | X |  | X |  |
| 1041 | Geburtszeit | Stunde und Minute der Geburt | X | X |  |  |  |
| 1050 | Ort der Geburt |  | X | X |  | X |  |
| 1051 | Geburtsort, Ortsteil | Bei landesrechtlicher Vorgabe | X | X |  |  |  |
| 1052 | Geburtsort, Straße, Hausnummer |  | X | X |  |  |  |
| 1055 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 1057 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  | X |  |
| 1090 | Art der Geburt | Nur bei Totgeburt | X | X |  |  |  |
|  | Angaben zum Kind |  |  |  |  |  |  |
| 1101 | Familienname/Geburtsname | Angabe des aktuellen Geburtsnamens des Kindes | X | X |  | X |  |
| 1101A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 1102 | Vornamen |  | X | X |  | X |  |
| 1102A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 1119 | Recht der Namensführung | Verweis auf maßgebliches Recht des Kindes |  |  | X |  |  |
| 1120 | Geschlecht |  | X | X |  |  |  |
| 1130 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 1180 | Deutsche Staatsangehörigkeit | Nur Erwerb nach § 4 Abs. 3 StAG |  |  | X |  |  |
| 1198 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
| 1199 | Familiennamensführung nicht nachgewiesen | Nur bei nicht nachgewiesener Identität der Eltern | X |  |  |  |  |
|  | Angaben zu den Eltern |  |  |  |  |  |  |
|  | 1. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Geburtsurkunde | X | X | X |  | 4) |
| 1200 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Mutter“ oder „Vater“ angegeben werden; bei Folgebeurkundungen sind Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, als „Elternteil“ anzugeben, Beispiel: „1. Mutter“ | X | X |  |  | 4) |
| 1201 | Familienname |  | X | X |  | X |  |
| 1201A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 1202 | Geburtsname |  | X | X |  | X |  |
| 1202A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 1203 | Vornamen |  | X | X |  | X |  |
| 1203A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 1220 | Geschlecht |  | X | X |  |  |  |
| 1230 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 1240 | Tag der Geburt |  |  |  | X |  |  |
| 1250 | Ort der Geburt |  |  |  | X |  |  |
| 1255 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1257 | Staat der Geburt | Nur bei Geburt im Ausland |  |  | X |  |  |
| 1270 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1271 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1275 | Registernummer | Beispiel: G 399/2010 |  |  | X |  |  |
| 1280 | Staatsangehörigkeit |  |  |  | X |  |  |
| 1298 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
| 1299 | Identität nicht nachgewiesen | Nur bei nicht nachgewiesener Identität | X | X |  |  |  |
| 1299A | Namensführung nicht nachgewiesen |  | X | X |  |  |  |
|  | 2. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Geburtsurkunde | X | X | X |  | 4) |
| 1300 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Mutter“ oder „Vater“ angegeben werden; bei Folgebeurkundungen sind Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, als „Elternteil“ anzugeben, Beispiel: „2. Vater“ | X | X |  |  | 4) |
| 1301 | Familienname |  | X | X |  | X |  |
| 1301A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 1302 | Geburtsname |  | X | X |  | X |  |
| 1302A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 1303 | Vornamen |  | X | X |  | X |  |
| 1303A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 1320 | Geschlecht |  | X | X |  |  |  |
| 1330 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 1340 | Tag der Geburt |  |  |  | X |  |  |
| 1350 | Ort der Geburt |  |  |  | X |  |  |
| 1355 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1357 | Staat der Geburt | Nur bei Geburt im Ausland |  |  | X |  |  |
| 1370 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1371 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1375 | Registernummer | Beispiel: G 1499/2009 |  |  | X |  |  |
| 1380 | Staatsangehörigkeit |  |  |  | X |  |  |
| 1398 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
| 1399 | Identität nicht nachgewiesen | Nur bei nicht nachgewiesener Identität | X | X |  |  |  |
| 1399A | Namensführung nicht nachgewiesen |  | X | X |  |  |  |
|  | Eheschließung der Eltern |  |  |  |  |  |  |
| 1440 | Tag der Eheschließung |  |  |  | X |  |  |
| 1450 | Ort der Eheschließung |  |  |  | X |  |  |
| 1457 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 1470 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1471 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1475 | Registernummer | Beispiel: E 67/2009 |  |  | X |  |  |
|  | Ehe des Kindes |  |  |  |  |  |  |
| 1540 | Tag der Eheschließung |  |  |  | X |  |  |
| 1550 | Ort der Eheschließung |  |  |  | X |  |  |
| 1555 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1557 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 1570 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1571 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1575 | Registernummer | Beispiel: E 288/2030 |  |  | X |  |  |
| 1590 | Art der Eheauflösung | Beispiel: Scheidung oder Tod |  |  | X |  | 3) |
| 1591 | Datum der Eheauflösung | Wirksamkeitsdatum oder Todestag |  |  | X |  | 3) |
| 1592 | Registerbehörde | Funktionsbezeichnung |  |  | X |  | 3) |
| 1593 | Behördenname | Ortsbezeichnung |  |  | X |  | 3) |
| 1595 | Registernummer/Aktenzeichen |  |  |  | X |  | 3) |
|  | Lebenspartnerschaft des Kindes |  |  |  |  |  |  |
| 1640 | Tag der Begründung |  |  |  | X |  |  |
| 1650 | Ort der Begründung |  |  |  | X |  |  |
| 1655 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1657 | Staat der Begründung | Nur bei Begründung im Ausland |  |  | X |  |  |
| 1670 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1671 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1675 | Registernummer | Beispiel: L 12/2009 |  |  | X |  |  |
| 1690 | Art der Auflösung der Lebenspartnerschaft | Beispiel: Aufhebung oder Tod |  |  | X |  | 3) |
| 1691 | Datum der Auflösung | Wirksamkeitsdatum oder Todestag |  |  | X |  | 3) |
| 1692 | Registerbehörde | Funktionsbezeichnung |  |  | X |  | 3) |
| 1693 | Behördenname | Ortsbezeichnung |  |  | X |  | 3) |
| 1695 | Registernummer/Aktenzeichen |  |  |  | X |  | 3) |
|  | Kind des Kindes |  |  |  |  |  |  |
| 1700 | Anzahl der eingetragenen Kinder |  |  |  | X |  | 1) |
| 1701 | Familienname | Angabe des Geburtsnamens des Kindes |  |  | X |  |  |
| 1705 | Vornamen |  |  |  | X |  |  |
| 1740 | Tag der Geburt |  |  |  | X |  |  |
| 1750 | Ort der Geburt |  |  |  | X |  |  |
| 1755 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1757 | Staat der Geburt | Nur bei Geburt im Ausland |  |  | X |  |  |
| 1770 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 1771 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1775 | Registernummer | Beispiel: G 475/2031 |  |  | X |  |  |
| 1790 | Art der Geburt | Nur bei Totgeburt |  |  | X |  | 2) |
|  | Testamentsverzeichnis |  |  |  |  |  |  |
| 1890 | Testamentsverzeichnisnummer |  |  |  | X |  | 3) |
|  | Tod, Todeserklärung, Feststellung der Todeszeit des Kindes |  |  |  |  |  |  |
| 1940 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war |  |  | X |  |  |
| 1942 | Tag des Beginns eines Sterbezeitzeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde |  |  | X |  |  |
| 1950 | Sterbeort |  |  |  | X |  |  |
| 1955 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 1957 | Sterbeort, Staat | Nur bei Tod im Ausland |  |  | X |  |  |
| 1960 | Festgestellter Todestag bei Todeserklärung | Datum |  |  | X |  | 2) |
| 1970 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 1971 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 1975 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
| Nr. | Datenfelder | Anmerkungen | Verwendung |
|  |  |  | Haupteintrag | Folgebeurkundung | Hinweis | Suchfeld | Beschränkung1 |
|  | Eheregister |  |  |  |  |  |  |
|  | Angaben zur Ehe |  |  |  |  |  |  |
| 2040 | Tag der Eheschließung | Ggf. Tag der Umwandlung einer Lebenspartnerschaft in eine Ehe | X |  |  | X |  |
| 2050 | Ort der Eheschließung | Ggf. Ort der Umwandlung einer Lebenspartnerschaft in eine Ehe | X |  |  | X |  |
| 2051 | Ort der Eheschließung, Ortsteil | Bei landesrechtlicher Vorgabe | X | X |  |  | 2) |
| 2055 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X |  |  |  | 2) |
| 2057 | Staat der Eheschließung | Nur bei Eheschließung im Ausland | X |  |  | X |  |
| 2058 | Namensbestimmung | Gemeinsamer Familienname ist Name des Ehegatten zu 1., zu 2. oder Doppelname |  |  | X |  |  |
|  | Angaben zur Lebenspartnerschaft bei Umwandlung in eine Ehe |  |  |  |  |  |  |
| 2060 | Tag der Begründung der Lebenspartnerschaft | Tag der Begründung einer zu dieser Ehe umgewandelten Lebenspartnerschaft | X | X |  | X | 4) |
| 2070 | Registerbehörde | Funktionsbezeichnung |  |  | X |  | 4) |
| 2071 | Behördenname | Ortsbezeichnung |  |  | X |  | 4) |
| 2075 | Registernummer |  |  |  | X |  | 4) |
|  | Angaben zu den Ehegatten |  |  |  |  |  |  |
|  | 1. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Eheurkunde | X | X | X |  | 4) |
| 2100 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Ehefrau“ oder „Ehemann“ angegeben werden; Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, sind als „Ehepartner“ anzugeben, Beispiel: „1. Ehemann“ | X | X |  |  | 4) |
| 2101 | Familienname vor der Ehe |  | X | X |  | X |  |
| 2101A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 2102 | Geburtsname vor der Ehe |  | X | X |  | X |  |
| 2102A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 2103 | Vornamen vor der Ehe |  | X | X |  | X |  |
| 2103A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 2111 | Familienname in der Ehe |  | X | X |  | X |  |
| 2111A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 2112 | Geburtsname in der Ehe |  | X | X |  | X |  |
| 2112A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 2113 | Vornamen in der Ehe |  | X | X |  | X | 2) |
| 2113A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  | 2) |
| 2114 | Familienname nach Eheauflösung |  |  | X |  | X |  |
| 2114A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens nach Eheauflösung |  | X |  |  |  |
| 2115 | Geburtsname nach Eheauflösung |  |  | X |  | X |  |
| 2115A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens nach Eheauflösung |  | X |  |  |  |
| 2116 | Vorname nach Eheauflösung |  |  | X |  | X | 2) |
| 2116A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens nach Eheauflösung |  | X |  |  | 2) |
| 2119 | Recht der Namensführung | Verweis auf maßgebliches Recht |  |  | X |  |  |
| 2120 | Geschlecht |  | X | X |  |  | 2) |
| 2130 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 2140 | Tag der Geburt |  | X | X |  | X |  |
| 2150 | Ort der Geburt |  | X | X |  |  |  |
| 2155 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 2157 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  |  |  |
| 2170 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2171 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2175 | Registernummer |  |  |  | X |  |  |
| 2180 | Staatsangehörigkeit |  |  |  | X |  |  |
| 2198 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
|  | 2. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Eheurkunde | X | X | X |  | 4) |
| 2200 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Ehefrau“ oder „Ehemann“ angegeben werden; Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, sind als „Ehepartner“ anzugeben, Beispiel: „2. Ehefrau“ | X | X |  |  | 4) |
| 2201 | Familienname vor der Ehe |  | X | X |  | X |  |
| 2201A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 2202 | Geburtsname vor der Ehe |  | X | X |  | X |  |
| 2202A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 2203 | Vornamen vor der Ehe |  | X | X |  | X |  |
| 2203A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 2211 | Familienname in der Ehe |  | X | X |  | X |  |
| 2211A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 2212 | Geburtsname in der Ehe |  | X | X |  | X |  |
| 2212A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 2213 | Vornamen in der Ehe |  | X | X |  | X | 2) |
| 2213A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  | 2) |
| 2214 | Familienname nach Eheauflösung |  |  | X |  | X |  |
| 2214A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens nach Eheauflösung |  | X |  |  |  |
| 2215 | Geburtsname nach Eheauflösung |  |  | X |  | X |  |
| 2215A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens nach Eheauflösung |  | X |  |  |  |
| 2216 | Vornamen nach Eheauflösung |  |  | X |  | X | 2) |
| 2216A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens nach Eheauflösung |  | X |  |  | 2) |
| 2219 | Recht der Namensführung | Verweis auf maßgebliches Recht |  |  | X |  |  |
| 2220 | Geschlecht |  | X | X |  |  | 2) |
| 2230 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 2240 | Tag der Geburt |  | X | X |  | X |  |
| 2250 | Ort der Geburt |  | X | X |  |  |  |
| 2255 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 2257 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  |  |  |
| 2270 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2271 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2275 | Registernummer |  |  |  | X |  |  |
| 2280 | Staatsangehörigkeit |  |  |  | X |  |  |
| 2298 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
|  | Auflösung der Ehe |  |  |  |  |  |  |
| 2390 | Art der Eheauflösung | Beispiel: Scheidung, Aufhebung, Tod, Wiederverheiratung nach Todeserklärung |  | X |  |  | 3) |
|  | Auflösung durch Entscheidung |  |  |  |  |  |  |
| 2391 | Datum der Eheauflösung | Datum der Rechtskraft der Scheidung |  | X |  |  |  |
| 2392 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 2393 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2395 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Tod, Todeserklärung, Feststellung der Todeszeit zu 1. |  |  |  |  |  |  |
| 2440 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war |  | X |  |  |  |
| 2442 | Tag des Beginns eines Sterbezeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde |  | X |  |  |  |
| 2450 | Sterbeort |  |  | X |  |  |  |
| 2455 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  | X |  |  | 2) |
| 2457 | Sterbeort, Staat | Nur bei Tod im Ausland |  | X |  |  |  |
| 2460 | Festgestellter Todestag bei Todeserklärung | Datum |  | X |  |  | 2) |
| 2470 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 2471 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2475 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Tod, Todeserklärung, Feststellung der Todeszeit zu 2. |  |  |  |  |  |  |
| 2540 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war |  | X |  |  |  |
| 2542 | Tag des Beginns eines Sterbezeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde |  | X |  |  |  |
| 2550 | Sterbeort |  |  | X |  |  |  |
| 2555 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  | X |  |  | 2) |
| 2557 | Sterbeort, Staat | Nur bei Tod im Ausland |  | X |  |  |  |
| 2560 | Festgestellter Todestag bei Todeserklärung | Datum |  | X |  |  | 2) |
| 2570 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 2571 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2575 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Neue Ehe zu 1. |  |  |  |  |  |  |
| 2640 | Tag der Eheschließung |  |  |  | X |  |  |
| 2641 | Tag der Eheschließung nach Todeserklärung | Nur im Fall der Wiederverheiratung nach Todeserklärung des vorherigen Ehegatten nach § 1319 BGB |  | X |  |  |  |
| 2650 | Ort der Eheschließung |  |  |  | X |  |  |
| 2657 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 2670 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2671 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2675 | Registernummer |  |  |  | X |  |  |
|  | Neue Ehe zu 2. |  |  |  |  |  |  |
| 2740 | Tag der Eheschließung |  |  |  | X |  |  |
| 2741 | Tag der Eheschließung nach Todeserklärung | Nur im Fall der Wiederverheiratung nach Todeserklärung des vorherigen Ehegatten nach § 1319 BGB |  | X |  |  |  |
| 2750 | Ort der Eheschließung |  |  |  | X |  |  |
| 2757 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 2770 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2771 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2775 | Registernummer |  |  |  | X |  |  |
|  | Neue Lebenspartnerschaft zu 1. |  |  |  |  |  |  |
| 2840 | Tag der Begründung |  |  |  | X |  |  |
| 2850 | Ort der Begründung |  |  |  | X |  |  |
| 2857 | Staat der Begründung | Nur bei Begründung im Ausland |  |  | X |  |  |
| 2870 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2871 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2875 | Registernummer |  |  |  | X |  |  |
|  | Neue Lebenspartnerschaft zu 2. |  |  |  |  |  |  |
| 2940 | Tag der Begründung |  |  |  | X |  |  |
| 2950 | Ort der Begründung |  |  |  | X |  |  |
| 2957 | Staat der Begründung | Nur bei Begründung im Ausland |  |  | X |  |  |
| 2970 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 2971 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 2975 | Registernummer |  |  |  | X |  |  |
| Nr. | Datenfelder | Anmerkungen | Verwendung |
|  |  |  | Haupteintrag | Folgebeurkundung | Hinweis | Suchfeld | Beschränkung1 |
|  | Lebenspartnerschaftsregister |  |  |  |  |  |  |
|  | Angaben zur Lebenspartnerschaft |  |  |  |  |  |  |
| 3040 | Tag der Begründung |  | X |  |  | X |  |
| 3050 | Ort der Begründung |  | X |  |  | X |  |
| 3051 | Ort der Begründung, Ortsteil | Bei landesrechtlicher Vorgabe | X | X |  |  | 2) |
| 3055 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X |  |  |  | 2) |
| 3057 | Staat der Begründung | Nur bei Begründung im Ausland | X |  |  | X |  |
| 3070 | Behörde der Begründung | Angabe einer vom Standesamt abweichenden Begründungsbehörde | X |  |  |  | 3) |
| 3078 | Namensbestimmung | Gemeinsamer Familienname ist Name des Lebenspartners zu 1., zu 2. oder Doppelname |  |  | X |  |  |
|  | Angaben zu den Lebenspartnern |  |  |  |  |  |  |
|  | 1. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Lebenspartnerschaftsurkunde | X | X | X |  | 4) |
| 3100 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Lebenspartner“ oder „Lebenspartnerin“ angegeben werden; Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, sind als „Lebenspartner“ anzugeben, Beispiel: „1. Lebenspartner“ | X | X |  |  | 4) |
| 3101 | Familienname vor der Begründung |  | X | X |  | X |  |
| 3101A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 3102 | Geburtsname vor der Begründung |  | X | X |  | X |  |
| 3102A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 3103 | Vornamen vor der Begründung |  | X | X |  | X |  |
| 3103A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 3111 | Familienname in der Lebenspartnerschaft |  | X | X |  | X |  |
| 3111A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 3112 | Geburtsname in der Lebenspartnerschaft |  | X | X |  | X |  |
| 3112A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 3113 | Vornamen in der Lebenspartnerschaft |  | X | X |  | X | 2) |
| 3113A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  | 2) |
| 3114 | Familienname nach Auflösung der Lebenspartnerschaft |  |  | X |  | X |  |
| 3114A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens |  | X |  |  |  |
| 3115 | Geburtsname nach Auflösung der Lebenspartnerschaft |  |  | X |  | X |  |
| 3115A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens |  | X |  |  |  |
| 3116 | Vornamen nach Auflösungder Lebenspartnerschaft |  |  | X |  | X | 2) |
| 3116A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens |  | X |  |  | 2) |
| 3119 | Recht der Namensführung | Verweis auf maßgebliches Recht |  |  | X |  |  |
| 3120 | Geschlecht |  | X | X |  |  | 2) |
| 3130 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 3140 | Tag der Geburt |  | X | X |  | X |  |
| 3150 | Ort der Geburt |  | X | X |  |  |  |
| 3155 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 3157 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  |  |  |
| 3170 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3171 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3175 | Registernummer |  |  |  | X |  |  |
| 3180 | Staatsangehörigkeit |  |  |  | X |  |  |
| 3198 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
|  | 2. | Leittext zur Zuordnung der folgenden Datenfelder sowie der Hinweise und Folgebeurkundungen im Registerausdruck und in der Lebenspartnerschaftsurkunde | X | X | X |  | 4) |
| 3200 | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Lebenspartner“ oder „Lebenspartnerin“ angegeben werden; Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, sind als „Lebenspartner“ anzugeben, Beispiel: „2. Lebenspartner“ | X | X |  |  | 4) |
| 3201 | Familienname vor der Begründung |  | X | X |  | X |  |
| 3201A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 3202 | Geburtsname vor der Begründung |  | X | X |  | X |  |
| 3202A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 3203 | Vornamen vor der Begründung |  | X | X |  | X |  |
| 3203A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 3211 | Familienname in der Lebenspartnerschaft |  | X | X |  | X |  |
| 3211A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 3212 | Geburtsname in der Lebenspartnerschaft |  | X | X |  | X |  |
| 3212A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 3213 | Vornamen in der Lebenspartnerschaft |  | X | X |  | X | 2) |
| 3213A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  | 2) |
| 3214 | Familienname nach Auflösung der Lebenspartnerschaft |  |  | X |  | X |  |
| 3214A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens |  | X |  |  |  |
| 3215 | Geburtsname nach Auflösung der Lebenspartnerschaft |  |  | X |  | X |  |
| 3215A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens |  | X |  |  |  |
| 3216 | Vornamen nach Auflösungder Lebenspartnerschaft |  |  | X |  | X | 2) |
| 3216A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens |  | X |  |  | 2) |
| 3219 | Recht der Namensführung | Verweis auf maßgebliches Recht |  |  | X |  |  |
| 3220 | Geschlecht |  | X | X |  |  | 2) |
| 3230 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 3240 | Tag der Geburt |  | X | X |  | X |  |
| 3250 | Ort der Geburt |  | X | X |  |  |  |
| 3255 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 3257 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  |  |  |
| 3270 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3271 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3275 | Registernummer |  |  |  | X |  |  |
| 3280 | Staatsangehörigkeit |  |  |  | X |  |  |
| 3298 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
|  | Auflösung oder Umwandlung der Lebenspartnerschaft in eine Ehe |  |  |  |  |  |  |
| 3390 | Art der Auflösung | Beispiel: Aufhebung, Tod, Todeserklärung, Feststellung der Todeszeit, Umwandlung in Ehe |  | X |  |  | 3) |
|  | Auflösung durch Entscheidung |  |  |  |  |  |  |
| 3391 | Datum der Auflösung | Datum der Rechtskraft der Auflösungsentscheidung oder der Umwandlung |  | X |  |  |  |
| 3392 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 3393 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3395 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Tod, Todeserklärung, Feststellung der Todeszeit zu 1. |  |  |  |  |  |  |
| 3440 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war |  | X |  |  |  |
| 3442 | Tag des Beginns eines Sterbezeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde |  | X |  |  |  |
| 3450 | Sterbeort |  |  | X |  |  |  |
| 3455 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  | X |  |  | 2) |
| 3457 | Sterbeort, Staat | Nur bei Tod im Ausland |  | X |  |  |  |
| 3460 | Festgestellter Todestag bei Todeserklärung | Datum |  | X |  |  | 2) |
| 3470 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 3471 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3475 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Tod, Todeserklärung, Feststellung der Todeszeit zu 2. |  |  |  |  |  |  |
| 3540 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war |  | X |  |  |  |
| 3542 | Tag des Beginns eines Sterbezeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde |  | X |  |  |  |
| 3550 | Sterbeort |  |  | X |  |  |  |
| 3555 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  | X |  |  | 2) |
| 3557 | Sterbeort, Staat | Nur bei Tod im Ausland |  | X |  |  |  |
| 3560 | Festgestellter Todestag bei Todeserklärung | Datum |  | X |  |  | 2) |
| 3570 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 3571 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3575 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
|  | Neue Ehe zu 1. |  |  |  |  |  |  |
| 3640 | Tag der Eheschließung |  |  |  | X |  |  |
| 3650 | Ort der Eheschließung |  |  |  | X |  |  |
| 3657 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 3670 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3671 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3675 | Registernummer |  |  |  | X |  |  |
|  | Neue Ehe zu 2. |  |  |  |  |  |  |
| 3740 | Tag der Eheschließung |  |  |  | X |  |  |
| 3750 | Ort der Eheschließung |  |  |  | X |  |  |
| 3757 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 3770 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3771 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3775 | Registernummer |  |  |  | X |  |  |
|  | Neue Lebenspartnerschaft zu 1. |  |  |  |  |  |  |
| 3840 | Tag der Begründung |  |  |  | X |  |  |
| 3850 | Ort der Begründung |  |  |  | X |  |  |
| 3857 | Staat der Begründung | Nur bei Begründung der Lebenspartnerschaft im Ausland |  |  | X |  |  |
| 3870 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3871 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3875 | Registernummer |  |  |  | X |  |  |
|  | Neue Lebenspartnerschaft zu 2. |  |  |  |  |  |  |
| 3940 | Tag der Begründung |  |  |  | X |  |  |
| 3950 | Ort der Begründung |  |  |  | X |  |  |
| 3957 | Staat der Begründung | Nur bei Begründung der Lebenspartnerschaft im Ausland |  |  | X |  |  |
| 3970 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 3971 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 3975 | Registernummer |  |  |  | X |  |  |
| Nr. | Datenfelder | Anmerkungen | Verwendung |
|  |  |  | Haupteintrag | Folgebeurkundung | Hinweis | Suchfeld | Beschränkung1 |
|  | Sterberegister |  |  |  |  |  |  |
|  | Angaben zum Sterbefall |  |  |  |  |  |  |
| 4140 | Todestag | Datum des Todes oder Datum des Tages, an dem die Person mit Sicherheit tot war | X | X |  | X |  |
| 4141 | Todeszeit | Uhrzeit des Todes oder Uhrzeit, zu der die Person mit Sicherheit tot war | X | X |  |  |  |
| 4142 | Tag des Beginns eines Sterbezeitzeitraums | Datum des Tages, an dem die Person zuletzt lebend gesehen wurde | X | X |  | X |  |
| 4143 | Uhrzeit des Beginns eines Sterbezeitzeitraums | Uhrzeit, zu der die Person zuletzt lebend gesehen wurde | X | X |  |  |  |
| 4144 | Todeszeit (nicht exakt) | Nur in Ergänzung zu Feld 4141, wenn Uhrzeit des Todes nur ungefähr (gegen … Uhr) feststeht | X | X |  |  | 2) |
| 4150 | Sterbeort | Bei unbekanntem Sterbeort auch Auffindungsort | X | X |  | X |  |
| 4151 | Sterbeort, Ortsteil | Bei landesrechtlicher Vorgabe | X | X |  |  |  |
| 4152 | Sterbeort, Straße, Hausnummer |  | X | X |  |  |  |
| 4155 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 4157 | Sterbeort, Staat | Nur bei Sterbefall im Ausland | X | X |  | X |  |
|  | Angaben zur verstorbenen Person |  |  |  |  |  |  |
| 4201 | Familienname |  | X | X |  | X |  |
| 4201A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 4202 | Geburtsname |  | X | X |  | X |  |
| 4202A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 4203 | Vornamen |  | X | X |  | X |  |
| 4203A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 4220 | Geschlecht |  | X | X |  |  | 2) |
| 4230 | Religion/Weltanschauung |  | X | X |  |  | 3) |
| 4240 | Tag der Geburt |  | X | X |  | X |  |
| 4250 | Ort der Geburt |  | X | X |  |  |  |
| 4255 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. | X | X |  |  | 2) |
| 4257 | Staat der Geburt | Nur bei Geburt im Ausland | X | X |  |  |  |
| 4270 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 4271 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 4275 | Registernummer |  |  |  | X |  |  |
| 4290 | Anschrift, Straße, Hausnummer |  | X | X |  |  |  |
| 4293 | Anschrift, Ort |  | X | X |  |  |  |
| 4294 | Anschrift, Ortsteil | Bei landesrechtlicher Vorgabe | X | X |  |  |  |
| 4297 | Anschrift, Staat | Nur bei Wohnort im Ausland | X | X |  |  |  |
| 4298 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
| 4299 | Identität nicht nachgewiesen | Nur bei nicht nachgewiesener Identität | X | X |  |  |  |
|  | Familienstand der verstorbenen Person |  |  |  |  |  |  |
| 4300 | Familienstand |  | X | X |  |  |  |
| 4300A | Familienrechtliche Bezeichnung | Es können die Bezeichnungen „Ehefrau“, „Ehemann, „Lebenspartner“ oder „Lebenspartnerin“ angegeben werden; Personen, die weder dem männlichen noch dem weiblichen Geschlecht angehören, sind als „Ehepartner“ oder „Lebenspartner“ anzugeben, Beispiel: „Lebenspartnerin“ | X | X |  |  | 4) |
| 4301 | Familienname des Ehegatten, Ehe- oder Lebenspartners |  | X | X |  |  |  |
| 4301A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Familiennamens | X | X |  |  |  |
| 4302 | Geburtsname des Ehegatten, Ehe- oder Lebenspartners |  | X | X |  |  |  |
| 4302A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Geburtsnamens | X | X |  |  |  |
| 4303 | Vornamen des Ehegatten, Ehe- oder Lebenspartners |  | X | X |  |  |  |
| 4303A | Ausländische Namensart | Bezeichnung einer ausländischen Namensform des Vornamens | X | X |  |  |  |
| 4320 | Geschlecht des Ehegatten, Ehe- oder Lebenspartners |  | X | X |  |  |  |
| 4398 | Identifikationsnummer | Gemäß § 139b der Abgabenordnung |  |  |  |  | 1) |
| 4399 | Identität nicht nachgewiesen | Nur bei nicht nachgewiesener Identität | X | X |  |  |  |
|  | Ehe der verstorbenen Person |  |  |  |  |  |  |
| 4440 | Tag der Eheschließung |  |  |  | X |  |  |
| 4450 | Ort der Eheschließung |  |  |  | X |  |  |
| 4455 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 4457 | Staat der Eheschließung | Nur bei Eheschließung im Ausland |  |  | X |  |  |
| 4470 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 4471 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 4475 | Registernummer |  |  |  | X |  |  |
| 4477 | Führungsort Heiratseintrag | Bei Eheschließung bis zum 31.12.2008 (§ 15a PStG a. F.) |  |  | X |  |  |
|  | Lebenspartnerschaft der verstorbenen Person |  |  |  |  |  |  |
| 4540 | Tag der Begründung |  |  |  | X |  |  |
| 4550 | Ort der Begründung |  |  |  | X |  |  |
| 4555 | Nähere Kennzeichnung des Ortes | Soweit zur Unterscheidung bei gleichlautenden Ortsnamen erforderlich, z. B. Kreis, Verwaltungsbezirk o. ä. |  |  | X |  | 2) |
| 4557 | Staat der Begründung | Nur bei Begründung im Ausland |  |  | X |  |  |
| 4570 | Registerbehörde | Funktionsbezeichnung |  |  | X |  |  |
| 4571 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 4575 | Registernummer |  |  |  | X |  |  |
|  | Todeserklärung, gerichtliche Feststellung der Todeszeit der verstorbenen Person |  |  |  |  |  |  |
| 4660 | Todeserklärung, gerichtliche Feststellung der Todeszeit | Beschlussdatum |  |  | X |  |  |
| 4670 | Registerbehörde/Gericht | Funktionsbezeichnung |  |  | X |  |  |
| 4671 | Behördenname | Ortsbezeichnung |  |  | X |  |  |
| 4675 | Registernummer/Aktenzeichen |  |  |  | X |  |  |
