# 7.1 -- try / except

## Concept

You have *caused* plenty of errors by now. Time to **handle** one.

When Python hits something impossible -- like `int("hello")` -- it **raises an
exception**: the normal flow stops dead and, unless someone deals with it, the
program crashes with a traceback. `try`/`except` is how you deal with it:

```python
try:
    n = int(text)
    print("a number!")
except ValueError:
    print("not a number")
```

How it runs:

- The `try` block runs normally -- **until** a line raises.
- If nothing raises, the `except` block is skipped entirely.
- If `int(text)` raises a `ValueError` (its complaint about unconvertible
  text), the rest of the `try` block is abandoned and the `except` block
  runs instead. **No crash.**

The program *recovers*: it chose what failure means instead of falling over.

## Example

Input `7` prints `14`. Input `seven` prints `not a number` -- the same code,
no crash either way.

## Your task

Read one line. If it converts to a whole number, print that number **doubled**.
If it doesn't, print exactly `not a number`. (This is a script puzzle again:
`input()` and `print()` are back.)

## Done when

- `7` prints `14`; `-3` prints `-6`.
- `seven` and `12abc` print `not a number` -- and the program exits cleanly,
  no traceback.
- You used `try`/`except` -- the checker requires the real thing.
