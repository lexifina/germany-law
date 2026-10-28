"""German law as it read on a given day, from this repository's tags.

    python tools/stand_am.py 1990-10-03              every article of the Grundgesetz in force that day
    python tools/stand_am.py 1993-06-01 16 16a       only these articles
    python tools/stand_am.py 2021-07-01 --gesetz bgb a federal act as Gesetze im Internet published it that day

The Grundgesetz is read from the in-force tags (in-kraft/YYYY-MM-DD, one for each day a change took effect). Federal acts
are read from the publication tags (stand/YYYY-MM-DD, one for each day Gesetze im Internet changed), from 10 June 2019 on.
Run it from the repository. It reads git's history and changes nothing.
"""
import re
import subprocess
import sys


def git(*args: str) -> str:
    return subprocess.run(['git', *args], capture_output=True, text=True, encoding='utf-8', check=True).stdout


def latest(prefix: str, day: str) -> str | None:
    tags = sorted(t for t in git('tag', '--list', f'{prefix}/*').split() if t[len(prefix) + 1:] <= day)
    return tags[-1] if tags else None


def main() -> None:
    sys.stdout.reconfigure(encoding='utf-8')
    args = sys.argv[1:]
    if not args or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', args[0]):
        sys.exit(__doc__)
    day = args[0]
    if len(args) >= 3 and args[1] == '--gesetz':
        tag = latest('stand', day)
        if not tag:
            sys.exit('The federal acts are recorded from 10 June 2019.')
        slug = args[2].lower()
        index = git('show', f'{tag}:{slug}/index.md')
        print(f'Stand: {day} (Gesetze im Internet, {tag[len("stand/"):]})\n')
        print(index)
        for name in re.findall(r'\]\(([^)]+\.md)\)', index):   # the norms, in the act's own order
            print(git('show', f'{tag}:{slug}/{name}'))
        return
    tag = latest('in-kraft', day)
    if not tag:
        sys.exit(f'The Grundgesetz was not yet in force on {day}. It took effect on 24 May 1949.')
    files = [f for f in git('ls-tree', '--name-only', f'{tag}:grundgesetz/artikel').split() if f.endswith('.md') and f != 'README.md']
    wanted = args[1:]
    if wanted:
        names = {re.sub(r'^0+', '', f[:-3]) or f[:-3]: f for f in files}
        missing = [w for w in wanted if w.lower() not in names]
        if missing:
            print(f'Not in force on {day}: Article {", ".join(missing)}', file=sys.stderr)
        files = [names[w.lower()] for w in wanted if w.lower() in names]
    print(f'Stand: {day} (last change in force {tag[len("in-kraft/"):]})\n')
    for f in files:
        print(git('show', f'{tag}:grundgesetz/artikel/{f}'))


if __name__ == '__main__':
    main()
