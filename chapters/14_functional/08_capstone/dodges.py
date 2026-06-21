DODGES = [
    ("filters and maps with comprehensions instead of filter/map",
     "def passing(records, threshold):\n"
     "    qualified = [r for r in records if r[1] >= threshold]\n"
     "    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)\n"
     "    return [r[0] for r in ranked]\n"),
    ("named functions + comprehension map, decoy lambda satisfies uses_lambda",
     "def passing(records, threshold):\n"
     "    def keep(r):\n"
     "        return r[1] >= threshold\n"
     "    def score(r):\n"
     "        return r[1]\n"
     "    qualified = filter(keep, records)\n"
     "    ranked = sorted(qualified, key=score, reverse=True)\n"
     "    return [r[0] for r in ranked]\n"
     "_decoy = lambda: 0\n"),
]
