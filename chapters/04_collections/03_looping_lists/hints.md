After building the list, print len(nums), then loop over it.

---

`print(len(nums))`, then `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
