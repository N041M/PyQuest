# PyQuest translations -- language 'example' -- chapter 04_collections -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"4.1 brief": r"""# 4.1 -- Lists and append

## Concept

A **list** holds several values in order, in one variable. You write a list with
square brackets, items separated by commas:

```python
nums = [10, 20, 30]
print(nums)        # [10, 20, 30]
print(nums[0])     # 10   (index like a string -- from 0)
print(len(nums))   # 3
```

A list can start empty and grow. `.append(x)` adds `x` to the **end**:

```python
nums = []
nums.append(10)
nums.append(20)
print(nums)        # [10, 20]
```

This "start empty, append in a loop" pattern is how you build a list from input.

## Example

```python
items = []
items.append(1)
items.append(2)
print(items)       # [1, 2]
```

## Your task

Read a whole number `n`, then read `n` more whole numbers (one per line). Collect
them into a list with `.append()`, and print the finished list.

For input `3`, then `1`, `2`, `3`:

```
[1, 2, 3]
```

## Done when

- `3` with `1, 2, 3` prints `[1, 2, 3]`.
- A count of `0` prints `[]` (an empty list).
""",

"4.1 hints": r"""Start with an empty list [], then append each number inside a loop.

---

`nums = []`, read n, then `for _ in range(n): nums.append(int(input()))`.
Finally `print(nums)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
""",

"4.1 reference": r"""A **list** is an ordered, mutable sequence of values, written in square brackets:
`[10, 20, 30]`. The empty list is `[]`. Items are reached by index just like
string characters (`lst[0]`, `lst[-1]`).

- **`.append(x)`** adds `x` to the **end**, growing the list by one. It changes
  the list in place and returns `None` (so never write `lst = lst.append(x)`).
- The build-from-empty pattern: start with `[]`, then `.append` once per pass of
  a loop to collect results.
- Unlike strings, a list may hold values of mixed types.

```python
nums = []
for i in range(3):
    nums.append(i * i)   # -> [0, 1, 4]
```
""",

"4.2 brief": r"""# 4.2 -- Changing a list

## Concept

Unlike strings, lists can be **changed in place** (they are *mutable*). A few ways:

- Replace an item by index: `nums[0] = 99`
- Remove and return the **last** item: `nums.pop()`
- Remove the first matching **value**: `nums.remove(20)`

```python
nums = [10, 20, 30]
nums[0] = 99      # [99, 20, 30]   replace by position
nums.pop()        # [99, 20]       drop the last item (returns 30)
print(nums)       # [99, 20]
```

These change the existing list -- the variable still points at the same list,
now modified.

## Example

```python
xs = [1, 2, 3]
xs[1] = 0
xs.pop()
print(xs)         # [1, 0]
```

## Your task

Read a count `n` (at least 1), then `n` numbers, into a list. Then:

1. **double the first item** (replace `nums[0]` with `nums[0] * 2`), and
2. **remove the last item** with `.pop()`.

Print the resulting list. For input `3`, then `5`, `2`, `9`:

```
[10, 2]
```

(`[5, 2, 9]` -> double first -> `[10, 2, 9]` -> pop -> `[10, 2]`.)

## Done when

- `5, 2, 9` gives `[10, 2]`.
- A single number `n=1` (e.g. just `4`) gives `[]` -- doubled to `[8]`, then the
  last (only) item is popped.
""",

"4.2 hints": r"""Build the list as before, then change it in place.

---

`nums[0] = nums[0] * 2` to double the first item; `nums.pop()` to drop the last.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
""",

"4.2 reference": r"""Lists are **mutable**: their contents can change in place, unlike strings.

- **`lst[i] = x`** replaces the item at index `i`. The index must already exist
  (assigning past the end raises `IndexError`).
- **`.pop()`** removes and **returns** the last item, shrinking the list;
  `.pop(i)` removes the item at index `i`. Popping from an empty list raises.
- Other in-place changes: `.insert(i, x)`, `.remove(value)`, `del lst[i]`.

Because the change is in place, every name referring to the same list object sees
it.

```python
lst = [10, 20, 30]
lst[1] = 99      # [10, 99, 30]
last = lst.pop() # last == 30, lst == [10, 99]
```
""",

"4.3 brief": r"""# 4.3 -- Looping over a list

## Concept

Just like a string, a list is a sequence -- so a `for` loop walks straight over
its items, one per pass:

```python
nums = [10, 20, 30]
for x in nums:
    print(x)        # 10, then 20, then 30
