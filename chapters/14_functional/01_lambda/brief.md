# 14.1 -- lambda: a function in an expression

## Concept

A **`lambda`** is a tiny function written inline, with no name and no `def`:

```python
double = lambda x: x * 2
double(5)      # 10
```

- `lambda args: expression` -- the value of the expression is returned
  automatically (no `return`, and only one expression allowed).
- A lambda is a **value**, so you can store it, **return** it from another
  function, or pass it as an argument (which is where it really earns its keep --
  the rest of this chapter).

Because a lambda is defined inside another function, it can **close over** that
function's variables. `lambda x: x * n` remembers the `n` from where it was made.

(For anything longer than one expression, use a normal `def` -- lambdas are for
small inline functions.)

## Example

```python
def adder(n):
    return lambda x: x + n     # remembers n
```

## Your task

Define `multiplier(n)` that **returns a lambda** which multiplies its argument by
`n`. So `multiplier(3)` returns a function, and calling that function with `4`
gives `12`.

## Done when

- `multiplier(3)(4)` is `12`; `multiplier(10)(5)` is `50`.
- `multiplier(0)(7)` is `0`.
- The returned function is a `lambda`, not a nested `def`.
