# 2.10 -- f-strings

## Concept

An **f-string** lets you drop values straight into text. Put an `f` before the
opening quote, then write `{...}` wherever a value should go:

```python
name = "Sam"
print(f"Hello, {name}!")     # Hello, Sam!
```

Inside the `{}` you can put any expression, not just a plain variable -- it is
worked out and its result is placed in the text:

```python
word = "cat"
print(f"{word} has {len(word)} letters")    # cat has 3 letters
print(f"{word} reversed is {word[::-1]}")   # cat reversed is tac
```

f-strings are the clearest way to build text out of values -- much tidier than
joining pieces with `+`.

## Example

```python
s = "python"
print(f"{s} reversed is {s[::-1]}")   # python reversed is nohtyp
```

## Your task

Read a word, then print this exact sentence using an f-string:

```
WORD reversed is REVERSED
```

where `WORD` is the input and `REVERSED` is it backwards. For input `hello`:

```
hello reversed is olleh
```

## Done when

- For `hello` it prints `hello reversed is olleh`.
- It works for any word, including a single letter. The checker tries a few.
