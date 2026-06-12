int("seven") raises a ValueError -- put the conversion inside a try block.

---

try: convert and print the double. except ValueError: print the message.
The except block only runs when the conversion failed.

---

line = input()
try:
    n = int(line)
    print(n * 2)
except ValueError:
    print("not a number")
