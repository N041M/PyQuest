from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(5,), expect=[5, 4, 3, 2, 1]),
          Case(args=(1,), expect=[1]),
          Case(args=(0,), expect=[]),          # edge: nothing to yield
          Case(args=(-3,), expect=[])]         # edge: negative is also empty
    for _ in range(8):
        n = random_int(0, 20)
        cs.append(Case(args=(n,), expect=list(range(n, 0, -1))))
    return cs


def check(T):
    for c in cases():
        gen = T.call("count_down", *c.args)
        T.is_generator(gen,
                       because="count_down must YIELD its numbers, so calling "
                               "it returns a generator -- not a finished list.")
        T.eq(list(gen), c.expect,
             because="list(count_down(%r)) should be %r." % (c.args[0], c.expect))
    T.uses_yield("count_down",
                 because="The lesson is yield: produce each number with yield "
                         "in count_down itself -- not a returned list or a "
                         "generator expression.")
