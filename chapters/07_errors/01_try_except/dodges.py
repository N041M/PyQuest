# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("look-before-you-leap .isdigit() guard instead of try/except",
     "line = input()\n"
     "if line.lstrip(\"-\").isdigit():\n"
     "    print(int(line) * 2)\n"
     "else:\n"
     "    print(\"not a number\")\n"),
]
