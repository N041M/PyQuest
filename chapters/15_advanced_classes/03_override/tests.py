from engine.inputs import random_word


def check(T):
    Animal = T.get("Animal")
    for name in [random_word(3, 7) for _ in range(8)]:
        cat = T.make("Cat", name)
        T.eq(T.method(cat, "speak"), "Meow",
             because="Cat overrides speak().")
        T.eq(T.attr(cat, "name"), name,
             because="Cat still inherits __init__ from Animal.")
        T.true(isinstance(cat, Animal), because="A Cat is an Animal.")
    base = T.make("Animal", "thing")
    T.eq(T.method(base, "speak"), "...",
         because="A plain Animal keeps the generic speak().")
    T.uses_class("Cat", because="Cat overrides Animal.speak.")
    T.uses_class("Animal", because="Animal is the base class.")
