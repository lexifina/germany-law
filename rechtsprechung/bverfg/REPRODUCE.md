# Reproducing this repository

Input: Zenodo record 16932395, the CSV "Datensatz" file of the Bundesverfassungsgericht corpus (snapshot 2025-09-22); lexifina/germany-law
`main` for the overlay (`tools/de_index.py`).

```
python tools/de_index.py <germany-law clone>
python tools/build.py bverfg <csv> <empty folder> --today 2026-11-06 --snapshot 2025-09-22 --record 16932395
```

Gives 9,301 decision commits and one documentation commit.
