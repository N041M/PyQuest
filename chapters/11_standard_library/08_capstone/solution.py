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
