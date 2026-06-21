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
    T.uses_class("Dog", because="Dog is a class that inherits from Animal.")
    T.uses_class("Animal", because="Animal is the base class.")
