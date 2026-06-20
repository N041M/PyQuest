A **boolean** is one of two values, `True` or `False` (type `bool`). The
**comparison operators** produce one by comparing two values:

- `==` equal, `!=` not equal,
- `<` less than, `>` greater than, `<=` at most, `>=` at least.

`==` (a question, "are these equal?") is not `=` (a command, "assign"). Numbers
compare by value; strings compare **lexicographically** (dictionary order, by
character code, so uppercase sorts before lowercase). Comparisons can be
**chained**: `0 <= x < 10` means `0 <= x and x < 10`.

```python
3 < 5        # True
3 == 3.0     # True   -- equal values, different types
"a" < "b"    # True
```
