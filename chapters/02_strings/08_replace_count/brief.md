# 2.8 -- Replacing and counting

## Concept

Two more string methods:

- `s.replace(old, new)` returns a copy of `s` with **every** occurrence of `old`
  swapped for `new`:
  ```python
  "banana".replace("a", "o")   # "bonono"
  ```
- `s.count(sub)` returns **how many times** `sub` appears (a number):
  ```python
  "banana".count("a")          # 3
  ```

If `old` is not present, `replace` returns the string unchanged; if `sub` is not
present, `count` returns `0`.

## Example

```python
s = "foo bar"
print(s.replace("o", "0"))   # f00 bar
print(s.count("o"))          # 2
```

## Your task

Read a line and print two lines:

1. the line with every letter `o` replaced by a zero `0`
2. how many `o`s were in the **original** line

For input `foobar` the output is:

```
f00bar
2
```

## Done when

- For `foobar` the lines are `f00bar` and `2`.
- For a line with no `o` it prints the line unchanged and `0`. The checker tries
  it.
