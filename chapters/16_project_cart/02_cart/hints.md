Keep a list on the cart (`self.items = []` in `__init__`); `add` appends to it.

---

`total` sums the prices -- `sum(price for name, price in self.items)` if you store
`(name, price)` pairs.
