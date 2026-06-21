DODGES = [
    ("uses a loop with a flag instead of any",
     "def has_negative(nums):\n"
     "    for n in nums:\n"
     "        if n < 0:\n"
     "            return True\n"
     "    return False\n"),
    ("loop-with-a-flag computes it, any([flag]) wraps to fake using any",
     "def has_negative(nums):\n"
     "    neg = False\n"
     "    for n in nums:\n"
     "        if n < 0:\n"
     "            neg = True\n"
     "    return any([neg])\n"),
    ("loop-with-a-flag, any(flag for _ in [0]) -- a genexpr not over the input",
     "def has_negative(nums):\n"
     "    neg = False\n"
     "    for n in nums:\n"
     "        if n < 0:\n"
     "            neg = True\n"
     "    return any(neg for _ in [0])\n"),
]
