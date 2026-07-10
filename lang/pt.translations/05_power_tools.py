# PyQuest translations -- language 'pt' -- chapter 05_power_tools -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"5.1 brief": r"""# 5.1 -- in: membership testing

## Concept

You met `in` with sets (4.11). It actually works on almost everything:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` is an expression that gives a **boolean** (`True`/`False`), so it
slots straight into an `if`:

```python
if "@" in address:
    print("looks like an email")
```

There is also the opposite, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Compare that with chapter 2, where you used `s.find()` and checked for `-1`.
`in` says the same thing in plain English -- prefer it whenever you only need
*whether* something is there, not *where*.

## Example

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## Your task

Read a word, then a single letter. Print `yes` if the letter appears in the
word, and `no` if it doesn't.

For input `banana`, then `n`:

```
yes
```

## Done when

- A letter that appears prints `yes`; one that doesn't prints `no`.
- It works for a one-letter word too.
- You used the `in` operator (not `.find()` or `.count()`).
""",

"5.1 hints": r"""`letter in word` is already True or False -- put it straight in an `if`.

---

Read the word, read the letter, then branch: `if letter in word:` print yes,
`else:` print no.

---

word = input()
letter = input()
if letter in word:
    print("yes")
else:
    print("no")
""",

"5.1 reference": r"""The **`in`** operator tests membership and yields a boolean, so it drops straight
into an `if` or `while`. `x in c` is `True` when `x` is found in `c`.

- For a **string**, `in` tests for a **substring**: `"cat" in "concatenate"` is
  `True`.
- For a **list** or **tuple**, it tests for an item (scanning the sequence).
- For a **dict** or **set**, it tests for a **key**/member — and is fast
  (hash-based), unlike the linear scan of a list.
- `x not in c` is the readable negation.

```python
"a" in "cat"          # True
3 in [1, 2, 3]        # True
"key" in {"key": 1}   # True  -- tests keys
```
""",

"5.2 brief": r"""# 5.2 -- sum()

## Concept

In 3.12 you wrote the **accumulator pattern** by hand:

```python
total = 0
for x in nums:
    total = total + x
```

That pattern is so common Python ships it as a built-in function:

```python
total = sum(nums)
```

`sum(list_of_numbers)` adds every item and returns the total. On an empty list
it returns `0` -- exactly what your hand-written accumulator started with.

This chapter is full of such **power tools**: built-ins that replace a loop you
have already written yourself once. You earn the shortcut by knowing what it
replaces.

## Example

```python
nums = [3, 1, 4]
print(sum(nums))    # 8
print(sum([]))      # 0
```

## Your task

Read a count `n`, then `n` whole numbers (one per line). Print their total
using `sum()`.

For input `3`, then `3`, `1`, `4`:

```
8
```

## Done when

- `3, 1, 4` prints `8`; negatives work too.
- A count of `0` prints `0`.
- You used `sum()` -- not a hand-written loop this time.
""",

"5.2 hints": r"""Build the list of numbers first (like 4.13), then hand the whole list to one
function call.

---

`sum(nums)` returns the total -- print that. No `total = 0` needed.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
""",

"5.2 reference": r"""**`sum(numbers)`** adds up an iterable of numbers and returns the total — the
accumulator loop of 3.12 as one built-in call.

- It works on any iterable of numbers (list, tuple, range, generator). `sum([])`
  is `0`.
- An optional second argument is the **start** value: `sum(nums, 100)` begins the
  total at 100.
- It only adds numbers; to total something derived from each item, feed it a
  comprehension or generator, e.g. `sum(len(w) for w in words)`.

```python
sum([3, 1, 4])              # 8
sum(range(1, 101))          # 5050
sum(len(w) for w in words)  # total characters
```
""",

"5.3 brief": r"""# 5.3 -- min() and max()

## Concept

Finding the smallest or largest item is another loop you could write by hand
("keep a best-so-far, compare each item") -- and another loop Python ships as
a built-in:

```python
nums = [3, 7, 1]
print(min(nums))    # 1
print(max(nums))    # 7
```

`min()` and `max()` take a list (any non-empty collection, in fact) and return
its smallest / largest item. They also work on strings -- "smallest" then means
earliest in alphabetical order:

```python
min("cab")     # "a"
```

One caution: on an **empty** list they crash (there is no smallest of
nothing), so this puzzle guarantees at least one number.

## Example

```python
nums = [4, -2, 9]
print(min(nums))    # -2
print(max(nums))    # 9
```

## Your task

Read a count `n` (always at least 1), then `n` whole numbers. Print two lines:
the smallest, then the largest.

For input `3`, then `4`, `-2`, `9`:

```
-2
9
```

## Done when

- `4, -2, 9` prints `-2` then `9`.
- A single number prints itself twice (it is both the min and the max).
- You used `min()` and `max()`.
""",

"5.3 hints": r"""Build the list first; then the smallest and largest are each one function call.

---

`print(min(nums))` then `print(max(nums))` -- two lines, two calls.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
""",

"5.3 reference": r"""**`min(items)`** and **`max(items)`** return the smallest and largest item of a
non-empty collection.

- They compare with `<`/`>`, so they work on numbers and on strings (which
  compare lexicographically).
- Called on an **empty** iterable they raise `ValueError`; pass `default=` to
  supply a fallback.
- A `key=` function ranks by a derived value instead of the item itself:
  `max(words, key=len)` returns the **longest** word.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
""",

"5.4 brief": r"""# 5.4 -- sorted()

## Concept

`sorted(nums)` returns a **new list** with the same items in order, smallest
first:

```python
nums = [3, 1, 2]
print(sorted(nums))    # [1, 2, 3]
print(nums)            # [3, 1, 2]  -- the original is untouched
```

Two things to know:

- It returns a *copy*; the original list keeps its order. (There is also
  `nums.sort()`, a method that reorders the list **in place** -- handy later,
  but `sorted()` is the safer default because nothing is changed behind your
  back.)
- Largest-first is one keyword away: `sorted(nums, reverse=True)`.

Duplicates are kept -- sorting reorders, it never removes.

## Example

```python
for x in sorted([3, 1, 2]):
    print(x)
