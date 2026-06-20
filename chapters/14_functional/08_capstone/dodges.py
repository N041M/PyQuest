DODGES = [
    ("filters and maps with comprehensions instead of filter/map",
     "def passing(records, threshold):\n"
     "    qualified = [r for r in records if r[1] >= threshold]\n"
     "    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)\n"
     "    return [r[0] for r in ranked]\n"),
]
