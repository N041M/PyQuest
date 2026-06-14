# 8.4 -- Writing a file

## Concept

Reading is half the story; programs also **create** files. Open with the mode
`"w"` (for *write*) and call `.write()`:

```python
with open("out.txt", "w") as f:
    f.write("hello\n")
```

Two things to know:

- `"w"` makes a brand-new file (or **empties** an existing one), then writes.
- `.write()` puts down **exactly** the text you give it -- no automatic
  newline like `print()` adds. If you want line breaks, include `"\n"`
  yourself.

A common shape is **read one file, write another**:

```python
with open("in.txt") as f:
    text = f.read()
with open("out.txt", "w") as f:
    f.write(text.upper())
```

## Example

If `in.txt` contains `quiet please`, then `out.txt` should end up holding
`QUIET PLEASE`.

## Your task

Read `in.txt`, and write its contents **in upper case** (7.x `.upper()` from
2.7) into a new file called `out.txt`.

## Done when

- `out.txt` contains exactly the text of `in.txt`, uppercased.
- An empty `in.txt` produces an empty `out.txt` -- no crash.
- You used `with` and opened `out.txt` in `"w"` mode.