# 1
# 2
# 3
```

## Your task

Read a count `n`, then `n` whole numbers. Print them smallest to largest,
one per line.

For input `4`, then `3`, `1`, `3`, `2`:

```
1
2
3
3
```

## Done when

- `3, 1, 3, 2` prints `1, 2, 3, 3` -- the duplicate `3` appears twice.
- A count of `0` prints nothing.
- You used `sorted()`.
""",

"5.4 hints": r"""Build the list, then loop over `sorted(nums)` instead of `nums`.

---

`for x in sorted(nums):` visits the items smallest-first; print each one.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
""",

"5.4 reference": r"""**`sorted(items)`** returns a **new** list with the items in ascending order,
leaving the original untouched.

- It accepts any iterable and always returns a list. Numbers sort numerically,
  strings lexicographically.
- **`reverse=True`** sorts descending. **`key=`** sorts by a derived value:
  `sorted(words, key=len)` orders by length, `sorted(d.items(), key=lambda kv:
  kv[1])` orders dict pairs by value.
- The list method `lst.sort()` sorts **in place** and returns `None`; use
  `sorted` when you want a new list or are sorting a non-list.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
""",

"5.5 brief": r"""# 5.5 -- enumerate()

## Concept

Sometimes a loop needs both the **item** and its **position**. You could track
a counter by hand, but Python has a built-in for exactly this:

```python
words = ["tea", "milk"]
for i, w in enumerate(words):
    print(i, w)
# 0 tea
# 1 milk
```

Each pass, `enumerate` hands you a pair `(position, item)`, which you unpack
into two variables (4.7) -- the same trick as `for k, v in d.items()`.

Counting from `0` is rarely what you want to *show* a person. The second
argument sets the starting number:

```python
for i, w in enumerate(words, 1):
    print(i, w)
# 1 tea
# 2 milk
```

## Example

```python
for i, ch in enumerate("hi", 1):
    print(f"{i}. {ch}")
# 1. h
# 2. i
```

## Your task

Read a count `n`, then `n` words. Print them as a numbered list starting at 1,
in the format `1. word` (a dot and a space after the number).

For input `3`, then `tea`, `milk`, `sugar`:

```
1. tea
2. milk
3. sugar
```

## Done when

- Three words print as `1. ...`, `2. ...`, `3. ...`.
- A count of `0` prints nothing.
- You used `enumerate()` -- no hand-kept counter.
""",

"5.5 hints": r"""`for i, w in enumerate(words, 1):` gives you the number and the word together,
starting at 1.

---

Inside the loop, build the line with an f-string: `f"{i}. {w}"`.

---

n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
""",

"5.5 reference": r"""**`enumerate(items)`** pairs each item with its position, so a `for` loop gets
both at once — no hand-kept counter.

- `for i, item in enumerate(lst):` binds `i` to the index (from 0) and `item` to
  the value each pass.
- A second argument sets the **starting number**: `enumerate(lst, 1)` numbers
  from 1, handy for human-facing lists.
- It's lazy (yields pairs on demand) and works on any iterable.

```python
for i, name in enumerate(["a", "b"], 1):
    print(i, name)        # 1 a / 2 b
