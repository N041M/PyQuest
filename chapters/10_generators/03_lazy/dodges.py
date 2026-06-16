# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    # A plain iterator over a range is not a generator. is_generator bites.
    ("return a range iterator, not a generator",
     'def naturals():\n'
     '    return iter(range(10 ** 9))\n'),
    # A generator expression IS a generator (and is lazy) but uses no yield.
    # uses_yield bites -- the lesson is writing the generator with yield.
    ("a bare generator expression, no yield",
     'from itertools import count\n'
     'def naturals():\n'
     '    return (i for i in count())\n'),
    # Manual sidestep (playbook): lazy genexpr target + a decoy yield elsewhere
    # fools a file-level uses_yield. Defeated by uses_yield("naturals").
    ("genexpr target + decoy yield in another function",
     'from itertools import count\n'
     'def _decoy():\n'
     '    yield 1\n'
     'def naturals():\n'
     '    return (i for i in count())\n'),
    # A FINITE generator sized to the checker's small take-counts -- yields the
    # right values for the first handful but runs out, so it is NOT endless.
    # Defeated by the large-offset endlessness probe in tests.py.
    ("finite generator sized to the take-counts, not endless",
     'def naturals():\n'
     '    yield from range(15)\n'),
]
