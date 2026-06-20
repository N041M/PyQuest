**`s.find(sub)`** returns the index of the **first** occurrence of `sub` in `s`,
or **`-1`** if it isn't found (it never raises). Pairing it with slicing extracts
the text around a marker.

- The returned index is where `sub` starts, so `s[:i]` is the part before it and
  `s[i + len(sub):]` the part after.
- Check for `-1` before using the result — `s.find` returning `-1` would
  otherwise slice from the end.
- `.index(sub)` is the same but **raises** `ValueError` when absent; use `.find`
  when "not present" is a normal case.

```python
s = "key=value"
i = s.find("=")     # 3
s[:i]               # 'key'
s[i + 1:]           # 'value'
```
