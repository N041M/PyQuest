# 5.1 -- in: membership testing

## Concept

You met `in` with sets (4.11). It actually works on almost everything:

```python
"e" in "hello"        # True   (substring of a string)
3 in [1, 2, 3]        # True   (item of a list)
"sam" in {"sam": 20}  # True   (KEY of a dict)
```

`x in s` is an expression that gives a **boolean** (`True`/`False`), so it
slots straight into an `if`:

```python
if "@" in address:
    print("looks like an email")
```

There is also the opposite, `not in`:

```python
if "x" not in word:
    print("no x here")
```

Compare that with chapter 2, where you used `s.find()` and checked for `-1`.
`in` says the same thing in plain English -- prefer it whenever you only need
*whether* something is there, not *where*.

## Example

```python
word = "banana"
print("n" in word)     # True
print("z" in word)     # False
```

## Your task

Read a word, then a single letter. Print `yes` if the letter appears in the
word, and `no` if it doesn't.

For input `banana`, then `n`:

```
yes
```

## Done when

- A letter that appears prints `yes`; one that doesn't prints `no`.
- It works for a one-letter word too.
- You used the `in` operator (not `.find()` or `.count()`).
