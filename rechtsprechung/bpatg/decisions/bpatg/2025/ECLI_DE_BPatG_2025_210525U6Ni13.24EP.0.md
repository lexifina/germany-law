---
ecli: "ECLI:DE:BPatG:2025:210525U6Ni13.24EP.0"
court: "Bundespatentgericht"
aktenzeichen: "6 Ni 13/24 (EP)"
decided: "2025-05-21"
typ: "Urteil"
source_url: "https://testphase.rechtsinformationen.bund.de/v1/rechtsprechung/JURE259032042.xml"
neuris_doknr: "JURE259032042"
---

# Bundespatentgericht, 6 Ni 13/24 (EP) vom 2025-05-21

## Tenor

In der Patentnichtigkeitssache

…

betreffend das europäische Patent EP 2 919 228 (DE 60 2014 004 358)

hat der 6. Senat (Nichtigkeitssenat) des Bundespatentgerichts auf Grund der mündlichen Verhandlung vom 21. Mai 2025 durch die Vorsitzende Richterin Dr. Schnurr sowie die Richter Dipl.-Phys. Dr. Schwengelbeck, Dr.-Ing. Flaschke und Dr. Söchtig und die Richterin Dipl.-Phys. Dr. Schenkl

für Recht erkannt:

I.

Das europäische Patent 2 919 228 wird mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland dadurch teilweise für nichtig erklärt, dass seine Ansprüche die nachfolgende Fassung erhalten:

1.

A method for scrolling a musical score on a screen of a device, comprising:

- loading a file having a digital score in a piece of memory of said device, said score comprising a plurality of measures, said digital score being in a format which contains the same information as provided by a paper score;

- displaying at least one measure from said score on the screen;

- scrolling said musical measures as a continuous string of musical signs, drawn on the screen in a consecutive way, by continuously showing on the screen additional measures of music while the already scrolled measures disappear from the screen, wherein at least one whole measure is simultaneously drawn on the screen; wherein a measure scrolled on the screen is shown incomplete until the whole measure is completed;

- adjusting the measures scrolling speed, which is the amount of space covered by at least one measure on the screen divided by the time required for playing that at least one measure, according to the music content of the measures being displayed on the screen, to a tempo and to a number of beats per measure, wherein said tempo is either a tempo indicated in the digital score or a tempo imposed by a user; and said number of beats per measure is either the number of beats per measure imposed by a user who is actually playing or the number of beats per measure indicated in the digital score.

2. The method of claim 1, wherein the scrolling speed is adjusted every time the screen is refreshed.

3. The method of claim 1, wherein when the digital score is scrolled vertically, said scrolling speed is adjusted when a whole line disappears from the screen and a complete new line shows up on the screen.

4. The method of claim 1, wherein when the digital score is scrolled horizontally, said scrolling speed is adjusted every time a new measure turns up on the screen.

5. The method of claim 1, wherein the digital score is scrolled vertically, the scrolling speed being calculated as follows:

- estimating the time T required for playing said at least one measure according to the following formula:

wherein N is the total number of measures displayed on the screen, N being read from the digital score, and

T measure_i = n_beats measure_i / tempo

wherein "tempo" is either the tempo indicated in the digital score or a tempo imposed by the user and n_beats measure_i is the number of beats that the measure number "i" has, said number being either read from the digital score or imposed by the user;

- obtaining from the device the dimensions of the screen, thus calculating the space to be covered by said at least one measure;

- calculating the scrolling speed from said estimated time T required for playing the measures displayed on the screen and from said calculated space to be covered by said measures and scrolling the score at said calculated speed;

- repeating said calculation and adjusting the scrolling speed every time the screen is refreshed.

6. The method of claim 5, wherein a plurality of musical lines K is shown on the screen, each of said lines having at least one measure Mk, said number of measures per line being variable from line to line, the scrolling speed being calculated as follows:

- estimating the time T k required for playing each musical line shown on the screen as follows:

wherein k varies from 1 to K, K being the total number of lines shown on the screen, wherein M k is the number of measures in line k, and M 1 M 2 … M k … M K being read from the digital score,

- calculating the total time T required for playing the M k lines shown on the screen as follows:

- calculating an average time T av per line:

- rounding off said T av to the lower natural number;

- calculating the scrolling speed from said estimated time T av required for

playing the measures displayed on the screen and from said calculated space to be covered by said measures and scrolling the score at said calculated speed;

- repeating said calculation and adjusting the scrolling speed every time the screen is refreshed.

7. The method of claim 1, wherein the digital score is scrolled horizontally, the scrolling speed being calculated as follows:

every time a measure i starts to be displayed on the screen:

- estimating the time T required for playing said measure as follows:

wherein "tempo" is either the tempo indicated in the digital score or a tempo imposed by the user and n_beats measure_i is the number of beats that the measure number "i" has, said number being either read from the digital score or imposed by the user;

- obtaining from the device the length of the screen, thus calculating the space to be covered by said measure i;

-reading from the digital score the length of said measure i;

- calculating the scrolling speed by dividing the sum of the space to be covered by said measure and the length of said measure, by said estimated time T required for playing said measure;

- and scrolling the score at said calculated speed.

8. The method of any preceding claim, further comprising the steps of:

- identifying in the digital score at least one mark which indicates the repetition of one block of music;

- copying said block to be repeated;

- pasting in the file as many repetitions as indicated by said at least one mark, in a concatenated way, thus allowing the user to play the music in a linear way, avoiding the need of going back in the digital score.

9. The method of any preceding claim, which can be carried out by a plurality of users playing simultaneously the same score, the digital score being shown in a device of each user.

10. The method of any preceding claim, wherein said digital score is in the MusicXML format.

11. A device comprising means for carrying out the method according to any preceding claim, said device being a personal digital assistant (PDA), a portable reader device, a tablet, a cell phone or any device which comprises a memory, a processor and a screen or display.

12. A computer program product comprising computer program instructions/code for performing the method according to any of claims 1 - 10.

13. A computer-readable memory/medium that stores program instructions/code for performing the method according to any of claims 1 - 10.

II.

Die weitergehende Klage wird abgewiesen.

III.

Von den Kosten des Rechtsstreits haben die Klägerin 1/3 und die Beklagte 2/3 zu tragen.

IV.

Das Urteil ist im Kostenausspruch jeweils gegen Sicherheitsleistung in Höhe von 120 % des vollstreckbaren Betrages vorläufig vollstreckbar.

## Tatbestand

1 Die Beklagte ist Inhaberin des auch mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland erteilten europäischen Patents 2 919 228 (im Folgenden: Streitpatent) mit der Bezeichnung „Method, device and computer program for scrolling a musical score“ („Verfahren, Vorrichtung und Computerprogramm zum Scrollen einer Partitur“). Das am 12. März 2014 in der Verfahrenssprache Englisch angemeldete Streitpatent, dessen Erteilung am 19. Oktober 2016 veröffentlicht worden ist, nimmt keine Priorität in Anspruch und wird beim deutschen Patent- und Markenamt unter dem Aktenzeichen 60 2014 004 358.5 geführt.

2 Das Streitpatent umfasst in seiner erteilten Fassung insgesamt 13 Patentansprüche mit dem unabhängigen Patentanspruch 1, den Unteransprüchen 2 bis 10, welche sämtlich unmittelbar oder mittelbar auf den Patentanspruch 1 rückbezogen sind, sowie den nebengeordneten Ansprüchen 11 bis 13.

3 Die Klägerin begehrt die vollumfängliche Nichtigerklärung des Streitpatents, wobei sie sich auf die Nichtigkeitsgründe der unzulässigen Erweiterung sowie der fehlenden Patentfähigkeit in Form mangelnder erfinderischer Tätigkeit sowie fehlender Neuheit stützt (Art. II, § 6 Abs. 1, Nr. 1, 3 IntPatÜbkG i. V. m. Art 52 bis 57 EPÜ).

4 Die Beklagte verteidigt das Streitpatent in der erteilten Fassung sowie mit insgesamt fünf Hilfsanträgen 1, 2a, 2b, 2c, 3 und 4 vom 14. April 2025.

