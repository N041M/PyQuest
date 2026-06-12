"Even" means the remainder after dividing by 2 is zero: `x % 2 == 0`.

---

Put that test at the end of the comprehension:
`evens = [x for x in nums if x % 2 == 0]` -- then print each item.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
