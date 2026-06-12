# 4.9 -- Looping over a dictionary

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
