# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right constants via the wrong arithmetic",     # the original report
     'print(7*2)\n'
     'print(10+10)\n'),
    ("precedence dodged through a variable",
     'x = 3 * 4\n'
     'print(2 + x)\n'
     'print((2 + 3) * 4)\n'),
    ("second line without parentheses",
     'print(2 + 3 * 4)\n'
     'print(2 * 4 + 3 * 4)\n'),
]
