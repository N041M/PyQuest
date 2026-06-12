# 1.7 -- Text vs number

## Concept

Python tells two kinds of values apart, and it matters a lot:

- A **number** like `5` -- written with no quotes. Python calls whole numbers
  `int` (integer).
- A **string** like `"5"` -- written with quotes. It is *text* that happens to
  look like a number. Python calls it `str`.

They behave differently with the `+` sign:

- With numbers, `+` **adds**: `5 + 5` is `10`.
- With strings, `+` **joins** (this is called **concatenation**):
  `"5" + "5"` is `"55"` -- the two pieces of text stuck together.

```python
print(5 + 5)        # 10   (numbers add)
print("5" + "5")    # 55   (text joins)
print("ab" + "cd")  # abcd
```

So `"5"` and `5` look the same on screen but are different types, and `+` treats
them in completely different ways.

## Common misconception

`"5"` is not the number five. The quotes make it text. You cannot do arithmetic
with it and expect addition -- `"5" + "5"` gives `"55"`, not `10`.

## Your task

Print these two lines, in this order:

```
55
10
```

- The first line must come from **joining two strings** `"5"` and `"5"` with `+`.
- The second line must come from **adding two numbers** `5` and `5` with `+`.

## Done when

- Output is `55` then `10`.
- Line one uses string concatenation; line two uses number addition.
