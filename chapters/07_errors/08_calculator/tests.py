from engine.inputs import random_word, random_int

OPS = "+-*/"


def expected(a, op, b):
    try:
        a, b = int(a), int(b)
    except ValueError:
        return "bad number"
    if op == "+":
        return "%d" % (a + b)
    if op == "-":
        return "%d" % (a - b)
    if op == "*":
        return "%d" % (a * b)
    if op == "/":
        if b == 0:
            return "cannot divide"
        return "%s" % (a / b)
    return "unknown op"


def run_case(T, a, op, b):
    line = "%s %s %s" % (a, op, b)
    T.eq(T.run(stdin=line + "\n"), expected(a, op, b),
         because="For the line %r." % line)


def check(T):
    run_case(T, "8", "+", "5")
    run_case(T, "9", "/", "2")
    run_case(T, "3", "*", "-2")
    run_case(T, "9", "/", "0")
    run_case(T, "two", "*", "3")
    run_case(T, "8", "?", "5")
    for _ in range(10):
        op = OPS[random_int(0, 3)] if random_int(0, 3) else "?"
        if op == "?":
            # keep the numbers valid: checking the op before or after the
            # conversions are both reasonable programs, so never combine an
            # unknown op with a bad number in one line.
            a, b = "%d" % random_int(-30, 30), "%d" % random_int(-5, 5)
        else:
            a = ("%d" % random_int(-30, 30) if random_int(0, 3)
                 else random_word(2, 4))
            b = ("%d" % random_int(-5, 5) if random_int(0, 3)
                 else random_word(2, 4))
        run_case(T, a, op, b)
    T.uses_try(because="Every failure is handled by an except block.")
