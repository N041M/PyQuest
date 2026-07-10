**`min(items)`** e **`max(items)`** devolvem o item mais pequeno e o maior de uma
coleção não vazia.

- Comparam com `<`/`>`, por isso funcionam com números e com cadeias de caracteres (que
  se comparam lexicograficamente).
- Chamados sobre um iterável **vazio** levantam `ValueError`; passa `default=` para
  fornecer um valor alternativo.
- Uma função `key=` ordena por um valor derivado em vez do próprio item:
  `max(words, key=len)` devolve a palavra **mais comprida**.

```python
min([3, 1, 4])             # 1
max("apple", "pear")       # 'pear'
max(words, key=len)        # the longest word
```
