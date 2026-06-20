DODGES = [
    ("collapses digit runs with a hand loop, never importing re",
     "def redact(text):\n"
     "    out, prev = [], False\n"
     "    for c in text:\n"
     "        if c.isdigit():\n"
     "            if not prev:\n"
     "                out.append('#')\n"
     "            prev = True\n"
     "        else:\n"
     "            out.append(c)\n"
     "            prev = False\n"
     "    return ''.join(out)\n"),
]
