# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    # Slices up to the first 0 and returns a list -- correct values, no generator.
    ("return a slice up to the first 0",
     'def until_zero(nums):\n'
     '    nums = list(nums)\n'
     '    cut = nums.index(0) if 0 in nums else len(nums)\n'
     '    return nums[:cut]\n'),
    # takewhile is the right tool but a genexpr/iterator dodge uses no yield.
    ("a takewhile generator expression, no yield",
     'from itertools import takewhile\n'
     'def until_zero(nums):\n'
     '    return (n for n in takewhile(lambda n: n != 0, nums))\n'),
    # Manual sidestep: genexpr target + a decoy yield elsewhere fools
    # a file-level uses_yield. Defeated by uses_yield("until_zero").
    ("genexpr target + decoy yield in another function",
     'from itertools import takewhile\n'
     'def _decoy():\n'
     '    yield 1\n'
     'def until_zero(nums):\n'
     '    return (n for n in takewhile(lambda n: n != 0, nums))\n'),
]
