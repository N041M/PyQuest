DODGES = [
    ("splits on '-' instead of using capture groups",
     "def parse_date(text):\n"
     "    y, mo, d = text.split('-')\n"
     "    return (int(y), int(mo), int(d))\n"),
]
