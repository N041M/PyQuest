**`sorted(items)`** devolve uma **nova** lista com os itens em ordem crescente,
deixando o original intacto.

- Aceita qualquer iterável e devolve sempre uma lista. Números ordenam-se numericamente,
  cadeias de caracteres lexicograficamente.
- **`reverse=True`** ordena de forma decrescente. **`key=`** ordena por um valor derivado:
  `sorted(words, key=len)` ordena por comprimento, `sorted(d.items(), key=lambda kv:
  kv[1])` ordena os pares do dicionário pelo valor.
- O método de lista `lst.sort()` ordena **no próprio local** e devolve `None`; usa
  `sorted` quando queres uma lista nova ou estás a ordenar algo que não é uma lista.

```python
sorted([3, 1, 2])               # [1, 2, 3]
sorted([3, 1, 2], reverse=True) # [3, 2, 1]
sorted(words, key=len)          # shortest to longest
```
