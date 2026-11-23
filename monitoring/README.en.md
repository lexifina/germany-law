<!-- lawwatch: written from data/checks by the check trail; edit the records, not this page -->

# Monitoring: what is read and what came of it

[Deutsch](README.md)

How global-law monitors every country: [global-law monitoring/](https://github.com/lexifina/global-law/tree/main/monitoring). This page is the same for Germany only: every time an official source is read, when, and what came of it (acts added, changed and removed). The machine-readable form is [data/checks/](../data/checks/) (JSON Lines, schema `lexifina-check/1`), in `git log` as `Kind: check` commits, and month by month in [checks/](checks/).

**Last check:** 2026-11-23 20:33 UTC, Gesetze im Internet (Federal Ministry of Justice): 7077 addresses read; 0 added, 0 changed, 0 removed; changes found; 8 not published, 0 of them with no reason. Flags: `audit-disagrees`.

## Sources

| Source | Folders | How often | Last successful check | Last result | State |
| --- | --- | --- | --- | --- | --- |
| [Gesetze im Internet (Federal Ministry of Justice)](https://www.gesetze-im-internet.de) | `bund/gesetze/`, `grundgesetz/` | daily | 2026-11-23 20:33 UTC | changes found | watched |

## The last 30 days

| Started (UTC) | Source | Read | Added | Changed | Removed | Not published (no reason) | Result | Commits |
| --- | --- | ---: | ---: | ---: | ---: | ---: | --- | ---: |
| [2026-11-23 17:42](checks/2026-11.md#de-gii-20261123t174212z) | gii | 7077 | 0 | 0 | 0 | 8 (0) | changes found `audit-disagrees` | [4](https://github.com/lexifina/germany-law/compare/a629f1a377f6...860263ebb5fe) |

## Check it yourself

```
python tools/checktrail.py                      # the latest check of every source
python tools/checktrail.py --day 2026-11-23     # every check of a day
python tools/checktrail.py --act <id>           # when an act was seen and published
git log --grep='^Kind: check' --format='%ci %s'  # the checks in the history
```

Only the official publication has legal force; the texts here are copies for reading and searching.
