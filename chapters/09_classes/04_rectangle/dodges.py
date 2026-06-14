# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("plain functions, not a class with methods",
     "def Rectangle(width, height):\n"
     "    return (width, height)\n"),
]
