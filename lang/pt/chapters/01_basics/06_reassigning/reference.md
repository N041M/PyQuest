Uma variável é um nome, não uma caixa: atribuir de novo **reassocia** o nome a um novo
valor. O nome guarda sempre a sua atribuição mais recente; o valor anterior
simplesmente deixa de ser alcançável através dele.

- Cada `=` substitui aquilo para onde o nome aponta. A ordem importa — as atribuições
  posteriores prevalecem.
- O lado direito é avaliado usando o valor *atual* do nome, e só depois o
  resultado é reassociado, por isso `x = x + 1` lê o `x` antigo e guarda o novo.
- As formas aumentadas (`x += 1`, `x *= 2`, …) são abreviaturas exatamente para isso:
  ler, combinar, reassociar.

```python
score = 10
score = 25        # score is now 25
score = score + 5 # reads 25, stores 30
```
