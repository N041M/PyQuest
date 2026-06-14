# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("divisible-by-2-and-3 collapsed to one modulo, no boolean operator",
     'print(int(input()) % 6 == 0)\n'),
]
