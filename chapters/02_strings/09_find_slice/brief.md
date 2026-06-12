# 2.9 -- Finding a position

## Concept

`s.find(sub)` returns the **index** where `sub` first appears -- a number you can
then use for slicing. (If `sub` is not found, it returns `-1`.)

```python
s = "name=Sam"
i = s.find("=")    # 4
print(i)           # 4
print(s[i+1:])     # Sam   (everything after the "=")
```

So `find` locates a marker, and a slice extracts the part you want relative to it.
Here `s[i+1:]` means "from one past the `=` to the end".

## Example

```python
s = "color=blue"
i = s.find("=")
print(s[i+1:])     # blue
```

## Your task

Each input is a line shaped like `key=value` (with one `=`). Print just the
**value** -- everything after the `=`.

For input `color=blue` the output is:

```
blue
```

## Done when

- For `color=blue` it prints `blue`.
- For `x=1` it prints `1`; for `a=` it prints an empty line; for `k=a=b` it prints
  `a=b` (only the first `=` splits it). The checker tries these.
