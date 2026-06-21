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
    # from_tuple must build with cls(...), so a SUBCLASS's from_tuple returns an
    # instance of the subclass. A @staticmethod, or a classmethod that hardcodes
    # Point(...), returns a plain Point and fails this -- the point of cls.
    class _Sub(Point):
        pass

    s = _Sub.from_tuple((1, 2))
    T.true(isinstance(s, _Sub),
           because="from_tuple must build via cls(...) -- on a subclass it must "
                   "return the subclass, not a hardcoded Point or a "
                   "@staticmethod's Point.")
    T.uses_class("Point", because="Point offers from_tuple as a classmethod.")
