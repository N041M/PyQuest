# PyQuest translations -- language 'example' -- chapter 06_functions -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"6.1 brief": r"""# 6.1 -- def: your first function

## Concept

A **function** is a named, reusable piece of code. You have *called* functions
all along -- `print()`, `len()`, `sorted()`. Now you get to **define** your
own:

```python
def double(x):
    return x * 2
```

- `def` starts the definition; `double` is the name you choose.
- `x` is a **parameter**: a variable that receives whatever value the caller
  passes in.
- `return` hands a value **back to the caller**. Calling `double(3)` is then
  an expression worth `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**This chapter checks your code differently.** Until now your file *ran* and
printed. From here, the checker **imports** your file and **calls your
functions directly**, passing in many different arguments -- so there is no
`input()` and no `print()` needed at all. Your file just defines the function.

## Example

```python
def double(x):
    return x * 2
```

That whole file is a valid answer to this puzzle: it defines `double`, and
`double(21)` returns `42`.

## Your task

Define a function `double(x)` that **returns** `x` doubled.

## Done when

- `double(3)` returns `6`, `double(0)` returns `0`, `double(-5)` returns `-10`.
- Your file only defines the function -- no `input()`, no `print()`.
""",

"6.1 hints": r"""The shape is:  def name(parameter):  then an indented body that returns
something.

---

`def double(x):` on the first line; the body is one line: return x times 2.

---

def double(x):
    return x * 2
""",

"6.1 reference": r"""A **function** packages a piece of work under a name so it can be run on demand,
as many times as needed. **`def`** introduces one: a header `def name():` and an
indented body.

- **Calling** it — `name()` — runs the body. Defining a function does not run it;
  the call does.
- **`return value`** hands a result back to the caller and ends the function
  immediately. The call expression `name()` then *becomes* that value.
- A function with no `return` (or a bare `return`) hands back `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
""",

"6.2 brief": r"""# 6.2 -- Two parameters

## Concept

A function can take several parameters -- list them with commas, and the
caller's values arrive **in the same order**:

```python
def rect_area(width, height):
    return width * height

rect_area(3, 4)     # 12  (width=3, height=4)
```

Inside the body, the parameters are ordinary variables. Everything you know
already works on them -- arithmetic, comparisons, f-strings, loops.

A subtlety worth meeting early: parameters are **local** to the function. The
`width` inside `rect_area` exists only while a call is running; it is not
visible (and does not clash with) anything outside.

## Example

```python
def diff(a, b):
    return a - b

print(diff(10, 4))   # 6
print(diff(4, 10))   # -6  -- order matters
```

## Your task

Define `rect_area(width, height)` that returns the area of a rectangle
(width times height).

## Done when

- `rect_area(3, 4)` returns `12`; `rect_area(4, 3)` does too.
- A zero side returns `0`.
- No `input()`, no `print()` -- the checker passes the values in.
""",

"6.2 hints": r"""Two parameters are listed with a comma:  def rect_area(width, height):

---

The body is one line: return the product of the two parameters.

---

def rect_area(width, height):
    return width * height
""",

"6.2 reference": r"""A **parameter** is a name in the function header that stands for a value the
caller supplies. The values passed in a call are the **arguments**, matched to
parameters left to right.

- `def f(a, b):` declares two parameters; `f(3, 4)` calls with `a = 3`, `b = 4`.
- Parameters are **local**: they exist only during the call and don't clash with
  names outside. The function works on whatever it's given, making it reusable.
- Passing the wrong number of arguments raises `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
""",

"6.3 brief": r"""# 6.3 -- return, not print

## Concept

`print()` and `return` look similar when you test by eye, but they do
completely different jobs:

- `print(x)` **shows** `x` on the screen -- and that's all. The caller gets
  nothing.
- `return x` **hands `x` back** to the caller, who can store it, compare it,
  or pass it on.

A function that prints instead of returning actually returns `None` (the
"no value" value). The difference bites the moment someone *uses* the result:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

The rule: **a function's job is to compute and return.** Let the *caller*
decide whether to print.

## Example

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## Your task

Define `shout(word)` that **returns** the word in UPPERCASE with a `!` stuck
on the end. (`.upper()` is from 2.7.)

## Done when

- `shout("hi")` returns `"HI!"`; `shout("")` returns `"!"`.
- The value is *returned* -- a version that only prints will fail, because the
  checker receives `None`.
""",

"6.3 hints": r"""If the checker says it got None, your function printed instead of returning.

---

Build the string with .upper() and + "!", then return it -- no print anywhere.

---

def shout(word):
    return word.upper() + "!"
""",

"6.3 reference": r"""**Returning** a value and **printing** it are different acts, and confusing them
is a common bug.

- **`return`** hands a value back to the calling code, which can store it, do
  arithmetic on it, or pass it on. The value travels.
- **`print`** writes text to the screen and returns `None`. The value is shown but
  not captured — `x = print(5)` makes `x` be `None`.
- A function that prints instead of returning can't be built on. Prefer to
  `return` the result and let the **caller** decide whether to print it.

```python
def double(n):
    return n * 2        # caller can use it
