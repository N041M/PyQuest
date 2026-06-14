# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# Accepted alternative (NOT a dodge): defining __repr__ instead of __str__ also
# passes -- str() falls back to __repr__, and it's a real display dunder, so the
# lesson (a dunder controls how the object prints) still lands.
DODGES = [
    ("a normal method named show() is not what str() calls",
     "class Point:\n"
     "    def __init__(self, x, y):\n"
     "        self.x = x\n"
     "        self.y = y\n"
     "    def show(self):\n"
     "        return f'({self.x}, {self.y})'\n"),
    ("a formatting function instead of a class",
     "def Point(x, y):\n"
     "    return f'({x}, {y})'\n"),
]
