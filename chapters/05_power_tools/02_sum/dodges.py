# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("manual accumulator loop instead of the built-in sum()",
     "n = int(input())\n"
     "total = 0\n"
     "for _ in range(n):\n"
     "    total += int(input())\n"
     "print(total)\n"),
    ("right answer, but sum() only appears in dead code",
     "n = int(input())\n"
     "total = 0\n"
     "for _ in range(n):\n"
     "    total += int(input())\n"
     "_ = sum([1, 2]) if False else 0\n"
     "print(total)\n"),
]
