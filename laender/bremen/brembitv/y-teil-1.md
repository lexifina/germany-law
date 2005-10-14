# Teil 1
Teil 1
Dieses Dokument enthält keine Vorgaben zur grundlegenden Technik, die für die Bereitstellung von elektronischen Inhalten und Informationen verwendet wird (Server, Router, Netzwerkarchitekturen und Protokolle, Betriebssysteme usw.) und hinsichtlich der zu verwendenden Benutzeragenten. Die Anforderungen und Bedingungen beziehen sich allein auf die der Nutzerin, dem Nutzer angebotenen elektronischen Inhalte und Informationen.
Die Anforderungen und Bedingungen dieser Anlage basieren grundsätzlich auf den Zugänglichkeitsrichtlinien für Web-Inhalte 1.0 (Web Content Accessibility Guidelines 1.0) des World Wide Web Consortiums vom 5. Mai 1999.
Die in Teil 1 dieser Anlage enthaltenen, bei ihrem ersten Auftreten im Text durch Unterstreichung kenntlich gemachten, grundlegenden technischen Fachbegriffe sind in Teil 2 dieser Anlage (Glossar) erläutert.
Priorität I
Anforderung | 1 | Für jeden Audio- oder visuellen Inhalt sind geeignete äquivalente Inhalte bereitzustellen, die den gleichen Zweck oder die gleiche Funktion wie der originäre Inhalt erfüllen.
Bedingung | 1.1 | Für jedes Nicht-Text-Element ist ein äquivalenter Text bereitzustellen. Dies gilt insbesondere für: Bilder, graphisch dargestellten Text einschließlich Symbolen, Regionen von Imagemaps, Animationen (z. B. animierte GIFs), Applets und programmierte Objekte, Zeichnungen, die auf der Verwendung von Zeichen und Symbolen des ASCII-Codes basieren (ASCII-Zeichnungen), Frames, Scripts, Bilder, die als Punkte in Listen verwendet werden, Platzhalter-Graphiken, graphische Buttons, Töne (abgespielt mit oder ohne Einwirkung des Benutzers), Audio-Dateien, die für sich allein stehen, Tonspuren von Videos und Videos.
 | 1.2 | Für jede aktive Region einer serverseitigen Imagemap sind redundante Texthyperlinks bereitzustellen
 | 1.3 | Für Multimedia-Präsentationen ist eine Audio-Beschreibung der wichtigen
 |  | Informationen der Videospur bereitzustellen.
 | 1.4 | Für jede zeitgesteuerte Multimedia-Präsentation (insbesondere Film oder Animation) sind äquivalente Alternativen (z.B. Untertitel oder Audiobeschreibungen der Videospur) mit der Präsentation zu synchronisieren.
Anforderung | 2 | Texte und Graphiken müssen auch dann verständlich sein, wenn sie ohne Farbe betrachtet werden.
 |  | Erläuterung:
 |  | Die Farb- und Signaturgestaltung z.B. von Bauleitplänen wird durch die Planzeichenverordnung 1990 (PlanzV 90) geregelt. Diese gesetzlich vorgegebene Farbgestaltung kann bei der Internet-Präsentation von Bauleitplänen auf einem Schwarz-Weiß-Bildschirm hinsichtlich einer ausreichend kontrastreichen Darstellung problematisch sein.
 |  | Die barrierefreie Umsetzung dieser Anforderung ist hier technisch und rechtlich noch nicht möglich - s. untenstehende Erläuterung zu 11.3 -.
Bedingung | 2.1 | Alle mit Farbe dargestellten Informationen müssen auch ohne Farbe verfügbar sein, z.B. durch den Kontext oder die hierfür vorgesehenen Elemente der verwendeten Markup-Sprache.
 | 2.2 | Bilder sind so zu gestalten, dass die Kombinationen aus Vordergrund- und Hintergrundfarbe auf einem Schwarz-Weiß-Bildschirm und bei der Betrachtung durch Menschen mit Farbfehlsichtigkeiten ausreichend kontrastieren.
