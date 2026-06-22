# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("return a list instead of yielding",
     'def squares(n):\n'
     '    return [i * i for i in range(n)]\n'),
    ("a bare generator expression, no yield",
     'def squares(n):\n'
     '    return (i * i for i in range(n))\n'),
    # Manual sidestep: genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("squares").
    ("genexpr target + decoy yield in another function",
     'def _decoy():\n'
     '    yield 1\n'
     'def squares(n):\n'
     '    return (i * i for i in range(n))\n'),
    # The forbidden genexpr in disguise: `yield from (genexpr)` re-emits the
    # comprehension the brief rules out (no yield inside a loop of its own).
    # Defeated by uses_yield(name) rejecting yield-from of a comprehension.
    ("yield from a generator expression (genexpr in disguise)",
     'def squares(n):\n'
     '    yield from (i * i for i in range(n))\n'),
]
