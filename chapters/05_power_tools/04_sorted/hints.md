Build the list, then loop over `sorted(nums)` instead of `nums`.

---

`for x in sorted(nums):` visits the items smallest-first; print each one.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
