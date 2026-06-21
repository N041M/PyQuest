from engine.inputs import random_int


def check(T):
    T.true(T.make("Temperature", 10) < T.make("Temperature", 20),
           because="10 degrees is less than 20.")
    for _ in range(8):
        degrees = [random_int(-50, 50) for _ in range(random_int(2, 7))]
        objs = [T.make("Temperature", d) for d in degrees]
        ordered = sorted(objs)
        T.eq([T.attr(o, "degrees") for o in ordered], sorted(degrees),
             because="sorted() must order the temperatures by degrees: %r"
                     % sorted(degrees))
    T.uses_class("Temperature",
                 because="Temperature defines __lt__ so it can be sorted.")
