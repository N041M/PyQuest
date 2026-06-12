# 7.5 -- raise: errors are yours too

## Concept

So far you have *caught* errors that Python raised. You can also **raise your
own** -- and good functions do, the moment they are handed something
senseless:

```python
def checked_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```

`raise` creates the error and throws it right there: the function stops, and
the caller gets the same treatment `int("nope")` gives them -- catchable with
`try`, loud if ignored.

Why raise instead of returning something like `None` or `-1`? Because a wrong
value travels: it gets stored, added, printed, and the crash (if any) happens
far from the real mistake. A raise pins the failure to the moment and the
message -- `ValueError("age cannot be negative")` says exactly what went
wrong, where it went wrong. Garbage in, **error** out -- never garbage out.

## Example

```python
checked_age(30)     # 30
checked_age(0)      # 0    -- zero is a fine age
checked_age(-1)     # ValueError: age cannot be negative
```

## Your task

Define `checked_age(age)` that returns the age unchanged -- but raises a
`ValueError` when it is negative. Give it a message saying what's wrong.

## Done when

- `checked_age(30)` returns `30`; `checked_age(0)` returns `0`.
- `checked_age(-1)` raises `ValueError`.
- You used `raise` -- the checker looks for the statement itself.
