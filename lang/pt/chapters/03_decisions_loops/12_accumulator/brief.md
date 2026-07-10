# 3.12 -- O padrão acumulador

## Conceito

Um padrão de ciclo muito comum: manter um **total corrente** numa variável, começá-la
em `0`, e somar-lhe algo em cada passagem. A variável "acumula" o resultado.

```python
total = 0
for n in [4, 2, 9]:
    total = total + n
print(total)        # 15
```

Os passos-chave são: **começar em 0 antes do ciclo**, **somar dentro do ciclo**,
**usar o resultado depois do ciclo**. A mesma forma serve para contar (começar em 0,
somar 1 de cada vez) ou construir uma string (começar em "", somar um pedaço de
cada vez).

Este puzzle combina o que já aprendeste: um ciclo `for`, `range`, ler entrada, e
um acumulador.

## Exemplo

```python
total = 0
for _ in range(3):
    total = total + int(input())
print(total)
```

(`_` é um nome de variável comum, usado quando não precisas do valor do ciclo.)

## A tua tarefa

Lê um número inteiro `n` (uma contagem). Depois lê mais `n` números inteiros, um
por linha, e imprime a sua **soma**.

Para a entrada `3`, seguida de `10`, `20`, `5`, a saída é:

```
35
```

## Está feito quando

- Contagem `3` com `10, 20, 5` imprime `35`.
- Uma contagem de `0` não lê mais nenhum número e imprime `0`.
- Os números podem ser negativos.
