A **`lambda`** is an anonymous function written as a single expression:
`lambda args: expression`. The expression's value is returned automatically —
there is no `return`, and the body must be **one** expression.

- A lambda is a first-class **value**: assign it, return it, or pass it as an
  argument. `f = lambda x: x * 2` is much like `def f(x): return x * 2`, just
  inline and nameless.
- Defined inside another function, a lambda **closes over** that scope's
  variables — `lambda x: x * n` captures `n` from where it was created, so each
  `multiplier(n)` yields a function bound to its own `n`.
- Lambdas are for *small* inline functions, especially as the `key=` to `sorted`
  or the function for `map`/`filter` (the rest of this chapter). For anything
  multi-statement, use a named `def`.

```python
double = lambda x: x * 2
double(5)                  # 10

def multiplier(n):
    return lambda x: x * n
multiplier(3)(4)           # 12
```