```
""",

"5.6 brief": r"""# 5.6 -- zip(): pairing lists

## Concept

Two lists often belong together item-by-item: names and scores, questions and
answers. `zip()` walks them **in step**, handing you one pair per pass:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Like `enumerate`, each pass gives a pair that you unpack into two variables.
The name is the image of a zipper: two rows of teeth joined one-to-one.

If the lists have different lengths, `zip` stops at the **shorter** one --
extra items on the longer list are simply never visited.

## Example

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## Your task

Read a count `n`, then `n` names, then `n` scores (whole numbers). Print one
line per pair: the name, a space, the score.

For input `2`, then `amy`, `ben`, then `90`, `85`:

```
amy 90
ben 85
```

## Done when

- Two names and two scores print as two `name score` lines, in order.
- A count of `0` prints nothing.
- You used `zip()` to pair the two lists.
""",

"5.6 hints": r"""Read ALL the names into one list first, then all the scores into another --
only then pair them.

---

`for name, score in zip(names, scores):` gives one pair per pass; print the
two with a space between (plain `print(name, score)` does that).

---

n = int(input())
names = []
for _ in range(n):
    names.append(input())
scores = []
for _ in range(n):
    scores.append(input())
for name, score in zip(names, scores):
    print(name, score)
""",

"5.6 reference": r"""**`zip(a, b)`** walks several iterables **in step**, yielding one tuple of
matching items per pass — the *i*-th from each. It pairs up parallel sequences
without indexing.

- `for x, y in zip(xs, ys):` binds `x` and `y` to the matching items each pass.
- It stops at the **shortest** input, so extra items in a longer one are ignored.
- Any number of iterables can be zipped; `dict(zip(keys, values))` builds a dict
  from two parallel lists.

```python
names, scores = ["Ada", "Linus"], [90, 85]
for n, s in zip(names, scores):
    print(n, s)           # Ada 90 / Linus 85
```
""",

"5.7 brief": r"""# 5.7 -- List comprehensions

## Concept

A very common loop shape is *"build a new list by doing something to each
item"*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

Python has a one-line form of exactly that, called a **list comprehension**:

```python
doubled = [x * 2 for x in nums]
```

Read it inside-out: *"for each `x` in `nums`, put `x * 2` in a new list"*. The
square brackets say "I am building a list"; the expression before `for` is
what each item becomes.

It works with anything you can loop over -- including `range`. Reading `n`
numbers (which you have done a dozen times now) collapses to:

```python
nums = [int(input()) for _ in range(n)]
```

## Example

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## Your task

Read a count `n`, then `n` whole numbers. Build a new list where every number
is **doubled**, then print its items one per line.

For input `3`, then `4`, `-1`, `0`:

```
8
-2
0
```

## Done when

- `4, -1, 0` prints `8, -2, 0` -- each doubled, order kept.
- A count of `0` prints nothing.
- You used a list comprehension to build a list.
""",

"5.7 hints": r"""The pattern is  new_list = [<what each item becomes> for x in old_list].

---

`doubled = [x * 2 for x in nums]` -- then a plain for loop prints each item.
(Reading the numbers can be a comprehension too: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
""",

"5.7 reference": r"""A **list comprehension** builds a new list in one expression: for each `x` in
`items`, it evaluates `expr` and collects the results, in order. It is the
build-by-loop-and-append pattern compressed into a line.

- `[expr for x in items]` is equivalent to starting `result = []` and
  `result.append(expr)` in a loop — same result, more direct.
- `expr` can be any expression in `x`: `[n * n for n in nums]`,
  `[w.upper() for w in words]`.
- Comprehensions also build sets (`{...}`) and dicts (`{k: v for ...}`).

```python
[n * n for n in range(5)]       # [0, 1, 4, 9, 16]
[w.upper() for w in ["a", "b"]] # ['A', 'B']
```
""",

"5.8 brief": r"""# 5.8 -- Filtering with comprehensions

## Concept

A comprehension can also **choose** which items to keep. Add an `if` at the
end:

```python
evens = [x for x in nums if x % 2 == 0]
```

Read it: *"each `x` from `nums` -- but only if `x % 2 == 0`"*. Items that fail
the test are simply left out.

The two parts are independent and combine freely:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Reminder from 1.9: `x % 2` is the remainder of dividing by 2, so it is `0`
exactly for even numbers -- and that includes `0` itself and negatives like
`-4`.

## Example

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## Your task

Read a count `n`, then `n` whole numbers. Keep only the **even** ones (in
their original order) and print them one per line.

For input `5`, then `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Done when

- `1, 2, 3, 4, -6` prints `2, 4, -6` -- negatives and zero count as even.
- If no number is even, nothing is printed.
- You used a comprehension with an `if` clause.
""",

"5.8 hints": r""""Even" means the remainder after dividing by 2 is zero: `x % 2 == 0`.