5 Der erteilte Anspruch 1 sowie die nebengeordneten Ansprüche 11 bis 13 lauten in der Verfahrenssprache Englisch wie folgt:

6 1.

A method for scrolling a musical score on a screen of a device, comprising:

7 - loading a file having a digital score in a piece of memory of said device, said score comprising a plurality of measures;

8 - displaying at least one measure from said score on the screen;

9 - scrolling said musical measures as a continuous string of musical signs, drawn on the screen in a consecutive way, by continuously showing on the screen additional measures of music while the already scrolled measures disappear from the screen, wherein at least one whole measure is simultaneously drawn on the screen; wherein a measure scrolled on the screen is shown incomplete until the whole measure is completed;

10 - adjusting the measures scrolling speed according to the music content of the measures being displayed on the screen, to a tempo and to a number of beats per measure, wherein said tempo is either a tempo indicated in the digital score or a tempo imposed by a user; and said number of beats per measure is either the number of beats per measure imposed by a user who is actually playing or the number of beats per measure indicated in the digital score.

11 11.

A device comprising means for carrying out the method according to any preceding claim, said device being a personal digital assistant (PDA), a portable reader device, a tablet, a cell phone or any device which comprises a memory, a processor and a screen or display.

12 12.

A computer program product comprising computer program instructions/code for performing the method according to any of claims 1-10.

13 13. A computer-readable memory/medium that stores program instructions/code for performing the method according to any of claims 1-10.

14 Deren deutsche Übersetzung ist in der Patentschrift wie folgt angegeben:

15 1.

Verfahren zum Rollen durch eine Partitur auf einem Bildschirm eines Geräts, das Folgendes beinhaltet:

16 - Laden einer Datei mit einer digitalen Partitur in einem Speicherteil des genannten Geräts, wobei die genannte Partitur mehrere Takte umfasst;

17 - Anzeigen wenigstens eines Takts aus der genannten Partitur auf dem Bildschirm;

18 - Rollen durch die genannten Musiktakte als kontinuierliche Folge von konsekutiv auf dem Bildschirm gezeichneten musikalischen Zeichen durch kontinuierliches Zeigen von zusätzlichen Musiktakten auf dem Bildschirm, während die bereits durchrollten Takte vom Bildschirm verschwinden, wobei wenigstens ein gesamter Takt gleichzeitig auf dem Bildschirm gezeichnet wird; wobei ein auf dem Bildschirm gerollter Takt unvollständig gezeigt wird, bis der gesamte Takt vollständig ist;

19 - Justieren der Taktrollgeschwindigkeit gemäß dem Musikeinhalt der auf dem Bildschirm angezeigten Maße, einem Tempo und einer Anzahl von Schlägen pro Takt, wobei das genannte Tempo entweder ein in der digitalen Partitur angezeigtes Tempo oder ein von einem Benutzer auferlegtes Tempo ist; und die genannte Anzahl von Schlägen pro Takt entweder die Anzahl von Schlägen pro Takt wie von einem tatsächlich spielenden Benutzer auferlegt oder die Anzahl von Schlägen pro Takt wie in der digitalen Partitur angezeigt ist.

20 11.

Gerät, das Mittel zum Ausführen des Verfahrens nach einem vorherigen Anspruch umfasst, wobei das genannte Gerät ein Personal Digital Assistant (PDA), ein tragbares Lesegerät, ein Tablet, ein Mobiltelefon oder ein beliebiges Gerät ist, das einen Speicher, einen Prozessor und einen Bildschirm oder ein Display umfasst.

21 12.

Computerprogrammprodukt, das Computerprogrammbefehle/-code zum Ausführen des Verfahrens nach einem der Ansprüche 1-10 umfasst.

22 13.

Computerlesbarer/-s Speicher/Medium, der/das Programmbefehle/-code zum Ausführen des Verfahrens nach einem der Ansprüche 1-10 speichert.

23 Wegen des Wortlauts der ebenfalls angegriffenen Unteransprüche 2 bis 10 wird auf die Streitpatentschrift EP 2 919 228 B1 verwiesen.

24 Die Klägerin ist der Auffassung, dass der Gegenstand des erteilten Patentanspruchs 1 über den Inhalt der europäischen Patentanmeldung in ihrer ursprünglich eingereichten Fassung hinausgehe.

25 Im Patentanspruch 1 sei die Formulierung „Partitur“ ersetzt worden durch die Formulierung „Musiktakte als kontinuierliche Folge von […] musikalischen Zeichen“. Diese Änderung sei nicht nur terminologischer Natur, sondern stelle auch eine substanzielle Verschiebung der beanspruchten Erfindung dar.

26 Darüber hinaus seien die ursprünglich offenbarten musikalischen Zeichen einer Partitur in solche eines Takts abgeändert worden und zusätzlich in den Anspruch 1 aufgenommen worden, dass wenigstens ein gesamter Takt gleichzeitig auf dem Bildschirm gezeichnet werde, was eine unzulässige Zwischenverallgemeinerung darstelle.

27 Schließlich sei die ursprünglich offenbarte „Rollgeschwindigkeit“ in eine „Taktrollgeschwindigkeit“ abgeändert worden. Zudem mache es ferner einen signifikanten Unterschied, ob die „Rollgeschwindigkeit“ - wie ursprünglich offenbart - gemäß den angezeigten Takten oder aber - wie in der erteilten Fassung des Streitpatents - gemäß dem Musikinhalt des auf dem Bildschirm angezeigten Takts justiert werde.

28 Zur Begründung einer mangelnden Patentfähigkeit beruft sich die Klägerin u. a. auf folgende Unterlagen:

29 K9

Anlagenkonvolut betreffend den Notationseditor „Reflow“, Quellcode veröffentlicht von Sébastien Burgeois

30 K9.1

Internetauszug zur URL https://github.com/Salimlou/reflow vom 16. Juli 2024

31 K9.2

ZIP-Datei mit Software-Quellcode vom 16. Juli 2024

32 K9.3

Video betreffend den Notationseditor „Reflow“

33 K9.4

User Manual “Reflow for iPad”, Version 1.5.1, englische Sprachfassung, Gargant Studios, 27. April 2012

34 K9.5

User Manual “Reflow for Mac“, Version 1.5, englische Sprachfassung, Gargant Studios, 27. April 2012, URL

35 https://www.yumpu.com/en/document/view/11583002/reflow-for-mac-user-manual

36 K10

Anlagenkonvolut betreffend die Tablet-App „The Orchestra“, veröffentlicht von „TouchPress“ in Zusammenarbeit mit der Music Sales Group, Esa-Pekka Salonen und dem Philharmonia Orchestra

37 K10.1

Auszug aus der Online-Enzyklopädie “Wikipedia” vom 26. Oktober 2021, “The Orchestra (app)”

38 K10.2

Auszug aus dem Internetarchiv “WayBack Machine”, Screenshot vom 16. Oktober 2013, URL https://web.archive.org/web/20131016072627/http://www.touchpress.com/titles/orchestra/

39 K10.3

Screenshot aus einem im Internet veröffentlichten Video zu Funktionen der Anwendung „The Orchestra“ mit dem Titel „The Orchestra by TouchPress“, URL https://www.youtube.com/watch?v=JwMfqaxmoMI) angegebenes Veröffentlichungsdatum 8. Januar 2013

40 K10.4

Videodatei zu Anlage K10.3,

41 K10.5

Videodatei zu Funktionen der Anwendung „The Orchestra“

42 K11

Anlagenkonvolut betreffend die Audiobearbeitungssoftware „Logic Pro 9.1.8“

43 K11.1a

Internetauszug zur URL https://support.apple.com/de-de/112574, angegebenes Veröffentlichungsdatum 12. März 2013

44 K11.1b

Internetauszug zur URL https://support.apple.com/kb/DL1601?locale=en_US&viewlocale=en_US, Veröffentlichungsdatum 2+4. Oktober 2012

45 K11.2 Videodatei betreffend die Audiobearbeitungssoftware „Logic Pro 9.1.8“

46 K11.3

Benutzerhandbuch zur Software Logic Pro 9,

47 K11.3a

Deutsche Fassung des Benutzerhandbuchs

48 K11.3b

