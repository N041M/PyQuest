# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("prepend-in-a-loop reversal instead of the s[::-1] slice",
     "s = input()\n"
     "result = \"\"\n"
     "for ch in s:\n"
     "    result = ch + result\n"
     "print(result)\n"),
]
