Uma lista é iterável, por isso **`for x in lst`** visita cada item por ordem,
associando a variável do ciclo ao próprio item (não ao seu índice).

- Esta é a forma habitual de percorrer uma lista. Quando também precisas da
  posição, combina-a com `range(len(lst))` ou `enumerate` (capítulo 5).
- **`len(lst)`** dá a contagem de itens; o **slicing** (`lst[1:3]`, `lst[::-1]`)
  funciona exatamente como nas cadeias de caracteres e devolve uma lista nova.

```python
for name in ["Ada", "Linus"]:
    print(name)

total = 0
for n in [3, 1, 4]:
    total += n           # iterate and accumulate
```