Englische Fassung des Benutzerhandbuchs

49 K11.3c

Auszug aus dem Internetarchiv “WayBack Machine”, undatierter Screenshot zur Verfügbarkeit der Software zum Download am 23. Januar 2012, URL https://web.archive.org/web/20120123091459/https://help.apple.com/logicpro/mac/9.1.6/en/logicpro/usermanual/Logic%20Pro%209%20User%20Manual%20(en).pdf

50 K12

Anlagenkonvolut zur Softwareplattform der digitalen Audio-Workstation „Pro Tools 8.1“

51 K12.1

Internetauszug der Seite „Avid Knowledge Base Pro Tools HD 8.1 Downloads and Details“ mit dem Hinweis „Last Updated: August 20, 2012“

52 K12.2 Videodatei betreffend die digitale Audio-Workstation „Pro Tools 8.1“

53 K12.3 Pro Tools Reference Guide Version 8.1 (Benutzerhandbuch), Guide Part Number 9329-62052-00 REV B 08/10 mit Copyright-Vermerk 2010

54 K13

Anlagenkonvolut zur Software-Anwendung „Midi Sheet Music“ umfassend die Belege

55 K13.1 Datei „Technical File Information, WINDOWS EXECUTABLE 32bit for Windows 95 and Windows NT“ zur Software-Anwendung mit Internet-Auszug zur URL https://sourceforge.net/projects/Midi

56 sheetmusic/files/ midisheetmusic/2.6/ und Auszug vom 11. Dezember 2013 aus dem Internetarchiv “WayBack Machine” zur Verfügbarkeit der Software zum Download seit dem 13. Juli 2013 , URL https://web.archive.org/web/20131211212424/

57 http://sourceforge.net/projects/midisheetmusic/files/?source=

58 navbar

59 K13.2.1

Datei mit gesamter Partitur zum Download im Format „MIDI“ betreffend das Werk von Antonio Vivaldi „Gloria in D-Dur“, RV 589, „vivaldi_gloriaVLN.mid“

60 K13.2.2

Violinen-Notation „vivaldi_gloriaVLN_vn.mid“)

61 K13.2.3

Piano-Notation „vivaldi_gloriaVLN_pn.mid“

62 K13.2.4

druckbare Partitur des Werkes, URL https://www.8notes.com/scores/17714.asp

63 K14

EP 2 690 618 A1

64 K15

Anlagenkonvolut zur Softwareanwendung „GarageBand“

65 K15.1

Videodatei zur Software-Anwendung vom 4. Juni 2011, URL https://www.youtube.com/watch?v=u0_hN6zrMhg,

66 K15.2

Videodatei zur Software-Anwendung vom 15. Januar 2011, URL https://www.youtube.com/watch?v=7AuZXPG6XOg

67 K16

GB 2473066 A

68 K17

WO 01/50452 A2

69 K18

DE 10 2004 036 356 B3

70 K19.1

Urteil des Commercial Court No. 04 of Barcelona vom 4. September 2024, Aktenzeichen 181/2014, englische Sprachfassung

71 K19.2 deutsche Übersetzung zur K19.1

72 Die Klägerin ist der Auffassung, der Gegenstand des erteilten Patentanspruchs 1 sei nicht neu gegenüber den Entgegenhaltungen K9 bis K15. Er basiere darüber hinaus nicht auf einer erfinderischen Tätigkeit ausgehend von dem Dokument K16 in Verbindung mit der Entgegenhaltung K17. Nämliches gelte für eine Kombination der beiden Entgegenhaltungen K18 und K17. Die nebengeordneten Ansprüche 11, 12 und 13 seien ebenso wie die Unteransprüche 2 bis 10 nicht patentfähig.

73 Die Klägerin beantragt,

74 das europäische Patent 2 919 228 mit Wirkung für das Hoheitsgebiet der Bundesrepublik Deutschland in vollem Umfang für nichtig zu erklären.

75 Die Beklagte beantragt,

76 die Klage abzuweisen sowie hilfsweise die Klage abzuweisen, soweit sie sich gegen das Streitpatent in einer der Fassungen der Hilfsanträge 1, 2a, 2b, 2c, 3 sowie 4 vom 14. April 2025 - in dieser Reihenfolge - richtet.

77 Der Hilfsantrag 1 entspricht der tenorierten Fassung. Wegen des Wortlauts der Hilfsanträge 2a bis 4 wird auf den Schriftsatz der Beklagten vom 14. April 2025 verwiesen.

78 Die Beklagte tritt dem Vorbringen der Klägerin in allen wesentlichen Punkten entgegen und erachtet das Streitpatent zumindest in einer der hilfsweise verteidigten Fassungen für patentfähig. Sie stützt ihren diesbezüglichen Vortrag u. a. auf folgende Unterlagen:

79 CF1 Auszug aus der Online-Enzyklopädie “Wikipedia”, englische Sprachfassung, Stand 7. Februar 2012, zum Stichwort “Sheet music”. URL https://en.wikipedia.org/w/index.php?title

80 =Sheet_music&oldid=594366217

81 CF2 Auszug aus der Online-Enzyklopädie “Wikipedia”, englische Sprachfassung, Stand 9. Januar 2014, zum Stichwort “Scorewriter”. URL https://en.wikipedia.org/w/index.php?title

82 =Scorewriter&oldid=593013372

83 CF3 Auszug aus der Online-Enzyklopädie “Wikipedia”, englische Sprachfassung, Stand 6. März 2014, zum Stichwort “Notensatzprogramm”. URL https://de.wikipedia.org/w/

84 index.php?title=Notensatzprogramm&oldid=128232564

85 CF4

Internetauszug der Seite „Notation Basics in MusicXML/MusicXML4.1 Draft”, URL https://w3c.github.io/

86 musicxml/tutorial/notation-basics/

87 CF5.1 bis

CF5.3

Video-Dateien (mp4), erzeugt von der Beklagten mit der Software “Logic Pro”, Version 9.1.8

88 Die Klägerin ist der Auffassung, dass das Streitpatent auch in den Fassungen der Hilfsanträge nicht rechtsbeständig sei.

89 Der Senat hat den Parteien am 26. Februar 2025 einen qualifizierten Hinweis sowie im Termin am 21. Mai 2025 einen weiteren rechtlichen Hinweis erteilt.

90 Hinsichtlich der weiteren Einzelheiten wird ergänzend auf die zwischen den Parteien gewechselten Schriftsätze sowie auf das Protokoll der mündlichen Verhandlung verwiesen.

## Entscheidungsgründe

91 Die zulässige Klage hat teilweise insoweit Erfolg, als sie sich gegen die erteilte Fassung des Streitpatents richtet. Der Lehre des erteilten Patentanspruchs 1 steht der geltend gemachte Nichtigkeitsgrund der fehlenden Patentfähigkeit in Form fehlender Neuheit entgegen.

92 Die weitergehende Klage war abzuweisen. Denn in der zulässigen Fassung des Hilfsantrags 1 hat das Streitpatent Bestand. Dessen Lehre ist insgesamt neu und beruht auf einer erfinderischen Tätigkeit (Art. II, § 6 Abs. 1, Nr. 1, 3 IntPatÜbkG i. V. m. Art 54, 56 EPÜ). Auf die nachgeordneten Hilfsanträge kam es daher nicht mehr an.

I.

93 1.

Das Streitpatent betrifft gemäß Beschreibungseinleitung eine Anzeige und das Scrollen von Informationen auf einem Anzeigebildschirm, insbesondere ein Verfahren und Systeme zur Anzeige und zum Scrollen von Musik auf einem Anzeigebildschirm (vgl. Streitpatentschrift, Abs. [0001]). Es sei bekannt, dass Musiker manchmal virtuelle Partituren oder elektronische Partituren anstelle der herkömmlichen Papierpartituren verwendeten. Elektronische Partituren hätten u. a. den Vorteil, dass sie eine beträchtliche Menge an Papier und damit auch Platz sparten (vgl. Streitpatentschrift, Abs. [0002]). Eine der größten Herausforderungen bei elektronischen Partituren sei die Frage gewesen, wie man virtuelle Noten für einen Benutzer, der ein Instrument spiele, blättern oder vorwärtsbewegen könne.

