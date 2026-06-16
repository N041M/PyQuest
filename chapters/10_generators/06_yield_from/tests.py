from engine.inputs import Case, random_int


def rand_list():
    return [random_int(-9, 9) for _ in range(random_int(0, 5))]


def cases():
    cs = [Case(args=([1, 2], [3, 4]), expect=[1, 2, 3, 4]),
          Case(args=([], [9]), expect=[9]),         # edge: empty first
          Case(args=([7], []), expect=[7]),         # edge: empty second
          Case(args=([], []), expect=[])]           # edge: both empty
    for _ in range(8):
        a, b = rand_list(), rand_list()
        cs.append(Case(args=(a, b), expect=a + b))
    return cs


def check(T):
    for c in cases():
        gen = T.call("chain", *c.args)
        T.is_generator(gen,
                       because="chain must YIELD its items, so calling it "
                               "returns a generator -- not a joined list.")
        T.eq(list(gen), c.expect,
             because="chain(%r, %r) should yield %r."
                     % (c.args[0], c.args[1], c.expect))
    T.uses_yield("chain",
                 because="The lesson is yield from: forward each stream with "
                         "yield in chain itself -- not by returning a + b as "
                         "one list, or a generator expression.")
