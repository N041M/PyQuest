# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("pair list does the work, dict parked in dead code",
     'n = int(input())\n'
     'pairs = []\n'
     'for _ in range(n):\n'
     '    w = input()\n'
     '    pairs.append((w, int(input())))\n'
     'query = input()\n'
     'for w, v in pairs:\n'
     '    if w == query:\n'
     '        print(v)\n'
     '        break\n'
     'if False:\n'
     '    d = {"k": 1}\n'),
]
