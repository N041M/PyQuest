d[key] crashes if the key is missing. d.get(key, 0) returns 0 instead.

---

After building the dict and reading the query, `print(d.get(query, 0))`.

---

n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
