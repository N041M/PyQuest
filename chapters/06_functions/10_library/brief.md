# 6.10 -- Capstone: a tiny library

## Concept

Nothing new -- this capstone is the chapter in miniature: several functions,
each with one clear job, the later ones **delegating** to the earlier ones
(6.8). A file of related functions like this is the seed of every real
*library* you will ever import.

The pieces: `for ch in word` (3.10), `in` (5.1), the tally idea (5.9),
f-strings (2.10), and early returns (6.5).

## Example

```python
count_vowels("tea")        # 2   ("e" and "a")
count_vowels("xyz")        # 0
describe("tea")            # "tea has 2 vowels"
describe("xyz")            # "xyz has no vowels"
```

## Your task

Define **both** functions:

- `count_vowels(word)` -- returns how many characters of `word` are vowels
  (`a`, `e`, `i`, `o`, `u`; the words are lowercase).
- `describe(word)` -- returns the string `"<word> has <n> vowels"`, except
  when the count is zero: then it is `"<word> has no vowels"`. It must **call
  `count_vowels`**.

## Done when

- `count_vowels("tea")` is `2`; `count_vowels("xyz")` is `0`.
- `describe("tea")` is `"tea has 2 vowels"`; `describe("xyz")` is
  `"xyz has no vowels"`.
- `describe` delegates to `count_vowels` -- the checker looks for the call.
