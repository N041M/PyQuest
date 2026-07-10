O padrão **acumulador** constrói um resultado ao longo de um ciclo. Inicializas uma
variável **antes** do ciclo, depois atualizas-a em **cada** passagem; depois do ciclo,
ela contém o resultado combinado.

- Para uma soma, começa o total em `0` e soma cada valor (`total = total + x`, ou
  `total += x`). Começar em `0` é o elemento neutro da `+`, pelo que um ciclo vazio
  o deixa em `0`.
- A mesma forma conta (começar em 0, `+= 1` por correspondência), constrói uma
  string (começar em `""`, `+=`), ou reúne uma lista (começar em `[]`, `.append`).
- O acumulador tem de viver **fora** do ciclo — declará-lo dentro reiniciá-lo-ia a
  cada passagem.

```python
total = 0
for n in [3, 1, 4]:
    total += n            # 3, then 4, then 8
print(total)             # 8
```
