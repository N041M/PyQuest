# PyQuest translations -- language 'pt' -- chapter 11_standard_library -- each puzzle's brief / hints / reference.
# Edit each value to your language; leave it as the English to keep
# English. Keep each value's markdown and ``` code blocks exactly -- only
# the prose is localized (literals the grader checks, like
#   print("Hello, output"), stay as they are).
# Pure data: read with ast.literal_eval, never executed. This folder is
# one file per chapter; after editing any of them run:
#     python3 tools/lang_worksheet.py apply pt

TRANSLATIONS = {

"11.1 brief": r"""# 11.1 -- import: bring in a module

## Concept

Python ships a large **standard library**: ready-made tools grouped into
**modules**. You don't get them for free in every file -- you **import** the
module you need, then reach its contents through its name.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
```

- `import math` runs once at the top of the file and binds the name `math` to
  the whole module.
- After that, `math.sqrt` is the square-root function and `math.pi` the
  constant -- `module.name` reaches anything the module provides.

The point of importing is that someone has already written and tested these, so
you call `math.sqrt` instead of re-deriving a square root yourself.

## Example

```python
import math

def diagonal(side):
    return math.sqrt(2) * side
```

## Your task

Define `hypotenuse(a, b)` that returns the length of the hypotenuse of a
right triangle with legs `a` and `b` -- the square root of `a*a + b*b` --
using **`math.sqrt`** from the imported `math` module.

## Done when

- `hypotenuse(3, 4)` returns `5.0`, `hypotenuse(5, 12)` returns `13.0`.
- `hypotenuse(0, 0)` returns `0.0`.
- The square root comes from `math.sqrt`, via `import math`.
""",

"11.1 hints": r"""The very first line of the file makes the module available: `import math`. After
that you can use anything it provides as `math.something`.

---

`math.sqrt(x)` returns the square root of `x`. You want the square root of
`a*a + b*b`. Put the `import math` at the top, then write the function.

---

import math


def hypotenuse(a, b):
    return math.sqrt(a * a + b * b)
""",

"11.1 reference": r"""An **`import`** statement loads a **module** — a file of ready-made code from the
standard library — and binds it to a name. `import math` makes the module object
available as `math`, and its contents are reached through it: `math.sqrt`,
`math.pi`, `math.floor`.

- The statement runs **once**, conventionally at the **top** of the file; the
  name then refers to the whole module for the rest of the program.
- **`module.name`** (attribute access) looks a function or constant up *on* the
  module, which keeps each module's names in their own namespace — `math.pi` and
  your own `pi` never collide.
- Importing a name that doesn't exist raises `ModuleNotFoundError`; the module's
  code runs the first time it is imported and is cached thereafter.
- The standard library ships with Python ("batteries included"), so these
  modules need no installation — just the import.

```python
import math

math.sqrt(9)     # 3.0
math.pi          # 3.141592653589793
math.floor(2.7)  # 2
```
""",

"11.2 brief": r"""# 11.2 -- from import: pull out one name

## Concept

`import math` brings in the *whole* module and you reach into it with
`math.something`. Often you want just one tool, used by its plain name. The
**`from ... import ...`** form does that:

```python
from math import gcd

gcd(12, 18)      # 6  -- called directly, no math. prefix
```

- `from math import gcd` binds the single name `gcd` into your file.
- You then call it as `gcd(...)`, not `math.gcd(...)`.
- You can pull several at once: `from math import gcd, sqrt, pi`.

`gcd(a, b)` is the **greatest common divisor** -- the largest integer that
divides both. It's exactly what you need to reduce a fraction to lowest terms:
divide the top and bottom by their gcd.

## Example

```python
from math import gcd

def both_divisible_by(a, b):
    return gcd(a, b)
```

## Your task

Using **`from math import gcd`**, define `simplify(num, den)` that returns the
fraction `num/den` reduced to lowest terms, as a tuple `(top, bottom)`: divide
both `num` and `den` by their `gcd`.

## Done when

- `simplify(6, 8)` returns `(3, 4)`, `simplify(10, 5)` returns `(2, 1)`.
- `simplify(7, 7)` returns `(1, 1)`.
- The gcd comes from `math`, imported with `from math import gcd`.
""",

"11.2 hints": r"""Start the file with `from math import gcd`. Now `gcd` is a function you can call
directly, no `math.` in front of it.

---

Find `g = gcd(num, den)`, then return the tuple `(num // g, den // g)`. Use `//`
(integer division) so the result stays whole numbers.

---

from math import gcd


def simplify(num, den):
    g = gcd(num, den)
    return (num // g, den // g)
""",

"11.2 reference": r"""The **`from module import name`** form binds a specific name from a module
*directly* into your file, so it's called without the module prefix. `from math
import gcd` makes `gcd` a plain name; you write `gcd(12, 18)`, not
`math.gcd(...)`.

- Several names at once: `from math import gcd, sqrt, pi`.
- It imports only what you name — `math.floor` is **not** available unless you
  also import `floor`. (`import math` brings everything but keeps the prefix; the
  two forms trade convenience against namespace clarity.)
- The whole module still runs and is cached; you've just chosen which of its
  names land in your namespace. Because the name arrives bare, it can **shadow**
  one of your own — `from math import e` would hide a variable called `e`.

```python
from math import gcd, sqrt

gcd(12, 18)    # 6
sqrt(16)       # 4.0
```
""",

"11.3 brief": r"""# 11.3 -- import as: rename on the way in

## Concept

Sometimes a module's name is long, or clashes with one of yours. **`import ... as
...`** brings the module in under a name **you** choose:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` binds the module to `stats`; `stats.mean` is
  exactly `statistics.mean`.
- The alias is just a local nickname -- the module is unchanged, and only your
  file sees the new name.
- This is why you'll see conventional aliases everywhere (`import numpy as np`);
  here we shorten `statistics`.

The **`statistics`** module does the common averages for you. `stats.mean(nums)`
is the arithmetic mean -- the sum divided by the count -- without you writing
`sum(nums) / len(nums)`.

## Example

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## Your task

Using **`import statistics as stats`**, define `average(nums)` that returns the
mean of the list `nums`, computed with `stats.mean`.

## Done when

- `average([2, 4, 6])` returns `4`, `average([1, 2])` returns `1.5`.
- `average([5])` returns `5`.
- The mean comes from `statistics.mean`, imported as `stats`.
""",

"11.3 hints": r"""Begin with `import statistics as stats`. From then on, `stats` is your name for
the module.

---

`stats.mean(nums)` returns the average of the list. Your whole function can be
one line that returns it.

---

import statistics as stats


def average(nums):
    return stats.mean(nums)
""",

"11.3 reference": r"""**`import module as alias`** imports a module but binds it under a name of your
choosing. `import statistics as stats` makes the module available as `stats`;
`stats.mean` *is* `statistics.mean` — the alias changes only the local name, not
the module.

- Use it to **shorten** a long module name or to **avoid a clash** with one of
  your own names. The convention-driven aliases you'll meet (`import numpy as
  np`) are exactly this.
- The same `as` works on a single name from a from-import: `from statistics
  import mean as avg`.
- Only your file sees the alias; other modules keep their own names for it.

```python
import statistics as stats

stats.mean([1, 2, 3, 4])     # 2.5
stats.median([1, 5, 2])      # 2
```
""",

"11.4 brief": r"""# 11.4 -- random: reproducible chance

## Concept

The **`random`** module produces pseudo-random values: `random.randint(1, 6)`
rolls a die, `random.shuffle(lst)` reorders a list in place. They're *pseudo*-
random -- computed from an internal state -- which means you can make them
**repeatable** by fixing that state with a **seed**:

```python
import random

random.seed(42)
random.shuffle(deck)     # always the same order for seed 42
```

- `random.seed(n)` sets the starting point. After the same seed, the same calls
  produce the same results, every run, every machine.
- `random.shuffle(lst)` shuffles **in place** (it returns `None`), so shuffle a
  copy if you need to keep the original.

Seeding is how a game replays a level, or a test checks "random" code.

## Example

```python
import random

def pick(options, seed):
    random.seed(seed)
    return random.choice(options)
```

## Your task

Define `shuffled(items, seed)` that returns a **new** list with the items of
`items` shuffled, made repeatable by seeding with `seed` **before** shuffling.
Don't change the original `items`.

## Done when

- `shuffled(items, seed)` gives the same result every time for the same
  `items` and `seed`.
- The original list passed in is left unchanged (shuffle a copy).
- `shuffled([], 1)` returns `[]`.
""",

"11.4 hints": r"""You need three steps: copy the list, seed the generator, shuffle the copy.
`out = list(items)` makes the copy so the original is safe.

---

`random.seed(seed)` fixes the starting point; `random.shuffle(out)` reorders
`out` in place (it returns None, so don't `return random.shuffle(...)`). Return
`out` afterwards.

---

import random


def shuffled(items, seed):
    out = list(items)
    random.seed(seed)
    random.shuffle(out)
    return out
""",

"11.4 reference": r"""The **`random`** module generates pseudo-random values from an internal state:
`random.randint(a, b)` (an integer in `[a, b]`), `random.choice(seq)` (a random
item), `random.shuffle(lst)` (reorder a list **in place**), `random.random()` (a
float in `[0, 1)`).

- The numbers are deterministic functions of the state, so **`random.seed(n)`**
  makes them **repeatable**: after the same seed, the same calls yield the same
  results on every run and machine. Seed once, before the draws you want to
  reproduce.
- `random.shuffle` mutates its argument and returns `None` — shuffle a **copy**
  (`out = list(items)`) to keep the original, and never `return
  random.shuffle(...)`.
- The default (unseeded) generator is seeded from the OS, so without a seed each
  run differs. `random` is **not** for cryptography — use the `secrets` module
  for tokens and passwords.

```python
import random

random.seed(42)
random.randint(1, 6)     # same value every run for seed 42
deck = [1, 2, 3, 4]
random.shuffle(deck)     # deck reordered in place
```
""",

"11.5 brief": r"""# 11.5 -- Counter: tally in one step

## Concept

Back in chapter 5 you tallied by hand: `counts[k] = counts.get(k, 0) + 1`. The
**`collections`** module ships that pattern, written and tested, as **`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` walks any iterable and returns a count of each distinct item.
- A `Counter` **is** a dict (it's a subclass), so `counts[x]` and
  `for k, v in counts.items()` work exactly as you'd expect -- and it compares
  equal to the plain dict with the same counts.
- It even handles the missing key: `counts["zzz"]` is `0`, not a `KeyError`.

This is the standard library's promise: the loop you'd write is already a tool.

## Example

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## Your task

Using **`Counter`** from `collections`, define `tally(items)` that returns a
count of how many times each item appears in the list `items`.

## Done when

- `tally(["a", "b", "a"])` equals `{"a": 2, "b": 1}`.
- `tally([])` equals `{}`.
- The counting is done by `Counter`, not a hand-written loop.
""",

"11.5 hints": r"""`from collections import Counter` at the top. `Counter` does the whole tally when
you hand it the list.

---

`Counter(items)` already returns the counts, and a Counter compares equal to the
plain dict of the same counts -- so you can return it directly.

---

from collections import Counter


def tally(items):
    return Counter(items)
""",

"11.5 reference": r"""**`Counter`** (from the **`collections`** module) is a `dict` subclass that
tallies an iterable in one call: `Counter(items)` returns a mapping of each
distinct item to how many times it appears — the `counts.get(k, 0) + 1` loop,
already written.

- Being a dict, it supports everything a dict does (`c[key]`, `c.items()`,
  `key in c`) and compares **equal** to a plain dict with the same counts.
- A **missing** key reads as `0` rather than raising `KeyError`, which suits
  counting.
- **`c.most_common(n)`** returns the `n` highest-count `(item, count)` pairs,
  already sorted — the report step for free. Counters also add and subtract
  (`c1 + c2`) to combine tallies.

```python
from collections import Counter

c = Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
c["a"]                    # 3
c["z"]                    # 0  -- no KeyError
c.most_common(1)          # [('a', 3)]
```
""",

"11.6 brief": r"""# 11.6 -- defaultdict: a default for missing keys

## Concept

To group items in a plain dict you must first check whether the key exists:

```python
if length not in groups:
    groups[length] = []
groups[length].append(word)
```

**`defaultdict`** removes that ceremony. You give it a **factory** -- a function
that makes the default value -- and it calls the factory automatically the first
time you touch a missing key:

```python
from collections import defaultdict

groups = defaultdict(list)     # missing key -> a fresh []
groups[5].append("hello")      # no setup needed
```

- `defaultdict(list)` makes an empty list for any new key, so `.append` just
  works.
- `defaultdict(int)` makes `0` for any new key -- a tally without `.get`.
- It's a real dict otherwise; convert with `dict(groups)` if you want a plain one.

## Example

```python
from collections import defaultdict

def by_first_letter(words):
    groups = defaultdict(list)
    for w in words:
        groups[w[0]].append(w)
    return dict(groups)
```

## Your task

Using **`defaultdict`** from `collections`, define `group_by_length(words)` that
returns a dict mapping each word **length** to the list of words of that length,
in their original order.

## Done when

- `group_by_length(["hi", "ok", "bye"])` equals `{2: ["hi", "ok"], 3: ["bye"]}`.
- `group_by_length([])` equals `{}`.
- Grouping uses a `defaultdict(list)`, not a manual "if key in dict" check.
""",

"11.6 hints": r"""`from collections import defaultdict`, then `groups = defaultdict(list)`. The
`list` is the factory: every new key starts as an empty list.

---

Loop the words; for each, `groups[len(w)].append(w)`. The key is the length,
the value is the growing list. Return `dict(groups)` at the end.

---

from collections import defaultdict


def group_by_length(words):
    groups = defaultdict(list)
    for w in words:
        groups[len(w)].append(w)
    return dict(groups)
""",

"11.6 reference": r"""**`defaultdict`** (from **`collections`**) is a `dict` that supplies a default for
a missing key automatically. You pass it a **factory** — a zero-argument callable
that builds the default — and the first time you read or touch an absent key, it
calls the factory, stores the result, and uses it.

- `defaultdict(list)` makes a fresh `[]` for each new key, so `d[k].append(x)`
  works with no "if key not in d" setup — the grouping idiom.
- `defaultdict(int)` makes `0` for each new key, so `d[k] += 1` tallies.
- Only **lookup** of a missing key triggers the factory; it's otherwise an
  ordinary dict. `dict(d)` converts to a plain dict, and a *genuinely* missing
  key still reads as the default rather than raising.

```python
from collections import defaultdict

groups = defaultdict(list)
groups[5].append("hello")    # key 5 auto-starts as []
groups                       # defaultdict(<class 'list'>, {5: ['hello']})
```
""",

"11.7 brief": r"""# 11.7 -- json: data as text

## Concept

To save data to a file or send it over a network, you need it as **text**.
**JSON** is the near-universal text format for structured data, and the **`json`**
module converts both ways:

```python
import json

json.dumps({"name": "Ada", "score": 90})   # '{"name": "Ada", "score": 90}'
json.loads('{"ok": true}')                  # {'ok': True}
```

- `json.dumps(obj)` -- "dump string" -- turns a Python dict/list/number/str into
  a JSON **string**.
- `json.loads(text)` -- "load string" -- parses a JSON string back into Python
  values.
- The two are inverses: `json.loads(json.dumps(x))` gives `x` back.

Note JSON's spelling differs slightly from Python's (`true`/`false`/`null`), which
is exactly why you let the module handle it instead of formatting by hand.

## Example

```python
import json

def parse(text):
    return json.loads(text)
```

## Your task

Using **`json.dumps`**, define `to_json(record)` that returns the JSON string
for the dictionary `record`.

## Done when

- `to_json({"a": 1, "b": 2})` returns `'{"a": 1, "b": 2}'`.
- `to_json({})` returns `'{}'`.
- The string is produced by `json.dumps`, not built by hand.
""",

"11.7 hints": r"""`import json` at the top. The function you want is `json.dumps`, which takes a
Python object and returns its JSON text.

---

`json.dumps(record)` does the whole job. The function body is one line that
returns it.

---

import json


def to_json(record):
    return json.dumps(record)
""",

"11.7 reference": r"""**JSON** (JavaScript Object Notation) is the standard **text** format for
structured data, and the **`json`** module converts Python values to and from it.

- **`json.dumps(obj)`** ("dump string") serializes a Python `dict`, `list`,
  `str`, number, `bool`, or `None` into a JSON string. Keys become strings, and
  Python's `True`/`False`/`None` are written as JSON's `true`/`false`/`null`.
- **`json.loads(text)`** ("load string") parses a JSON string back into Python
  values. The two are inverses: `json.loads(json.dumps(x)) == x`.
- `dumps` takes options — `indent=2` pretty-prints, `sort_keys=True` orders the
  keys. The file-oriented `json.dump(obj, f)` / `json.load(f)` write and read a
  file object directly.
- Only JSON-compatible types serialize; a `set` or a custom object raises
  `TypeError` unless you tell `dumps` how to convert it.

```python
import json

json.dumps({"name": "Ada", "ok": True})   # '{"name": "Ada", "ok": true}'
json.loads('[1, 2, 3]')                    # [1, 2, 3]
```
""",

"11.8 brief": r"""# 11.8 -- Capstone: a stats summary from JSON

## Concept

This chapter's real lesson is that everyday work is **composing library tools**:
let one module read the data, another crunch it, and return the result. Here you
combine two of the modules you just met.

The input is a **JSON string** holding a list of numbers, e.g. `"[4, 8, 15, 16]"`.
You'll:

1. parse it with **`json.loads`** into a Python list,
2. summarize it with **`statistics`** and the built-ins `max` / `min`,
3. return a plain dict of the results.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## Your task

Define `summary(numbers_json)` that takes a JSON string of a list of numbers and
returns a dict with these keys:

- `"count"` -- how many numbers (`len`),
- `"mean"` -- their mean (`statistics.mean`),
- `"max"` -- the largest (`max`),
- `"min"` -- the smallest (`min`).

Parse the input with `json.loads`. Assume at least one number.

## Done when

- `summary("[2, 4, 6]")` equals
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` equals `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- The input is parsed with `json.loads`, not by hand.
""",

"11.8 hints": r"""Two imports at the top: `import json` and `import statistics`. First turn the
text into a list with `json.loads(numbers_json)`.

---

Once you have the list `nums`, build the dict: `len(nums)` for count,
`statistics.mean(nums)` for mean, and the built-in `max(nums)` / `min(nums)`.

---

import json
import statistics


def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {
        "count": len(nums),
        "mean": statistics.mean(nums),
        "max": max(nums),
        "min": min(nums),
    }
""",

"11.8 reference": r"""The capstone is the chapter's real point: **composing standard-library modules**
into a small pipeline rather than writing each step from scratch.

- **Read** with `json` — `json.loads(text)` turns the JSON input into Python
  values (here, a list of numbers).
- **Summarize** with `statistics` and the built-ins — `statistics.mean(nums)` for
  the average, `max(nums)` / `min(nums)` for the extremes, `len(nums)` for the
  count.
- **Return** a plain `dict`, so the caller gets ordinary Python values to use.

Each stage is a module someone else wrote and tested; your job is to wire them
together. That is what most real programs are — glue between well-made libraries.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
""",
}
