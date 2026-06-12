n = int(input())
words = []
for _ in range(n):
    words.append(input())
print(len(set(words)))
