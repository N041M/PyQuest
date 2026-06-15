# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("range(len()) index counter instead of enumerate()",
     "n = int(input())\n"
     "words = []\n"
     "for _ in range(n):\n"
     "    words.append(input())\n"
     "for i in range(len(words)):\n"
     "    print(f\"{i + 1}. {words[i]}\")\n"),
]
