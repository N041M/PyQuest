DODGES = [
    ("collects digit runs by hand, never importing re",
     "def all_numbers(text):\n"
     "    out, cur = [], ''\n"
     "    for c in text:\n"
     "        if c.isdigit():\n"
     "            cur += c\n"
     "        elif cur:\n"
     "            out.append(cur)\n"
     "            cur = ''\n"
     "    if cur:\n"
     "        out.append(cur)\n"
     "    return out\n"),
]
