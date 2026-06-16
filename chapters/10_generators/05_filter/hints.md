Loop over every number, but only `yield` the ones that pass an evenness test.

---

`for n in nums:` then `if n % 2 == 0:` and, indented under the if, `yield n`.
The odd numbers simply fall through without yielding.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
