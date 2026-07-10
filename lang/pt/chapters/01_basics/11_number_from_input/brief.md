# 1.11 -- Um número a partir da entrada

## Conceito

`input()` devolve sempre **texto**, mesmo quando a pessoa escreve dígitos. Se tentares
fazer contas com isso, `+` vai juntar em vez de somar -- lembra-te do puzzle 1.7:

```python
n = input()      # user types 21  ->  n is the string "21"
print(n + n)     # "2121", not 42
```

Para fazer aritmética, primeiro **converte** o texto num número com `int(...)`:

```python
n = int(input())   # "21" -> 21, a real number now
print(n * 2)       # 42
```

`int(...)` pega em texto que se parece com um número inteiro e transforma-o num `int`
com que podes calcular. Este padrão -- `int(input())` -- é extremamente comum.

## Erro comum

`int` não se limita a "remover as aspas"; produz um tipo diferente. Depois de
`int(input())` o valor é um número, por isso `+`, `*`, `//` e companhia fazem contas a sério.

## A tua tarefa

Lê um número inteiro da entrada, depois imprime-o **duplicado**. Exemplos:

- entrada `21` -> resultado `42`
- entrada `0`  -> resultado `0`
- entrada `-5` -> resultado `-10`

Portanto: lê com `input()`, converte com `int(...)`, multiplica por 2, imprime o resultado.

## Está feito quando

- Para a entrada `21` o resultado é `42`.
- Também funciona para `0` e para um número negativo como `-5` (o verificador testa
  estes casos).
