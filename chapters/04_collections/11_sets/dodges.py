# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("manual dedup into a list instead of using a set",
     "n = int(input())\n"
     "words = []\n"
     "for _ in range(n):\n"
     "    words.append(input())\n"
     "distinct = []\n"
     "for w in words:\n"
     "    if w not in distinct:\n"
     "        distinct.append(w)\n"
     "print(len(distinct))\n"),
]
