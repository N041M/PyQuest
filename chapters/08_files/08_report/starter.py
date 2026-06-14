# Puzzle 8.8 -- Capstone: a ranking report
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: read scores.txt ("name score" per line). Write ranking.txt with one
#   "name - score" line per player, highest score first (ties alphabetical),
#   then a final "Total: <sum>" line.
#
#     scores.txt = alice 40 / bob 25 / cara 40
#       -> ranking.txt = "alice - 40" / "cara - 40" / "bob - 25" / "Total: 105"
#
# Shape: read lines; name, score = line.split(); int(score); sort by
#        key=lambda p: (-score, name); write each line, then the Total.
#
# Write your code in this file, save it, then run:  check

# TODO: your code here
