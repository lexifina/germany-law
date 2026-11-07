# Reproducing this repository

Input: the CC0 "Corpus der Entscheidungen des Bundesgerichtshofs" (CE-BGH, Zenodo record 15153244, decisions from 2000) and "Entscheidungen des Bundesgerichtshofs in Strafsachen aus dem 20. Jahrhundert" (BGH-Strafsachen-20Jhd, Zenodo record 4540377, CC0, the criminal senates 1950-1999), both by Seán Fobbe: the CSV "Datensatz" file(s) (snapshot 2025-04-07); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py bgh <csv>[,<csv>] <empty folder> --today 2026-11-07 --snapshot 2025-04-07 --record 15153244
```

Gives 113,604 decision commits and one documentation commit.
