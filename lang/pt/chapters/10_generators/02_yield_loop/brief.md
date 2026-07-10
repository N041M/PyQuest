# 10.2 -- yield dentro de um ciclo

## Conceito

O verdadeiro poder do `yield` aparece quando está **dentro de um ciclo**: uma
linha `yield` executa uma vez por passagem, transmitindo em fluxo uma
sequência transformada inteira -- um valor de cada vez, nunca a lista toda de
uma vez.

```python
def letters(word):
    for ch in word:
        yield ch.upper()
```

`list(letters("hi"))` é `["H", "I"]`. O ciclo percorre a entrada; o `yield`
emite um item transformado de cada vez, pausando entre eles.

## Exemplo

```python
def doubles(nums):
    for x in nums:
        yield x * 2
```

`list(doubles([1, 5, 9]))` é `[2, 10, 18]`.

## A tua tarefa

Define um gerador `squares(n)` que **produz** os quadrados dos números
inteiros de `0` até (mas sem incluir) `n`: `0, 1, 4, 9, ...`. Se `n` for `0`
(ou menos), não produz nada.

## Está feito quando

- `list(squares(4))` é `[0, 1, 4, 9]`.
- `list(squares(1))` é `[0]`; `list(squares(0))` é `[]`.
- Usas `yield` dentro de um ciclo -- não uma lista devolvida nem uma
  compreensão.
