# Reproducing this repository

Input: the CC0 "Corpus der Entscheidungen" CSV on Zenodo (record 14622341): the CSV "Datensatz" file(s) (snapshot 2025-01-14); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py bfh <csv>[,<csv>] <empty folder> --today 2026-11-07 --snapshot 2025-01-14 --record 14622341
```

Gives 10,885 decision commits and one documentation commit.