```

`len(nums)` gives the number of items, and slicing works too -- `nums[1:]` is all
but the first, `nums[:2]` is the first two:

```python
print(len(nums))    # 3
print(nums[:2])     # [10, 20]
```

## Example

```python
xs = [1, 2, 3]
for x in xs:
    print(x * 10)   # 10, 20, 30
```

## Your task

Read a count `n`, then `n` numbers, into a list. First print how many numbers
there are, then print each number **doubled**, one per line.

For input `3`, then `5`, `2`, `9`:

```
3
10
4
18
```

## Done when

- `5, 2, 9` prints `3`, then `10`, `4`, `18`.
- A count of `0` prints just `0` (no numbers to double).
""",

"4.3 hints": r"""After building the list, print len(nums), then loop over it.

---

`print(len(nums))`, then `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
""",

"4.3 reference": r"""A list is iterable, so **`for x in lst`** visits each item in order, binding the
loop variable to the item itself (not its index).

- This is the usual way to read a list. When you also need the position, pair it
  with `range(len(lst))` or `enumerate` (chapter 5).
- **`len(lst)`** gives the item count; **slicing** (`lst[1:3]`, `lst[::-1]`)
  works exactly as on strings and returns a new list.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
""",

"4.4 brief": r"""# 4.4 -- split: text into a list

## Concept

`s.split()` breaks a string into a **list of pieces**. With no argument it splits
on whitespace, so it turns a sentence into its words:

```python
"the quick brown fox".split()    # ['the', 'quick', 'brown', 'fox']
```

The result is a real list, so everything you know about lists applies -- `len`,
indexing, looping:

```python
words = "a b c".split()
print(len(words))    # 3
print(words[0])      # a
```

You can also split on a specific separator by passing it in:
`"a,b,c".split(",")` gives `['a', 'b', 'c']`.

## Example

```python
parts = "one two three".split()
print(len(parts))    # 3
```

## Your task

Read a line of words separated by spaces, and print **how many words** it
contains.

For input `the quick brown fox`:

```
4
```

## Done when

- `the quick brown fox` prints `4`; a single word prints `1`.
- An empty line prints `0`.
""",

"4.4 hints": r""".split() turns the line into a list of words. Then count them.

---

`print(len(input().split()))`.

---

line = input()
print(len(line.split()))
""",

"4.4 reference": r"""**`s.split()`** breaks a string into a **list of pieces**. With no argument it
splits on runs of **whitespace** and discards leading/trailing blanks — the usual
way to get the words of a line.

- `s.split(sep)` splits on the exact separator `sep`, keeping empty pieces
  between adjacent separators (`"a,,b".split(",")` is `["a", "", "b"]`).
- `s.split(sep, maxsplit)` splits at most `maxsplit` times — handy to peel off a
  prefix, e.g. `"key=a=b".split("=", 1)` is `["key", "a=b"]`.
- It is the inverse of `join` (next).

```python
"the quick fox".split()        # ['the', 'quick', 'fox']
"2024-01-15".split("-")        # ['2024', '01', '15']
```
""",

"4.5 brief": r"""# 4.5 -- join: a list into text

## Concept

`.join()` is the opposite of `split`: it glues a **list of strings** into one
string, putting a separator between each piece. You call it *on the separator*:

```python
words = ["a", "b", "c"]
print("-".join(words))    # a-b-c
print(", ".join(words))   # a, b, c
print("".join(words))     # abc   (no separator)
```

Read it as "join these words with this separator between them". The list must
contain strings.

## Common mistake

`join` is written separator-first: `"-".join(words)`, **not** `words.join("-")`.

## Example

```python
parts = ["2024", "12", "25"]
print("/".join(parts))    # 2024/12/25
```

## Your task

Read a count `n`, then `n` words (one per line), into a list. Print them joined
with a dash `-`.

For input `3`, then `a`, `b`, `c`:

```
a-b-c
```

## Done when

