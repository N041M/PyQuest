# 8.1 -- Opening a file

## Concept

So far every value came from a literal you typed or from `input()`. Real
programs also read **files** -- text already sitting on disk.

`open(name)` hands you a *file object*. The clean way to use one is a `with`
block:

```python
with open("note.txt") as f:
    text = f.read()
```

- `with open(...) as f:` opens the file and binds it to `f`;
- `f.read()` returns the file's **entire contents** as one string;
- when the block ends, Python **closes the file for you** -- even if the code
  inside raised. That automatic close is the whole reason to prefer `with`
  over a bare `open()`.

The file is found relative to where the program runs, so `"note.txt"` means "a
file called note.txt next to me".

## Example

If `note.txt` contains:

```
buy milk
call sam
```

then `text` is the string `"buy milk\ncall sam\n"` -- newlines and all.

## Your task

A file named `note.txt` sits beside your program. Read its whole contents and
print them.

## Done when

- The program prints exactly what `note.txt` contains.
- It works whatever the file holds -- one line, many lines, or nothing.
- You opened the file with a `with` statement.
