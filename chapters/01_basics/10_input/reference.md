`input` reads **one line** from standard input — everything the user types until
they press Enter — strips the trailing newline, and returns it as a **string**.

- The return value is *always* a `str`, even if the user typed digits:
  `input()` on `42` returns `"42"`, not `42`. To do arithmetic, convert it
  (see `int()`).
- The optional `prompt` argument is written to the screen first, without a
  trailing newline, so the user types on the same line.
- If the input stream ends with no line to read (end-of-file), `input` raises
  `EOFError`.

```python
name = input("Your name? ")   # prompts, then reads a line
print("Hi, " + name)
```
