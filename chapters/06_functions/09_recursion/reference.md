A **recursive** function calls **itself** to solve a smaller version of the same
problem. Two parts are essential:

- a **base case** that returns directly **without** recursing — this stops the
  recursion;
- a **recursive case** that calls the function on a smaller input and builds on
  the result, moving toward the base case each time.

Miss or never reach the base case and the calls nest until Python raises
`RecursionError`. Many recursions have a simpler loop form; recursion shines when
the problem is itself self-similar.

```python
def factorial(n):
    if n <= 1:          # base case
        return 1
    return n * factorial(n - 1)   # smaller subproblem

factorial(4)   # 24
```
