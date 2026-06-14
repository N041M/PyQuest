# 8.5 -- Append, don't overwrite

## Concept

Mode `"w"` is ruthless: it **empties** the file before writing. That's wrong
when you want to *add* to a file -- a log you keep growing, say. For that there
is mode `"a"` (for *append*):

```python
with open("log.txt", "a") as f:
    f.write("another line\n")
```

`"a"` leaves everything already in the file untouched and writes your new text
**after** it (and if the file doesn't exist yet, `"a"` simply creates it).
Same `.write()`, same need to add your own `"\n"` -- only the mode letter
changes, and that one letter is the whole difference between "add to" and
"wipe and replace". The whole point of `"a"` is that you *don't* read the file
first -- you just write at the end.

## Example

If `log.txt` already contains:

```
woke up
ate
```

then appending the line `ran` leaves it holding `woke up`, `ate`, `ran` -- all
three, in order.

## Your task

A file `log.txt` already exists. Read one line of text from input (`input()`)
and **append** it to `log.txt` as a new line, keeping everything already there.

## Done when

- The original contents of `log.txt` are still present, in order.
- The new entry is added as its own line at the end.
- Using `"w"` would erase the old lines -- so you must use `"a"`.
