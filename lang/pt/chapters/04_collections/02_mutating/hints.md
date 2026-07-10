Constrói a lista como antes, e depois altera-a no próprio local.

---

`nums[0] = nums[0] * 2` para duplicar o primeiro item; `nums.pop()` para eliminar o último.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums[0] = nums[0] * 2
nums.pop()
print(nums)
