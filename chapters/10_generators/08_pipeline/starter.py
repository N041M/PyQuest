# Puzzle 10.8 -- Capstone: a streaming pipeline
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: define THREE generators that compose into a pipeline:
#
#   numbers(n)        -> yields 0, 1, ..., n-1   (n <= 0 yields nothing)
#   keep_even(stream) -> yields only the even numbers from stream
#   labelled(stream)  -> yields "#x" for each x in stream
#
#   list(labelled(keep_even(numbers(6)))) -> ["#0", "#2", "#4"]
#
# Each uses yield. keep_even and labelled must work on ANY iterable (a list, or
# another generator), so the three can be chained.
#
# Write your code in this file, save it, then run:  check

# TODO: your code here
