from engine.inputs import random_word, random_int


def expected(players):
    ranked = sorted(players, key=lambda p: (-p[1], p[0]))
    lines = ["%s - %d" % (name, score) for name, score in ranked]
    total = sum(score for _, score in players)
    lines.append("Total: %d" % total)
    return "\n".join(lines)


def run_with(T, players):
    text = "".join("%s %d\n" % (name, score) for name, score in players)
    T.run(files={"scores.txt": text})
    return T.file("ranking.txt")


def check(T):
    players = [("alice", 40), ("bob", 25), ("cara", 40)]
    T.eq(run_with(T, players), expected(players),
         because="Ranked high-to-low, ties alphabetical, then the total.")

    T.eq(run_with(T, [("solo", 7)]), "solo - 7\nTotal: 7",
         because="One player, then the Total line.")

    for _ in range(8):
        n = random_int(1, 6)
        names = set()
        while len(names) < n:
            names.add(random_word(3, 7))
        players = [(name, random_int(0, 99)) for name in names]
        T.eq(run_with(T, players), expected(players),
             because="Ranking report for %r." % players)
    T.uses_with_open(because="Open both files with `with open(...) as f:`.")
