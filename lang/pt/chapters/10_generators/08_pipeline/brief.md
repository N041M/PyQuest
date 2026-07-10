# 10.8 -- Peça de resistência: um pipeline em fluxo

## Conceito

Nada de novo -- esta peça de resistência é o capítulo em miniatura. A razão
real por que os geradores importam é que **se compõem**: a saída de um
gerador é a entrada de outro, por isso os dados fluem através de um
**pipeline**, um item de cada vez, sem nunca construir a lista completa
pelo meio.

Uma etapa de pipeline é apenas um gerador que percorre `stream` (qualquer
iterável -- uma lista, ou *outro gerador*) e vai produzindo à medida que
avança:

```python
def only_long(stream):
    for word in stream:
        if len(word) >= 4:
            yield word
```

Vais construir uma fonte, um filtro e uma etapa de reetiquetagem, depois
ligá-las entre si.

## Exemplo

```python
numbers(4)                              # yields 0, 1, 2, 3
keep_even(numbers(4))                   # yields 0, 2
labelled(keep_even(numbers(4)))         # yields "#0", "#2"
```

## A tua tarefa

Define **três** geradores:

- `numbers(n)` -- produz `0, 1, ..., n-1` (a fonte). `n <= 0` não produz
  nada.
- `keep_even(stream)` -- produz apenas os números pares de `stream`
  (qualquer iterável).
- `labelled(stream)` -- produz a cadeia de caracteres `"#x"` para cada `x`
  em `stream` (por exemplo, `7` torna-se `"#7"`).

Cada um tem de usar `yield`. `keep_even` e `labelled` têm de funcionar em
**qualquer** stream, incluindo a saída de outro gerador, para que se
componham.

## Está feito quando

- `list(numbers(4))` é `[0, 1, 2, 3]`; `list(numbers(0))` é `[]`.
- `list(keep_even([1, 2, 3, 4]))` é `[2, 4]`.
- `list(labelled([0, 2]))` é `["#0", "#2"]`.
- `list(labelled(keep_even(numbers(6))))` é `["#0", "#2", "#4"]`.
- Os três usam `yield`, e as etapas de filtro/reetiquetagem aceitam
  qualquer iterável.
