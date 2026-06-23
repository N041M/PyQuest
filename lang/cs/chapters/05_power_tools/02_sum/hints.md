Nejprve sestav seznam čísel (jako v 4.13), pak celý seznam předej jedinému volání
funkce.

---

`sum(nums)` vrátí součet -- ten vypiš. Žádné `total = 0` není potřeba.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