Anforderung | 3 | Markup-Sprachen (insbesondere HTML) und Stylesheets sind entsprechend ihrer Spezifikationen und formalen Definitionen zu verwenden.
Bedingung | 3.1 | Soweit eine angemessene Markup-Sprache existiert, ist diese anstelle von Bildern zu verwenden, um Informationen darzustellen.
 | 3.2 | Mittels Markup-Sprachen geschaffene Dokumente sind so zu erstellen und zu deklarieren, dass sie gegen veröffentlichte formale Grammatiken validieren.
 | 3.3 | Es sind Stylesheets zu verwenden, um die Text- und Bildgestaltung sowie die Präsentation von mittels Markup-Sprachen geschaffener Dokumente zu beeinflussen.
 | 3.4 | Es sind relative anstelle von absoluten Einheiten in den Attributwerten der verwendeten Markup-Sprache und den Stylesheet-Property-Werten zu verwenden.
 | 3.5 | Zur Darstellung der Struktur von mittels Markup-Sprachen geschaffener Dokumente sind Überschriften-Elemente zu verwenden.
 | 3.6 | Zur Darstellung von Listen und Listenelementen sind die hierfür vorgesehenen Elemente der verwendeten Markup-Sprache zu verwenden.
 | 3.7 | Zitate sind mittels der hierfür vorgesehenen Elemente der verwendeten Markup-Sprache zu kennzeichnen.
Anforderung | 4 | Sprachliche Besonderheiten wie Wechsel der Sprache oder Abkürzungen sind erkennbar zu machen.
Bedingung | 4.1 | Wechsel und Änderungen der vorherrschend verwendeten natürlichen Sprache sind kenntlich zu machen.
Anforderung | 5 | Tabellen sind mittels der vorgesehenen Elemente der verwendeten Markup-Sprache zu beschreiben und in der Regel nur zur Darstellung tabellarischer Daten zu verwenden.
Bedingung | 5.1 | In Tabellen, die tabellarische Daten darstellen, sind die Zeilen- und Spaltenüberschriften mittels der vorgesehenen Elemente der verwendeten Markup-Sprache zu kennzeichnen.
 | 5.2 | Soweit Tabellen, die tabellarische Daten darstellen, zwei oder mehr Ebenen von Zeilen- und Spaltenüberschriften aufweisen, sind mittels der vorgesehenen Elemente der verwendeten Markup-Sprache Datenzellen und Überschriftenzellen einander zuzuordnen.
 | 5.3 | Tabellen sind nicht für die Text- und Bildgestaltung zu verwenden, soweit sie nicht auch in linearisierter Form dargestellt werden können.
 | 5.4 | Soweit Tabellen zur Text- und Bildgestaltung genutzt werden, sind keine der Strukturierung dienenden Elemente der verwendeten Markup-Sprache zur visuellen Formatierung zu verwenden.
Anforderung | 6 | Internetangebote müssen auch dann nutzbar sein, wenn der verwendete Benutzeragent neuere Technologien nicht unterstützt oder diese deaktiviert sind.
 |  | Erläuterung:
 |  | Geodaten bzw. Geoinformationen werden im Internet z.B. mittels Web Map Service (WMS) bereitgestellt. Hierbei werden die von einem Client (interaktiv) angeforderten Informationen auf der Serverseite aus sehr umfangreichen Vektordaten dynamisch in eine Kartenansicht in Form von Pixelgraphiken generiert und dem Client zur Verfügung gestellt. Diese relativ neue Technologie setzt zur Zeit teilweise auf Clientseite das Vorhandensein von installierten und aktivierten Plugins voraus.
 |  | Die barrierefreie Umsetzung dieser Anforderung ist in diesem Bereich technisch noch nicht möglich - s. untenstehende Erläuterung zu 11.3 -.
Bedingung | 6.1 | Es muss sichergestellt sein, dass mittels Markup-Sprachen geschaffene Dokumente verwendbar sind, wenn die zugeordneten Stylesheets deaktiviert sind.
 | 6.2 | Es muss sichergestellt sein, dass Äquivalente für dynamischen Inhalt aktualisiert werden, wenn sich der dynamische Inhalt ändert.
 | 6.3 | Es muss sichergestellt sein, dass mittels Markup-Sprachen geschaffene Dokumente verwendbar sind, wenn Scripts, Applets oder andere programmierte Objekte deaktiviert sind.
 | 6.4 | Es muss sichergestellt sein, dass die Eingabebehandlung von Scripts, Applets oder anderen programmierten Objekten vom Eingabegerät unabhängig ist.
 | 6.5 | Dynamische Inhalte müssen zugänglich sein. Insoweit dies nur mit unverhältnismäßig hohem Aufwand zu realisieren ist, sind gleichwertige alternative Angebote unter Verzicht auf dynamische Inhalte bereitzustellen.
