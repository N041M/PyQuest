Constrói a lista. A contagem é len(nums); a contagem de distintos usa um conjunto.

---

`print(len(nums))`, `print(len(set(nums)))`, depois o total (um ciclo, ou sum).

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
