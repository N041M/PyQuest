First decide positive vs not. Only if positive do you ask small vs big.

---

Outer: `if n > 0:` ... `else: print("non-positive")`. Inside the if, another
if/else comparing n to 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