print(double(5) + 1)    # 11  -- works because double returned
```
""",

"6.4 brief": r"""# 6.4 -- Default values

## Concept

A parameter can carry a **default**: the value used when the caller leaves it
out. Write it with `=` in the `def` line:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

You have already *used* this: `print(..., sep=" ")` from 1.3 -- `sep` has a
default of one space, which you overrode with `sep=", "`. Now you can build
the same flexibility into your own functions.

Rules: parameters with defaults go **after** the ones without, and the
default is used *only* when the caller omits that argument.

## Example

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## Your task

Define `greet(name, greeting="Hello")` that returns `"<greeting>, <name>!"` --
exactly: the greeting, a comma and a space, the name, an exclamation mark.

## Done when

- `greet("Ada")` returns `"Hello, Ada!"` (the default at work).
- `greet("Ada", "Hi")` returns `"Hi, Ada!"`.
- Without the default, the one-argument call would crash -- the checker makes
  both kinds of call.
""",

"6.4 hints": r"""The default goes in the def line:  def greet(name, greeting="Hello"):

---

Build the result with an f-string: the greeting, then ", ", then the name,
then "!".

---

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"
""",

"6.4 reference": r"""A **default value** in the header makes a parameter optional: if the caller omits
that argument, the default is used.

- `def greet(name, greeting="hi"):` can be called `greet("Ada")` (uses `"hi"`) or
  `greet("Ada", "hello")` (overrides it).
- Parameters **with** defaults must come **after** those without.
- Use a *new* default each call for mutable types — write `def f(items=None):`
  then `if items is None: items = []`, never `def f(items=[]):` (one shared list
  persists between calls).

```python
def power(base, exp=2):
    return base ** exp

power(5)       # 25  -- exp defaults to 2
power(5, 3)    # 125
```
""",

"6.5 brief": r"""# 6.5 -- return ends the function

## Concept

`return` doesn't just hand back a value -- it **stops the function on the
spot**. Nothing after an executed `return` runs. That makes branching
functions read cleanly: settle each case and leave.

```python
def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
```

Notice there is no `else` -- none is needed. If the first `return` fired, the
function is already over; reaching the last line *means* `n` was positive.
This style is called an **early return**.

A function with several `return` statements still returns exactly **one**
value per call: whichever `return` runs first.

## Example

```python
sign(-3)    # "negative"
sign(0)     # "zero"
sign(42)    # "positive"
```

## Your task

Define `sign(n)` that returns `"negative"`, `"zero"`, or `"positive"` for a
whole number `n`.

## Done when

- `sign(-3)`, `sign(0)`, `sign(42)` return the three words above.
- The boundary cases `-1` and `1` are right too.
""",

"6.5 hints": r"""Each case is an if with its own return. Once a return runs, the function is
over.

---

Check `n < 0` first, then `n == 0`; if neither returned, n must be positive --
just return "positive" with no condition.

---

def sign(n):
    if n < 0:
        return "negative"
    if n == 0:
        return "zero"
    return "positive"
""",

"6.5 reference": r"""A `return` can appear **anywhere** in a function, and reaching it ends the call at
once — later lines don't run. An **early return** uses this to handle a case and
leave immediately.

- It flattens code: handle the special or invalid case up front with a guard
  (`if bad: return ...`), then write the main path without nesting it in an
  `else`.
- The first `return` reached wins; nothing after it in that call executes.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
""",

"6.6 brief": r"""# 6.6 -- Returning two values

## Concept

`return` can hand back **several values at once** -- separate them with a
comma and Python packs them into a **tuple** (4.7):

```python
def min_max(nums):
    return min(nums), max(nums)
```

The caller can keep the tuple, or unpack it straight into variables -- the
same unpacking you used for `a, b = b, a`:

```python
pair = min_max([3, 1, 4])     # (1, 4)  -- one tuple
lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4  -- unpacked
```

This is how Python functions return "two answers" -- there is no special
trick, just a tuple and unpacking.

## Example

```python
def split_name(full):
    parts = full.split()
    return parts[0], parts[-1]

