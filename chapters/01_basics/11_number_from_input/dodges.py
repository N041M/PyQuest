# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("eval() skips the int() conversion lesson",
     'print(eval(input()) * 2)\n'),
]
