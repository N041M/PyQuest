DODGES = [
    ("tallies by hand with get(k, 0) + 1, never using Counter",
     "def tally(items):\n"
     "    counts = {}\n"
     "    for x in items:\n"
     "        counts[x] = counts.get(x, 0) + 1\n"
     "    return counts\n"),
]
