# 12.4 -- Quantifiers: + means one or more

## Concept

A **quantifier** says how many times the pattern before it may repeat:

- **`+`** -- one or more (`[a-z]+` is a run of one or more lowercase letters)
- **`*`** -- zero or more
- **`?`** -- optional (zero or one)
- **`{n}`** -- exactly `n`; **`{n,m}`** -- between `n` and `m`

```python
import re

re.findall(r"[A-Za-z]+", "Hello, world!")     # ['Hello', 'world']
```

Without the `+`, `[A-Za-z]` would match single letters one at a time. The `+`
makes it grab the **whole word**, stopping at the first character that doesn't
fit (a space, comma, digit). That's how you split text into words while ignoring
punctuation.

## Example

```python
import re

def integers(text):
    return re.findall(r"\d+", text)
```

## Your task

Using **`re.findall`** with a quantifier, define `find_words(text)` that returns
a list of the words in `text` -- each a run of one or more letters
(`[A-Za-z]+`), with punctuation and spaces ignored.

## Done when

- `find_words("Hello, world!")` returns `["Hello", "world"]`.
- `find_words("one-two three")` returns `["one", "two", "three"]`.
- `find_words("")` returns `[]`.
- Words are matched with `[A-Za-z]+`, not split by hand.
