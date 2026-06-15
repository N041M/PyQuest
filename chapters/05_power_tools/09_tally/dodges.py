# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("list.count() instead of a dict tally with .get()",
     "words = input().split()\n"
     "query = input()\n"
     "print(words.count(query))\n"),
]
