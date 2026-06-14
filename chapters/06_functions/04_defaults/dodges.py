# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("*args with a manual fallback, dodging the default parameter",
     'def greet(name, *r):\n'
     '    g = r[0] if r else "Hello"\n'
     '    return "%s, %s!" % (g, name)\n'),
]
