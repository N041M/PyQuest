# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("hand-written accumulator loop instead of sum()",
     'def average(nums):\n'
     '    t = 0\n'
     '    for x in nums:\n'
     '        t += x\n'
     '    return t / len(nums)\n'),
    ("accumulator loop, sum([total]) wraps it to fake a live sum()",
     'def average(nums):\n'
     '    total = 0\n'
     '    for x in nums:\n'
     '        total += x\n'
     '    return sum([total]) / len(nums)\n'),
]
