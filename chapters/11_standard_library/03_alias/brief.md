# 11.3 -- import as: rename on the way in

## Concept

Sometimes a module's name is long, or clashes with one of yours. **`import ... as
...`** brings the module in under a name **you** choose:

```python
import statistics as stats

stats.mean([1, 2, 3, 4])    # 2.5
```

- `import statistics as stats` binds the module to `stats`; `stats.mean` is
  exactly `statistics.mean`.
- The alias is just a local nickname -- the module is unchanged, and only your
  file sees the new name.
- This is why you'll see conventional aliases everywhere (`import numpy as np`);
  here we shorten `statistics`.

The **`statistics`** module does the common averages for you. `stats.mean(nums)`
is the arithmetic mean -- the sum divided by the count -- without you writing
`sum(nums) / len(nums)`.

## Example

```python
import statistics as stats

def midpoint(nums):
    return stats.median(nums)
```

## Your task

Using **`import statistics as stats`**, define `average(nums)` that returns the
mean of the list `nums`, computed with `stats.mean`.

## Done when

- `average([2, 4, 6])` returns `4`, `average([1, 2])` returns `1.5`.
- `average([5])` returns `5`.
- The mean comes from `statistics.mean`, imported as `stats`.
