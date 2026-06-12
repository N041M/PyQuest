Start with an empty list [], then append each number inside a loop.

---

`nums = []`, read n, then `for _ in range(n): nums.append(int(input()))`.
Finally `print(nums)`.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(nums)
