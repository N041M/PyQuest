# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("manual min/max tracking instead of the built-ins",
     "n = int(input())\n"
     "lo = hi = None\n"
     "for _ in range(n):\n"
     "    x = int(input())\n"
     "    if lo is None or x < lo:\n"
     "        lo = x\n"
     "    if hi is None or x > hi:\n"
     "        hi = x\n"
     "print(lo)\n"
     "print(hi)\n"),
    ("manual tracking, min([lo])/max([hi]) wrap to fake the built-ins",
     "n = int(input())\n"
     "nums = [int(input()) for _ in range(n)]\n"
     "lo = hi = nums[0]\n"
     "for x in nums:\n"
     "    if x < lo:\n"
     "        lo = x\n"
     "    if x > hi:\n"
     "        hi = x\n"
     "print(min([lo]))\n"
     "print(max([hi]))\n"),
]
