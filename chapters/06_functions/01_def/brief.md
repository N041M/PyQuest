# 6.1 -- def: your first function

## Concept

A **function** is a named, reusable piece of code. You have *called* functions
all along -- `print()`, `len()`, `sorted()`. Now you get to **define** your
own:

```python
def double(x):
    return x * 2
```

- `def` starts the definition; `double` is the name you choose.
- `x` is a **parameter**: a variable that receives whatever value the caller
  passes in.
- `return` hands a value **back to the caller**. Calling `double(3)` is then
  an expression worth `6`:

```python
result = double(3)     # result is 6
print(double(10))      # 20
```

**This chapter checks your code differently.** Until now your file *ran* and
printed. From here, the checker **imports** your file and **calls your
functions directly**, passing in many different arguments -- so there is no
`input()` and no `print()` needed at all. Your file just defines the function.

## Example

```python
def double(x):
    return x * 2
```

That whole file is a valid answer to this puzzle: it defines `double`, and
`double(21)` returns `42`.

## Your task

Define a function `double(x)` that **returns** `x` doubled.

## Done when

- `double(3)` returns `6`, `double(0)` returns `0`, `double(-5)` returns `-10`.
- Your file only defines the function -- no `input()`, no `print()`.
