# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
# OOP puzzles are validated through make/method/attr (not the tape), so the
# generic adversaries don't apply -- these pin the lesson by hand: it must be a
# real `class`, not a look-alike built another way.
DODGES = [
    ("a namedtuple is not a class definition",
     "from collections import namedtuple\n"
     "Dog = namedtuple('Dog', ['name', 'age'])\n"),
    ("a factory function returning an object is not a class",
     "from types import SimpleNamespace\n"
     "def Dog(name, age):\n"
     "    return SimpleNamespace(name=name, age=age)\n"),
    ("type() builds a class object but skips the `class` syntax lesson",
     "Dog = type('Dog', (), {})\n"
     "def _init(self, name, age):\n"
     "    self.name = name\n"
     "    self.age = age\n"
     "Dog.__init__ = _init\n"),
    ("a decoy class beside a namedtuple -- the named check must see `class Dog`",
     "class _Decoy:\n"
     "    pass\n"
     "from collections import namedtuple\n"
     "Dog = namedtuple('Dog', ['name', 'age'])\n"),
]

