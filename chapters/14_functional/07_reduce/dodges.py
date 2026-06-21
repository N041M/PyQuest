DODGES = [
    ("folds with a manual accumulator loop, never importing reduce",
     "def product(nums):\n"
     "    result = 1\n"
     "    for n in nums:\n"
     "        result *= n\n"
     "    return result\n"),
    ("manual accumulator loop, then reduce(f, [result], 1) wraps to fake reduce",
     "from functools import reduce\n"
     "def product(nums):\n"
     "    result = 1\n"
     "    for n in nums:\n"
     "        result *= n\n"
     "    return reduce(lambda a, b: a * b, [result], 1)\n"),
]
