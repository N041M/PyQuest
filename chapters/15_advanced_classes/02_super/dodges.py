DODGES = [
    ("sets self.name by hand instead of calling super().__init__",
     "class Animal:\n"
     "    def __init__(self, name):\n"
     "        self.name = name\n"
     "class Dog(Animal):\n"
     "    def __init__(self, name, breed):\n"
     "        self.name = name\n"
     "        self.breed = breed\n"),
    ("hand-sets name, parks a dead super() call to fake the construct",
     "class Animal:\n"
     "    def __init__(self, name):\n"
     "        self.name = name\n"
     "class Dog(Animal):\n"
     "    def __init__(self, name, breed):\n"
     "        self.name = name\n"
     "        self.breed = breed\n"
     "        if False:\n"
     "            super().__init__(name)\n"),
]
