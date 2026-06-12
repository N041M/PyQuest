Build the list of numbers first (like 4.13), then hand the whole list to one
function call.

---

`sum(nums)` returns the total -- print that. No `total = 0` needed.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
