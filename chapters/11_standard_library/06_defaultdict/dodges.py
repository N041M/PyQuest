DODGES = [
    ("groups with setdefault, never using defaultdict",
     "def group_by_length(words):\n"
     "    groups = {}\n"
     "    for w in words:\n"
     "        groups.setdefault(len(w), []).append(w)\n"
     "    return groups\n"),
]
