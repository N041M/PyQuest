# 2.7 -- Cleaning up text

## Concept

Strings come with **methods** -- actions you call with a dot after the string:
`s.method()`. Three common ones:

- `s.upper()` -> an UPPERCASE copy
- `s.lower()` -> a lowercase copy
- `s.strip()` -> a copy with spaces removed from **both ends** (not the middle)

```python
"Hello".upper()     # "HELLO"
"Hello".lower()     # "hello"
"  hi  ".strip()    # "hi"
```

Methods return a **new** string; they do not change the original. You can chain
them -- each one works on the result of the one before:

```python
"  Hi  ".strip().upper()   # "HI"
```

## Example

```python
s = "  python  "
print(s.strip().upper())   # PYTHON
```

## Your task

Read a line, remove any spaces around it, and print it in **uppercase**.

For input `  hello  ` the output is:

```
HELLO
```

## Done when

- For `  hello  ` it prints `HELLO`.
- Spaces in the middle stay; only the ends are trimmed. The checker also tries a
  line that is only spaces (the result is an empty line).
