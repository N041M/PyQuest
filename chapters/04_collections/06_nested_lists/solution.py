n = int(input())
pairs = []
for _ in range(n):
    a = int(input())
    b = int(input())
    pairs.append([a, b])
print(pairs)
for p in pairs:
    print(p[0] + p[1])
