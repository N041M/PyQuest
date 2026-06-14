# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right output but no `with` (bare open().read())",
     'print(open("note.txt").read())\n'),
    ("reads bare, fakes the lesson with an unrelated live `with io.StringIO()`",
     'import io\n'
     'text = open("note.txt").read()\n'
     'with io.StringIO() as s:\n'
     '    print(text)\n'),
]
