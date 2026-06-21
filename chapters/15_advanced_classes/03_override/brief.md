# 15.3 -- Overriding: a child's own version

## Concept

A subclass can **override** a parent method -- define its own version of a method
the parent already has. For the subclass's instances, the new version wins:

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."          # generic

class Cat(Animal):
    def speak(self):
        return "Meow"         # Cat's own
```

- `Cat("Felix").speak()` returns `"Meow"`; a plain `Animal(...).speak()` still
  returns `"..."`.
- This is **polymorphism**: the *same* call, `x.speak()`, does the right thing for
  whatever type `x` is.
- The subclass still inherits everything it doesn't override (here, `__init__` and
  `self.name`).

## Your task

Define `Animal` with `__init__(self, name)` and `speak(self)` returning `"..."`.
Then define `Cat(Animal)` that **overrides** `speak` to return `"Meow"`.

## Done when

- `Cat("Felix").speak()` returns `"Meow"`.
- `Animal("thing").speak()` returns `"..."` (unchanged).
- `Cat("Felix").name` is `"Felix"` (inherited `__init__`), and a Cat is an Animal.
