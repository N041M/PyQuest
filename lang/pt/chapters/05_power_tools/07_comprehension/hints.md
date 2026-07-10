O padrão é  nova_lista = [<o que cada item se torna> for x in lista_antiga].

---

`doubled = [x * 2 for x in nums]` -- depois um `for` simples imprime cada item.
(Ler os números também pode ser uma compreensão: `[int(input()) for _ in range(n)]`.)

---

n = int(input())
nums = [int(input()) for _ in range(n)]
doubled = [x * 2 for x in nums]
for d in doubled:
    print(d)
