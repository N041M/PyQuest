# 3.7 -- while

## Conceito

Um **ciclo `while`** repete um bloco **enquanto** uma condição se mantiver `True`. Ele
verifica a condição, executa o bloco, e verifica outra vez -- sucessivamente:

```python
count = 1
while count <= 3:
    print(count)
    count = count + 1   # move toward making the condition False
# prints 1, 2, 3
```

A linha `count = count + 1` é essencial: altera `count` para que a condição
acabe por se tornar `False`. Sem ela, o ciclo nunca para.

## Erro comum -- o ciclo sem fim

Se a condição nunca se tornar `False`, o ciclo executa-se para sempre. Certifica-te
sempre de que algo dentro do ciclo se aproxima do ponto de paragem. (Se o teu
programa parecer bloqueado, geralmente é um ciclo sem fim.)

## Exemplo

```python
n = 4
i = 1
while i <= n:
    print(i)
    i = i + 1
# prints 1, 2, 3, 4
```

## A tua tarefa

Lê um número inteiro `n` e depois imprime todos os números de `1` até `n`, cada um na
sua própria linha, usando um ciclo `while`.

Para a entrada `3` a saída é:

```
1
2
3
```

## Está feito quando

- `3` imprime `1`, `2`, `3`. `1` imprime apenas `1`.
- `0` (ou um número negativo) não imprime nada -- o corpo do ciclo nunca é executado.
