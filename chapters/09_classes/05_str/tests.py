from engine.inputs import random_int


def check(T):
    T.eq(str(T.make("Point", 3, 4)), "(3, 4)",
         because="str(Point(3, 4)) should be exactly '(3, 4)'.")
    T.eq(str(T.make("Point", 0, 0)), "(0, 0)")

    for _ in range(8):
        x = random_int(-50, 50)
        y = random_int(-50, 50)
        T.eq(str(T.make("Point", x, y)), "(%d, %d)" % (x, y),
             because="str(Point(%d, %d)) should be '(%d, %d)'." % (x, y, x, y))
    # the values are still stored, not just formatted
    p = T.make("Point", 7, 9)
    T.eq(T.attr(p, "x"), 7, because="x is still stored on the object.")
    T.uses_class('Point', because="The display comes from a __str__ method on a class.")
