# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("nested-list membership scan instead of set intersection (a & b)",
     "n = int(input())\n"
     "a = []\n"
     "for _ in range(n):\n"
     "    a.append(input())\n"
     "m = int(input())\n"
     "b = []\n"
     "for _ in range(m):\n"
     "    b.append(input())\n"
     "count = 0\n"
     "seen = []\n"
     "for x in a:\n"
     "    if x in b and x not in seen:\n"
     "        count += 1\n"
     "        seen.append(x)\n"
     "print(count)\n"),
]
