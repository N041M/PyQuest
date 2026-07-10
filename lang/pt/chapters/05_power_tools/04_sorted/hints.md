Constrói a lista, depois percorre `sorted(nums)` em vez de `nums`.

---

`for x in sorted(nums):` visita os itens do mais pequeno para o maior; imprime cada um.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
for x in sorted(nums):
    print(x)
