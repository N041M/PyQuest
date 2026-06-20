# 11.8 -- Capstone: a stats summary from JSON

## Concept

This chapter's real lesson is that everyday work is **composing library tools**:
let one module read the data, another crunch it, and return the result. Here you
combine two of the modules you just met.

The input is a **JSON string** holding a list of numbers, e.g. `"[4, 8, 15, 16]"`.
You'll:

1. parse it with **`json.loads`** into a Python list,
2. summarize it with **`statistics`** and the built-ins `max` / `min`,
3. return a plain dict of the results.

```python
import json
import statistics

data = json.loads("[4, 8, 15, 16]")     # [4, 8, 15, 16]
statistics.mean(data)                    # 10.75
```

## Your task

Define `summary(numbers_json)` that takes a JSON string of a list of numbers and
returns a dict with these keys:

- `"count"` -- how many numbers (`len`),
- `"mean"` -- their mean (`statistics.mean`),
- `"max"` -- the largest (`max`),
- `"min"` -- the smallest (`min`).

Parse the input with `json.loads`. Assume at least one number.

## Done when

- `summary("[2, 4, 6]")` equals
  `{"count": 3, "mean": 4, "max": 6, "min": 2}`.
- `summary("[5]")` equals `{"count": 1, "mean": 5, "max": 5, "min": 5}`.
- The input is parsed with `json.loads`, not by hand.
