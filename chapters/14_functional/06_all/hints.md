`all(...)` returns True only if every value in the sequence is true. Build the
sequence of tests with a generator expression.

---

`all(n > 0 for n in nums)` -- each `n > 0` is True or False, and `all` is True
only if none were False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