94 Die Entwicklung von Software habe zu modernen Telepromptern geführt, die auf Desktop-, Laptop- oder Tablet-Computern funktionierten und es dem Redner ermöglichten, das Tempo und den Fluss seiner Rede zu kontrollieren (vgl. Streitpatentschrift, Abs. [0003]). Es sei auch erwähnenswert, wie spezifisch die musikalische Sprache sei, so dass sie mit keiner auf Worten basierenden Sprache vergleichbar sei (vgl. Streitpatentschrift, Abs. [0004]). Bei Musiknoten basierten die derzeitigen Lösungen für die Anzeige elektronischer Partituren auf einem seitenweisen System. Dies bedeute, dass elektronische Partituren Seite für Seite auf einem Speichermedium gespeichert würden. Das Anzeigegerät blättere dann die Seiten kontinuierlich durch. In der Welt der Musik sei es unvermeidlich, dass die Musiknoten entweder entsprechend dem Echtzeittempo des Benutzers durchgeblättert würden, der gerade spiele, oder entsprechend dem Tempo, das von der Person, die eine Gruppe von Musikern dirigiere, vorgegeben werde, oder sich das Tempo zum Blättern nach dem Tempo richte, das vom Komponisten in der Partitur selbst festgelegt worden sei (vgl. Streitpatentschrift, Abs. [0005]).

95 Das US-Patent US 8 530 735 B2 beschreibe beispielsweise ein Verfahren zur Anzeige von Musik auf einem Bildschirm, bei dem, während ein Teil der Musiknoten eines Liedes auf dem Bildschirm angezeigt werde und der Spieler gleichzeitig sein Instrument spiele, das Tempo des Benutzers beim Spielen des Liedes ermittelt werde. Sobald das Tempo des Benutzers bekannt sei, werde die Zeitspanne berechnet, die der Spieler benötige, um den angezeigten Teil der Musiknoten zu Ende zu spielen. Am Ende dieser Zeitspanne werde der auf dem Bildschirm angezeigte Teil der Musiknoten automatisch durch einen nachfolgenden Teil der Musiknoten ersetzt.

96 Diese Methode habe mehrere Einschränkungen. Die wichtigste sei, dass diese Methode nur in der Lage sei, die Musiknoten entsprechend dem Echtzeit-Tempo des Benutzers durchlaufen zu lassen, der gerade spiele. Insbesondere sei sie nicht in der Lage, sich an das vom Komponisten vorgeschlagene (und durch Anmerkungen in der Partitur dargestellte) Tempo anzupassen. Ein weiterer Nachteil dieser Methode wie auch jeder anderen konventionellen Methode, die auf einer seitenweisen Anzeige beruhe, sei, dass sie nicht in der Lage sei, die in Partituren so häufigen Wiederholungen zu bewältigen. Das bedeute, dass die einzige Möglichkeit für einen Spieler, eine zu wiederholende Gruppe von Noten zu wiederholen, darin bestehe, manuell an den Anfang der zu wiederholenden Gruppe zurückzugehen (vgl. Streitpatentschrift, Abs. [0006] und [0007]).

97 2.

Dem Streitpatent liegt gemäß der Streitpatentschrift die Aufgabe zugrunde, ein Verfahren zum Scrollen von Partituren auf einer Anzeige oder einem Bildschirm bereitzustellen, das die vorstehend genannten Nachteile überwindet (vgl. Streitpatentschrift, Abs. [0010]).

98 Als zuständiger Fachmann ist ein Softwareingenieur anzusehen, der über mehrjährige Erfahrung im Bereich der Entwicklung von Anwendungssoftware im Bereich der elektronischen Darstellung von Notentexten verfügt.

99 3.

Der Patentanspruch 1 in der erteilten Fassung des Streitpatents lässt sich wie folgt gliedern (deutsche Übersetzung in Anlehnung an die deutsche Anspruchsfassung gemäß Patentschrift in Klammern angefügt):

100 1.1

A method for scrolling a musical score on a screen of a device, comprising:

101 (Verfahren zum Rollen durch eine Partitur auf einem Bildschirm eines Geräts, das Folgendes beinhaltet:)

102 1.2

loading a file having a digital score in a piece of memory of said device, said score comprising a plurality of measures;

103 (Laden einer Datei mit einer digitalen Partitur in einem Speicherteil des genannten Geräts, wobei die genannte Partitur mehrere Takte umfasst;)

104 1.3

displaying at least one measure from said score on the screen;

105 (Anzeigen wenigstens eines Takts aus der genannten Partitur auf dem Bildschirm;)

106 1.4.1

scrolling said musical measures as a continuous string of musical signs,

107 (Rollen durch die genannten Musiktakte als kontinuierliche Folge von konsekutiv auf dem Bildschirm gezeichneten musikalischen Zeichen)

108 1.4.2

drawn on the screen in a consecutive way, by continuously showing on the screen additional measures of music while the already scrolled measures disappear from the screen, wherein at least one whole measure is simultaneously drawn on the screen;

109 (durch kontinuierliches Zeigen von zusätzlichen Musiktakten auf dem Bildschirm, während die bereits durchrollten Takte vom Bildschirm verschwinden, wobei wenigstens ein gesamter Takt gleichzeitig auf dem Bildschirm gezeichnet wird;)

110 1.4.3

wherein a measure scrolled on the screen is shown incomplete until the whole measure is completed;

111 (wobei ein auf dem Bildschirm gerollter Takt unvollständig gezeigt wird, bis der gesamte Takt vollständig ist;)

112 1.5.1

adjusting the measures scrolling speed according to the music content of the measures being displayed on the screen, to a tempo and to a number of beats per measure,

113 (Justieren der Taktrollgeschwindigkeit gemäß dem Musikinhalt der auf dem Bildschirm angezeigten Maße, einem Tempo und einer Anzahl von Schlägen pro Takt,)

114 1.5.2.1 wherein said tempo is either a tempo indicated in the digital score or a tempo imposed by a user;

115 (wobei das genannte Tempo entweder ein in der digitalen Partitur angezeigtes Tempo oder ein von einem Benutzer auferlegtes Tempo ist;)

116 1.5.2.2 and said number of beats per measure is either the number of beats per measure imposed by a user who is actually playing or the number of beats per measure indicated in the digital score.

117 (und die genannte Anzahl von Schlägen pro Takt entweder die Anzahl von Schlägen pro Takt wie von einem tatsächlich spielenden Benutzer auferlegt oder die Anzahl von Schlägen pro Takt wie in der digitalen Partitur angezeigt ist,)

118 4.

Der Fachmann versteht den Patentanspruch 1 unter Heranziehung der Beschreibung und den Figuren des Streitpatents wie folgt (Auslegung):

119 Der Anspruch 1 betrifft ein Verfahren zum Scrollen (scrolling) durch einen musikalischen Notentext (musical score), wobei der Notentext auf einem Bildschirm (screen) eines Geräts gerollt wird und der Begriff scrolling von screen und rolling abgeleitet ist (Merkmal 1.1). In der deutschen Übersetzung des Anspruchs 1 gemäß dem Streitpatent, welches in der Verfahrenssprache Englisch erteilt worden ist, wird „musical score“ als „Partitur“ übersetzt. In der Streitpatentschrift ist in Absatz [0027] diesbezüglich ausgeführt, dass der Begriff „score“ allgemein sowohl für die von Dirigenten verwendeten Notenblätter („sheet music“) verwendet wird – also Notenblätter, welche gleichzeitig alle Töne bzw. Tonfolgen der Instrumente von mehreren zusammenspielenden Musikern enthalten - als auch für die Noten eines einzelnen Musikers, der ein einzelnes Instrument spielt. Das in der Musik übliche fachmännische Verständnis einer Partitur betrifft eine Aufzeichnung mehrstimmiger Musik in Notenschrift, bei der die einzelnen Stimmen im Sinne von Tonfolgen (beispielsweise von Violine und Klavier) übereinander angeordnet und oftmals mit senkrecht durchlaufenden Taktstrichen verbunden sind. Eine „Partitur“ stellt dementsprechend einen speziellen musikalischen Notentext für mehrere Stimmen/Tonfolgen und mehrere Musiker dar. Unter einem musikalischen Notentext (musical score) versteht der Fachmann hingegen allgemein in Notenschrift aufgezeichnete Musik. In einem Notentext werden musikalische Symbole verwendet, um die Tonhöhen, Rhythmen oder Akkorde eines Musikstücks anzugeben.

