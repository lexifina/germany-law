# Fassungen vor 2019 / Versions before 2019

**Deutsch.** Dieser Ordner enthält ältere Fassungen von Bundesgesetzen, die vor dem ersten Stand von Gesetze im
Internet in diesem Archiv (10. Juni 2019, `bund/gesetze/`) galten. Sie sind aus dem Bundesgesetzblatt rekonstruiert:
Ausgangspunkt ist die letzte Bekanntmachung der Neufassung eines Gesetzes; danach wird jedes Änderungsgesetz, das der
Fundstellennachweis A nennt, mit seinen Änderungsbefehlen auf den vorigen Stand angewandt, in der Reihenfolge des
Inkrafttretens. Ein Commit je Änderungsgesetz, datiert auf den Tag des Inkrafttretens (vor 1970: 1970-01-01, das
echte Datum steht im Betreff und in `In-Kraft:`), Autor ist das Änderungsgesetz.

Geschrieben wird eine Vorschrift nur, wenn ihre so rekonstruierte letzte Fassung Wort für Wort dem amtlichen Text von
Gesetze im Internet vom 10. Juni 2019 entspricht. Der Text der Bundesgesetzblätter stammt aus der Textschicht der
PDF-Ausgaben bei OffeneGesetze (Abbild des amtlichen Bundesgesetzblatts); ältere Ausgaben sind Scans, ihr Text ist
OCR. Wörter, die sich vom Text 2019 nur durch Lesefehler unterscheiden (verwechselte Zeichen, Trennung, Abstände,
Satzzeichen im Wort) und die bis 2019 unverändert blieben, sind in der amtlichen Fassung von 2019 geschrieben; jeder
Commit nennt diese Korrekturen. Andere Abweichungen werden nie ersetzt: die Vorschrift wird dann zurückgehalten (im
ersten Commit des Gesetzes unter `Zurückgehalten:` genannt). Maßgeblich ist das amtliche Bundesgesetzblatt.

Korrektur (18. November 2026): Sieben Commits tragen ein zu spätes Datum (2019-08-01 bis 2025-01-01). Ihre Änderungsgesetze traten in Teilen an verschiedenen Tagen in Kraft, der Commit nahm den spätesten Tag für das ganze Gesetz. Der Text ist richtig, nur das Datum nicht. Die richtigen Tage je Artikel und Nummer stehen in [`data/date-corrections.json`](data/date-corrections.json); die Geschichte wird nicht umgeschrieben.

**English.** This folder holds older versions of federal acts, in force before this record's first Gesetze im Internet
snapshot (10 June 2019, `bund/gesetze/`). They are rebuilt from the Federal Law Gazette: starting from an act's last
promulgated consolidated text (Neufassung), every amending act listed in the Fundstellennachweis A is applied to the
previous state through its amendment instructions, in order of entry into force. One commit per amending act, dated
by the day it took effect (before 1970: 1970-01-01, the real date in the subject and in `In-Kraft:`), authored by the
amending act.

A provision is written only when its rebuilt last version equals the official Gesetze im Internet text of 10 June 2019
word for word. The gazette text is the text layer of the PDF issues at OffeneGesetze (a copy of the official gazette);
older issues are scans and their text is OCR. Words that differ from the 2019 text only as misreadings do (confused
characters, hyphenation, spacing, marks inside a word) and that stood unchanged until 2019 are written in the official
2019 wording; each commit lists these corrections. Other differences are never replaced: the provision is held back
instead (listed under `Zurückgehalten:` in the act's first commit). The official Federal Law Gazette is authoritative.

Correction (18 November 2026): seven commits carry a date that is too late (2019-08-01 to 2025-01-01). Their amending acts took effect in parts on different days, and the commit took the latest day for the whole act. The text is right; only the date is not. The right days per Artikel and Nummer are in [`data/date-corrections.json`](data/date-corrections.json); the history is not rewritten.
