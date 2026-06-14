# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("reads the line from sys.stdin instead of input()",
     'import sys\n'
     'print("Hello, " + sys.stdin.readline().rstrip("\\n"))\n'),
]
