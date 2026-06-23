Drž na košíku seznam (`self.items = []` v `__init__`); `add` do něj přidává.

---

`total` sečte ceny -- `sum(price for name, price in self.items)`, pokud ukládáš
dvojice `(name, price)`.