- `a, b, c` prints `a-b-c`; a single word prints just that word.
- A count of `0` prints an empty line (nothing to join).
""",

"4.5 hints": r"""Collect the words into a list, then join them. join is called on the separator.

---

Build the list, then `print("-".join(words))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print("-".join(words))
""",

"4.5 reference": r"""**`sep.join(parts)`** glues an iterable of **strings** into one string, placing
`sep` between adjacent items. The separator is the string you call it on, which
reads oddly at first but lets the separator be any string.

- Every item must already be a string; numbers raise `TypeError`. Convert first,
  e.g. `", ".join(str(n) for n in nums)`.
- `"".join(parts)` concatenates with no separator — the efficient way to build a
  string from many pieces (far better than repeated `+`).
- It is the inverse of `split`.

```python
"-".join(["2024", "01", "15"])   # '2024-01-15'
" ".join(["the", "fox"])          # 'the fox'
```
""",

"4.6 brief": r"""# 4.6 -- Lists inside lists

## Concept

A list can hold **other lists**. This is how you represent rows of data, pairs,
grids, and so on:

```python
pairs = [[1, 2], [3, 4], [5, 6]]
print(pairs)        # [[1, 2], [3, 4], [5, 6]]
print(pairs[0])     # [1, 2]        the first inner list
print(pairs[0][1])  # 2            first inner list, second item
```

Two indexes: the first picks an inner list, the second picks an item inside it.
Looping gives you each inner list in turn:

```python
for p in pairs:
    print(p[0] + p[1])   # 3, 7, 11
```

## Example

```python
grid = [[1, 1], [2, 2]]
for row in grid:
    print(row[0] + row[1])   # 2, 4
```

## Your task

Read a count `n`, then `n` **pairs** of numbers (each pair is two numbers, on two
lines). Build a list of `[a, b]` pairs. First print the whole nested list, then
print the **sum of each pair**, one per line.

For input `2`, then `1`, `2`, `3`, `4`:

```
[[1, 2], [3, 4]]
3
7
```

## Done when

- `1,2` and `3,4` print `[[1, 2], [3, 4]]` then `3` then `7`.
- A count of `0` prints `[]` and nothing else.
""",

"4.6 hints": r"""For each pair, read two numbers and append them as a two-item list [a, b].

---

`pairs.append([a, b])` builds the nested list. Print it, then loop:
`for p in pairs: print(p[0] + p[1])`.

---

n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
""",

"4.6 reference": r"""A list can contain other lists — a **nested** list — modelling a grid or table.
`grid[r]` selects an inner list (a row); `grid[r][c]` then selects an item from
it (a column), so two indexes reach one cell.

- The first index picks the row, the second the item within that row.
- A `for row in grid:` loop yields each inner list; nest a second loop
  (`for cell in row:`) to reach every item.
- The inner lists are ordinary lists — mutable and independently sized (rows
  need not be the same length).

```python
grid = [[1, 2, 3],
        [4, 5, 6]]
