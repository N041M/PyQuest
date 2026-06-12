from engine.inputs import random_word, random_int


def check(T):
    T.eq(T.run(stdin="21\n"), "42",
         because="A good first line needs no retries.")
    T.eq(T.run(stdin="cat\ndog\n21\n"), "42",
         because="Garbage lines are retried silently; only 42 is printed.")
    T.eq(T.run(stdin="x\n-4\n"), "-8",
         because="Negative numbers are valid input.")
    for _ in range(8):
        junk = [random_word(2, 6) for _ in range(random_int(0, 4))]
        n = random_int(-99, 99)
        stdin = "".join(w + "\n" for w in junk) + "%d\n" % n
        T.eq(T.run(stdin=stdin), "%d" % (n * 2),
             because="After %d bad line(s), %r should print %r."
                     % (len(junk), n, n * 2))
    T.uses_loop(because="Keep asking -- that's a loop.")
    T.uses_try(because="The retry is powered by try/except ValueError.")
