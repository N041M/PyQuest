DODGES = [
    ("rearranges split pieces by hand, never importing datetime",
     "def pretty(text):\n"
     "    y, m, d = text.split('-')\n"
     "    return '%s/%s/%s' % (d, m, y)\n"),
]
