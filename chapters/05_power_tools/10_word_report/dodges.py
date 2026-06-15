# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("sorted(set()) + list.count() instead of a dict tally",
     "words = input().split()\n"
     "for w in sorted(set(words)):\n"
     "    print(w, words.count(w))\n"),
]
