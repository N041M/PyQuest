The capstone chains the chapter's higher-order functions into a **data
pipeline** — the shape of much real processing:

1. **`filter(lambda r: r[1] >= threshold, records)`** narrows to the records that
   qualify;
2. **`sorted(..., key=lambda r: r[1], reverse=True)`** ranks them by score, high
   to low (stable, so equal scores keep their order);
3. **`map(lambda r: r[0], ...)`** projects out just the field you want — the name.

Each stage takes a function and an iterable and yields another iterable, so they
compose directly: the filter feeds the sort, the sort feeds the map. The same
pipeline could be written with comprehensions; expressing it as
`filter`/`sorted`/`map` is the functional style, and seeing a task *as* a pipeline
of transformations is the skill the chapter builds toward.

```python
def passing(records, threshold):
    qualified = filter(lambda r: r[1] >= threshold, records)
    ranked = sorted(qualified, key=lambda r: r[1], reverse=True)
    return list(map(lambda r: r[0], ranked))
```
