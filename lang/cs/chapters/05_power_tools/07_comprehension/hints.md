Vzor je  new_list = [<čím se každá položka stane> for x in old_list].

---

`doubled = [x * 2 for x in nums]` -- pak prostý cyklus for vypíše každou položku.
(Čtení čísel může být také komprehenze: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
