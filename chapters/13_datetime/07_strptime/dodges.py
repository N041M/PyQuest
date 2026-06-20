DODGES = [
    ("slices the hour out of the string, never importing datetime",
     "def hour_of(text):\n"
     "    return int(text.split()[1].split(':')[0])\n"),
]
