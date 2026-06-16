def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
