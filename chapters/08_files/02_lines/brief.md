# 8.2 -- A file, line by line

## Concept

`f.read()` gives you everything at once. More often you want the file **one
line at a time** -- and a file object is *iterable*, so a `for` loop walks its
lines for you:

```python
with open("tasks.txt") as f:
    for line in f:
        ...
```

One catch: each `line` still carries the newline that ended it -- `"wash\n"`,
not `"wash"`. Strip it with `line.strip()` (3.7) before you use the text, or
your output grows blank lines.

## Example

For a `tasks.txt` of:

```
wash
cook
sleep
```

numbering each line gives:

```
1. wash
2. cook
3. sleep
```

`enumerate` (5.5) is the natural fit -- start it at `1`:

```python
for i, line in enumerate(f, start=1):
    print(f"{i}. {line.strip()}")
```

## Your task

Read `tasks.txt` and print every line **numbered from 1**, in the form
`1. wash`. Drop the trailing newline so there are no stray blank lines.

## Done when

- Each line is printed as `<number>. <text>`, counting from 1.
- It works for a file of any length.
- You opened the file with `with` and looped over it with `for`.
