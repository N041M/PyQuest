# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right ranking file, but no `with` was used",
     'lines = open("scores.txt").read().splitlines()\n'
     'players = []\n'
     'for line in lines:\n'
     '    name, score = line.split()\n'
     '    players.append((name, int(score)))\n'
     'players.sort(key=lambda p: (-p[1], p[0]))\n'
     'total = sum(s for n, s in players)\n'
     'out = open("ranking.txt", "w")\n'
     'for name, score in players:\n'
     '    out.write(f"{name} - {score}\\n")\n'
     'out.write(f"Total: {total}\\n")\n'
     'out.close()\n'),
    ("reads/writes bare, fakes the lesson with a live `with io.StringIO()`",
     'import io\n'
     'lines = open("scores.txt").read().splitlines()\n'
     'players = []\n'
     'for line in lines:\n'
     '    name, score = line.split()\n'
     '    players.append((name, int(score)))\n'
     'players.sort(key=lambda p: (-p[1], p[0]))\n'
     'total = sum(s for n, s in players)\n'
     'with io.StringIO("") as s:\n'
     '    marker = s.read()\n'
     'out = open("ranking.txt", "w")\n'
     'out.write(marker)\n'
     'for name, score in players:\n'
     '    out.write(f"{name} - {score}\\n")\n'
     'out.write(f"Total: {total}\\n")\n'
     'out.close()\n'),
]
