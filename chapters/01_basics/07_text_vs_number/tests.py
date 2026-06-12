def check(T):
    out = T.run()
    T.eq(out, "55\n10",
         because="Line 1 joins text \"5\"+\"5\" = 55; line 2 adds 5+5 = 10.")
    # both lines must use + (concatenation, then addition) -- not multiplication
    # or a typed-in answer.
    T.uses_op("+", min_count=2,
        because="Build each line with +: \"5\" + \"5\" and 5 + 5 -- not "
                "multiplication, and not the answer typed in.")
