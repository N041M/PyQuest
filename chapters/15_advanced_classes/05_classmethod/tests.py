from engine.inputs import random_int


def check(T):
    Point = T.get("Point")
    for _ in range(8):
        x, y = random_int(-30, 30), random_int(-30, 30)
        p = Point.from_tuple((x, y))
        T.true(isinstance(p, Point),
               because="from_tuple must build a Point via cls(...).")
        T.eq(T.attr(p, "x"), x, because="x comes from the tuple's first item.")
        T.eq(T.attr(p, "y"), y, because="y comes from the tuple's second item.")
    T.uses_class("Point", because="Point offers from_tuple as a classmethod.")
