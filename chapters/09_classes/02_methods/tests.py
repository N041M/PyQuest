from engine.inputs import random_int


def check(T):
    T.eq(T.method(T.make("Square", 5), "area"), 25,
         because="Square(5).area() should be 25.")
    T.eq(T.method(T.make("Square", 0), "area"), 0,
         because="A side of 0 has area 0.")

    for _ in range(8):
        side = random_int(1, 50)
        T.eq(T.method(T.make("Square", side), "area"), side * side,
             because="Square(%d).area() should be %d." % (side, side * side))
    T.uses_class('Square', because="area() must be a method on a `class`.")
