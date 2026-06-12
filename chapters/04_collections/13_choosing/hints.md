Build the list. The count is len(nums); the distinct count uses a set.

---

`print(len(nums))`, `print(len(set(nums)))`, then the total (a loop, or sum).

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
print(len(set(nums)))
total = 0
for x in nums:
    total = total + x
print(total)
