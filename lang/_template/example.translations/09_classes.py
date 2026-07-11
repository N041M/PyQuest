# PyQuest translations -- language 'example' -- chapter 09_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"9.1 brief": r"""# 9.1 -- A first class

## Concept

A **class** is a blueprint for an object that bundles related data together. So
far a dog's name and age would be two loose variables; a class ties them into
one thing you can pass around.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

- `class Dog:` names the blueprint.
- `__init__` is the **constructor** -- it runs when you build a new Dog, and its
  job is to set up the object's data.
- `self` is the object being built; `self.name = name` stores the value **on the
  object** so it's still there later.

You build one (an *instance*) by calling the class like a function, and you read
its data with a dot:

```python
d = Dog("Rex", 3)
print(d.name)   # Rex
print(d.age)    # 3
```

## Your task

Define a class `Dog` whose `__init__` takes a `name` and an `age` and stores
each on the object as `self.name` and `self.age`.

## Done when

- `Dog("Rex", 3)` makes an object whose `.name` is `"Rex"` and `.age` is `3`.
- It works for any name and age.
- You used a `class` with an `__init__` that stores both values on `self`.
""",

"9.1 hints": r"""Start with `class Dog:` and give it an `__init__(self, name, age)` method.

---

Inside `__init__`, copy each parameter onto the object with `self.`:
`self.name = name`. That's what makes the value stick.

---

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
""",

"9.1 reference": r"""A **class** defines a new type of object, bundling related data into one value.
**`__init__`** is the initialiser: Python calls it automatically when you create
an instance, to set up its starting data.

- `class Point:` opens the definition; calling `Point(3, 4)` makes an
  **instance** and runs `__init__`.
- **`self`** is the instance being built; `self.x = x` stores a value as an
  **attribute** on it, where every method can later reach it.
- `__init__`'s first parameter is always `self`; the rest are the arguments the
  caller passes.

```python
class Point:
    def __init__(self, x, y):
        self.x = x          # store data on the instance
        self.y = y

p = Point(3, 4)
p.x                         # 3
```
""",

"9.2 brief": r"""# 9.2 -- Methods: behaviour on the data

## Concept

Objects don't just hold data -- they have **methods**, functions that live on
the object and work with its own data through `self`.

```python
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
```

