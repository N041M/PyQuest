# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# Each stage must be a real yield-driven generator; these prove the per-stage
# yield check bites (a genexpr or a returned list is not the lesson).
DODGES = [
    ("filter stage as a generator expression, no yield",
     'def numbers(n):\n'
     '    for i in range(n):\n'
     '        yield i\n'
     'def keep_even(stream):\n'
     '    return (x for x in stream if x % 2 == 0)\n'
     'def labelled(stream):\n'
     '    for x in stream:\n'
     '        yield f"#{x}"\n'),
    ("a stage returns a list instead of yielding",
     'def numbers(n):\n'
     '    for i in range(n):\n'
     '        yield i\n'
     'def keep_even(stream):\n'
     '    for x in stream:\n'
     '        if x % 2 == 0:\n'
     '            yield x\n'
     'def labelled(stream):\n'
     '    return ["#%d" % x for x in stream]\n'),
    # Manual sidestep: a genexpr stage with a DEAD yield in a nested,
    # uncalled inner function -- defeats a naive per-function ast.walk scan that
    # descends into nested scopes. Defeated by uses_yield(name), which only
    # counts a yield in the stage's OWN body (nested defs are a different scope).
    ("genexpr stage hiding a yield in a nested function",
     'def numbers(n):\n'
     '    for i in range(n):\n'
     '        yield i\n'
     'def keep_even(stream):\n'
     '    def _unused():\n'
     '        yield\n'
     '    return (x for x in stream if x % 2 == 0)\n'
     'def labelled(stream):\n'
     '    for x in stream:\n'
     '        yield f"#{x}"\n'),
    # The forbidden genexpr in disguise: every stage delegates to a comprehension
    # behind `yield from`, so no stage is a real yield-driven generator of its
    # own. Defeated by uses_yield(name) rejecting yield-from of a comprehension.
    ("every stage a yield-from genexpr (genexpr in disguise)",
     'def numbers(n):\n'
     '    yield from (i for i in range(n))\n'
     'def keep_even(stream):\n'
     '    yield from (x for x in stream if x % 2 == 0)\n'
     'def labelled(stream):\n'
     '    yield from ("#%d" % x for x in stream)\n'),
]