120 Damit ist der englische Begriff „musical score“ im Merkmal 1.1 des Anspruchs 1 als allgemeiner Notentext für eine oder mehrere Stimmen auszulegen. Eine Partitur stellt für den Fachmann einen speziellen Notentext mit mehreren übereinander angeordneten Stimmen/Tonfolgen dar.

121 Gemäß Merkmal 1.2 wird eine Datei mit einem darin befindlichen Notentext in digitaler Form in einen Speicher des Geräts geladen, wobei der Notentext mindestens/wenigstens einen Takt (measure) umfasst. Ein Takt (engl.: measure oder auch bar) ist ein festgelegter zeitlicher Abschnitt in einem Musikstück bzw. ein Muster gleicher Grundschläge/Zählzeiten. Ein Takt, der einen zeitlichen Abschnitt der Musik darstellt, wird auf einem Notenblatt durch zwei vertikale Taktstriche begrenzt und enthält eine feste Anzahl an Schlägen/Beats. Die Länge des Takts, gemessen an der Anzahl der darin enthaltenen Notenwerte, wird durch die Taktart (feste Anzahl an Schlägen/Beats) angegeben, z. B. vier Grundschläge/Zählzeiten im Wert je einer Viertelnote beim 4⁄4-Takt. Zum Inhalt eines Takts zählen sowohl Notenwerte (beispielsweise Viertelnoten oder Achtelnoten) als auch Pausenwerte. Unter einer Datei, wie sie im Merkmal 1.2 genannt wird, versteht der Fachmann allgemein eine Ressource oder Quelle zur Zusammenfassung/Aufbewahrung von Daten, wobei eine Datei mit einem Dateinamen versehen ist. Gemäß der Beschreibung des Streitpatents handelt es sich bei den Daten um digitale Daten zu einem Notentext. Als Datei ist nach der Beschreibung des Streitpatents, die der Auslegung zugrunde zu legen ist, eine Datei in einem digitalen Format gemeint, die einen ganzen Notentext (a whole musical score) enthält (vgl. Streitpatentschrift, Abs. [0032]: […] From now on, the term "file" refers to a file in a digital format comprising a whole musical score).

122 Der Takt oder mehrere Takte (wenigstens ein Takt) aus dem Notentext werden aufeinanderfolgend auf dem Bildschirm des Geräts angezeigt (vgl. Streitpatentschrift, Fig. 1 bis 4 mit dargestellten Takten / Merkmal 1.3).

123 Das beanspruchte Verfahren umfasst das Scrollen (scrolling) durch die genannten Musiktakte als kontinuierliche Folge von aufeinanderfolgenden musikalischen Zeichen (Merkmal 1.4.1 / vgl. Streitpatentschrift, Abs. [0039] und Fig. 1 und 4 bzgl. einem horizontalen Scrollen/Bildlauf, sowie Fig. 2 in Bezug auf ein vertikales Scrollen, wobei der Takt an Position „X=0“ bzw. „Y=0“startet; vgl. auch Abs. [0049] und Fig. 3, in der mehrere Takte dargestellt sind).

124 Die musikalischen Takte werden als eine fortlaufende Kette von musikalischen Zeichen nacheinander auf den Bildschirm gezeichnet/geschrieben (drawn), indem kontinuierlich zusätzliche Takte der Musik auf dem Bildschirm gezeigt werden, während die bereits gescrollten Takte vom Bildschirm verschwinden. Dabei ist mindestens ein ganzer Takt auf dem Bildschirm angezeigt (vgl. Streitpatentschrift, Fig. 1 bis 3 sowie den zugehörigen Text in Abs. [0039] und [0049] / Merkmal 1.4.2). Ein auf dem Bildschirm gescrollter Takt wird unvollständig gezeigt, bis der gesamte Takt vollständig gezeichnet/geschrieben ist (vgl. a. a. O. / Merkmal 1.4.3).

125 Das beanspruchte Verfahren beinhaltet zudem ein Justieren/Anpassen der Geschwindigkeit während des Durchlaufs der Takte (measures scrolling speed) in Abhängigkeit vom musikalischen Inhalt (content) der auf dem Bildschirm angezeigten Takte (measures being displayed) und in Abhängigkeit vom Tempo sowie von der Anzahl der Beats/Schläge (beats) pro Takt (Merkmal 1.5.1). Wie im Rahmen der Auslegung des Merkmals 1.2 ausgeführt, zählen Notenwerte und Pausenwerte zum musikalischen Inhalt (content) der auf dem Bildschirm angezeigten Takte (vgl. Figuren 1 bis 3 sowie die dort innerhalb der Taktstriche dargestellten Noten- und Pausenwerte). Im Hinblick auf Merkmal 1.5.1 geht aus der Beschreibung im Rahmen eines Ausführungsbeispiels hervor, dass die Geschwindigkeit (the speed at which a single measure moves on the screen / v measure ) durch die Zeitspanne (T measure ) bestimmt wird, die ein Takt benötigt, um einen Raum (E) auf dem Bildschirm abzudecken (vgl. Streitpatentschrift, Abs. [0045] bis [0048]).

126 Das im Merkmal 1.5.1 genannte Tempo ist gemäß Merkmal 1.5.2.1 entweder ein im digitalen Notentext (digital score) angegebenes Tempo oder ein von einem Benutzer gewähltes Tempo (vgl. Streitpatentschrift, a. a. O. sowie u. a. Abs. [0011], [0012] bis [0014] und Abs. [0043], in welchem beispielsweise ein Tempo von 60 Schlägen pro Minute und ein Tempo von 120 beats per minute (that is 2 beats per second) genannt werden).

127 Die Anzahl der Beats/Schläge pro Takt (number of beats per measure) ist gemäß Merkmal 1.5.2.2 entweder

128 -

die Anzahl der Schläge pro Takt (z. B. drei Schläge/Beats in Viertelnoten bei einem ¾-Takt), die im digitalen Notentext (digital score) einer Datei (score file) angegeben ist (vgl. Streitpatentschrift, Fig. 1 bis 3 und Abs. [0046]: […] the number of beats per measure ( n_beats measure ) is obtained from the score file […])

129 oder

130 -

die Anzahl der Schläge/Beats pro Takt, die von einem tatsächlich spielenden Benutzer vorgegeben wird (imposed by a user who is actually playing).

131 Letztere Merkmalsalternative bedeutet, dass das Tempo und die Taktart (d. h. die feste Anzahl an Schlägen/Beats pro Takt) aus der gemäß Merkmal 1.2 geladenen Notentext-Datei (score file) nicht berücksichtigt werden (vgl. Streitpatentschrift, Abs. [0047] i. V. m. Abs. [0046]: […] Alternatively, this [number of beats per measure] is imposed by the user. [0047] Then, the tempo applied to the beats is obtained. Alternatively, this is imposed by the user).

II.

132 In der erteilten Fassung vermag die Beklagte das Streitpatent nicht erfolgreich zu verteidigen, da dieser Fassung der geltend gemachte Nichtigkeitsgrund der fehlenden Patentfähigkeit entgegensteht (Art. II § 6 Abs. 1 S. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Buchst. a), Art. 52 bis 57 EPÜ).

133 1.

Der Gegenstand des Anspruchs 1 erweist sich als nicht neu gegenüber dem Stand der Technik (Art. II § 6 Abs. 1 S. 1 Nr. 1 IntPatÜG i. V. m. Art. 138 Abs. 1 Nr. 1, Art. 52, 54 EPÜ).

134 a)

