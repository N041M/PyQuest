split() a linha em três partes; converte parts[0] e parts[2] dentro do try.

---

Empilha os dois excepts depois de um try: ValueError -> "bad number",
ZeroDivisionError -> "cannot divide". A cadeia da operação é if/elif/else,
com o else a imprimir "unknown op".

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
