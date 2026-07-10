# PyQuest translations -- language 'pt' -- chapter 15_advanced_classes -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"15.1 brief": r"""# 15.1 -- Inheritance: build on a base class

## Concept

Chapter 9 built single classes. **Inheritance** lets one class build on another:
a **subclass** automatically gets the **base class's** methods, then adds or
changes its own.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return self.name + " the animal"

class Dog(Animal):           # Dog IS an Animal
    def speak(self):
        return "Woof"
```

- `class Dog(Animal):` makes `Dog` a subclass of `Animal`. A `Dog` instance can
  call `describe()` -- inherited from `Animal` -- *and* `speak()`, its own.
- The relationship is "**is-a**": a `Dog` **is an** `Animal`, so
  `isinstance(dog, Animal)` is `True`.
- Shared behaviour lives once in the base; subclasses don't repeat it.

## Your task

Define a base class `Animal` with an `__init__(self, name)` and a
`describe(self)` returning `"<name> the animal"`. Then define `Dog(Animal)` that
**inherits** from it and adds `speak(self)` returning `"Woof"`.

## Done when

- `Dog("Rex").describe()` returns `"Rex the animal"` (inherited).
- `Dog("Rex").speak()` returns `"Woof"`.
- A `Dog` **is an** `Animal`: it inherits rather than copying `describe`.
""",

"15.1 hints": r"""Write `Animal` first, with `__init__` storing `self.name` and `describe`
returning the sentence. Then `class Dog(Animal):` -- the `(Animal)` is what makes
Dog inherit.

---

Inside `Dog` you only write `speak`; `describe` comes for free from `Animal`.
Don't redefine `describe` in `Dog`.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return self.name + " the animal"


class Dog(Animal):
    def speak(self):
        return "Woof"
""",

"15.1 reference": r"""**Inheritance** lets a class build on another. Writing `class Child(Parent):`
makes `Child` a **subclass**: it automatically has all of `Parent`'s methods, and
can add new ones or replace existing ones.

- The relationship is **"is-a"**: a `Dog(Animal)` *is an* `Animal`, so
  `isinstance(dog, Animal)` is `True` and a `Dog` works anywhere an `Animal` is
  expected.
- Shared behaviour lives **once** in the base class; subclasses inherit it rather
  than copying it, so a fix in the parent reaches every child.
- Python finds a method by walking the **MRO** (method resolution order): the
  instance's class first, then its bases. `object` is the implicit base of every
  class.

```python
class Animal:
    def __init__(self, name): self.name = name
    def describe(self): return self.name + " the animal"

class Dog(Animal):
    def speak(self): return "Woof"

d = Dog("Rex")
d.describe()              # 'Rex the animal'  -- inherited
isinstance(d, Animal)    # True
```
""",

"15.2 brief": r"""# 15.2 -- super(): extend the parent

## Concept

A subclass often needs everything the parent's `__init__` does **plus** a bit
more. **`super()`** gives you the parent, so you call its method and then add to
it -- rather than copying the parent's code:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # run Animal's __init__ (sets self.name)
        self.breed = breed         # then add Dog's own attribute
```

- `super().__init__(name)` calls the **parent's** `__init__` on this instance, so
  `self.name` gets set by `Animal`.
- After that, the child adds what's special to it (`self.breed`).
- This keeps the parent's set-up in one place; if `Animal.__init__` changes, `Dog`
  picks it up automatically.

## Your task

Define `Animal` with `__init__(self, name)` storing `self.name`. Then define
`Dog(Animal)` whose `__init__(self, name, breed)` calls **`super().__init__(name)`**
and then stores `self.breed`.

## Done when

- `Dog("Rex", "Lab").name` is `"Rex"` (set via `super().__init__`).
- `Dog("Rex", "Lab").breed` is `"Lab"`.
- A `Dog` is an `Animal`, and the name is set by the parent, not re-assigned by
  hand.
""",

"15.2 hints": r"""`Dog` takes two arguments. The first, `name`, belongs to `Animal` -- hand it up
with `super().__init__(name)`.

---

After the `super().__init__(name)` line, set `self.breed = breed` for Dog's own
part.

---

class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
""",

"15.2 reference": r"""**`super()`** returns a proxy to the **parent class**, so a subclass can call the
parent's method and build on it instead of duplicating its code. The usual case
is `__init__`:

- `super().__init__(args)` runs the parent's initialiser on this instance,
  setting up whatever the parent owns; the child then adds its own attributes.
- It keeps the parent's logic in **one place** — change `Animal.__init__` and
  every subclass that calls `super().__init__` inherits the change.
- `super()` works for any method, not just `__init__`: an overriding method can
  call `super().method()` to reuse the parent's version and extend it.