Anforderung | 7 | Zeitgesteuerte Änderungen des Inhalts müssen durch die Nutzerin, den Nutzer kontrollierbar sein.
Bedingung | 7.1 | Bildschirmflackern ist zu vermeiden.
 | 7.2 | Blinkender Inhalt ist zu vermeiden.
 | 7.3 | Bewegung in mittels Markup-Sprachen geschaffener Dokumente ist entweder zu vermeiden oder es sind Mechanismen bereitzustellen, die der Nutzerin, dem Nutzer das Einfrieren der Bewegung oder die Änderung des Inhalts ermöglichen.
 | 7.4 | Automatische periodische Aktualisierungen in mittels Markup-Sprachen geschaffener Dokumente sind zu vermeiden.
 | 7.5 | Die Verwendung von Elementen der Markup-Sprache zur automatischen Weiterleitung ist zu vermeiden. Insofern auf eine automatische Weiterleitung nicht verzichtet werden kann, ist der Server entsprechend zu konfigurieren.
Anforderung | 8 | Die direkte Zugänglichkeit der in Internetangeboten eingebetteten Benutzerschnittstellen ist sicherzustellen.
Bedingung | 8.1 | Programmierte Elemente (insbesonder Scripts und Applets) sind so zu gestalten, dass sie entweder direkt zugänglich oder kompatibel mit assistiven Technologien sind.
Anforderung | 9 | Internetangebote sind so zu gestalten, dass Funktionen unabhängig vom Eingabegerät oder Ausgabegerät nutzbar sind.
Bedingung | 9.1 | Es sind clientseitige Imagemaps bereitzustellen, es sei denn die Regionen können mit den verfügbaren geometrischen Formen nicht definiert werden.
 | 9.2 | Jedes über eine eigene Schnittstelle verfügende Element muss in geräteunabhängiger Weise bedient werden können.
 | 9.3 | In Scripts sind logische anstelle von geräteabhängigen Event-Handlern zu spezifizieren.
Anforderung | 10 | Die Verwendbarkeit von nicht mehr dem jeweils aktuellen Stand der Technik entsprechenden assistiven Technologien und Browsern ist sicherzustellen, so weit der hiermit verbundene Aufwand nicht unverhältnismäßig ist.
 |  | Erläuterung:
 |  | Die Sicherstellung der Verwendbarkeit assistiver Technologien und Browser ist insbesondere dann unverhältnismäßig, wenn die assistiven Technologien und Browser älter als drei Jahre sind und der Verbreitungsgrad in der einschlägigen Benutzergruppe unter 5 % liegt.
Bedingung | 10.1 | Das Erscheinenlassen von Pop-Ups oder anderen Fenstern ist zu vermeiden. Die Nutzerin, der Nutzer ist über Wechsel der aktuellen Ansicht zu informieren.
 | 10.2 | Bei allen Formular-Kontrollelementen mit implizit zugeordneten Beschriftungen ist dafür Sorge zu tragen, dass die Beschriftungen korrekt positioniert sind.
Anforderung | 11 | Die zur Erstellung des Internetangebots verwendeten Technologien sollen öffentlich zugänglich und vollständig dokumentiert sein, wie z.B. die vom World Wide Web Consortium entwickelten Technologien.
Bedingung | 11.1 | Es sind öffentlich zugängliche und vollständig dokumentierte Technologien in ihrer jeweils aktuellen Version zu verwenden, soweit dies für die Erfüllung der angestrebten Aufgabe angemessen ist.
 | 11.2 | Die Verwendung von Funktionen, die durch die Herausgabe neuer Versionen überholt sind, ist zu vermeiden.
 | 11.3 | Soweit auch nach bestem Bemühen die Erstellung eines barrierefreien Internetangebots nicht möglich ist, ist ein alternatives, barrierefreies Angebot zur Verfügung zu stellen, dass äquivalente Funktionalitäten und Informationen gleicher Aktualität enthält, soweit es die technischen Möglichkeiten zulassen. Bei Verwendung nicht barrierefreier Technologien sind diese zu ersetzen, sobald aufgrund der technologischen Entwicklung äquivalente, zugängliche Lösungen verfügbar und einsetzbar sind.
 |  | Erläuterung
 |  | Das Erstellen eines zusätzlichen alternativen Internetangebots, das die Barrierefreiheit dadurch realisiert, dass eine z.B. eine reine Textdarstellung angeboten wird, ist nur vorgesehen, soweit nach bestem Bemühen das eigentliche Internetangebot nicht barrierefrei gestaltet werden kann. Für diese Ausnahmefälle wird die Möglichkeit eröffnet, bis zum Vorliegen barrierefreier Lösungen im Rahmen der technischen Gegebenheiten ein alternatives Angebot, das äquivalente Funktionalitäten und Informationen gleicher Aktualität enthält, anzubieten. Hierbei ist regelmäßig aktiv zu prüfen, ob aufgrund der technologischen Entwicklung barrierefreie Lösungen verfügbar und einsetzbar sind. Soweit die Prüfung das Vorliegen äquivalenter, barrierefreier Lösungen ergibt, sind die eingesetzten nicht barrierefreien Technologien umgehend zu ersetzen.
