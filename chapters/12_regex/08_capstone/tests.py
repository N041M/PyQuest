from engine.inputs import Case, random_word, random_int


def _make_config():
    n = random_int(0, 4)
    keys = []
    while len(keys) < n:
        k = random_word(2, 5)
        if k not in keys:
            keys.append(k)
    pairs = [(k, random_word(2, 5)) for k in keys]
    text = " ".join("%s=%s" % kv for kv in pairs)
    return text, dict(pairs)


def cases():
    cs = [Case(args=("host=local port=8080",),
               expect={"host": "local", "port": "8080"}),
          Case(args=("debug=on",), expect={"debug": "on"}),
          Case(args=("",), expect={})]
    for _ in range(8):
        text, expected = _make_config()
        cs.append(Case(args=(text,), expect=expected))
    return cs


def check(T):
    for c in cases():
        T.eq(T.call("parse_config", *c.args), c.expect,
             because="parse_config(%r) -> %r" % (c.args[0], c.expect))
    T.uses_import("re",
                  because="Extract the pairs with one (\\w+)=(\\w+) pattern via "
                          "re.findall, not by splitting the string by hand.")
    T.uses_call("findall",
                because="The lesson is a multi-group findall -- use it to capture "
                        "every key=value pair.")
