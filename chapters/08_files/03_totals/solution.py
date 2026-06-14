total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
