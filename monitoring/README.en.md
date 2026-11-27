<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Deutsch](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Germany only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-27 07:01 UTC, Gesetze im Internet (Federal Ministry of Justice): 7050 addresses read; 0 added, 9 changed, 0 removed; changes found; 13 not published, 0 of them with no reason. Flags: `verify-differ`, `audit-disagrees`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Gesetze im Internet (Federal Ministry of Justice)](https://www.gesetze-im-internet.de) | `bund/gesetze/`, `grundgesetz/` | daily | 2026-11-27 07:01 UTC | changes found | watched |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-27 05:01](checks/2026-11.md#de-gii-20261127t050105z) | gii | 7050 | 0 | 9 | 0 | 13 (0) | changes found `verify-differ` `audit-disagrees` | [1](https://github.com/lexifina/germany-law/compare/d14796a08f2b...3572f358087b) |
| [2026-11-26 05:01](checks/2026-11.md#de-gii-20261126t050106z) | gii | 7066 | 1 | 21 | 0 | 14 (0) | changes found `audit-disagrees` | [5](https://github.com/lexifina/germany-law/compare/b90679ca67fc...c6362a0a9f63) |
| [2026-11-25 05:01](checks/2026-11.md#de-gii-20261125t050103z) | gii | 7072 | 3 | 28 | 3 | 14 (0) | changes found `verify-differ` | [3](https://github.com/lexifina/germany-law/compare/5dabc17ee120...b6a371018158) |
| [2026-11-24 05:08](checks/2026-11.md#de-gii-20261124t050802z) | gii | 7054 | 1 | 12 | 1 | 8 (0) | changes found `audit-disagrees` | [4](https://github.com/lexifina/germany-law/compare/42644a9080d2...b54399c9f0a8) |
| [2026-11-23 21:34](checks/2026-11.md#de-gii-20261123t213453z) | gii | 7038 | 0 | 0 | 0 | 4 (0) | no change `verify-differ` `audit-disagrees` | — |
| [2026-11-23 17:42](checks/2026-11.md#de-gii-20261123t174212z) | gii | 7077 | 0 | 0 | 0 | 8 (0) | changes found `audit-disagrees` | [4](https://github.com/lexifina/germany-law/compare/a629f1a377f6...860263ebb5fe) |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
