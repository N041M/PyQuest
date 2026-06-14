from engine.inputs import random_int


def check(T):
    a = T.make("Vector", 1, 2)
    b = T.make("Vector", 3, 4)
    c = T.method(a, "add", b)
    T.eq(T.attr(c, "x"), 4, because="1 + 3 = 4.")
    T.eq(T.attr(c, "y"), 6, because="2 + 4 = 6.")
    T.eq(T.attr(a, "x"), 1, because="add must NOT change the first vector.")
    T.eq(T.attr(b, "y"), 4, because="add must NOT change the other vector.")

    for _ in range(8):
        x1, y1 = random_int(-20, 20), random_int(-20, 20)
        x2, y2 = random_int(-20, 20), random_int(-20, 20)
        v1 = T.make("Vector", x1, y1)
        v2 = T.make("Vector", x2, y2)
        s = T.method(v1, "add", v2)
        T.eq(T.attr(s, "x"), x1 + x2,
             because="sum x of (%d,%d)+(%d,%d)." % (x1, y1, x2, y2))
        T.eq(T.attr(s, "y"), y1 + y2,
             because="sum y of (%d,%d)+(%d,%d)." % (x1, y1, x2, y2))
        # originals untouched
        T.eq(T.attr(v1, "x"), x1, because="the first vector is unchanged.")
        T.eq(T.attr(v2, "x"), x2, because="the other vector is unchanged.")
    T.uses_class('Vector', because="Vector is a `class`, and add returns a new Vector.")
