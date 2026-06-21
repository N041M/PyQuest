DODGES = [
    ("uses @staticmethod returning Point(...) instead of a classmethod with cls",
     "class Point:\n"
     "    def __init__(self, x, y):\n"
     "        self.x = x\n"
     "        self.y = y\n"
     "    @staticmethod\n"
     "    def from_tuple(pair):\n"
     "        return Point(pair[0], pair[1])\n"),
    ("classmethod but hardcodes Point(...) instead of cls(...)",
     "class Point:\n"
     "    def __init__(self, x, y):\n"
     "        self.x = x\n"
     "        self.y = y\n"
     "    @classmethod\n"
     "    def from_tuple(cls, pair):\n"
     "        return Point(pair[0], pair[1])\n"),
]