Die vorveröffentlichte und damit als Stand der Technik geltende Anwendung/App „Logic Pro“ gemäß K11 (K11.1a-b, K11.2, K11.3) beschreibt ein Verfahren zum Darstellen eines musikalischen Notentexts auf dem Bildschirm eines Geräts (iPad), wobei ein grüner Rollbalken im zeitlichen Verlauf eines Musikstücks durch einen Notentext „gerollt“, d. h. gescrollt wird (vgl. Benutzerhandbuch K11.3a sowie Screenshots aus einem Video K11.2 zu zwei aufeinanderfolgenden Zeiten). Der dargestellte Notentext wird demnach entsprechend Merkmal 1.1 gescrollt.

135 Bei dem Verfahren wird eine Datei (z. B. mit dem Namen „My Score“) mit einem darin befindlichen Notentext (Score) in digitaler Form in einen Speicher des Geräts geladen, wobei der Notentext einen oder mehrere Takte umfasst (vgl. nachfolgenden Screenshot aus K11.2 zum Öffnen einer Datei mit dem Namen My Score).

136 Ausweislich des Benutzerhandbuchs zu K11/„Logic Pro“ werden Standard-MIDI-Files als Dateien verwendet (vgl. K11.3a, S. 1099, Arbeiten mit Standard-MIDI-Files). Diesbezüglich weiß der Fachmann, dass eine MIDI-Datei nicht nur eine digitale Schnittstelle für Musikinstrumente darstellt und dem Austausch von Steuerinformationen für Musikinstrumente dient, sondern auch ein Kommunikationsprotokoll für die zu übermittelnden Daten in Bezug auf Noten enthalten kann. Die Datei „My Score“ (übersetzt: „Mein Notentext“) beinhaltet auch die zur Darstellung von Notentext notwendigen Informationen (Merkmal 1.2). Dem steht nicht entgegenstehen, dass auf Seite 935 der K11.3a aufgeführt wird, dass „Logic Pro“ bei der Notendarstellung den Inhalt der MIDI-Regionen mithilfe verschiedener benutzerdefinierter Methoden interpretiert.

137 Wie schon im Hinweis an die Parteien ausgeführt, wird auf dem Bildschirm des Geräts (iPad) wenigstens ein Musiktakt aus einem Notentext (score) angezeigt (vgl. vorherige Screenshots sowie auch den nachfolgenden Screenshot aus K11.2, in dem mehrere Takte dargestellt sind / Merkmal 1.3).

138 Das Verfahren beinhaltet zudem einen Bildlauf durch die Musiktakte als kontinuierliche Folge von musikalischen Zeichen, wobei zusätzliche Takte aufeinanderfolgend/konsekutiv auf dem Bildschirm gezeigt werden (vgl. nachfolgende Screenshots aus K11.2 / Merkmale 1.4.1 und 1.4.2).

139 Aus den zu K11 zugehörigen Screenshots (vgl. K11.2) geht auch eindeutig hervor, dass ein auf dem Bildschirm gescrollter Takt unvollständig gezeigt wird, bis der gesamte gescrollte Takt vollständig ist (Merkmal 1.4.3).

140 Wie den zu K11 zugehörigen Screenshots (vgl. K11.2) ebenfalls eindeutig zu entnehmen ist, wird die Geschwindigkeit des Bildlaufs je nach musikalischem Inhalt der einzelnen Takte angepasst. Dabei wird im Zeitabschnitt von 01:28 bis 01:36 der 4. Takt mit Viertelnoten und Viertelpause in der Zeit von 01:28 bis 01:30 durchlaufen.

141 Demnach werden beide Takte in jeweils zwei Sekunden (hier von 01:30 bis 01:32) durchlaufen, obwohl der 4. Takt – mit mehr Inhalt – viel breiter dargestellt wird (etwa dreimal so breit; vgl. rote Pfeile) als der 5. Takt. Die Taktroll-Geschwindigkeit wird also an ein Tempo sowie an die Anzahl der Beats/Schlägen pro Takt angepasst. Folglich ist auch ein Anpassen der Scrollgeschwindigkeit offenbart, welche damit offensichtlich nicht konstant ist (vgl. Duplik, S. 13/14, seitenübergreifender Absatz). Damit ist auch das Merkmal 1.5.1 bereits bekannt.

142 Das Tempo ist ein im digitalen Notentext angezeigtes Tempo (vgl. nachfolgenden ersten Screenshot aus K11.2 / Merkmal 1.5.2.1), kann aber auch durch einen Benutzer über ein Bedienfeld (Button) eingestellt werden (vgl. nachfolgenden zweiten Screenshot mit grüner Tempoanzeige sowie den dritten Screenshot (Bedienfeld/Button) aus K11.2 / Merkmal 1.5.2.2).

143 Damit weist das aus der K11 bekannte Verfahren sämtliche Merkmale des Anspruchs 1 der erteilten Fassung des Streitpatents auf, was der erforderlichen Neuheit entgegensteht.

144 b)

Da die Beklagte in der mündlichen Verhandlung ausdrücklich erklärt hat, die erteilte Fassung des Streitpatents und die Fassung der Hilfsanträge als geschlossenen Anspruchssatz dergestalt zu verteidigen, dass der Senat zur Prüfung des nächsten Hilfsantrags übergehen soll, wenn sich, wie hier, einer der nebengeordneten Ansprüche als nicht patentfähig erweist, hat das Streitpatent somit in der erteilten Fassung insgesamt keinen Bestand (vgl. hierzu auch BGH Urteil vom 13. September 2016 – X ZR 64/14, GRUR 2017, 57 – Datengenerator).

III.

145 In der aus dem Tenor ersichtlichen, zulässigen Fassung des Hilfsantrags 1 vom 14. April 2025 erweist sich das Streitpatent jedoch als rechtsbeständig. Die geltend gemachten Nichtigkeitsgründe der unzulässigen Erweiterung und der fehlenden Patentfähigkeit stehen ihm in dieser Fassung nicht entgegen (Artikel II § 6 Abs. 1 S. 1 Nr. 1 und 2 IntPatÜbkG i. V. m. Art. 138 Abs. 1 Buchst. a und b, Art. 83, 54, 56 EPÜ).

146 1.

Die Fassung des Hilfsantrags 1 ist zulässig.

147 Die Anspruchsfassung weist keine unzulässige Erweiterung auf. Die Lehre seiner nebengeordneten Ansprüche 1 und 10 bis 13 ist sowohl in der Patentschrift als auch in den ursprünglichen Anmeldungsunterlagen offenbart. Dies gilt auch für die auf den Patentanspruch 1 rückbezogenen Unteransprüche 2 bis 10. Die Anspruchsfassung des Hilfsantrags 1 erweitert nicht den Schutzbereich des Patents. Patentanspruch 1 dieser Fassung stellt auch eine Einschränkung gegenüber dem erteilten Patentanspruch 1 dar.

148 a)

Patentanspruch 1 des Hilfsantrags 1 ist nicht unzulässig erweitert. Die Merkmale 1.1, 1.3, 1.5.2.1 und 1.5.2.2 des Anspruchs 1 nach Hilfsantrag 1 sind zugleich Inhalt des ursprünglich eingereichten Anspruchs 1 sowie des Anspruchs 1 in der erteilten Fassung des Streitpatents. Merkmal 1.2 und Merkmal 1.5.1 sind in der Anspruchsfassung nach Hilfsantrag 1 gegenüber der erteilten Fassung wie folgt präzisiert (Änderungen hervorgehoben):

149 1.2 H1

loading a file having a digital score in a piece of memory of said device, said score comprising a plurality of measures, said digital score being in a format which contains the same information as provided by a paper score;

150 1.5.1 H1 adjusting the measures scrolling speed, which is the amount of space covered by at least one measure on the screen divided by the time required for playing that at least one measure, according to the music content of the measures being displayed on the screen, to a tempo and to a number of beats per measure

151 Demnach wird eine Datei mit einem digitalen Notentext in einen Teil des Speichers des Geräts geladen, wobei der Notentext eine Vielzahl von Takten umfasst und in einem Format vorliegt, welches die gleichen Informationen enthält, wie sie von einem (klassischen) Notentext in Papier bereitgestellt werden. Dies ist sowohl in der Streitpatentschrift (vgl. Fig. 1 bis 4 sowie Abs. [0030]) wie auch der ursprünglich eingereichten Anmeldung (vgl. Fig. 1 bis 4 der Offenlegungsschrift sowie Abs. [0028]) offenbart (Merkmal 1.2 H1 ).

