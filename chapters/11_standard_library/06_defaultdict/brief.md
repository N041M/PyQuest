# 11.6 -- defaultdict: a default for missing keys

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
