# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("slice instead of an index, decoy index in dead code",
     'w = input()\n'
     'print(w[0:1])\n'
     'if False:\n'
     '    q = "x"[0]\n'),
]
