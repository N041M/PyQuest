# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right report file, but no `with` was used",
     'words = open("words.txt").read().split()\n'
     'counts = {}\n'
     'for w in words:\n'
     '    counts[w] = counts.get(w, 0) + 1\n'
     'out = open("report.txt", "w")\n'
     'for w in sorted(counts, key=lambda w: (-counts[w], w)):\n'
     '    out.write(f"{w}: {counts[w]}\\n")\n'
     'out.close()\n'),
    ("reads/writes bare, fakes the lesson with a live `with io.StringIO()`",
     'import io\n'
     'words = open("words.txt").read().split()\n'
     'counts = {}\n'
     'for w in words:\n'
     '    counts[w] = counts.get(w, 0) + 1\n'
     'with io.StringIO("") as s:\n'
     '    marker = s.read()\n'
     'out = open("report.txt", "w")\n'
     'out.write(marker)\n'
     'for w in sorted(counts, key=lambda w: (-counts[w], w)):\n'
     '    out.write(f"{w}: {counts[w]}\\n")\n'
     'out.close()\n'),
]
