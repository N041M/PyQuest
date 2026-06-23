Po sestavení seznamu vypiš len(nums), pak ho projdi.

---

`print(len(nums))`, pak `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
