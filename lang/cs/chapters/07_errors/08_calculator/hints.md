split() řádek na tři části; převeď parts[0] a parts[2] uvnitř try.

---

Naskládej dva excepty za jeden try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". Řetěz operací je if/elif/else, s else
vypisujícím "unknown op".

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
