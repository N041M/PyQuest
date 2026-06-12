word = input()
for ch in word:
    if ch == "x":
        break
    if ch == "o":
        continue
    print(ch)
