# 3.8 -- Repetir até uma sentinela

## Conceito

Um ciclo não precisa de contar. Pode continuar até o utilizador introduzir um valor
especial, a **sentinela**, que significa "parar". O truque é ler uma vez *antes*
do ciclo, e voltar a ler *no fim* de cada passagem:

```python
line = input()
while line != "quit":
    print("you said:", line)
    line = input()        # read the next one
print("done")
```

O ciclo continua a executar-se enquanto a entrada não for a sentinela (`"quit"`
neste caso). Assim que a sentinela chega, a condição é falsa e o ciclo termina.

## Exemplo

Lê números e soma-os até ser introduzido um `0`:

```python
total = 0
n = int(input())
while n != 0:
    total = total + n
    n = int(input())
print(total)
```

## A tua tarefa

Lê números inteiros, um por linha, e soma-os. Para quando o número `0` for
introduzido (não somes o `0`). Depois imprime o total.

Para a entrada `4`, `5`, `0` a saída é:

```
9
```

## Está feito quando

- `4`, `5`, `0` imprime `9`; um único `0` imprime `0`.
- O próprio `0` não é somado; os números podem ser negativos.
