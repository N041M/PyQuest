def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
