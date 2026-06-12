# 3.6 -- Nested conditions

## Concept

An `if` block can contain **another** `if`. This is called **nesting**. The inner
check only happens when the outer condition is already true. Each level is
indented one step further.

```python
if logged_in:
    if is_admin:
        print("admin panel")
    else:
        print("user page")
else:
    print("please log in")
```

Here `is_admin` is only checked when `logged_in` is true.

## Example

```python
n = 250
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
# prints: big
```

## Your task

Read a whole number and classify it:

- if it is **0 or negative**, print `non-positive`;
- otherwise (it is positive), print `small` when it is **less than 100**, or
  `big` when it is **100 or more**.

Use a nested `if` (an outer check for positive, an inner check for the size).

For input `42` the output is:

```
small
```

## Done when

- `-1` and `0` print `non-positive`; `42` prints `small`; `100` and `500` print
  `big`.