---

Put that test at the end of the comprehension:
`evens = [x for x in nums if x % 2 == 0]` -- then print each item.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
""",

"5.8 reference": r"""Adding an **`if`** to a comprehension keeps only the items that pass the test.
`[x for x in items if test]` collects each `x` for which `test` is true,
**skipping** the rest.

- The `if` clause filters; the leading expression still transforms, so the two
  combine: `[n * n for n in nums if n % 2 == 0]` squares only the evens.
- It replaces the loop-with-an-`if`-and-`append` pattern.
- Don't confuse it with a **conditional expression** in the value position
  (`[a if cond else b for x in items]`), which chooses per item rather than
  filtering.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
""",

"5.9 brief": r"""# 5.9 -- Counting with a dict

## Concept

*"How many times does each thing appear?"* is one of the most useful questions
in programming. The answer is the **tally pattern**: a dict where each key is a
thing you have seen and its value is how many times you have seen it.

The whole trick is one line, built on `.get()` from 4.10:

```python
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
```

Read the line slowly: *"the count for `w` becomes whatever it was -- or 0 if
`w` is new -- plus one."* `.get(w, 0)` is what makes the first sighting work:
there is no entry yet, so it counts up from 0.

After the loop, `counts.get(thing, 0)` answers "how many?" for anything --
including things never seen, which are `0`, not a crash.

## Example

```python
words = ["tea", "milk", "tea"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts.get("tea", 0))     # 2
print(counts.get("cocoa", 0))   # 0
```

## Your task

Read one line of words (separate them with `.split()`, like 4.4), then read a
**query word** on a second line. Print how many times the query appears in the
line.

For input `tea milk tea`, then `tea`:

```
2
```

## Done when

- `tea milk tea` with query `tea` prints `2`; query `milk` prints `1`.
- A query that never appears prints `0` (no crash).
- You built a dict tally (not a one-off scan).
""",

"5.9 hints": r"""Split the line into a list of words, then loop over it building the tally dict.

---

The tally line is  counts[w] = counts.get(w, 0) + 1  -- and the final answer is
another .get with a default: counts.get(query, 0).

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
query = input()
print(counts.get(query, 0))
""",

"5.9 reference": r"""The **tally** pattern counts how many times each distinct thing appears, using a
dict whose keys are the things and whose values are running counts.

- For each item, `counts[k] = counts.get(k, 0) + 1` reads the current count
  (`0` the first time the key is seen, via `.get`'s default) and writes one more.
- Start from an empty dict `{}`; keys appear as they're first encountered.
- The standard-library `collections.Counter` does this in one step, but the
  `.get(k, 0) + 1` idiom shows exactly what's happening.

```python
counts = {}
for w in ["a", "b", "a"]:
    counts[w] = counts.get(w, 0) + 1   # {'a': 2, 'b': 1}
```
""",

"5.10 brief": r"""# 5.10 -- Capstone: word report

## Concept

Nothing new this time -- this puzzle combines the chapter (and chapter 4) into
one small, real program: a **word frequency report**, the heart of every
"most common words" feature you have ever seen.

The pieces, all of which you have:

- `.split()` -- the line into words (4.4)
- the tally pattern -- count each word (5.9)
- `sorted()` -- order the report (5.4). One new convenience: looping over a
  dict visits its **keys**, so `sorted(counts)` is simply the keys in
  alphabetical order.
- printing a word and its count on one line (1.2)

## Example

For the line `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## Your task

Read one line of words. Print one line per **distinct** word -- the word, a
space, and how many times it appeared -- in **alphabetical** order.

For input `tea milk tea`:

```
milk 1
tea 2
```

## Done when

- `tea milk tea` prints `milk 1` then `tea 2` -- distinct words, alphabetical.
- A single repeated word prints one line with its full count.
- An empty line prints nothing.
- You used a dict tally and `sorted()`.
""",

"5.10 hints": r"""Three steps: split the line, tally the words (5.9), then print -- and
`sorted(counts)` gives the dict's keys in alphabetical order.

---

After the tally loop:  `for w in sorted(counts): print(w, counts[w])`.

---

words = input().split()
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
for w in sorted(counts):
    print(w, counts[w])
""",

"5.10 reference": r"""A **word-frequency report** composes the chapter's tools into a small pipeline:

1. **`split()`** the text into a list of words;
2. **tally** them into a dict of `word -> count` with `counts.get(w, 0) + 1`;
3. **`sorted`** the `dict.items()` to order the report — by word, or by count
   with `key=lambda kv: kv[1]` (and `reverse=True` for most-frequent first).

Each step is a tool you've met; the skill is seeing that a real task is their
composition.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
""",
}