Anforderung | 12 | Der Nutzerin, dem Nutzer sind Informationen zum Kontext und zur Orientierung bereitzustellen.
Bedingung | 12.1 | Jeder Frame ist mit einem Titel zu versehen, um Navigation und Identifikation zu ermöglichen.
 | 12.2 | Der Zweck von Frames und ihre Beziehung zueinander ist zu beschreiben, soweit dies nicht aus den verwendeten Titeln ersichtlich ist.
 | 12.3 | Große Informationsblöcke sind mittels Elementen der verwendeten Markup-Sprache in leichter handhabbare Gruppen zu unterteilen.
 | 12.4 | Beschriftungen sind genau ihren Kontrollelementen zuzuordnen.
Anforderung | 13 | Navigationsmechanismen sind übersichtlich und schlüssig zu gestalten.
Bedingung | 13.1 | Das Ziel jedes Hyperlinks muss auf eindeutige Weise identifizierbar sein.
 | 13.2 | Es sind Metadaten bereitzustellen, um semantische Informationen zu Internetangeboten hinzuzufügen.
 | 13.3 | Es sind Informationen zur allgemeinen Anordnung und Konzeption eines Internetangebots, z.B. mittels eines Inhaltsverzeichnisses oder einer Sitemap, bereitzustellen.
 | 13.4 | Navigationsmechanismen müssen schlüssig und nachvollziehbar eingesetzt werden.
Anforderung | 14 | Das allgemeine Verständnis der angebotenen Inhalte ist durch angemessene Maßnahmen zu fördern.
Bedingung | 14.1 | Für jegliche Inhalte ist die klarste und einfachste Sprache zu verwenden, die angemessen ist.
Priorität II
Anforderung | 1 | Für jeden Audio- oder visuellen Inhalt sind geeignete äquivalente Inhalte bereitzustellen, die den gleichen Zweck oder die gleiche Funktion wie der originäre Inhalt erfüllen.
Bedingung | 1.5 | Für jede aktive Region einer clientseitigen Imagemap sind redundante Texthyperlinks bereitzustellen.
Anforderung | 2 | Texte und Graphiken müssen auch dann verständlich sein, wenn sie ohne Farbe betrachtet werden.
Bedingung | 2.3 | Texte sind so zu gestalten, dass die Kombinationen aus Vordergrund- und Hintergrundfarbe auf einem Schwarz-Weiß-Bildschirm und bei der Betrachtung durch Menschen mit Farbfehlsichtigkeiten ausreichend kontrastieren.
Anforderung | 3 | Markup-Sprachen (insbesondere HTML) und Stylesheets sind entsprechend ihrer Spezifikationen und formalen Definitionen zu verwenden.
Anforderung | 4 | Sprachliche Besonderheiten wie Wechsel der Sprache oder Abkürzungen sind erkennbar zu machen.
Bedingung | 4.2 | Abkürzungen und Akronyme sind an der Stelle ihres ersten Auftretens im Inhalt zu erläutern und durch die hierfür vorgesehenen Elemente der verwendeten Markup-Sprache kenntlich zu machen.
 | 4.3 | Die vorherrschend verwendete natürliche Sprache ist durch die hierfür vorgesehenen Elemente der verwendeten Markup-Sprache kenntlich zu machen.
Anforderung | 5 | Tabellen sind mittels der vorgesehenen Elemente der verwendeten Markup-Sprache zu beschreiben und in der Regel nur zur Darstellung tabellarischer Daten zu verwenden.
Bedingung | 5.5 | Für Tabellen sind unter Verwendung der hierfür vorgesehenen Elemente der genutzten Markup-Sprache Zusammenfassungen bereitzustellen.
 | 5.6 | Für Überschriftenzellen sind unter Verwendung der hierfür vorgesehenen Elemente der genutzten Markup-Sprache Abkürzungen bereitzustellen.
