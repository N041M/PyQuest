`__init__` sets the starting point: `self.count = 0`. Then `tick` changes it.

---

Inside `tick`, do `self.count = self.count + 1` (or `self.count += 1`), then
`return self.count`. Keep the count on `self` so each counter has its own.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
