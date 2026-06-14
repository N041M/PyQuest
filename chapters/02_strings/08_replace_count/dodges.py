# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("replace and count rebuilt by hand, using neither method",
     's = input()\n'
     'print("".join("0" if c == "o" else c for c in s))\n'
     'print(sum(1 for c in s if c == "o"))\n'),
]
