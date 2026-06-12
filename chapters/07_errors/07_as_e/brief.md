# 7.7 -- Reading the error: except ... as e

## Concept

An exception is not just a signal -- it is an **object carrying a message**.
Catch it *into a variable* with `as`, and you can use that message:

```python
try:
    n = int(text)
except ValueError as e:
    print(e)
```

For `text = "5x"`, that prints Python's own diagnosis:

```
invalid literal for int() with base 10: '5x'
```

`e` is the error object; printing it shows its message. This is how real
programs log what actually went wrong instead of a vague "something failed" --
the difference between a bug report you can act on and one you can't.

(You don't write the message yourself here -- you *relay* the one Python
attached when it raised.)

## Example

Input `7` prints `7`. Input `5x` prints
`invalid literal for int() with base 10: '5x'`.

## Your task

Read one line. If it converts to a whole number, print the number. If it
doesn't, catch the `ValueError` **as `e`** and print `e` itself -- Python's
message, not your own.

## Done when

- `7` prints `7`.
- `5x` prints the exact `invalid literal ...: '5x'` message -- with the
  offending text quoted inside it.
- You did not type the message by hand (it must match for *any* input, which
  only printing `e` gets right).
