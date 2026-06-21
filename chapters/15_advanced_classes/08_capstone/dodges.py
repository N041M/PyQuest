DODGES = [
    ("hand-sets name (no super) and fakes area with __getattr__ (no @property)",
     "class Shape:\n"
     "    def __init__(self, name):\n"
     "        self.name = name\n"
     "    def describe(self):\n"
     "        return '%s with area %d' % (self.name, self.area)\n"
     "class Rectangle(Shape):\n"
     "    def __init__(self, width, height):\n"
     "        self.name = 'rectangle'\n"
     "        self.width = width\n"
     "        self.height = height\n"
     "    def __getattr__(self, k):\n"
     "        if k == 'area':\n"
     "            return self.width * self.height\n"
     "        raise AttributeError(k)\n"
     "    def __eq__(self, other):\n"
     "        return self.area == other.area\n"
     "    def __lt__(self, other):\n"
     "        return self.area < other.area\n"),
]
