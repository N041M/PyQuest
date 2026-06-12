# 1.6 -- Reassigning a variable

## Concept

A variable can be **changed** after it is created. Assigning to the same name
again replaces the old value with a new one. The name always refers to whatever
was stored **most recently**.

```python
x = 10
print(x)   # 10
x = 20
print(x)   # 20
```

The order matters: the program runs top to bottom, so the first `print(x)` sees
`10`, and only after the second assignment does `x` become `20`.

A common and useful pattern is updating a variable using its own current value:

```python
x = 10
x = x + 5   # take the current x (10), add 5, store 15 back in x
print(x)    # 15
```

The right side is worked out first (`10 + 5`), then the result is stored back
into `x`.

## Common misconception

Reassigning does not create a second variable. There is still just one `x`; its
stored value was swapped. The old value is simply gone.

## Your task

Create a variable holding `10` and print it. Then reassign that same variable to
`20` and print it again. The output must be:

```
10
20
```

## Done when

- The output is `10` then `20` on two lines.
- Both lines print the **same** variable, before and after you change it.
