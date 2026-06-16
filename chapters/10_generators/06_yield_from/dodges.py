# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("return the joined list instead of yielding",
     'def chain(a, b):\n'
     '    return list(a) + list(b)\n'),
    ("a bare generator expression, no yield",
     'def chain(a, b):\n'
     '    return (x for x in list(a) + list(b))\n'),
    # Manual sidestep (playbook): genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("chain").
    ("genexpr target + decoy yield in another function",
     'def _decoy():\n'
     '    yield 1\n'
     'def chain(a, b):\n'
     '    return (x for x in list(a) + list(b))\n'),
]
