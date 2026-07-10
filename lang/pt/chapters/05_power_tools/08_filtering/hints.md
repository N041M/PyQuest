"Par" significa que o resto da divisão por 2 é zero: `x % 2 == 0`.

---

Coloca esse teste no final da compreensão:
`evens = [x for x in nums if x % 2 == 0]` -- depois imprime cada item.

---

n = int(input())
nums = [int(input()) for _ in range(n)]
evens = [x for x in nums if x % 2 == 0]
for e in evens:
    print(e)
