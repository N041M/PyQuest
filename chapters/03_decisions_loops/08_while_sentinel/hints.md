Read one number before the loop, and read the next at the end of each pass.

---

`total = 0`, read n, then `while n != 0:` add to total and read the next n.
After the loop, print total.

---

total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
