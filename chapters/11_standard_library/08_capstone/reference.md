The capstone is the chapter's real point: **composing standard-library modules**
into a small pipeline rather than writing each step from scratch.

- **Read** with `json` — `json.loads(text)` turns the JSON input into Python
  values (here, a list of numbers).
- **Summarize** with `statistics` and the built-ins — `statistics.mean(nums)` for
  the average, `max(nums)` / `min(nums)` for the extremes, `len(nums)` for the
  count.
- **Return** a plain `dict`, so the caller gets ordinary Python values to use.

Each stage is a module someone else wrote and tested; your job is to wire them
together. That is what most real programs are — glue between well-made libraries.

```python
import json
import statistics

def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {"count": len(nums), "mean": statistics.mean(nums),
            "max": max(nums), "min": min(nums)}

summary("[2, 4, 6]")   # {'count': 3, 'mean': 4, 'max': 6, 'min': 2}
```
