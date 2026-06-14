from engine.inputs import random_word, random_int


def check(T):
    d = T.make("Dog", "Rex", 3)
    T.eq(T.attr(d, "name"), "Rex", because="__init__ should store name on self.")
    T.eq(T.attr(d, "age"), 3, because="__init__ should store age on self.")

    for _ in range(8):
        name = random_word(2, 8).capitalize()
        age = random_int(0, 20)
        d = T.make("Dog", name, age)
        T.eq(T.attr(d, "name"), name,
             because="Dog(%r, %r).name should be %r." % (name, age, name))
        T.eq(T.attr(d, "age"), age,
             because="Dog(%r, %r).age should be %r." % (name, age, age))

    # two dogs are independent objects
    a = T.make("Dog", "Ada", 1)
    b = T.make("Dog", "Bo", 2)
    T.eq(T.attr(a, "name"), "Ada",
         because="Each Dog keeps its own data -- a is not b.")
    T.uses_class('Dog', because="Bundle the data with a `class`, not a tuple or dict.")
