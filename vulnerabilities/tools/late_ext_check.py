"""Hand-check helper for the empty periods that survived the rebuttal (next to build_vulns.py; writes late_ext_check.json
there): the word-diff lines of the extending commit that hold the old or the new date (German or numeric format); whether a
line of the old text, with the new date in place of the old, is a line of the new text (the old date replaced in an
otherwise unchanged line: "same"); and the extending act's own date, where the record names an act ("G v. 22.12.2025 ...").

    python -X utf8 late_ext_check.py
"""
import json, os, re, subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.join(HERE, "gl", "vulnerabilities", "scripts")
G = os.path.join(SCR, "sources", "corpus", "germany-law.git")
RUN = os.path.join(SCR, "findings", "run")
PIN = json.load(open(os.path.join(SCR, "pins.json"), encoding="utf-8"))["corpora"][0]["sha"]
MON = "Januar Februar März April Mai Juni Juli August September Oktober November Dezember".split()


def forms(d):
    y, m, dd = d.split("-"); m, dd = int(m), int(dd)
    return [f"{dd}. {MON[m-1]} {y}", f"{dd}.{m}.{y}", f"{dd}. {m}. {y}", f"{dd:02d}.{m:02d}.{y}", d]


def git(*a):
    return subprocess.run(["git", "-C", G, *a], capture_output=True).stdout.decode("utf-8", "replace")


def lines(t):
    return [s.strip() for s in t.split("\n") if s.strip()]  # one paragraph or item per line ("31. Dezember" has a full stop)


def same_line(commit, path, old, new):
    a = git("show", f"{commit}^:{path}"); b = git("show", f"{commit}:{path}")
    lb = set(lines(b))
    for s in lines(a):
        for fo, fn in zip(forms(old), forms(new)):
            if fo in s and s.replace(fo, fn) in lb:
                return "same"
    return "partly" if any(f in b for f in forms(new)) and not any(f in b for f in forms(old)) else "no"


ACT = re.compile(r"[GV] v\. (\d+)\.(\d+)\.(\d{4})")
seen, out = set(), []
for x in map(json.loads, open(os.path.join(RUN, "late_extension_triage.jsonl"), encoding="utf-8")):
    if not x.get("rebut", {}).get("survives"):
        continue
    r = x["row"]; k = (r["path"], r["old_until"], r["new_until"], r["law"], r["extended_in_force"])
    if k in seen:
        continue
    seen.add(k)
    log = [l.split("\t") for l in git("log", "--format=%h\t%an\t%(trailers:key=In-Kraft,valueonly,separator=)\t"
                                      "%(trailers:key=In-Kraft-laut-Fussnote,valueonly,separator=)", PIN, "--", r["path"]).splitlines()]
    c = [l for l in log if l[1] == r["law"] and (l[3] or l[2]).strip() == r["extended_in_force"]]
    hits = []
    for cc in c:
        for line in git("diff", "-U0", "--word-diff", f"{cc[0]}^", cc[0], "--", r["path"]).splitlines():
            if any(f in line for f in forms(r["old_until"]) + forms(r["new_until"])) and ("{+" in line or "[-" in line):
                hits.append(line.strip()[:400])
    m = ACT.match(r["law"])
    out.append({"path": r["path"], "old": r["old_until"], "new": r["new_until"], "law": r["law"], "in_force": r["extended_in_force"],
                "gap": r["gap_days"], "commit": c[0][0] if c else "", "hits": hits[:3],
                "same_line": same_line(c[0][0], r["path"], r["old_until"], r["new_until"]) if c else "?",
                "act_date": f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}" if m else ""})
json.dump(out, open(os.path.join(HERE, "late_ext_check.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for o in out:
    late = "act made after the old end" if o["act_date"] and o["act_date"] > o["old"] else ("act made before the old end" if o["act_date"] else "no act named")
    print(f"## {o['path']} {o['old']} -> {o['new']} by {o['law']}, dated {o['in_force']} ({o['gap']} d); {o['same_line']}; {late}")
print(Counter((o["same_line"], "act" if o["act_date"] else "no act") for o in out))
