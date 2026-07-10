# PyQuest translations -- language 'pt' -- chapter 14_functional -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"14.1 brief": r"""# 14.1 -- lambda: a function in an expression

## Concept

A **`lambda`** is a tiny function written inline, with no name and no `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- the value of the expression is returned
  automatically (no `return`, and only one expression allowed).
- A lambda is a **value**, so you can store it, **return** it from another
  function, or pass it as an argument (which is where it really earns its keep --
  the rest of this chapter).

Because a lambda is defined inside another function, it can **close over** that
function's variables. `lambda x: x * n` remembers the `n` from where it was made.

(For anything longer than one expression, use a normal `def` -- lambdas are for
small inline functions.)

## Example

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## Your task

Define `multiplier(n)` that **returns a lambda** which multiplies its argument by
`n`. So `multiplier(3)` returns a function, and calling that function with `4`
gives `12`.

## Done when

- `multiplier(3)(4)` is `12`; `multiplier(10)(5)` is `50`.
- `multiplier(0)(7)` is `0`.
- The returned function is a `lambda`, not a nested `def`.
""",

"14.1 hints": r"""A lambda is `lambda args: expression`. You want one that takes an `x` and gives
back `x * n`.

---

`multiplier` returns that lambda. The lambda closes over `n`, so each call to
`multiplier` makes a function tied to its own `n`.

---

def multiplier(n):
    return lambda x: x * n
""",

"14.1 reference": r"""A **`lambda`** is an anonymous function written as a single expression:
`lambda args: expression`. The expression's value is returned automatically —
there is no `return`, and the body must be **one** expression.

- A lambda is a first-class **value**: assign it, return it, or pass it as an
  argument. `f = lambda x: x * 2` is much like `def f(x): return x * 2`, just
  inline and nameless.
- Defined inside another function, a lambda **closes over** that scope's
  variables — `lambda x: x * n` captures `n` from where it was created, so each
  `multiplier(n)` yields a function bound to its own `n`.
- Lambdas are for *small* inline functions, especially as the `key=` to `sorted`
  or the function for `map`/`filter` (the rest of this chapter). For anything
  multi-statement, use a named `def`.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
""",

"14.2 brief": r"""# 14.2 -- map: apply to every item

## Concept

**`map(func, iterable)`** runs `func` on **every** item and yields the results.
It's the "apply to each" pattern as a higher-order function -- a function that
takes another function:

```python
list(map(str.upper, ["a", "b"]))     # ['A', 'B']
list(map(lambda x: x * x, [1, 2, 3])) # [1, 4, 9]
```

- `map` returns a **lazy iterator**, so wrap it in `list(...)` to get a list.
- The function can be a `lambda`, a `def`, or a built-in like `str.upper` or
  `int`.

(A list comprehension `[f(x) for x in items]` does the same thing and often reads
more naturally; this puzzle is about learning `map` itself, the tool you'll meet
in plenty of code.)

## Example

```python
def lengths(words):
    return list(map(len, words))
```

## Your task

Using **`map`**, define `squares(nums)` that returns a list of each number in
`nums` squared.

## Done when

- `squares([1, 2, 3])` returns `[1, 4, 9]`.
- `squares([])` returns `[]`.
- The mapping is done with `map`, not a comprehension or manual loop.
""",

"14.2 hints": r"""`map(func, nums)` applies `func` to each number. Your `func` squares its input:
`lambda x: x * x`.

---

`map` is lazy, so wrap it: `list(map(lambda x: x * x, nums))`.

---

def squares(nums):
    return list(map(lambda x: x * x, nums))
""",

"14.2 reference": r"""**`map(func, iterable)`** applies `func` to every item and yields the results —
the "transform each item" pattern as a higher-order function (one that takes
another function as an argument).

- It returns a **lazy iterator**, computing each result on demand; wrap it in
  `list(...)` (or `tuple`, or feed a `for`) to consume it.
- `func` can be a `lambda`, a named `def`, or any callable — a built-in like
  `len`, `str.upper`, or `int` is common.
- Given several iterables, `map(func, a, b)` calls `func(a_i, b_i)` in lockstep,
  stopping at the shortest.
- A list comprehension `[func(x) for x in items]` expresses the same thing and is
  often clearer; `map` is the functional-style equivalent you'll see widely.

```python
list(map(len, ["hi", "there"]))        # [2, 5]
list(map(lambda x: x * x, [1, 2, 3]))  # [1, 4, 9]
list(map(int, ["1", "2", "3"]))        # [1, 2, 3]
```
""",

"14.3 brief": r"""# 14.3 -- filter: keep what passes

## Concept

Where `map` transforms every item, **`filter`** keeps only **some** of them.
You give it a **predicate** -- a function that returns true or false -- and it
keeps each item the predicate says yes to:

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))     # [2, 4]
```

