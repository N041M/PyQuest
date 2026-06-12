split() the line into three parts; convert parts[0] and parts[2] inside the
try.

---

Stack the two excepts after one try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". The op chain is if/elif/else, with else
printing "unknown op".

---

parts = input().split()
try:
    a = int(parts[0])
    op = parts[1]
    b = int(parts[2])
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b)
    else:
        print("unknown op")
except ValueError:
    print("bad number")
except ZeroDivisionError:
    print("cannot divide")
