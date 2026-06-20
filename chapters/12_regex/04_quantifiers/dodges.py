DODGES = [
    ("collects letter runs by hand, never importing re",
     "def find_words(text):\n"
     "    out, cur = [], ''\n"
     "    for c in text:\n"
     "        if c.isalpha():\n"
     "            cur += c\n"
     "        elif cur:\n"
     "            out.append(cur)\n"
     "            cur = ''\n"
     "    if cur:\n"
     "        out.append(cur)\n"
     "    return out\n"),
]
