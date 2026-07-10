Indexar para lá do fim de uma lista (ou string) levanta **`IndexError`**.
Apanhá-lo transforma uma pesquisa arriscada num **acesso seguro** que
devolve uma alternativa quando a posição não existe.

- `lst[i]` levanta uma exceção se `i >= len(lst)` (ou `i < -len(lst)`); o
  `except` fornece uma alternativa em vez de deixar cair o programa.
- Este é o contraponto EAFP de verificar primeiro `if i < len(lst):` —
  útil quando o caso fora do intervalo é normal e não um bug.

```python
def get(lst, i, default=None):
    try:
        return lst[i]
    except IndexError:
        return default   # position absent -> fallback
```