152 Das Merkmal 1.5.1 H1 , welches in der Streitpatentschrift (vgl. Abs. [0011]) beschrieben wird und welches das Anpassen der Geschwindigkeit (speed) des Durchlaufs der Takte (measures) gemäß (according) dem musikalischen Inhalt (music content) der auf dem Bildschirm angezeigten Takte beinhaltet, kann der Fachmann der ursprünglichen Beschreibung entnehmen (vgl. u. a. Abs. [0009] ff: […] adjusting the scrolling speed according to the displayed measures, to a tempo and […]; vgl. auch Abs. [0033]: Therefore, it is desirable to adapt the scrolling according to the content of the score, and in particular, to the music displayed on the screen). Der Inhalt des angezeigten Notentexts umfasst hier einen oder mehrere Takte. Das Justieren/Anpassen der Geschwindigkeit des Durchlaufs der Takte (measures) gemäß dem musikalischen Inhalt (music content) der auf dem Bildschirm angezeigten Takte stellt nichts Anderes dar als das Anpassen der Geschwindigkeit gemäß den auf dem Bildschirm angezeigten Takten (vgl. a. a. O. und Fig. 1 bis 4 der Streitpatentschrift, die mit den Figuren der Offenlegungsschrift bzw. den ursprünglich eingereichten Figuren mitsamt zugehöriger Beschreibung übereinstimmen).

153 In den Merkmalen 1.4.1 und 1.4.2 des Anspruchs 1 nach Hilfsantrag 1, die nachfolgend unter Hervorhebung von Änderungen gegenüber der erteilten Fassung wiedergegeben sind,

154 1.4.1

scrolling said score musical measures as a continuous string of musical signs

155 1.4.2

drawn on the screen in a consecutive way, by continuously showing on the screen additional measures of music while the already scrolled measures disappear from the screen, wherein at least one whole measure is simultaneously drawn on the screen,

156 kommt zum Ausdruck, dass das Verfahren ein Scrollen (scrolling) durch die Musiktakte als kontinuierliche Folge von musikalischen Zeichen umfasst (musical measures as a continuous string of musical signs). Die Takte werden als eine fortlaufende Kette von musikalischen Zeichen ( musical measures as a continuous string of musical signs ) nacheinander (in a consecutive way) auf dem Bildschirm (screen) gezeichnet (drawn), indem kontinuierlich zusätzliche Takte der Musik auf dem Bildschirm gezeigt werden, während bereits gescrollte Takte verschwinden und zeitgleich mindestens ein ganzer Takt des Notentexts auf den Bildschirm dargestellt ist. Die Merkmale 1.4.1 und 1.4.2 ergeben sich unmittelbar und eindeutig aus der Streitpatentschrift (vgl. Absatz [0078], letzter Satz, sowie den Figuren 1 bis 3 und dem zugehörigen Text in den Absätzen [0039] und [0049]). In gleicher Weise ist dies auch in den ursprünglichen Figuren 1 bis 3 und der ursprünglichen Beschreibung offenbart (vgl. Offenlegungsschrift, u. a. Abs. [0075], letzter Satz).

157 Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 geht damit weder über den Inhalt der Patentanmeldung in ihrer ursprünglich eingereichten Fassung noch über den Inhalt der erteilten Fassung hinaus, beinhaltet damit keine unzulässige Erweiterung. Er erweitert auch nicht den Schutzbereich des Patents.

158 b)

Dies gilt für die in ihrem Wortlaut gegenüber der erteilten Fassung unverändert gebliebenen, auf den neuen Patentanspruch 1 mittelbar oder unmittelbar rückbezogenen Unteransprüche 2 bis 10 der Fassung des Hilfsantrags 1 in gleicher Weise. Die in ihrem Wortlaut ebenfalls unverändert gebliebenen, nebengeordneten Ansprüche 11 bis 13 des Hilfsantrags 1 sind zulässig und unterscheiden sich von ihrer erteilten Fassung in ihrem Sinngehalt lediglich durch ihren Rückbezug auf den nun - wie dargestellt - veränderten Patentanspruch 1. Dies führt zu einer insgesamt zulässigen Antragsfassung.

159 2.

Der Gegenstand des Anspruchs 1 nach Hilfsantrag 1 ist neu gegenüber dem im Verfahren befindlichen Stand der Technik.

160 a)

Die Anwendung/App „Logic Pro“ gemäß K11 (K11.1a-b, K11.2, K11.3) beschreibt – wie ausgeführt – ein Verfahren zum Darstellen eines musikalischen Notentexts auf einem Bildschirm eines Geräts (iPad), wobei ein Rollbalken im zeitlichen Verlauf eines Musikstücks durch den Notentext geschoben/gerollt wird (vgl. Benutzerhandbuch K11.3a sowie Screenshots aus einem Video K11.2). Der Notentext wird hier ebenfalls entsprechend Merkmal 1.1 gescrollt.

161 Das Merkmal 1.5.1 H1 des Anspruchs 1 nach Hilfsantrag 1, dass die Taktscrollgeschwindigkeit der Platz ist, der von mindestens einem Takt auf dem Bildschirm abgedeckt wird, geteilt durch die Zeit, die für das Spielen mindestens eines Takts benötigt wird, ist jedoch nicht aus K11 bekannt. Es ist vielmehr erkennbar, dass die Geschwindigkeit hier auf Basis der Zeitdauer einzelner Noten – Note für Note – ermittelt und bestimmt wird (vgl. a. a. O. sowie K11.2 und die vorherigen Ausführungen dazu).

162 b)

Auch aus der Druckschrift K14 ist das Merkmal 1.5.1 H1 des Anspruchs 1 gemäß Hilfsantrag 1 nicht bekannt. Diesem Merkmal entsprechend ist die justierte Taktscrollgeschwindigkeit (measures scrolling speed) der Platz, der von mindestens einem angezeigten Takt auf dem Bildschirm abgedeckt wird, geteilt durch die Zeit, die für das Spielen des mindestens einen Takts benötigt wird (Merkmal 1.5.1 H1 fehlt). Druckschrift K14 lehrt vielmehr, dass die Geschwindigkeit auf Basis der Zeitdauer einzelner Noten (time data of each of the notes) bestimmt wird (vgl. Abs. [0044]). Die Bestimmung der Geschwindigkeit des Scrollens des Notentextes geschieht dabei, bevor der Notentext gescrollt wird, also vorab und nicht während der laufenden Anzeige des Notentextes (vgl. a. a. O. und Fig. 5, Schritt S102 bis Schritt 105).

163 c)

Im Handbuch K9.4 wird eine Anwendung/App (K9 / Reflow) beschrieben, die ein Verfahren zum Scrollen durch einen musikalischen Notentext (score) auf einem Bildschirm eines Geräts (iPad) beinhaltet (vgl. u. a. S. 1, 2 und 7 mit dem dort dargestellten und nachfolgend wiedergegebenen Screenshot / Merkmal 1.1). Ein und mehrere Musiktakte aus einem Notentext werden auf dem Bildschirm angezeigt (vgl. K9.4, S. 7 und Screenshot / Merkmal 1.3).

164 Der Fachmann kann der K9.4 zwar entnehmen, dass die dort beschriebene App einen Bildlauf bzw. ein sogenanntes Scrollen durch die genannten Musikakte als kontinuierliche Folge von musikalischen Zeichen umfasst (vgl. a. a. O. / Merkmal 1.4.1). Die musikalischen Takte werden hier als eine fortlaufende Kette von musikalischen Zeichen nacheinander auf dem Bildschirm dargestellt, indem kontinuierlich zusätzliche Takte der Musik auf dem Bildschirm gezeigt werden, während bereits gescrollte Takte vom Bildschirm verschwinden (vgl. Merkmal 1.4.2). Ein auf dem Bildschirm gescrollter Takt wird auch unvollständig gezeigt, bis der gesamte Takt vollständig ist (vgl. K9.4, S. 7 und den zuvor dargestellten Screenshot / Merkmal 1.4.3).

