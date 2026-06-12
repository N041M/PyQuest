# 7.8 -- Capstone: a robust calculator

## Concept

One `try` can have **several** `except` blocks -- one per kind of failure,
each choosing its own recovery:

```python
try:
    ...
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
```

Whichever error is raised picks its matching block; the others are skipped.
This capstone wires the whole chapter into the classic exercise: a calculator
that **cannot be crashed** by its input. It also needs `split` (4.4),
indexing (2.1), `elif` (3.4), and `/` (1.9).

## Example

```
input "8 + 5"   ->  13
input "9 / 2"   ->  4.5
input "9 / 0"   ->  cannot divide
input "two * 3" ->  bad number
input "8 ? 5"   ->  unknown op
```

## Your task

Read one line of the form `<number> <op> <number>` (three parts separated by
spaces). For ops `+`, `-`, `*` print the whole-number result; for `/` print
the float result. Handle every failure:

- a part that isn't a whole number -> print `bad number`
- division by zero -> print `cannot divide`
- any other op symbol -> print `unknown op`

## Done when

- `8 + 5` -> `13`, `9 / 2` -> `4.5`, `3 * -2` -> `-6`.
- `9 / 0` -> `cannot divide`; `two * 3` -> `bad number`; `8 ? 5` ->
  `unknown op`.
- No input crashes it: each failure prints its own message via `except`
  blocks (and an `else`/`elif` for the unknown op).
