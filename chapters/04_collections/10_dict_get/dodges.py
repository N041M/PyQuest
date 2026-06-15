# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("`if key in d` branch instead of d.get(key, 0)",
     "n = int(input())\n"
     "d = {}\n"
     "for _ in range(n):\n"
     "    key = input()\n"
     "    d[key] = int(input())\n"
     "query = input()\n"
     "if query in d:\n"
     "    print(d[query])\n"
     "else:\n"
     "    print(0)\n"),
]
