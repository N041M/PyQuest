An `if` block may itself contain another `if` — **nesting**. The inner test runs
**only when** the outer condition was true, so nesting expresses "this, and then
within that, this".

- Each level adds a step of indentation; the inner block is indented under the
  inner `if`.
- Nesting and `and` can express the same thing — `if a: if b:` is like
  `if a and b:` — but nesting is the right tool when the outer case needs its own
  handling (e.g. an `else`) separate from the inner one.
- Keep nesting shallow; deep pyramids are hard to read, and an `elif` chain or
  early `return` often reads better.

```python
if logged_in:
    if is_admin:
        show_admin_panel()   # only when logged_in AND is_admin
    else:
        show_user_panel()    # logged_in but not admin
```
