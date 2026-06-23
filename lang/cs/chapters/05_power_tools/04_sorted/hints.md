Sestav seznam, pak procházej `sorted(nums)` místo `nums`.

---

`for x in sorted(nums):` navštíví položky od nejmenší; každou vypiš.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
