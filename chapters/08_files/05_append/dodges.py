# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# This puzzle's lesson is behavioral: "a" appends without first reading. The
# randomized existing content makes truncation observable, and the absent-file
# case makes "read it first, then rewrite with 'w'" crash -- so a solution must
# genuinely append rather than re-read and overwrite.
DODGES = [
    ("\"w\" wipes the existing log before writing",
     'entry = input()\n'
     'with open("log.txt", "w") as f:\n'
     '    f.write(entry + "\\n")\n'),
    ("read the whole file then rewrite with \"w\" -- crashes when absent",
     'entry = input()\n'
     'with open("log.txt") as f:\n'
     '    old = f.read()\n'
     'with open("log.txt", "w") as f:\n'
     '    f.write(old + entry + "\\n")\n'),
    ("ignores the file entirely, prints instead",
     'print(input())\n'),
]
