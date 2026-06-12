# 3.11 -- break and continue

## Concept

Two keywords change how a loop flows:

- **`break`** stops the loop **immediately** -- no more passes.
- **`continue`** skips the **rest of the current pass** and jumps to the next
  one.

```python
for ch in "a,b,c":
    if ch == ",":
        continue        # skip commas
    print(ch)
# prints a, b, c (commas skipped)

for n in range(100):
    if n == 3:
        break           # stop the whole loop at 3
    print(n)
# prints 0, 1, 2
```

`continue` skips one item; `break` ends the loop.

## Example

```python
for ch in "abxcd":
    if ch == "x":
        break
    print(ch)
# prints a, b   (stops at x)
```

## Your task

Read a word and loop over its characters:

- **skip** the letter `o` (use `continue` -- do not print it),
- **stop** completely at the letter `x` (use `break` -- print nothing from `x`
  onward),
- print every other character on its own line.

For input `boxes` the output is:

```
b
```

(`b`, then `o` is skipped, then `x` stops the loop.)

## Done when

- `boxes` prints `b`; `good` prints `g` then `d` (the `o`s skipped); `abc` prints
  `a`, `b`, `c`.
