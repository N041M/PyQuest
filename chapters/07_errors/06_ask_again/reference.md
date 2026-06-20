The **retry loop** keeps asking until it gets a valid value. It combines a
`while True` with `try` / `except`: succeed and `break` out; fail and loop round
to ask again.

- The `try` attempts the parse/operation; a successful path ends with `break`,
  leaving the loop.
- The `except` handles the bad input (often just printing a hint and falling
  through), so the `while True` runs another pass.
- `while True` with no other exit relies on that `break` — the valid case is the
  only way out.

```python
while True:
    try:
        n = int(input("number: "))
        break                 # valid -> leave the loop
    except ValueError:
        print("not a number, try again")
```
