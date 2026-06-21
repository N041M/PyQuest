DODGES = [
    ("Dog subclasses Animal but copies (redefines) describe instead of "
     "inheriting it",
     "class Animal:\n"
     "    def __init__(self, name):\n"
     "        self.name = name\n"
     "    def describe(self):\n"
     "        return self.name + ' the animal'\n"
     "class Dog(Animal):\n"
     "    def describe(self):\n"
     "        return self.name + ' the animal'\n"
     "    def speak(self):\n"
     "        return 'Woof'\n"),
]
