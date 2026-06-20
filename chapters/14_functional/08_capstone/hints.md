Three steps. First `filter(lambda r: r[1] >= threshold, records)` keeps the
records that qualify (r[1] is the score).

---

Then `sorted(qualified, key=lambda r: r[1], reverse=True)` ranks them high to
low, and `map(lambda r: r[0], ...)` pulls out the names. Wrap the map in `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
