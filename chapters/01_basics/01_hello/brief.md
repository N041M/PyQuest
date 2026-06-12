# 1.1 -- Hello, output

## Concept

A **program** is a list of instructions the computer runs from top to bottom.
The most basic instruction is to **print** -- to put a line of text on the
screen. In Python you do that with `print(...)`. Whatever you put inside the
parentheses, in quotes, is shown.

`print` is a **function**: a built-in action you trigger by writing its name
followed by parentheses. The thing in quotes is **text** (Python calls text a
*string* -- a string of characters).

## Example

```python
print("Good morning")
```

When this runs, the screen shows:

```
Good morning
```

The quotes mark where the text starts and ends; they are not printed. Python
also adds a line break at the end automatically, so the next print starts on a
new line.

## Your task

Make the program print exactly this line:

```
Hello, output
```

Open the chapter workspace `work.py`, write one `print(...)` that produces that
line, **save the file**, then run `check`.

## Done when

- Running `check` shows CHECK PASSED.
- The output reads `Hello, output` -- same words, same comma. (The checker
  ignores capitalisation, but matching the brief exactly is good practice.)