Anforderung | 6 | Internetangebote müssen auch dann nutzbar sein, wenn der verwendete Benutzeragent neuere Technologien nicht unterstützt oder diese deaktiviert sind.
Anforderung | 7 | Zeitgesteuerte Änderungen des Inhalts müssen durch die Nutzerin, den Nutzer kontrollierbar sein.
Anforderung | 8 | Die direkte Zugänglichkeit der in Internetangeboten eingebetteten Benutzerschnittstellen ist sicherzustellen.
Anforderung | 9 | Internetangebote sind so zu gestalten, dass Funktionen unabhängig vom Eingabegerät oder Ausgabegerät nutzbar sind.
Bedingung | 9.4 | Es ist eine mit der Tabulatortaste navigierbare, nachvollziehbare und schlüssige Reihenfolge von Hyperlinks, Formularkontrollelementen und Objekten festzulegen.
 | 9.5 | Es sind Tastaturkurzbefehle für Hyperlinks, die für das Verständnis des Angebots von entscheidender Bedeutung sind (einschließlich solcher in clientseitigen Imagemaps), Formularkontrollelemente und Gruppen von Formularkontrollelementen bereitzustellen.
Anforderung | 10 | Die Verwendbarkeit von nicht mehr dem jeweils aktuellen Stand der Technik entsprechenden assistiven Technologien und Browsern ist sicherzustellen, so weit der hiermit verbundene Aufwand nicht unverhältnismäßig ist.
Bedingung | 10.3 | Für alle Tabellen, die Text in parallelen Spalten mit Zeilenumbruch enthalten, ist alternativ linearer Text bereitzustellen.
 | 10.4 | Leere Kontrollelemente in Eingabefeldern und Textbereichen sind mit Platzhalterzeichen zu versehen.
 | 10.5 | Nebeneinanderliegende Hyperlinks sind durch von Leerzeichen umgebene, druckbare Zeichen zu trennen.
Anforderung | 11 | Die zur Erstellung des Internetangebots verwendeten Technologien sollen öffentlich zugänglich und vollständig dokumentiert sein, wie z.B. die vom World Wide Web Consortium entwickelten Technologien.
Bedingung | 11.4 | Der Nutzerin, dem Nutzer sind Informationen bereitzustellen, die es ihnen erlauben, Dokumente entsprechend ihren Vorgaben (z.B. Sprache) zu erhalten.
Anforderung | 12 | Der Nutzerin, dem Nutzer sind Informationen zum Kontext und zur Orientierung bereitzustellen.
Anforderung | 13 | Navigationsmechanismen sind übersichtlich und schlüssig zu gestalten.
Bedingung | 13.5 | Es sind Navigationsleisten bereitzustellen, um den verwendeten Navigationsmechanismus hervorzuheben und einen Zugriff darauf zu ermöglichen.
 | 13.6 | Inhaltlich verwandte oder zusammenhängende Hyperlinks sind zu gruppieren. Die Gruppen sind eindeutig zu benennen und müssen einen Mechanismus enthalten, der das Umgehen der Gruppe ermöglicht.
 | 13.7 | Soweit Suchfunktionen angeboten werden, sind der Nutzerin, dem Nutzer verschiedene Arten der Suche bereitzustellen.
 | 13.8 | Es sind aussagekräftige Informationen am Anfang von inhaltlich zusammenhängenden Informationsblöcken (z.B. Absätzen, Listen) bereitzustellen, die eine Differenzierung ermöglichen.
 | 13.9 | Soweit inhaltlich zusammenhängende Dokumente getrennt angeboten werden, sind Zusammenstellungen dieser Dokumente bereitzustellen.
 | 13.10 | Es sind Mechanismen zum Umgehen von ASCII-Zeichnungen bereitzustellen.
Anforderung | 14 | Das allgemeine Verständnis der angebotenen Inhalte ist durch angemessene Maßnahmen zu fördern.
Bedingung | 14.2 | Text ist mit graphischen oder Audio-Präsentationen zu ergänzen, sofern dies das Verständnis der angebotenen Information fördert.
 | 14.3 | Der gewählte Präsentationsstil ist durchgängig beizubehalten.
