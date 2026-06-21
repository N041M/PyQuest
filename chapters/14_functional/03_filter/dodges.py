DODGES = [
    ("uses a comprehension instead of filter",
     "def evens(nums):\n"
     "    return [x for x in nums if x % 2 == 0]\n"),
    ("comprehension selects, filter(lambda: True, ...) wraps to fake filter",
     "def evens(nums):\n"
     "    return list(filter(lambda v: True, [x for x in nums if x % 2 == 0]))\n"),
]
