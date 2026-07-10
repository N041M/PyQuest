# 10.5 -- filtrar enquanto produzes

## Conceito

Um gerador não tem de produzir a cada passagem. Coloca o `yield` atrás de um
`if`, e **filtras** o fluxo à medida que corre -- saltando os itens que não
queres, emitindo apenas os que queres.

```python
def shouts(words):
    for w in words:
        if w.isupper():
            yield w          # only the all-caps words come out
```

`list(shouts(["hi", "STOP", "go", "NOW"]))` é `["STOP", "NOW"]`. O ciclo
visita cada palavra; o `yield` só executa quando o `if` é verdadeiro.

## Exemplo

```python
def positives(nums):
    for n in nums:
        if n > 0:
            yield n
```

`list(positives([-1, 4, 0, 2]))` é `[4, 2]`.

## A tua tarefa

Define um gerador `evens(nums)` que produz apenas os números **pares** de
`nums`, mantendo a sua ordem original. (Um número é par quando
`n % 2 == 0`.) Se nenhum for par, não produz nada.

## Está feito quando

- `list(evens([1, 2, 3, 4]))` é `[2, 4]`.
- `list(evens([1, 3, 5]))` é `[]`; `list(evens([]))` é `[]`.
- Usas `yield` atrás de um `if` -- não uma lista devolvida nem uma
  compreensão.
