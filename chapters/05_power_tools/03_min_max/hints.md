Build the list first; then the smallest and largest are each one function call.

---

`print(min(nums))` then `print(max(nums))` -- two lines, two calls.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
