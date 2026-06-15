# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("loop + if + append instead of the filtering comprehension",
     "n = int(input())\n"
     "nums = []\n"
     "for _ in range(n):\n"
     "    nums.append(int(input()))\n"
     "evens = []\n"
     "for x in nums:\n"
     "    if x % 2 == 0:\n"
     "        evens.append(x)\n"
     "for e in evens:\n"
     "    print(e)\n"),
    ("a plain comprehension reads input, but the filter is a separate loop",
     "n = int(input())\n"
     "nums = [int(input()) for _ in range(n)]\n"
     "evens = []\n"
     "for x in nums:\n"
     "    if x % 2 == 0:\n"
     "        evens.append(x)\n"
     "for e in evens:\n"
     "    print(e)\n"),
]
