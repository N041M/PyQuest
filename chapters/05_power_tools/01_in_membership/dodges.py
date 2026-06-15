# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    (".find() instead of the `in` operator",
     "word = input()\n"
     "letter = input()\n"
     "if word.find(letter) >= 0:\n"
     "    print(\"yes\")\n"
     "else:\n"
     "    print(\"no\")\n"),
    (".count() instead of `in`",
     "word = input()\n"
     "letter = input()\n"
     "if word.count(letter) > 0:\n"
     "    print(\"yes\")\n"
     "else:\n"
     "    print(\"no\")\n"),
]
