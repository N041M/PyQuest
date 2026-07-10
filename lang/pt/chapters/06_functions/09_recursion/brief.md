# 6.9 -- Recursão: uma função a chamar-se a si própria

## Conceito

Uma função pode chamar-se **a si própria**. Isso chama-se **recursão**, e funciona
sempre que um problema contém uma cópia mais pequena do mesmo problema.

O fatorial é o clássico: `5!` significa `5 * 4 * 3 * 2 * 1`. Mas olha outra vez:

> `5!` é apenas `5 * 4!` -- e `4!` é `4 * 3!` ...

Uma função recursiva afirma exatamente isso, mais um **caso base** -- a entrada
mais pequena respondida diretamente, sem mais chamadas:

```python
def fact(n):
    if n == 0:
        return 1            # base case: 0! is 1
    return n * fact(n - 1)  # the smaller copy of the same problem
```

`fact(3)` corre como `3 * fact(2)` -> `3 * 2 * fact(1)` -> `3 * 2 * 1 * fact(0)`
-> `3 * 2 * 1 * 1` = `6`. Sem o caso base as chamadas nunca parariam --
a versão da recursão de um ciclo sem fim.

Podias calcular um fatorial com um ciclo `for` -- mas a *lição* aqui é a
auto-chamada, por isso este puzzle exige-a.

## Exemplo

```python
fact(0)    # 1
fact(3)    # 6
fact(5)    # 120
```

## A tua tarefa

Define `fact(n)` que devolva `n!` **recursivamente**: um caso base para `0`, e
`n * fact(n - 1)` para o resto. `n` nunca é negativo.

## Está feito quando

- `fact(0)` é `1`, `fact(1)` é `1`, `fact(5)` é `120`.
- `fact` chama-se a si própria -- o verificador procura a auto-chamada, por isso uma versão
  com ciclo não vai passar.
