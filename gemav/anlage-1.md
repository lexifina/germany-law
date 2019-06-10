# Anlage 1 (zu § 2 Absatz 1 Nummer 5 und 6, den §§ 10 und 11)Verteilernetzausbaugebiete und Verteilernetzkomponenten

1. Ein Landkreis ist ein Verteilernetzausbaugebiet (VNAG), wenn in diesem Landkreis gilt:
  (PWind ∙ KWind + PPV ∙ KPV + PSonst ∙ KSonst − PHL ∙ KHL) – PHL> 0
2a. Die Verteilernetzkomponente für Windenergieanlagen an Land (VNKWind), die nicht unmittelbar an das Höchstspannungsnetz angeschlossen sind, ergibt sich je VNAG aus folgender Formel:
  VNKWind = KWind ∙ BWind
2b. Die Verteilernetzkomponente für Solaranlagen (VNKPV), die nicht unmittelbar an das Höchstspannungsnetz angeschlossen sind, ergibt sich je VNAG aus folgender Formel:
  VNKPV = KPV ∙ BPV
3. Im Sinn dieser Anlage ist oder sind:
  BPV der Basiswert für Solaranlagen; er beträgt 1,6 Cent pro Kilowattstunde,
  BWind der Basiswert für Windenergieanlagen an Land; er beträgt 0,73 Cent pro Kilowattstunde,
  KHL der jeweilige Minimallastfaktor für den Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist; dieser beträgt 0,45 für einen Landkreis mit einem PQ von 0; er beträgt 0,3 für einen Landkreis mit einem PQ von 1; für die Ermittlung der Minimallastfaktoren für Landkreise mit einem PQ zwischen 0 und 1 findet eine lineare Interpolation zwischen den Werten 0,45 und 0,3 statt,
  KPV der jeweilige Kapazitätsfaktor für Solaranlagen
    – für den Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist, oder
    – für das VNAG, für das die VNK nach Nummer 2b ermittelt wird;
    dieser beträgt 0,55 für einen Landkreis mit einem PQ kleiner 0,3; er beträgt 0,05 für einen Landkreis mit einem PQ größer 0,55; für die Ermittlung der Kapazitätsfaktoren für Landkreise mit einem PQ zwischen 0,3 und 0,55 findet eine lineare Interpolation zwischen den Werten 0,55 und 0,05 statt,
  KWind der jeweilige Kapazitätsfaktor für Windenergieanlagen an Land
    – für den Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist, oder
    – für das VNAG, für das die VNK nach Nummer 2a ermittelt wird;
    dieser beträgt 0 für einen Landkreis mit einem PQ kleiner 0,25; er beträgt 0,8 für einen Landkreis mit einem PQ größer 0,55; für die Ermittlung der Kapazitätsfaktoren für Landkreise mit einem PQ zwischen 0,25 und 0,55 findet eine lineare Interpolation zwischen den Werten 0 und 0,8 statt,
  KSonst der Kapazitätsfaktor für sonstige Anlagen zur Erzeugung von Strom aus erneuerbaren Energien; dieser beträgt 0,9,
  PHL der Näherungswert für die Höchstlast in dem Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist; er berechnet sich nach folgender Formel:
    PHL = 28 146 MW ∙ RFHL,HH + 27 295 MW ∙ RFHL,GHD + 28 259 MW ∙ RFHL,IND
    wobei:
    RFHL,HH der Regionalisierungsfaktor für die Höchstlast des Sektors „Haushalte“ für einen Landkreis ist; er berechnet sich aus dem Verhältnis der Bevölkerungszahl im jeweiligen Landkreis zur Bevölkerungszahl aller deutschen Landkreise gemäß der am 1. November 2017 vorliegenden aktuellsten Bevölkerungsstatistik des Statistischen Bundesamtes,
    RFHL,GHD der Regionalisierungsfaktor für die Höchstlast des Sektors „Gewerbe/Handel/Dienstleistung“ für einen Landkreis ist; er berechnet sich aus dem Verhältnis der Summe der Bruttowertschöpfung für die Wirtschaftszweige „Dienstleistungsbereiche“ (G-T) und „Baugewerbe“ (F) im jeweiligen Landkreis zur Summe der Bruttowertschöpfung für die Wirtschaftszweige „Dienstleistungsbereiche“ (G-T) und „Baugewerbe“ (F) aller deutschen Landkreise gemäß der neuesten am 1. November 2017 vorliegenden Volkswirtschaftlichen Gesamtrechnung der Länder und
    RFHL,IND der Regionalisierungsfaktor für die Höchstlast des Sektors „Industrie“ für einen Landkreis ist; er berechnet sich aus dem Verhältnis der Bruttowertschöpfung für den Wirtschaftszweig „produzierendes Gewerbe ohne Baugewerbe“ (B-E) im jeweiligen Landkreis zur Bruttowertschöpfung für den Wirtschaftszweig „produzierendes Gewerbe ohne Baugewerbe“ (B-E) aller deutschen Landkreise gemäß der neuesten am 1. November 2017 vorliegenden Volkswirtschaftlichen Gesamtrechnung der Länder,
  PPV die installierte Leistung von Solaranlagen, die nicht unmittelbar an das Höchstspannungsnetz angeschlossen sind, in dem Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist, gemäß Marktstammdatenregister zum relevanten Stichtag nach § 11 Absatz 2 Satz 2; dabei gelten nur solche Solaranlagen als unmittelbar an das Höchstspannungsnetz angeschlossen, bei denen das zum relevanten Stichtag nach § 11 Absatz 2 Satz 2 im Marktstammdatenregister ausdrücklich vermerkt ist,
  PSonst die installierte Leistung von sonstigen Anlagen zur Erzeugung von Strom aus erneuerbaren Energien, die nicht unmittelbar an das Höchstspannungsnetz angeschlossen sind, in dem Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist, gemäß Marktstammdatenregister zum relevanten Stichtag nach § 11 Absatz 2 Satz 2; dabei gelten nur solche Anlagen als unmittelbar an das Höchstspannungsnetz angeschlossen, bei denen das zum relevanten Stichtag nach § 11 Absatz 2 Satz 2 im Marktstammdatenregister ausdrücklich vermerkt ist,
  PWind die installierte Leistung von Windenergieanlagen an Land, die nicht unmittelbar an das Höchstspannungsnetz angeschlossen sind, in dem Landkreis, für den nach Nummer 1 ermittelt wird, ob er ein VNAG ist, gemäß Marktstammdatenregister zum relevanten Stichtag nach § 11 Absatz 2 Satz 2; dabei gelten nur solche Windenergieanlagen an Land als unmittelbar an das Höchstspannungsnetz angeschlossen, bei denen das zum relevanten Stichtag nach § 11 Absatz 2 Satz 2 im Marktstammdatenregister ausdrücklich vermerkt ist,
  PQ der Portfolio-Quotient, d. h. das Verhältnis der installierten Leistung von Windenergieanlagen an Land (PWind) zur installierten Leistung von Solaranlagen (PPV) in einem Landkreis; er bestimmt sich für einen Landkreis nach folgender Formel:
    [Bild: bgbl1_2017_j3167-1_0010.jpg]
