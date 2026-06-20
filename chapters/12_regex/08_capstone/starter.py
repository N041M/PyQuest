# Puzzle 12.8 -- Capstone: parse key=value config
# Read this puzzle's brief.md first (its path is shown by `start`).
#
# TASK: define parse_config(text) that parses space-separated key=value pairs
#       into a dict, using re.findall with two capture groups.
#
#     parse_config("host=local port=8080") -> {"host": "local", "port": "8080"}
#     parse_config("")                     -> {}
#
# A two-group pattern gives findall a list of (key, value) tuples; dict() does
# the rest.

# TODO: your code here
