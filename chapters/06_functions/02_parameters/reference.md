A **parameter** is a name in the function header that stands for a value the
caller supplies. The values passed in a call are the **arguments**, matched to
parameters left to right.

- `def f(a, b):` declares two parameters; `f(3, 4)` calls with `a = 3`, `b = 4`.
- Parameters are **local**: they exist only during the call and don't clash with
  names outside. The function works on whatever it's given, making it reusable.
- Passing the wrong number of arguments raises `TypeError`.

```python
def add(a, b):
    return a + b

add(3, 4)      # 7
```
