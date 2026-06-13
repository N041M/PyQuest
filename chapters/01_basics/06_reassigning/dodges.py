# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("decoy reassignment + computed prints",
     'a = 1\n'
     'a = 2\n'
     'print(int("10"))\n'
     'print(int("20"))\n'),
    ("two different variables instead of one reassigned",
     'x = 10\n'
     'y = 20\n'
     'print(x)\n'
     'print(y)\n'),
]
