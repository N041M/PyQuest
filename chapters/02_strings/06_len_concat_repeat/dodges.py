# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# len() is the pinned construct here; these count the characters another way.
# (Repeat is intentionally open: s*3 and s+s+s are both accepted.)
DODGES = [
    ("character count via sum(1 for _ in s), dodging len()",
     "s = input()\n"
     "print(sum(1 for _ in s))\n"
     "print(s + '!')\n"
     "print(s * 3)\n"),
    ("character count via a manual loop, dodging len()",
     "s = input()\n"
     "n = 0\n"
     "for _ in s:\n"
     "    n += 1\n"
     "print(n)\n"
     "print(s + '!')\n"
     "print(s * 3)\n"),
]
