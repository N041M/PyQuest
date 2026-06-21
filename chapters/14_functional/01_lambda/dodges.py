DODGES = [
    ("returns a nested def instead of a lambda",
     "def multiplier(n):\n"
     "    def f(x):\n"
     "        return x * n\n"
     "    return f\n"),
    ("nested def for the real work, decoy lambda to satisfy uses_lambda",
     "def multiplier(n):\n"
     "    def f(x):\n"
     "        return x * n\n"
     "    return f\n"
     "_decoy = lambda: 0\n"),
]
