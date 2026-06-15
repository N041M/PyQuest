# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("manual string building with a separator instead of .join()",
     "n = int(input())\n"
     "words = []\n"
     "for _ in range(n):\n"
     "    words.append(input())\n"
     "result = \"\"\n"
     "for i in range(len(words)):\n"
     "    if i > 0:\n"
     "        result += \"-\"\n"
     "    result += words[i]\n"
     "print(result)\n"),
]
