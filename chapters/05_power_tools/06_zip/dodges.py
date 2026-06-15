# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("index loop over both lists instead of zip()",
     "n = int(input())\n"
     "names = []\n"
     "for _ in range(n):\n"
     "    names.append(input())\n"
     "scores = []\n"
     "for _ in range(n):\n"
     "    scores.append(input())\n"
     "for i in range(len(names)):\n"
     "    print(names[i], scores[i])\n"),
]
