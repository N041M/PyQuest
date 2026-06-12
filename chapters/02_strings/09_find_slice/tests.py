from engine.inputs import random_word


def check(T):
    T.eq(T.run(stdin="a=\n"), "",
         because="Nothing follows the '=', so the value is empty.")
    T.eq(T.run(stdin="k=a=b\n"), "a=b",
         because="find returns the FIRST '='; the value keeps the rest.")
    for _ in range(8):
        key = random_word(1, 6)
        value = random_word(1, 8)
        line = key + "=" + value
        T.eq(T.run(stdin=line + "\n"), value,
             because="In %r the value after '=' is %r." % (line, value))
