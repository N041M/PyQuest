# 5.8 -- Filtrar com compreensões

## Conceito

Uma compreensão também pode **escolher** que itens manter. Acrescenta um `if` no
final:

```python
evens = [x for x in nums if x % 2 == 0]
```

Lê-a: *"cada `x` de `nums` -- mas só se `x % 2 == 0`"*. Os itens que falham
o teste são simplesmente deixados de fora.

As duas partes são independentes e combinam-se livremente:

```python
[x * 2 for x in nums]                 # transform every item   (5.7)
[x for x in nums if x > 0]            # keep some, unchanged   (this puzzle)
[x * 2 for x in nums if x > 0]        # keep some AND transform
```

Lembrete de 1.9: `x % 2` é o resto da divisão por 2, por isso é `0`
exatamente para números pares -- e isso inclui o próprio `0` e negativos como
`-4`.

## Exemplo

```python
nums = [1, 2, 3, 4]
print([x for x in nums if x % 2 == 0])    # [2, 4]
```

## A tua tarefa

Lê uma contagem `n`, depois `n` números inteiros. Mantém apenas os **pares** (na
sua ordem original) e imprime-os um por linha.

Para a entrada `5`, depois `1`, `2`, `3`, `4`, `-6`:

```
2
4
-6
```

## Está feito quando

- `1, 2, 3, 4, -6` imprime `2, 4, -6` -- negativos e zero contam como pares.
- Se nenhum número for par, nada é impresso.
- Usaste uma compreensão com uma cláusula `if`.
