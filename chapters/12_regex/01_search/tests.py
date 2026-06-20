from engine.inputs import Case, random_word, random_int


def cases():
    cs = [Case(args=("abc4",), expect=True),
          Case(args=("abc",), expect=False),
          Case(args=("",), expect=False)]
    for _ in range(8):
        word = random_word(3, 8)
        if random_int(0, 1):
            pos = random_int(0, len(word))
            word = word[:pos] + str(random_int(0, 9)) + word[pos:]
        cs.append(Case(args=(word,), expect=any(c.isdigit() for c in word)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("has_digit", *c.args), c.expect,
             because="has_digit(%r) should be %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Detect the digit with re.search(r'\\d', ...), not a "
                          "hand-written character scan.")
