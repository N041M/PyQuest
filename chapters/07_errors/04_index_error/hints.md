Just index it inside a try -- Python already knows exactly which indexes are
bad.

---

`except IndexError: return default` -- this gets negatives right for free,
which a hand-written bounds check usually doesn't.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
