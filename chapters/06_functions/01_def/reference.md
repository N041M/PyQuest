A **function** packages a piece of work under a name so it can be run on demand,
as many times as needed. **`def`** introduces one: a header `def name():` and an
indented body.

- **Calling** it — `name()` — runs the body. Defining a function does not run it;
  the call does.
- **`return value`** hands a result back to the caller and ends the function
  immediately. The call expression `name()` then *becomes* that value.
- A function with no `return` (or a bare `return`) hands back `None`.

```python
def greet():
    return "hello"

greet()        # 'hello'  -- the call evaluates to the returned value
```
