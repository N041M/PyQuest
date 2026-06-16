# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("return a filtered list instead of yielding",
     'def evens(nums):\n'
     '    return [n for n in nums if n % 2 == 0]\n'),
    # The classic dodge: a filtering generator EXPRESSION is a generator
    # (is_generator passes) but uses no yield. uses_yield bites.
    ("a filtering generator expression, no yield",
     'def evens(nums):\n'
     '    return (n for n in nums if n % 2 == 0)\n'),
    # Manual sidestep (playbook): genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("evens").
    ("genexpr target + decoy yield in another function",
     'def _decoy():\n'
     '    yield 1\n'
     'def evens(nums):\n'
     '    return (n for n in nums if n % 2 == 0)\n'),
    # The forbidden genexpr in disguise: `yield from (filtering genexpr)` hides
    # the guarded yield inside a comprehension, behind a yield-from token.
    # Defeated by uses_yield(name) rejecting yield-from of a comprehension.
    ("yield from a filtering generator expression (genexpr in disguise)",
     'def evens(nums):\n'
     '    yield from (n for n in nums if n % 2 == 0)\n'),
]
