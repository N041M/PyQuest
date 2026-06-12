# 5.9 -- Counting with a dict

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