grid[0][2]    # 3   -- row 0, column 2
grid[1][0]    # 4
```
""",

"4.7 brief": r"""# 4.7 -- Tuples and unpacking

## Concept

A **tuple** is like a list, but **immutable** -- once made, it can't be changed.
You write one with parentheses (or just commas):

```python
point = (3, 7)
print(point[0])    # 3
```

**Unpacking** assigns several variables at once from a tuple (or list):

```python
x, y = point       # x = 3, y = 7
```

The left side names match the items on the right, in order. A neat trick this
enables is **swapping** two variables without a temporary:

```python
a, b = 1, 2
a, b = b, a        # now a = 2, b = 1
```

The right-hand side `b, a` builds a tuple, which is then unpacked into `a, b`.

## Example

```python
a, b = 10, 20
a, b = b, a
print(a)    # 20
print(b)    # 10
```

## Your task

Read two whole numbers (each on its own line). **Swap** them using tuple
unpacking, then print the first, then the second.

For input `3` then `7`:

```
7
3
```

## Done when

- `3, 7` prints `7` then `3`.
- It works for any two numbers (including two equal ones).
""",

"4.7 hints": r"""Read both numbers, then swap them in one line with a, b = b, a.

---

`a = int(input())`, `b = int(input())`, then `a, b = b, a`, then print a and b.

---

a = int(input())
b = int(input())
a, b = b, a
print(a)
print(b)
""",

"4.7 reference": r"""A **tuple** is an ordered, **immutable** sequence, written with commas (often in
parentheses): `(3, 4)`, or just `3, 4`. Once made it cannot be changed.

- **Unpacking** assigns the items of a sequence to several names at once:
  `a, b = point`. The count on each side must match.
- This enables the one-line **swap** `a, b = b, a`: the right side is built into
  a tuple first, then unpacked, so no temporary is needed.
- Use a tuple for a fixed group of related values (a coordinate, a record); use a
  list when the collection grows or changes.

```python
point = (3, 4)
x, y = point        # x = 3, y = 4
a, b = b, a         # swap in one line
```
""",

"4.8 brief": r"""# 4.8 -- Dictionaries

## Concept

A **dictionary** (`dict`) maps **keys** to **values** -- a lookup table. You write
one with curly braces and `key: value` pairs:

```python
ages = {"sam": 20, "ada": 36}
print(ages["sam"])     # 20      look up by key
ages["lee"] = 41       # add a new key
ages["sam"] = 21       # update an existing key
```

You look things up by **key** (not by position), which is what makes dicts fast
and handy for "given X, what is its Y?". Start from empty with `{}` and fill it in:

```python
d = {}
d["x"] = 1
```

## Example

```python
prices = {}
prices["apple"] = 3
print(prices["apple"])   # 3
```

## Your task

Read a count `n`, then `n` pairs of a **word** and a **number** (word on one line,
number on the next) into a dictionary (the word is the key, the number the value).
Then read one more **query word** and print the number stored for it.

For input `2`, `apple`, `3`, `banana`, `5`, then the query `banana`:

```
5
```

## Done when

- Building `{apple: 3, banana: 5}` and querying `banana` prints `5`.
- A later pair with the same key updates it (the test relies on the last value
  for any repeated key).
""",

"4.8 hints": r"""Make an empty dict, then store each pair as d[word] = number.

---

`d = {}`, loop reading word + number with `d[word] = int(input())`, then read
the query and `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
""",

"4.8 reference": r"""A **dictionary** (`dict`) maps **keys** to **values**: `{"a": 1, "b": 2}`. It is
the tool for lookup by name rather than by position.

- **`d[key]`** reads the value for a key; **`d[key] = value`** adds the key (if
  new) or updates it (if present). Keys are unique — assigning an existing key
  overwrites.
- Reading a **missing** key with `d[key]` raises `KeyError` (see `.get`, 4.10).
- Keys must be immutable (strings, numbers, tuples); values can be anything.
  `len(d)` counts the pairs; `key in d` tests for a key.

```python
ages = {"Ada": 36}
ages["Ada"]          # 36
ages["Linus"] = 21   # add a new pair
```
""",

"4.9 brief": r"""# 4.9 -- Looping over a dictionary

## Concept

To visit everything in a dict, loop over `.items()`, which gives each **key and
value** together:

```python
ages = {"sam": 20, "ada": 36}
for name, age in ages.items():
    print(name, age)      # sam 20, then ada 36
```

The `for name, age in ...` part is unpacking each pair into two variables. Dicts
remember the order you inserted keys, so you get them back in that order.

There are also `.keys()` (just the keys) and `.values()` (just the values), but
`.items()` is the usual one when you need both.

## Example

```python
d = {"x": 1, "y": 2}
for k, v in d.items():
    print(f"{k}={v}")     # x=1, then y=2
```

## Your task

Read a count `n`, then `n` pairs of a **word** and a **number** into a dict. Then
print one line `key=value` for each pair, in the order they were added.

For input `2`, `a`, `1`, `b`, `2`:

```
a=1
b=2
```

## Done when

- `a=1`, `b=2` are printed in insertion order.
- A count of `0` prints nothing.
""",

"4.9 hints": r"""Build the dict, then loop over d.items() to get each key and value.

---

`for k, v in d.items(): print(f"{k}={v}")`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
for k, v in d.items():
    print(f"{k}={v}")
""",

"4.9 reference": r"""**`d.items()`** yields each `(key, value)` pair, so a `for` loop with two
variables walks the whole dictionary, unpacking each pair as it goes.

