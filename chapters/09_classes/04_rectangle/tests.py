from engine.inputs import random_int


def check(T):
    r = T.make("Rectangle", 3, 4)
    T.eq(T.method(r, "area"), 12, because="Rectangle(3, 4).area() is 12.")
    T.eq(T.method(r, "perimeter"), 14,
         because="Rectangle(3, 4).perimeter() is 14.")

    for _ in range(8):
        w = random_int(1, 40)
        h = random_int(1, 40)
        r = T.make("Rectangle", w, h)
        T.eq(T.method(r, "area"), w * h,
             because="area of %dx%d is %d." % (w, h, w * h))
        T.eq(T.method(r, "perimeter"), 2 * (w + h),
             because="perimeter of %dx%d is %d." % (w, h, 2 * (w + h)))
    T.uses_class('Rectangle', because="width, height and both methods belong to a `class`.")
