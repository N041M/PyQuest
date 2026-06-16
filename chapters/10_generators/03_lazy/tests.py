from itertools import islice

from engine.inputs import random_int


def check(T):
    # Pull a fixed handful first (the documented edge: the very first value).
    gen = T.call("naturals")
    T.is_generator(gen,
                   because="naturals must YIELD, so calling it returns a "
                           "generator -- not a list (which couldn't be endless).")
    T.eq(list(islice(gen, 5)), [0, 1, 2, 3, 4],
         because="The first 5 naturals are 0, 1, 2, 3, 4.")

    # Randomized take-counts: a fresh generator each time, only ever sliced --
    # so an endless `while True` is exercised but never hangs.
    for _ in range(8):
        k = random_int(1, 15)
        got = list(islice(T.call("naturals"), k))
        T.eq(got, list(range(k)),
             because="The first %d naturals should be %r." % (k, list(range(k))))

    # Endlessness, probed at a large UNPREDICTABLE offset: skip far ahead and
    # take three. A truly endless stream answers; a finite generator sized to
    # the small take-counts above (e.g. `yield from range(15)`) is exhausted
    # here and yields nothing. islice skips lazily, so this never builds a list.
    far = random_int(500, 4000)
    tail = list(islice(T.call("naturals"), far, far + 3))
    T.eq(tail, [far, far + 1, far + 2],
         because="naturals must be endless: items %d, %d, %d should be "
                 "%d, %d, %d -- a finite generator runs out before here."
                 % (far, far + 1, far + 2, far, far + 1, far + 2))

    T.uses_yield("naturals",
                 because="The lesson is a lazy, endless generator built with "
                         "yield in naturals itself -- not a returned iterator "
                         "or a generator expression.")
