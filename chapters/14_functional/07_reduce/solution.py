from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
