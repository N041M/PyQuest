from engine.inputs import Case, random_word, random_int


def cases():
    cs = [Case(args=(["pear", "fig", "kiwi"],), expect=["fig", "kiwi", "pear"]),
          Case(args=([],), expect=[])]
    for _ in range(8):
        words = [random_word(1, 6) for _ in range(random_int(2, 7))]
        cs.append(Case(args=(words,),
                       expect=sorted(words, key=lambda w: w[-1])))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("by_last", *c.args), c.expect,
             because="by_last(%r) -> %r" % (c.args[0], c.expect))
    T.uses_call("sorted",
                because="Order the words with sorted(...), not a hand-written "
                        "sort.")
    T.uses_lambda(because="Sort by an inline key=lambda, the lesson here.")
