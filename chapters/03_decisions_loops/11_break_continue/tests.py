from engine.inputs import random_word


def expected(s):
    out = []
    for ch in s:
        if ch == "x":
            break
        if ch == "o":
            continue
        out.append(ch)
    return "\n".join(out)


def check(T):
    T.eq(T.run(stdin="boxes\n"), "b", because="b, skip o, stop at x.")
    T.eq(T.run(stdin="good\n"), "g\nd", because="The two o's are skipped.")
    T.eq(T.run(stdin="abc\n"), "a\nb\nc", because="No o or x here.")
    T.eq(T.run(stdin="xyz\n"), "", because="x first -> stop immediately.")
    for _ in range(8):
        w = random_word(1, 12)
        T.eq(T.run(stdin=w + "\n"), expected(w),
             because="skip 'o', stop at 'x' for %r." % w)
    T.uses_break(because="Use break to stop at 'x'.")
    T.uses_continue(because="Use continue to skip 'o'.")
