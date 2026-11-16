# Tools

The scripts behind this Germany-only run of global-law's vulnerability detectors. They run inside a copy of
[global-law/vulnerabilities/scripts](https://github.com/lexifina/global-law/tree/main/vulnerabilities/scripts) (Python 3.11+,
`pip install duckdb pyarrow`), with a bare clone of this repository at `sources/corpus/germany-law.git`, a blobless bare
clone of global-law at `sources/global-law.git`, and a `pins.json` that names only germany-law, its commit, its language
(`de`) and its code (`DE`). `build_vulns.py`, `flags_chart.py`, `late_ext_select.py`, `late_ext_rebut.py`,
`late_ext_check.py` and `config.json` sit three folders up, next to the copy of global-law (`gl/vulnerabilities/scripts/`).

| Script | What it does |
| --- | --- |
| `run.sh` | Indexes the history and texts, adds this repository's history rows, and runs the detectors, the two Germany-only ones last (`bash run.sh <shards>`) |
| `add_root.py` | Builds the history rows from this repository's own commits, so the history detectors read every change; changed for this repository (below) |
| `owi_de.py` | global-law's Germany-only detector for fines and criminal provisions whose underlying rule is missing ("Ordnungswidrig handelt, wer … entgegen § X Absatz Y"); changed for this run (below). global-law's other Germany-only detector, `subref_de.py` (references to missing paragraphs), ran unchanged |
| `run_triage.sh` | The model review: the 40 strongest flags per category, the 40 strongest lapsed time limits in law texts, and the empty periods |
| `late_ext_select.py` | Chooses the empty periods for global-law's review of that category: those whose old and new dates open the same sentence (here 230, all of them reviewed), and, below 40, the shortest of the rest |
| `late_ext_rebut.py` | Adds the second, arguing-against pass to the empty-period review, as `triage.py` does for the other categories |
| `late_ext_check.py` | The hand check of the empty periods that survived: whether the change replaced the old date in an otherwise unchanged line, and the date of the extending act, where the record names one, against the end of the period |
| `build_vulns.py` | Builds `data/flags.csv`, `data/reviewed.csv` and `data/by_category.csv` from the findings and the model review; here with the two Germany-only categories |
| `flags_chart.py` | Draws the chart at the top of the READMEs, in German and English, light and dark |
| `config.json` | The repository, the German category names, the files and folders that are not law (with `index.md`, the tables of contents), and the chart's labels |
| `patch_detectors.py` | Fixes blind spots found in runs on several country repositories in the copy of global-law's scripts (`python -X utf8 patch_detectors.py <scripts dir>`; a fix already in place is skipped) |
| `patch_de.py` | The German-language fixes found by the Austria run: "Jänner", "bis zum Ablauf des", another act named after the section ("§ 60 Absatz 1 … des Lebensmittel- und Futtermittelgesetzbuches"), "§§ 70 bis 75" as a range, "S. 28" as a page, the schilling |
| `patch_detectors_vi.py`, `patch_es.py`, `patch_ca.py`, `patch_en.py`, `patch_en_et.py` | The same for Vietnamese, Spanish, Catalan and English text (found by other runs); they change nothing in German text, but `redo.py` runs them on every repository |
| `patch_co.py`, `patch_sv.py`, `patch_pt.py` | The same for Colombian and Salvadoran Spanish and Brazilian Portuguese; written after this run and not applied here |
| `apply_patches.py` | Runs the patches above once each, in a fixed order, and records them in the scripts folder (`.kit_patches.json`) |
| `map_moved.py` | For a repository that moved its act folders (`data/paths.json`), rewrites the paths in the history table to each act's folder since the move; this repository has not moved its folders, so it does nothing here |
| `redo.py` | Runs the patches, then again only the scans and detectors the fixes change, the model review of lapsed time limits, references to deleted provisions and empty periods, and the build (`python -X utf8 redo.py <run folder> [--keep-reviews] [--full]`; `--keep-reviews` keeps every review already made and reviews only new strong flags; `--full` runs every step again through `run.sh`, sends every category to the model and keeps every review already made; `EMBED_FONTS` names the script that embeds the chart's fonts) |

The model review needs `LLM_BASE_URL`, `LLM_API_KEY`, `LLM_MODEL` and `LLM_AUTH` set for an OpenAI-compatible Responses API.
`run_triage.sh` was given `^(data|tools)/|(^|/)index\.md$|^grundgesetz/(gesetze|KORREKTUREN)` as the files that are not
law; the 40 strongest lapsed time limits in law texts turned out to be the 40 strongest of all.

The detectors carried `patch_detectors.py` through its sixteenth round and `patch_detectors_vi.py`, `patch_es.py`,
`patch_ca.py`, `patch_en.py`, `patch_de.py` and `patch_en_et.py` when they were run. The seventeenth round of
`patch_detectors.py` (found by the Colombia run: "francos suizos", and the sucre and the zaire in lower case only) and
`patch_co.py`, `patch_sv.py` and `patch_pt.py` came later and were not applied; the seventeenth round would drop the two
"100 Sucres" in the conversion tables of UmstBauSparkV and UmstGeldInstV, which German writes with a capital letter.
Changes made for this repository:

- `add_root.py`: germany-law dates its commits in the trailer `In-Kraft:` (and, where the act's footnotes give an earlier
  day, `In-Kraft-laut-Fussnote:`), not `In-force:`, so the first run found no history rows at all (it was stopped
  there: the text and reference scans join on those rows). The date is now `In-force:`, else `In-Kraft-laut-Fussnote:`, else
  `In-Kraft:`, and a commit with any of them counts; all 3,304 dated commits count as law (none has a `Kind:` trailer).
  Everything from the text scan onward was run again.
- `owi_de.py`: it wrote `findings/<run>/dead_fine.jsonl`, the file `detectors/dead_fine.py` writes, so whichever ran last
  replaced the other. It now writes `dead_fine_de.jsonl`, and `build_vulns.py` reads it as its own category ("Fines citing a
  missing provision"), as it reads `missing_paragraph.jsonl` from `subref_de.py`; `config.json` names both in German.
- `detectors/currency_scan.py` (in the copy of global-law's scripts): `patch_de.py` added "S" after an amount as the
  schilling for every German-language repository. In German law it is a page ("506 S."), a stereo descriptor
  ("(5R,6S)"), "H2S" or "S-Bahnen": 54 false flags. In `pat_for` the "S" form is now left out unless `pins.json` gives
  the code `AT`:

  ```python
  extra = EXTRA_CURRENCY.get((c.get("language") or "").lower(), "")
  if c.get("code") != "AT":  # "S" after an amount is the schilling only in Austria
      extra = extra.replace(r"|(?-i:S)\b(?![.,]?\s*\d)", "")
  cur = cur[:-1] + extra + ")"
  ```

  The currency scan was run again: dead currencies went from 1,954 to 1,900.
- `run.sh` runs `owi_de.py` and `subref_de.py` after the other detectors. `redo.py` does not run them; the patches do not
  change what they read.

Not changed, and stated in the READMEs: `owi_de.py` and `subref_de.py` read another act named at the end of a list
("nach § 324, 326, 330 oder 330a des Strafgesetzbuches") or with a name of several words ("des Lebensmittel- und
Futtermittelgesetzbuches", "der Makler- und Bauträgerverordnung") as the citing act, and `subref_de.py` takes a lettered item
that continues an offence list ("q) Absatz 3 Nummer 3") as a paragraph of the citing section; `triage.py` has no evidence
for these two categories, so the model does not review them; and the search for dates of promulgation reads `Published:`,
`Enacted:` and the like, not the Grundgesetz's `Verkuendet:`.
