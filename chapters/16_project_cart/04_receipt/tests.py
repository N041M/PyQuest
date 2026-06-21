from engine.inputs import random_word, random_int


def _expected(items):
    lines = ["%s: $%.2f" % (name, price) for name, price in items]
    lines.append("TOTAL: $%.2f" % sum(price for name, price in items))
    return "\n".join(lines)


def check(T):
    T.eq(T.call("receipt", [("Apple", 1.5), ("Bread", 2.0)]),
         _expected([("Apple", 1.5), ("Bread", 2.0)]),
         because="one line per item, then the TOTAL line.")
    T.eq(T.call("receipt", []), "TOTAL: $0.00",
         because="an empty cart is just the TOTAL line at $0.00.")
    for _ in range(8):
        items = [(random_word(3, 6).capitalize(), random_int(0, 5000) / 100)
                 for _ in range(random_int(1, 5))]
        T.eq(T.call("receipt", items), _expected(items),
             because="receipt of %r" % (items,))
