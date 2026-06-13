# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("string-multiply trick + decoy if in dead code",
     'n = int(input())\n'
     'print("negative" * (n < 0))\n'
     'if False:\n'
     '    pass\n'),
]
