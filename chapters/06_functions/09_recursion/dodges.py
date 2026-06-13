# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("loop factorial + self-call parked in dead code",
     'def fact(n):\n'
     '    out = 1\n'
     '    for i in range(2, n + 1):\n'
     '        out *= i\n'
     '    if False:\n'
     '        fact(0)\n'
     '    return out\n'),
]
