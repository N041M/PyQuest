import json

from engine.inputs import Case, random_word, random_int


def cases():
    cs = [Case(args=({"a": 1, "b": 2},), expect='{"a": 1, "b": 2}'),
          Case(args=({},), expect="{}")]
    for _ in range(8):
        record = {}
        for _ in range(random_int(1, 4)):
            record[random_word(3, 6)] = random_int(-100, 100)
        cs.append(Case(args=(record,), expect=json.dumps(record)))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("to_json", *c.args), c.expect,
             because="to_json(%r) is the JSON string %r" % (c.args[0], c.expect))
    T.uses_import("json",
                  because="Serialize with json.dumps, not by gluing the string "
                          "together yourself.")
