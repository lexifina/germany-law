# Reproducing this repository

Input: the CC0 "Corpus der Entscheidungen" CSV on Zenodo (record 4006645): the CSV "Datensatz" file(s) (snapshot 2020-08-28); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py bag <csv>[,<csv>] <empty folder> --today 2026-11-07 --snapshot 2020-08-28 --record 4006645
```

Gives 5,624 decision commits and one documentation commit.
