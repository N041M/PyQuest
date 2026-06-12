Build the list as before, then change it in place.

---

`nums[0] = nums[0] * 2` to double the first item; `nums.pop()` to drop the last.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
