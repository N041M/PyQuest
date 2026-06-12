# 3.3 -- if / else

## Concept

`else` gives an `if` a second branch: code to run when the condition is
**False**. Exactly one of the two blocks runs.

```python
if temperature > 30:
    print("hot")
else:
    print("not hot")
```

The `else:` lines up with the `if` (same indentation), and its block is indented
just like the `if` block.

## A reminder

`n % 2` is the remainder when `n` is divided by 2 (you met `%` in chapter 1). A
number is **even** exactly when `n % 2 == 0`.

## Example

```python
n = 7
if n % 2 == 0:
    print("even")
else:
    print("odd")
# prints: odd
```

## Your task

Read a whole number and print `even` if it is even, or `odd` if it is not.

For input `10` the output is:

```
even
```

## Done when

- Even numbers print `even`, odd numbers print `odd`.
- It works for `0` (even) and for negative numbers too.
