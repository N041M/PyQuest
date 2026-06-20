DODGES = [
    ("returns a nested def instead of a lambda",
     "def multiplier(n):\n"
     "    def f(x):\n"
     "        return x * n\n"
     "    return f\n"),
]