- `filter(pred, iterable)` yields each item for which `pred(item)` is truthy,
  dropping the rest, in order.
- Like `map`, it returns a **lazy iterator**, so wrap it in `list(...)`.

(The comprehension `[x for x in items if pred(x)]` does the same; this puzzle is
about `filter` itself.)

## Example

```python
def nonempty(strings):
    return list(filter(lambda s: s != "", strings))
```

## Your task

Using **`filter`**, define `evens(nums)` that returns a list of only the even
numbers in `nums`.

## Done when

- `evens([1, 2, 3, 4])` returns `[2, 4]`.
- `evens([1, 3, 5])` returns `[]`.
- The selection is done with `filter`, not a comprehension or manual loop.
""",

"14.3 hints": r"""`filter(pred, nums)` keeps each number where `pred` is true. Your predicate tests
even: `lambda x: x % 2 == 0`.

---

Wrap it in `list(...)`: `list(filter(lambda x: x % 2 == 0, nums))`.

---

def evens(nums):
    return list(filter(lambda x: x % 2 == 0, nums))
""",

"14.3 reference": r"""**`filter(pred, iterable)`** keeps the items for which the **predicate** `pred`
(a function returning true or false) is truthy, dropping the rest — the "keep if"
counterpart to `map`'s "transform each".

- It returns a **lazy iterator** in original order; wrap it in `list(...)` to
  collect.
- `pred` is any callable returning a truthy/falsy value — a `lambda`, a `def`, or
  a built-in. Passing **`None`** as the predicate (`filter(None, items)`) keeps
  the items that are themselves truthy, dropping `0`, `""`, `None`, etc.
- The comprehension `[x for x in items if pred(x)]` is the equivalent and often
  reads better; `filter` is the functional form.

```python
list(filter(lambda x: x > 0, [-1, 2, -3, 4]))   # [2, 4]
list(filter(None, [0, 1, "", "a", None]))        # [1, 'a']
list(filter(str.isalpha, "a1b2"))                # ['a', 'b']
```
""",

"14.4 brief": r"""# 14.4 -- sorted(key=lambda): sort by a derived value

## Concept

`sorted` (chapter 5) orders items by their natural order. Its **`key=`** argument
changes *what* it sorts on: a function mapping each item to the value to compare.
An inline **lambda** is the usual way to write that:

```python
words = ["pear", "fig", "apple"]
sorted(words, key=len)                  # ['fig', 'pear', 'apple']
sorted(words, key=lambda w: w[-1])      # by last letter
```

- `key` is called once per item; `sorted` then orders items by those key values.
- The lambda lets you sort by anything **derived** from an item -- its length, a
  field, a computed score -- without changing the items themselves.
- `sorted` is **stable**: items with equal keys keep their original order.

## Example

```python
def by_size(nums):
    return sorted(nums, key=lambda n: abs(n))   # by distance from zero
```

## Your task

Using **`sorted`** with a **`key=lambda`**, define `by_last(words)` that returns
the words sorted by their **last character**.

## Done when

- `by_last(["pear", "fig", "kiwi"])` returns `["fig", "kiwi", "pear"]`
  (last letters g, i, r are in order).
- `by_last([])` returns `[]`.
- The order comes from `sorted(..., key=lambda ...)`, not a manual sort.
""",

"14.4 hints": r"""`sorted(words, key=...)` sorts by whatever the key function returns. You want to
sort by the last character of each word.

---

The last character of `w` is `w[-1]`, so the key is `lambda w: w[-1]`:
`sorted(words, key=lambda w: w[-1])`.

---

def by_last(words):
    return sorted(words, key=lambda w: w[-1])
""",

"14.4 reference": r"""`sorted`'s **`key=`** argument is a function mapping each item to the value to
sort on, so you can order by something **derived** from the items rather than the
items themselves. An inline **`lambda`** is the idiomatic way to write that key.

- `key` is called **once per item**; `sorted` orders the items by the resulting
  key values, but returns the original items. `sorted(words, key=len)` orders by
  length, `sorted(words, key=lambda w: w[-1])` by last letter.
- `sorted` is **stable**: items with equal keys keep their input order.
- Pair `key=` with **`reverse=True`** to sort descending. The same `key=` works on
  `list.sort`, `min`, and `max`.

```python
sorted(["pear", "fig", "apple"], key=len)            # ['fig', 'pear', 'apple']
sorted([-3, 1, -2], key=lambda n: abs(n))            # [1, -2, -3]
sorted(records, key=lambda r: r[1], reverse=True)    # by 2nd field, high first
```
""",

"14.5 brief": r"""# 14.5 -- any: is at least one true?

