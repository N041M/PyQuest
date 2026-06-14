# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("mutates self instead of returning a new vector",
     "class Vector:\n"
     "    def __init__(self, x, y):\n"
     "        self.x = x\n"
     "        self.y = y\n"
     "    def add(self, other):\n"
     "        self.x += other.x\n"
     "        self.y += other.y\n"
     "        return self\n"),
    ("returns a tuple, not a Vector (no .x / .y)",
     "class Vector:\n"
     "    def __init__(self, x, y):\n"
     "        self.x = x\n"
     "        self.y = y\n"
     "    def add(self, other):\n"
     "        return (self.x + other.x, self.y + other.y)\n"),
]
