Sestav seznam jako dřív, pak ho změň na místě.

---

`nums[0] = nums[0] * 2` pro zdvojnásobení první položky; `nums.pop()` pro odebrání
poslední.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
