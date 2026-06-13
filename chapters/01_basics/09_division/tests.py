def check(T):
    out = T.run()
    T.eq(out, "3.5\n3\n1",
         because="7/2 is 3.5, 7//2 is 3, 7%2 is 1.")
    # the lesson is the same pair of numbers through three operators -- each
    # line must compute from 7 and 2 with its own operator, not be typed in.
    T.line_uses_op(0, "/", because="Line 1 divides: 7 / 2.")
    T.line_only_literals(0, {7, 2},
        because="Build line 1 from 7 and 2 only.")
    T.line_uses_op(1, "//", because="Line 2 floor-divides: 7 // 2.")
    T.line_only_literals(1, {7, 2},
        because="Build line 2 from the same 7 and 2.")
    T.line_uses_op(2, "%", because="Line 3 takes the remainder: 7 % 2.")
    T.line_only_literals(2, {7, 2},
        because="Build line 3 from the same 7 and 2.")
