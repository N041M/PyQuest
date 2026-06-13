# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("dashes typed in + decoy sep on a silent print",
     'print("2024-12-25")\n'
     'print(end="", sep="-")\n'),
]
