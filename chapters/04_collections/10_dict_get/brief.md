# 4.10 -- Missing keys and .get()

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
