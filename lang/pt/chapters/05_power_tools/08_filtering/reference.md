Acrescentar um **`if`** a uma compreensão mantém apenas os itens que passam o teste.
`[x for x in items if test]` reúne cada `x` para o qual `test` é verdadeiro,
**ignorando** os restantes.

- A cláusula `if` filtra; a expressão inicial continua a transformar, por isso as duas
  combinam-se: `[n * n for n in nums if n % 2 == 0]` eleva ao quadrado apenas os pares.
- Substitui o padrão ciclo-com-`if`-e-`append`.
- Não a confundas com uma **expressão condicional** na posição do valor
  (`[a if cond else b for x in items]`), que escolhe por item em vez de
  filtrar.

```python
[n for n in range(10) if n % 2 == 0]   # [0, 2, 4, 6, 8]
[w for w in words if len(w) > 3]       # only long words
```
