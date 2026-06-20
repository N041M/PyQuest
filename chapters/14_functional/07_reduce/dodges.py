DODGES = [
    ("folds with a manual accumulator loop, never importing reduce",
     "def product(nums):\n"
     "    result = 1\n"
     "    for n in nums:\n"
     "        result *= n\n"
     "    return result\n"),
]
