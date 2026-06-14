# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("value taken with split(), dodging find + slice",
     'print(input().split("=", 1)[1])\n'),
    ("partition() instead of find + slice",
     'print(input().partition("=")[2])\n'),
]
