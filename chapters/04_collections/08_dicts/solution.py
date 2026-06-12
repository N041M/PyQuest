n = int(input())
d = {}
for _ in range(n):
    word = input()
    d[word] = int(input())
query = input()
print(d[query])
