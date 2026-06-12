# 6.4 -- Default values

## Concept

A parameter can carry a **default**: the value used when the caller leaves it
out. Write it with `=` in the `def` line:

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Ada")              # "Hello, Ada!"   -- default used
greet("Ada", "Hi")        # "Hi, Ada!"      -- default overridden
```

You have already *used* this: `print(..., sep=" ")` from 1.3 -- `sep` has a
default of one space, which you overrode with `sep=", "`. Now you can build
the same flexibility into your own functions.

Rules: parameters with defaults go **after** the ones without, and the
default is used *only* when the caller omits that argument.

## Example

```python
def repeat(word, times=2):
    return word * times

repeat("ha")        # "haha"
repeat("ha", 3)     # "hahaha"
```

## Your task

Define `greet(name, greeting="Hello")` that returns `"<greeting>, <name>!"` --
exactly: the greeting, a comma and a space, the name, an exclamation mark.

## Done when

- `greet("Ada")` returns `"Hello, Ada!"` (the default at work).
- `greet("Ada", "Hi")` returns `"Hi, Ada!"`.
- Without the default, the one-argument call would crash -- the checker makes
  both kinds of call.
