# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("flat if/elif chain, no nesting",
     'n = int(input())\n'
     'if n <= 0:\n'
     '    print("non-positive")\n'
     'elif n < 100:\n'
     '    print("small")\n'
     'else:\n'
     '    print("big")\n'),
]
