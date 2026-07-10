# 3.9 -- for e range

## Conceito

Um **ciclo `for`** executa o seu bloco uma vez para cada item de uma sequência.
Combinado com o **`range`**, é a forma habitual de repetir algo um número fixo de
vezes.

`range(n)` produz os números `0, 1, 2, ..., n-1` (para *antes* de `n`):

```python
for i in range(4):
    print(i)
# prints 0, 1, 2, 3
```

Em cada volta, a variável do ciclo (`i` aqui) assume o valor seguinte. Não geres
tu próprio um contador -- o `range` faz isso por ti, pelo que não há risco de
ciclo sem fim.

O `range` também pode receber um início e um passo: `range(1, 5)` é `1,2,3,4`;
`range(0, 10, 2)` é `0,2,4,6,8`.

## Exemplo

```python
for i in range(3):
    print(i)
# prints 0, 1, 2
```

## A tua tarefa

Lê um número inteiro `n` e depois imprime todos os números de `0` até `n-1`, cada
um na sua própria linha, usando um ciclo `for` com `range`.

Para a entrada `4` a saída é:

```
0
1
2
3
```

## Está feito quando

- `4` imprime `0,1,2,3` (cada um numa linha). `1` imprime apenas `0`.
- `0` não imprime nada.