165 Das Merkmal 1.2 bzw. 1.2 H1 ist der K9 bzw. K9.1 bis K9.5 nicht zu entnehmen. In K9.4 wird zwar beschrieben, dass ein Musikinstrument/Tasteninstrument (Keyboard) mittels einer digitalen Schnittstelle für Musikinstrumente (MIDI) an das Gerät (iPad) angeschlossen werden kann, um Noten für einen musikalischen Notentext in die auf dem Gerät (iPad) befindliche Reflow-Anwendung/App einzugeben und dort direkt zu spielen (vgl. S. 8, erster Abs.).Die MIDI-Schnittstelle sorgt dafür, dass Signale des Musikinstruments im Rahmen eines Schnittstellenprotokolls (MIDI-Protokoll) an das Gerät (iPad) und die Reflow-Anwendung/App übertragen werden. Eine MIDI-Schnittstelle und ein Protokoll stellen jedoch noch keine Datei dar (vgl. Ausführungen zur Auslegung des Merkmals 1.2). Dass eine Datei mit einem darin befindlichen Notentext in digitaler Form entsprechend Merkmal 1.2 bzw. 1.2 H1 in einem Speicherteil des Geräts (iPad) geladen wird, wobei der Notentext wenigstens einen Musiktakt – d. h. wenigstens ein Muster gleicher Grundschläge/Zählzeiten – umfasst, ist K9.4 nicht zu entnehmen. Dies gilt in gleicher Weise für K9.5 (und K9.1 bis K9.3 im Zusammenhang mit K9.4). Dem von der Klägerin zu K9.2 gezeigten Screenshot (vgl. Klageschrift S. 31) ist zwar zu entnehmen, dass ein Programm-Quellcode REMidiFile.cpp in der Programmiersprache C++ ein Menü zum Öffnen (Open) einer Datei vorsieht. Weitere Details sind dem Screenshot jedoch nicht zu entnehmen.

166 Dass entsprechend Merkmal 1.5.1 H1 des Anspruchs 1 gemäß Hilfsantrag 1 die Taktscrollgeschwindigkeit (measures scrolling speed) der Platz ist, der von mindestens einem Takt auf dem Bildschirm abgedeckt wird, geteilt durch die Zeit, die für das Spielen mindestens eines Takts benötigt wird, kann der Fachmann der K9.4 /K9 ebenfalls nicht entnehmen. Auch K9.5 bzw. K9.1 bis K9.3 ist dies nicht zu entnehmen. Im Gegensatz zu Merkmal 1.5.1 H1 wird die Geschwindigkeit hier auf Basis der Zeitdauer einzelner Noten – Note für Note – ermittelt und bestimmt (vgl. Screenshots aus K9.3 zu aufeinanderfolgenden Zeiten).

167 d)

Auch der Entgegenhaltung K10 ist das Merkmal 1.5.1 H1 des Anspruchs 1 gemäß Hilfsantrag 1 bezüglich der Taktscrollgeschwindigkeit nicht zu entnehmen. In dem zugehörigen Wikipedia-Artikel K10.1 ist von einem Notentext (score) die Rede, der automatisch synchronisiert angezeigt wird, wobei dies Note für Note geschieht (graphical note-by-note visualization; vgl. auch Screenshots aus K10.5), aus denen eine Bestimmung und Einstellung der Taktscrollgeschwindigkeit in Abhängigkeit von einzelnen Noten hervorgeht, im Gegensatz zu Merkmal 1.5.1 H1 .

168 e)

Die weiteren im Verfahren befindlichen Druckschriften geben ebenfalls keinen Hinweis auf das Merkmal 1.5.1 H1 . Dergleichen ist auch nicht von der Klägerin geltend gemacht worden.

169 So entnimmt der Fachmann der Software/Anwendung K15 (GarageBand) ein Verfahren zum Editieren, Abspielen und Darstellen von musikalischem Notentext (sheet music), bei dem eine Datei mit einem darin befindlichen digitalen Notentext in einen Speicher eines Geräts (iPad oder Mac) geladen wird, wobei der Notentext mehrere Takte umfasst (vgl. u. a. Screenshot gemäß Anlage K15.1 / Merkmal 1.2).

170 Die Geschwindigkeit des Durchlaufs der Take wird an den musikalischen Inhalt angepasst – einen Hinweis darauf, dass die Taktscrollgeschwindigkeit entsprechend Merkmal 1.5.1 H1 der Platz ist, der von mindestens einem Takt auf dem Bildschirm abgedeckt wird, geteilt durch die Zeit, die für das Spielen mindestens eines Takts benötigt wird, gibt es jedoch nicht in K15.

171 Druckschrift K16 offenbart, dass ein Anzeigeprogramm (display application 164) Befehle zur Tempoanpassung verarbeitet, die von einem Benutzer über die Benutzereingabeschnittstelle (user input interface 158) empfangen werden (vgl. u. a. S. 15, Z. 14-20). Ein Hinweis auf eine Anpassung der Taktscollgeschwindigkeit gemäß Merkmal 1.5.1 H1 findet sich jedoch auch nicht in Druckschrift K16.

172 Druckschrift K17 lehrt lediglich eine seitenweise Darstellung von Takten und ein Umblättern (page turn) von Seiten (vgl. u. a. Fig. 1 und S. 9, Z. 33-35). Ein Scrollen oder Rollen sowie ein Anpassen/Justieren der Taktrollgeschwindigkeit gemäß dem Musikinhalt des auf dem Bildschirm angezeigten Takts, einem Tempo und einer Anzahl von Schlägen pro Takt entsprechend Merkmal 1.5.1 H1 werden jedoch nicht beschrieben.

173 In Druckschrift K18 wird lediglich auf eine aktivierbare dynamische Geschwindigkeitsregelung hingewiesen, ohne jedoch Einzelheiten zu nennen, die auf das Merkmal 1.5.1 H1 hinweisen könnten (vgl. u. a. Abs. 18, letzter Satz).

174 Im Übrigen gibt das von der Klägerin als Anlage K19 beigefügte Urteil aus einem parallelen Nichtigkeitsverfahren in Spanien ebenfalls keinen Hinweis auf einen Stand der Technik, der das Merkmal 1.5.1 H1 offenbart.

175 3.

Der Gegenstand des Patentanspruchs 1 nach Hilfsantrag 1 beruht auch auf einer erfinderischen Tätigkeit.

176 a)

Wie ausgeführt, gibt es in keiner der im Verfahren befindlichen Entgegenhaltungen einen Hinweis auf das Merkmal 1.5.1 H1 . Auch eine Zusammenschau der im Verfahren befindlichen Entgegenhaltungen führt damit nicht zum Gegenstand des Anspruchs 1 nach Hilfsantrag 1. Das Merkmal 1.5.1 H1 des Anspruchs 1 gemäß Hilfsantrag 1, dass die Taktscrollgeschwindigkeit der Platz ist, der von mindestens einem Takt auf dem Bildschirm abgedeckt wird, geteilt durch die Zeit, die für das Spielen mindestens eines Takts benötigt wird, ergibt sich dabei für den Fachmann auch nicht in naheliegender Weise unter Hinzunahme seines Fachwissens.

177 b)

Die vorstehenden Ausführungen gelten in gleicher Weise in Bezug auf die Patentfähigkeit der Gegenstände der nebengeordneten Ansprüche 11 bis 13 nach Hilfsantrag 1, die unter anderem jeweils auf den Anspruch 1 rückbezogen sind.

178 c)

Die auf den Anspruch 1 rückbezogenen Unteransprüche in der Fassung des Hilfsantrags 1 erfüllen ebenfalls die an sie hinsichtlich ihrer Schutzfähigkeit zu stellenden Anforderungen.

179 4.

Da sich das Streitpatent in der zulässig verteidigten Fassung nach Hilfsantrag 1 somit als rechtsbeständig erweist, war die Klage insoweit abzuweisen.

5.

IV.

180 Die Kostenentscheidung beruht auf § 84 Abs. 2 Satz 1 und 2 PatG, § 92 Abs. 1 Satz 1 1. Alt. ZPO, der Ausspruch über die vorläufige Vollstreckbarkeit auf § 99 Abs. 1 PatG i. V. m. § 709 ZPO.
