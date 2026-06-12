Make an empty dict, then store each pair as d[word] = number.

---

`d = {}`, loop reading word + number with `d[word] = int(input())`, then read
the query and `print(d[query])`.

---

n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
