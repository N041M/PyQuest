A program runs top to bottom, so successive `print` statements produce successive
lines — each call emits its arguments and then a newline.

Passing **several values to one `print`**, separated by commas, is different from
several `print` calls: the values appear on a *single* line, joined by `sep` (a
space by default). This is comma-separation in the call, not string concatenation
— the values keep their own types and are converted independently.

```python
print("one")
print("two")          # two lines

print("x", "y", 3)    # one line:  x y 3
```
