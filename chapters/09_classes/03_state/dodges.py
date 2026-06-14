# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("a class-level count is shared, so counters collide",
     "class Counter:\n"
     "    count = 0\n"
     "    def tick(self):\n"
     "        Counter.count += 1\n"
     "        return Counter.count\n"),
    ("a module global isn't per-instance state (and isn't a class)",
     "_count = 0\n"
     "def Counter():\n"
     "    return None\n"),
]
