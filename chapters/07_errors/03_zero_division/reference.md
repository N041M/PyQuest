Dividing by zero raises **`ZeroDivisionError`**. Catching it demonstrates the
**EAFP** style — "easier to ask forgiveness than permission": attempt the
operation and handle the failure, rather than testing for every bad case first.

- `a / 0` and `a // 0` and `a % 0` all raise. Wrapping the division in `try`
  lets you supply a fallback when the divisor turns out to be zero.
- EAFP often reads cleaner than a guarding `if b != 0:` and avoids a race between
  the check and the use.

```python
try:
    rate = hits / total
except ZeroDivisionError:
    rate = 0.0           # no data yet -- sensible fallback
```
