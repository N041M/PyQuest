def check(T):
    out = T.run()
    T.eq(out, "55\n10",
         because="Line 1 joins text \"5\"+\"5\" = 55; line 2 adds 5+5 = 10.")
    # the lesson is the SAME + sign doing two different jobs on the same
    # digits -- so each line must be built from its own pair of 5s.
    T.line_uses_op(0, "+",
        because="Build the first line with +: \"5\" + \"5\" (text joining).")
    T.line_only_literals(0, {"5"},
        because="The first line glues the TEXT \"5\" and \"5\" -- nothing else.")
    T.line_uses_op(1, "+",
        because="Build the second line with + too: 5 + 5 (number adding).")
    T.line_only_literals(1, {5},
        because="The second line adds the NUMBERS 5 and 5 -- nothing else.")
