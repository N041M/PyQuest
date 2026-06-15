# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("loop + append instead of the list comprehension",
     "n = int(input())\n"
     "nums = []\n"
     "for _ in range(n):\n"
     "    nums.append(int(input()))\n"
     "doubled = []\n"
     "for x in nums:\n"
     "    doubled.append(x * 2)\n"
     "for d in doubled:\n"
     "    print(d)\n"),
]
