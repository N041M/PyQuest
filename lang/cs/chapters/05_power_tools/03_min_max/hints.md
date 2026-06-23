Nejprve sestav seznam; nejmenší a největší jsou pak po jednom volání funkce.

---

`print(min(nums))` pak `print(max(nums))` -- dva řádky, dvě volání.

---

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
print(min(nums))
print(max(nums))
