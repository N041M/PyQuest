# 8.6 -- Filtering lines into a new file

## Concept

Put reading and writing together and you get the everyday data chore: walk an
input file line by line, **decide** which lines to keep (3.2 `if`), and write
just those to an output file.

```python
with open("lines.txt") as f:
    lines = f.readlines()
with open("kept.txt", "w") as f:
    for line in lines:
        if keep(line):
            f.write(line)
```

`f.readlines()` reads the whole file into a list of lines up front -- handy
when you want to finish reading before you start writing.

A line that is empty or only spaces is "blank": `line.strip()` returns `""` for
it, and an empty string is falsey (3.1), so `if line.strip():` is a tidy test
for "this line has real content".

## Example

From a `lines.txt` of:

```
keep me

and me
```

the blank middle line is dropped, leaving `keep me` and `and me`.

## Your task

Read `lines.txt` and write only its **non-blank** lines to `kept.txt`, in the
same order. Drop any line that is empty or just whitespace.

## Done when

- `kept.txt` holds exactly the non-blank lines of `lines.txt`, in order.
- A file with no blank lines is copied unchanged; an all-blank file yields an
  empty `kept.txt`.
- You used `with`, a loop, and an `if` to decide what to keep.
