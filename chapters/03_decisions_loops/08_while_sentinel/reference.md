A **sentinel** loop reads values repeatedly and stops when it sees a special
"stop" value rather than after a fixed count. The pattern is a `while` whose
condition tests the most recent input against the sentinel.

- Read once before the loop (or read at the top of each pass), then compare to
  the sentinel to decide whether to continue.
- The sentinel itself is **not** processed — the check happens before the work,
  so the stop value ends the loop instead of being counted.

```python
line = input()
while line != "quit":     # "quit" is the sentinel
    print("you said:", line)
    line = input()        # read the next, then re-check
```
