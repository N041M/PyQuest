n = int(input())
words = []
for _ in range(n):
    words.append(input())
for i, w in enumerate(words, 1):
    print(f"{i}. {w}")