- With no `super().__init__`, the parent's initialiser does **not** run, so the
  attributes it would set are missing.

```python
class Animal:
    def __init__(self, name): self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)     # Animal sets self.name
        self.breed = breed         # Dog adds self.breed

Dog("Rex", "Lab").name             # 'Rex'
```
""",

"15.3 brief": r"""# 15.3 -- Overriding: a child's own version

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
""",

"15.3 hints": r"""Give `Animal` both `__init__` and `speak` (returning "..."). Then `Cat(Animal)`
defines its own `speak`.

---

Cat's `speak` simply returns "Meow". Don't redefine `__init__` in Cat -- it's
inherited.

---

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Cat(Animal):
    def speak(self):
        return "Meow"
""",

"15.3 reference": r"""**Overriding** is defining, in a subclass, a method the parent already has. For
the subclass's instances, Python finds the subclass's version first (it's earlier
in the MRO), so the child's behaviour replaces the parent's.

- This is **polymorphism**: one call site, `x.speak()`, runs the right code for
  whatever type `x` actually is — `Cat` says "Meow", a generic `Animal` says
  "...". Calling code needn't know the exact type.
- The subclass still **inherits** everything it does *not* override (here
  `__init__`).
- An override can reuse the parent's version with `super().method()` — extend
  rather than fully replace.

```python
class Animal:
    def speak(self): return "..."
class Cat(Animal):
    def speak(self): return "Meow"

for a in [Animal(), Cat()]:
    print(a.speak())     # '...' then 'Meow' -- same call, different result
```
""",

"15.4 brief": r"""# 15.4 -- @property: a computed attribute

## Concept

Sometimes a value is **derived** from others -- a rectangle's area from its width
and height. You could store it, but then it goes stale when width changes. A
**`@property`** computes it on every access, while still being read like a plain
attribute:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12   -- no parentheses, but the method runs
r.width = 5
r.area        # 20   -- recomputed from the new width
```

- `@property` above a method makes `obj.area` (no `()`) call that method and
  return its result.
- Because it runs each time, the value is always current -- unlike a value stored
  once in `__init__`.

## Your task

Define `Rectangle` with `__init__(self, width, height)` and an **`area`**
**property** that returns `width * height`.

## Done when

- `Rectangle(3, 4).area` is `12` (accessed with no parentheses).
- After `r = Rectangle(3, 4); r.width = 5`, `r.area` is `20` -- recomputed, not
  stored.
""",

"15.4 hints": r"""Write `area` as a normal method that returns `self.width * self.height`, then put
`@property` on the line directly above `def area`.

---

With `@property`, callers write `r.area` (no parentheses) and the method runs each
time, so it always reflects the current width and height.

---

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
""",

"15.4 reference": r"""**`@property`** is a decorator that turns a method into a **computed, read-only
attribute**. `obj.area` (no parentheses) runs the method and returns its result,
so a derived value is recomputed on every access and never goes stale.

- It hides the fact that work happens: callers use `obj.area`, not `obj.area()`,
  exactly as for a stored attribute — but the value always reflects the current
  state.
- A bare `@property` is read-only; assigning to it raises `AttributeError`. Add a
  matching `@area.setter` to allow assignment with validation.
- Prefer a property over a value stored in `__init__` whenever the value *depends*
  on other attributes that can change.

```python
class Rectangle:
    def __init__(self, w, h): self.width, self.height = w, h
    @property
    def area(self): return self.width * self.height

r = Rectangle(3, 4)
r.area        # 12
r.width = 5
r.area        # 20  -- recomputed
```
""",

"15.5 brief": r"""# 15.5 -- @classmethod: an alternative constructor

## Concept

A normal method takes `self` (an instance). A **`@classmethod`** takes **`cls`**
(the class itself), so it can build and return a **new instance** -- a handy way
to offer an alternative, named constructor:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])

p = Point.from_tuple((3, 4))     # called on the class, not an instance
p.x, p.y                          # (3, 4)
```

- `@classmethod` makes `cls` the first parameter -- the class the method is called
  on (`Point` here).
- `cls(...)` is the same as `Point(...)`, but using `cls` means subclasses get an
  instance of *their* type for free.
- You call it on the **class**: `Point.from_tuple(...)`.

## Your task

Define `Point` with `__init__(self, x, y)`, and a **classmethod** `from_tuple(cls,
pair)` that builds a `Point` from a `(x, y)` tuple.

## Done when

- `Point.from_tuple((3, 4)).x` is `3` and `.y` is `4`.
- `from_tuple` is a `@classmethod` taking `cls`, and builds the point with
  `cls(...)`.
