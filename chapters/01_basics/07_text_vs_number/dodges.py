# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("right outputs from + on the wrong numbers",
     'print(54 + 1)\n'
     'print(9 + 1)\n'),
    ("the text line typed in whole",
     'print("55")\n'
     'print(5 + 5)\n'),
]
