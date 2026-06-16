# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    # Returns the right numbers, but as a list -- no generator. is_generator bites.
    ("return a list instead of yielding",
     'def count_down(n):\n'
     '    return list(range(n, 0, -1))\n'),
    # A generator expression IS a generator (is_generator passes) but uses no
    # yield -- the lesson is the yield form. uses_yield bites.
    ("a bare generator expression, no yield",
     'def count_down(n):\n'
     '    return (i for i in range(n, 0, -1))\n'),
    # Manual sidestep (playbook): genexpr target passes is_generator, and a
    # yield parked in an UNRELATED function satisfies a file-level uses_yield.
    # Defeated by scoping the check: uses_yield("count_down").
    ("genexpr target + decoy yield in another function",
     'def _decoy():\n'
     '    yield 1\n'
     'def count_down(n):\n'
     '    return (i for i in range(n, 0, -1))\n'),
    # The forbidden genexpr in disguise: `yield from (genexpr)` re-emits the
    # very comprehension the brief rules out, behind a yield-from token.
    # Defeated by uses_yield(name) rejecting yield-from of a comprehension.
    ("yield from a generator expression (genexpr in disguise)",
     'def count_down(n):\n'
     '    yield from (i for i in range(n, 0, -1))\n'),
]
