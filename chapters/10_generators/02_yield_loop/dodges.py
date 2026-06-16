# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("return a list instead of yielding",
     'def squares(n):\n'
     '    return [i * i for i in range(n)]\n'),
    ("a bare generator expression, no yield",
     'def squares(n):\n'
     '    return (i * i for i in range(n))\n'),
    # Manual sidestep (playbook): genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("squares").
    ("genexpr target + decoy yield in another function",
     'def _decoy():\n'
     '    yield 1\n'
     'def squares(n):\n'
     '    return (i * i for i in range(n))\n'),
]
