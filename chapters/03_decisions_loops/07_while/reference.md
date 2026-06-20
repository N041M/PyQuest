A **`while`** loop repeats its block **as long as** its condition stays true. The
condition is checked **before** each pass; when it becomes false, the loop ends
and the program continues below.

- Something inside the loop must eventually make the condition false (e.g.
  advancing a counter), or it loops forever — an infinite loop.
- If the condition is false at the very first check, the body runs zero times.
- Use `while` when you don't know the number of passes up front (you loop until
  something happens); use `for` when you're counting a known range.

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # moves toward ending the loop -> 3, 2, 1
```
