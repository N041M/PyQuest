from engine.inputs import random_word


def check(T):
    Animal = T.get("Animal")
    for name in ["Rex", "Bella"] + [random_word(3, 7) for _ in range(6)]:
        dog = T.make("Dog", name)
        T.eq(T.method(dog, "describe"), name + " the animal",
             because="Dog inherits describe() from Animal.")
        T.eq(T.method(dog, "speak"), "Woof",
             because="Dog adds its own speak().")
        T.true(isinstance(dog, Animal),
               because="A Dog IS an Animal -- inherit from it, don't copy "
                       "describe into Dog.")
    # Inherit describe, don't copy it: a Dog that redefines its own describe
    # passes the value checks above but skips the lesson. The inherited method
    # is literally Animal's function object; a copied one is a different object.
    Dog = T.get("Dog")
    T.true(Dog.describe is Animal.describe,
           because="Dog must INHERIT describe from Animal, not redefine its own "
                   "copy -- shared behavior lives once in the base.")
    T.uses_class("Dog", because="Dog is a class that inherits from Animal.")
    T.uses_class("Animal", because="Animal is the base class.")
