from engine.inputs import random_int


def check(T):
    # ---- numbers(n): the source --------------------------------------------
    for n in [0, 1, 4] + [random_int(0, 15) for _ in range(5)]:
        gen = T.call("numbers", n)
        T.is_generator(gen, because="numbers must yield, not return a list.")
        T.eq(list(gen), list(range(n)),
             because="numbers(%r) should yield %r." % (n, list(range(n))))

    # ---- keep_even(stream): the filter, on a plain list --------------------
    for nums in [[1, 2, 3, 4], [1, 3, 5], []] + [
            [random_int(-9, 9) for _ in range(random_int(0, 7))]
            for _ in range(5)]:
        gen = T.call("keep_even", list(nums))
        T.is_generator(gen, because="keep_even must yield, not return a list.")
        T.eq(list(gen), [x for x in nums if x % 2 == 0],
             because="keep_even(%r) should yield its even numbers." % (nums,))

    # ---- labelled(stream): the transform, on a plain list ------------------
    for nums in [[0, 2], [7], []] + [
            [random_int(0, 20) for _ in range(random_int(0, 6))]
            for _ in range(5)]:
        gen = T.call("labelled", list(nums))
        T.is_generator(gen, because="labelled must yield, not return a list.")
        T.eq(list(gen), ["#%d" % x for x in nums],
             because="labelled(%r) should yield '#x' strings." % (nums,))

    # ---- the pipeline: stages feeding stages -------------------------------
    for n in [6, 0, 1] + [random_int(0, 15) for _ in range(5)]:
        piped = T.call("labelled", T.call("keep_even", T.call("numbers", n)))
        T.is_generator(piped, because="the composed pipeline is still a stream.")
        T.eq(list(piped), ["#%d" % x for x in range(n) if x % 2 == 0],
             because="labelled(keep_even(numbers(%r))) should yield the even "
                     "numbers below %r as '#x' labels." % (n, n))

    # each stage is a real yield-driven generator written with yield in its own
    # body -- not a genexpr, and not a yield parked in a nested/unrelated function
    for fname in ("numbers", "keep_even", "labelled"):
        T.uses_yield(fname,
                     because="Each pipeline stage must be a generator: %s must "
                             "use yield in its own body." % fname)
