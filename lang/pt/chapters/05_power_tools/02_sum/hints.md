Constrói primeiro a lista de números (como em 4.13), depois entrega a lista toda a uma só
chamada de função.

---

`sum(nums)` devolve o total -- imprime isso. Não precisas de `total = 0`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(sum(nums))
