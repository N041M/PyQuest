from engine.inputs import random_int


def check(T):
    for _ in range(8):
        w, h = random_int(1, 20), random_int(1, 20)
        r = T.make("Rectangle", w, h)
        T.eq(T.attr(r, "area"), w * h,
             because="area is width * height, read with no parentheses.")
        # change a side: a computed property updates; a value stored in __init__
        # would go stale. This is what forces @property over a plain attribute.
        new_w = w + 3
        r.width = new_w
        T.eq(T.attr(r, "area"), new_w * h,
             because="area must recompute after width changes (a property, not "
                     "a value stored once).")
    T.uses_class("Rectangle", because="Rectangle exposes area as a property.")
