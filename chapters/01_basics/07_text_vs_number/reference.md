Every value has a **type**. Two fundamental ones appear immediately:

- a **string** (`str`) is text, written in quotes: `"42"`, `"hello"`;
- an **integer** (`int`) is a number, written as bare digits: `42`.

The quotes are the whole difference. `type("42")` is `str`; `type(42)` is `int`.

The type decides what an operator means. `+` between two **strings**
*concatenates* (joins) them; `+` between two **numbers** *adds* them:

```python
"2" + "2"   # "22"  -- text joined
 2  +  2    #  4    -- numbers added
```

Mixing the two with `+` is an error (`TypeError`), because Python won't guess
whether you meant to add or join. Convert explicitly first: `int("2") + 2` is
`4`, and `"$" + str(2)` is `"$2"`.
