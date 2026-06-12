Read the count first. Start a total at 0, then loop that many times adding each
number.

---

`n = int(input())`, `total = 0`, then `for _ in range(n):` add `int(input())`
to total. Print total after the loop.

---

n = int(input())
total = 0
for _ in range(n):
    total = total + int(input())
print(total)
