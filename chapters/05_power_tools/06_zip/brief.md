# 5.6 -- zip(): pairing lists

## Concept

Two lists often belong together item-by-item: names and scores, questions and
answers. `zip()` walks them **in step**, handing you one pair per pass:

```python
names = ["amy", "ben"]
scores = [90, 85]
for name, score in zip(names, scores):
    print(name, score)
# amy 90
# ben 85
```

Like `enumerate`, each pass gives a pair that you unpack into two variables.
The name is the image of a zipper: two rows of teeth joined one-to-one.

If the lists have different lengths, `zip` stops at the **shorter** one --
extra items on the longer list are simply never visited.

## Example

```python
for a, b in zip("ab", [1, 2]):
    print(a, b)
# a 1
# b 2
```

## Your task

Read a count `n`, then `n` names, then `n` scores (whole numbers). Print one
line per pair: the name, a space, the score.

For input `2`, then `amy`, `ben`, then `90`, `85`:

```
amy 90
ben 85
```

## Done when

- Two names and two scores print as two `name score` lines, in order.
- A count of `0` prints nothing.
- You used `zip()` to pair the two lists.
