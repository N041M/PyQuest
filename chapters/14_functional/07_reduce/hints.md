`from functools import reduce`. It takes a two-argument combiner, the items, and
a start value.

---

The combiner multiplies the running result by the next number:
`reduce(lambda a, b: a * b, nums, 1)`. The start `1` makes the empty list give 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
