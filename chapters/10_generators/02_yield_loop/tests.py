from engine.inputs import Case, random_int


def cases():
    cs = [Case(args=(4,), expect=[0, 1, 4, 9]),
          Case(args=(1,), expect=[0]),
          Case(args=(0,), expect=[]),          # edge: nothing to yield
          Case(args=(-2,), expect=[])]         # edge: negative is also empty
    for _ in range(8):
        n = random_int(0, 20)
        cs.append(Case(args=(n,), expect=[i * i for i in range(n)]))
    return cs


def check(T):
    for c in cases():
        gen = T.call("squares", *c.args)
        T.is_generator(gen,
                       because="squares must YIELD its values, so calling it "
                               "returns a generator -- not a finished list.")
        T.eq(list(gen), c.expect,
             because="list(squares(%r)) should be %r." % (c.args[0], c.expect))
    T.uses_yield("squares",
                 because="The lesson is yield inside a loop: emit each square "
                         "with yield in squares itself -- not a returned list "
                         "or a generator expression.")
