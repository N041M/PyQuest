DODGES = [
    ("splits on spaces and '=' by hand, never importing re",
     "def parse_config(text):\n"
     "    result = {}\n"
     "    for pair in text.split():\n"
     "        if '=' in pair:\n"
     "            k, v = pair.split('=', 1)\n"
     "            result[k] = v\n"
     "    return result\n"),
]
