A `return` can appear **anywhere** in a function, and reaching it ends the call at
once — later lines don't run. An **early return** uses this to handle a case and
leave immediately.

- It flattens code: handle the special or invalid case up front with a guard
  (`if bad: return ...`), then write the main path without nesting it in an
  `else`.
- The first `return` reached wins; nothing after it in that call executes.

```python
def reciprocal(n):
    if n == 0:
        return None     # bail out early on the bad case
    return 1 / n        # main path, not indented under an else
```