`area` is a method: it takes `self` (the object it's called on) and uses
`self.side`. You call it with a dot and parentheses -- no need to pass `self`,
Python fills it in:

```python
s = Square(5)
print(s.area())   # 25
```

The point of a method is that the behaviour travels *with* the data: any Square
already knows how to compute its own area.

## Your task

Define a class `Square` whose `__init__` stores a `side`, and add a method
`area()` that returns the square's area (`side * side`).

## Done when

- `Square(5).area()` returns `25`.
- It works for any side length, including `0`.
- `area` is a method on the class and computes from `self.side`.
""",

"9.2 hints": r"""Store the side in `__init__` like last time, then add a second method `area`.

---

A method takes `self` first: `def area(self):`. Inside, return
`self.side * self.side`.

---

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
""",

"9.2 reference": r"""A **method** is a function defined inside a class. It always takes **`self`**
first and computes from the object's own attributes, so behaviour lives with the
data it acts on.

- Call it with `instance.method()`; Python passes the instance as `self`
  automatically, so `p.dist()` calls `dist(p)`.
- Inside, reach the object's data through `self`: `self.x`, `self.y`.
- A method may take more parameters after `self` and `return` a value like any
  function.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

Point(3, 4).dist()      # 5.0
```
""",

"9.3 brief": r"""# 9.3 -- State that remembers

## Concept

An object's data lives **between** method calls -- a method can change `self`,
and the next call sees the change. That's what makes objects useful: they
*remember*.

```python
class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count = self.count + 1
        return self.count
```

Each `tick()` bumps `self.count` and hands back the new value:

```python
c = Counter()
c.tick()   # 1
c.tick()   # 2
c.tick()   # 3
```

Crucially, the count lives **on the instance** (`self.count`), so two counters
keep separate tallies -- ticking one never touches the other.

## Your task

Define a class `Counter` that starts its `count` at `0`. Add a method `tick()`
that adds one to the count and **returns the new count**.

## Done when

- A fresh `Counter` ticked three times returns `1`, `2`, `3`.
- Two counters are independent -- ticking one doesn't change the other.
- The count is stored on `self`, not shared across all counters.
""",

"9.3 hints": r"""`__init__` sets the starting point: `self.count = 0`. Then `tick` changes it.

---

Inside `tick`, do `self.count = self.count + 1` (or `self.count += 1`), then
`return self.count`. Keep the count on `self` so each counter has its own.

---

class Counter:
    def __init__(self):
        self.count = 0

    def tick(self):
        self.count += 1
        return self.count
""",

"9.3 reference": r"""An object holds **state** — data that persists between calls. A method can
**mutate** `self`, and the next method call sees the change, so the object
remembers what happened to it.

- `self.count += 1` updates an attribute in place; the new value lives on until
  changed again.
- This is the point of objects: they carry their data with them across calls,
  unlike a plain function whose locals vanish when it returns.
- Each instance has its **own** copy of the attributes, so two counters count
  independently.

```python
class Counter:
    def __init__(self):
        self.n = 0
    def tick(self):
        self.n += 1         # remembered for next time

c = Counter(); c.tick(); c.tick(); c.n   # 2
```
""",

"9.4 brief": r"""# 9.4 -- More data, more methods

## Concept

A class can hold several pieces of data and offer several methods over them.
Nothing new in the syntax -- just more of it:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
```

Both methods read the same stored data through `self`; each Rectangle answers
either question about itself:

```python
r = Rectangle(3, 4)
r.area()        # 12
r.perimeter()   # 14
```

## Your task

Define a class `Rectangle` whose `__init__` stores a `width` and a `height`,
with two methods: `area()` returns `width * height`, and `perimeter()` returns
`2 * (width + height)`.

## Done when

- `Rectangle(3, 4).area()` is `12` and `.perimeter()` is `14`.
- Both work for any width and height.
- Both are methods on the class, computing from `self`.
""",

"9.4 hints": r"""Store both values in `__init__`: `self.width = width` and
`self.height = height`.

---

Add two methods. `area` returns `self.width * self.height`; `perimeter` returns
`2 * (self.width + self.height)`.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
""",

"9.4 reference": r"""A class can hold **several attributes** and offer **several methods** that work
together over them — modelling something with more than one property.

- `__init__` stores each piece of data (`self.width`, `self.height`); each method
  reads whatever attributes it needs.
- Methods can build on the same data for different answers: `area` multiplies,
  `perimeter` adds — one object, many questions.
- Keeping the data and the operations in one class means callers ask the object
  rather than juggling loose variables.

```python
class Rectangle:
    def __init__(self, w, h):
        self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

r = Rectangle(3, 4); r.area(), r.perimeter()   # (12, 14)
```
""",

"9.5 brief": r"""# 9.5 -- Printing an object: `__str__`

## Concept

Print an object as-is and you get something useless like
`<__main__.Point object at 0x10f3d2b80>`. To control how an object looks as
text, define the special method `__str__`, which returns the string Python
should show.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
```

`__str__` is a **dunder** (double-underscore) method -- Python calls it for you
whenever the object is turned into text, by `print()` or `str()`:

```python
p = Point(3, 4)
print(p)        # (3, 4)
str(p)          # "(3, 4)"
```

You never call `__str__` yourself; you just define it, and `str(p)` triggers it.

## Your task

Define a class `Point` storing `x` and `y`, with a `__str__` method so that
`str(Point(3, 4))` is exactly `"(3, 4)"` -- the two values in parentheses,
comma-and-space between them.

## Done when

- `str(Point(3, 4))` is `"(3, 4)"`.
- It works for any `x` and `y`, including negatives.
- The formatting comes from a `__str__` method on the class.
""",

"9.5 hints": r"""Store `x` and `y` in `__init__` as usual, then add a `__str__(self)` method.

---

`__str__` must **return** the text (not print it). Build it with an f-string:
`return f"({self.x}, {self.y})"`. Mind the comma and the space.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
""",

"9.5 reference": r"""**`__str__`** defines the human-readable text for an object. When you `print` an
instance or call `str()` on it, Python calls `__str__` and uses what it returns.

- Without it, printing an object shows an unhelpful default like
  `<Point object at 0x...>`; `__str__` replaces that with something meaningful.
- It must **return** a string (not print one), typically built with an f-string
  from the object's attributes.
- `__str__` is one of several **dunder** ("double-underscore") methods Python
  calls on your behalf, like `__init__`.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return f"({self.x}, {self.y})"

print(Point(3, 4))      # (3, 4)
```
""",

"9.6 brief": r"""# 9.6 -- A sensible default

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
""",

"9.6 hints": r"""Give `__init__` a parameter with a default: `def __init__(self,
greeting="Hello"):`, then store it on `self`.

---

`greet` builds the message: `return f"{self.greeting}, {name}!"`. The default
belongs in the signature, so don't write an `if greeting is None` instead.

---

class Greeter:
    def __init__(self, greeting="Hello"):
        self.greeting = greeting

    def greet(self, name):
        return f"{self.greeting}, {name}!"
""",

"9.6 reference": r"""`__init__` is an ordinary function, so its parameters can have **default
values** — letting an object be created with or without certain arguments.

- `def __init__(self, balance=0):` allows `Account()` (starts at 0) or
  `Account(100)` (starts at 100).
- The same rules apply: defaulted parameters follow non-defaulted ones, and a
  mutable default needs the `None` sentinel trick
  (`def __init__(self, items=None): self.items = items or []`).
- Defaults make the common case effortless while keeping the option open.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance

Account().balance        # 0
Account(100).balance     # 100
```
""",

"9.7 brief": r"""# 9.7 -- Objects working together

## Concept

A method can take **another object** as an argument and build a **new** object
as its result. This is how objects combine without losing their own identity.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

`add` reaches into `other` (another Vector) for its data, and **returns a brand
new `Vector`** -- it does not change `self` or `other`:

```python
a = Vector(1, 2)
b = Vector(3, 4)
c = a.add(b)      # Vector(4, 6)
a.x               # still 1 -- a is untouched
```

Building a `Vector(...)` *inside* `Vector`'s own method is normal: the class can
use itself.

## Your task

Define a class `Vector` storing `x` and `y`, with a method `add(other)` that
returns a **new** `Vector` whose coordinates are the two vectors' coordinates
added together. The originals must be left unchanged.

## Done when

- `Vector(1, 2).add(Vector(3, 4))` is a Vector with `.x == 4` and `.y == 6`.
- The two input vectors are unchanged afterwards.
- `add` returns a new `Vector` object (not a tuple), built inside the method.
""",

"9.7 hints": r"""Store `x` and `y` in `__init__`. The method takes the other vector:
`def add(self, other):`.

---

Read both vectors through the dot (`self.x`, `other.x`) and **return a new
Vector**: `return Vector(self.x + other.x, self.y + other.y)`. Don't assign back
onto `self`.

---

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)
""",

"9.7 reference": r"""Objects **collaborate**: a method can take **another object** of the same class
as a parameter, read its attributes, and **return a new** object holding the
result — leaving both inputs unchanged.

- `def add(self, other):` reaches `self.x` and `other.x`, then
  `return Vector(self.x + other.x, ...)`. Returning a fresh instance keeps the
  operands immutable.
- This is how value-like objects compose (points, vectors, money). Defining the
  dunder `__add__` would even let `a + b` call it.

```python
class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y
    def add(self, other):
        return Vector(self.x + other.x, self.y + other.y)

Vector(1, 2).add(Vector(3, 4)).x    # 4
```
""",

"9.8 brief": r"""# 9.8 -- Capstone: a bank account

## Concept

Time to put the chapter together: a class with state, several methods, a
sensible default, and a rule it enforces.

A `BankAccount` keeps a `balance`. You can deposit (it grows) and withdraw (it
shrinks) -- but a withdrawal that would overdraw the account must be **refused**,
leaving the balance untouched.

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
```

- `balance` defaults to `0`, so `BankAccount()` is an empty account.
- `deposit` and `withdraw` change the stored balance (state that persists).
- `withdraw` **returns `True`** when it succeeds and **`False`** when it refuses
  -- and on refusal the balance does not change.

```python
acc = BankAccount(100)
acc.deposit(50)       # balance 150
acc.withdraw(70)      # True,  balance 80
acc.withdraw(999)     # False, balance still 80
```

## Your task

Define `BankAccount` exactly as above: a `balance` that defaults to `0`, a
`deposit(amount)` method, and a `withdraw(amount)` method that subtracts and
returns `True` only when there's enough -- otherwise it changes nothing and
returns `False`.

## Done when

- `BankAccount()` starts at `0`; `BankAccount(100)` starts at `100`.
- `deposit` and `withdraw` update `balance`, and withdrawing too much returns
  `False` and leaves `balance` unchanged.
- Withdrawing exactly the balance is allowed.
""",

"9.8 hints": r"""`__init__(self, balance=0)` stores the starting balance. `deposit` just adds to
`self.balance`.

---

`withdraw` needs a guard: `if amount <= self.balance:` subtract and
`return True`; otherwise change nothing and `return False`.

---

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False
""",

"9.8 reference": r"""The capstone is a **stateful class** that puts the chapter together: a default in
`__init__`, methods that **mutate** state, a **guard** that raises on invalid
operations, and `__str__` for display.

- `__init__` sets the starting balance (with a default); `deposit` and `withdraw`
  change `self.balance` in place.
- A guard protects the invariant: `withdraw` checks funds and
  `raise ValueError(...)` rather than allowing an impossible state.
- `__str__` renders the object for printing. Together these make an object that
  is reliable to use and pleasant to read.

```python
class Account:
    def __init__(self, balance=0):
        self.balance = balance
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"balance: {self.balance}"
```
""",
}
