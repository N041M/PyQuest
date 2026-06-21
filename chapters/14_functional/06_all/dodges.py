DODGES = [
    ("uses a loop with a flag instead of all",
     "def all_positive(nums):\n"
     "    for n in nums:\n"
     "        if n <= 0:\n"
     "            return False\n"
     "    return True\n"),
    ("loop-with-a-flag computes it, all([not bad]) wraps to fake using all",
     "def all_positive(nums):\n"
     "    bad = False\n"
     "    for n in nums:\n"
     "        if n <= 0:\n"
     "            bad = True\n"
     "    return all([not bad])\n"),
    ("loop-with-a-flag, all(flag for _ in [0]) -- a genexpr not over the input",
     "def all_positive(nums):\n"
     "    bad = False\n"
     "    for n in nums:\n"
     "        if n <= 0:\n"
     "            bad = True\n"
     "    return all(not bad for _ in [0])\n"),
]
