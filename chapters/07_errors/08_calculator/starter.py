# Puzzle 7.8 -- Capstone: a robust calculator
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: read one line "<number> <op> <number>" and print the result.
#   + - *  -> whole-number result      /  -> float result
#   bad number parts  -> "bad number"
#   division by zero  -> "cannot divide"
#   any other op      -> "unknown op"
#
#     "8 + 5" -> 13      "9 / 0"   -> cannot divide
#     "9 / 2" -> 4.5     "two * 3" -> bad number
#                        "8 ? 5"   -> unknown op
#
# One try, two excepts (ValueError, ZeroDivisionError), an elif chain for ops.
#
# Write your code in this file, save it, then run:  check

# TODO: your code here
