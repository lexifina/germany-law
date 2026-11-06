# Reproducing this repository

Input: Zenodo record 15754093, the CSV "Datensatz" file of the Bundespatentgericht corpus (snapshot 2025-07-08); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py bpatg <csv> <empty folder> --today 2026-11-06 --snapshot 2025-07-08 --record 15754093
```

Gives 31,203 decision commits and one documentation commit.
