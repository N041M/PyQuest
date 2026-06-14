# Known sidesteps that must FAIL this puzzle's tests, forever (see audit.py).
DODGES = [
    ("*args + an if reaches the same result but skips the default parameter",
     "class Greeter:\n"
     "    def __init__(self, *args):\n"
     "        self.greeting = args[0] if args else 'Hello'\n"
     "    def greet(self, name):\n"
     "        return f'{self.greeting}, {name}!'\n"),
    ("required parameter -- Greeter() with no greeting then crashes",
     "class Greeter:\n"
     "    def __init__(self, greeting):\n"
     "        self.greeting = greeting\n"
     "    def greet(self, name):\n"
     "        return f'{self.greeting}, {name}!'\n"),
]
