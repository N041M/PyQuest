# 2.6 -- Length, joining, repeating

## Concept

Three everyday string tools:

- `len(s)` gives the **number of characters** in `s` (a number):
  ```python
  len("cat")    # 3
  ```
- `+` joins two strings (you met this in chapter 1):
  ```python
  "cat" + "!"   # "cat!"
  ```
- `*` with a number **repeats** a string:
  ```python
  "ab" * 3      # "ababab"
  "-" * 5       # "-----"
  ```

`len` returns a number, so you can do maths with it. `+` and `*` build new
strings.

## Example

```python
s = "hi"
print(len(s))    # 2
print(s + "!")   # hi!
print(s * 3)     # hihihi
```

## Your task

Read a word and print three lines:

1. the number of characters in the word
2. the word with an exclamation mark added on the end
3. the word repeated three times

For input `hi` the output is:

```
2
hi!
hihihi
```

## Done when

- For `hi` the three lines are `2`, `hi!`, `hihihi`.
- It also works for an empty input: `0`, `!`, and an empty line. The checker
  tries it.