## Concept

**`any(iterable)`** returns `True` if **at least one** item is truthy, `False`
otherwise. Fed a generator of tests, it answers "does *any* item pass?":

```python
any(n < 0 for n in [1, 2, -3])     # True
any(n < 0 for n in [1, 2, 3])      # False
```

- It replaces the loop-with-a-flag (`found = False; for ...: if ...: found =
  True`) with one expression.
- It **short-circuits**: it stops and returns `True` at the first truthy item.
- `any([])` is `False` (nothing passed).

The pattern is `any(<test> for <item> in <iterable>)` -- a generator expression
of booleans handed to `any`.

## Example

```python
def has_blank(strings):
    return any(s == "" for s in strings)
```

## Your task

Using **`any`**, define `has_negative(nums)` that returns `True` if `nums`
contains at least one negative number.

## Done when

- `has_negative([1, 2, -3])` is `True`; `has_negative([1, 2, 3])` is `False`.
- `has_negative([])` is `False`.
- The answer comes from `any(...)`, not a hand-written loop with a flag.
""",

"14.5 hints": r"""`any(...)` takes a sequence of true/false values and returns True if any is true.
Build that sequence with a generator expression.

---

`any(n < 0 for n in nums)` -- for each number, the test `n < 0` is True or False,
and `any` reports whether at least one was True.

---

def has_negative(nums):
    return any(n < 0 for n in nums)
""",

"14.5 reference": r"""**`any(iterable)`** returns `True` as soon as **one** item is truthy, else
`False`. Handed a generator of tests, it answers "does any item pass?" in a single
expression, replacing a loop that sets a flag.

- It **short-circuits**: evaluation stops at the first truthy item, so it's
  efficient and works on infinite/lazy iterables.
- `any([])` is `False` — there is nothing to be true.
- The idiom is `any(<test> for <item> in <iterable>)`: a generator expression of
  booleans. (Its partner `all` is 14.6.)

```python
any(n < 0 for n in [1, 2, -3])    # True
any(c.isdigit() for c in "abc")   # False
any([])                           # False
```
""",

"14.6 brief": r"""# 14.6 -- all: are they every one true?

## Concept

**`all(iterable)`** is `any`'s partner: it returns `True` only if **every** item
is truthy. It answers "do they *all* pass?":

```python
all(n > 0 for n in [1, 2, 3])      # True
all(n > 0 for n in [1, -2, 3])     # False
```

- It **short-circuits** the other way: it stops and returns `False` at the first
  item that fails.
- `all([])` is `True` -- vacuously, since no item failed. (A common surprise:
  "all of nothing" is true.)

Same shape as `any`: `all(<test> for <item> in <iterable>)`.

## Example

```python
def all_words(strings):
    return all(s.isalpha() for s in strings)
```

## Your task

Using **`all`**, define `all_positive(nums)` that returns `True` if **every**
number in `nums` is greater than zero.

## Done when

- `all_positive([1, 2, 3])` is `True`; `all_positive([1, -2, 3])` is `False`.
- `all_positive([])` is `True` (nothing fails).
- The answer comes from `all(...)`, not a hand-written loop with a flag.
""",

"14.6 hints": r"""`all(...)` returns True only if every value in the sequence is true. Build the
sequence of tests with a generator expression.

---

`all(n > 0 for n in nums)` -- each `n > 0` is True or False, and `all` is True
only if none were False.

---

def all_positive(nums):
    return all(n > 0 for n in nums)
""",

"14.6 reference": r"""**`all(iterable)`** returns `True` only if **every** item is truthy — the partner
to `any`. It answers "do they all pass?" in one expression.

- It **short-circuits** on the first falsy item, returning `False` immediately.
- `all([])` is `True` — *vacuously*, since no item failed. This "all of nothing
  is true" rule is a common surprise; guard for the empty case if it matters.
- Same shape as `any`: `all(<test> for <item> in <iterable>)`. Together they
  express the universal ("for all") and existential ("there exists") questions
  over a sequence.

```python
all(n > 0 for n in [1, 2, 3])     # True
all(n > 0 for n in [1, -2, 3])    # False
all([])                           # True  -- vacuously
```
""",

"14.7 brief": r"""# 14.7 -- reduce: fold a sequence to one value

## Concept

