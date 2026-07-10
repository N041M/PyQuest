# 11.5 -- Counter: contagem num só passo

## Conceito

Lá no capítulo 5 fizeste a contagem à mão: `counts[k] = counts.get(k, 0) + 1`. O
módulo **`collections`** traz esse padrão, já escrito e testado, como
**`Counter`**:

```python
from collections import Counter

Counter("banana")     # Counter({'a': 3, 'n': 2, 'b': 1})
```

- `Counter(items)` percorre qualquer iterável e devolve uma contagem de cada
  item distinto.
- Um `Counter` **é** um dict (é uma subclasse), por isso `counts[x]` e
  `for k, v in counts.items()` funcionam exatamente como esperarias -- e é
  igual, na comparação, a um dict simples com as mesmas contagens.
- Até trata da chave em falta: `counts["zzz"]` é `0`, e não um `KeyError`.

É essa a promessa da biblioteca padrão: o ciclo que escreverias já é uma
ferramenta.

## Exemplo

```python
from collections import Counter

def letter_counts(word):
    return Counter(word)
```

## A tua tarefa

Usando **`Counter`** de `collections`, define `tally(items)` que devolve
uma contagem de quantas vezes cada item aparece na lista `items`.

## Está feito quando

- `tally(["a", "b", "a"])` é igual a `{"a": 2, "b": 1}`.
- `tally([])` é igual a `{}`.
- A contagem é feita pelo `Counter`, não por um ciclo escrito à mão.
