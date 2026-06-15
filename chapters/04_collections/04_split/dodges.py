# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("hand-rolled whitespace scan instead of .split()",
     "line = input()\n"
     "count = 0\n"
     "in_word = False\n"
     "for ch in line:\n"
     "    if ch.isspace():\n"
     "        in_word = False\n"
     "    elif not in_word:\n"
     "        in_word = True\n"
     "        count += 1\n"
     "print(count)\n"),
]
