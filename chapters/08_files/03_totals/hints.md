Start a running total at 0, open the file, and loop over its lines.

---

Each line is a string like `"25\n"`. `int(line)` turns it into a number you can
add. Print the total after the loop.

---

total = 0
with open("prices.txt") as f:
    for line in f:
        total += int(line)
print(total)
