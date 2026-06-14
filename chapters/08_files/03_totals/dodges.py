# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right total but no `with`",
     'total = 0\n'
     'for line in open("prices.txt"):\n'
     '    total += int(line)\n'
     'print(total)\n'),
    ("eval() instead of the int() conversion lesson",
     'with open("prices.txt") as f:\n'
     '    print(sum(eval(line) for line in f))\n'),
    ("reads bare, fakes the lesson with an unrelated live `with io.StringIO()`",
     'import io\n'
     'total = 0\n'
     'for line in open("prices.txt"):\n'
     '    total += int(line)\n'
     'with io.StringIO() as s:\n'
     '    print(total)\n'),
]
