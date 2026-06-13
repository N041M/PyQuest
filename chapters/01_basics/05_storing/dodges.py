# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("computed prints + decoy assignment, no stored 42",
     'x = 1\n'
     'print(int("42"))\n'
     'print(40 + 2)\n'),
    ("the text \"42\" stored instead of the number",
     'v = "42"\n'
     'print(v)\n'
     'print(v)\n'),
]
