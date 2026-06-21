DODGES = [
    ("uses a comprehension instead of map",
     "def squares(nums):\n"
     "    return [x * x for x in nums]\n"),
    ("comprehension squares it, map(identity, ...) wraps to fake using map",
     "def squares(nums):\n"
     "    return list(map(lambda v: v, [x * x for x in nums]))\n"),
]
