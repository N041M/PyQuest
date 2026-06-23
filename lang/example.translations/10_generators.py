# PyQuest translations -- language 'example' -- chapter 10_generators -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply example

TRANSLATIONS = {

"10.1 brief": r"""# 10.1 -- yield: a function that pauses

## Concept

A normal function `return`s **once** and is done. A **generator** is a
function that uses `yield` instead: each `yield` hands back **one** value and
**pauses** the function right there. Ask for the next value and it **resumes**
from where it stopped.

```python
def two_words():
    yield "hello"
    yield "world"
```

Calling it does **not** run the body. It hands you a **generator** -- an object
you pull values from, one at a time, usually with a `for` loop:

```python
for w in two_words():
    print(w)        # hello, then world
```

The payoff: a generator produces a sequence **without building the whole list
in memory**. You will feel that in 10.3.

## Example

```python
def count_up(n):
    i = 1
    while i <= n:
        yield i
        i = i + 1
```

`list(count_up(3))` is `[1, 2, 3]` -- each loop pass yields one number, then
pauses until the next is asked for.

## Your task

Define a generator `count_down(n)` that **yields** the whole numbers from `n`
down to `1`, in that order. If `n` is `0` (or less), it yields nothing.

## Done when

- `list(count_down(5))` is `[5, 4, 3, 2, 1]`.
- `list(count_down(1))` is `[1]`; `list(count_down(0))` is `[]`.
- You use `yield` -- so calling `count_down` returns a generator, not a list.
""",

"10.1 hints": r"""A generator looks like a normal function, but it says `yield` where a normal
one would build a result. Each `yield` produces one number.

---

Count with a loop from `n` downwards and `yield` each value. A `while` loop:
start `i` at `n`, `yield i`, then `i = i - 1`, while `i >= 1`. (A
`for i in range(n, 0, -1):` works too.)

---

def count_down(n):
    i = n
    while i >= 1:
        yield i
        i = i - 1
""",

"10.1 reference": r"""A function containing **`yield`** is a **generator function**. Calling it doesn't
run the body — it returns a **generator object** that produces values one at a
time, **pausing** at each `yield` and resuming where it left off when asked for
the next.

- Each `yield value` hands one value to whoever is iterating, then freezes the
  function's state until the next value is requested.
- You consume a generator by iterating it (`for x in gen:`) or with `next(gen)`.
- This differs from `return`, which hands back **one** value and ends the
  function for good.

```python
def two():
    yield 1
    yield 2

for n in two():
    print(n)            # 1, then 2
```
""",

"10.2 brief": r"""# 10.2 -- yield inside a loop

## Concept

The real power of `yield` shows when it sits **inside a loop**: one `yield` line
runs once per pass, streaming a whole transformed sequence -- a value at a time,
never the whole list at once.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` is `["H", "I"]`. The loop walks the input; the `yield`
emits one transformed item each time round, pausing in between.

## Example

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` is `[2, 10, 18]`.

## Your task

Define a generator `squares(n)` that **yields** the squares of the whole
numbers from `0` up to (but not including) `n`: `0, 1, 4, 9, ...`. If `n` is `0`
(or less), it yields nothing.

## Done when

- `list(squares(4))` is `[0, 1, 4, 9]`.
- `list(squares(1))` is `[0]`; `list(squares(0))` is `[]`.
- You use `yield` inside a loop -- not a returned list or comprehension.
""",

"10.2 hints": r"""Walk the numbers `0, 1, ..., n-1` with a loop, and `yield` each one squared.

---

`for i in range(n):` then `yield i * i`. The loop gives you each number; the
yield emits its square and pauses until the next is asked for.

---

def squares(n):
    for i in range(n):
        yield i * i
""",

"10.2 reference": r"""Placing a **`yield` inside a loop** streams a whole sequence: the generator emits
one transformed value per pass, pausing after each and resuming on the next
request.

- `for x in source: yield f(x)` yields `f(x)` for every item — the generator form
  of building a list with a comprehension, but produced lazily.
- Nothing is computed until something iterates the generator, and only as far as
  it's consumed.

```python
def squares(nums):
    for n in nums:
        yield n * n

list(squares([1, 2, 3]))    # [1, 4, 9]
```
""",

"10.3 brief": r"""# 10.3 -- generators are lazy

## Concept

This is the superpower. A generator only does work **when you ask for the next
value**. It never builds the whole sequence up front -- so a generator can be
**endless** and still cost almost nothing until you pull from it.

```python
def naturals():
    i = 0
    while True:        # never stops on its own...
        yield i
        i = i + 1
```

`while True` in a normal function would hang forever. In a generator it is
fine: each `yield` **pauses** the loop until the caller wants one more. You
take only as many as you need:

```python
from itertools import islice
list(islice(naturals(), 4))     # [0, 1, 2, 3] -- then it just stops asking
```

`islice(gen, k)` pulls the first `k` items from a generator and no more. The
generator produces exactly those four, then sits paused.

## Example

`naturals()` above yields `0, 1, 2, 3, ...` with no end. Pulling 3 items gives
`[0, 1, 2]`; pulling 10 gives `[0, 1, ..., 9]`. The same endless generator,
asked for different amounts.

## Your task

Define an **endless** generator `naturals()` that yields the whole numbers
starting at `0`: `0, 1, 2, 3, ...` forever. It must never stop on its own; the
checker only ever pulls a handful of values from it.

## Done when

- The first 5 values of `naturals()` are `[0, 1, 2, 3, 4]`.
- It is endless -- pulling more values just gives more numbers; it never runs
  out.
- You use `yield`, so calling `naturals()` returns a generator.
""",

"10.3 hints": r"""You need a loop that never ends, yielding a counter that goes up by one each
time. The `yield` is what stops it from hanging.

---

Start `i` at `0`. Then `while True:` -- `yield i`, then `i = i + 1`. The loop
"never ends", but each yield pauses it until the next value is wanted.

---

def naturals():
    i = 0
    while True:
        yield i
        i = i + 1
""",

"10.3 reference": r"""Generators are **lazy**: each value is computed only when requested, so a
generator can describe an **endless** sequence and still be useful — you just
take the values you need.

- An infinite `while True: yield n; n += 1` never finishes on its own, but a
  consumer can stop early (a `break`, or `next` called a few times).
- Laziness means a generator holds essentially **no memory** for the sequence — it
  keeps only its current state, not every value — unlike a list that materialises
  all of them.

```python
def naturals():
    n = 0
    while True:
        yield n             # endless, but only as far as asked
        n += 1

g = naturals(); next(g), next(g)   # (0, 1)
```
""",

"10.4 brief": r"""# 10.4 -- a generator remembers

## Concept

Because a generator **pauses** instead of finishing, its local variables stay
alive between `yield`s. A value you build up survives every pause -- the
generator picks up exactly where it left off, accumulator and all.

```python
def tally(words):
    seen = 0
    for w in words:
        seen = seen + 1
        yield seen          # 1, then 2, then 3, ... -- `seen` is remembered
```

`list(tally(["a", "b", "c"]))` is `[1, 2, 3]`. The `seen` counter is not reset
on each pass; it keeps its value across the yields.

## Example

```python
def running_max(nums):
    best = None
    for n in nums:
        if best is None or n > best:
            best = n
        yield best
```

`list(running_max([3, 1, 5]))` is `[3, 3, 5]` -- each item is the largest seen
**so far**.

## Your task

Define a generator `running_total(nums)` that yields the **running sum** of
`nums`: each value is the total of every number up to and including the current
one. An empty list yields nothing.

## Done when

- `list(running_total([3, 1, 2]))` is `[3, 4, 6]`.
- `list(running_total([5]))` is `[5]`; `list(running_total([]))` is `[]`.
- You use `yield`, and a variable that carries the total across the yields.
""",

"10.4 hints": r"""Keep a `total` variable outside the loop, add each number to it inside the
loop, and `yield` the total after each addition.

---

`total = 0` before the loop. Then `for n in nums:` -- `total = total + n`,
then `yield total`. The total is remembered across the yields, so it keeps
growing.

---

def running_total(nums):
    total = 0
    for n in nums:
        total = total + n
        yield total
""",

"10.4 reference": r"""A generator **remembers** its local variables across `yield`s: execution freezes
at the `yield` and every local keeps its value until the next request resumes the
function. This lets a generator **carry state** as it streams.

- A variable updated in the loop (a running total, a previous value) persists
  between yields without any object or global.
- This is what makes a generator a natural **running accumulator** — a running
  sum, for instance, that emits the total so far each step.

```python
def running_sum(nums):
    total = 0
    for n in nums:
        total += n          # total survives across yields
        yield total

list(running_sum([1, 2, 3]))    # [1, 3, 6]
```
""",

"10.5 brief": r"""# 10.5 -- filter while you yield

## Concept

A generator does not have to yield on every pass. Put the `yield` behind an
`if`, and you **filter** the stream as it flows -- skipping the items you don't
want, emitting only the ones you do.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` is `["STOP", "NOW"]`. The loop
visits every word; the `yield` runs only when the `if` is true.

## Example

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` is `[4, 2]`.

## Your task

Define a generator `evens(nums)` that yields only the **even** numbers of
`nums`, keeping their original order. (A number is even when `n % 2 == 0`.) If
none are even, it yields nothing.

## Done when

- `list(evens([1, 2, 3, 4]))` is `[2, 4]`.
- `list(evens([1, 3, 5]))` is `[]`; `list(evens([]))` is `[]`.
- You use `yield` behind an `if` -- not a returned list or comprehension.
""",

"10.5 hints": r"""Loop over every number, but only `yield` the ones that pass an evenness test.

---

`for n in nums:` then `if n % 2 == 0:` and, indented under the if, `yield n`.
The odd numbers simply fall through without yielding.

---

def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n
""",

"10.5 reference": r"""Putting **`yield` behind an `if`** filters a stream as it flows: the generator
emits only the items that pass the test and silently skips the rest — the lazy
counterpart of a comprehension's `if` clause.

- `for x in source: if test(x): yield x` produces a filtered stream without
  building any intermediate list.
- Because it's lazy, it composes cleanly: a filter generator can feed another
  generator, each handling one stage.

```python
def evens(nums):
    for n in nums:
        if n % 2 == 0:
            yield n         # only the evens make it out

list(evens(range(10)))      # [0, 2, 4, 6, 8]
```
""",

"10.6 brief": r"""# 10.6 -- yield from: pass a whole stream along

## Concept

When you want a generator to re-emit **every** item of another iterable, you
could loop and yield each one:

```python
def both(a, b):
    for x in a:
        yield x
    for y in b:
        yield y
```

Python has a shorthand for exactly that inner loop: **`yield from`**.

```python
def both(a, b):
    yield from a        # yield every item of a, one by one
    yield from b        # then every item of b
```

`yield from iterable` is "yield each value this iterable produces". The two
versions above behave identically; `yield from` just says it in one line.

## Example

```python
def repeat_each(items):
    for x in items:
        yield from (x, x)      # yield x, then x again

list(repeat_each([1, 2]))      # [1, 1, 2, 2]
```

## Your task

Define a generator `chain(a, b)` that yields **all** the items of `a`, then
**all** the items of `b`, in order. Use `yield from`. Either list may be empty.

## Done when

- `list(chain([1, 2], [3, 4]))` is `[1, 2, 3, 4]`.
- `list(chain([], [9]))` is `[9]`; `list(chain([], []))` is `[]`.
- You use `yield from`, so calling `chain` returns a generator.
""",

"10.6 hints": r"""You want to re-emit every item of `a`, then every item of `b`. `yield from`
does exactly that for one iterable at a time.

---

Two lines: `yield from a` then `yield from b`. Each one streams that whole list
into the generator's output.

---

def chain(a, b):
    yield from a
    yield from b
""",

"10.6 reference": r"""**`yield from iterable`** re-emits **every** item the iterable produces, as if you
had written a loop of `yield`s. It delegates a whole sub-stream in one line.

- `yield from sub` is equivalent to `for x in sub: yield x`, but shorter and
  faster — and it works with lists, ranges, other generators, any iterable.
- It's the tool for **flattening** or **chaining**: a generator can `yield from`
  several sources in turn to splice their streams together.

```python
def chain(a, b):
    yield from a
    yield from b            # splice two streams into one

list(chain([1, 2], [3, 4]))     # [1, 2, 3, 4]
```
""",

"10.7 brief": r"""# 10.7 -- stop early

## Concept

A generator ends the moment its function ends -- and a plain `return` (with no
value) inside a generator means "stop now, no more items". So a generator can
decide to **finish early**, before the input runs out.

```python
def before_blank(words):
    for w in words:
        if w == "":
            return          # stop the generator here
        yield w
```

`list(before_blank(["a", "b", "", "c"]))` is `["a", "b"]` -- once the blank is
reached, `return` ends the generator and `"c"` is never produced.

## Example

```python
def while_positive(nums):
    for n in nums:
        if n <= 0:
            return
        yield n

list(while_positive([3, 1, -1, 5]))    # [3, 1]
```

## Your task

Define a generator `until_zero(nums)` that yields each number **until it reaches
a `0`**, then stops. The `0` itself, and anything after it, is **not** yielded.
If there is no `0`, it yields the whole list.

## Done when

- `list(until_zero([1, 2, 0, 3]))` is `[1, 2]`.
- `list(until_zero([0, 9]))` is `[]`; `list(until_zero([1, 2, 3]))` is
  `[1, 2, 3]`.
- You use `yield`, and stop early when you hit a `0`.
""",

"10.7 hints": r"""Loop over the numbers. As soon as you see a `0`, stop the whole generator;
otherwise yield the number.

---

`for n in nums:` -- first `if n == 0: return` (this ends the generator), then
`yield n` for everything before the zero.

---

def until_zero(nums):
    for n in nums:
        if n == 0:
            return
        yield n
""",

"10.7 reference": r"""A bare **`return`** inside a generator — or simply reaching the end of the
function — **stops** it: iteration ends and no further values come. `return` in a
generator carries **no value**; it only signals "done".

- This lets a generator **stop early** on a condition: `if x == sentinel: return`
  ends the stream at that point.
- To a `for` loop, a stopped generator is just an iterable that has run out — the
  loop ends naturally (internally, the generator raises `StopIteration`).

```python
def until_zero(nums):
    for n in nums:
        if n == 0:
            return          # stop the stream here
        yield n

list(until_zero([3, 1, 0, 9]))  # [3, 1]
```
""",

"10.8 brief": r"""# 10.8 -- Capstone: a streaming pipeline

## Concept

Nothing new -- this capstone is the chapter in miniature. The real reason
generators matter is that they **compose**: one generator's output is another
generator's input, so data flows through a **pipeline**, one item at a time,
without ever building the full list in between.

A pipeline stage is just a generator that loops over `stream` (any iterable --
a list, or *another generator*) and yields as it goes:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

You will build a source, a filter, and a relabel stage, then wire them
together.

## Example

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## Your task

Define **three** generators:

- `numbers(n)` -- yields `0, 1, ..., n-1` (the source). `n <= 0` yields nothing.
- `keep_even(stream)` -- yields only the even numbers from `stream` (any
  iterable).
- `labelled(stream)` -- yields the string `"#x"` for each `x` in `stream`
  (e.g. `7` becomes `"#7"`).

Each must use `yield`. `keep_even` and `labelled` must work on **any** stream,
including the output of another generator, so they compose.

## Done when

- `list(numbers(4))` is `[0, 1, 2, 3]`; `list(numbers(0))` is `[]`.
- `list(keep_even([1, 2, 3, 4]))` is `[2, 4]`.
- `list(labelled([0, 2]))` is `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` is `["#0", "#2", "#4"]`.
- All three use `yield`, and the filter/relabel stages accept any iterable.
""",

"10.8 hints": r"""Each stage is its own little generator. `numbers` loops over `range(n)` and
yields; `keep_even` loops over `stream` and yields only the evens; `labelled`
loops over `stream` and yields a formatted string. None of them build a list.

---

`keep_even` and `labelled` take a `stream` and `for x in stream:` -- that loop
works whether `stream` is a list or another generator, which is what lets you
nest them. Use an f-string for the label: `yield f"#{x}"`.

---

def numbers(n):
    for i in range(n):
        yield i


def keep_even(stream):
    for x in stream:
        if x % 2 == 0:
            yield x


def labelled(stream):
    for x in stream:
        yield f"#{x}"
""",

"10.8 reference": r"""The capstone composes generators into a **streaming pipeline**: a **source**
generator feeds a **filter** generator, which feeds a **transform** generator.
Each stage is lazy, so values flow through one at a time and nothing is
materialised in full.

- Because each stage consumes the previous lazily, the pipeline processes huge or
  endless data with tiny memory — one item is in flight at a time.
- Stages stay small and independent: swap or add a stage without touching the
  others. This is the generator analogue of composing functions.

```python
def reader(nums):  yield from nums
def keep_pos(src): yield from (n for n in src if n > 0)
def doubled(src):  yield from (n * 2 for n in src)

list(doubled(keep_pos(reader([-1, 2, -3, 4]))))   # [4, 8]
```
""",
}
