from engine.inputs import random_int


def check(T):
    c = T.make("Counter")
    T.eq(T.method(c, "tick"), 1, because="First tick returns 1.")
    T.eq(T.method(c, "tick"), 2, because="State persists: second tick is 2.")
    T.eq(T.method(c, "tick"), 3, because="Third tick is 3.")
    T.eq(T.attr(c, "count"), 3, because="count is stored on self.")

    for _ in range(6):
        n = random_int(1, 15)
        c = T.make("Counter")
        last = None
        for _ in range(n):
            last = T.method(c, "tick")
        T.eq(last, n, because="After %d ticks the count is %d." % (n, n))

    # independence: two counters keep separate tallies
    a = T.make("Counter")
    b = T.make("Counter")
    T.method(a, "tick")
    T.method(a, "tick")
    T.eq(T.method(b, "tick"), 1,
         because="Ticking a must not affect b -- count lives on the instance, "
                 "not the class.")
    T.uses_class('Counter', because="The counter's memory is an instance of a `class`.")
