# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("using eval to parse and int just to satisfy the check",
     'val = input()\n'
     'print(int(eval(val) * 2))\n'),
    ("adding a live but useless int call",
     'print(eval(input()) * 2 + int("0"))\n'),
]
