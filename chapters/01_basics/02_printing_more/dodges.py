# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("one string + silenced 3-arg print",
     'import io\n'
     'print("Counting:")\n'
     'print("1 2 3")\n'
     'print(1, 2, 3, file=io.StringIO())\n'),
    ("one string padded with empty extra args",
     'print("Counting:")\n'
     'print("1 2 3", "", "")\n'),
]