first, last = split_name("Ada King Lovelace")
# first = "Ada", last = "Lovelace"
```

## Your task

Define `min_max(nums)` that returns the smallest and largest item of a
non-empty list, **in that order**, as a tuple. (`min()`/`max()` are from 5.3.)

## Done when

- `min_max([3, 1, 4])` returns `(1, 4)` -- a tuple, smallest first.
- `min_max([7])` returns `(7, 7)`.
- Negative numbers work.
""",

"6.6 hints": r"""Two values after one return, separated by a comma, come back as a tuple.

---

You already have both halves from 5.3: `return min(nums), max(nums)`.

---

def min_max(nums):
    return min(nums), max(nums)
""",

"6.6 reference": r"""A function returns **one** object, but that object can be a **tuple**, so
`return a, b` hands back several values at once (Python packs them into a tuple).
The caller **unpacks** them with matching names.

- `return lo, hi` returns the tuple `(lo, hi)`; `low, high = bounds(xs)` unpacks
  it into two names.
- The counts must match on unpacking. Catch the whole tuple with one name if you
  prefer: `result = bounds(xs)` then `result[0]`, `result[1]`.

```python
def min_max(nums):
    return min(nums), max(nums)

lo, hi = min_max([3, 1, 4])   # lo = 1, hi = 4
```
""",

"6.7 brief": r"""# 6.7 -- Building on built-ins

## Concept

Functions shine when they bundle a small *recipe* behind a good name. The
recipe for an average:

> the total, divided by how many there are

You own every ingredient: `sum()` (5.2), `len()` (2.6), and `/` (1.9).
Remember from 1.9 that `/` **always returns a float** -- `4 / 2` is `2.0`,
not `2`. That is correct here: an average is naturally a decimal number.

```python
def average(nums):
    return sum(nums) / len(nums)
```

One function, one line, instantly reusable -- and the name says what the line
means.

## Example

```python
average([1, 2])        # 1.5
average([10, 20, 30])  # 20.0
```

## Your task

Define `average(nums)` that returns the average of a non-empty list of
numbers.

## Done when

- `average([1, 2])` returns `1.5`; `average([10, 20, 30])` returns `20.0`.
- The result is a **float** even when the division is exact (use `/`,
  not `//`).
- A one-item list returns that item (as a float).
""",

"6.7 hints": r"""An average is the total divided by the count -- and you have a built-in for
each half.

---

`sum(nums)` over `len(nums)`, with `/` (the float division from 1.9).

---

def average(nums):
    return sum(nums) / len(nums)
""",

"6.7 reference": r"""Functions **compose built-ins** into a named, reusable operation. An `average`
function is the model: it wraps `sum` and `len` behind one clear name.

- `return sum(nums) / len(nums)` computes the mean — but `len(nums)` is `0` for an
  empty list, which raises `ZeroDivisionError`, so guard it with an early return.
- Naming the operation (`average(scores)`) makes calling code read as intent, and
  fixing or improving the logic happens in one place.

```python
def average(nums):
    if not nums:
        return 0
    return sum(nums) / len(nums)

average([2, 4, 9])    # 5.0
```
""",

"6.8 brief": r"""# 6.8 -- Functions calling functions

## Concept

Your functions can call **each other**. That is the real power move: solve a
small problem once, name it, and build the next function on top.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` doesn't repeat the strip-and-lower recipe -- it *delegates* to
`clean`. If you ever improve `clean` (say, also removing punctuation), every
function built on it improves for free. Repeating the recipe in both places
is how bugs are born: fix one copy, forget the other.

Note `same_word` returns the result of a comparison -- a **boolean**
(`True`/`False`), like 3.1. No `if` needed: `clean(a) == clean(b)` already
*is* the answer.

## Example

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## Your task

Define **both** functions:

- `clean(text)` -- returns the text with surrounding spaces stripped and
  lowercased (2.7).
- `same_word(a, b)` -- returns `True` exactly when the two texts are the same
  after cleaning. It must **call `clean`** rather than redo the recipe.

## Done when

- `clean("  Tea ")` returns `"tea"`.
- `same_word("  Tea ", "tea")` is `True`; `same_word("tea", "milk")` is `False`.
- `same_word` calls `clean` -- the checker looks for the delegation.
""",

"6.8 hints": r"""Write clean first and get it passing in your head: .strip() then .lower(),
chained.

---

same_word is one line: compare clean(a) with clean(b) using == and return the
result -- a comparison already IS True or False.

---

def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
""",

"6.8 reference": r"""Functions **call other functions**, so a larger task is built from small, tested
pieces. The result of one becomes the argument or building block of the next.

- A helper does one job well; a higher-level function calls several helpers and
  combines their results. This is the core of structuring a program.
- `f(g(x))` feeds `g`'s result straight into `f`. Each function stays simple and
  independently checkable.

```python
def clean(s):  return s.strip().lower()
def is_yes(s): return clean(s) == "yes"

