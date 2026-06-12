# 4.8 -- Dictionaries

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
