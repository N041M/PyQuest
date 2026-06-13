# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("each operator on the wrong numbers",
     'print(3.5 / 1)\n'
     'print(3 // 1)\n'
     'print(1 % 2)\n'),
    ("answers typed + operators parked in dead code",
     'print(3.5)\n'
     'print(3)\n'
     'print(1)\n'
     'q = 7 / 2 if False else 0\n'
     'w = 7 // 2 if False else 0\n'
     'e = 7 % 2 if False else 0\n'),
]
