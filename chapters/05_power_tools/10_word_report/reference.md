A **word-frequency report** composes the chapter's tools into a small pipeline:

1. **`split()`** the text into a list of words;
2. **tally** them into a dict of `word -> count` with `counts.get(w, 0) + 1`;
3. **`sorted`** the `dict.items()` to order the report — by word, or by count
   with `key=lambda kv: kv[1]` (and `reverse=True` for most-frequent first).

Each step is a tool you've met; the skill is seeing that a real task is their
composition.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
