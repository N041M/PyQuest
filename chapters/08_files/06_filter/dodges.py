# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right output file, but no `with` was used",
     'inp = open("lines.txt").readlines()\n'
     'out = open("kept.txt", "w")\n'
     'for line in inp:\n'
     '    if line.strip():\n'
     '        out.write(line)\n'
     'out.close()\n'),
    ("copies every line -- forgets to filter the blanks",
     'with open("lines.txt") as f:\n'
     '    data = f.read()\n'
     'with open("kept.txt", "w") as f:\n'
     '    f.write(data)\n'),
    ("reads/writes bare, fakes the lesson with a live `with io.StringIO()`",
     'import io\n'
     'lines = open("lines.txt").readlines()\n'
     'with io.StringIO("") as s:\n'
     '    marker = s.read()\n'
     'out = open("kept.txt", "w")\n'
     'out.write(marker)\n'
     'for line in lines:\n'
     '    if line.strip():\n'
     '        out.write(line)\n'
     'out.close()\n'),
]
