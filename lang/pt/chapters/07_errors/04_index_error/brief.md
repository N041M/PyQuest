# 7.4 -- IndexError e acesso seguro

## Conceito

Indexar para lá do fim de uma lista levanta `IndexError`:

```python
items = ["a", "b"]
items[5]      # IndexError!
```

Um "safe get" devolve uma alternativa em vez de falhar -- e é mais um sítio
onde *tentar* vence *testar antecipadamente*. Lembra-te de que índices
negativos são **válidos** (2.2): `items[-1]` é o último elemento, `items[-2]`
o anterior a esse. Uma verificação de limites escrita à mão tem de acertar em
`0 <= i`... não, espera, `-len <= i < len`... exatamente, nas duas direções.
Ou simplesmente tentas:

```python
try:
    return items[i]
except IndexError:
    return default
```

O `except` está correto *por definição* -- dispara precisamente quando o
próprio Python diz que o índice é mau, negativos incluídos.

## Exemplo

```python
item_or(["a", "b"], 0, "?")     # "a"
item_or(["a", "b"], -1, "?")    # "b"   -- valid negative index
item_or(["a", "b"], 5, "?")     # "?"   -- out of range, fallback
```

## A tua tarefa

Define `item_or(items, i, default)` que devolve `items[i]`, ou `default`
quando `i` está fora do intervalo -- usando `try`/`except IndexError`.

## Está feito quando

- `item_or(["a", "b"], 1, "?")` é `"b"`; o índice `5` dá `"?"`.
- `item_or(["a", "b"], -1, "?")` é `"b"` -- negativos que cabem são válidos.
- `item_or([], 0, "?")` é `"?"` -- uma lista vazia não tem nenhum índice
  válido.
- Usaste `try`/`except` -- aritmética de limites foge à lição e falha.
