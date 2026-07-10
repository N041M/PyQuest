Constrói primeiro a lista; depois o mais pequeno e o maior são cada um uma só chamada de função.

---

`print(min(nums))` depois `print(max(nums))` -- duas linhas, duas chamadas.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
