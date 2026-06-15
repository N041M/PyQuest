# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("list.sort() in place instead of the sorted() built-in",
     "n = int(input())\n"
     "nums = []\n"
     "for _ in range(n):\n"
     "    nums.append(int(input()))\n"
     "nums.sort()\n"
     "for x in nums:\n"
     "    print(x)\n"),
]
