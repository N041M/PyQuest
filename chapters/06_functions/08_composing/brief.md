# 6.8 -- Functions calling functions

## Concept

Your functions can call **each other**. That is the real power move: solve a
small problem once, name it, and build the next function on top.

```python
def clean(text):
    return text.strip().lower()

def same_word(a, b):
    return clean(a) == clean(b)
```

`same_word` doesn't repeat the strip-and-lower recipe -- it *delegates* to
`clean`. If you ever improve `clean` (say, also removing punctuation), every
function built on it improves for free. Repeating the recipe in both places
is how bugs are born: fix one copy, forget the other.

Note `same_word` returns the result of a comparison -- a **boolean**
(`True`/`False`), like 3.1. No `if` needed: `clean(a) == clean(b)` already
*is* the answer.

## Example

```python
clean("  Tea ")              # "tea"
same_word("  Tea ", "tea")   # True
same_word("tea", "milk")     # False
```

## Your task

Define **both** functions:

- `clean(text)` -- returns the text with surrounding spaces stripped and
  lowercased (2.7).
- `same_word(a, b)` -- returns `True` exactly when the two texts are the same
  after cleaning. It must **call `clean`** rather than redo the recipe.

## Done when

- `clean("  Tea ")` returns `"tea"`.
- `same_word("  Tea ", "tea")` is `True`; `same_word("tea", "milk")` is `False`.
- `same_word` calls `clean` -- the checker looks for the delegation.
