The three core collections fit different jobs — choosing the right one makes code
simpler and faster:

- **list** — an **ordered** sequence that may repeat. Use it to keep every value,
  in order (a log, a queue of items to process).
- **set** — an unordered group of **distinct** items with fast membership. Use it
  to drop duplicates or ask "have I seen this?".
- **dict** — a mapping from **keys to values**. Use it to look something up by
  name (a count per word, a price per item).

Ask: do I need order and repeats (list), uniqueness and membership (set), or
lookup by key (dict)?

```python
order  = ["a", "b", "a"]    # keep all, in order
unique = {"a", "b"}         # distinct only
price  = {"a": 2, "b": 5}   # look up by key
```
