# Puzzle 11.4 -- random: reproducible chance
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: define shuffled(items, seed) that RETURNS a new shuffled list,
#       made repeatable by seeding random with `seed` before shuffling.
#       Leave the original `items` unchanged.
#
#     shuffled([1, 2, 3], 7)  -> always the same order for seed 7
#
# Make a copy first, seed, then shuffle the copy in place.

# TODO: your code here
