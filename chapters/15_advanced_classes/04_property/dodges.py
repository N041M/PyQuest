DODGES = [
    ("recomputes area via __getattr__ instead of a @property",
     "class Rectangle:\n"
     "    def __init__(self, width, height):\n"
     "        self.width = width\n"
     "        self.height = height\n"
     "    def __getattr__(self, k):\n"
     "        if k == 'area':\n"
     "            return self.width * self.height\n"
     "        raise AttributeError(k)\n"),
]
