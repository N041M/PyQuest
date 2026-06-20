# 12.3 -- Character classes: [aeiou]

## Concept

A **character class** `[...]` matches **any one** of the characters listed inside
it:

```python
import re

re.findall(r"[aeiou]", "education")     # ['e', 'u', 'a', 'i', 'o']
```

- `[aeiou]` matches a single vowel; `[abc]` matches `a`, `b`, or `c`.
- A **range** uses a hyphen: `[a-z]` is any lowercase letter, `[0-9]` any digit
  (the same as `\d`), `[A-Za-z0-9]` any letter or digit.
- A leading `^` **negates** the class: `[^aeiou]` is any character that is *not*
  a vowel.

A class is one character; add a quantifier (`[a-z]+`) to match a run of them.

## Example

```python
import re

def count_letters(text):
    return len(re.findall(r"[a-z]", text))
```

## Your task

Using a character class with **`re.findall`**, define `count_vowels(text)` that
returns how many vowels (`a e i o u`) are in `text`.

## Done when

- `count_vowels("education")` returns `5`, `count_vowels("xyz")` returns `0`.
- `count_vowels("")` returns `0`.
- Counting uses `re.findall` with a `[aeiou]` class, not a manual `in` check.
