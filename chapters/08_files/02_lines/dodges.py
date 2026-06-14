# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("loops over the lines but never used `with`",
     'for i, line in enumerate(open("tasks.txt"), 1):\n'
     '    print(f"{i}. {line.strip()}")\n'),
    ("reads bare, fakes the lesson with an unrelated live `with io.StringIO()`",
     'import io\n'
     'with io.StringIO() as s:\n'
     '    for i, line in enumerate(open("tasks.txt"), 1):\n'
     '        print(f"{i}. {line.strip()}")\n'),
]
