Tři kroky. Nejprve `filter(lambda r: r[1] >= threshold, records)` ponechá záznamy,
které kvalifikují (r[1] je skóre).

---

Pak `sorted(qualified, key=lambda r: r[1], reverse=True)` je seřadí od nejvyššího po
nejnižší a `map(lambda r: r[0], ...)` vytáhne jména. Obal map do `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
