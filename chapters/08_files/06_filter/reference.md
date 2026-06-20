A **filtering** pass reads one file, keeps only the lines an `if` accepts, and
writes them to another — the file form of the comprehension-with-`if` pattern.

- Open the source for reading and the destination for writing, loop the source,
  and `f_out.write(line)` only when the line passes your test.
- Lines from the input keep their newline, so writing them back reproduces line
  breaks without adding any.
- Reading and writing the **same** path at once is unsafe; write to a new file
  (or collect results, then write).

```python
with open("all.txt") as src, open("kept.txt", "w") as out:
    for line in src:
        if "ERROR" in line:
            out.write(line)       # keep only matching lines
```
