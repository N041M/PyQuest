# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("a plain function is not a class with a method",
     "def Square(side):\n"
     "    return side\n"),
    ("type()-built class skips the `class` syntax lesson",
     "Square = type('Square', (), {\n"
     "    '__init__': lambda self, side: setattr(self, 'side', side),\n"
     "    'area': lambda self: self.side * self.side,\n"
     "})\n"),
]