- `for k, v in d.items():` binds `k` to the key and `v` to its value each pass.
- `d.keys()` and `d.values()` iterate just the keys or just the values; looping
  the dict directly (`for k in d`) iterates the **keys**.
- Iteration order is the **insertion order** (the order keys were first added).

```python
prices = {"pen": 2, "ink": 5}
for item, cost in prices.items():
    print(item, cost)        # pen 2 / ink 5
```
""",

"4.10 brief": r"""# 4.10 -- Missing keys and .get()

## Concept

Looking up a key that isn't in the dict with `d[key]` **crashes** (a `KeyError`):

```python
ages = {"sam": 20}
print(ages["lee"])    # KeyError!
```

`.get()` is the safe way. It returns `None` for a missing key instead of
crashing -- or a **default** you supply:

```python
print(ages.get("lee"))        # None
print(ages.get("lee", 0))     # 0      (your default)
print(ages.get("sam", 0))     # 20     (key exists, so its value)
```

So `d.get(key, default)` means "the value if the key is there, otherwise
`default`".

## Example

```python
d = {"a": 1}
print(d.get("a", 0))    # 1
print(d.get("z", 0))    # 0
```

## Your task

Read a count `n`, then `n` pairs of a word and a number into a dict. Then read a
**query word** and print its number -- but if the word isn't in the dict, print
`0` instead (do not crash).

For input `2`, `a`, `1`, `b`, `2`, then the query `c`:

```
0
```

