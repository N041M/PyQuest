A `#` begins a **comment**: from the `#` to the end of that line, the text is
ignored by Python. Comments explain *why* code does something; they have no
effect on what runs.

- A comment may sit on its own line or follow code on the same line
  (`x = 1  # set up`).
- A `#` inside a string literal is just a character, not a comment
  (`"#1"` is the text `#1`).
- Python has **no block-comment syntax**: comment each line with `#`, or — for a
  throwaway block — use a string literal, which is evaluated and discarded.

"Commenting out" a line (putting `#` in front) is the quickest way to disable it
without deleting it.

```python
# this whole line is ignored
print("hi")   # and this trailing note is too
```
