DODGES = [
    ("sorts with a named key function instead of an inline lambda",
     "def _last(w):\n"
     "    return w[-1]\n"
     "def by_last(words):\n"
     "    return sorted(words, key=_last)\n"),
]
