Prostě to zaindexuj uvnitř try -- Python už přesně ví, které indexy jsou špatné.

---

`except IndexError: return default` -- tím zvládneš záporné zadarmo, což ručně
psaná kontrola mezí obvykle ne.

---

def item_or(items, i, default):
    try:
        return items[i]
    except IndexError:
        return default
