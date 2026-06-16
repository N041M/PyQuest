# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    # Builds the totals into a list and returns it -- no generator.
    ("return a list of totals instead of yielding",
     'def running_total(nums):\n'
     '    out = []\n'
     '    total = 0\n'
     '    for n in nums:\n'
     '        total += n\n'
     '        out.append(total)\n'
     '    return out\n'),
    # A genexpr over accumulate yields the right totals and IS a generator
    # (is_generator passes), but uses no yield -- uses_yield bites.
    ("a generator expression over accumulate, no yield",
     'from itertools import accumulate\n'
     'def running_total(nums):\n'
     '    return (t for t in accumulate(nums))\n'),
    # Manual sidestep (playbook): genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("running_total").
    ("genexpr target + decoy yield in another function",
     'from itertools import accumulate\n'
     'def _decoy():\n'
     '    yield 1\n'
     'def running_total(nums):\n'
     '    return (t for t in accumulate(nums))\n'),
]