""",

"15.5 hints": r"""Write `__init__` as usual. Then add a method decorated with `@classmethod` whose
first parameter is `cls`, not `self`.

---

Inside `from_tuple`, unpack the pair and build the object with `cls`:
`return cls(pair[0], pair[1])`.

---

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, pair):
        return cls(pair[0], pair[1])
""",

"15.5 reference": r"""A **`@classmethod`** is bound to the **class**, not an instance: its first
parameter is **`cls`** (the class itself) instead of `self`. Because it has the
class, it can build instances — the classic use is an **alternative constructor**.

- Call it on the class: `Point.from_tuple((3, 4))`. Python passes `Point` as
  `cls`.
- Building with `cls(...)` rather than the literal class name means a **subclass**
  that calls the inherited classmethod gets an instance of *itself*.
- Contrast with **`@staticmethod`**, which takes neither `self` nor `cls` — just a
  plain function namespaced under the class, used when the method needs no access
  to the instance or class.

```python
class Point:
    def __init__(self, x, y): self.x, self.y = x, y
    @classmethod
    def from_tuple(cls, pair): return cls(pair[0], pair[1])

Point.from_tuple((3, 4)).x     # 3
```
""",

"15.6 brief": r"""# 15.6 -- __eq__: value equality

## Concept

By default, `==` on objects asks "are these the **same object**?" -- so two
separately-built objects with identical data are *not* equal. The **`__eq__`**
dunder method changes that to **value equality**:

```python
class Money:
    def __init__(self, cents):
        self.cents = cents
    def __eq__(self, other):
        return self.cents == other.cents

Money(500) == Money(500)     # True   -- same value
Money(500) == Money(750)     # False
```

- Python calls `a.__eq__(b)` for `a == b`. You return whether they should count as
  equal -- usually by comparing the attributes that define the value.
