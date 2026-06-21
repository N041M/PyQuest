from engine.inputs import random_int


def check(T):
    Shape = T.get("Shape")
    # fixed checks
    r = T.make("Rectangle", 3, 4)
    T.true(isinstance(r, Shape), because="Rectangle inherits from Shape.")
    T.eq(T.attr(r, "name"), "rectangle", because="name set via super().__init__.")
    T.eq(T.attr(r, "area"), 12, because="area property is width * height.")
    T.eq(T.method(r, "describe"), "rectangle with area 12",
         because="describe (from Shape) uses the subclass's area property.")
    T.true(T.make("Rectangle", 2, 6) == T.make("Rectangle", 3, 4),
           because="equal areas (12) -> equal rectangles via __eq__.")

    for _ in range(8):
        dims = [(random_int(1, 12), random_int(1, 12)) for _ in range(4)]
        objs = [T.make("Rectangle", w, h) for w, h in dims]
        ordered = sorted(objs)
        T.eq([T.attr(o, "area") for o in ordered],
             sorted(w * h for w, h in dims),
             because="rectangles sort by area via __lt__.")
        # property stays live after a change
        o = objs[0]
        o.width = o.width + 5
        T.eq(T.attr(o, "area"), o.width * dims[0][1],
             because="area recomputes after width changes (a property).")
    # area must be a real @property descriptor (not a stored value or a
    # __getattr__ stand-in), and the name must be set by super().__init__ (not
    # assigned by hand) -- both pass the value checks above otherwise.
    Rectangle = T.get("Rectangle")
    T.true(isinstance(getattr(Rectangle, "area", None), property),
           because="area must be a @property on Rectangle, not a plain "
                   "attribute or a __getattr__ stand-in.")
    called = []
    orig = Shape.__init__

    def spy(self, *a, **k):
        called.append(True)
        return orig(self, *a, **k)

    Shape.__init__ = spy
    try:
        T.make("Rectangle", 3, 4)
    finally:
        Shape.__init__ = orig
    T.true(bool(called),
           because="Rectangle.__init__ must set the name via "
                   "super().__init__('rectangle'), not assign it by hand.")
    T.uses_class("Rectangle", because="Rectangle extends Shape with the lot.")
    T.uses_class("Shape", because="Shape is the base class.")
