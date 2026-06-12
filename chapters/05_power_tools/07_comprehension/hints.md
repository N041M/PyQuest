The pattern is  new_list = [<what each item becomes> for x in old_list].

---

`doubled = [x * 2 for x in nums]` -- then a plain for loop prints each item.
(Reading the numbers can be a comprehension too: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
