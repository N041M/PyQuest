Depois de construir a lista, imprime len(nums), e depois percorre-a num ciclo.

---

`print(len(nums))`, depois `for x in nums: print(x * 2)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(len(nums))
for x in nums:
    print(x * 2)