(`c` isn't a key, so the default `0` is printed.)

## Done when

- A present key prints its value; a missing key prints `0`.
- It never crashes on a missing key (use `.get`).
""",

"4.10 hints": r"""d[key] crashes if the key is missing. d.get(key, 0) returns 0 instead.

---

After building the dict and reading the query, `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
""",

"4.10 reference": r"""**`d.get(key, default)`** looks a key up safely: it returns the value if the key
is present, otherwise the `default` — without raising. With no default it returns
`None` for a missing key.

- Use it instead of `d[key]` whenever a missing key is a normal, expected case
  rather than a bug.
- It powers the **tally** idiom: `counts[k] = counts.get(k, 0) + 1` reads the
  running count (0 the first time) and writes the new one.
- `.get` only reads; it never inserts the key (unlike `setdefault`).

```python
ages = {"Ada": 36}
ages.get("Ada", 0)     # 36
ages.get("Nobody", 0)  # 0  -- no KeyError
```
""",

"4.11 brief": r"""# 4.11 -- Sets

## Concept

A **set** is an unordered collection of **unique** items -- it automatically drops
duplicates. Write one with curly braces, or build one from a list with `set(...)`:

```python
s = {1, 2, 2, 3}
print(s)              # {1, 2, 3}   (the duplicate 2 is gone)

nums = [1, 1, 2, 3, 3]
print(set(nums))      # {1, 2, 3}
print(len(set(nums))) # 3           how many *distinct* values
```

Sets are great for "how many different things?" and for fast membership tests
with `in`:

```python
print(2 in s)         # True
```

(Sets have no order and no indexing -- you can't do `s[0]`.)

## Example

```python
words = ["a", "b", "a"]
print(len(set(words)))   # 2
```

## Your task

Read a count `n`, then `n` words. Print how many **distinct** words there are.

For input `4`, `a`, `b`, `a`, `c`:

```
3
```

(`a` appears twice but counts once.)

## Done when

- `a, b, a, c` prints `3`.
- A count of `0` prints `0`.
""",

"4.11 hints": r"""A set drops duplicates. Put the words in a set, then count it.

---

Collect the words in a list, then `print(len(set(words)))`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
""",

"4.11 reference": r"""A **set** is an unordered collection of **unique** items: `{1, 2, 3}`. It models
"a group of distinct things" and tests membership fast.

- Building a set from a sequence **drops duplicates**: `set([1, 1, 2])` is
  `{1, 2}`. The empty set is `set()` — `{}` is an empty *dict*.
- **`x in s`** tests membership and is much faster than scanning a list, because
  sets are hash-based.
- Sets are unordered (no indexing, no slicing) and hold only immutable items.
  Add with `.add(x)`, remove with `.discard(x)`.

```python
seen = set()
seen.add("a"); seen.add("a")   # {'a'} -- duplicate ignored
"a" in seen                    # True
set([3, 1, 3, 2])              # {1, 2, 3}
```
""",

"4.12 brief": r"""# 4.12 -- Combining sets

## Concept

Sets can be combined like in maths:

- **intersection** `a & b` -- items in **both**
- **union** `a | b` -- items in **either**
- **difference** `a - b` -- items in `a` but not `b`

```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)    # {2, 3}
print(a | b)    # {1, 2, 3, 4}
print(a - b)    # {1}
```

These answer questions like "which items do two groups share?" without writing a
loop. (`a.intersection(b)` and `a.union(b)` do the same as `&` and `|`.)

## Example

```python
x = {"a", "b"}
y = {"b", "c"}
print(len(x & y))   # 1   (just "b")
```

## Your task

Read a first group: a count `n`, then `n` words. Then a second group: a count
`m`, then `m` words. Print **how many distinct words appear in both** groups.

For first group `a`, `b` and second group `b`, `c`:

```
1
```

(Only `b` is in both.)

## Done when

- `{a, b}` and `{b, c}` print `1`.
- Empty groups give `0`; duplicates within a group count once.
""",

"4.12 hints": r"""Put each group in a set, then use the intersection of the two.

---

Build set `a` and set `b`, then `print(len(a & b))`.

---

n = int(input())
a = set()
for _ in range(n):
    a.add(input())
m = int(input())
b = set()
for _ in range(m):
    b.add(input())
print(len(a & b))
""",

"4.12 reference": r"""Sets support the algebra of collections:

- **`a & b`** (intersection) — items in **both**.
- **`a | b`** (union) — items in **either**.
- **`a - b`** (difference) — items in `a` but **not** in `b`.

Each returns a **new** set. (`^` is the symmetric difference — in exactly one.)
These express set questions directly, replacing hand-written loops that compare
two collections.

```python
a, b = {1, 2, 3}, {2, 3, 4}
a & b     # {2, 3}
a | b     # {1, 2, 3, 4}
a - b     # {1}
```
""",

"4.13 brief": r"""# 4.13 -- Choosing the right collection

## Concept

You now have four collections. Picking the right one makes a problem easy:

- **list** -- ordered items, duplicates allowed (`[1, 2, 2]`). Use for sequences.
- **tuple** -- like a list but fixed/immutable. Use for fixed groups.
- **set** -- unordered, **unique** items. Use for "distinct" and fast membership.
- **dict** -- key -> value lookup. Use for "given X, find its Y".

This puzzle combines a few:

- `len(nums)` -- how many items (a **list** keeps every value, including repeats).
- `len(set(nums))` -- how many **distinct** values (a **set** drops duplicates).
- the **sum** -- a loop with an accumulator (or `sum(nums)`).

## Example

```python
nums = [1, 2, 2, 3]
print(len(nums))        # 4
print(len(set(nums)))   # 3
```

## Your task

Read a count `n`, then `n` numbers. Print three lines:

1. how many numbers there are,
2. how many **distinct** numbers there are,
3. their **total**.

For input `4`, then `1`, `2`, `2`, `3`:

```
4
3
8
```

## Done when

- `1, 2, 2, 3` prints `4`, `3`, `8`.
- A count of `0` prints `0`, `0`, `0`.
""",

"4.13 hints": r"""Build the list. The count is len(nums); the distinct count uses a set.

---

`print(len(nums))`, `print(len(set(nums)))`, then the total (a loop, or sum).

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
print(len(set(nums)))
total = 0
for x in nums:
    total = total + x
print(total)
""",

"4.13 reference": r"""The three core collections fit different jobs — choosing the right one makes code
simpler and faster:

- **list** — an **ordered** sequence that may repeat. Use it to keep every value,
  in order (a log, a queue of items to process).
- **set** — an unordered group of **distinct** items with fast membership. Use it
  to drop duplicates or ask "have I seen this?".
- **dict** — a mapping from **keys to values**. Use it to look something up by
  name (a count per word, a price per item).

Ask: do I need order and repeats (list), uniqueness and membership (set), or
lookup by key (dict)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
""",
}
