# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("correct output file but no `with` anywhere",
     'open("out.txt", "w").write(open("in.txt").read().upper())\n'),
    ("reads/writes bare, fakes the lesson with a live `with io.StringIO()`",
     'import io\n'
     'inp = open("in.txt").read()\n'
     'with io.StringIO("") as s:\n'
     '    marker = s.read()\n'
     'open("out.txt", "w").write(inp.upper() + marker)\n'),
]
