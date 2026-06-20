DODGES = [
    ("splits the string by hand, never parsing into a date",
     "def parts(text):\n"
     "    y, m, d = text.split('-')\n"
     "    return (int(y), int(m), int(d))\n"),
]
