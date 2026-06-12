def check(T):
    out = T.run()
    T.eq(out, "3.5\n3\n1",
         because="7/2 is 3.5, 7//2 is 3, 7%2 is 1.")
    # must use the three division operators, not type the answers.
    T.uses_op("/", because="Use / for the 3.5 -- don't type the answers.")
    T.uses_op("//", because="Use // for the 3.")
    T.uses_op("%", because="Use % for the remainder 1.")
