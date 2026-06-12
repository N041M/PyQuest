# 5.7 -- List comprehensions

## Concept

A very common loop shape is *"build a new list by doing something to each
item"*:

```python
doubled = []
for x in nums:
    doubled.append(x * 2)
```

Python has a one-line form of exactly that, called a **list comprehension**:

```python
doubled = [x * 2 for x in nums]
```

Read it inside-out: *"for each `x` in `nums`, put `x * 2` in a new list"*. The
square brackets say "I am building a list"; the expression before `for` is
what each item becomes.

It works with anything you can loop over -- including `range`. Reading `n`
numbers (which you have done a dozen times now) collapses to:

```python
nums = [int(input()) for _ in range(n)]
```

## Example

```python
nums = [1, 2, 3]
squares = [x * x for x in nums]
print(squares)    # [1, 4, 9]
```

## Your task

Read a count `n`, then `n` whole numbers. Build a new list where every number
is **doubled**, then print its items one per line.

For input `3`, then `4`, `-1`, `0`:

```
8
-2
0
```

## Done when

- `4, -1, 0` prints `8, -2, 0` -- each doubled, order kept.
- A count of `0` prints nothing.
- You used a list comprehension to build a list.
