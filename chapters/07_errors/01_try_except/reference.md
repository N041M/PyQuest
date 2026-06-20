A **`try` / `except`** statement runs risky code and catches the error if it
fails, instead of letting the program crash. The `try` block holds the code that
might **raise**; the `except` block runs only if it does.

- If the `try` block succeeds, the `except` is skipped entirely.
- If a statement in `try` raises, the **rest of the `try` is abandoned** and
  control jumps to the matching `except`; the program then continues below.
- An uncaught error unwinds the whole program with a traceback — `except` is how
  you intervene.

```python
try:
    n = int(text)        # may raise ValueError
except ValueError:
    n = 0                # recover instead of crashing
```
