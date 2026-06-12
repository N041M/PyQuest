# 3.8 -- Looping until a sentinel

## Concept

A loop does not have to count. It can keep going until the user enters a special
**sentinel** value that means "stop". The trick is to read once *before* the
loop, then read again *at the end* of each pass:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

The loop keeps running while the input is not the sentinel (`"quit"` here). As
soon as the sentinel arrives, the condition is false and the loop ends.

## Example

Read numbers and add them up until a `0` is entered:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## Your task

Read whole numbers, one per line, and add them up. Stop when the number `0` is
entered (do not add the `0`). Then print the total.

For the input `4`, `5`, `0` the output is:

```
9
```

## Done when

- `4`, `5`, `0` prints `9`; a lone `0` prints `0`.
- The `0` itself is not added; numbers can be negative.
