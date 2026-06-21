from engine.inputs import random_word


def check(T):
    T.eq(T.method(T.make("Greeter"), "greet", "Ada"), "Hello, Ada!",
         because="No greeting given -> the default 'Hello' is used.")
    T.eq(T.method(T.make("Greeter", "Hi"), "greet", "Bo"), "Hi, Bo!",
         because="A given greeting overrides the default.")

    for _ in range(6):
        name = random_word(2, 8).capitalize()
        T.eq(T.method(T.make("Greeter"), "greet", name),
             "Hello, %s!" % name,
             because="Default greeting for %r." % name)
        greeting = random_word(2, 6).capitalize()
        T.eq(T.method(T.make("Greeter", greeting), "greet", name),
             "%s, %s!" % (greeting, name),
             because="Custom greeting %r for %r." % (greeting, name))
    T.uses_class('Greeter', because="Greeter is a `class`.")
    T.uses_default_param("__init__",
                         because="The greeting must be a default PARAMETER of "
                                 "__init__ (greeting=\"Hello\"), not an if-check "
                                 "inside it or *args -- and a decoy default on "
                                 "some other function doesn't count.")
