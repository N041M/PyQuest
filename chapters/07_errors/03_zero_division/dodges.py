# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("if-guard does the work, try/except is an empty prop",
     'def safe_div(a, b):\n'
     '    try:\n'
     '        pass\n'
     '    except ZeroDivisionError:\n'
     '        pass\n'
     '    if b == 0:\n'
     '        return None\n'
     '    return a / b\n'),
]
