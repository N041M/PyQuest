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
    T.uses_call("find",
                because="The lesson is s.find('=') to locate the marker -- "
                        "split() jumps straight to the answer and skips it.")
    T.uses_slice(
        because="Slice from one past the '=' to the end (s[i+1:]) -- finding "
                "a position then slicing relative to it is the point.")
