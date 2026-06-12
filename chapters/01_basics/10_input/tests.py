from engine.inputs import random_word


def check(T):
    # fixed: the exact example from the brief, and a one-letter name
    T.eq(T.run(stdin="World\n"), "Hello, World",
         because="With input 'World', output should be: Hello, World")
    T.eq(T.run(stdin="Q\n"), "Hello, Q")
    # randomized names so the greeting can't be hardcoded
    for _ in range(6):
        name = random_word(1, 9)
        T.eq(T.run(stdin=name + "\n"), "Hello, " + name,
             because="With input %r, output should be %r."
                     % (name, "Hello, " + name))
