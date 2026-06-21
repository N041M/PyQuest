DODGES = [
    ("sorts with a named key function instead of an inline lambda",
     "def _last(w):\n"
     "    return w[-1]\n"
     "def by_last(words):\n"
     "    return sorted(words, key=_last)\n"),
    ("named key function does the work, decoy lambda satisfies uses_lambda",
     "def _last(w):\n"
     "    return w[-1]\n"
     "def by_last(words):\n"
     "    return sorted(words, key=_last)\n"
     "_decoy = lambda: 0\n"),
]