- `!=` is handled for you (it's the negation of `__eq__`).
- (Defining `__eq__` is also what lets your objects be compared in tests, lists,
  and `in` checks by value.)

## Your task

Define `Money` with `__init__(self, cents)` and an **`__eq__`** so two `Money`
objects are equal exactly when their `cents` match.

## Done when

- `Money(500) == Money(500)` is `True`.
- `Money(500) == Money(750)` is `False`.
- Equality compares `cents`, not object identity.
""",

"15.6 hints": r"""Add a method `__eq__(self, other)` to Money. Python calls it for `==`.

---

Return the comparison of the values: `return self.cents == other.cents`.

---

class Money:
    def __init__(self, cents):
        self.cents = cents

    def __eq__(self, other):
        return self.cents == other.cents
""",

"15.6 reference": r"""By default, `==` between objects tests **identity** — whether they are the very
same object — so two independently built objects with identical data compare
unequal. Defining **`__eq__(self, other)`** redefines `==` as **value equality**.

- Python calls `a.__eq__(b)` to evaluate `a == b`; return whether they should
  count as equal, normally by comparing the defining attributes. `!=` follows
  automatically as its negation.
- Value equality is what makes objects work intuitively in `==` tests, in `list`
  membership (`in`), and when comparing results.
- If you define `__eq__`, the class becomes **unhashable** (its `__hash__` is set
  to `None`), so it can't go in a `set` or `dict` key until you also define
  `__hash__` — often `return hash(self.cents)`.

```python
class Money:
    def __init__(self, cents): self.cents = cents
    def __eq__(self, other): return self.cents == other.cents

Money(500) == Money(500)     # True
Money(500) == Money(750)     # False
```
""",

"15.7 brief": r"""# 15.7 -- __lt__: make objects sortable

## Concept

`sorted`, `min`, and `max` all order things using the **`<`** operator. By
default Python doesn't know how to compare two of your objects -- sorting them
raises `TypeError`. Define **`__lt__`** ("less than") and they become sortable:

```python
class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees
    def __lt__(self, other):
        return self.degrees < other.degrees

temps = [Temperature(30), Temperature(10), Temperature(20)]
sorted(temps)        # ordered 10, 20, 30 -- by degrees
```

- Python calls `a.__lt__(b)` for `a < b`. Return whether `a` should come **before**
  `b` -- usually by comparing the attribute you want to sort on.
- `sorted` only needs `<`, so `__lt__` alone makes a list of your objects
  sortable.

## Your task

Define `Temperature` with `__init__(self, degrees)` and an **`__lt__`** so
temperatures compare by `degrees`.

## Done when

- `Temperature(10) < Temperature(20)` is `True`.
- `sorted([Temperature(30), Temperature(10), Temperature(20)])` is ordered
  `10, 20, 30` by degrees.
- Comparison uses `degrees`.
""",

"15.7 hints": r"""Add `__lt__(self, other)` to Temperature. Python calls it for `<`, and `sorted`
uses `<`.

---

Return the comparison of the values: `return self.degrees < other.degrees`. That
single method is enough to make a list sortable.

---

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __lt__(self, other):
        return self.degrees < other.degrees
""",

"15.7 reference": r"""**`__lt__(self, other)`** defines the **`<`** operator for your objects, and `<` is
exactly what **`sorted`**, **`min`**, and **`max`** use to order things. Without
it, comparing two of your objects raises `TypeError`; with it, a list of them
sorts directly.

- Python calls `a.__lt__(b)` for `a < b`; return whether `a` should come **before**
  `b`, usually by comparing the attribute you sort on.
- `sorted` needs only `<`, so `__lt__` alone makes objects sortable. The full set
  of ordering dunders is `__lt__`, `__le__`, `__gt__`, `__ge__`.
- `functools.total_ordering` is a class decorator that fills in the other three
  from `__lt__` and `__eq__`, if you want all comparisons.

```python
class Temperature:
    def __init__(self, degrees): self.degrees = degrees
    def __lt__(self, other): return self.degrees < other.degrees

sorted([Temperature(30), Temperature(10), Temperature(20)])   # 10, 20, 30
min([Temperature(30), Temperature(10)]).degrees               # 10
```
""",

"15.8 brief": r"""# 15.8 -- Capstone: a shape hierarchy

## Concept

Pull the chapter together into one small hierarchy. A base `Shape` holds a name
and can describe itself; a `Rectangle` inherits from it, adds size, computes its
area as a property, and compares to other rectangles by area.

```python
class Shape:
    def __init__(self, name):
        self.name = name
    def describe(self):
        return "%s with area %d" % (self.name, self.area)   # uses the property

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height
    def __eq__(self, other):
        return self.area == other.area
    def __lt__(self, other):
        return self.area < other.area
```

Notice `Shape.describe` uses `self.area`, which only `Rectangle` defines -- the
base method works through the subclass's property (polymorphism).

## Your task

Build exactly the two classes above:

- `Shape.__init__(self, name)` and `describe(self)` -> `"<name> with area
  <area>"`.
- `Rectangle(Shape)`: `__init__(self, width, height)` sets the name to
  `"rectangle"` via `super()`, stores width/height; an `area` **property**; and
  `__eq__` / `__lt__` comparing by `area`.

## Done when

- `Rectangle(3, 4).area` is `12`; `.name` is `"rectangle"`; `.describe()` is
  `"rectangle with area 12"`; it is a `Shape`.
- `Rectangle(2, 6) == Rectangle(3, 4)` is `True` (equal areas).
- `sorted([Rectangle(3, 4), Rectangle(1, 1), Rectangle(2, 5)])` is ordered by
  area (1, 10, 12).
""",

"15.8 hints": r"""Start with `Shape`: `__init__(self, name)` and `describe` returning
`"%s with area %d" % (self.name, self.area)`. It refers to `self.area`, which the
subclass will provide.

---

`Rectangle(Shape)`: in `__init__` call `super().__init__("rectangle")`, store
width/height; add `@property area` returning `width * height`; add `__eq__` and
`__lt__` that compare `self.area` to `other.area`.

---

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return "%s with area %d" % (self.name, self.area)


class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        return self.area == other.area

    def __lt__(self, other):
        return self.area < other.area
""",

"15.8 reference": r"""The capstone blends the chapter into one hierarchy, the way real classes are
built:

- **Inheritance** — `Rectangle(Shape)` *is a* `Shape`, so it gets `describe` for
  free and `isinstance(r, Shape)` is true.
- **`super()`** — `Rectangle.__init__` calls `super().__init__("rectangle")` to let
  the base set `self.name`, then adds its own width and height.
- **`@property`** — `area` is computed from width and height on each access, so it
  stays correct when a side changes.
- **Polymorphism** — `Shape.describe` reads `self.area`, which only `Rectangle`
  defines; the base method works through the subclass's property.
- **Dunders** — `__eq__` and `__lt__` (both by area) make rectangles compare and
  sort like built-in values, so `==` and `sorted` just work.

Together these turn a plain object into one that behaves like a first-class
value: it has an identity in a hierarchy, derived data, and meaningful equality
and ordering — the payoff of the whole chapter.

```python
r = Rectangle(3, 4)
r.describe()                              # 'rectangle with area 12'
Rectangle(2, 6) == Rectangle(3, 4)        # True  -- equal areas
sorted([Rectangle(3, 4), Rectangle(1, 1)])   # by area: 1, then 12
```
""",
}
