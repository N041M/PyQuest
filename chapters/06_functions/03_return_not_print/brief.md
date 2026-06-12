# 6.3 -- return, not print

## Concept

`print()` and `return` look similar when you test by eye, but they do
completely different jobs:

- `print(x)` **shows** `x` on the screen -- and that's all. The caller gets
  nothing.
- `return x` **hands `x` back** to the caller, who can store it, compare it,
  or pass it on.

A function that prints instead of returning actually returns `None` (the
"no value" value). The difference bites the moment someone *uses* the result:

```python
def shout_wrong(word):
    print(word.upper() + "!")     # shows it... returns None

answer = shout_wrong("hi")        # HI! appears, but...
print(answer)                     # None  -- the caller got nothing
```

The rule: **a function's job is to compute and return.** Let the *caller*
decide whether to print.

## Example

```python
def shout(word):
    return word.upper() + "!"

print(shout("hi"))      # HI!  -- printed BY THE CALLER
loud = shout("ok")      # and it can be stored instead
```

## Your task

Define `shout(word)` that **returns** the word in UPPERCASE with a `!` stuck
on the end. (`.upper()` is from 2.7.)

## Done when

- `shout("hi")` returns `"HI!"`; `shout("")` returns `"!"`.
- The value is *returned* -- a version that only prints will fail, because the
  checker receives `None`.
