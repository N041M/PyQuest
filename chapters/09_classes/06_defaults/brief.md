# 9.6 -- A sensible default

## Concept

A constructor is just a function, so it can take **default parameters** (6.4),
too. That lets a caller leave out what they don't care about and still get a
working object.

```python
class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
```

If you don't pass a greeting, you get `"Hello"`; if you do, it's used instead:

```python
Greeter().greet("Ada")        # "Hello, Ada!"
Greeter("Hi").greet("Bo")     # "Hi, Bo!"
```

The default lives in `__init__`'s signature (`greeting="Hello"`), so the object
is configured once at construction and every `greet` reuses it.

## Your task

Define a class `Greeter` whose `__init__` takes a `greeting` that **defaults to
`"Hello"`** and stores it. Add a method `greet(name)` that returns
`"{greeting}, {name}!"`.

## Done when

- `Greeter().greet("Ada")` is `"Hello, Ada!"` (default used).
- `Greeter("Hi").greet("Bo")` is `"Hi, Bo!"` (default overridden).
- The default is a default *parameter* of `__init__`, not an `if` inside it.
