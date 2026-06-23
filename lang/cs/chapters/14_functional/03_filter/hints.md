`filter(pred, nums)` ponechá každé číslo, kde je `pred` pravda. Tvůj predikát
testuje sudost: `lambda x: x % 2 == 0`.

---

Obal ho do `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
