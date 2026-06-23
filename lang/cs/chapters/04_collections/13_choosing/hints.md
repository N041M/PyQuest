Sestav seznam. Počet je len(nums); počet odlišných používá množinu.

---

`print(len(nums))`, `print(len(set(nums)))`, pak součet (cyklus, nebo sum).

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
