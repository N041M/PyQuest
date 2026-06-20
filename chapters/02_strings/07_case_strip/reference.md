Strings carry **methods** — functions called with the `s.method()` syntax that
compute from the string.

- **`.strip()`** returns the string with leading and trailing **whitespace**
  removed (spaces, tabs, newlines). `.lstrip()` / `.rstrip()` trim one side.
- **`.upper()`** / **`.lower()`** return the string with every letter in upper
  or lower case.

Because every method returns a **new** string (the original is never modified),
calls **chain**: each acts on the result of the previous.

```python
"  Hi  ".strip()            # 'Hi'
"Hi".upper()                # 'HI'
"  Hello  ".strip().lower() # 'hello'  -- trimmed, then lowered
```
