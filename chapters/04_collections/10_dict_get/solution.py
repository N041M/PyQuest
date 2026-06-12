n = int(input())
d = {}
for _ in range(n):
    key = input()
    d[key] = int(input())
query = input()
print(d.get(query, 0))
