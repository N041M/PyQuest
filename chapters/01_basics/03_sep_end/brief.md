# 1.3 -- Choosing the separator

## Concept

When you give `print` several values, it joins them with a space by default. You
can change that join string with a special setting called **`sep`** (short for
*separator*).

A setting like this is written `name=value` inside the parentheses, after your
values:

```python
print("a", "b", "c", sep="-")
```

shows:

```
a-b-c
```

`sep="-"` tells `print` to put a dash between values instead of a space. The
separator goes *between* values only -- not before the first or after the last.
You can use any text as the separator: `sep=", "`, `sep=""` (nothing), `sep="/"`,
and so on.

`sep` must be written exactly, with no space before the `=`, and the value in
quotes because it is text.

## Example

```python
print("home", "user", "docs", sep="/")
```

shows:

```
home/user/docs
```

## Your task

Print this exact date, using three **numbers** joined by dashes:

```
2024-12-25
```

Pass `2024`, `12`, `25` to a single `print` and set `sep` so they are joined with
`-`. Do not type the dashes as part of the text yourself.

## Done when

- The output is exactly `2024-12-25`.
- It comes from three numbers plus a `sep` setting, not from one typed string.
