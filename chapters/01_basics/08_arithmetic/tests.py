def check(T):
    out = T.run()
    T.eq(out, "14\n20",
         because="2 + 3 * 4 is 14; (2 + 3) * 4 is 20.")
    # the lesson is precedence with THESE numbers: both lines compute from
    # 2, 3 and 4 with + and *, and only the parentheses differ. Computing the
    # constants any other way (7*2, 10+10, a variable...) dodges the point.
    T.line_uses_op(0, "+",
        because="The first line is 2 + 3 * 4 -- use + in it.")
    T.line_shape(0, "+", "*",
        because="First line: NO parentheses, so * runs before + (2 + 3 * 4).")
    T.line_only_literals(0, {2, 3, 4},
        because="Build the first line from 2, 3 and 4 only.")
    T.line_shape(1, "*", "+",
        because="Second line: parentheses make + run first ((2 + 3) * 4).")
    T.line_only_literals(1, {2, 3, 4},
        because="Build the second line from the SAME numbers 2, 3 and 4.")
