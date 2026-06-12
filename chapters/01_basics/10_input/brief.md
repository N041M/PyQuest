# 1.10 -- Asking the user

## Concept

`input()` pauses the program, lets the person type a line, and **gives back what
they typed as text** (a string). You usually store that in a variable:

```python
name = input()
print("Hi, " + name)
```

If the person types `Sam`, the program prints `Hi, Sam`.

`input()` always returns a **string**, even if the person types digits. (You will
deal with that in the next puzzle.)

You can join the typed text with other text using `+`, exactly like in puzzle 1.7:

```python
city = input()
print("You live in " + city)
```

> Note: when you run `check`, the checker feeds the input for you automatically
> -- you do not type anything by hand.

## Example

Input typed: `Berlin`

```python
city = input()
print("Welcome to " + city)
```

Output:

```
Welcome to Berlin
```

## Your task

Read one line of input (a name) and greet it. If the input is `World`, the output
must be exactly:

```
Hello, World
```

So: read the name with `input()`, then print `Hello, ` joined with the name. Mind
the comma and the single space after it.

## Done when

- Given input `World`, output is `Hello, World`.
- Given any other name, it greets that name the same way (the checker tries
  more than one).
