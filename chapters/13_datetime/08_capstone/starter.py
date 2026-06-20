# Puzzle 13.8 -- Capstone: shift a timestamp
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: define add_hours(timestamp, hours) that takes "YYYY-MM-DD HH:MM" and an
#       int hours (may be negative), and RETURNS the timestamp shifted by that
#       many hours, in the same format.
#
#     add_hours("2026-06-20 23:30", 2)  -> "2026-06-21 01:30"
#     add_hours("2026-01-01 00:30", -1) -> "2025-12-31 23:30"
#
# strptime to parse, timedelta(hours=...) to shift, strftime to format.

# TODO: your code here
