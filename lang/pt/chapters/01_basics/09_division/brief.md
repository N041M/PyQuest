# 1.9 -- Três tipos de divisão

## Conceito

Dividir tem três operadores úteis em Python:

- `/`  divisão normal -- dá sempre um número decimal (o Python chama-lhes
  `float`). `7 / 2` é `3.5`.
- `//` divisão inteira -- divide e descarta a parte fracionária, dando um
  número inteiro. `7 // 2` é `3`.
- `%`  módulo -- dá o **resto** depois da divisão. `7 % 2` é `1`
  (porque o 2 cabe três vezes no 7, sobrando 1).

```python
print(7 / 2)    # 3.5
print(7 // 2)   # 3
print(7 % 2)    # 1
```

Um número com um ponto decimal, como `3.5`, é um `float`. Um número inteiro sem
ponto, como `3`, é um `int`. Repara que `/` dá `3.5` mesmo quando divide
números que parecem dar um resultado exato: `4 / 2` é `2.0`, não `2`.

`%` é surpreendentemente útil: um número é par exatamente quando `n % 2` é `0`.

## Erro comum

`/` não arredonda para um número inteiro. `7 / 2` é `3.5`, nunca `3`. Se quiseres a
parte inteira, é para isso que serve o `//`.

## A tua tarefa

Usando os números 7 e 2, imprime estas três linhas por ordem:

```
3.5
3
1
```

Usa `/` para a primeira, `//` para a segunda, e `%` para a terceira.

## Está feito quando

- O resultado é exatamente `3.5`, depois `3`, depois `1`.
- Cada linha usa o operador correspondente (`/`, `//`, `%`).
