Keep a `total` variable outside the loop, add each number to it inside the
loop, and `yield` the total after each addition.

---

`total = 0` before the loop. Then `for n in nums:` -- `total = total + n`,
then `yield total`. The total is remembered across the yields, so it keeps
growing.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
