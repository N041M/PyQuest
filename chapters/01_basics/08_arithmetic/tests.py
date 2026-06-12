def check(T):
    out = T.run()
    T.eq(out, "14\n20",
         because="2 + 3 * 4 is 14; (2 + 3) * 4 is 20.")
    # must actually compute with + and * (not type 14/20, or stash them in a
    # variable first).
    T.uses_op("*",
        because="Let Python multiply -- don't type 14 and 20 (or assign them).")
    T.uses_op("+",
        because="Use + as well: the point is how + and * combine.")
