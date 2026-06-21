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
    T.uses_class("Dog", because="Dog extends Animal via super().")
    T.uses_class("Animal", because="Animal is the base class.")
