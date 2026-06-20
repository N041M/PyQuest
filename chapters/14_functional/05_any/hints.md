`any(...)` takes a sequence of true/false values and returns True if any is true.
Build that sequence with a generator expression.

---

`any(n < 0 for n in nums)` -- for each number, the test `n < 0` is True or False,
and `any` reports whether at least one was True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
