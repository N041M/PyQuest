Two statements alter a loop's flow from inside it:

- **`break`** ends the loop **immediately**, skipping any remaining passes and
  jumping to the code after the loop. Use it to stop as soon as you've found
  what you need.
- **`continue`** skips the **rest of the current pass** and jumps straight to the
  loop's next iteration (re-checking the condition / taking the next item).

Both affect only the **innermost** loop that encloses them.

```python
for n in range(10):
    if n == 5:
        break             # stop the whole loop at 5
    if n % 2 == 0:
        continue          # skip evens, go to the next n
    print(n)              # 1, 3
```
