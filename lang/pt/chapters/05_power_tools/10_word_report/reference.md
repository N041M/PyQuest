Um **relatório de frequência de palavras** compõe as ferramentas do capítulo num pequeno pipeline:

1. **`split()`** o texto numa lista de palavras;
2. **conta**-as num dicionário de `palavra -> contagem` com `counts.get(w, 0) + 1`;
3. **`sorted`** os `dict.items()` para ordenar o relatório — por palavra, ou por contagem
   com `key=lambda kv: kv[1]` (e `reverse=True` para a mais frequente primeiro).

Cada passo é uma ferramenta que já conheces; a competência está em ver que uma tarefa real é a sua
composição.

```python
counts = {}
for w in text.split():
    counts[w] = counts.get(w, 0) + 1
for word, n in sorted(counts.items(), key=lambda kv: kv[1], reverse=True):
    print(word, n)        # most frequent first
```
