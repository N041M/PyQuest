`filter(pred, nums)` keeps each number where `pred` is true. Your predicate tests
even: `lambda x: x % 2 == 0`.

---

Wrap it in `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
