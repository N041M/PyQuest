from engine.inputs import random_word


def check(T):
    Animal = T.get("Animal")
    for _ in range(8):
        name, breed = random_word(3, 7), random_word(3, 7)
        dog = T.make("Dog", name, breed)
        T.eq(T.attr(dog, "name"), name,
             because="name is set by super().__init__ (Animal's init).")
        T.eq(T.attr(dog, "breed"), breed,
             because="breed is added by Dog's own __init__.")
        T.true(isinstance(dog, Animal),
               because="Dog is an Animal.")
    # name must be set by the PARENT via super().__init__, not assigned by
    # hand. Spy on Animal.__init__: building a Dog must actually call it. A
    # hand-written self.name = name (or a dead `if False: super()`) never does.
    called = []
    orig = Animal.__init__

    def spy(self, *a, **k):
        called.append(True)
        return orig(self, *a, **k)

    Animal.__init__ = spy
    try:
        T.make("Dog", "Rex", "Lab")
    finally:
        Animal.__init__ = orig
    T.true(bool(called),
           because="Dog.__init__ must call super().__init__(name) -- the name "
                   "is set by Animal's init, not assigned by hand.")
    T.uses_class("Dog", because="Dog extends Animal via super().")
    T.uses_class("Animal", because="Animal is the base class.")