is_yes("  YES ")   # True  -- is_yes builds on clean
```
""",

"6.9 brief": r"""# 6.9 -- Recursion: a function calling itself

## Concept

A function may call **itself**. That is called **recursion**, and it works
whenever a problem contains a smaller copy of the same problem.

The factorial is the classic: `5!` means `5 * 4 * 3 * 2 * 1`. But look again:

> `5!` is just `5 * 4!` -- and `4!` is `4 * 3!` ...

A recursive function states exactly that, plus a **base case** -- the smallest
input answered directly, with no further calls:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` runs as `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Without the base case the calls would never stop --
recursion's version of an endless loop.

You could compute a factorial with a `for` loop -- but the *lesson* here is the
self-call, so this puzzle requires it.

## Example

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## Your task

Define `fact(n)` that returns `n!` **recursively**: a base case for `0`, and
`n * fact(n - 1)` for the rest. `n` is never negative.

## Done when

- `fact(0)` is `1`, `fact(1)` is `1`, `fact(5)` is `120`.
- `fact` calls itself -- the checker looks for the self-call, so a loop
  version won't pass.
""",

"6.9 hints": r"""Answer the smallest case first: if n is 0, return 1 -- no call needed.

---

For everything else, trust the function you are writing:
return n * fact(n - 1). The early return (6.5) keeps the base case clean.

---

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)
""",

"6.9 reference": r"""A **recursive** function calls **itself** to solve a smaller version of the same
problem. Two parts are essential:

- a **base case** that returns directly **without** recursing — this stops the
  recursion;
- a **recursive case** that calls the function on a smaller input and builds on
  the result, moving toward the base case each time.

Miss or never reach the base case and the calls nest until Python raises
`RecursionError`. Many recursions have a simpler loop form; recursion shines when
the problem is itself self-similar.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
""",

"6.10 brief": r"""# 6.10 -- Capstone: a tiny library

## Concept

Nothing new -- this capstone is the chapter in miniature: several functions,
each with one clear job, the later ones **delegating** to the earlier ones
(6.8). A file of related functions like this is the seed of every real
*library* you will ever import.

The pieces: `for ch in word` (3.10), `in` (5.1), the tally idea (5.9),
f-strings (2.10), and early returns (6.5).

## Example

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## Your task

Define **both** functions:

- `count_vowels(word)` -- returns how many characters of `word` are vowels
  (`a`, `e`, `i`, `o`, `u`; the words are lowercase).
- `describe(word)` -- returns the string `"<word> has <n> vowels"`, except
  when the count is zero: then it is `"<word> has no vowels"`. It must **call
  `count_vowels`**.

## Done when

- `count_vowels("tea")` is `2`; `count_vowels("xyz")` is `0`.
- `describe("tea")` is `"tea has 2 vowels"`; `describe("xyz")` is
  `"xyz has no vowels"`.
- `describe` delegates to `count_vowels` -- the checker looks for the call.
""",

"6.10 hints": r"""count_vowels is a tally over the characters: loop with `for ch in word` and
test `ch in "aeiou"`.

---

describe calls count_vowels once, stores the number, then early-returns the
"no vowels" wording when it is 0; otherwise an f-string with the count.

---

def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

def describe(word):
    n = count_vowels(word)
    if n == 0:
        return f"{word} has no vowels"
    return f"{word} has {n} vowels"
""",

"6.10 reference": r"""A **library** here means a set of related functions you've written, each named
for its job, that together form a reusable toolkit — the payoff of the chapter.

- Build small functions that each do one thing and `return` their result; then
  higher-level functions call them. Calling code reads as a sequence of intents.
- Keeping logic inside named functions (rather than copied inline) means a fix or
  improvement lands in one place and every caller benefits.

```python
def clean(s):    return s.strip().lower()
def words(s):    return clean(s).split()
def wordcount(s): return len(words(s))

wordcount("  The quick fox ")   # 3  -- each function builds on the last
```
""",
}
