DODGES = [
    ("parses with eval instead of json.loads",
     "import statistics\n"
     "def summary(numbers_json):\n"
     "    nums = eval(numbers_json)\n"
     "    return {\"count\": len(nums), \"mean\": statistics.mean(nums),\n"
     "            \"max\": max(nums), \"min\": min(nums)}\n"),
]
