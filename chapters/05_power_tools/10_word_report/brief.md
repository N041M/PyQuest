# 5.10 -- Capstone: word report

## Concept

Nothing new this time -- this puzzle combines the chapter (and chapter 4) into
one small, real program: a **word frequency report**, the heart of every
"most common words" feature you have ever seen.

The pieces, all of which you have:

- `.split()` -- the line into words (4.4)
- the tally pattern -- count each word (5.9)
- `sorted()` -- order the report (5.4). One new convenience: looping over a
  dict visits its **keys**, so `sorted(counts)` is simply the keys in
  alphabetical order.
- printing a word and its count on one line (1.2)

## Example

For the line `b a b`:

```python
counts = {"b": 2, "a": 1}
for w in sorted(counts):
    print(w, counts[w])
# a 1
# b 2
```

## Your task

Read one line of words. Print one line per **distinct** word -- the word, a
space, and how many times it appeared -- in **alphabetical** order.

For input `tea milk tea`:

```
milk 1
tea 2
```

## Done when

- `tea milk tea` prints `milk 1` then `tea 2` -- distinct words, alphabetical.
- A single repeated word prints one line with its full count.
- An empty line prints nothing.
- You used a dict tally and `sorted()`.