**`reduce`** (from `functools`) **folds** a whole sequence into a single value by
applying a two-argument function cumulatively, left to right:

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10  ((((1+2)+3)+4))
reduce(lambda a, b: a * b, [1, 2, 3, 4])     # 24
```

- `reduce(func, items)` computes `func(func(func(i0, i1), i2), i3)...` -- each
  step combines the running result with the next item.
- A third argument is a **start** value: `reduce(func, items, start)` begins the
  fold from `start`, which also defines the answer for an **empty** sequence.
- It's the accumulator loop (chapter 3) as a higher-order function. (`sum` is the
  special case for `+`; `reduce` lets you fold with *any* combiner.)

## Example

```python
from functools import reduce

def total(nums):
    return reduce(lambda a, b: a + b, nums, 0)
```

## Your task

Using **`reduce`** from `functools`, define `product(nums)` that returns the
product of all the numbers (with a start of `1`, so the empty list gives `1`).

## Done when

- `product([1, 2, 3, 4])` returns `24`; `product([5])` returns `5`.
- `product([])` returns `1`.
- The fold uses `reduce`, not a manual accumulator loop.
""",

"14.7 hints": r"""`from functools import reduce`. It takes a two-argument combiner, the items, and
a start value.

---

The combiner multiplies the running result by the next number:
`reduce(lambda a, b: a * b, nums, 1)`. The start `1` makes the empty list give 1.

---

from functools import reduce


def product(nums):
    return reduce(lambda a, b: a * b, nums, 1)
""",

"14.7 reference": r"""**`functools.reduce(func, iterable[, start])`** **folds** a sequence into a single
value by applying a two-argument `func` cumulatively, left to right:
`func(func(func(i0, i1), i2), i3)...`. Each step combines the running result with
the next item.

- A **start** value (`reduce(func, items, start)`) seeds the fold and defines the
  result for an **empty** sequence; without it, reducing an empty iterable raises
  `TypeError`.
- It generalises the accumulator loop to *any* combiner: `+` gives a sum, `*` a
  product, `max` the largest. The dedicated `sum` is the `+` special case, and
  `math.prod` the `*` one — but `reduce` folds with whatever function you supply.
- `reduce` lives in `functools` (it's not a built-in), so it must be imported.

```python
from functools import reduce

reduce(lambda a, b: a + b, [1, 2, 3, 4])      # 10
reduce(lambda a, b: a * b, [1, 2, 3, 4], 1)   # 24
reduce(lambda a, b: a if a > b else b, [3, 9, 2])   # 9  (max)
```
""",

"14.8 brief": r"""# 14.8 -- Capstone: a ranked shortlist

## Concept

The chapter's tools chain into a **pipeline**. Given a list of `(name, score)`
records, build a shortlist:

1. **`filter`** to the records that meet a threshold,
2. **`sorted`** with a `key=lambda` (and `reverse=True`) to rank them high to low,
3. **`map`** out just the names.

```python
records = [("Ada", 90), ("Linus", 70), ("Grace", 95)]
qualified = filter(lambda r: r[1] >= 80, records)
ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
list(map(lambda r: r[0], ranked))     # ['Grace', 'Ada']
```

Each record is a tuple, so `r[0]` is the name and `r[1]` the score.

## Your task

Define `passing(records, threshold)` that takes a list of `(name, score)` tuples
and returns the **names** of those with `score >= threshold`, ordered by score
**highest first**, built with `filter`, `sorted(key=lambda ...)`, and `map`.

## Done when

- `passing([("Ada", 90), ("Linus", 70), ("Grace", 95)], 80)` returns
  `["Grace", "Ada"]`.
- `passing([], 50)` returns `[]`; a threshold above every score returns `[]`.
- The result is built by filtering, sorting by a lambda key, and mapping -- a
  pipeline of the chapter's tools.
""",

"14.8 hints": r"""Three steps. First `filter(lambda r: r[1] >= threshold, records)` keeps the
records that qualify (r[1] is the score).

---

Then `sorted(qualified, key=lambda r: r[1], reverse=True)` ranks them high to
low, and `map(lambda r: r[0], ...)` pulls out the names. Wrap the map in `list`.

---

def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
""",

"14.8 reference": r"""The capstone chains the chapter's higher-order functions into a **data
pipeline** — the shape of much real processing:

1. **`filter(lambda r: r[1] >= threshold, records)`** narrows to the records that
   qualify;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** ranks them by score, high
   to low (stable, so equal scores keep their order);
3. **`map(lambda r: r[0], ...)`** projects out just the field you want — the name.

Each stage takes a function and an iterable and yields another iterable, so they
compose directly: the filter feeds the sort, the sort feeds the map. The same
pipeline could be written with comprehensions; expressing it as
`filter`/`sorted`/`map` is the functional style, and seeing a task *as* a pipeline
of transformations is the skill the chapter builds toward.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
""",
}
