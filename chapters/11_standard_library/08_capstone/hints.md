Two imports at the top: `import json` and `import statistics`. First turn the
text into a list with `json.loads(numbers_json)`.

---

Once you have the list `nums`, build the dict: `len(nums)` for count,
`statistics.mean(nums)` for mean, and the built-in `max(nums)` / `min(nums)`.

---

import json
import statistics


def summary(numbers_json):
    nums = json.loads(numbers_json)
    return {
        "count": len(nums),
        "mean": statistics.mean(nums),
        "max": max(nums),
        "min": min(nums),
    }
