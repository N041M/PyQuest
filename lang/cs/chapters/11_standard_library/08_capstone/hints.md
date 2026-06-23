Dva importy nahoře: `import json` a `import statistics`. Nejprve proměň text na
seznam pomocí `json.loads(numbers_json)`.

---

Jakmile máš seznam `nums`, sestav slovník: `len(nums)` na count,
`statistics.mean(nums)` na mean a vestavěné `max(nums)` / `min(nums)`.

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
