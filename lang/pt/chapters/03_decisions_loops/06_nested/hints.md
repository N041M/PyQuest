Primeiro decide positivo ou não. Só se for positivo é que perguntas small ou big.

---

Exterior: `if n > 0:` ... `else: print("non-positive")`. Dentro do if, outro
if/else a comparar n com 100.

---

n = int(input())
if n > 0:
    if n < 100:
        print("small")
    else:
        print("big")
else:
    print("non-positive")
