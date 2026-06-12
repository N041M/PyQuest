# 1.5 -- Storing a value

## Concept

A **variable** is a name that holds a value so you can use it later. You create
one with `=`, the **assignment** sign:

```python
score = 100
```

Read this as "let `score` be `100`." The name goes on the left, the value on the
right. After that line, writing `score` anywhere means `100`.

This is different from `==` (which you will meet later for comparing). A single
`=` *stores*.

Once stored, you can use the name as many times as you like:

```python
score = 100
print(score)
print(score)
```

shows:

```
100
100
```

Notice `print(score)` has **no quotes** around `score`. Quotes would make it the
literal text "score"; without quotes it means the variable's value, `100`.

## Naming rules (quick version)

A variable name can use letters, digits, and underscores, but cannot start with a
digit and cannot contain spaces. Use clear names: `total`, `user_name`, `count`.

## Your task

Store the number `42` in a variable, then print that variable **twice** so the
output is:

```
42
42
```

Use the variable both times -- do not type `42` inside the prints.

## Done when

- The output is `42` on two separate lines.
- Both lines come from printing your variable (no quotes around its name).
