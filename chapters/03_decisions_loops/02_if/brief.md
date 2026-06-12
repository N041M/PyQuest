# 3.2 -- if

## Concept

An **`if` statement** runs a block of code **only when** a condition is `True`:

```python
if condition:
    do_something()
    do_more()
```

Two things to notice:

1. The line ends with a **colon** `:`.
2. The lines that should run when the condition is true are **indented** (use 4
   spaces). The indentation is how Python knows which lines belong to the `if`.
   When the condition is `False`, the indented lines are skipped.

```python
age = 20
if age >= 18:
    print("adult")     # runs only when age >= 18
```

If `age` were `15`, nothing would print.

## Common misconception

Indentation is not decoration in Python -- it defines the block. Forgetting to
indent (or mixing spaces) is a syntax error.

## Your task

Read a whole number. **If it is negative**, print `negative`. If it is not
negative, print nothing at all.

For input `-4` the output is:

```
negative
```

For input `7` there is no output.

## Done when

- A negative number prints `negative`.
- Zero and positive numbers print nothing (`0` is not negative).
